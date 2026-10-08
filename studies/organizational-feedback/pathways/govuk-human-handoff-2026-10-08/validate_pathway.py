"""Check chronology and evidence scope; this does not validate source truth."""
import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def validate(sources, pathway):
    errors = []
    def require(ok, msg):
        if not ok:
            errors.append(msg)
    sids = [s['source_id'] for s in sources]
    require(len(sids) == len(set(sids)), 'duplicate source ID')
    smap = {s['source_id']: s for s in sources}
    claims = pathway['claims']
    cids = [c['claim_id'] for c in claims]
    require(len(cids) == len(set(cids)), 'duplicate claim ID')
    cmap = {c['claim_id']: c for c in claims}
    cutoff = date.fromisoformat(pathway['search_cutoff'])
    for s in sources:
        require(s['url'].startswith('https://'), f"{s['source_id']}: missing official URL")
        require(len(s['snapshot_sha256']) == 64, f"{s['source_id']}: missing snapshot hash")
        require(bool(s['reading_scope']), f"{s['source_id']}: missing reading scope")
    for c in claims:
        require(c['source_id'] in smap, f"{c['claim_id']}: unknown source")
        require(bool(c['locator']), f"{c['claim_id']}: missing locator")
        if c['statement_date']:
            sd = date.fromisoformat(c['statement_date'])
            require(sd <= cutoff, f"{c['claim_id']}: statement after cutoff")
            src = smap.get(c['source_id'], {})
            pd = src.get('publication_date')
            if pd:
                require(date.fromisoformat(pd) <= sd, f"{c['claim_id']}: statement precedes publication")
            if c['evidence_kind'] == 'exploration_reply':
                require(any(a['date'] == c['statement_date'] and a['kind'] == 'official_public_reply' for a in src.get('dated_addenda', [])), 'dated reply lacks matching source addendum')
        else:
            require(bool(c.get('date_note')), f"{c['claim_id']}: unknown date without explanation")
    seen_dates = []
    for event in pathway['timeline']:
        day = date.fromisoformat(event['record_date'])
        seen_dates.append(day)
        require(day <= cutoff, 'timeline event after search cutoff')
        for cid in event['claim_ids']:
            require(cid in cmap, 'timeline unknown claim')
            if cid in cmap:
                require(cmap[cid]['statement_date'] == event['record_date'], 'timeline must use the statement/reply date, not an inferred release date')
    require(seen_dates == sorted(seen_dates), 'timeline out of date order')
    for field, value in pathway.items():
        if isinstance(value, dict) and 'basis' in value:
            require(set(value['basis']) <= set(cids), f'{field}: unknown basis claim')
    rules = {
        'implementation': ('not_established_in_reviewed_sources', 'feature_implementation', 'feature_specific'),
        'later_assessment': ('no_handoff_linked_assessment_established', 'feature_assessment', 'feature_specific'),
        'change_authorization': ('not_reported', 'feature_approval', 'feature_specific'),
        'authority_to_revise_goal': ('not_reported', 'goal_change_authority', 'feature_specific'),
        'feedback_to_original_pilot_users': ('not_reported', 'original_reporter_feedback', 'original_pilot_users'),
        'goal_or_metric_revision': ('not_reported', 'goal_revision', 'feature_specific'),
        'individual_judgment_or_learning': ('not_measured', 'human_outcome_measure', 'feature_specific')
    }
    for field, (unknown, kind, scope) in rules.items():
        value = pathway[field]
        if value['status'] == unknown:
            require(not value['basis'], f'{field}: unknown status with evidence basis')
        elif value['status'] == 'reported':
            require(bool(value['basis']), f'{field}: positive claim without evidence')
            for cid in value['basis']:
                c = cmap.get(cid, {})
                require(c.get('evidence_kind') == kind and c.get('evidence_scope') == scope, f'{field}: evidence kind/scope cannot support this upgrade')
        else:
            require(False, f'{field}: unrecognized status')
    require(pathway['candidate_followup_measures']['status'] == 'analyst_proposals_not_reported_as_used', 'proposed measures presented as observed')
    require(pathway['source_count'] == len(sources), 'source count mismatch')
    require(pathway['baseline_episode_id'] == 'E02', 'unexpected pilot lineage')
    if errors:
        raise ValueError('\n'.join(errors))
    return {'status':'structural_checks_passed','source_count':len(sources),'claim_count':len(claims),'timeline_statement_count':len(pathway['timeline']),'linked_pathway_count':1,'additional_independent_organizations':0,'implementation':'not_established_in_reviewed_sources','change_linked_assessment':'not_established_in_reviewed_sources','human_review':'pending','meaning':'Reference, date and scope checks only; no effect, source-truth or independent-review validation.'}


def main():
    result = validate(json.loads((ROOT/'SOURCE_VERSIONS.json').read_text()), json.loads((ROOT/'pathway.json').read_text()))
    (ROOT/'checks.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()

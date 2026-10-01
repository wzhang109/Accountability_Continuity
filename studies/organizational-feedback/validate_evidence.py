"""Validate source-linked records; counts describe this document set, not institutions."""
import hashlib
import json
from collections import Counter
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent
STATUSES = {'implemented_reported', 'planned_reported', 'local_adjustment_reported',
            'requested_only', 'declined_with_reason_reported', 'not_reported'}
KINDS = {'reported_change_episode', 'reported_plan', 'aggregate_user_account'}


def validate(sources, episodes):
    errors = []
    def require(condition, message):
        if not condition:
            errors.append(message)
    sids = [s['source_id'] for s in sources]
    eids = [e['episode_id'] for e in episodes]
    require(len(sids) == len(set(sids)), 'Duplicate source ID')
    require(len(eids) == len(set(eids)), 'Duplicate episode ID')
    source_map = {s['source_id']: s for s in sources}
    for s in sources:
        require(s['url'].startswith('https://'), f"{s['source_id']}: missing public URL")
        require(len(s['html_sha256']) == 64, f"{s['source_id']}: missing retrieval hash")
        require(bool(s['reading_scope']), f"{s['source_id']}: missing reading scope")
        require(len(s['locator_excerpt'].split()) <= 25, f"{s['source_id']}: excerpt too long")
        date.fromisoformat(s['publication_date'])
    for e in episodes:
        eid = e['episode_id']
        require(e['action_status'] in STATUSES, f'{eid}: invalid action status')
        require(e['record_kind'] in KINDS, f'{eid}: invalid record kind')
        require(bool(e['interpretation']), f'{eid}: missing interpretation limits')
        require(bool(e['claims']), f'{eid}: no sourced claims')
        claim_ids = {c['claim_id'] for c in e['claims']}
        for c in e['claims']:
            require(c['source_id'] in source_map, f'{eid}: unknown source')
            require(bool(c['locator']), f'{eid}: missing passage locator')
            if c['source_id'] in source_map:
                require(date.fromisoformat(source_map[c['source_id']]['publication_date']) <= date.fromisoformat(e['report_cutoff']), f'{eid}: evidence postdates cutoff')
        require(set(e['implementation_basis']) <= claim_ids, f'{eid}: unknown implementation claim')
        require(set(e['evaluation_basis']) <= claim_ids, f'{eid}: unknown evaluation claim')
        if e['action_status'] in {'implemented_reported', 'local_adjustment_reported'}:
            require(bool(e['implementation_basis']), f'{eid}: implementation without evidence')
        else:
            require(not e['implementation_basis'], f'{eid}: unimplemented status has implementation evidence')
        if e['action_status'] == 'local_adjustment_reported':
            require(e['action_scope'] == 'local_output', f'{eid}: local adjustment promoted to shared change')
        if e['record_kind'] == 'reported_plan':
            require(e['action_status'] == 'planned_reported', f'{eid}: plan treated as completed')
        if e['evaluation_status'] == 'no_episode_linked_assessment_established':
            require(not e['evaluation_basis'], f'{eid}: inconsistent evaluation evidence')
        else:
            require(bool(e['evaluation_basis']), f'{eid}: evaluation without evidence')
    if errors:
        raise ValueError('\n'.join(errors))


def main():
    sources = json.loads((ROOT/'sources.json').read_text())
    episodes = json.loads((ROOT/'episodes.json').read_text())
    validate(sources, episodes)
    counts = lambda key: dict(sorted(Counter(e[key] for e in episodes).items()))
    result = {
        'status': 'structural_checks_passed',
        'dataset_date': '2026-10-01',
        'source_count': len(sources), 'episode_count': len(episodes),
        'program_count': len({e['program_id'] for e in episodes}),
        'episodes_by_program': counts('program_id'),
        'action_status_counts': counts('action_status'),
        'evaluation_status_counts': counts('evaluation_status'),
        'authorization_evidence_counts': counts('authorization'),
        'reporter_feedback_evidence_counts': counts('reporter_feedback'),
        'input_sha256': {f: hashlib.sha256((ROOT/f).read_bytes()).hexdigest() for f in ['sources.json','episodes.json']},
        'interpretation': 'Counts of coded public records only. Unknown links are not absent practices. Episodes are clustered within programs. No effect, prevalence, AC score, or independent coding reliability is estimated.'
    }
    (ROOT/'evidence_summary.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()

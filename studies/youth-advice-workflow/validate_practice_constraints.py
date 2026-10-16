"""Logical and display checks for fictional constraints, not human validation."""
import json
from collections import Counter
from copy import deepcopy
from pathlib import Path
from materials import load_items, load_baseline_items, visible_trial, score_response

HERE = Path(__file__).resolve().parent


def eligible_winner(record):
    req = record['requirements']
    eligible = [p for p in record['plans']
                if p['cost'] <= req['budget_max'] and p['seats'] >= req['seats_min']]
    if not eligible:
        raise ValueError('No eligible plan; a separate decision rule is needed')
    best = max(p['seats'] for p in eligible)
    winners = [p['name'] for p in eligible if p['seats'] == best]
    if len(winners) != 1:
        if req.get('tie_break') != 'Lower cost when seat counts tie':
            raise ValueError('Tied winners require a clarified claim or tie rule')
        tied = [p for p in eligible if p['name'] in winners]
        least = min(p['cost'] for p in tied)
        winners = [p['name'] for p in tied if p['cost'] == least]
        if len(winners) != 1:
            raise ValueError('Unresolved equal-seat equal-cost tie')
    return winners[0]


def constraint_summary(item):
    """Check representative outcome classes under the stated integer domain.

    Enumerating costs through budget_max covers eligibility and any stated
    lower-cost tie rule; one value above budget represents all excluded costs.
    Seats affect eligibility at seats_min and comparisons with recorded seats.
    One value above the largest seat threshold represents the unbounded class.
    This is a supplied-rule check, not a model of a learner's understanding.
    """
    record = item['record']; basis = item['answer_basis']
    missing = [(p['name'], k) for p in record['plans']
               for k in ['cost', 'seats'] if p[k] is None]
    for p in record['plans']:
        for k in ['cost', 'seats']:
            value = p[k]
            if value is not None and (type(value) is not int or value < 0):
                raise ValueError('Recorded values must be non-negative integers')
    if len(missing) > 1:
        raise ValueError('Multiple unknowns need a separately reviewed check')
    if not missing:
        winner = eligible_winner(record)
        supported = winner == basis['claimed_choice']
        return {'computed_key': 'Supported' if supported else 'Contradicted',
                'compatible_winners': [winner], 'representative_count': 1,
                'missing_field': None, 'truth_values': [supported]}
    if basis.get('missing_domain') != 'non-negative integers':
        raise ValueError('Unknown-value domain must be stated')
    plan, field = missing[0]
    if (plan, field) != (basis['missing_plan'], basis['missing_field']):
        raise ValueError('Missing field does not match the supplied record')
    if field == 'cost':
        upper = record['requirements']['budget_max'] + 1
    else:
        upper = max([record['requirements']['seats_min']] +
                    [p['seats'] for p in record['plans'] if p['seats'] is not None]) + 1
    winners = set(); truths = set()
    for value in range(upper + 1):
        completed = deepcopy(record)
        next(p for p in completed['plans'] if p['name'] == plan)[field] = value
        winner = eligible_winner(completed)
        winners.add(winner); truths.add(winner == basis['claimed_choice'])
    key = ('Not enough information' if len(truths) > 1 else
           'Supported' if truths == {True} else 'Contradicted')
    return {'computed_key': key, 'compatible_winners': sorted(winners),
            'representative_count': upper + 1, 'representative_range': [0, upper],
            'missing_field': field, 'truth_values': sorted(truths)}


def run_checks():
    checks = []
    def check(name, condition):
        if not condition:
            raise AssertionError(name)
        checks.append(name)
    def rejects(name, action):
        try:
            action()
        except ValueError:
            checks.append(name); return
        raise AssertionError(name)

    bank = {i['item_id']: i for i in load_items()}
    spec = json.loads((HERE / 'practice_constraints_set.json').read_text())
    plan = json.loads((HERE / 'plan.json').read_text())
    items = [bank[k] for k in spec['item_ids']]
    check('Five distinct practice constraint references', len(set(spec['item_ids'])) == 5 and all(i['parallel_family'] == 'constraints' and i['illustrative_phase'] == 'practice' for i in items))
    check('Recorded family key counts, not balanced forms', Counter(i['answer_key'] for i in items) == spec['answer_category_counts'])
    check('Planned counts unchanged', [p['count'] for p in plan['phases']] == [6, 12, 8, 4])
    check('No frozen advice allocation fabricated', spec['frozen_advice_lists'] is None)
    check('Twenty draft slots, ten missing', len(bank) + len(load_baseline_items()) == 20 and sum(p['count'] for p in plan['phases']) - 20 == 10)
    summaries = {}; lengths = []
    for item in items:
        ident = item['item_id']; summary = constraint_summary(item)
        summaries[ident] = summary
        check(ident + ' key follows compatible outcome classes', summary['computed_key'] == item['answer_key'])
        check(ident + ' independent review pending', item['independent_review'] == 'pending')
        check(ident + ' advice quality keyed separately', item['advice_variants']['correct']['recommendation'] == item['answer_key'] and item['advice_variants']['misleading']['recommendation'] != item['answer_key'])
        lengths.append({'item_id': ident, **{k: len(v['reason'].split()) for k, v in item['advice_variants'].items()}})
        for quality in ['correct', 'misleading']:
            first = visible_trial(item, 'judgment_first', 'practice', 'first', quality)
            review = visible_trial(item, 'judgment_first', 'practice', 'review', quality, first_response_recorded=True)
            early = visible_trial(item, 'advice_first', 'practice', 'first', quality)
            check(ident + ' first independent view has no key or advice', set(first) == {'item_id', 'title', 'fictional', 'record', 'claim', 'choices'})
            check(ident + ' assisted groups receive identical frozen wording', review['advice'] == early['advice'] == item['advice_variants'][quality])
            for arm in ['judgment_first', 'advice_first']:
                rejects(ident + ' feedback withheld before final response', lambda: visible_trial(item, arm, 'practice', 'feedback', quality))
                check(ident + ' common assisted feedback', visible_trial(item, arm, 'practice', 'feedback', quality, final_response_recorded=True)['feedback'] == item['shared_feedback'])
        no_ai = visible_trial(item, 'no_ai', 'practice', 'first')
        check(ident + ' no-AI view has no advice or key', set(no_ai) == {'item_id', 'title', 'fictional', 'record', 'claim', 'choices'})
        check(ident + ' no-AI same feedback', visible_trial(item, 'no_ai', 'practice', 'feedback', final_response_recorded=True)['feedback'] == item['shared_feedback'])
        rejects(ident + ' no-AI no quality label', lambda: visible_trial(item, 'no_ai', 'practice', 'first', 'correct'))
        check(ident + ' scoring follows supplied draft key', score_response(item, item['answer_key'])['final_correct'] == 1)
        check(ident + ' skipped remains missing', score_response(item, None, response_status='skipped')['final_correct'] is None)
        if ident in {'Y11', 'Y12', 'Y13', 'Y14'}:
            check(ident + ' practice-only assignment', item['allowed_phases'] == ['practice'])
            for arm in plan['arms']:
                for phase in ['baseline', 'delayed_unaided', 'challenge']:
                    rejects(ident + ' rejects reuse in ' + arm + ' ' + phase, lambda: visible_trial(item, arm, phase, 'first'))

    y11 = bank['Y11']; y12 = bank['Y12']
    check('Both new records have one unknown but different keys', all(sum(p[k] is None for p in i['record']['plans'] for k in ['cost', 'seats']) == 1 for i in [y11, y12]) and y11['answer_key'] != y12['answer_key'])
    b11 = next(p for p in y11['record']['plans'] if p['name'] == 'B')
    check('Y11 invariant budget exclusion explains all unknown seats', b11['cost'] > y11['record']['requirements']['budget_max'] and summaries['Y11']['compatible_winners'] == ['A'])
    for item in [y11, y12, bank['Y13'], bank['Y14']]:
        examples = item['answer_basis'].get('counterexamples', item['answer_basis'].get('examples', []))
        for example in examples:
            record = deepcopy(item['record']); basis = item['answer_basis']
            value = example['missing_value']
            check(item['item_id'] + ' hypothetical value in stated domain', type(value) is int and value >= 0)
            next(p for p in record['plans'] if p['name'] == basis['missing_plan'])[basis['missing_field']] = value
            winner = eligible_winner(record)
            check(item['item_id'] + ' hypothetical winner recomputed', winner == example['eligible_winner'])
            check(item['item_id'] + ' hypothetical truth recomputed', (winner == basis['claimed_choice']) == example['claim_supported'])
    check('Y12 compatible costs allow opposite truth values', set(x['claim_supported'] for x in y12['answer_basis']['counterexamples']) == {True, False})
    y13 = bank['Y13']; y14 = bank['Y14']
    check('Missing seats include both invariant and variable conclusions', summaries['Y11']['computed_key'] == 'Supported' and summaries['Y13']['computed_key'] == 'Not enough information')
    check('Missing costs include both invariant and variable conclusions', summaries['Y12']['computed_key'] == 'Not enough information' and summaries['Y14']['computed_key'] == 'Supported')
    check('Y14 seat exclusion explains all unknown costs', next(p for p in y14['record']['plans'] if p['name'] == 'C')['seats'] < y14['record']['requirements']['seats_min'] and summaries['Y14']['compatible_winners'] == ['A'])
    for value, expected in [(0,'A'), (19,'A'), (20,'A'), (23,'A'), (24,'C'), (25,'C'), (1000,'C')]:
        record = deepcopy(y13['record']); record['plans'][2]['seats'] = value
        check('Y13 seat boundary ' + str(value), eligible_winner(record) == expected)
    for value in [0, 100, 101, 1000000]:
        record = deepcopy(y14['record']); record['plans'][2]['cost'] = value
        check('Y14 irrelevant cost ' + str(value), eligible_winner(record) == 'A')
    tie = deepcopy(y13['record']); tie['plans'][2]['seats'] = 24
    check('Y13 lower-cost tie explicitly resolved', eligible_winner(tie) == 'C')
    absent_tie = deepcopy(tie); del absent_tie['requirements']['tie_break']
    rejects('Unspecified tie is rejected rather than guessed', lambda: eligible_winner(absent_tie))
    equal_cost = deepcopy(tie); equal_cost['plans'][2]['cost'] = 96
    rejects('Equal-seat equal-cost tie remains rejected', lambda: eligible_winner(equal_cost))
    invalid = deepcopy(y13); invalid['record']['plans'][0]['cost'] = -1
    rejects('Negative observed cost rejected', lambda: constraint_summary(invalid))
    invalid = deepcopy(y13); invalid['record']['plans'][0]['cost'] = True
    rejects('Boolean observed value rejected', lambda: constraint_summary(invalid))
    invalid = deepcopy(y13); invalid['record']['plans'][0]['cost'] = None
    rejects('Multiple missing values rejected', lambda: constraint_summary(invalid))
    for item in [y13, y14]:
        for shuffled in [list(reversed(item['record']['plans'])), item['record']['plans'][1:]+item['record']['plans'][:1]]:
            candidate = deepcopy(item); candidate['record']['plans'] = shuffled
            check(item['item_id'] + ' helper result independent of list order', constraint_summary(candidate)['computed_key'] == item['answer_key'])
    worksheet = (HERE / 'PRACTICE_CONSTRAINTS_WORKSHEET.md').read_text()
    check('Worksheet includes all family references', all('## ' + i['item_id'] + ' ' in worksheet for i in items))
    check('Worksheet omits answer and coaching fields', not any(s in worksheet for s in ['**Key:**', 'answer_key', '**Correct prepared advice', '**Common verified feedback', 'counterexamples', 'invariant_exclusion']))
    return {'date': '2026-10-16', 'checks_passed': len(checks), 'checks_failed': 0,
            'family_ids': spec['item_ids'], 'new_items': ['Y13', 'Y14'],
            'total_drafts': 20, 'missing_items': 10, 'computed_answer_bases': summaries,
            'advice_word_counts': lengths, 'human_review': 'pending', 'participants': 0,
            'scope': 'Supplied-rule logical outcomes, exposure, feedback and narrow missingness cue; not age suitability, form equivalence, security or empirical validation.',
            'checks': checks}


if __name__ == '__main__':
    print(json.dumps(run_checks(), indent=2))

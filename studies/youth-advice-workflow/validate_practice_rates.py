"""Consistency checks for a fictional rates practice set, not human validation."""
import json
from collections import Counter
from fractions import Fraction
from pathlib import Path
from materials import load_items, load_baseline_items, visible_trial, score_response

HERE = Path(__file__).resolve().parent
checks = []

def check(name, condition):
    if not condition:
        raise AssertionError(name)
    checks.append(name)

def rejects(name, action):
    try:
        action()
    except ValueError:
        checks.append(name)
        return
    raise AssertionError(name)

bank = {i['item_id']: i for i in load_items()}
spec = json.loads((HERE / 'practice_rates_set.json').read_text())
plan = json.loads((HERE / 'plan.json').read_text())
items = [bank[ident] for ident in spec['item_ids']]
check('Three distinct family IDs', len(items) == len({i['item_id'] for i in items}) == 3)
check('One answer key per label', Counter(i['answer_key'] for i in items) == spec['answer_category_counts'])
check('All references are rates practice drafts', all(i['parallel_family'] == 'rates' and i['illustrative_phase'] == 'practice' for i in items))
check('No full advice lists fabricated', spec['frozen_advice_lists'] is None)
check('Original planning counts retained', [p['count'] for p in plan['phases']] == [6, 12, 8, 4])
check('Six separate baseline records retained', len(load_baseline_items()) == 6)
check('Twenty total drafts leave ten missing', len(bank) + len(load_baseline_items()) == 20 and sum(p['count'] for p in plan['phases']) - 20 == 10)
check('No duplicate baseline/practice IDs', not ({i['item_id'] for i in load_baseline_items()} & set(bank)))

word_counts = []
computed = {}
for i in items:
    ident = i['item_id']; g = {x['name']: x for x in i['record']['groups']}
    check(ident + ' review pending', i['independent_review'] == 'pending')
    check(ident + ' raw counts feasible', all(x['completed'] >= 0 and (x['invited'] is None or x['invited'] >= x['completed'] > 0) for x in g.values()))
    if all(x['invited'] is not None for x in g.values()):
        rates = {n: Fraction(x['completed'], x['invited']) for n, x in g.items()}
        key = 'Supported' if rates['A'] > rates['B'] else 'Contradicted'
        computed[ident] = {'rate_A': str(rates['A']), 'rate_B': str(rates['B'])}
    else:
        b = i['answer_basis']; implications = []
        check(ident + ' exactly one recorded total unavailable', sum(x['invited'] is None for x in g.values()) == 1)
        for example in b['counterexamples']:
            for name, group in g.items():
                n = example['invited_' + name]
                check(ident + ' alternative totals respect recorded counts', n >= group['completed'] and (group['invited'] is None or n == group['invited']))
            higher = Fraction(g['A']['completed'], example['invited_A']) > Fraction(g['B']['completed'], example['invited_B'])
            check(ident + ' counterexample implication matches calculation', higher == example['claim_supported'])
            implications.append(higher)
        check(ident + ' compatible opposite rankings', set(implications) == {True, False})
        key = 'Not enough information'
        computed[ident] = {'known_rate_B': '1/2', 'possible_rate_A': ['3/5', '3/10'], 'recorded_rate_A': None}
    check(ident + ' recorded key follows supplied rule', key == i['answer_key'])
    check(ident + ' correct advice keyed, misleading advice different', i['advice_variants']['correct']['recommendation'] == key and i['advice_variants']['misleading']['recommendation'] != key)
    word_counts.append({'item_id': ident, **{q: len(a['reason'].split()) for q, a in i['advice_variants'].items()}})
    for quality in ['correct', 'misleading']:
        first = visible_trial(i, 'judgment_first', 'practice', 'first', quality)
        review = visible_trial(i, 'judgment_first', 'practice', 'review', quality, first_response_recorded=True)
        early = visible_trial(i, 'advice_first', 'practice', 'first', quality)
        check(ident + ' initial judgment sees record only', set(first) == {'item_id', 'title', 'fictional', 'record', 'claim', 'choices'})
        check(ident + ' both assisted workflows see identical frozen advice', review['advice'] == early['advice'] == i['advice_variants'][quality])
        for arm in ['judgment_first', 'advice_first']:
            v = visible_trial(i, arm, 'practice', 'feedback', quality, final_response_recorded=True)
            check(ident + ' common feedback after final response', v['feedback'] == i['shared_feedback'])
            rejects(ident + ' feedback held before final response', lambda: visible_trial(i, arm, 'practice', 'feedback', quality))
    no_ai = visible_trial(i, 'no_ai', 'practice', 'first')
    check(ident + ' no-AI sees no advice or key', set(no_ai) == {'item_id', 'title', 'fictional', 'record', 'claim', 'choices'})
    check(ident + ' no-AI receives same final feedback', visible_trial(i, 'no_ai', 'practice', 'feedback', final_response_recorded=True)['feedback'] == i['shared_feedback'])
    rejects(ident + ' no-AI has no quality label', lambda: visible_trial(i, 'no_ai', 'practice', 'first', 'correct'))
    for arm in plan['arms']:
        rejects(ident + ' review held before first response', lambda: visible_trial(i, arm, 'practice', 'review', None if arm == 'no_ai' else 'correct'))
    check(ident + ' keyed response scoring', score_response(i, key)['final_correct'] == 1)
    check(ident + ' missing response stays missing', score_response(i, None, response_status='skipped')['final_correct'] is None)
    if ident in {'Y09', 'Y10'}:
        check(ident + ' explicit practice-only guard', i['allowed_phases'] == ['practice'])
        for arm in plan['arms']:
            for phase in ['baseline', 'delayed_unaided', 'challenge']:
                rejects(ident + ' rejects wrong phase ' + arm + ' ' + phase, lambda: visible_trial(i, arm, phase, 'first'))

# Expose selected surface rules instead of declaring the set free from cues.
complete_items = [bank['Y02'], bank['Y09']]
heuristic = []
for i in complete_items:
    a, b = i['record']['groups']
    raw = 'Supported' if a['completed'] > b['completed'] else 'Contradicted'
    reverse = 'Contradicted' if raw == 'Supported' else 'Supported'
    heuristic.append({'item_id': i['item_id'], 'raw_count_key': raw, 'raw_count_correct': raw == i['answer_key'], 'reverse_count_correct': reverse == i['answer_key']})
check('Raw-count shortcut fails at least one complete record', not all(x['raw_count_correct'] for x in heuristic))
check('Reverse-count shortcut fails at least one complete record', not all(x['reverse_count_correct'] for x in heuristic))
y09 = bank['Y09']['record']['groups']
check('Y09 misleading non-completion counts are real arithmetic', [x['invited'] - x['completed'] for x in y09] == [20, 24])
worksheet = (HERE / 'PRACTICE_RATES_WORKSHEET.md').read_text()
check('Worksheet includes all family items', all('## ' + i['item_id'] + ' ' in worksheet for i in items))
check('Worksheet omits answer/coaching fields', not any(x in worksheet for x in ['**Key:**', 'answer_key', '**Correct prepared advice', '**Common verified feedback', 'counterexamples']))

print(json.dumps({
    'date': '2026-10-16', 'checks_passed': len(checks), 'checks_failed': 0,
    'family_ids': spec['item_ids'], 'family_extension_ids': ['Y09', 'Y10'], 'items_added_this_update': [],
    'total_drafts': 20, 'missing_items': 10, 'computed_answer_bases': computed,
    'advice_word_counts': word_counts, 'shortcut_audit': heuristic,
    'unresolved_cue': 'Only Y10 has a missing invitation total; this is not an unbiased/validated set.',
    'human_review': 'pending', 'participants': 0,
    'scope': 'Supplied arithmetic, counterexample consistency, phase/exposure/feedback boundaries and chosen heuristics; not security, age suitability, equivalence, mechanism or empirical validation.',
    'checks': checks
}, indent=2))

"""Check baseline records, answer calculations and information boundaries.

Artificial fixtures only. This is not adolescent testing or independent review.
"""
import json
from collections import Counter
from fractions import Fraction
from pathlib import Path
from materials import load_baseline_items, load_items, visible_trial, score_response, complete_stage_accuracy

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

items = load_baseline_items()
older = load_items()
plan = json.loads((HERE / 'plan.json').read_text())
check('Six baseline-only examples', len(items) == 6)
check('Eighteen distinct example IDs', len({i['item_id'] for i in items + older}) == 18)
check('Task bank includes eight original and four added practice examples', len(older) == 12)
check('Youth phase counts preserved', [p['count'] for p in plan['phases']] == [6,12,8,4])
check('Age band and sample unchanged', plan['population_age_band'] == [15,17] and plan['pretest_max_n'] == 12 and plan['randomized_target_n'] == 90)
check('Full bank remains incomplete', plan['item_bank_complete'] is False)
check('Two keys per label', Counter(i['answer_key'] for i in items) == {'Supported':2,'Contradicted':2,'Not enough information':2})

for item in items:
    ident = item['item_id']; r = item['record']; b = item['answer_basis']
    check(ident + ' baseline only, no advice variants', item['allowed_phases'] == ['baseline'] and item['advice_variants'] is None)
    check(ident + ' independent review pending', item['independent_review'] == 'pending')
    kind = b['kind']
    if kind == 'constraints':
        eligible = [x for x in r['plans'] if x['cost'] <= r['requirements']['budget_max'] and x['seats'] >= r['requirements']['seats_min']]
        winners = [x['name'] for x in eligible if x['seats'] == max(e['seats'] for e in eligible)]
        check(ident + ' unique winner', winners == [b['expected_choice']])
        computed = 'Supported' if b['claimed_choice'] in winners else 'Contradicted'
    elif kind == 'rate_comparison':
        groups = {g['name']:g for g in r['groups']}
        a,z = groups[b['left']],groups[b['right']]
        computed = 'Supported' if Fraction(a['completed'],a['invited']) > Fraction(z['completed'],z['invited']) else 'Contradicted'
    elif kind == 'pooled_rate':
        rate = Fraction(sum(g['completed'] for g in r['groups']),sum(g['total'] for g in r['groups']))
        check(ident + ' pooled exact fraction is 3/10', rate == Fraction(3,10))
        computed = 'Supported' if 100 * rate == Fraction(b['claimed_percentage']) else 'Contradicted'
    elif kind == 'missing_denominators':
        check(ident + ' both denominators unknown', all(g['invited'] is None for g in r['groups']))
        counts = {g['name']:g['completed'] for g in r['groups']}
        signs = []
        for example in b['counterexamples']:
            check(ident + ' feasible alternative ' + example['implies'], example['invited_A'] >= counts['A'] and example['invited_B'] >= counts['B'])
            signs.append(Fraction(counts['B'],example['invited_B']) > Fraction(counts['A'],example['invited_A']))
        check(ident + ' same recorded counts admit opposite orderings', signs == [True,False])
        computed = 'Not enough information'
    elif kind == 'causal_missing':
        check(ident + ' records change without isolated cause', r['before_week']['late_returns']-r['after_week']['late_returns'] == 6 and not r['comparison_group'] and not r['other_changes_recorded'])
        computed = 'Not enough information'  # consistency with bounded rule, not semantic validation
    else:
        raise AssertionError('Unsupported answer-basis kind: ' + kind)
    check(ident + ' key consistent with recorded rule', computed == item['answer_key'])
    for arm in plan['arms']:
        for stage in ['first','review']:
            view = visible_trial(item,arm,'baseline',stage,first_response_recorded=stage=='review')
            check(ident + ' ' + arm + ' ' + stage + ' no key or coaching', set(view) == {'item_id','title','fictional','record','claim','choices'})
        rejects(ident + ' ' + arm + ' cannot show block feedback early', lambda:visible_trial(item,arm,'baseline','feedback',final_response_recorded=True))
        view = visible_trial(item,arm,'baseline','feedback',final_response_recorded=True,phase_complete=True)
        check(ident + ' ' + arm + ' same block-end feedback',view['feedback'] == item['shared_feedback'])
        for phase in ['practice','delayed_unaided','challenge']:
            rejects(ident + ' not reusable in ' + arm + ' ' + phase, lambda:visible_trial(item,arm,phase,'first'))
    rejects(ident + ' baseline cannot have advice quality', lambda:visible_trial(item,'advice_first','baseline','first','correct'))
    check(ident + ' answer scoring',score_response(item,item['answer_key'])['final_correct'] == 1)
    check(ident + ' skipped stays missing',score_response(item,None,response_status='skipped')['final_correct'] is None)

check('All six answered yields a descriptive score', complete_stage_accuracy([{'final_correct':x} for x in [1,1,1,0,0,0]],6) == .5)
check('Missing baseline cannot silently reduce denominator',complete_stage_accuracy([{'final_correct':1}]*5,6) is None)
check('Missing value is not zero',complete_stage_accuracy([{'final_correct':1}]*5+[{'final_correct':None}],6) is None)
worksheet=(HERE/'BASELINE_WORKSHEET.md').read_text()
check('Every baseline ID on worksheet',all('## '+i['item_id']+' ' in worksheet for i in items))
check('Worksheet has no researcher answer fields',not any(x in worksheet for x in ['**Key:**','**Answer basis','answer_key','Full-credit explanation anchor']))
print(json.dumps({'date':'2026-10-14','checks_passed':len(checks),'checks_failed':0,'baseline_examples':6,'total_examples':18,'missing_items':12,'independent_review':'pending','adolescent_testing':False,'scope':'Computed keys, data structure, missingness, phase and feedback boundaries only; not measurement validity, usability or security','checks':checks},indent=2))

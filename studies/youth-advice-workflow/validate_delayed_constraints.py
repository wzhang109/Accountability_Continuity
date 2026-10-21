"""Supplied-rule and exposure checks for fictional unaided delayed items.

AI-assisted review tooling. A second algorithm is not an independent reviewer.
No test establishes adolescent suitability or a learning effect.
"""
import json
from collections import Counter
from copy import deepcopy
from itertools import permutations
from pathlib import Path

from materials import (load_items, load_baseline_items, visible_trial,
                       score_response, complete_stage_accuracy)
from validate_practice_constraints import constraint_summary

HERE = Path(__file__).resolve().parent


def independent_winner(record):
    """Separate calculation using pairwise dominance, not the existing helper."""
    req = record['requirements']
    eligible = [row for row in record['plans']
                if row['cost'] <= req['budget_max']
                and row['seats'] >= req['seats_min']]
    if not eligible:
        raise ValueError('No eligible option')
    winners = [row['name'] for row in eligible if all(
        row['name'] == other['name']
        or row['seats'] > other['seats']
        or (row['seats'] == other['seats']
            and req.get('tie_break') == 'Lower cost when seat counts tie'
            and row['cost'] < other['cost']) for other in eligible)]
    if len(winners) != 1:
        raise ValueError('Choice rule does not give one winner')
    return winners[0]


def complete_record(item, value):
    record = deepcopy(item['record'])
    basis = item['answer_basis']
    next(row for row in record['plans'] if row['name'] == basis['missing_plan'])[
        basis['missing_field']] = value
    return record


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
            checks.append(name)
            return
        raise AssertionError(name)

    bank = {item['item_id']: item for item in load_items()}
    spec = json.loads((HERE / 'delayed_constraints_set.json').read_text())
    plan = json.loads((HERE / 'plan.json').read_text())
    items = [bank[ident] for ident in spec['item_ids']]
    check('Two new delayed examples', spec['item_ids'] == ['Y15', 'Y16'])
    check('Counts and incomplete bank retained',
          len(bank) + len(load_baseline_items()) == 22
          and [phase['count'] for phase in plan['phases']] == [6, 12, 8, 4]
          and plan['item_bank_complete'] is False)
    check('New labels match specification',
          Counter(i['answer_key'] for i in items) == spec['answer_category_counts'])
    check('Six delayed drafts, not a full eight-item form',
          sum(i['illustrative_phase'] == 'delayed_unaided' for i in bank.values()) == 6)
    results = {}
    view_fields = {'item_id', 'title', 'fictional', 'record', 'claim', 'choices'}
    for item in items:
        ident = item['item_id']
        basis = item['answer_basis']
        check(ident + ' delayed-only without advice',
              item['allowed_phases'] == ['delayed_unaided']
              and item['illustrative_phase'] == 'delayed_unaided'
              and item['advice_variants'] is None)
        check(ident + ' human review pending', item['independent_review'] == 'pending')
        check(ident + ' one explicit unknown in a nonnegative domain',
              sum(row[k] is None for row in item['record']['plans']
                  for k in ['cost', 'seats']) == 1
              and basis['missing_domain'] == 'non-negative integers')
        summary = constraint_summary(item)
        check(ident + ' key follows compatible classes',
              summary['computed_key'] == item['answer_key'])
        # Every integer through the last decision threshold, plus a large tail
        # representative. Above that threshold, eligibility/rank is invariant.
        if basis['missing_field'] == 'seats':
            upper = max(item['record']['requirements']['seats_min'],
                        *(row['seats'] for row in item['record']['plans']
                          if row['seats'] is not None)) + 1
        else:
            upper = item['record']['requirements']['budget_max'] + 1
        values = list(range(upper + 1)) + [1000000]
        truths = set()
        for value in values:
            record = complete_record(item, value)
            winner = independent_winner(record)
            truths.add(winner == basis['claimed_choice'])
            for ordered_rows in permutations(record['plans']):
                permuted = deepcopy(record)
                permuted['plans'] = list(ordered_rows)
                check(ident + ' completion/order ' + str(value) + ' ' +
                      ''.join(row['name'] for row in ordered_rows),
                      independent_winner(permuted) == winner)
        check(ident + ' separately enumerated truth set',
              sorted(truths) == summary['truth_values'])
        for example in basis.get('counterexamples', basis.get('examples', [])):
            winner = independent_winner(complete_record(item, example['missing_value']))
            check(ident + ' hypothetical example ' + str(example['missing_value']),
                  winner == example['eligible_winner']
                  and (winner == basis['claimed_choice']) == example['claim_supported'])
        reference_view = None
        for arm in plan['arms']:
            for stage in ['first', 'review']:
                view = visible_trial(item, arm, 'delayed_unaided', stage,
                                     first_response_recorded=stage == 'review')
                check(ident + ' no key/advice ' + arm + ' ' + stage,
                      set(view) == view_fields)
                if reference_view is None:
                    reference_view = view
                check(ident + ' same unaided task ' + arm + ' ' + stage,
                      view == reference_view)
            rejects(ident + ' no review before response ' + arm,
                    lambda: visible_trial(item, arm, 'delayed_unaided', 'review'))
            rejects(ident + ' no feedback before final ' + arm,
                    lambda: visible_trial(item, arm, 'delayed_unaided', 'feedback',
                                          phase_complete=True))
            rejects(ident + ' individual final does not finish block ' + arm,
                    lambda: visible_trial(item, arm, 'delayed_unaided', 'feedback',
                                          final_response_recorded=True))
            view = visible_trial(item, arm, 'delayed_unaided', 'feedback',
                                 final_response_recorded=True, phase_complete=True)
            check(ident + ' common feedback after block ' + arm,
                  view['feedback'] == item['shared_feedback']
                  and view['answer_key'] == item['answer_key']
                  and 'advice' not in view)
            for quality in ['correct', 'misleading']:
                rejects(ident + ' no delayed advice quality ' + arm + ' ' + quality,
                        lambda: visible_trial(item, arm, 'delayed_unaided', 'first', quality))
            for phase in ['baseline', 'practice', 'challenge']:
                rejects(ident + ' no reuse ' + arm + ' ' + phase,
                        lambda: visible_trial(item, arm, phase, 'first'))
        check(ident + ' keyed response correct',
              score_response(item, item['answer_key'])['final_correct'] == 1)
        check(ident + ' other labels incorrect', all(
            score_response(item, option)['final_correct'] == 0
            for option in item['choices'] if option != item['answer_key']))
        check(ident + ' absent outcome missing',
              score_response(item, None, response_status='technical_missing') ==
              {'final_correct': None, 'brier_error': None})
        results[ident] = summary

    y15, y16 = items
    for value, winner in [(0, 'C'), (11, 'C'), (12, 'C'), (17, 'C'),
                          (18, 'A'), (19, 'A'), (22, 'A')]:
        check('Y15 eligibility/rank boundary ' + str(value),
              independent_winner(complete_record(y15, value)) == winner)
    for value in [0, 84, 85, 1000000]:
        check('Y16 invariant exclusion ' + str(value),
              independent_winner(complete_record(y16, value)) == 'B')
    check('Missing-information heuristic does not determine both keys',
          y15['answer_key'] != y16['answer_key'])
    check('Irrelevant missingness can support rejecting the claim',
          y16['answer_key'] == 'Contradicted')
    tie = complete_record(y15, 18)
    del tie['requirements']['tie_break']
    rejects('No unstated tie decision', lambda: independent_winner(tie))
    check('Six draft responses cannot replace eight-item primary measure',
          complete_stage_accuracy([{'final_correct': 1}] * 6, 8) is None)
    check('Incomplete eight-item outcome not imputed',
          complete_stage_accuracy([{'final_correct': 1}] * 7 +
                                  [{'final_correct': None}], 8) is None)
    sheet = (HERE / 'DELAYED_CONSTRAINTS_WORKSHEET.md').read_text()
    check('All new IDs in answer-free worksheet',
          all('## ' + i['item_id'] + ' ' in sheet for i in items))
    check('No answers or coaching fields on worksheet', not any(
        marker in sheet for marker in ['**Key:**', 'answer_key', 'counterexamples',
                                      'shared_feedback', 'Explanation anchor']))
    return {'date': '2026-10-19', 'checks_passed': len(checks), 'checks_failed': 0,
            'new_item_ids': spec['item_ids'], 'total_drafts': 22, 'missing_items': 8,
            'computed_answer_bases': results, 'participants': 0,
            'independent_human_review': 'pending',
            'scope': 'Supplied integer-rule outcomes, view/scoring boundaries and '
                     'record-order invariance; not difficulty, validity, secure '
                     'deployment, learning or independent human review.',
            'checks': checks}


if __name__ == '__main__':
    print(json.dumps(run_checks(), indent=2))

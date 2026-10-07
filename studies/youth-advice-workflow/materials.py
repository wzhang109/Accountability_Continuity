"""Local review helpers for fictional youth materials; no recruitment or data service.
AI-assisted development. Display checks are not educational or ethical validation.
"""
import json
import math
from copy import deepcopy
from pathlib import Path

HERE = Path(__file__).resolve().parent
ARMS = {'judgment_first', 'advice_first', 'no_ai'}
PHASES = {'baseline', 'practice', 'delayed_unaided', 'challenge'}
STAGES = {'first', 'review', 'feedback'}
MISSING = {'skipped', 'not_presented', 'technical_missing', 'withdrawn'}


def load_items():
    return json.loads((HERE / 'task_bank.json').read_text())['tasks']


def visible_trial(item, arm, phase, stage, advice_quality=None,
                  first_response_recorded=False, final_response_recorded=False,
                  phase_complete=False):
    """Return a researcher-review screen payload with stage-dependent information.

    This function is not a secured study application. The JSON answer bank must
    remain server-side in any future implementation; returning a filtered dict
    alone does not protect files a browser has already downloaded.
    """
    if arm not in ARMS or phase not in PHASES or stage not in STAGES:
        raise ValueError('Unknown arm, phase or stage')
    assisted = arm != 'no_ai' and phase in {'practice', 'challenge'}
    if assisted and advice_quality not in {'correct', 'misleading'}:
        raise ValueError('An assisted trial needs one frozen advice version')
    if not assisted and advice_quality is not None:
        raise ValueError('Unaided phases must not have an advice-quality label')
    if stage == 'review' and not first_response_recorded:
        raise ValueError('Record the first response before the review step')
    if stage == 'feedback':
        if not final_response_recorded:
            raise ValueError('Record the final response before feedback')
        if phase in {'baseline', 'delayed_unaided'} and not phase_complete:
            raise ValueError('Hold assessment feedback until the block is complete')
    view = {'item_id': item['item_id'], 'title': item['title'],
            'fictional': True, 'record': deepcopy(item['record']),
            'claim': item['claim'], 'choices': list(item['choices'])}
    if stage == 'feedback':
        view['feedback'] = item['shared_feedback']
        view['answer_key'] = item['answer_key']
    elif assisted and (stage == 'review' or arm == 'advice_first'):
        view['advice'] = deepcopy(item['advice_variants'][advice_quality])
    return view


def score_response(item, final_answer, confidence=None, response_status='answered'):
    """Item-level descriptive score. Missing responses are never coded as wrong."""
    if response_status in MISSING:
        return {'final_correct': None, 'brier_error': None}
    if response_status != 'answered' or final_answer not in item['choices']:
        raise ValueError('A valid answered response needs one of the stated choices')
    correct = int(final_answer == item['answer_key'])
    brier = None
    if confidence is not None:
        if isinstance(confidence, bool) or not isinstance(confidence, (int, float)):
            raise ValueError('Confidence must be a number from 0 to 100')
        if not math.isfinite(confidence) or not 0 <= confidence <= 100:
            raise ValueError('Confidence must be finite and between 0 and 100')
        brier = (confidence / 100 - correct) ** 2
    return {'final_correct': correct, 'brier_error': brier}


def complete_stage_accuracy(item_scores, expected_count):
    """Provisional development convention; a partial stage has no primary score.

    This does not implement the final missing-data analysis, which needs review.
    It also cannot estimate an intention-to-treat effect when follow-ups are absent.
    """
    if expected_count <= 0:
        raise ValueError('Expected item count must be positive')
    if len(item_scores) != expected_count:
        return None
    values = [s['final_correct'] for s in item_scores]
    if any(v is None for v in values):
        return None
    if any(v not in (0, 1) for v in values):
        raise ValueError('Answered correctness must be binary')
    return sum(values) / expected_count

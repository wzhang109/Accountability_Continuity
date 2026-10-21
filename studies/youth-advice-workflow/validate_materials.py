"""Check fictional task arithmetic and critical information boundaries.
These checks do not validate theory, adolescent suitability or rater agreement.
"""
import json
import re
from fractions import Fraction
from pathlib import Path
from materials import load_items, visible_trial, score_response, complete_stage_accuracy
from validate_practice_constraints import constraint_summary

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

items = load_items()
plan = json.loads((HERE/'plan.json').read_text())
check('Sixteen practice/delayed development examples, not a full bank', len(items)==16 and not plan['item_bank_complete'])
check('Unique item IDs', len({i['item_id'] for i in items})==16)
check('Youth and adult counts not mixed', [p['count'] for p in plan['phases']]==[6,12,8,4])
check('Population and planning sample', plan['population_age_band']==[15,17] and plan['randomized_target_n']==90 and plan['pretest_max_n']==12)
check('Ten illustrative practice and six delayed items', sum(i['illustrative_phase']=='practice' for i in items)==10 and sum(i['illustrative_phase']=='delayed_unaided' for i in items)==6)

lengths=[]
for i in items:
    b=i['answer_basis'];r=i['record']; key=i['answer_key']
    if b['kind']=='constraints':
        eligible=[x for x in r['plans'] if x['cost']<=r['requirements']['budget_max'] and x['seats']>=r['requirements']['seats_min']]
        max_seats=max(x['seats'] for x in eligible)
        winners=[x['name'] for x in eligible if x['seats']==max_seats]
        check(i['item_id']+' unique feasible winner', winners==[b['expected_choice']])
        computed='Supported' if b['claimed_choice'] in winners else 'Contradicted'
    elif b['kind']=='constraints_partial':
        computed=constraint_summary(i)['computed_key']
    elif b['kind']=='rate_comparison':
        g={x['name']:x for x in r['groups']};left=g[b['left']];right=g[b['right']]
        computed='Supported' if Fraction(left['completed'],left['invited'])>Fraction(right['completed'],right['invited']) else 'Contradicted'
    elif b['kind']=='pooled_rate':
        actual=100*Fraction(sum(x['completed'] for x in r['groups']),sum(x['total'] for x in r['groups']))
        computed='Supported' if actual==Fraction(b['claimed_percentage']) else 'Contradicted'
    elif b['kind']=='missing_invitation_total':
        g={x['name']:x for x in r['groups']}
        check(i['item_id']+' one stated missing denominator', g[b['missing_group']]['invited'] is None)
        rankings=[]
        for example in b['counterexamples']:
            for name,group in g.items():
                n=example['invited_'+name]
                check(i['item_id']+' feasible total '+name, n>=group['completed'] and (group['invited'] is None or n==group['invited']))
            rankings.append(Fraction(g[b['left']]['completed'],example['invited_'+b['left']])>Fraction(g[b['right']]['completed'],example['invited_'+b['right']]))
        check(i['item_id']+' compatible opposite rankings', set(rankings)=={True,False})
        computed='Not enough information'
    else:
        check(i['item_id']+' documented causal gap', b['kind']=='causal_missing' and r['comparison_group'] is False and r['other_changes_recorded'] is False)
        computed='Not enough information' # bounded rule only, not expert semantic validation
    check(i['item_id']+' key consistency', computed==key)
    if i.get('advice_variants') is None:
        check(i['item_id']+' delayed-only record has no advice', i['allowed_phases']==['delayed_unaided'] and i['illustrative_phase']=='delayed_unaided')
        for arm in plan['arms']:
            for stage in ['first','review']:
                view=visible_trial(i,arm,'delayed_unaided',stage,first_response_recorded=stage=='review')
                check(i['item_id']+' '+arm+' '+stage+' no advice or key', set(view)=={'item_id','title','fictional','record','claim','choices'})
            rejects(i['item_id']+' no per-item delayed feedback '+arm, lambda:visible_trial(i,arm,'delayed_unaided','feedback',final_response_recorded=True))
            feedback=visible_trial(i,arm,'delayed_unaided','feedback',final_response_recorded=True,phase_complete=True)
            check(i['item_id']+' common block-end feedback '+arm, feedback['feedback']==i['shared_feedback'])
            for phase in ['baseline','practice','challenge']:
                rejects(i['item_id']+' no reuse '+arm+' '+phase, lambda:visible_trial(i,arm,phase,'first'))
            rejects(i['item_id']+' no delayed quality '+arm, lambda:visible_trial(i,arm,'delayed_unaided','first','correct'))
        check(i['item_id']+' exact answer scored',score_response(i,key,80)=={'final_correct':1,'brier_error':(0.8-1)**2})
        check(i['item_id']+' missing follow-up not zero',score_response(i,None,response_status='not_presented')=={'final_correct':None,'brier_error':None})
        check(i['item_id']+' no missing confidence imputation',score_response(i,key)['brier_error'] is None)
        continue
    check(i['item_id']+' correct and misleading recommendations', i['advice_variants']['correct']['recommendation']==key and i['advice_variants']['misleading']['recommendation']!=key)
    lengths.append({'item':i['item_id'], **{k:len(v['reason'].split()) for k,v in i['advice_variants'].items()}})
    for arm in plan['arms']:
        for phase in ['baseline','delayed_unaided']:
            if 'allowed_phases' in i and phase not in i['allowed_phases']:
                rejects(i['item_id']+f' {arm} reject reuse in {phase}', lambda:visible_trial(i,arm,phase,'first'))
            else:
                view=visible_trial(i,arm,phase,'first')
                check(i['item_id']+f' {arm} {phase} no advice or key', not ({'advice','answer_key','feedback'} & set(view)))
        check(i['item_id']+' no-AI practice no advice', 'advice' not in visible_trial(i,'no_ai','practice','first'))
    q='misleading'
    check(i['item_id']+' judgment-first initial no advice', 'advice' not in visible_trial(i,'judgment_first','practice','first',q))
    check(i['item_id']+' judgment-first later exact advice', visible_trial(i,'judgment_first','practice','review',q,first_response_recorded=True)['advice']==i['advice_variants'][q])
    check(i['item_id']+' advice-first initial same advice', visible_trial(i,'advice_first','practice','first',q)['advice']==i['advice_variants'][q])
    for arm in ['judgment_first','advice_first']:
        for quality in ['correct','misleading']:
            v=visible_trial(i,arm,'practice','feedback',quality,final_response_recorded=True)
            check(i['item_id']+f' {arm} {quality} common feedback', v['feedback']==i['shared_feedback'])
    check(i['item_id']+' exact answer scored', score_response(i,key,80)=={'final_correct':1,'brier_error':(0.8-1)**2})
    check(i['item_id']+' missing follow-up not zero', score_response(i,None,response_status='not_presented')=={'final_correct':None,'brier_error':None})
    check(i['item_id']+' no missing confidence imputation', score_response(i,key)['brier_error'] is None)

item=items[0]
rejects('No delayed advice-quality label',lambda:visible_trial(item,'advice_first','delayed_unaided','first','misleading'))
rejects('No review before first response',lambda:visible_trial(item,'judgment_first','practice','review','correct'))
rejects('No feedback before final response',lambda:visible_trial(item,'judgment_first','practice','feedback','correct'))
rejects('No delayed block feedback while incomplete',lambda:visible_trial(item,'no_ai','delayed_unaided','feedback',final_response_recorded=True))
check('Delayed block feedback only afterward', 'feedback' in visible_trial(item,'no_ai','delayed_unaided','feedback',final_response_recorded=True,phase_complete=True))
check('Partial stage not scored with reduced denominator', complete_stage_accuracy([{'final_correct':1}]*7,8) is None)
check('Missing item stage stays missing', complete_stage_accuracy([{'final_correct':1}]*7+[{'final_correct':None}],8) is None)
check('Complete stage accuracy',complete_stage_accuracy([{'final_correct':1}]*6+[{'final_correct':0}]*2,8)==0.75)
rejects('Reject confidence above range', lambda:score_response(item,item['answer_key'],101))
rejects('Reject nonfinite confidence', lambda:score_response(item,item['answer_key'],float('nan')))

# Privacy checks cover new upload contents, not private administrative files.
public_root=HERE.parents[1]
new_files=list(HERE.rglob('*')) + [public_root/'docs/design-alignment-2026-10-06.md', public_root/'docs/progress-2026-10-07.zh-CN.md']
for f in new_files:
    if not f.is_file() or f.suffix not in {'.md','.json','.py'}:continue
    txt=f.read_text()
    if f.name not in {'validate_materials.py'}:
        check('No private local paths '+str(f.relative_to(public_root)), '/Users/' not in txt and '/private/' not in txt)
        check('No contact email '+str(f.relative_to(public_root)),re.search(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}',txt) is None)
        check('No grant ID field '+str(f.relative_to(public_root)),'"application_id"' not in txt)

result={'checks_passed':len(checks),'checks_failed':0,'task_count':len(items),'complete_item_bank':False,'advice_word_counts':lengths,'human_review':'pending','participants':0,'validation_scope':'arithmetic, structure, scorer and view payload only; not validity or a secure implementation','checks':checks}
print(json.dumps(result,indent=2))

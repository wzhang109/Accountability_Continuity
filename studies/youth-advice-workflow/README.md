# Youth advice workflow feasibility materials

**Development version October 12, 2026**

This folder makes one practical question reviewable: does requiring an initial
answer before prepared AI advice change what 15–17-year-old learners can do on
new related tasks without advice about a week later? It develops an earlier
proposal into a protocol, sixteen fictional examples, explicit scoring boundaries,
and a data structure. It contains no participants, pilot data or results.

The study tests a workflow package. Initial judgment adds effort and commitment
as well as changing when advice appears. No workflow is assumed to be better.
This is separate from the adult [operational draft](../ai-advice-timing/DRAFT_PROTOCOL.md)
and from the organizational [public-document pilot](../organizational-feedback/README.md).

| File | Use |
|---|---|
| [Protocol](PROTOCOL.md) | Population, phases, advice exposure, feedback, analysis limits and review gates |
| [Baseline worksheet](BASELINE_WORKSHEET.md) and [review guide](BASELINE_REVIEW.md) | Six unaided starting items, answer bases and unresolved measurement choices |
| [Baseline records](baseline_items.json) and [checks](validate_baseline.py) | Separate baseline-only examples, arithmetic and feedback-boundary checks |
| [Rates practice review](PRACTICE_RATES_REVIEW.md) and [answer-free worksheet](PRACTICE_RATES_WORKSHEET.md) | One label-balanced family: Y02, Y09, Y10; paired advice and cue/burden limits |
| [Rates set](practice_rates_set.json) and [checks](validate_practice_rates.py) | Development references, computed counterexamples, exposure checks and shortcut risks |
| [Example tasks](TASK_EXAMPLES.md) | Fictional school records, answer bases and paired advice for human review |
| [Measure to claim map](MEASURES_AND_CLAIMS.md) | What each response can support and what it cannot |
| [Minimal data dictionary](DATA_DICTIONARY.md) | Stage-specific fields, missingness and privacy boundaries |
| [Sources](SOURCES.md) | Focused primary-source positioning and retrieval limits |
| [Review checklist](REVIEW_CHECKLIST.md) | Decisions still requiring people, a setting or feasibility evidence |
| [Task bank](task_bank.json) and [plan](plan.json) | Machine-readable development specifications |
| [Display and scoring helpers](materials.py) | A local review prototype, not a deployed participant interface |
| [Structural checks](validate_materials.py) | Arithmetic keys, advice access, response scoring and privacy checks |

Six baseline, six practice and four new related assessment examples are present.
The complete six-baseline, twelve-practice, eight-delayed and four-challenge bank
still lacks fourteen items (six practice, four delayed and four challenge).
The rates practice family has one key per answer category, but full-bank labels
and correct/misleading advice lists are not yet balanced or frozen.
The six baseline slots have draft examples, not reviewed or frozen instruments. All answers and advice remain pending educator and methodological
review. AI-assisted drafting and automated checks do not establish age
suitability, plausible misleading advice, equal difficulty or rater agreement.

A stated task objective is part of the fictional record. It does not define
what all schools or organizations ought to value. Correct evidence use and a
choice about the purpose of an organization are different questions.

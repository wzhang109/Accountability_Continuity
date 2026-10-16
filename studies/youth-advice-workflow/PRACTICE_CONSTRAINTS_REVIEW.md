# Constraint practice family and missing information

**October 16, 2026 · fictional development materials · human review pending**

Apply the supplied eligibility rules before maximizing seats. Y01/Y11/Y12
are preserved; Y13/Y14 add the reverse missing-information cases. The rule
is a fictional task objective, not a judgment about what schools should value.

All five use budget at most 100 and at least 20 seats. Pairs below are cost/seats.
Unknown is not zero. Y13/Y14 explicitly break equal-seat ties by lower cost;
the earlier records have no ties and their wording remains unchanged.

| Item | Record and claim | Answer basis |
|---|---|---|
| Y01 | A: 96/24; B: 88/18; C: 108/30. Choose C. | Contradicted. Only A qualifies. |
| Y11 | A: 94/26; B: 128/unknown; C: 82/22. Choose A. | Supported. B fails the budget at every seat count. |
| Y12 | A: 94/26; B: unknown/30; C: 82/22. Choose B. | Not enough information. B can be within budget or excluded. |
| Y13 | A: 96/24; B: 82/22; C: 90/unknown. Choose C. | Not enough information. C can fail the seat minimum or have more seats than A. At 24 seats, C wins the stated cost tie. |
| Y14 | A: 96/24; B: 82/22; C: unknown/18. Choose A. | Supported. C fails the seat minimum at every cost. |

Possible completions in an answer explanation are logical examples, not
additional recorded values. All new records remain practice-only; Y05 is a
separate delayed unaided example.

## Advice, feedback and explanation anchors

[task_bank.json](task_bank.json) stores both advice variants and shared feedback.
The [worksheet](PRACTICE_CONSTRAINTS_WORKSHEET.md) omits coaching and keys for
inspection. The repository itself is not a secured participant interface.
A future assisted trial shows only one advice variant, identically worded
across assisted arms. Everyone receives the same feedback after a final answer.

Y13's misleading advice uses a lower known cost to settle a choice without
establishing either the minimum or an equal seat count. Y14's misleading
advice treats a missing cost as decisive despite a known seat shortfall.
Both patterns need independent plausibility and comprehension review.

A relevant Y13 explanation connects the unknown seats to eligibility or rank;
the tie rule does not supply the missing value. For Y14, it connects C's known
seat shortfall to the irrelevance of the unknown cost, then compares A and B.
Numerical counterexamples are optional. These are candidate rater anchors,
not automated explanation grades or evidence of independent rater approval.

## Logical checks and their limits

For Y11–Y14, costs and seats range over non-negative integers. The checker
represents missing costs by 0–101: values above 100 have the same eligibility
effect. For missing seats, it includes every integer through one above the
largest relevant seat threshold; larger values have the same ranking effect.
Y13 therefore includes the exact 24-seat tie and the 25-or-more class.

Every compatible Y14 cost leaves C excluded and A the winner. Y13 admits
different winners: C=18 gives A; C=28 gives C. At C=24, C wins because 90<96.
Unspecified or unresolved ties are rejected rather than silently guessed.
The script also checks boundary values, table-order invariance, phase guards,
withheld keys/advice and shared feedback. These are implementation checks,
not evidence that adolescents understand the intended distinction.

## Which shortcut is addressed

| Missing field | Irrelevant to conclusion | Can change conclusion |
|---|---|---|
| Seats | Y11, Supported | Y13, Not enough information |
| Cost | Y14, Supported | Y12, Not enough information |

Neither field type alone predicts the key across these four records. This is
coverage of four logical situations, **not a matched factorial experiment**.
Y11/Y12 omit B; Y13/Y14 omit C and state a tie rule. The target plan, numbers,
wording and possible within-family learning still differ. Table position and
question targets may still cue answers. No claim of equal difficulty, removed
response bias, construct validity or transfer follows from the matrix.

Five constraint examples have two Supported, one Contradicted and two Not
enough information keys. Across ten practice drafts the counts are 3/3/4,
respectively. The bank has twenty of thirty planned drafts; two practice,
four delayed and four challenge items remain. Full advice lists and item
order are not frozen. Age/language burden, tie-rule comprehension, answer
bases, feedback and rater agreement still require people and feasibility data.

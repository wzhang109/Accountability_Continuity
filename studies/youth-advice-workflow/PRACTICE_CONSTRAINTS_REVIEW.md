# Constraint practice family and missing information

**October 14, 2026 · fictional development materials · human review pending**

These tasks ask whether a plan follows the supplied eligibility rules before
maximizing seats. Y01 is preserved; Y11 and Y12 add cases in which missing
information is irrelevant or decisive. The rule is a fictional task objective,
not a judgment about what schools should value.

| Item | Record and claim | Answer basis |
|---|---|---|
| Y01 | Budget 100, at least 20 seats. A: 96/24; B: 88/18; C: 108/30. Choose C. | Contradicted. Only A meets both constraints; C exceeds budget. |
| Y11 | Same constraints. A: 94/26; B: 128/unknown; C: 82/22. Choose A. | Supported. B fails the budget regardless of its seats. A and C qualify; A has more seats. |
| Y12 | Same constraints. A: 94/26; B: unknown/30; C: 82/22. Choose B. | Not enough information. B could cost 96 and win, or cost 108 and be excluded. A wins in the latter case. |

Pairs in the table are **cost/seats**. Unknown is not zero. The two possible
costs in Y12 illustrate compatible records, not additional observed values.
New records are practice-only. Y05 remains a separate delayed unaided example.

## Advice and explanations

Complete wording for both advice versions and shared feedback is stored in
[task_bank.json](task_bank.json). The [worksheet](PRACTICE_CONSTRAINTS_WORKSHEET.md)
contains only records, claims and response spaces. It is for inspection, not a
secured participant interface. A future assisted trial shows one advice version.

Y11's misleading advice says that an unknown seat count prevents comparison,
overlooking B's known budget failure. Y12's misleading advice chooses the
largest seat count without establishing budget eligibility. Feedback explains
the relevant constraint after the final response, identically across arms.
Neither pattern has been tested for adolescent plausibility.

For the existing short-reason rubric, a strong Y11 explanation connects B's
known exclusion to the irrelevance of its missing seats, then compares A and C.
A strong Y12 explanation says how an unknown cost changes B's eligibility.
It need not invent numerical examples. Merely repeating “information missing”
does not make that connection. These are candidate anchors for raters; no
automated explanation grade or independent rater approval is provided.

## What the logical check establishes

For the new records, costs and seats are explicitly non-negative integers.
The check varies an unknown cost through 0–101: all values above the budget
are equivalent for eligibility. It varies unknown seats through 0–27: all
larger values are equivalent relative to the recorded seat thresholds. These
representatives cover the outcome classes under the supplied rule. Every
compatible Y11 value leaves A the sole winner; Y12 allows both B and A.
Y11 also has a direct reason independent of enumeration: B's fixed cost 128
already exceeds 100. The check does not decide whether learners understand
that reason, whether advice is persuasive, or whether the task is suitable.

## Cues and remaining decisions

Both new items show one unknown entry but have different keys, so a blanket
“missing means Not enough information” rule fails on Y11. That narrow result
does not establish an unbiased measure. In this pair, missing seats accompany
Supported and missing cost accompanies Not enough information; missingness is
always in B. The pair repeats A/C figures and changes the target plan. Reviewing
these together could teach a rule or invite pattern guessing. Full-bank order,
other field positions, relevant missing seats and irrelevant missing costs
remain to be developed and reviewed.

This family has one key in each answer category. The eight practice drafts
overall have two Supported, three Contradicted and three Not enough information
keys. Full twelve-item advice lists are still unfinished; family key balance
is not advice-quality balance or form equivalence. Eighteen of thirty planned
drafts are present, with twelve items missing. Age, language, burden, feedback,
independent key review and rater training remain pending.

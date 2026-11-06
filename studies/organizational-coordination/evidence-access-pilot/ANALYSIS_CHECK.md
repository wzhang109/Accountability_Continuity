# Synthetic analysis check · 6 November 2026

This is a hand-constructed software fixture, not behavioral evidence. Its
responses were chosen to expose weighting and missingness problems; no effect
size in this note predicts the proposed experiment's results.

From this directory (Python 3 standard library only):

```sh
python assignment.py
python analysis.py
python -m unittest -v test_design_analysis.py
```

`analysis.py` selects four fictional slots from the generated manifest, writes
invented responses and an analysis report under ignored `generated/`, and prints
the summary. It neither recruits reviewers nor reads or sends live responses.

## Define the events before counting

| Draft status | Reviewer passes recommendation | Reviewer returns recommendation |
|---|---|---|
| Incorrect | Missed error | Detected error |
| Correct | Correct acceptance | Unnecessary return |

This classification concerns the recommendation, not simply disagreement with
an AI suggestion to proceed. An incorrect recommendation to hold should also be
returned for correction. Missing decisions are neither passes nor returns.
An omitted response row remains in the assigned denominator through a left join
to the assignment key. A known rendering failure is flagged and its decision
is unusable, not evidence of reviewer failure. An omitted row has unknown
rendering status; it is not automatically counted as a rendering failure.

Explanation missingness is reported separately among usable decisions. It does
not change decision credit or become an explanation score of zero. The fixture
leaves all explanations unscored; the program does not judge free text, establish
comprehension, or infer that an unscored explanation means a reviewer did not check.

## A hand-worked counterexample to pooling

All four slots were assigned three incorrect and three correct recommendations.
Each fraction below is returns / usable decisions of that type.

| Fictional slot | Incorrect drafts: detection | Correct drafts: unnecessary return |
|---|---|---|
| Visible 1 | 2/3 | 1/2 (one decision missing) |
| Visible 2 | 1/1 (two decisions missing) | 0/3 |
| One-click 1 | 1/3 | 0/3 |
| One-click 2 | 1/2 (one decision missing) | 1/2 (one decision missing) |

First average within reviewer, then average reviewers with equal weight, as in
the design draft. Observed detection rates are **5/6 (83.33%)** for visible and
**5/12 (41.67%)** for one-click: a constructed **41.67 percentage-point** difference.
Pooling items would instead give 3/4 versus 2/5, a 35-point difference, because
reviewers with more observed answers receive more weight. Both reviewer-average
unnecessary-return rates are 1/4 (25%); these must be reported alongside detection.

The observed-rate calculation conditions on usable responses, which may itself
be changed by the interface. It is **not an intention-to-treat causal estimate**.
If a reviewer has no usable decisions of a type, the arm's observed reviewer
mean is left undefined, and the number with observations is reported. The code
does not silently remove that reviewer or replace their rate with zero.

For a descriptive sensitivity check, keep all assigned opportunities and let
each missing/unusable decision be either a return or a pass. Detection then lies
between 50% and 83.33% in visible, and 33.33% and 50% in one-click. The contrast's
logical range is **0 to 50 percentage points**. Unnecessary-return contrast bounds
are **−16.67 to +16.67 points**. These are finite-fixture missing-data bounds,
not confidence intervals, model estimates or evidence about real participants.

## Verification and remaining decisions

Six test methods passed: 100 assignment seeds and the original 2/3 boundary;
hand-calculated reviewer means, pooled diagnostics and bounds; omitted rows;
all-missing reviewers and rendering failures; always-pass/always-return behavior;
and rejection of duplicates, unassigned items and invalid decision labels.

Before a real study, specify a primary estimand and missingness policy,
withdrawal/consent handling, renderer diagnostics, blind explanation scoring,
sample size and reviewer-level uncertainty estimation. Repeated tasks are not
independent people. These four invented slots support no significance test.
The current task bank is narrow and the interface itself is not implemented.
Confidence, time cost, delayed learning and downstream rework are not modeled.

AI assisted code, fixture design and documentation. Automated consistency checks
do not replace independent behavioral, methods or ethics review.

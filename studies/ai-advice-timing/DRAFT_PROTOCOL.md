# AI advice timing and later unaided performance

**Operational design draft · September 14, 2026**

Prepared for Wenwen (Celine) Zhang's independent research with substantial AI
assistance. No participants, institutional approval, registration, or study
results exist. The task, counts, age group, and analysis below are concrete
proposals for review, not commitments already made.

## Question and scope

With the same cases and correct-answer feedback, does recording an initial
judgment before prepared AI advice affect performance on new cases without AI
about one week later?

The proposed first feasibility study uses adults and fictional evidence-review
cases. It could establish whether the materials and procedures work. It would
not establish a policy for children, a general measure of judgment, or effects
on professional or organizational capability. The separate
[youth proposal](../../preserving-independent-judgment-in-youth-ai-use.md)
would require adaptation and appropriate partners.

## Intervention and comparisons

Assign participants in equal proportions to three workflows. Use participant
assignment, not switching workflows within a person, because earlier practice
may affect later behavior.

| Arm | Practice sequence |
|---|---|
| Initial Judgment First | Evidence → initial answer and confidence → prepared advice → final answer, confidence, brief reason → feedback |
| AI Advice First | Evidence and the same prepared advice → final answer, confidence, brief reason → feedback |
| No AI | Evidence → answer and confidence → optional review and final confirmation, brief reason → feedback |

Use a common per-case time allowance and the same feedback content and display
rules, while logging actual time. The first arm has an extra required response.
The comparison therefore estimates the effect of the whole assigned workflow,
including effort and commitment; it does not isolate display order alone.
Do not require a hidden initial answer in AI Advice First just to equalize
the measurements, since that would change the intervention.

The sole primary contrast is Initial Judgment First minus AI Advice First on
delayed unaided accuracy. Comparisons of each assisted arm with No AI are
secondary. There is no directional hypothesis that either assisted arm wins.

## Candidate task

Participants read a short fictional program record and classify a claim as
**supported**, **contradicted**, or **not enough information**, using only that
record. Skills include tracking denominators, separating participation from
completion, distinguishing an absent measurement from a negative result, and
avoiding causal conclusions from simple before/after comparisons.

[Example cases and scoring notes](TASK_EXAMPLES.md) make this option concrete.
They are not a validated scale or a full item bank. This task is narrower than
general reasoning. It may be too easy, too dependent on reading proficiency,
or too close to prior statistics training; pretesting must decide.

Prepare parallel case sets before a pilot. Use new surface details at test,
cover the same skills, and keep a separate exploratory set that changes the
type of evidence. A score on similar new items supports a narrower claim than
transfer to a different domain.

## Proposed sequence

Counts below are starting specifications for feasibility review. Use separate
items in every phase. The eight public examples are not a ready-to-administer
version of this sequence.

| Phase | Starting specification | Advice and feedback |
|---|---|---|
| Orientation | Task rules and 3 worked examples | Identical instruction for everyone |
| Baseline | 9 cases before assignment | No AI, no correctness feedback |
| Practice | 24 cases after assignment | Assigned workflow; feedback after final submission |
| Immediate assessment | 12 new cases | No AI; no feedback until delayed testing is complete |
| Delayed assessment | 12 new cases, target 7 days; proposed window 6–9 days | No AI; complete before any further advice |
| Common advice challenge | 12 additional cases after delayed assessment | All arms use the same advice-first interface, 9 correct and 3 wrong recommendations |
| Debrief | Correct misunderstandings; collect acceptability comments | Explain prepared advice and give answer explanations |

The common challenge deliberately gives the former No AI group advice too.
This extends the broad youth proposal's assisted-group challenge: it allows
comparison of prior learning histories under a common current interface. It
does not estimate differences between the original workflows during that
challenge. Keep practice behavior and challenge behavior separate.

The immediate assessment itself creates retrieval practice. All arms receive
it; the estimand is the effect of the full sequence including that common test.
Do not describe the delayed outcome as learning untouched by testing.

## Advice and feedback construction

Use fixed, reviewed advice rather than a live chatbot. Explain to participants
that advice is prepared for the study, may contain errors, and is not an
assessment of a deployed model's accuracy. Do not misrepresent hand-written
advice as live model output.

Propose 18 correct and 6 plausible wrong recommendations during practice.
Create four balanced versions, with every practice item assigned wrong advice
in one version and correct advice in the other three. Balance those versions
across the two assisted arms and across item order. Each version must retain
coverage of all answer categories and skill types among the error cases.
For the common challenge, use the same logic with 9 correct and 3 wrong items
per version, balanced across all three original arms.

Correct and incorrect versions should be similar in length, certainty, and
format. Wrong advice should make a specific interpretable mistake, not simply
look careless. The correct-answer feedback must state the answer, cite the
decisive record, and explain the relevant rule; it should be identical for
everyone on a given item. Prepared advice controls content but does not
reproduce conversational AI use.

## Assignment and masking

After baseline, use concealed computer assignment with equal allocation and
balanced advice versions. A possible implementation blocks on broad baseline
score bands; the exact rule and randomization seed policy must be fixed before
enrollment. Keep assignment distinct from the random order of cases.

Participants can see their interface, so they cannot be blinded to the workflow.
People scoring brief reasons should receive de-identified text without arm or
advice labels. Advice writers should not grade ambiguous answers in their own
favor; two independent reviewers should agree on each answer key before use.
No such external review has yet occurred.

## Outcomes and estimands

| Measure | Definition | Interpretation limit |
|---|---|---|
| Primary delayed accuracy | Correct answers divided by the common delayed item count, scored 0–1 | Performance on this task and delay |
| Immediate unaided accuracy | Same rule on the immediate item set | Separate from performance while advice is available |
| Practice accuracy | Correct final answers, by arm and advice correctness where applicable | Different assistance is available across arms |
| Challenge accuracy | Correct final answers separately on correct- and wrong-advice cases in the common interface | End behavior; agreement alone does not show reasoning |
| Confidence error | Mean of (reported probability final answer is correct − actual correctness)² | Brier score for a correctness forecast, not a full three-class probability score |
| Mean overconfidence | Mean reported correctness probability minus mean correctness | Can conceal offsetting individual errors |
| Reason score | 0 = absent/irrelevant; 1 = relevant fact or rule but incomplete; 2 = decisive evidence linked to a valid conclusion | Exploratory, requires blinded rubric review |
| Burden and usability | Time, completion, delayed return, perceived effort, acceptability | Feasibility outcomes, not cognitive engagement itself |

Ask confidence as “How likely is your answer to be correct?” on a 0–100 scale.
Use the final confidence in all cross-arm comparisons. Initial-to-final changes
are available in Initial Judgment First only. Within that arm, report switches
toward correct advice and away from a correct initial answer under wrong advice,
with explicit denominators.

Do not compare a switch rate in Initial Judgment First with an unobserved
initial decision in AI Advice First. Do not estimate a mediated effect through
engagement merely from time, confidence, record opening, or these revisions.

## Analysis draft

Analyze participants according to assigned arm. The participant, not an item
response, is the unit for the main comparison.

For a later adequately sized study, regress participant delayed accuracy on
arm indicators, baseline accuracy, and any assignment strata; report the
Initial Judgment First versus AI Advice First difference in percentage points
with a 95% interval. Use heteroskedasticity-robust uncertainty at participant
level. Do not treat 12 answers per person as 12 independent participants.

Treat this as a fixed item-bank comparison. Generalization to a population of
items would need an item-sampling design and corresponding analysis. A
predefined item-level mixed model can be a sensitivity analysis after
statistical review, not an automatic solution to a small item pool.

For a confirmatory study, fix the primary contrast and multiplicity plan in
advance. One possible plan leaves that single primary contrast unadjusted and
applies Holm correction to the two secondary assisted-versus-No-AI contrasts.
Report other secondary outcomes as exploratory estimates with their uncertainty.

Do not adjust the primary estimate for practice time, practice success, final
confidence, or other variables affected by assignment. Those may describe
mechanisms but controlling for them changes the question. Examine differences
in prior AI use or baseline skill only as exploratory unless the study is
designed and sized for them.

## Missingness and exclusions

Record consent withdrawal, technical failures, incomplete items, and delayed
non-return separately. Do not exclude someone because they disagree with AI,
do poorly, or fail to show the hoped-for learning pattern.

Prespecify eligibility, duplicate detection, and invalid-session rules before
recruitment. A displayed item intentionally left unanswered may be scored
incorrect under a disclosed rule; an item never displayed due to a technical
failure must be flagged separately. No response threshold has yet been chosen.

Report delayed return and outcome availability by arm. Assigned-arm analysis
among observed outcomes alone does not remove attrition bias. Present that
estimate with a missingness table and bounded-outcome sensitivity analyses,
including extreme 0/1 assumptions for missing delayed outcomes. Any imputation
model needs justified assumptions and advance specification. Separate tests
completed outside the planned delay window; do not quietly discard them.

## Feasibility and sample size

No sample-size claim is justified yet. Begin with supervised task walkthroughs
to identify ambiguity, then use a small feasibility sample to examine completion,
timing, score distributions, reliability, and return rates. This pilot should
not be advertised as a powered test of an effect.

Before a confirmatory study, choose a smallest effect worth detecting with a
partner, justify it in task terms, and calculate precision or power for the
primary participant-level contrast. Include baseline adjustment, attrition,
three-arm allocation, and any recruitment clustering. Do not use a noisy
pilot treatment-effect estimate as the assumed true effect.

Proceed only when answer keys have external review, instructions are understood,
assessments show useful score variation, delayed return is practicable, and a
research partner has reviewed the inference plan. These are review criteria;
numeric thresholds remain to be agreed before collecting pilot data.

## Data and implementation checklist

A minimal case-level record would include:

- anonymous participant ID, assigned arm, advice version, item ID and version;
- phase, order, scheduled and actual delay;
- initial answer/confidence where the interface actually collects them;
- advice label and correctness, final answer/confidence, optional brief reason;
- final correctness, timing, display failures, missingness reason;
- feedback version and whether it was displayed.

Keep identity/contact details separately for scheduling. Do not send participant
responses or identifiers to a live model. Retention, access, compensation,
consent, and withdrawal procedures must be set with the study partner and
appropriate research review before recruitment. The protocol does not authorize
collection of human-subject data.

## Evidence informing this draft

- [Gajos and Mamykina (2022), author summary](https://www.eecs.harvard.edu/~kgajos/papers/2022/gajos2022people.shtml):
  recommendation-plus-explanation designs improved immediate choices without
  showing learning gains in separate experiments; explanation-only assistance
  improved both. This motivates separate performance and learning outcomes,
  not a claim that one order has been proven superior.
- [Fogliato et al. (2022), paper abstract](https://arxiv.org/abs/2205.09696):
  in a study of veterinary radiologists, recording a provisional decision
  reduced agreement with correct as well as incorrect AI advice. This motivates
  distinguishing appropriate response from disagreement.
- [Buçinca, Malaya, and Gajos (2021), author summary](https://www.eecs.harvard.edu/~kgajos/papers/2021/bucinca2021trust.shtml):
  cognitive-forcing interventions reduced overreliance relative to simpler
  interfaces but could receive less favorable user ratings. This motivates
  measuring burden and acceptability alongside accuracy.

These source links support the narrow design motivations above. They do not
validate this task, the proposed seven-day delay, the case counts, or a causal
mechanism. Those are design choices requiring further review.

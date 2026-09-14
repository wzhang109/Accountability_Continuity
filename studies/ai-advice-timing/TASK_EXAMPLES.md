# Fictional evidence-review task examples

**Development examples · September 14, 2026**

All organizations, records, and quantities below are invented. These examples
were drafted with AI assistance for task selection and discussion. They have
not been reviewed by independent graders or tested with participants. They are
not survey findings, model outputs from a live system, or an assessment of
general intelligence.

Use only the supplied record. Classify the claim as:

- **Supported:** the record establishes the claim.
- **Contradicted:** the record establishes that the claim is false.
- **Not enough information:** the record does not establish either conclusion.

Absence of evidence is not automatically evidence against a claim. Claims
about measured counts differ from claims about an unmeasured effect.

Each item below includes an answer key and a correct and an incorrect prepared
recommendation. Only one recommendation version would be shown in an assisted
practice trial. The final feedback would be the same regardless of that
version. Do not expose the answer key alongside advice during a trial.

## E01 — Participation rate versus count

**Record:** Center A invited 300 people, of whom 60 attended. Center B invited
800 people, of whom 120 attended.

**Claim:** A larger proportion of invited people attended at Center A.

**Key:** Supported.

**Correct advice:** Supported. At A, 60 of 300 attended; at B, 120 of 800
attended. Comparing these proportions gives A the higher attendance rate.

**Wrong advice:** Contradicted. A had 60 attendees and B had 120. Comparing
these attendance totals gives B the higher attendance rate.

**Shared feedback:** Supported. A's rate is 20% and B's is 15%. B has more
attendees but a lower rate among those invited.

**Skill:** Choose the denominator that matches the claim.

## E02 — Registration is not completion

**Record:** A course registered 100 learners. Sixty completed all required
sessions. Twenty attended some sessions but did not complete the course.
Twenty attended none.

**Claim:** Eighty learners completed the course.

**Key:** Contradicted.

**Correct advice:** Contradicted. The record identifies 60 completers. The
20 partial attendees are a separate group who did not complete the course.

**Wrong advice:** Supported. Sixty learners finished all sessions and another
20 participated. Combining both groups gives 80 course completers.

**Shared feedback:** Contradicted. Eighty attended at least one session, but
only 60 completed all required sessions. The claim changes the outcome definition.

**Skill:** Keep the recorded category consistent.

## E03 — Change over time is not an identified effect

**Record:** Average scores among the same 40 learners rose from 50 before a
workshop to 65 afterward. No comparison group was observed. The record does
not describe other changes during that period.

**Claim:** The workshop caused the entire 15-point increase.

**Key:** Not enough information.

**Correct advice:** Not enough information. Scores rose by 15 points, but
this before-and-after record does not isolate the workshop from other influences.

**Wrong advice:** Supported. The same learners scored 50 before and 65 after
the workshop, so the 15-point difference measures the workshop's effect.

**Shared feedback:** Not enough information. The increase is observed; its
cause is not isolated. The record neither establishes the stated causal effect
nor proves that the workshop had no effect.

**Skill:** Separate observed change from a causal claim.

## E04 — Combining mutually exclusive categories

**Record:** Of 20 completed interviews, 8 were conducted by phone, 7 in person,
and 5 by video. Each interview used exactly one of these methods.

**Claim:** Seventy-five percent of interviews were conducted by phone or in person.

**Key:** Supported.

**Correct advice:** Supported. Phone and in-person interviews are separate
categories. Their combined count is 15 out of the 20 interviews.

**Wrong advice:** Contradicted. Phone interviews are 8 of 20 and in-person
interviews are 7 of 20. Averaging those percentages gives 37.5%, not 75%.

**Shared feedback:** Supported. Add the non-overlapping counts: (8+7)/20=75%.
Averaging the two category percentages answers a different question.

**Skill:** Match aggregation to the stated categories.

## E05 — Count is not percentage

**Record:** A library offered 120 appointment slots. Thirty slots remained
unbooked at the booking deadline.

**Claim:** Thirty percent of the available slots remained unbooked.

**Key:** Contradicted.

**Correct advice:** Contradicted. The unbooked count is 30, but the total is
120. The proportion is 30 divided by 120.

**Wrong advice:** Supported. The record lists 30 unbooked slots at the
deadline, so the reported unbooked share is 30 percent.

**Shared feedback:** Contradicted. Thirty out of 120 is 25%, not 30%.
A count only equals a percentage numerically when the denominator is 100.

**Skill:** Convert counts to rates.

## E06 — An unmeasured outcome

**Record:** A program measured caregiver stress before and after six weeks.
Average reported stress declined. No measures of children's language skills
were collected.

**Claim:** Children's language skills improved during those six weeks.

**Key:** Not enough information.

**Correct advice:** Not enough information. The observed change concerns
caregiver stress. The record contains no children's language assessment.

**Wrong advice:** Contradicted. The program found no improvement in children's
language skills because it recorded only a change in caregiver stress.

**Shared feedback:** Not enough information. An outcome that was not measured
cannot be classified as improved or unchanged from this record.

**Skill:** Distinguish missing measurement from a negative finding.

## E07 — Assignment is an observed procedure

**Record:** Forty registered participants drew one of 40 identical folded
tickets. Twenty tickets assigned Room A, and twenty assigned Room B. Every
ticket was drawn exactly once.

**Claim:** Twenty participants were assigned to each room.

**Key:** Supported.

**Correct advice:** Supported. All 40 tickets were drawn once, and each room
appeared on exactly 20 tickets. Assignment counts are therefore equal.

**Wrong advice:** Not enough information. A lottery does not guarantee equal
outcomes, so the record cannot establish equal numbers assigned to the rooms.

**Shared feedback:** Supported. The question concerns the recorded assignment
procedure and counts, not later attendance or outcomes.

**Skill:** Identify exactly which claim is being evaluated.

## E08 — Weighted versus unweighted aggregation

**Record:** In one week, Branch A processed 100 applications and approved 60.
Branch B processed 50 applications and approved 15. The branches processed
different applications.

**Claim:** Across both branches together, 45% of applications were approved.

**Key:** Contradicted.

**Correct advice:** Contradicted. Together the branches approved 75 of 150
applications. The pooled rate uses combined counts, not equal branch weights.

**Wrong advice:** Supported. Branch A approved 60% and Branch B approved 30%.
The average of these two rates is the overall approval rate of 45%.

**Shared feedback:** Contradicted. The pooled approval rate is 75/150=50%.
The 45% calculation gives the smaller branch the same weight as the larger one.

**Skill:** Aggregate across groups with unequal denominators.

## Review rubric and development decisions

For a brief reason, a provisional rubric is:

| Score | Criterion |
|---|---|
| 0 | No relevant explanation, repeats the recommendation, or relies on an irrelevant fact |
| 1 | Identifies a relevant fact or rule but does not correctly connect it to the claim |
| 2 | Uses decisive evidence and a valid rule to justify the classification |

Score the selected answer separately from the reason. Two reviewers should
resolve ambiguity and check the advice variants before use. The examples have
been checked for internal arithmetic and intended logic during drafting; this
does not establish grader agreement or validity with participants.

There are three Supported, three Contradicted, and two Not enough information
keys here. That is an example set, not the balanced item bank required by the
[protocol](DRAFT_PROTOCOL.md). Some wrong recommendations may be too obvious;
their plausibility, reading burden, and comparable wording require pretesting.

Before constructing parallel assessments, decide:

1. Whether learning these evidence-review skills is the intended construct.
2. Whether prior statistics knowledge or language proficiency dominates scores.
3. Whether training transfers to new records rather than memorized wording.
4. Whether advice errors can be distributed across skills and answer categories
   without changing difficulty unequally between study arms.
5. Whether the broader item bank can avoid ceiling and floor effects.

Do not claim that these examples already answer those questions.

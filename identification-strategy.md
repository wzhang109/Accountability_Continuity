# Accountability Continuity Index — Identification Strategy

Status: first formal pass, drafted Week 5 (2026-07-31). Not yet tested against real data.
This document consolidates the design decisions from the Week 5 log entry into a standalone reference, so `/research-log.md` stays a dated narrative and this stays the thing that gets revised as the design changes.

## Unit of analysis

**Decision-type × organization × time period (quarter or year).**

Not organization alone. A "decision-type" is a recurring class of decisions sharing the same underlying judgment domain within an organization — e.g., loan-approval decisions at a bank, triage decisions in an emergency department, code-merge decisions in an engineering org. Accountability continuity is a property of who bears responsibility for a *kind* of decision over time, not a property of the organization as a whole. The same company can score high AC in one decision-type and near-zero in another.

## Treatment definition

**Staggered adoption of an AI/agentic tool for a given decision-type**, coded as an ordinal intensity variable rather than binary:

1. Advisory only — AI produces a recommendation; a human makes and owns the decision.
2. Co-pilot with sign-off — AI produces a decision; a human reviews and must affirmatively approve before it takes effect.
3. Autonomous — AI executes/finalizes the decision without required human sign-off.

The treatment threshold for this project's purposes is the move from (2) to (3) for a given decision-type — that's the point accountability structurally leaves the loop, not merely the point AI enters it. Binary adoption coding would throw away the variation that matters most (how much discretion transfers), so intensity is the primary treatment variable, with the (2)→(3) threshold as the headline event for an event-study design if one is warranted later.

## Outcome variables

- Error/reversal rates — decisions later overturned or corrected.
- Correction speed — time between decision and correction being caught/made.
- Dispute rates — formal complaints or appeals tied to the decision-type.

**Explicit scope note:** these are behavioral-gap proxies, not existential-gap measures. The Index cannot observe whether anyone "bears" a decision in the philosophical sense developed in the Track 1 literature — only whether the accountability structure around a decision-type produces measurably different downstream outcomes once continuity is reduced. This is consistent with treating AC(O,t) as a hard constraint (per the two-axis framework, Week 4) rather than something these variables are meant to prove or disprove: they test what happens when the constraint is relaxed, not whether the constraint is philosophically "real."

## AC-score coding criteria

Three operational indicators, scored 0–2 (low/medium/high) per decision-type × organization × year cell:

1. **Primary-evidence engagement** — does the decision-maker engage the raw, case-specific evidence, or only a summary/recommendation?
2. **Real discretion** — is override of the AI recommendation observed at non-trivial rates and without penalty, not merely formally permitted?
3. **Repeated exposure** — does the same decision-maker handle repeat instances of this decision-type over time, allowing feedback to accumulate on one continuous "mind-stream" (the causal-continuity concept from the Track 1 lit review, applied institutionally rather than metaphysically)?

This rubric is structurally the same shape as the State Support Index rubric used on the parallel China/WTO project (dimension scores × sources, coder_id, review_status) — that consistency is deliberate, not coincidental, and should be kept that way as both projects mature.

**Open risk, not yet resolved:** whether primary-evidence engagement and real discretion are actually separable in real data, or whether they collapse into one underlying thing in practice.

## Candidate data sources

No organizational partners are secured yet — listing categories, not named partnerships, to avoid overstating progress:

1. Public court/regulatory records where AI-assisted decisions are being formally challenged (EEOC/CFPB-adjacent algorithmic hiring or lending complaints).
2. Published clinical-decision-support override-rate audits (several hospital systems publish these).
3. Outreach contacts from Week 4 (researchers in the organizational-AI space) as possible access points — though that outreach was originally about framework feedback, not data access, and the two purposes shouldn't be conflated.

## Decisions log

- Treatment is ordinal (advisory / co-pilot / autonomous), not binary.
- Outcome variables are explicitly scoped as behavioral-gap proxies only.

## Next

Pressure-test whether the three AC-score indicators are actually separable in real data — the open risk above.

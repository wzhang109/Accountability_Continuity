# Accountability Continuity Research Log
**Researcher:** Wenwen (Celine) Zhang
**Project:** Accountability Continuity — An Institutional Framework for Human-Agentic Task Allocation
**Status:** Independent research, in progress — developed alongside a parallel project on compute governance (not public)

## The problem

When an organization starts using AI for a task, the person who signs off
usually stays the same. What changes is what signing off consists of.

A concrete version: a hospital adopts AI-assisted imaging. The rule is that the
model produces a reading and a radiologist confirms it. In month one the
radiologist looks at the scan and occasionally overrides. A year later the
radiologist reads the model's summary and confirms. The signature is the same.
The liability is the same. The judgment has moved.

The measurement problem is that these two states are hard to tell apart from
the outside. The reviewer's disagreement rate with the model drifts toward zero
in both — once because the model got better, once because the reviewer stopped
checking. `simulations/` first contained a constructive counterexample showing
that the two can be exactly observationally equivalent under a stated,
illustrative model. The current
[`override_identification_v2`](simulations/override_identification_v2/) study
makes the analytic identification result primary, adds constrained likelihood
estimation, independent measurement channels, repeated Monte Carlo evaluation,
and explicit calibration-drift checks.

## The question

Which decisions require a human who could have decided otherwise and who bears
the consequence — and how would you know whether a given process still has one?

The second half is the harder half, and it is what this project is mainly about.

## What "could have decided otherwise" requires

Three conditions, each necessary and none sufficient on its own:

| Condition | What it requires | Observable proxy |
|---|---|---|
| **Grounds** | an independent basis for disagreeing | does the reviewer open the primary record, or only the summary? |
| **Standing** | disagreement is affordable | override rate is not near zero; overrides do not trigger penalty or delay |
| **Discrimination** | the ability to tell when to disagree | volume of same-class cases seen, with feedback |

These are an adaptation of a long-standing decomposition of responsible agency —
roughly, an act is blameworthy unless done in ignorance or under compulsion
(Aristotle, *NE* III), with competence added as the modern third condition.

They are claimed as **necessary, not sufficient**: someone can satisfy all three
and still rubber-stamp. The claim is only that failing any one of them means the
sign-off is not a judgment.

## Why not go through consciousness

An obvious alternative framing asks whether AI systems have moral status or
subjective experience. This project deliberately does not go that way. That
question faces an explanatory barrier that evidence can narrow but not close
(Nagel 1974; Chalmers; Block; Butlin, Long et al. 2023), which makes it a poor
foundation for institutional policy that has to be written now.

Accountability continuity is a weaker and more tractable criterion: whether the
same subject who errs also bears the consequence and carries it into the next
decision. It does not require resolving the harder question.

## Why this sits across three literatures

- **Philosophy of mind and AI welfare research** (Nagel 1974; Chalmers; Block; Parfit 1984; Butlin, Long et al. 2023; Long, Sebo, Butlin, Plunkett et al. 2026) supplies the grounding for why the existential-gap question is a poor foundation for policy, and why a weaker claim — causal/psychological continuity of a mind-stream, not a metaphysical self — is defensible and sufficient for the accountability-continuity criterion.
- **Organizational behavior and management science treatments of agentic AI** (Liu 2026; Stanford HAI / Google DeepMind's Organizational AI Research program) supply empirical and theoretical groundwork on how agent collectives coordinate and where human accountability is currently assumed to sit — often as an unexamined premise this project treats as the central object of study, not a background fact.
- **Applied microeconometrics for policy evaluation** supplies the identification strategy. The author's prior work uses event-study panel designs with differential treatment exposure — a common event date, with units differing in exposure intensity — applied to South Korea's 1987 democratic transition and sectoral state coordination legacies. This project extends that lineage to a harder setting: staggered adoption, where organizations adopt at different times, combined with an ordinal rather than binary treatment. That combination requires estimators built for non-binary and potentially non-absorbing treatments (de Chaisemartin & D'Haultfœuille) rather than the standard binary staggered-DiD toolkit.

The philosophy and organizational-behavior literatures currently do not cite each other on this question. The contribution of this project is treating that gap as the thing to be filled, using the economics toolkit as the bridge — not developing a purely philosophical or purely qualitative argument.

## Repository structure

```
/research-log.md          -- weekly dated entries (primary record)
/proposal/                -- formal model, identification strategy, index construction
/simulations/sim_identification.py
                           -- initial constructive counterexample
/simulations/override_identification_v2/
                           -- current identification study, results, tests,
                              figures, and plain-language guide

Planned:
/lit-review/              -- two tracks: philosophy of mind; organizational behavior
/framework-drafts/
/expert-conversations/
```
## Relationship to other projects

This project developed alongside a parallel line of work on institutional resource allocation under capacity constraints (not public). It is best understood as a zoom-out from that work rather than a separate direction: who should hold authority and bear responsibility when capacity or decision rights are reallocated — whether by policy or
by automation — is the general question, and both projects are instances of it.

The measurement approach comes from an earlier applied-economics project on state coordination and sectoral policy legacies, publicly documented here:
**[state-coordination](https://github.com/wzhang109/state-coordination)** — source-traceable policy-text measurement, rubric-based coding with human review, index construction, and an event-study workflow.

The shared inheritance is the measurement design — dimensions fixed before outcomes are examined, every score traceable to a primary passage, ambiguous cases routed to human review rather than machine finalization, and a rubric schema (`coder_id`, `confidence`, `review_status`) kept deliberately consistent across projects.

The identification strategies differ and should not be conflated. The earlier project uses a common event date with units differing in exposure intensity. This project faces staggered adoption timing and an ordinal treatment, which is why it requires estimators built for non-binary, potentially non-absorbing treatments rather than the standard binary staggered-DiD toolkit.

## A note on scope and confidence

This log records real-time research judgment, including reversals and open disagreements — for example, an active internal debate (documented in the log) about whether markers-based AI consciousness research can ever produce evidence that tracks the underlying property it targets, given the absence of an evolutionary anchor that licenses this kind of inference in animal welfare research. Claims in early entries should be read as working hypotheses, not settled conclusions, unless a later entry states they have been tested.

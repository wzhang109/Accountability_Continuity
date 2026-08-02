# Accountability Continuity Research Log
**Researcher:** Wenwen (Celine) Zhang
**Project:** Accountability Continuity — An Institutional Framework for Human-Agentic Task Allocation
**Status:** Independent research, in progress — developed alongside a parallel project on compute governance (not public)

## Purpose

This repository documents ongoing development of a research program studying a specific institutional design question: as AI systems and agent collectives become more capable, which decisions require a continuous, accountable human subject to remain in the decision loop — and which do not?

The project deliberately does not try to resolve whether AI systems have consciousness, moral status, or subjective experience. That question (the "existential gap") faces a well-documented explanatory barrier in philosophy of mind — evidence can narrow uncertainty but cannot, even in principle, resolve it with the kind of confidence institutional policy requires. Instead, this project develops and tests an alternative, empirically tractable criterion: **accountability continuity** — whether the same subject who errs also bears the consequence and carries it into the next decision. This question does not depend on resolving consciousness, and it can be operationalized, measured, and tested using standard applied-economics methods.

## Core research question

Given a decision or task that is increasingly delegable to AI or agent collectives: which decisions require a continuous human subject who bears the consequences of error and carries them forward into future judgment — and which do not? Can this requirement be operationalized precisely enough to construct a measurable **Accountability Continuity Index**, and tested empirically against organizational and policy outcomes (error rates, correction speed, dispute/litigation rates)?

## Why this sits across three literatures

- **Philosophy of mind and AI welfare research** (Nagel 1974; Chalmers; Block; Parfit 1984; Butlin, Long et al. 2023; Long, Sebo, Butlin, Plunkett et al. 2026) supplies the grounding for why the existential-gap question is a poor foundation for policy, and why a weaker claim — causal/psychological continuity of a mind-stream, not a metaphysical self — is defensible and sufficient for the accountability-continuity criterion.
- **Organizational behavior and management science treatments of agentic AI** (Liu 2026; Stanford HAI / Google DeepMind's Organizational AI Research program) supply empirical and theoretical groundwork on how agent collectives coordinate and where human accountability is currently assumed to sit — often as an unexamined premise this project treats as the central object of study, not a background fact.
- **Applied microeconometrics for policy evaluation** supplies the identification strategy. The author's prior work uses event-study panel designs with differential treatment exposure — a common event date, with units differing in exposure intensity — applied to South Korea's 1987 democratic transition and sectoral state coordination legacies. This project extends that lineage to a harder setting: staggered adoption, where organizations adopt at different times, combined with an ordinal rather than binary treatment. That combination requires estimators built for non-binary and potentially non-absorbing treatments (de Chaisemartin & D'Haultfœuille) rather than the standard binary staggered-DiD toolkit.

The philosophy and organizational-behavior literatures currently do not cite each other on this question. The contribution of this project is treating that gap as the thing to be filled, using the economics toolkit as the bridge — not developing a purely philosophical or purely qualitative argument.

## Repository structure

```
/research-log.md          -- weekly dated entries (primary record)
/proposal/                -- formal model, identification strategy, index construction

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

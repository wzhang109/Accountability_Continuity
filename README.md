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
/proposal/                -- formal model, identification strategy, index construction plan

Planned, not yet populated:
/lit-review/              -- two tracks: (1) philosophy of mind / AI welfare,
                                         (2) organizational behavior/management science
/framework-drafts/        -- working drafts of the two-axis framework and formal model
/expert-conversations/    -- summarized notes from conversations with researchers
```

This project uses the same staggered-adoption panel methodology developed in an earlier applied economics project on South Korea's 1987 democratic transition and sectoral state coordination legacies. See that repository ("State Coordination Reproducibility Demo") for the shared methodological lineage.

## A note on scope and confidence

This log records real-time research judgment, including reversals and open disagreements — for example, an active internal debate (documented in the log) about whether markers-based AI consciousness research can ever produce evidence that tracks the underlying property it targets, given the absence of an evolutionary anchor that licenses this kind of inference in animal welfare research. Claims in early entries should be read as working hypotheses, not settled conclusions, unless a later entry states they have been tested.

# The Two-Axis Framework

Status: first formal pass, drafted Week 4 (2026-07-16/17). Consolidated from the research log into a standalone reference.

## Starting point: Liu (2026)

Liu (2026), "The Organizational Behavior of Agentic AI," argues agent collectives resemble human organizations functionally (differentiation, coordination, routines) but are sustained by context architecture rather than motivation, identity, trust, or moral accountability. Liu formalizes organizational choice around a value function V(O,T): the payoff to an organizational form O for a task T, driven centrally by *contextual transaction cost* — the cost of maintaining shared context, verification, and coordination across human and agent participants.

Two observations on Liu's own examples motivated this project's extension:

1. Liu's examples (a lawyer remaining accountable for AI-assisted advice; an engineer remaining accountable for AI-assisted deployment) show accountability sitting at multiple points across a workflow, not only at "which goal to pursue." This corrected an earlier, too-narrow framing of this project that treated accountability as purely an upstream, goal-selection question.
2. Liu's central distinction rests on an unexamined premise — that agent collectives "do not experience responsibility as a moral burden" — stated, not argued for. That premise is precisely this project's object of study, not a fact Liu is entitled to assume. This reframes the accountability-relevant portion of the organizational-behavior literature as *downstream of* an unresolved philosophy-of-mind question (see `/lit-review/track-1-philosophy-of-mind-ai-welfare.md`), not a parallel, independent literature.

## The framework

Cross **coordination cost** (Liu's contextual transaction cost) with **accountability requirement** (this project's contribution) to produce a four-quadrant map:

| | Low accountability requirement | High accountability requirement |
|---|---|---|
| **Low coordination cost** | Agent-native organization | Designed human-agent interface, accountability-gated |
| **High coordination cost** | Human-led judgment, or targeted agent tooling | Human-led judgment (default) |

The two-by-two is a starting map, not a finished model — it hasn't been tested against real organizational cases yet. Its main current function is to state precisely what the accountability requirement axis is doing that Liu's original one-axis account doesn't capture.

## The formal extension

Extend Liu's V(O,T) with accountability continuity AC(O,t) as a **hard constraint**, not a tradeable cost, for tasks requiring it:

> V(O,T) is only an admissible choice if AC(O,t) ≥ the task's required threshold; otherwise O is excluded from the choice set regardless of its value on V.

Reasoning: institutions that already require accountability have, by definition, decided efficiency should not be traded against it. Treating AC as a soft cost inside V would let a large enough efficiency gain buy down an accountability requirement that the institution itself has already decided is non-negotiable — which misdescribes how these institutions actually reason.

## Open extension: taste, one level up

"Taste" (see `/essays/the-gap-that-cant-close.md`), originally defined only over outputs, plausibly also operates one level up — over which questions or directions are worth pursuing, and whether a candidate answer genuinely fits one's own accumulated judgment rather than merely sounding plausible. Flagged explicitly as a new hypothesis extending, not restating, the earlier argument — not yet tested against likely objections, e.g. whether the much longer feedback delay in direction-setting breaks the taste-formation loop the same way it operates at the output level.

## Status

First formal pass only. Next steps: test the four-quadrant map against 2-3 real organizational cases; formalize the AC(O,t) threshold function once the Accountability Continuity Index (`/proposal/identification-strategy.md`) produces real scored data to calibrate against.

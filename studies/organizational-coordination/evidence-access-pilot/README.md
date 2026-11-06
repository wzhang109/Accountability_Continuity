# When does easier access to evidence change a review decision?

Design draft · 5 November 2026 · AI-assisted; investigator review pending.

A reviewer inherits an AI-drafted recommendation and must decide whether to pass it on or return it for correction. Does removing one navigation step help the reviewer distinguish supported from unsupported recommendations? This is one testable question within the [organizational coordination branch](../README.md).

## A comparison with a decision attached

Randomly assign reviewers to one interface for the session. Both interfaces show the same recommendation, source title, source location and decision options. In one, the relevant passage is already visible; in the other, one click reveals the identical passage. Both allow access to the full document. Keep passage selection, viewport size, task order distribution and time allowance comparable. Record rendering failures. Use fictional cases and balance correct and incorrect recommendations across conditions.

The primary contrast is the difference between arms in the proportion of incorrect recommendations correctly returned, averaged first within reviewer. Report alongside it the proportion of correct recommendations unnecessarily returned. More returns of both types would suggest a response shift, not necessarily better discrimination. A displayed passage also changes salience: this contrast identifies the effect of the interface package, not the isolated cost of a click.

## What could distinguish the explanations?

- **Easier checking:** more erroneous recommendations are caught and reviewers cite the decisive fact, without a comparable rise in unnecessary returns.
- **Borrowed credibility:** a prominent source makes a recommendation look vetted. Unsupported recommendations are accepted more often, including when the passage contradicts the draft.
- **Work transferred downstream:** first reviewers finish sooner, but recipients must reopen cases. Testing this requires an actual second reviewer and linked rework records; the single-reviewer comparison cannot answer it.

Do not count an automatically visible passage as a source check, or a click as comprehension. Collect the decision first, then ask for the decisive fact in both arms; score it without seeing interface assignment. This is a proposed comparison, not a registered or completed study.

## Reproducible design checks

The [assignment check](DESIGN_CHECK.md) and [Python generator](assignment.py) turn
this proposal into a checkable fictional manifest. They do not run an experiment
or collect responses. See the [matched walkthrough pair](case-pair.md) for the
original wording and scoring problem.

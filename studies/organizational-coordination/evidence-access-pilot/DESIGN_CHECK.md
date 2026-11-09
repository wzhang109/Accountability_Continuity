# Executable assignment check · 6 November 2026

Run with Python 3 standard library only, from this directory:

```sh
python assignment.py
```

The command creates 24 **fictional design slots**, not recruited reviewers,
and 144 task presentations in ignored `generated/`. Separate files contain
allocation, displayable task content, the scoring key, and balance checks.
No responses, identifiers or contact details are collected. Do not serve the
answer key or whole assignment bundle to participants in a future interface.

There are six fictional rule families: release, training access, invoice
routing, equipment dispatch, archive publication and stock transfer. Each slot
sees one version of each family, three valid and three invalid recommendations,
and three recommendations to proceed and three to hold. Thus blindly rejecting
every recommendation is distinguishable from correcting errors. The wording
always asks whether to pass **the recommendation**, not whether to release the
underlying file; this avoids ambiguity when an AI recommendation to hold is wrong.

In each interface there are 12 slots. Each family × validity cell and each
position × validity cell has six presentations per interface. Whole-session
interface assignments are shuffled within complete blocks; order uses cyclic
rotations of a shuffled family list. Each slot sees just one variant of a family.
The November 9 correction also crosses recommendation direction with validity:
each family × recommendation × validity cell has three presentations per arm.
Every slot now has both eligible and ineligible underlying records. Within each
arm, six slots have two eligible records and six have four, for 36 of each
disposition overall. The former formula accidentally made the underlying
disposition constant within a slot. All six rules now explicitly require the
specified action when their conditions hold and require holding otherwise;
this makes incorrect hold recommendations scoreable from the displayed rule.

The same seed reproduces the manifest. A different seed changes ordering and
slot assignment, not the rule content.

## What this verifies, and what it leaves open

Checks passed for seeds 0–99 and the default seed: 24 unique slots, 144 unique presentations,
matched task/key IDs, balanced cells and no answer fields in task records.
These counts are engineering checks, not a sample-size or power justification.
Exact balance depends on completing whole blocks; attrition would break it.

This is a small draft bank of simple threshold tasks. Names differ, but most
reasoning remains structurally similar. It is not yet a realistic research-review
task set, a validated instrument, or an executable participant interface. It
does not check viewport equality, actual click effort, perceived credibility,
explanation quality, learning or downstream rework. A programmer could inspect
the public answer key: future deployment needs a separate private delivery layer.

Before recruitment, obtain independent rule/key and behavioral review, test
wording and salience, add substantively different reasoning tasks, and settle
ethics, sample size, analysis and missing-data rules. AI assisted this code and
documentation; researcher and independent methodological review remain pending.

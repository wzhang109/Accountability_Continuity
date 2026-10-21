# Accountability Continuity

**Wenwen (Celine) Zhang · Independent research in progress**

As more work is delegated to AI, do the people making or reviewing decisions
learn what happened afterward, have the ability to respond, and carry that
experience into later decisions and organizational practice?

The project approaches this concern through a synthetic measurement model,
an unimplemented human-learning study design, and an initial public-document
pilot tracing reported issues and organizational responses. It also preserves
earlier philosophical exploration. There are no recruited participants, private
organizational records, or original field-study results.

A related question comes before measurement: who defines what a good outcome
means, whose experience counts, and can that definition change in light of its
consequences? The [reflection on purpose and judgment](docs/purpose-judgment-and-accountability.md)
explains this motivation without treating it as an established result.

## Start here

| Material | What it provides |
|---|---|
| [Youth feasibility materials October 19](studies/youth-advice-workflow/README.md) | A separate proposed 15–17 study protocol, 22 fictional task drafts, scoring boundaries and a proposed workflow; no participants |
| [Research status and contributions](RESEARCH_STATUS.md) | Completed work, assumptions, proposals, and the role of AI assistance |
| [What counts as good when an organization uses AI](docs/purpose-judgment-and-accountability.md) | A philosophical reflection on purposes, measures, and revising judgment through experience |
| [October 8 human-support response pathway](studies/organizational-feedback/pathways/govuk-human-handoff-2026-10-08/README.md) | One existing issue followed through public records; purpose, approval and outcome evidence kept separate, with unresolved links |
| [October 1 organizational evidence pilot](studies/organizational-feedback/README.md) | Five source-linked entries from two public-sector programs; implementation, plans, and unknowns kept separate |
| [Latest research progress in plain Chinese](docs/progress-2026-10-19.zh-CN.md) | The current question, this update, and what can and cannot be concluded |
| [Plain-language model walkthrough, English and Chinese](simulations/override_identification_v2/PLAIN_LANGUAGE_GUIDE.md) | The equation, a worked example, and what each measurement can establish |
| [Simulation methods and results](simulations/override_identification_v2/README.md) | Model specification, code, uncertainty checks, and synthetic results |
| [Methods verification, September 2026](simulations/override_identification_v2/VERIFICATION_2026-09-14.md) | Checks performed, a numerical correction, and remaining limitations |
| [Research program](RESEARCH_PROGRAM.md) | How the measurement and learning questions fit together |
| [Operational study draft](studies/ai-advice-timing/DRAFT_PROTOCOL.md) | Three workflows, common assessments, outcomes, and analysis decisions |
| [Illustrative task examples](studies/ai-advice-timing/TASK_EXAMPLES.md) | Fictional evidence-review cases for discussing task suitability |
| [Youth study proposal](preserving-independent-judgment-in-youth-ai-use.md) | A separate application that requires appropriate research partners |
| [Focused literature review](ai-advice-timing-and-human-learning.md) | Earlier reading on advice timing and learning; not a systematic review |

## What the simulation establishes

Under the stated model, improving AI accuracy and declining human review can
produce exactly the same expected override path. The equality is constructed
algebraically. Repeated simulations then examine estimation error after adding
an accuracy audit and a calibrated process measure.

That does not show that people in real organizations are disengaging. The
additional measurements help only under assumptions about reviewer behavior,
sampling, and calibration. Opening a record, disagreeing with AI, or recording
an initial answer is not itself proof of careful judgment.

The proposed learning studies ask a different question. The existing adult
operational draft compares **Initial Judgment First**, **AI Advice First**, and
**No AI** with common assessments. The separate youth feasibility version uses
6 baseline and 12 practice items, 8 delayed unaided items and 4 later challenge
items. No-AI remains unaided in that challenge, so it is not a common-current-
interface comparison of all three arms. Neither workflow is assumed to be
better. There are no recruited participants or registered or completed study.

The organizational pilot asks what published records establish about the route
from an issue to a response. Public reporting is selective; entries are not
independent cases, missing links are not absent practices, and no causal effect
or organizational accountability score is estimated. The
[measurement clarification](studies/organizational-feedback/MEASUREMENT_NOTES.md)
also explains which early assumptions have been revised.

## Research context

My background is in development economics and public policy. A recurring
interest is how people's environments shape their opportunities to learn and
develop. Field research, institutional questions, and AI-assisted work led me
to explore different parts of that problem; this was not a single plan fixed
from the beginning.

State Coordination is a separate, ongoing line of work on constructing
source-based coordination measures from Chinese policy texts. It is not a
validated theory, and it should not be conflated with my Korean economic
research experience. Neither project validates the other.

## Earlier exploratory writing

The [research log](research-log.md), [philosophical essay](the-gap-that-cant-close.md),
and earlier framework and identification notes preserve the development of the
ideas. They include conceptual claims and proposed methods that have not been
empirically established. The current [status note](RESEARCH_STATUS.md) governs
how the work should be described today. In particular, this repository does
not establish a new theory of responsibility, an uncited gap between whole
literatures, or a completed organizational causal study.

## Contributions and collaboration

The problem selection and research motivation are mine. AI tools contributed
substantially to the design, Python implementation, debugging, and writing. I
am still learning the technical details; automated checks do not substitute
for independent methodological review. See the [contribution statement](RESEARCH_STATUS.md#contributions-and-review).

I welcome discussion of measurement validity, feasible learning tasks, and
research partnerships. The current materials are research tools and working
proposals.

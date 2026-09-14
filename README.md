# Accountability Continuity

**Wenwen (Celine) Zhang · Independent research in progress**

When a person still signs off on an AI-assisted decision, what can we learn
about the review and judgment behind that signature?

This project examines that measurement question and a related learning
question: how does the order of AI advice affect what people can later do on
their own? The repository contains a mathematical example, synthetic-data
simulations, exploratory essays, and study proposals. It contains no evidence
collected from people or organizations for these studies.

## Start here

| Material | What it provides |
|---|---|
| [Research status and contributions](RESEARCH_STATUS.md) | Completed work, assumptions, proposals, and the role of AI assistance |
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

The proposed experiment asks a different question. It compares **Initial
Judgment First**, **AI Advice First**, and **No AI**, with the same outcome
feedback, followed by common unaided assessments. Neither assisted workflow
is assumed to be better. No participants have been recruited, and this is not
a registered or completed experiment.

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

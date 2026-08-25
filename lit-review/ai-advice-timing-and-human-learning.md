# Focused Literature Review: AI Advice Timing and Human Learning

**Date:** August 22, 2026  
**Purpose:** Assess whether the proposed first study has already been done and identify the narrowest defensible contribution.

## Bottom Line

The study is worth pursuing, but its contribution needs to be stated narrowly.

Prior work has already shown that Human-First and AI-First workflows can produce different levels of immediate accuracy, calibration, and reliance on AI. A separate and rapidly growing literature shows that AI use can either help or harm later independent performance. The broad ideas—“timing matters” and “AI can change human learning”—are therefore not new.

What I did not find in this focused search is a randomized study that combines all of the following:

- a direct Human-First versus AI-First comparison;
- the same task, AI advice, advice accuracy, incentives, and ground-truth outcome feedback in both conditions;
- repeated decisions with a learnable structure;
- a common post-test using novel cases; and
- tests conducted without AI or with systematically misleading AI.

That combination is the project’s strongest remaining contribution. The study should not be framed as the first comparison of Human-First and AI-First workflows. It can instead ask an unresolved question: **does workflow order change what people learn from the same outcome feedback, and does any difference survive when the AI is absent or unreliable?**

This is a focused scoping review, not yet a publication-grade systematic review. The conclusion should therefore be read as “no exact match located in the sources searched,” not as proof that no such study exists anywhere.

## Why the Question Still Matters

Organizations usually evaluate AI by asking whether it improves the decision being made now. That leaves out a second outcome: what happens to the person’s ability to make the next decision.

That distinction is consequential. Standard AI access improved students’ practice performance but reduced their performance once AI was removed in a large field experiment; guarded tutoring largely removed that harm ([Bastani et al., 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12232635/)). Brief AI use has also been found to reduce later independent performance and persistence across reasoning and reading tasks ([Liu et al., 2026](https://arxiv.org/abs/2604.04721)). In medical training, people have carried an AI system’s systematic error into a later unassisted phase ([Vicente et al., 2025](https://doi.org/10.1016/j.ijhcs.2025.103474)). Yet AI does not always deskill: other studies find retained learning from accurate AI exposure or well-designed feedback ([Ruan et al., 2026](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6736799); [Cabitza & Vicente, 2026](https://www.sciencedirect.com/science/article/pii/S1071581926001308)).

The mixed evidence is precisely why a clean workflow experiment is useful. Advice order is an inexpensive and reversible design choice. If it changes learning, organizations have a practical lever for preserving expertise. If it does not, that null result is also useful: organizations may be imposing an extra Human-First step without gaining independent capability in return.

The theoretical value is similarly specific. Advice-taking research usually measures how much people use advice on the current case. Learning research usually compares AI access with no AI, or one form of AI support with another. The proposed study connects those literatures by asking whether workflow sequence changes the *learning value* of otherwise identical ground-truth feedback.

## The Closest Prior Studies

| Study | What it already establishes | What it leaves unresolved |
|---|---|---|
| [Green & Chen (2019)](https://doi.org/10.1145/3359152) | Across repeated bail and lending predictions, an “Update” condition—judge first, then see the algorithm—slightly outperformed simultaneous algorithmic advice. Initial pre-AI judgments also improved across cases. | Outcome feedback was a separate experimental condition, not something held constant across the two advice orders. There was no common transfer or AI-withdrawal post-test. This is the most important precedent to address directly. |
| [Buçinca, Malaya, and Gajos (2021)](https://www.eecs.harvard.edu/~kgajos/papers/2021/bucinca2021trust.shtml) | Requiring people to engage before or during AI advice can reduce overreliance on incorrect recommendations, although users may dislike the added effort. | The study concerned immediate reliance, not learning from repeated outcome feedback or later independent performance. |
| [Gajos and Mamykina (2022)](https://www.eecs.harvard.edu/~kgajos/papers/2022/gajos2022people.shtml) | AI recommendations improved current nutrition decisions but did not produce incidental learning. Asking for an initial choice before showing an always-correct AI also failed to produce learning; explanation-only support did. | AI-First and Human-First appeared in separate experiments rather than a direct randomized comparison. AI-assisted trials did not provide case-level outcome feedback, and the AI never erred. The study is a warning that recording an initial judgment may be necessary but is not sufficient for learning. |
| [Fogliato et al. (2022)](https://arxiv.org/abs/2205.09696) | In a study of veterinary radiologists, a provisional judgment before AI reduced agreement with the system whether its advice was right or wrong. | It measured current-case behavior only. There was no outcome feedback, learning phase, novel-case test, or AI withdrawal. |
| [Cabitza et al. (2023)](https://doi.org/10.1016/j.artmed.2023.102506) | Two medical studies directly compared collaboration protocols and found higher immediate diagnostic accuracy for AI-First in their settings. | They did not study repeated learning from ground-truth feedback or independent performance after AI removal. The result also cautions against assuming Human-First is always superior. |
| [Yin et al. (2025)](https://pubsonline.informs.org/doi/10.1287/mnsc.2022.01454) | In a *Management Science* study of physicians, advice shown after an initial diagnosis improved immediate accuracy and calibration. Think-aloud evidence linked this to more thorough evidence processing and better discrimination between correct and incorrect AI advice. | There was no case-level outcome feedback, learning post-test, transfer, or withdrawal phase. This paper already owns much of the immediate-performance and cognitive-engagement argument. |
| [Aiyer and Yeung (2025)](https://doi.org/10.1002/bdm.70021) | Across three experiments, advice shown after people had viewed the evidence influenced judgments more than advice shown before the evidence. Feedback reduced but did not eliminate the timing effect. | Participants were not required to record a pre-advice judgment, and the outcomes were advice utilization on current trials rather than later unaided learning or transfer. |
| [Wong and Qiu (2026)](https://link.springer.com/article/10.1007/s10648-026-10118-7) | Students who first generated ideas and then collaborated with ChatGPT outperformed both unrestricted-ChatGPT and human-only groups on a later unaided creativity task. | This is the closest conceptual competitor, but it changed several things at once: a 3/6/3-minute workflow, prompt scaffolding, the role assigned to ChatGPT, and the requirement to generate several initial ideas. The task had no objective ground-truth outcome feedback. It does not isolate advice timing. |
| [Xu et al. (2026)](https://www.nature.com/articles/s41591-026-04553-w) | A large 4 × 2 dermatology experiment directly randomized Human-First versus AI-First alongside four explanation types. Final accuracy did not differ by order after information was equalized, although AI-First tended to increase deference. | Participants received no case-level ground-truth feedback, and the second response concerned the same image rather than a novel transfer case. It tests workflow order, not learning. |

Two current projects make the area especially fast-moving. An [ECIS 2026 research-in-progress paper](https://aisel.aisnet.org/ecis2026/cog_hbis/cog_hbis/30/) proposes advice order × accuracy warnings in repeated forecasting, and an [INSEAD working paper](https://www.insead.edu/faculty-research/publications/working-papers/timing-algorithmic-advice-effects-team-performance-and) examines how early algorithmic advice affects team reasoning. Neither public description reports the proposed combination of identical outcome feedback and a common independent transfer test, but both narrow the space for broad novelty claims.

## What the Learning Literature Adds

The second literature stream shows why feedback must be treated as a central part of the design rather than as a background feature.

[Cabitza and Vicente (2026)](https://www.sciencedirect.com/science/article/pii/S1071581926001308) found that medical students acquired and retained a hidden diagnostic rule only when AI-supported practice included trial-by-trial feedback on the correctness of both human and AI decisions. Advice alone, even with confidence information, did not produce durable learning. [Gajos and Mamykina (2022)](https://www.eecs.harvard.edu/~kgajos/papers/2022/gajos2022people.shtml) likewise found no learning from recommendations and explanations when AI-assisted trials lacked outcome feedback. Together, these studies make the proposed “same feedback in both workflows” design more than a control: it is the condition that allows the timing question to be identified.

The literature also shows that learning can run in either direction. Accurate AI may transmit useful patterns, while systematically wrong AI may teach the wrong rule. Repeated interaction with biased AI has increased later human bias across perceptual and social judgments ([Glickman and Sharot, 2025](https://www.nature.com/articles/s41562-024-02077-2)). Any study of learning should therefore measure not only whether people improve, but also what they have learned from the system.

## The Defensible Contribution

A suitable positioning statement is:

> Prior research has examined how advice timing affects immediate accuracy, reliance, and cognitive engagement. We ask a distinct question: holding case-level ground-truth feedback constant, does requiring an unaided pre-advice judgment change what people learn across repeated human–AI decisions, and does that learning persist when the AI is absent or unreliable?

This is stronger and safer than claiming that the study is the first Human-First versus AI-First experiment. In a paper, “we isolate an unresolved comparison” or “one of the first randomized tests of feedback-based learning across advice workflows” would be defensible only after a full database review.

## Design Implications from the Review

1. **Define “the same feedback” precisely.** Both groups should receive the same ground-truth outcome, at the same time, in the same format. The feedback screen should not give the Human-First group an extra explanation unavailable to the AI-First group. The recorded initial judgment is part of the workflow treatment, not additional outcome information.

2. **Do not call the treatment pure timing.** Human-First changes when advice appears, whether a person commits to a judgment, and how much cognitive work is required. Unless the study adds timing-only and commitment-only arms, the estimand is the effect of a *workflow package*.

3. **Make later independent performance the primary outcome.** Immediate accuracy and reliance have already been studied extensively. A novel-case, no-AI post-test is the cleanest primary test. Performance with systematically misleading AI can be a second resilience outcome.

4. **Use a task with a learnable rule.** If every case is unrelated, there is nothing stable for outcome feedback to teach. If the rule is too obvious, both groups will hit a ceiling. A pilot should verify that unaided performance improves gradually and that feedback is informative.

5. **Pre-register feedback and calibration measures.** Green and Chen’s feedback condition pushed probabilistic judgments toward extremes, illustrating that feedback format can change calibration in unintended ways. Accuracy, confidence, Brier score or calibration error, and response to correct versus incorrect AI advice should be specified in advance.

6. **Do not assume a Human-First advantage.** Early AI may reveal useful features, and a pre-advice commitment may create self-anchoring. The study is valuable because both directions—and a meaningful null—are plausible.

## Recommended Next Review Step

Before making a formal novelty claim, extend this note into a structured review covering PsycINFO, Web of Science or Scopus, ABI/INFORM, ACM Digital Library, and current working-paper repositories. Forward- and backward-citation searches should start from Green and Chen (2019), Gajos and Mamykina (2022), Fogliato et al. (2022), Yin et al. (2025), Wong and Qiu (2026), and Xu et al. (2026).

Each study should be coded for: direct order manipulation; recorded pre-advice judgment; AI fallibility; repeated cases; case-level ground-truth feedback; feedback equivalence across groups; unaided post-test; novel-case transfer; reliability shift; delayed retention; and participant expertise. That coding table—not a general narrative review—will provide the strongest evidence that the final experimental comparison remains unresolved.

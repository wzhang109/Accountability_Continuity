# Research Log — Accountability Continuity Project

**Current-status note, October 1, 2026:** earlier entries preserve exploratory
reasoning and proposed methods, including claims that remain untested. Use the
[research status](RESEARCH_STATUS.md) and current [research program](RESEARCH_PROGRAM.md)
for present descriptions. There are no participant or private organizational
data; an initial public-document coding pilot has now been added. Design,
implementation, coding, and writing received substantial AI assistance.

## October 16, 2026 — Reverse missing-information cases

Added two practice-only drafts reversing the earlier missing-field shortcut,
with an explicit tie rule, paired advice and common feedback. Checked outcome
classes and exposure boundaries; preserved earlier task records and planning
counts. Twenty drafts, ten slots missing. Independent review is pending; there
are no participant data. AI assisted the design, coding and documentation.

## October 14, 2026 — Constraints and missing information

Added Y11/Y12 beside preserved Y01, including an unknown value that cannot
change the choice and one that can. Kept paired advice, shared feedback and
phase boundaries; checked compatible logical outcomes. There are 18 fictional
drafts and 12 remaining slots. Human review remains pending; no participant data.

## October 12, 2026 — Rates practice materials

Added Y09/Y10 alongside preserved Y02, covering three answer categories.
Documented paired advice, missing-denominator counterexamples and cue/burden
limits. Computed and exposure checks passed; human review remains pending.
The bank has 16 fictional drafts and 14 missing items, with no participant data.

## October 8, 2026 — A partial human-support response pathway

Followed existing organizational entry E02 across three refreshed publications
and three newly read public sources. Added a dated official reply, program
purpose/measurement context and a responsibility label. Kept feature-level
approval, implementation, later assessment and feedback to original users
unknown when the reviewed records did not establish them.

A launch statement does not show that the handoff feature launched; developer
on-call escalation does not show that a citizen can reach a departmental
advisor. The result is a bounded, inspectable pathway and gap list, with
structural checks. No new independent case, causal effect, goal revision,
human outcome or independent human review is claimed. Existing pilot records
and youth/adult study versions retain their scopes. This batch was prepared
for review against the October 7 published commit. Source versions and
publication are traceable in the repository history; human review is pending.

## October 7, 2026 — Youth feasibility materials prepared

Converted the adolescent proposal into a distinct workflow protocol, eight
fictional school-project records with keyed advice, a measure-to-claim map and
a minimal data dictionary. Added explicit baseline and delayed feedback timing
for review. The local helper separates pre-advice, post-advice and unaided
responses and prevents advice or keys from leaking into the delayed assessment.

Checked arithmetic keys, missing responses, confidence calculations, advice
visibility and public-file privacy boundaries. These are AI-assisted structural
checks, not participant evidence, age suitability or independent methodological
validation. Twenty-two further items, balanced lists, partner/ethics arrangements
and expert review remain pending. The assigned workflow includes commitment and
effort; it does not identify a pure order mechanism.

Close primary-source precedents were located; the three-arm design is not new.
One source's complete delayed section remains incompletely retrieved. The
GitHub baseline was subsequently verified through Git before integration;
publication is traceable in the repository history. Independent review is still
pending. Next: one source-linked organizational issue-response pathway.

## October 1, 2026 — Purpose and revisable judgment

Later in the day's discussion, Celine connected AC to a question about the good
life: without active reflection on what matters, available measures can begin
to define it for us. The organizational extension asks who defines a good
outcome, whose experience is heard, and whether consequences can lead people to
reconsider their goals as well as their procedures.

Added a [working reflection](docs/purpose-judgment-and-accountability.md), retaining
“心” as an expression of care, judgment, and willingness to learn, rather than a
new psychological score. This is conceptual development, not an empirical finding.
The earlier simulation, learning-study design, and public-document coding retain
their separate scopes. No new claim has been imposed on the five coded entries.

## October 1, 2026 — First public-document pilot of organizational responses

Reviewed the September 29 audit and checked the remote repository against commit
`c9f8d29634203035cf153507dc82ddd57298d93e`. The organizational branch now has five
source-linked entries from two public-sector programs, drawn from five primary
publications, plus a coding guide and selection log. Multiple entries from one
program are not independent observations. The coding distinguishes implemented
changes, plans, local adjustments, and expressed needs.

The methodological takeaway is that a person's review, an organizational response,
and demonstrated improvement require separate evidence. Missing details in public
reports remain unknown. No causal effect, prevalence estimate, validated AC score,
or independent inter-coder reliability is claimed.

Added current clarifications to the early index and framework notes while keeping
their historical text. The previous simulation and advice-timing protocol remain
unchanged. Next: independent review and one issue-level record connecting a report,
response decision, action or justified refusal, later assessment, and feedback.
See the [pilot](studies/organizational-feedback/README.md).

## September 14, 2026 — Methods review and operational study draft

An AI-assisted review expanded the model walkthrough, made the assumptions
and contribution limits explicit, and identified a numerical failure: an
uninformative measurement could yield a zero standard error through a
pseudoinverse. An information-rank guard now reports that the parameters cannot
be separately identified at the fitted numerical precision. Seventeen tests
passed, and the full default simulation was rerun: 36,000 replication records
and 72,000 fits, with all nine CSV summaries reproduced within tolerance.
Details are in the [verification record](simulations/override_identification_v2/VERIFICATION_2026-09-14.md).

The related learning study now has a [three-arm operational draft](studies/ai-advice-timing/DRAFT_PROTOCOL.md)
and eight fictional task examples. An adult feasibility study is proposed as
one starting option; it has not been arranged or run. Task validation,
statistical review, a research setting, and any required ethics process remain
future work. This update does not establish an empirical finding or independent
methodological validation.

---

Each entry should take 15–20 minutes to write. Short is fine. The point is a continuous, dated, verifiable record — not polish.

**How to fill each entry:**
1. Date 
2. What did you do this week 
3. What you found/decided
4. What's next

**Note on retroactive entries (Weeks 1–4):** these reconstruct work that was already underway, documented in working notes and conversation records, before this log was formally split out from the Compute Gatekeeping repository. Dates are approximate where the exact day is uncertain — flagged inline.

---

## Week 1 — July 11
**Focus:** Initial question — the cognitive/consciousness gap between humans and AI

**Notes:**
Started pulling on a thread that had been sitting underneath the compute gatekeeping work: alignment research keeps reducing, at bottom, to a question about the difference between human and AI decision-making that isn't really about capability — it's about something closer to reflection, or judgment formed through lived consequence. Framed initially (too strongly) as "AI can't reach human 悟 (genuine realization) no matter how it's trained." Flagged this early framing as an intuition to be tested, not a conclusion — a discipline I want to hold to throughout this project.

**Next:** Develop this into something more precise than an intuition.

---

## Week 2 — July 13
**Focus:** Building the philosophical grounding — taste, reflection, and the existential/behavioral gap distinction

**Notes:**
Worked through why "taste" (a trained, domain-specific quality judgment, distinct from raw intuition) survives as the right concept, even though RLHF has the same judge-rate-adjust loop taste requires. The missing piece is reflection carried by the same subject across time — the rater reflects, but the model inherits only the verdict, not the reflection. This produces two separable claims: a **behavioral gap** (whether outputs match what a reflective subject would produce — plausibly compressible) and an **existential gap** (whether there's a continuous someone bearing the outcome — plausibly not compressible the same way, possibly closer to binary than continuous).

Grounded the existential-gap claim in Nagel (1974) and Chalmers' hard problem / philosophical zombies, then hit a real problem: Buddhist 无我 (anatta) and Parfit (1984) both deny a persistent metaphysical self, even in humans — which threatens the premise that humans have "a continuous self" AI lacks. Resolved this by weakening the claim: not metaphysical selfhood, but **causal continuity of a mind-stream** (心相续 / 阿赖耶識 seed metaphor in Buddhist philosophy, psychological continuity/connectedness in Parfit) — a claim both traditions accept. AI's retrieval-based memory provides informational continuity (a record of experience) but not this causal continuity (the experience itself, carried forward) — illustrated with an amnesia-patient/case-file analogy.

**Decision:** The existential-gap argument will be built on causal continuity, not metaphysical selfhood, going forward. This is the version that needs to survive scrutiny, not the stronger one.

**Next:** Translate this into something with policy/economic teeth rather than leaving it as a philosophy-of-mind argument.

---

## Week 3 — July 15
**Focus:** Public-facing synthesis — drafting "The Gap That Can't Close"

**Notes:**
Wrote a ~1,850-word essay synthesizing Week 2's argument for a general audience (Substack/LinkedIn): taste → what RLHF's loop is missing → who actually carries the cost → why averaged feedback fits no one particular case well → why memory doesn't resolve the continuity problem → gradual vs. sudden cultivation (Cook Ding; 神秀 vs. 慧能) as a way of asking whether the behavioral gap and existential gap close the same way → closing with what remains distinctly human once the behavioral gap narrows (being changed by a cost actually borne, unprompted truth-seeking, judgment that costs something real).

Deliberately marked the essay's strongest claims ("AI currently is a tool; genuine realization may require conditions it lacks") as held intuitions, not proofs — consistent with the epistemic standard set in Week 2.

**Next:** This essay is downstream output, not the research program itself. Week 4 needs to turn back toward how the argument becomes usable for institutional design.

---

## Week 4 — July 16–17
**Focus:** From philosophy to institutional design — building the two-axis framework and situating it in the literature

**Notes:**
Found Liu (2026), "The Organizational Behavior of Agentic AI" — an organization-theory paper arguing agent collectives resemble human organizations functionally (differentiation, coordination, routines) but are sustained by context architecture rather than motivation, identity, trust, or moral accountability. Read it in full (not excerpted). Two things stood out: (1) Liu's own examples (a lawyer remaining accountable for AI-assisted advice, an engineer remaining accountable for AI-assisted deployment) show accountability sitting at multiple points across a workflow, not only at "which goal to pursue" — corrected an earlier, too-narrow version of this project's framing that treated accountability as purely an upstream, goal-selection question. (2) Liu's central distinction rests on an unexamined premise — that agent collectives "do not experience responsibility as a moral burden" — stated, never argued for. That premise is precisely this project's object of study, not a fact Liu is entitled to assume. This reframes the accountability-relevant portion of organizational-behavior literature on agentic AI as *downstream of* an unresolved question in philosophy of mind, not a parallel, independent literature.

Built a first formal pass at a **two-axis framework**: coordination cost (Liu's contextual transaction cost) crossed with accountability requirement (this project's contribution), producing a four-quadrant map of when agent-native organization, human-led judgment, or a designed interface between the two is appropriate. Extended Liu's value function V(O,T) with accountability continuity AC(O,t) as a hard constraint (not a tradeable cost) for tasks requiring it — reasoning: institutions that already require accountability have, by definition, decided efficiency should not be traded against it.

Identified a further extension: "taste," originally defined only over outputs, plausibly also operates one level up — over which questions/directions are worth pursuing, and whether a candidate answer genuinely fits one's own accumulated judgment rather than merely sounding plausible. Flagged explicitly as a new hypothesis extending, not restating, the Week 2–3 argument — not yet tested against likely objections (e.g., whether the much longer feedback delay in direction-setting breaks the taste-formation loop the same way).

Read Long, Sebo, Butlin, Plunkett et al. (2026), "Studying AI Welfare Empirically" (Eleos AI / NYU CMEP) — the field's current best-practice methodology paper for markers-based AI consciousness/welfare research. Notable for this project: its "entities" section (model vs. persona vs. instance vs. instance-persona vs. forward pass) independently arrives at a Parfit-style move to handle AI entity individuation, and its own catalog of challenges (mismatch problem, specificity problem, solution space problem, anchor problem) supports a live open concern for this project — whether markers-based research can ever be evidentially decisive about AI consciousness at all, given AI systems lack the evolutionary/anatomical anchor that licenses behavior-to-inner-state inference in animal welfare science. Recorded as an open, unresolved disagreement this project holds with the marker-based research program, not a settled objection — worth stress-testing further, potentially by raising it directly with researchers in that literature.

Began outreach to researchers spanning both literatures (AI welfare: Eleos AI; organizational AI: Google DeepMind, UCL) to pressure-test the framework against people actively working in it.

**Decision:** This project proceeds as a parallel track alongside Compute Gatekeeping, not a replacement. Splitting into its own log as of this entry.

**Next:** Week 5 — draft a formal identification strategy for the Accountability Continuity Index (see `/proposal/`); begin literature review write-up split into the two source literatures.

---

## Week 5 — July 31 (note: both Week 5 and Week 6 tasks were completed in one sitting on 7/31, not spread across their nominal weeks — logged honestly rather than backdated)
**Focus:** Formal identification strategy for the Accountability Continuity Index

**Notes:**

Worked through all five checklist items as a single connected design, not five independent choices.

*Unit of analysis:* decision-type × organization × time period (quarter or year), not organization alone. "Decision-type" = a recurring class of decisions sharing the same underlying judgment domain within an org (e.g., loan-approval decisions at a bank, triage decisions in an ED, code-merge decisions in an eng org). This matters because accountability continuity is a property of who bears responsibility for a *kind* of decision over time, not a property of the organization as a whole — the same company can have high AC in one decision-type and near-zero in another.

*Treatment definition:* staggered adoption of an AI/agentic tool for a given decision-type, with the treatment threshold set at the point the tool moves from advisory-only to executing/finalizing without required human sign-off for that decision-type. Decided to code this as an ordinal intensity variable (advisory → co-pilot-with-signoff → autonomous) rather than a binary, since the project's actual interest is in how much discretion transfers, not whether AI is merely present — a binary would throw away the variation that matters most.

*Outcome variables:* error/reversal rates (decisions later overturned or corrected), correction speed (time between decision and correction), dispute rates (formal complaints/appeals tied to the decision-type). Flagged explicitly: these are behavioral-gap proxies, not existential-gap measures — the AC Index cannot observe whether anyone "bears" the decision in the sense Week 2 cared about, only whether the accountability structure produces measurably different downstream outcomes. This is consistent with treating AC(O,t) as a hard constraint (Week 4) rather than something these variables are meant to prove or disprove — they test what happens when the constraint is relaxed, not whether the constraint is "real."

*AC-score coding criteria:* operationalized the three indicators as a 0–2 rubric per decision-type × org × year cell — primary-evidence engagement (does the decision-maker engage the raw case-specific evidence, or only a summary/recommendation?), real discretion (is override of the AI recommendation observed at non-trivial rates and without penalty, not just formally permitted?), repeated exposure (does the same decision-maker handle repeat instances of this decision-type over time, allowing feedback to accumulate on one continuous "mind-stream" — the causal-continuity concept from Week 2, applied institutionally rather than metaphysically). Noted this rubric is structurally the same shape as the State Support Index rubric on the China/WTO project (dimension scores × sources, coder_id, review_status) — worth keeping that consistency deliberate rather than coincidental.

*Candidate data sources:* no organizational partners are actually secured yet, so logging categories rather than named partnerships to avoid overstating progress — (1) public court/regulatory records where AI-assisted decisions are being formally challenged (EEOC/CFPB-adjacent algorithmic hiring or lending complaints), (2) published clinical-decision-support override-rate audits (several hospital systems publish these), (3) the Week 4 outreach contacts (Eleos AI; UCL/DeepMind organizational-AI researchers) as possible access points, though that outreach is about framework feedback, not data access, and shouldn't be conflated with the two.

**Decision:** Treatment is ordinal (advisory/co-pilot/autonomous), not binary. Outcome variables are explicitly scoped as behavioral-gap proxies only — the log should not later describe them as measuring the existential gap.

**Next:** Pressure-test whether the three AC-score indicators are actually separable in real data, or whether primary-evidence engagement and real discretion collapse into the same underlying thing in practice — that's an open risk, not yet resolved.

---

## Week 6 — July 31
**Focus:** Literature review — Track 1 (philosophy of mind / AI welfare)

**Notes:**

Followed up directly on the Week 4 concern — whether markers-based AI consciousness research can ever be evidentially decisive, given AI lacks the evolutionary/anatomical anchor that licenses behavior-to-inner-state inference in animal welfare science (the "anchor problem").

Read Butlin, Long, Bayne, Bengio, Birch, Chalmers, Constant, Deane, Elmoznino, Fleming, Ji, Kanai, Klein, Lindsay, Michel, Mudrik, Peters, Schwitzgebel, Simon & VanRullen, "Identifying indicators of consciousness in AI systems" (*Trends in Cognitive Sciences*, 2025/2026) — this is the direct methodological ancestor of the Long/Sebo/Butlin/Plunkett welfare-empirics paper already cited in Week 4: derives indicator properties from multiple competing theories of consciousness (global workspace, IIT, recurrent processing, higher-order, predictive processing, attention schema) rather than committing to one, producing a probabilistic rather than binary assessment tool.

Found Koch (2026), "From indicators to biology: the calibration problem in artificial consciousness" (arXiv:2603.27597) — this essentially formalizes the same anchor-problem worry independently: argues the indicator-based program is "epistemically under-calibrated" because indicators lack independent validation and no ground truth of artificial phenomenality exists, making probabilistic consciousness attribution to current AI systems premature. Koch's own proposed fix — redirect effort toward biologically-grounded engineering (biohybrid, neuromorphic, connectome-scale systems) that stays anchored to the one domain where consciousness is empirically anchored (living systems) — doesn't resolve this project's problem, since the project isn't trying to build biologically-anchored AI. But the critique itself is useful: it's independent confirmation that the anchor-problem worry isn't just this project's own skepticism, it's a live, named problem in the indicators literature itself.

Read Schwitzgebel (2026), "AI and Consciousness" (arXiv:2510.09858, skeptical overview; Cambridge Elements monograph forthcoming August 2026) — central verdict: "none of the standard arguments either for or against AI consciousness takes us far," and we may soon have systems judged conscious under some mainstream theories and not others, with no way to adjudicate between the theories. Chapter Seven, "The Mimicry Argument Against AI Consciousness," is directly relevant — reinforces the project's existing worry that behavioral markers may be systematically confoundable by mimicry rather than genuine indicators.

**Decision:** These three sources converge on a reading that *strengthens* rather than undermines Week 4's institutional-design move. If the calibration problem is real and durable (Koch) and the standard arguments don't resolve it (Schwitzgebel), then a research program that tries to wait for consciousness science to settle the existential-gap question before designing institutions is choosing a strategy that may never pay off. That's an argument *for* treating AC(O,t) as a hard institutional constraint decided on grounds other than resolving the metaphysics — not a workaround, but the actual right response to persistent epistemic uncertainty.


## Week 7 — Aug 18


**Focus:** Formalized the identification problem that motivates the index.

**Notes:**
Built a two-world simulation (`simulations/sim_identification.py`) in which a
model-improvement process and a reviewer-disengagement process produce an
identical override-rate path. Engagement in the disengagement world is solved
analytically so the two paths match exactly rather than approximately, which
makes the non-identification a construction rather than a coincidence of
parameters.

Three additional observables separate them: model accuracy on a held-out gold
set, whether the reviewer opened the primary record, and the precision of the
overrides that still occur.

**Unexpected result:** override precision falls further in the world where oversight is
working, because as the model improves a growing share of remaining overrides
are reviewer error rather than model error. This means low override precision is
not on its own a warning sign — it has to be read against model accuracy.

**Open:** the direction of that result depends on the false-alarm rate F. A sweep
over F to locate the flip point has not been run. Until it is, panel 4 is
suggestive only.

**Why this matters for the framework:** the three index components were
previously stated without a derivation. They are now answerable to a specific
question — what second signal do you need — rather than asserted.


## 2026-10-10 — Six baseline examples prepared

Added six fictional unaided starting tasks, an answer-free review worksheet,
answer justifications and explanation anchors. Covered constraints, denominators,
pooling and limits of before/after causal claims. Preserved the existing eight
examples, giving fourteen of thirty planned items; sixteen remain. Added checks
of arithmetic, missing denominators admitting opposite conclusions, missingness,
block-end feedback and rejection of baseline item reuse in assisted phases.

This makes the starting assessment reviewable, not validated. The review guide
flags arithmetic/language burden, answer-label cues, unequal family coverage,
feedback reactivity and non-equivalent forms. No participants, approvals or
partner were added. Independent human review is pending; work received AI
assistance. October 10 preparation uses the verified October 8 main commit;
publication is tracked separately. Next bounded unit: review these six items with
the researcher, then develop one balanced practice-family set rather than expand
the entire study without reviewing burden.

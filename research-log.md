# Research Log — Accountability Continuity Project

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

## Week 5 — [DATE]
**Focus:** Formal identification strategy for the Accountability Continuity Index
- [ ] Draft candidate unit of analysis (decision-type × organization × year)
- [ ] Draft candidate treatment definition (staggered AI/agentic-tool adoption for a given decision type)
- [ ] Draft candidate outcome variables (error/reversal rates, correction speed, dispute rates)
- [ ] Draft AC-score coding criteria from the three operational indicators (primary-evidence engagement, real discretion, repeated exposure)
- [ ] Identify 2–3 candidate data sources or organizational partners for a pilot

**Notes:**

**Next:** Week 6 — literature review, Track 1 (philosophy of mind / AI welfare)

---

## Week 6 — [DATE]
**Focus:** Literature review — Track 1 (philosophy of mind / AI welfare)
- [ ]
- [ ]

**Notes:**

**Next:** Week 7 — literature review, Track 2 (organizational behavior / management science)

---

## Template for future weekly entries (copy below as needed)

## Week N — [DATE]
**Focus:**
- [ ]
- [ ]

**Notes:**

**Next:**

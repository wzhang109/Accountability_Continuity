# Accountability Continuity Index: Formal Model and Identification Strategy
*Working proposal draft — v0.1*

## 1. Motivation

Whether an AI system possesses consciousness, sentience, or moral status is, on current evidence, not resolvable with the confidence institutional policy requires — the explanatory gap between third-person evidence and first-person experience (Nagel, 1974; Chalmers, 1996) is a structural barrier, not a data limitation. Waiting for this question to resolve before designing institutions for human-AI task allocation is not a viable policy strategy.

This project substitutes a different, empirically tractable question: **does a given decision require a continuous human subject who bears the consequence of error and carries it into future judgment (accountability continuity), and does the organizational form actually delivering that decision preserve this property?** This question does not require resolving consciousness. It can be answered, in principle, by observing institutional design and outcomes.

## 2. Formal model

Following Liu (2026), the value of an organizational form $O$ executing task $T$ can be written:

$$V(O,T) = G(O,T) - CTC(O,T) - K(O,T) - R_g(O,T)$$

where $G$ collects gains from specialization, parallelism, diversity, and verification; $CTC$ is contextual transaction cost (the cost of moving usable context across boundaries within a collective); $K$ is compute cost; and $R_g$ is governance risk.

This project's extension: for a task $t$ belonging to the set $A$ of accountability-requiring tasks, the optimization is constrained rather than penalized —

$$\max_O V(O,t) \quad \text{subject to} \quad AC(O,t) = 1$$

where $AC(O,t) \in \{0,1\}$ indicates whether organizational form $O$ preserves genuine accountability continuity for task $t$, as distinct from mere evidentiary traceability. For $t \notin A$, the unconstrained Liu optimization applies.

**Why a constraint rather than a cost term:** domains that already require accountability (medicine, law, comparable high-stakes judgment) are, definitionally, domains where institutions have decided efficiency should not be traded against a genuinely accountable subject remaining in the loop. Modeling $AC$ as a soft cost that a sufficiently large efficiency gain could outweigh would misdescribe the institutional logic these domains already operate under.

## 3. Operationalizing AC(O,t)

$AC(O,t) = 1$ requires evidence on three indicators, each measurable from organizational workflow design and records rather than from claims about AI's internal states:

1. **Primary-evidence engagement** — does the accountable party engage with primary case material, or only a compressed/summarized trace?
2. **Real discretion** — does the accountable party have actual power to change the outcome, or is sign-off a formality rarely exercised?
3. **Repeated, trackable exposure** — does the same person or role face comparable decisions repeatedly, such that error in one instance can plausibly inform the next?

These three indicators can be coded from process documentation, workflow audit logs, and structured interviews — a measurement strategy closer to labor economics' study of task allocation and supervisory discretion than to AI interpretability research.

## 4. Identification strategy

**Unit of analysis:** decision-type × organization × year (e.g., loan-approval decisions at Bank X, radiology second-reads at Hospital Y, code-deployment sign-off at Firm Z).

**Treatment:** adoption of AI or agentic tooling for a given decision type. Adoption timing varies by organization and decision type — a staggered-adoption design structurally identical to the compute gatekeeping project's design, and to earlier work on South Korea's 1987 transition.

**Estimator:** Sun & Abraham (2021) event-study specification as the main spec (preserves an interpretable $\beta_k$ event-time pattern), with Callaway & Sant'Anna (2021) group-time average treatment effects as a robustness cross-check — the same estimator choice made for compute gatekeeping, for the same reason (avoiding negative-weighting bias from already-treated units acting as comparisons under naive TWFE).

**Outcome variables (candidates, to be refined during pilot):**
- Error/reversal rate for the decision type, before/after adoption
- Time-to-correction when errors are identified
- Dispute, appeal, or litigation rate
- AC score itself, coded from the three indicators above, tracked over time as organizations redesign workflows around AI adoption

**Core empirical question:** does AI/agentic adoption that preserves high AC (genuine accountability continuity) produce different outcome trajectories than adoption that does not — controlling for decision-type fixed effects? This tests whether the accountability-continuity concept has real predictive content, not just conceptual appeal.

**Known identification threats to check during the pilot (in the spirit of the compute gatekeeping log's early threat-flagging):**
- Selection: organizations that adopt AI tooling for high-stakes decisions earlier may differ systematically from late adopters in ways correlated with baseline error rates (parallel-trends threat — check pre-adoption trends explicitly, as in compute gatekeeping Week 12).
- Measurement: AC coding from workflow documentation may itself be sparser or less reliable for smaller organizations, mirroring the Epoch AI documentation-coverage concern from the compute gatekeeping project (Week 3) — worth cross-checking AC codings against a second, independent method (e.g., structured interviews) for a subsample.
- Reverse causality: organizations with worse baseline error rates might adopt AI tooling *because* of those errors, confounding the direction of the AC–outcome relationship — needs explicit discussion in the identification strategy, not just an assumption of exogenous adoption timing.

## 5. Relationship to the qualitative/philosophical argument

The formal model and identification strategy in this document depend on a prior argument, developed in the research log (Weeks 1–4) and the essay "The Gap That Can't Close," that the accountability-continuity criterion is a defensible substitute for the unresolvable existential-gap question — grounded in causal continuity (Parfit; 心相续) rather than metaphysical selfhood. That argument is not re-derived here; this document treats it as an input and focuses on making it operational and testable. The two should be read together, not as competing approaches — the philosophical work establishes *why* this criterion is the right one to operationalize, and this document establishes *how*.

## 6. Status

This is a v0.1 design sketch, not an executed study. No data collection has begun. The next log entries should refine the outcome variables and AC-coding protocol before any pilot organization or dataset is approached.
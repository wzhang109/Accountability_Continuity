# Coding evidence of responses to AI issues

**Draft for review · October 1, 2026**

This codebook records what a publication supports about a particular issue or response. It deliberately avoids producing an accountability score.

## Unit and scope

An entry is a reported issue-response episode, or an explicitly marked aggregate account where event-level records are unavailable. Keep program, organization, publication date, and event period separate. An article can yield several related entries; those entries are not independent samples. Do not manufacture precise event dates from publication dates.

Include a source when it identifies a concrete use context and an issue, need, or response. Prefer original team accounts, evaluations, published field studies, and primary institutional records. A developer blog is evidence of what the team reports, not an independently verified incident log. Guidance documents inform concepts but are not case observations.

## Fields

| Field | Meaning and evidence rule |
|---|---|
| `program_id` | Group entries from the same deployment; prevent counting them as independent organizations. |
| `record_kind` | `reported_change_episode`, `reported_plan`, or `aggregate_user_account`. |
| `issue_type` | Separate answer failure, unmet service need, expectation design, output quality, and training need. Training needs are not automatically AI errors. |
| `report_cutoff` | Date of the publication supporting the action status; not a claim about present operations. |
| `event_period` | Only the period the source supports; use `not_precisely_reported` when necessary. |
| `claims` | Concise sourced paraphrases. Every claim must specify a source and a passage locator. |
| `signal_origin` | For example, public pilot interaction or staff self-report; do not substitute one for another. |
| `recipient` | A reported receiving role, a team-level account without the precise route, or `not_reported`. |
| `authorization` | Record a documented approval right separately from observed participation in development. A team implementing something does not identify who authorized it. |
| `action_status` | `implemented_reported`, `planned_reported`, `local_adjustment_reported`, `requested_only`, `declined_with_reason_reported`, or `not_reported`. |
| `action_scope` | `shared_system`, `local_output`, `training`, or `undetermined`. Local correction must not become organizational redesign through coding. |
| `implementation_basis` | Claim IDs establishing implementation, including staff reports for local correction; empty for unimplemented or unreported actions. |
| `evaluation_status` | Distinguish a change-linked assessment from a general program metric or no episode-linked assessment. Neither automatically establishes causality. |
| `evaluation_basis` | Claim IDs for a linked assessment if present; empty otherwise. |
| `reporter_feedback` | Is there a documented return of the response or outcome to the original reporter? `not_reported` is not “no feedback happened.” |
| `interpretation` | The analyst's inference and its limits, kept outside the factual claims. |

## Missing evidence

Use `not_reported` for an unobserved link. Do not convert it into zero authority, no learning, or institutional failure. For a plan, record its status at publication; later sources must explicitly establish completion before the code changes. Preserve the earlier dated observation.

Report partial evidence without forcing a binary “closed loop” label. A general quality metric is not an episode-specific reassessment. A rollout after research does not identify which finding caused which change. A source describing “the team” does not establish a junior employee's influence.

## Validity and comparison

- Observation, participant self-report, team self-report, and evaluator interpretation are different evidence modes.
- More transparent organizations may appear to have more problems simply because they publish more. Silence is not a valid comparison outcome.
- GDS public users and DWP employees occupy different roles. This pilot does not compare their personal learning or rank their institutions.
- Distinguish authority to change one answer, pause a task, revise a shared workflow, and deploy a system. None is inferred from override frequency.
- Formal accountability additionally concerns who must explain a decision, to whom, and what follows. A feedback pathway alone does not demonstrate accountability in that full sense.
- No reliability coefficient is reported: there has been only AI-assisted coding and review, not independent human double-coding.

## Prospective extension

For a later round, consider recording the stated purpose, the measure used,
who helped define it, and whether a response changed a procedure or reconsidered
the goal. These are candidate fields requiring evidence and independent review;
they have not been inferred or scored for the current five entries.

Before adding outcomes, define the eligible population of issues, the period of follow-up, and how repeated reports of one underlying problem are merged. Include unresolved, declined, and successful responses. Severity, complexity, visibility, and available resources can affect both response and outcomes; a comparison of “high” and “low” feedback continuity would not by itself identify a causal effect.

The next review should test whether two readers can identify the same issue, distinguish a plan from implementation, and locate the same evidence. If not, revise the rules before expanding the dataset.

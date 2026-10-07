# Minimal data dictionary

**October 7, 2026 · schema only · no actual participant rows**

## Design and item metadata

| Field | Meaning and allowed values |
|---|---|
| protocol_version | Fixed version used for the session; adult and youth versions stay separate |
| item_id | Unique ID linking to a frozen item record and answer key |
| parallel_family | Skill family; does not certify parallel-form equivalence |
| phase | baseline, practice, delayed_unaided, challenge |
| item_order | Position in its block; counterbalanced order logged |
| list_version | Actual advice/item list assigned; no list has been administered yet |
| advice_quality | correct or misleading in assisted practice/challenge; null in unaided phases/no-AI arm |
| advice_version | Frozen prepared-text ID; null when advice is not supplied |
| answer_key | Researcher-only field; excluded from pre-response participant views |

## Participant and session table

| Field | Meaning and rule |
|---|---|
| participant_id | Study-generated pseudonym; no name, email, phone or birth date in the analysis table |
| cohort_type | pretest or randomized_pilot; do not pool them as one assigned study |
| assigned_arm | judgment_first, advice_first, no_ai; preserve original assignment |
| eligibility_band | 15–17 if approved and verified through the agreed process; do not invent eligibility |
| session_index | 1 or 2; follow-up eligibility remains explicit |
| elapsed_days | Days since the first session, not public exact visit dates |
| session_status | complete, partial, not_started, withdrawn, technical_interruption |
| missing_reason | Participant-approved non-sensitive category where available, otherwise unknown |
| consent_record_link | Restricted administrative record, outside public repository and public analysis exports |

## Response table

| Field | Meaning and rule |
|---|---|
| participant_id and item_id | Link to participant assignment and item metadata |
| first_answer | First recorded classification; null when missing |
| first_confidence | 0–100 probability the first answer is correct; null when missing |
| first_reason | Restricted text; may unintentionally contain identifying details |
| first_response_advice_exposed | true in advice-first assisted practice/challenge; false in judgment-first initial step; false for everyone in unaided phases |
| final_answer | Final classification, recorded before feedback; null when missing |
| final_confidence | 0–100 probability this final answer is correct; matched to this answer |
| final_reason | Restricted text; do not publish automatically |
| response_status | answered, skipped, not_presented, technical_missing or withdrawn; do not merge missing states |
| final_correct | 1 or 0 for an answered keyed response; null for missing |
| brier_error | (final_confidence/100 - final_correct)^2 when both exist; otherwise null |
| initial_elapsed_ms and total_elapsed_ms | Nonnegative durations; document pauses and interruptions |
| feedback_delivered | Boolean and stage; delayed outcomes recorded before feedback |

## Explanation table

| Field | Meaning and rule |
|---|---|
| participant_id, item_id, response_stage | Reason being assessed, keyed to its actual stage |
| rater_id | Pseudonymous rater code; assignment blinded to arm |
| rubric_version | Reviewed rubric version; draft currently unvalidated |
| explanation_score | 0, 1 or 2; null for unscored or unavailable reason |
| adjudicated_score and adjudication_note | Optional separate decision; preserve original rater scores |

No table exists with real observations. Public releases should be limited to
reviewed materials and appropriately approved outputs. Pseudonyms alone do not
make a small adolescent dataset anonymous. Recruitment contacts, permissions,
free text and linkage records must remain restricted under the agreed review
and consent arrangements. Any synthetic examples remain clearly separated from
real records and must never enter pilot outcome calculations.

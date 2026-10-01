# From reported AI problems to organizational change

**Public document coding pilot · October 1, 2026 · Prepared for Wenwen (Celine) Zhang with substantial AI assistance**

This pilot asks: **when an issue is reported in AI-assisted work, which steps from noticing it to changing practice can we actually document?** It begins the organizational branch of Accountability Continuity using public records. It is a descriptive evidence exercise, not a field study, causal estimate, organizational ranking, or validated AC index.

The immediate contribution is a coding distinction: correcting an individual output, implementing a shared change, and demonstrating that the change helped require different evidence. A public account may document one without documenting the others.

## What was examined

Five primary publications cover two deliberately selected UK public-sector settings: GDS's public-facing GOV.UK Chat and DWP's internal Copilot trial. Five reported issue or response episodes were extracted. Multiple episodes from one program are not independent organizations or five separately observed incidents. The DWP entries describe reported patterns, rather than identified individual events.

The cases were chosen for accessible accounts of use, feedback, and responses. They were not randomly sampled. GDS develops a public service; DWP deploys a vendor assistant internally. They serve different purposes and cannot be treated as a matched comparison. The US/China outreach preference does not define this research sample.

## Initial evidence distinctions

| Entry | Setting and issue | What the reviewed publication supports | What remains unknown |
|---|---|---|---|
| E01 | GOV.UK Chat and ambiguous queries | Clarifying questions were introduced following problems in the web pilot. [S02](https://insidegovuk.blog.gov.uk/2026/03/16/5-things-we-learned-testing-gov-uk-chat-an-ai-assistant-for-government/) | Approval rights and the isolated effect of this change |
| E02 | GOV.UK Chat and personalized support | A handoff to departmental support was described as future work. [S02](https://insidegovuk.blog.gov.uk/2026/03/16/5-things-we-learned-testing-gov-uk-chat-an-ai-assistant-for-government/) | Implementation at that reporting date and subsequent outcomes |
| E03 | GOV.UK Chat and user expectations | Designers report revising onboarding around purpose, answer checking, and data use. [S04](https://insidegovuk.blog.gov.uk/2026/08/19/designing-gov-uk-chat-for-the-gov-uk-app/) | Whether that revision changed checking behavior |
| E04 | DWP and checking generated outputs | Interview-based accounts describe staff reviewing and editing outputs. [S05](https://www.gov.uk/government/publications/an-evaluation-of-dwps-microsoft-copilot-365-trial/an-evaluation-of-dwps-microsoft-365-copilot-trial) | A traceable organizational response to a particular recurring error |
| E05 | DWP and training needs | Users requested training adapted to their roles. [S05](https://www.gov.uk/government/publications/an-evaluation-of-dwps-microsoft-copilot-365-trial/an-evaluation-of-dwps-microsoft-365-copilot-trial) | A linked decision, implementation, and reassessment |

“Unknown” means not established by the reviewed passages, not that an organization failed to act. E02's future-work classification is dated to its source, not a claim about the current service. Neither case supplies a linked record showing that the person who raised a particular issue later learned what happened to it. No source-based absence claim or cross-case performance comparison follows.

GDS also describes expert log review and monitoring within its development process. That supplies context for possible response pathways, not proof that a particular employee had approval authority. [S03](https://insidegovuk.blog.gov.uk/2026/05/15/developing-gov-uk-chat-our-data-science-and-ai-engineering-journey/)

## What changes in the research

The next tractable question is about a **reported issue and its subsequent treatment**, rather than assigning one accountability score to an entire organization. This permits a record to distinguish:

1. A signal was noticed or a need expressed.
2. Someone received it and considered a response.
3. A person or role had authority to authorize that response.
4. An action was implemented, deferred, declined, or remained unreported.
5. Its consequences were assessed, and relevant people learned the result.

These are proposed research fields, not mandatory steps in every workflow. An issue may appropriately be declined; a resolved individual case may need no organization-wide change. A documented decision not to change is distinct from a missing response. Individual learning, organizational memory, and formal accountability remain separate constructs.

The public records make this sequence partly observable, while leaving important links unresolved. The usable output today is an evidence structure and a first application, not evidence that a particular organizational arrangement causes better judgment.

## Materials and reproduction

- [Coding rules](CODEBOOK.md): units, field definitions, and what missing evidence means.
- [Measurement notes](MEASUREMENT_NOTES.md): how this branch relates to earlier AC claims.
- [Source register](sources.json): dates, reading scope, locators, and retrieval hashes.
- [Coded episodes](episodes.json): source-linked statements and separate interpretations.
- [Selection log](SEARCH_LOG.md): why these records were included and what was not covered.
- [Generated checks](evidence_summary.json): structural validation and counts of these records only.

From the repository root, run:

```sh
python3 studies/organizational-feedback/validate_evidence.py
```

The checks inspect source references, dated status, required distinctions, and the consistency of the files. They do not validate source truth or establish agreement between independent coders. No simulation code or learning-study protocol was changed for this pilot.

## Next evidence to obtain

For one concrete issue, seek a linked issue report, response decision, implemented change or recorded decision not to change, and later evaluation. Then have a second reader independently assess the coding. Only after this should a broader sample or causal design be chosen.

A useful practitioner question is: “When someone notices a recurring problem with an AI tool, what usually happens next? Could you walk me through an example you can share?” A normal networking conversation is not automatically research participation; no private chat content has been included here.

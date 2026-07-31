# What You Can't Teach Your AI

*Why knowing the limits of judgment transfer is the key to scaling it*

---

Every company is now attempting some version of the same project: figure out how your best people make decisions, and hand that ability to AI agents.

The instinct is sound. As Jen Stave, Ryan Kurt, and John Winsor argued in a recent HBR piece, "Teach Your AI How You Make Decisions," the binding constraint on AI at scale is no longer the technology — it's an organization's ability to make its own judgment explicit. Most valuable judgment was never written down as rules or policy; it lives in people.

But once an organization successfully extracts and codifies that judgment, a secondary, hidden challenge immediately emerges: which extracted judgments actually transfer to agents, and which must remain in human hands?

Get this wrong in one direction, and you automate decisions that quietly fail. Get it wrong in the other, and you keep expensive humans on work that agents already do better. Both mistakes are costly. Only one of them is visible.

The numbers suggest companies are struggling with this allocation. Gartner projected in mid-2025 that more than 40% of agentic AI projects would be canceled by 2027 — citing escalating costs and inadequate risk controls, not technical limits. Recent survey work by Forrester and Anaconda found that 88% of enterprise agent pilots never reach production, with leaders naming evaluation gaps (64%) and governance friction (57%) as bigger blockers than model reliability (51%).

Look at what those blockers are. The ones leaders name most often aren't about whether the model works. They're about evaluation and governance — which is to say, about the allocation of judgment. The decisions about which decisions to delegate.

## Two Gaps, Not One

The confusion starts with treating "can AI make this call?" as a single question. It is actually two distinct gaps:

**The Capability Gap:** How well does an agent's judgment fit the case in front of it? This gap is real, it is closing fast, and investing to close it further is rational. Nearly all AI strategy discussions live here.

**The Accountability Gap:** When this judgment is wrong, does someone need to bear the consequences — and carry them forward into the next decision? This gap does not close with better training because it was never a performance problem. An agent trained on your decisions inherits your verdicts, but not your stake in them. It gets the grade without taking the class.

These two gaps demand different management strategies. You close a capability gap with engineering. You design around an accountability gap with governance. Companies that collapse the two into one question end up either over-automating — delegating calls no one can answer for — or under-automating, paralyzed by a vague unease they can't operationalize.

## Why Decision-Training Has a Ceiling

Three mechanisms limit what codification can safely capture, no matter how capable the models become:

**Verdicts without deliberation.** Training data records what your experts decided, but rarely the hesitation or context behind it. Consider a credit officer who approves a loan that trips three automated red flags based on a half-second hesitation in the applicant's voice, weighed against eighteen years of industry experience. The system simply logs: *approved, manual override, reason code "relationship."* Everything that truly mattered is missing from the record.

**Averages don't fit outliers.** Feedback pooled across many situations optimizes for the average case. But human judgment earns its keep exactly where cases drift from precedent. A customer service agent trained on routine refunds handles them beautifully until a case arrives combining a language barrier, a regulatory grey area, and signs of financial abuse. The agent applies a generic policy; a five-year human employee would have flagged it in the first sentence.

**Nobody bears the cost.** A human who makes a bad call carries it into the next one. That is how judgment compounds. An agent carries nothing — every mistake is borne by someone else, later, off the model's books.

To be clear, none of this means agent judgment is bad. On average cases, it is often more consistent, entirely apolitical, and never fatigued. The point is knowing exactly where "on average" stops.

## The Judgment Audit

Before deploying codified judgment, every class of decision should be mapped across two axes:

**Axis 1: Case Stability.** How closely do tomorrow's cases resemble yesterday's? High override rates or frequent escalations mean the work is less standard than it looks. Adversarial or fast-moving environments (fraud, competitive pricing) are inherently unstable, even if historical data looks clean.

**Axis 2: Accountability Weight.** When this judgment is wrong, does someone need to own it legally, reputationally, or relationally? Is there a licensure requirement, a named signatory, or contractual liability? A category that gets contested is a category where someone will eventually be asked, "Who decided this?"

Mapping these axes yields four distinct strategic zones for AI deployment:

| | **Drifting Cases** | **Stable Cases** |
|---|---|---|
| **High Accountability** | **Human judgment, AI-supported.** Codify the inputs. Never delegate the final call. | **Agent drafts, human owns.** The signature stays human — and only counts if the signer actively engages the case. |
| **Low Accountability** | **Augment.** Agent proposes; human filters for drift. | **Automate.** Full delegation; monitor by exception. |

The most dangerous quadrant is the top right: stable cases that still carry real accountability weight. Routine pharmacy prescriptions, for example, follow the same handful of patterns thousands of times a day, yet require a pharmacist's personal review because liability sits with a named person.

When a corporate decision looks routine, "routine" quietly gets read as "safe to fully automate," and the accountability question is bypassed. The top-left quadrant (drifting cases with high accountability) is not a temporary state awaiting better models. It is a permanent design constraint.

## The Evolution of the Org Chart

In her commentary accompanying the HBR article, Stave made a prediction worth taking seriously: "Perhaps in the future there will be a whole job family focused on understanding and codifying all of the inferred knowledge and context in an environment."

This highlights a critical new frontier for the enterprise. The most valuable professionals in this emerging job family — call them "judgment curators" — will not just extract what is codifiable. The harder half of their work will be identifying what isn't, and designing the human backstops for those edge cases. They will act as part analyst, part translator, and part boundary-setter.

They will also need a way to answer a question every company now faces: how do you know your agent's actual capability on your own decisions, rather than trusting a vendor benchmark? Two methods require no new tooling. Score the agent against past cases with known, expert-reviewed outcomes. Then run it in shadow mode — let it decide silently alongside your people, affecting nothing — and study where its disagreements cluster. Those clusters are often the fastest read on how stable a case type really is.

These teams will need to measure AI ROI not by adoption metrics like seats deployed or tokens consumed, but by judgment fit: the error cost in each quadrant, measured against the allocation the audit prescribed. Technology spend converts to value only where the allocation of judgment is right.

## The Strategy Is Knowing the Boundary

None of this is AI skepticism. It is exactly the opposite.

The companies that scale agents with confidence will be the ones that know precisely where agent judgment ends — because that knowledge is what allows them to delegate everything else without fear.

Knowing what you can't teach your AI is not a limitation on your strategy. It is the strategy.

---

*A deeper essay exploring the philosophical foundation of this argument — what taste is, why feedback loops alone don't produce it, and what remains distinctly human — can be found here: [The Gap That Can't Close: On taste, machines, and what's left for us to become].*

---

**Sources**

- Stave, Kurt & Winsor, "Teach Your AI How You Make Decisions," *Harvard Business Review*, June 25, 2026
- Gartner, "Gartner Predicts Over 40% of Agentic AI Projects Will Be Canceled by End of 2027," press release, June 25, 2025
- Forrester / Anaconda enterprise agentic AI survey data, 2026

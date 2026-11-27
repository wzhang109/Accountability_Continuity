# The Gap That Can't Close

*On taste, machines, and what's left for us to become*

Ask anyone who works with AI long enough and they'll eventually say something like this: it has no taste. Not that it produces bad output. Often it produces very good output. Still, there's a sense that something is missing, and people reach for the word "taste" because it's the closest word we have.

I want to take that claim seriously enough to test it, because I think it survives, but not for the reason most people assume.

## Two easy answers, and why neither holds

The first is that taste follows no rule you can write down. You don't calculate that a sentence works; you just see it. This is an old idea, and it doesn't hold up well against the way AI is actually built and discussed today. Machine learning researchers talk about "research taste" constantly. It's a feel for which problems are worth years of your life. Researchers recognize it in colleagues without being able to write down a rule for it, and some now say they recognize it in models too. So the absence of a written rule can't be the whole story.

The second is that taste comes from consequence. You don't download good judgment; you earn it. A bad price kills a product, and that failure teaches you something no lecture could. Taste, on this view, is built through a loop: judge, watch what happens, adjust, and repeat.

This is closer. Something like that loop already exists in reinforcement learning from human feedback (RLHF). In one familiar version, people compare a model's answers, their preferences shape a reward signal, and training adjusts the model. If a consequence-bearing feedback loop were enough, trained models should already have taste. In narrow ways, arguably some do. So the loop, by itself, isn't the answer either.

## What RLHF's loop is actually missing

Here's a hypothesis, and I want to flag it clearly as a hypothesis rather than a settled fact. Human taste seems to form through a loop that looks similar to RLHF on the surface (judge, watch what happens, reflect, adjust, repeat), with one extra step. Accumulated experience, filtered through reflection, calibrates into something more specific than raw intuition: a trained sense of what's fitting in one particular domain. That's taste. Not intuition in general, but intuition that's been aimed and sharpened by repetition and reflection together.

Taste doesn't travel easily. It takes shape in the domain where the cost was paid. A master carpenter does not automatically possess good taste in software architecture; a brilliant litigator does not necessarily have good taste in typography. Human taste is narrow, forged in the specific constraints and consequences of a single discipline. A general-purpose assistant can feel like a frictionless generalist, moving from joinery to typography in the same conversation. That ease tells me little about whose standards it's applying.

Line this up against RLHF and something looks absent. The rating step, the adjustment step, and the repetition are all there, at a scale no human could ever match. A rater may think hard before choosing one answer over another. When only the choice is recorded, the model inherits the verdict—a grade without the class, a scar without the wound. What doesn't carry over into the model is the reflection itself. Could the model develop a capacity of its own from many such verdicts? That's an empirical question, and I'd want better evidence before answering it.

## Who actually carries the cost

Push on "reflection" and a deeper question appears: what does reflection actually require? In a human, the one who judges, the one who lives with the outcome, and the one who judges next time are the same continuous person. The cost lands on oneself, and that self carries it forward. Reflection may not be a step you can simply bolt onto a loop. It may require someone still there to do it.

In preference-based training, one person's judgment can shape a model's answer to someone else months later. We can trace the influence of that feedback. Whether anyone inside the model feels the sting of being wrong and carries it into the next attempt is a separate question. That, I think, is the real gap. Not the rule. Not the feedback. Who bears it, and whether that someone is still there next time.

## Averages don't fit anyone

There's a second complication, independent of the first. Pooling feedback from people in different situations can favor an answer that does well on average, especially when the ratings come without the context that made them matter. But there is rarely one standard for "doing well" that holds across every circumstance a judgment might land in. What you get is closer to a statistical estimate than a judgment made for the specific case in front of you, the same effect you get from averaging a thousand faces into one smooth, symmetrical composite that resembles no actual face precisely. Fine-tuning on a narrower domain can reduce this problem. A model given enough context can even learn when an unusual answer fits. The harder case is a disagreement within the domain itself. When two editors on the same desk disagree for good reasons, whose standard should govern the piece, and who will answer for that choice?

## Memory isn't the fix people assume it is

Someone might object here: give a model memory across conversations, and haven't you rebuilt the continuous self this argument says is missing?

Not quite, and the distinction matters. What memory systems provide, as currently built, is informational continuity: facts about a person, stored and handed back at the next encounter. What the argument actually needs is experiential continuity, where the same self that felt an earlier mistake shows up changed by it for the next one.

Picture someone with severe amnesia. Before every meeting, you hand them a file: her name is Celine, she prefers being challenged over being flattered, last time you discussed an idea worth returning to. They can act consistently with the file. They might even seem, from the outside, like they remember you. But the person reading the file and the person who actually lived through the earlier conversation are not the same person. A file is a record of memory. It isn't memory. If taste requires this lived kind of continuity, not a record of experience but experience itself carried forward, then the next question is how humans actually build it. Here it's worth taking a detour through a very old story.

## What Cook Ding knew, and why it complicates things

There's an old story in the Zhuangzi about a butcher named Cook Ding (庖丁), who carves an ox without ever striking bone, guided by something past ordinary sight. "I go by intuition, not by what my eyes see," he says, and even he can't fully explain his method, only describe what it feels like from the inside. Whatever taste is, once it's formed, it seems to be this kind of knowledge: real, reliable, and resistant to being written down as a rule.

But the story complicates the argument as much as it supports it, and I think the complication is worth sitting with rather than smoothing over. Cook Ding's skill wasn't a sudden illumination. The text is explicit that his blade is nineteen years old and still as sharp as if it had just come from the whetstone—kept that way by his feel for the gaps. His mastery is gradual cultivation, not a discontinuous leap.

This matters because there's a real, old disagreement inside Chan Buddhism about this exact question: whether genuine insight comes through gradual practice (神秀's 时时勤拂拭, "polish constantly, don't let dust settle") or through a sudden, discontinuous seeing that accumulation alone doesn't guarantee (慧能's 本来无一物, "there was never anything there to gather dust on," where the seeing simply arrives whole rather than being built up piece by piece).

If taste is Cook Ding's kind of thing, earned through structured, reflective accumulation, then in principle it isn't obviously closed off to a machine. The question becomes an engineering one: what's missing from the accumulation, not whether accumulation could ever work at all. If taste is closer to the sudden kind, a discontinuous seeing that only a subject undergoing it could have, then no amount of structurally correct training closes the gap, because the gap was never about structure or duration in the first place.

I don't think this is settled, and I'd be overstating things to claim it is. What I'll say honestly is this: I currently believe the second kind of gap is real, and that it doesn't shrink the way the first kind does. But I hold that as an intuition, not a proof, the same way I'd want anyone to hold strong claims about consciousness in either direction.

## Two gaps, not one

This is the distinction the whole argument has been circling: there may be a behavioral gap between human and machine judgment, and a separate, different-in-kind existential gap.

The behavioral gap is about output, about how well a judgment fits the case in front of it. There's real commercial and scientific value in narrowing it, and I expect people will keep doing so for a long time.

A team can fine-tune a model on its own code reviews, use reinforcement learning to reward patches that pass its tests, or have the model critique and revise its first patch at inference time. All three can narrow the behavioral gap. When a patch passes every test and still wakes the on-call engineer at two in the morning, I wonder who inside the model, if anyone, carries that night into the next review.

The existential gap is about whether there's a continuous someone on the inside, bearing what happens and being changed by it. I don't think this gap shrinks the way the first one does, because it isn't clear it's a gap in the ordinary sense at all, something with more and less. It may be closer to a binary: either someone is home, or no one is. If that's right, "getting closer to closing it" might be a category error, the same way making a photograph more detailed never turns it into the person it depicts, no matter how much detail you add.

## What this means, practically, for us

I don't think this is a piece of AI anxiety. I think it's closer to a chance, or an invitation.

For most of the industrial and post-industrial era, a large part of what it meant to be a good worker, a good professional, and a good adult was to behave like a very reliable tool: consistent, predictable, not derailed by being personally affected by things, and not prone to caring beyond your assigned function. That was, in a real sense, what was asked of us.

If a large share of that behavioral competence can now be handled by something that was never a self to begin with, that doesn't diminish us. It removes a certain pressure to perform a role we were never actually suited for in the first place, the role of the unfeeling, infinitely consistent instrument. What's left, once that pressure lifts, isn't nothing. It's a fairly specific, recognizable list: being changed by a cost you actually bore, not just knowing you were wrong. An unprompted pull toward the truth someone would rather you didn't find, what an older tradition calls 求真, seeking truth for its own sake rather than because you were asked to look. Care that isn't pointed at an assigned goal. Judgment that costs the one making it something real.

None of this is a claim about what AI can produce. A good enough system can already generate outputs that resemble all four. The claim is narrower, and I think more durable: what may separate a person from a tool was never about what either one does. It's about whether someone is actually there, living through the weight of it. And right now, there's no way to check. Not yes. Not no. Just a gap, still open, that might be the most interesting thing left to study. Not because we'll ever close it, but because trying to understand it is one of the few things only we can do.

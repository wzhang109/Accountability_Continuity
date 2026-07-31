# The Gap That Can't Close

*On taste, machines, and what's left for us to become*

Ask anyone who works with AI long enough and they'll eventually say something like this: it has no taste. Not that it produces bad output — often it produces very good output. But there's a sense that something is missing, and people reach for the word "taste" because it's the closest word we have.

I want to take that claim seriously enough to test it, because I think it survives, but not for the reason most people assume.

## Two easy answers, and why neither holds

The first one is that taste follows no rule you can write down. You don't calculate that a sentence works—you just see it. This is an old idea. But it doesn't hold up well against the way AI is actually built and discussed today. Machine learning researchers talk about "research taste" constantly—a feel for which problems are worth years of your life, never written down as a rule, and yet real, and yet something models are increasingly said to have some version of. So the absence of a written rule can't be the whole story.

The second one is that taste comes from consequence. You don't download good judgment; you earn it—a bad price kills a product, and that failure teaches you something no lecture could. Taste, on this view, is built through a loop: judge, watch what happens, adjust, and repeat.

This is closer. But RLHF — the method used to train most of today's chatbots — is structurally exactly this loop. Output, human rating, adjustment, repeat, across millions of cycles. If a consequence-bearing feedback loop were enough, trained models should already have taste. In narrow ways, arguably some do. So the loop, by itself, isn't the answer either.

## What RLHF's loop is actually missing

Here's a hypothesis, and I want to flag it clearly as a hypothesis rather than a settled fact: human taste seems to form through a loop that looks similar to RLHF on the surface — judge, watch what happens, reflect, adjust, repeat — but with one extra step. Accumulated experience, filtered through reflection, calibrates into something more specific than raw intuition: a trained sense of what's fitting, in one particular domain. That's taste—not intuition in general, but intuition that's been aimed and sharpened by repetition and reflection together.

Crucially, this means taste does not transfer. It is inextricably bound to the specific domain where the cost was paid. A master carpenter does not automatically possess good taste in software architecture; a brilliant litigator does not necessarily have good taste in typography. Human taste is narrow, forged in the specific constraints and consequences of a single discipline. Large language models, by contrast, are designed to be frictionless generalists—optimizing for acceptable averages across every domain simultaneously, without ever anchoring to the lived constraints of one.

Line this up against RLHF and something looks absent. The rating step, the adjustment step, and the repetition are there, all at a scale no human could ever match. To be fair, reflection is not entirely absent from RLHF — the human raters presumably reflect before they score. But their reflection stays with them. The model inherits the verdicts, stripped of the deliberation that produced them—a grade without the class, a scar without the wound. What's not obviously there is reflection—and without it, it's unclear whether repetition and accumulation ever turn into anything like instinct at all, or just into a better-calibrated average. This needs real verification, not just intuition; it's entirely possible some functional analog to reflection is buried in how gradient updates aggregate across a model's own prior outputs, and I don't want to claim more certainty here than the evidence supports. But on the surface, the loop looks incomplete in exactly the step that seems to matter most.

## Who actually carries the cost

Push on "reflection" and a deeper question appears: what does reflection actually require? In a human, the one who judges, the one who lives with the outcome, and the one who judges next time are the same continuous person. The cost lands on oneself, and that self carries it forward. Reflection may not be a step you can simply bolt onto a loop—it may require someone still there to do it.

In a trained model, the rating shaping the next output came from one of thousands of different people, averaged across countless training runs. No one is there to feel the sting of being wrong and carry that sting into the next attempt. That, I think, is the real gap. Not the rule. Not the feedback. Who bears it, and whether that someone is still there next time.

## Averages don't fit anyone

There's a second complication, independent of the first. Even feedback with genuine consequences behind it, once pooled across many people and many situations, optimizes toward doing well on average. But there is rarely one standard for "doing well" that holds across every circumstance a judgment might land in. What you get is closer to a statistical estimate than a judgment made for the specific case in front of you — the same effect you get from averaging a thousand faces into one smooth, symmetrical composite that resembles no actual face precisely. A trained sense of taste will fit well exactly where a situation resembles the training average, and worse the further a real situation drifts from it. A person doesn't have this problem in quite the same way, because the same self recalibrates fresh every time for the case actually in front of them—not the average case.

## Memory isn't the fix people assume it is

Someone might object here: give a model memory across conversations, and haven't you rebuilt the continuous self this argument says is missing?

Not quite, and the distinction matters. What memory systems provide, as currently built, is informational continuity — facts about a person, stored and handed back at the next encounter. What the argument actually needs is experiential continuity—the same self that felt an earlier mistake, showing up changed by it, for the next one.

Picture someone with severe amnesia. Before every meeting, you hand them a file: her name is Celine, she prefers being challenged over being flattered, last time you discussed some idea worth returning to. They can act consistently with the file. They might even seem, from the outside, like they remember you. But the person reading the file and the person who actually lived through the earlier conversation are not the same person. A file is a record of memory. It isn't memory. If taste requires this lived kind of continuity—not a record of experience but experience itself, carried forward—then the next question is how humans actually build it. And here it's worth taking a detour through a very old story.

## What Cook Ding knew, and why it complicates things

There's an old story in the Zhuangzi about a butcher named Cook Ding (庖丁), who carves an ox without ever striking bone, guided by something past ordinary sight. "I go by intuition, not by what my eyes see," he says, and even he can't fully explain his method, only describe what it feels like from the inside. Whatever taste is, once it's formed, it seems to be this kind of knowledge: real, reliable, and resistant to being written down as a rule.

But the story complicates the argument as much as it supports it, and I think the complication is worth sitting with rather than smoothing over. Cook Ding's skill wasn't a sudden illumination—the text is explicit that his blade is nineteen years old and still fresh from the whetstone— kept sharp not by grinding but by knowing where the gaps are. His mastery is gradual cultivation, not a discontinuous leap.

This matters because there's a real, old disagreement inside Chan Buddhism about exactly this question—whether genuine insight comes through gradual practice (神秀's 时时勤拂拭, "polish constantly, don't let dust settle") or through a sudden, discontinuous seeing that accumulation alone doesn't guarantee (慧能's 本来无一物, "there was never anything there to gather dust on"—the seeing simply arrives, whole, not built up piece by piece).

If taste is Cook Ding's kind of thing—earned through structured, reflective accumulation—then in principle it isn't obviously closed off to a machine. The question becomes an engineering one: what's missing from the accumulation, not whether accumulation could ever work at all. If taste is closer to the sudden kind—a discontinuous seeing that only a subject undergoing it could have—then no amount of structurally correct training closes the gap, because the gap was never about structure or duration in the first place.

I don't think this is settled, and I'd be overstating things to claim it is. What I'll say honestly is this: I currently believe the second kind of gap is real and that it doesn't shrink the way the first kind does. But I hold that as an intuition, not a proof—the same way I'd want anyone to hold strong claims about consciousness, in either direction.

## Two gaps, not one

This is the distinction the whole argument has been circling: there may be a behavioral gap between human and machine judgment and a separate, different-in-kind existential gap.

The behavioral gap is about output — how well a judgment fits the case in front of it. This gap can plausibly be narrowed, maybe indefinitely, through better training, better reflection-like mechanisms, better everything. There's real commercial and scientific value in narrowing it, and I expect people will keep doing so for a long time.

The existential gap is about whether there's a continuous someone on the inside, bearing what happens and being changed by it. I don't think this gap shrinks the way the first one does—because it isn't clear it's a gap in the ordinary sense at all, something with more and less. It may be closer to a binary: either someone is home, or no one is. If that's right, "getting closer to closing it" might be a category error—the same way getting a photograph more detailed never turns it into the person it depicts, no matter how much detail you add.

## What this means, practically, for us

I don't think this is a piece of AI anxiety. I think it's closer to a chance or an invitation.

For most of the industrial and post-industrial era, a large part of what it meant to be a good worker, a good professional, and a good adult was to behave like a very reliable tool—consistent, predictable, not derailed by being personally affected by things, and not prone to caring beyond your assigned function. That was, in a real sense, what was asked of us.

If a large share of that kind of behavioral competence can now be handled by something that was never a self to begin with, that doesn't diminish us. It removes a certain pressure to perform a role we were never actually suited to in the first place—the role of the unfeeling, infinitely consistent instrument. What's left, once that pressure lifts, isn't nothing. It's a fairly specific, recognizable list: being changed by a cost you actually bore, not just knowing you were wrong. An unprompted pull toward the truth someone would rather you didn't find—what an older tradition calls 求真, seeking truth for its own sake, not because you were asked to look. Care that isn't pointed at an assigned goal. Judgment that costs the one making it something real.

None of this is a claim about what AI can produce — a good enough system can already generate outputs that resemble all four. The claim is narrower, and I think more durable: what may separate a person from a tool was never about what either one does. It's about whether someone is actually there, living through the weight of it. And right now, there's no way to check. Not yes. Not no. Just a gap, still open, that might be the most interesting thing left to study—not because we'll ever close it, but because trying to understand it is one of the few things only we can do.

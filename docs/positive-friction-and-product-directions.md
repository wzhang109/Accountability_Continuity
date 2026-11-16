# Easier to check, or easier to believe?

*Research and product note · 16 November 2026*

I brought this question to my pitch at Foresight Vision Weekend: when we put evidence beside an AI recommendation, do we help people check it, or simply make it more convincing?

It is a small interface question within a broader concern of mine: how to build AI-supported work environments where people can use their judgment, keep learning, and take responsibility for decisions.

## What I want to understand

Imagine reviewing an AI-drafted recommendation. The source is available, but you are short on time. Would showing the relevant passage beside the recommendation help you spot a mistake? Would it make the recommendation seem more trustworthy even when the passage does not support it?

The [current evidence-access proposal](../studies/organizational-coordination/evidence-access-pilot/README.md) compares an immediately visible passage with the identical passage available through one click. Both groups can open the full document. This changes how evidence is encountered, including its visibility and salience; it does not isolate the effort of a click.

I would look at errors caught alongside correct recommendations sent back unnecessarily. A design that makes people reject everything would not solve the problem.

## When might a pause help?

A possible extension is to require someone to open the source before they can approve a recommendation. I think of this as a question about “positive friction”: when is an extra step worth asking someone to take?

There are reasons it might fail. Someone could learn to click through without reading. An added step could become irritating, slow down straightforward decisions, or give a team false confidence that review has happened.

That makes it a separate question from the current proposal. Making evidence easier to find and requiring people to open it are different design choices. A later comparison could hold evidence presentation constant while changing whether opening it is required. The useful outcome would be better decisions at a reasonable time cost. Opening a source, by itself, would not count as success.

## Where this could lead

I can imagine a practical tool for teams that review AI-drafted analysis: an interface that keeps recommendations close to their sources, lets reviewers flag uncertainty or ask for a correction, and carries that information forward to the next person.

Research and policy teams would be a starting point to explore. A useful first conversation would be about a recent piece of work: what needed checking, what made it difficult, and what happened after someone raised a concern?

There may be a commercial opportunity in building such interfaces, or helping organizations evaluate the review workflows they already use. Before choosing a product, I would need to learn whether this is a recurring problem, how existing tools handle it, who would use or buy a solution, and whether the improvement is worth the cost.

Review records could help a team reconstruct what happened. They would show observable actions, such as opening a source or requesting a correction. They would not prove that someone understood the evidence, establish legal compliance, or settle who should be accountable.

## Where the work stands

The repository contains fictional cases, allocation code, and synthetic analysis checks for the evidence-access comparison. No participants have taken part. The required-source-viewing idea is a proposed extension, and commercial demand has not been tested.

My next step is to seek feedback on the task and interface from people who review AI-assisted work, then refine the pilot before collecting participant data. Any study would need an appropriate consent, privacy, and ethics-review plan.

The larger questions about learning, agency, and responsibility will need more than a short interface experiment. This is one place to begin.

---

*This note develops my research motivation and Vision Weekend pitch. AI tools assisted with drafting and editing.*

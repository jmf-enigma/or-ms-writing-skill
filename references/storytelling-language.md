# Storytelling And Language

Use this when the user says the writing should be readable, logical, "say it like a human," or tell a story.

## The OR/MS Story Spine

Good OR/MS writing is not decorative storytelling. It is a disciplined causal path:

1. **Actor**: platform, seller, regulator, manager, customer, patient, driver, worker, algorithm.
2. **Decision**: price, match, allocate, recommend, inspect, disclose, regulate, learn, wait.
3. **Friction**: limited information, strategic behavior, fairness, churn, capacity, ambiguity, externality, delay.
4. **Model/Method**: formalizes the friction in the smallest useful way.
5. **Result**: identifies a threshold, ranking, impossibility, policy structure, or comparative static.
6. **Consequence**: tells the reader when to act differently.

If a paragraph lacks actor + decision + friction, it will read abstract and lifeless.

## Plain-English Discipline

- Start paragraphs with a concrete decision or tension before naming the technique.
- Prefer verbs with actors: "a platform learns," "a seller chooses," "a regulator restricts," "customers leave."
- Translate every formal object once: "the fairness parameter controls how similar prices must be across groups."
- Use "because" sentences for mechanism. Use "when" sentences for conditions.
- Give the paragraph one live turn when the local job needs story: old belief to missing friction, current objective to unintended consequence, method default to decision mismatch, result to boundary, or mechanism to alternative mechanism.
- Keep one technical noun stack per sentence at most. If a sentence has three stacked concepts, split it.
- Avoid empty connective tissue: "In today's fast-paced world," "plays a crucial role," "is of great importance."
- Replace vague "insight" with the actual implication.
- Avoid machine-like cadence. Do not lean on "not only ... but also," "this underscores," "this highlights," "it is worth noting," or repeated "by doing so" transitions.
- Avoid colon, semicolon, and dash scaffolding. If a sentence has the shape "The implication is ..." followed by a punctuation reveal, rewrite it as a direct sentence with a subject and verb.
- Avoid "This enables/allows/ensures" openings unless the previous sentence gives a precise antecedent. Prefer naming the actor or mechanism.
- Avoid itinerary cadence such as "we first..., we then..., finally..." unless the passage is a roadmap. In abstracts and result interpretation, name the decision object, formal result, benchmark, or mechanism instead of narrating the author's sequence of work.
- Avoid weak `which allows/enables` clauses. If the relative clause points to an entire sentence, rewrite with the actual subject: the theorem, estimator, field design, decomposition, or policy comparison.
- Avoid everything as bullets. Use bullets only when the reader needs to compare parallel items. In introductions and result interpretation, prose usually reads better.

## Sentence Moves That Work

Use these as reasoning moves, then rewrite them in the paper's own nouns.

- Move from the obvious difficulty to the deeper operational tension.
- Explain why a distinction matters by naming the mechanism it changes.
- Let the model isolate one force through a clear abstraction.
- State conditional results in two sentences when one sentence feels crowded: first the regime where the policy helps, then the regime where it can fail.
- Recast managerial implications as a changed decision, not as a slogan.
- Use the benchmark to show what is captured and what is missing.
- Let the design separate one mechanism from a nearby alternative; do not call the design "useful" without saying what it separates.

## Rewrite Patterns For Banned Punctuation

- Colon reveal: change "The mechanism is X" plus explanation into two sentences.
- Semicolon chain: split into two sentences or use "because," "although," or "whereas."
- Dash pivot: replace the dash with a period, then make the second clause explain the first.
- Spaced hyphen: treat it as a dash and rewrite.

## Rewrite Patterns For Generic AI Prose

- Puffery: replace "crucial, pivotal, robust, cutting-edge, seamless" with the exact theorem, estimate, or operational effect.
- Empty "-ing" phrase: replace "highlighting the importance of X" with "X changes Y when Z holds."
- "This enables" sentence: name what enables what and why.
- Itinerary prose: replace the author's work order with the reader's logic. A paragraph should not sound like a project-management update unless it is a roadmap.
- Weak "which allows" clause: name the mechanism or formal object rather than letting "which" carry the argument.
- Over-parallel list: vary the rhythm or turn the list into a sentence if the items are not truly comparable.
- Passive abstraction: replace "it is shown that" with "Proposition 1 shows" or "the model shows."

## Telling A Story Without Overclaiming

- Do not claim a model "solves" an industry problem; say what decision it clarifies.
- Do not turn every result into advice. Some results are warnings, impossibility statements, or boundary conditions.
- Do not hide assumptions. Use them to tell the reader what the model isolates.
- If the result is counterintuitive, first state the intuition the reader likely has, then explain the force that overturns it.

## Before / After Logic

Weak: "We study an important revenue management problem with fairness constraints."

Better structure: "Personalized pricing can increase revenue, but it can also charge protected groups systematically different prices. We study how a seller's pricing decision changes when fairness is imposed as an explicit constraint."

Weak: "Our model has many managerial implications."

Better structure: "The model implies that regulators should first choose the fairness notion they want to enforce; imposing multiple notions can be infeasible even in simple markets."

## Final Read-Aloud Check

After drafting, ask:

- Can a domain expert explain the paragraph to a manager after reading it once?
- Does the paragraph say who makes the decision and what changes?
- Does every technical term earn its place?
- Does the last sentence teach the reader something, or merely restate the first sentence?

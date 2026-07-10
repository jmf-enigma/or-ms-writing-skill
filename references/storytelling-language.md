# Storytelling And Language

Use this when the user says the writing should be readable, logical, "say it like a human," or tell a story.

## The OR/MS Story Core

Good OR/MS writing is not decorative storytelling. It makes the paper's central relation and support easy to recover. Depending on the passage, the active objects may include:

1. **Actor**: platform, seller, regulator, manager, customer, patient, driver, worker, algorithm.
2. **Decision**: price, match, allocate, recommend, inspect, disclose, regulate, learn, wait.
3. **Friction**: limited information, strategic behavior, fairness, churn, capacity, ambiguity, externality, delay.
4. **Model/Method**: defines, estimates, tests, or computes the relevant object.
5. **Result**: identifies a threshold, ranking, impossibility, policy structure, estimate, comparison, or bound.
6. **Consequence or boundary**: changes a decision or belief, or marks where the result stops.

Do not require all six. A definition paragraph may need only the formal object and its role. A theorem paragraph may need the result, condition, and benchmark. A transition may need only a stable noun and a clear change of scope. Abstractness is a problem when the reader cannot identify the object or relation, not merely because an actor or friction is absent.

## Plain-English Discipline

- In motivation passages, make the decision, formal object, or tension legible before asking the technique to carry the argument. In method and result sections, a direct formulation or result-first opening can be natural.
- Prefer verbs with actors: "a platform learns," "a seller chooses," "a regulator restricts," "customers leave."
- Translate every formal object once: "the fairness parameter controls how similar prices must be across groups."
- Use `because` only for a reason or mechanism and `when` only for a condition or regime. Neither word is required when the relation is already clear.
- When the local job needs movement, make one consequential relation clear: definition to use, evidence to claim, benchmark to comparison, mechanism to outcome, whole to decomposition, result to boundary, or one scope to another. Do not add a reversal merely to make the paragraph feel like a story.
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

- Move from one object to the next only through the relation the paper actually establishes.
- Explain why a distinction matters by naming the mechanism it changes.
- Let the model isolate one force through a clear abstraction.
- State conditional results in two sentences when one sentence feels crowded. The favorable regime, failed regime, or general claim may come first according to emphasis and setup.
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
- If the result is counterintuitive, make both the relevant intuition and the force that overturns it visible. Either may come first when the comparison remains clear.

## Before / After Logic

Weak: "We study an important revenue management problem with fairness constraints."

Better structure: "Personalized pricing can increase revenue, but it can also charge protected groups systematically different prices. We study how a seller's pricing decision changes when fairness is imposed as an explicit constraint."

Weak: "Our model has many managerial implications."

Better structure: "The model implies that regulators should first choose the fairness notion they want to enforce; imposing multiple notions can be infeasible even in simple markets."

## Final Read-Aloud Check

After drafting, ask:

- Can a domain expert explain the paragraph to a manager after reading it once?
- Does the paragraph make its central object, relation, and support recoverable?
- Does every technical term earn its place?
- Does the ending complete the paragraph's burden, qualify it, or move the argument forward without a forced teaser?

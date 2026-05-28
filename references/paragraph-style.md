# Paragraph Style

Use this when the user wants a fixed-quality paragraph, rewrite, or section paragraph.

## Voice

- Precise, restrained, analytical.
- Human first, technical second: introduce the business or operational decision before the formal object unless the section is already technical.
- Prefer "we show," "we characterize," "we identify," "we establish," "we find" over inflated novelty language.
- Use "suggests," "indicates," "is consistent with," or "under our model" when evidence is conditional.
- Avoid unsupported "significant," "novel," "important," "dramatic," and "surprising."
- Use quiet punctuation. In polished prose, do not use colons, semicolons, em dashes, en dashes, double hyphens, or spaced hyphens as dash substitutes.
- If a draft contains one of those marks, first try to rewrite it as two sentences. Use parentheses only for short asides that would otherwise interrupt the sentence.

## Paragraph Contract

Every paragraph should have one dominant job. It may contain supporting details, but the reader should be able to say why the paragraph exists.

1. **Context paragraph**: phenomenon -> operational decision -> why it matters.
2. **Gap paragraph**: literature has X -> misses Y -> this paper studies Y.
3. **Model paragraph**: decision maker -> primitives -> objective -> why abstraction is useful.
4. **Result paragraph**: result -> mechanism -> condition -> implication.
5. **Comparison paragraph**: benchmark -> difference -> source of difference.
6. **Managerial paragraph**: action -> condition -> mechanism -> caveat.
7. **Transition paragraph**: summarize what was established -> motivate next analysis.

## Within-Paragraph Story Order

The order of sentences should follow the reader's state, not the author's notes.

Useful sentence orders:

- **Context paragraph**: known setting -> decision maker -> decision -> friction.
- **Gap paragraph**: closest prior view -> maintained assumption -> missing object -> paper question.
- **Model paragraph**: decision environment -> information/timing -> control -> objective -> why the abstraction is useful.
- **Empirical design paragraph**: setting -> treatment or variation -> comparison -> outcome metric -> credibility threat addressed.
- **Result paragraph**: result or estimate -> benchmark or contrast -> mechanism -> boundary or interpretation.
- **Proof idea paragraph**: result target -> constructed object -> hard term -> proof move -> appendix verification.
- **Robustness paragraph**: threat -> check -> conclusion -> appendix details if secondary.

Do not use all elements every time. The point is sequence: each sentence should make the next sentence easier to understand.

## Between-Paragraph Story Order

A section feels coherent when the last sentence of one paragraph prepares the first sentence of the next.

Good handoffs:

- A setting paragraph ends with a friction; the next paragraph explains why existing work or current practice does not resolve it.
- A gap paragraph ends with a question; the next paragraph introduces the model, data, or design that answers it.
- A design paragraph ends with the comparison it makes credible; the next paragraph reports the main result.
- A result paragraph ends with an unresolved mechanism; the next paragraph tests, models, or explains that mechanism.
- A theorem paragraph ends with a condition; the next paragraph explores comparative statics, boundary cases, or implementation.

Weak handoffs:

- A paragraph ends with a broad implication and the next begins with notation.
- A result appears before the reader knows the benchmark.
- A robustness paragraph appears before the main estimate has been interpreted.
- A proof detail appears before the theorem's economic or operational meaning is clear.

## Clarity And Concision Pass

Use this pass after the paragraph has the right logic.

- Make the actor grammatical subject when possible.
- Prefer active voice unless the object or result matters more than the actor.
- Use positive form. Say what the model does, not only what it does not do.
- Choose concrete nouns and specific verbs. Replace "provides insights into" with the actual action, condition, or comparison.
- Omit needless words. Remove "in order to," "it is important to note," "the fact that," "various," "several," and unsupported intensifiers.
- Keep related words together. Do not separate a subject from its verb with a long methodological aside.
- Put emphasis at the end of the sentence. End on the decision, mechanism, condition, or result rather than a filler phrase.
- Vary sentence openings. Do not start three consecutive sentences with "This," "We," or "Our."

## Paragraph Repair Patterns

Use these only when a paragraph is missing a local job. They describe movement, not final paragraph templates. After choosing a movement, write ordinary sentences in the paper's own nouns.

### Motivation Pattern

Move from phenomenon to decision maker, then to the tradeoff that makes the decision nontrivial. If a method enters, name the exact mechanism it isolates rather than writing a `which allows` clause.

### Gap Pattern

Move from the closest stream to the assumption it holds fixed. Then state the paper's departure and why that departure changes the decision or outcome.

### Contribution Pattern

Group contributions by what the reader learns. A contribution paragraph usually needs the result object, the evidence type, and the precise departure from prior work; it does not need a perfectly parallel numbered list.

### Result Interpretation Pattern

State the proposition in words, then explain the mechanism or comparison that makes it true. Put the condition close to the action or interpretation it supports.

### Managerial Implication Pattern

Name the decision maker, observable condition, action, and metric. If the action can fail, give the failure condition before the recommendation starts to sound universal.

## Revision Checklist

- First sentence tells the reader what the paragraph is for.
- No sentence makes a claim that the paragraph cannot support.
- Sentences appear in the order the reader needs: known object, new relation, evidence, interpretation, handoff.
- The paragraph handoff is visible: the last sentence prepares the next paragraph's object or question.
- Technical terms are defined before being used.
- The last sentence either interprets the result or moves the reader forward.
- Citations are used to position the paper, not to replace explanation.
- Punctuation is quiet. If the paragraph contains any colon, semicolon, dash pivot, or "X, which ..." chain, rewrite before finalizing unless the mark is required by a venue or mathematical notation.
- The paragraph does not rely on puffery, repeated sentence openers, empty "-ing" phrases, or a generic "This enables/allows/highlights" sentence.

## Story Check

Before finalizing, verify that the paragraph has:

- a decision maker or actor,
- a decision,
- a friction or tradeoff,
- a result or evidence,
- a consequence for action, theory, or interpretation.

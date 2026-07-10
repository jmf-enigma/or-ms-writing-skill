# Management Science Model, Proof, And Equation Layout

Use this when the user asks how to write a model section, mathematical process, derivation, theorem, proof sketch, appendix proof, or body-versus-appendix split in Management Science style. The goal is to decide what equations belong in the body, what formulas move to the appendix, and how prose should surround each display. These are layout and exposition patterns, not templates to copy.

## Paper Signals

These notes draw especially on model/proof sections from:

- Cao, "Collaborative Learning and Decision Making on Pricing and Recommendation," Management Science, 2025.
- DeValve and Myles, "Approximation Algorithms for Dynamic Inventory Management on Networks," Management Science, 2024.
- Guo, "The Mnemonomics of Contractual Screening," Management Science, 2022.
- Loewenstein et al./related MS theory papers with baseline model plus appendix extensions.
- Payment for ecosystem services contract papers with short body proof sketches and complete appendix proofs.
- Recent open INFORMS examples with body/appendix pairings: model-theory papers that keep theorem meaning in the body and proofs in labeled appendix subsections; applied optimization papers that keep the reformulation in the body and notation/proof details in online appendices; ML/empirical papers that keep the primary model and comparison in the body and auxiliary baselines in appendices.
- Recent full-text close readings of dynamic pricing/matching, matching queues with incentives, policy-gradient guarantees, recommendation-based demand estimation, and GAI-screening papers. These papers are useful because they show how the body moves from an operating object to notation, then from a theorem to interpretation and appendix verification.
- Additional full-text checks from AI calibration experiments, competitor-information field experiments, automation field evidence, bargaining/information acquisition theory, optimal learning/control, and energy DP papers. These show that model writing includes construct measurement, empirical frameworks, potential outcomes, short mechanism models, and applied optimization formulations, not only theorem-first analytical models.
- Bertsimas and Kallus, "From Predictive to Prescriptive Analytics," which defines its conditional optimization object early, uses an illustrative example before the general theory, and translates its prescriptiveness metric in the application.
- Ban and Rudin, "The Big Data Newsvendor," which organizes the introduction around substantive questions, states section conclusions before appendix handoffs, and reserves the electronic companion for full proofs and dependencies.
- Elmachtoub and Grigas, "Smart Predict, then Optimize," which moves from a decision loss to computational difficulty, a convex surrogate, consistency, algorithms, and experiments.
- Besbes and Zeevi, "Dynamic Pricing Without Knowing the Demand Function," which makes the full-information benchmark and regret metric do both mathematical and economic work.
- Ferreira, Lee, and Simchi-Levi, "Analytics for an Online Retailer," which earns the model through the operating workflow, explains a theorem's bound and proof mechanism in the body, and places implementation details in the appendix.
- Cachon and Swinney, "The Value of Fast Fashion," which uses a one-line `Proof.` pointer directly below lemmas and then gives the economic interpretation. This is evidence against treating complete body proofs as the only legitimate use of the label.

## What Main-Text Equations Do

Main-text displays usually perform one of five jobs:

1. **Define the system**: state variables, evolution equations, budget constraints, transition laws, utility/payoff, or feasibility.
2. **Define the decision problem**: objective, feasible policy class, benchmark, optimization problem, or estimand.
3. **Create the analysis object**: relaxation, lower bound, regret decomposition, implicit revenue, uncertainty set, estimator, or stochastic program.
4. **State the headline result**: theorem condition, approximation factor, regret bound, identification expression, threshold, or policy rule.
5. **Support a body proof idea**: one key inequality or decomposition that explains why the theorem is credible.

If a display does none of these jobs, it probably belongs in the appendix or should be prose.

Empirical equations have analogous jobs. A display may define a construct, an elicited belief measure, a treatment contrast, a potential outcome, an estimating equation, or a counterfactual exercise. It belongs in the body when the reader needs it to understand the claim; it belongs in the appendix when it is an alternative coding, repeated robustness specification, or implementation detail.

## Body Formula Choreography

A body display needs a recoverable role, not a mandatory prose sentence on each side.

- Make clear whether the display defines state evolution, states the firm problem, gives a lower-bound program, records an estimand, or decomposes a proof term. That role may be established by the preceding paragraph or subsection heading.
- Show only the object needed for later results. Number it if it is referenced later.
- Translate central variables and consequential modeling choices before or after the display according to dependency. A display can open a technical subsection when its role is already active.

Good MS body writing often looks like this:

- Prose defines inventory/backlog/process variables.
- Two short displayed equations give the state evolution.
- Prose says the policy is nonanticipating and defines the objective.
- One displayed optimization problem states the firm problem.
- Prose explains intractability and introduces the policy or bound.

Or, in learning/regret papers:

- Prose defines the policy space and equivalent randomized policy.
- Displays define implicit revenue, implicit regret, and predicted regret.
- One displayed equality decomposes regret.
- A short proof idea says which lemmas control each term.
- Later inequalities are shown only if they are the load-bearing bounds; full proofs move to Online Appendix EC sections.

## Formula Density In The Body

Use more than one consecutive display only when the paper is defining a system or the displays form a single logical object.

Appropriate consecutive displays:

- inventory and backlog evolution equations;
- objective and feasibility constraints;
- definition of revenue, regret, and predicted regret before a decomposition;
- policy rule components that are used together;
- theorem condition followed by the bound.

Inappropriate consecutive displays:

- algebraic simplifications that only verify a theorem already stated;
- repeated cases of the same inequality;
- constants that never change the reader's interpretation;
- KKT lines or complementary slackness unless they are the characterization itself.

If the body has three or more displays in a row, add prose that tells the reader what changed between them.

## Model Section Layout

Use a dependency inventory rather than a universal order:

- operational, economic, empirical, or formal object;
- agents or system, timing, state, information, and actions;
- notation used by later statements;
- system evolution, payoff, budget, utility, estimand, or feasibility;
- objective, decision problem, comparator, solution concept, or optimal value;
- analytical role, difficulty, or abstraction boundary.

Select only what the model needs. A practice-led paper may explain the operating process before notation. A technical algorithm paper may begin with a canonical formulation, state, or policy class. In either case, explain each consequential state, control, construct, and comparator by the time a theorem or estimate relies on it.

Close-reading update: many practice-led MS/OR model sections open with the real operating process. A two-sided queueing paper says customers and servers arrive, wait, are matched, and generate profit before introducing the bipartite graph and arrival processes. A screening paper identifies sender, receiver, signal, effort, and expertise before showing the signal equation. These are examples of environment-first exposition, not evidence that every technical paper should use it.

Construct-heavy empirical papers must connect construct meaning, observation or elicitation, the displayed measure, and coefficient or prediction interpretation. Definition-first is often clearest, but a compact formal definition may precede ordinary-language explanation. The hard dependency is that validation and construct meaning are available before later claims rely on the measure.

Potential-outcome and regression passages should be written as design prose, not just formulas. Make treatment, control, outcome, unit, sample, comparison, coefficient interpretation, and identifying variation recoverable across the local passage. A display may come first when prior context has activated those objects. If the paper cannot fully separate nearby channels, say so and use `suggestive`, `consistent with`, or `difficult to cleanly disentangle`.

## Observed Main-Text Math Paths

Recent MS/OR full texts show several ways that formulas become readable in the body. These paths are examples, not required sequences.

- **Equilibrium model path**: prose names the actors, timing, information, and objective; displays define the demand, payoff, or expected sales object; the proposition characterizes equilibrium; the following paragraph explains each regime or strategic channel. Verification, long cases, and repeated inequalities move to the appendix.
- **Benchmark comparison path**: make both the baseline and first-best, centralized, relaxed, or complete-information object recoverable before interpreting their comparison. Either result may appear first. Explain the distortion, constraint, or information channel only when the analysis establishes it.
- **Approximation path**: connect the exact object, computational difficulty, approximation or surrogate, performance theorem, and numerical evidence. An approximation can be stated early when its target and role are already clear.
- **Potential-outcome path**: connect units, treatment, control, outcomes, potential outcomes, coefficient of interest, and the assumption or randomization supporting the treatment-effect interpretation. Their prose/display order can follow the active design context.
- **Mechanism-regression path**: connect a possible channel, interaction or fine-grained measure, estimate, and permitted mechanism claim. The channel or estimate may lead; do not require a mechanism section to mimic the main-effect section's order.
- **Appendix-proof path**: the appendix can begin directly with binding constraints, first-order conditions, HJB verification, coupling details, or case analysis because the body has already explained the object and meaning. The body should not make the appendix carry the first explanation of why the result matters.

When deciding whether a mathematical step belongs in the body, ask whether it creates an object the reader will use later. A virtual surplus, threshold, Bellman objective, potential outcome, or value-function approximation may belong in the body. A derivative check, repeated case split, constant definition, or table of alternative codings usually belongs in the appendix.

## Theorem And Result Layout

A theorem in the body belongs to a local result package. The setup and conditions must be available by the statement; the exact assumption, policy class, comparator, and conclusion belong in the statement when they define its scope; and needed interpretation should remain nearby. Interpretation may precede a short proof, follow it, or bracket the result according to the manuscript's convention.

For approximation and regret results, nearby prose may need to say:

- what the comparator is;
- what parameter makes the problem hard;
- when the factor or rate is useful;
- how the result differs from the standard model.

For structural results, nearby prose may need to say:

- what the policy/equilibrium/threshold looks like;
- which parameter or state determines the regime;
- what decision implication follows.

## Theorem And Proposition Captions

The result label should not do the work of the result paragraph.

- Default to bare labels: `Proposition 1.`, `Theorem 1.`, `Lemma 1.`.
- Use short parenthetical captions only when they help navigation across many results: `Theorem 1 (Approximation Guarantee)`, `Lemma 2 (One-Step Improvement)`, `Proposition 3 (Platform Revenue)`.
- Keep captions noun-like. They should name a result type, object, or mechanism, not state the whole claim.
- Do not use long colon titles after propositions. The claim belongs in the formal statement and the interpretation paragraph.
- Do not add a subheading between a proposition and its interpretation unless the paper has a repeated, long structure that makes the heading necessary.

Good local shape:

```text
The next proposition characterizes the platform's optimal disclosure rule when sellers are symmetric.

Proposition 1.
[Formal statement.]

The proposition shows that disclosure becomes less precise as seller congestion increases. The condition matters because...
```

Also acceptable in a result-heavy technical section:

```text
Theorem 2 (Regret Bound).
[Formal statement.]
```

Avoid:

```text
Proposition 1: The Platform Should Reduce Disclosure Because Congestion Dominates Information Benefits
Key Insight.
[Interpretation.]
```

Some papers place the key derivation before the proposition rather than after it. This works when the derivation creates the threshold, objective, or comparison that the proposition then characterizes. Do not move that derivation to the appendix merely because it is mathematical; move only the verification steps that do not change the reader's understanding of the result.

## Proof Placement After A Theorem Or Proposition

There is no single MS/OR rule that every proposition must be followed by a formal proof in the body. Follow the target journal and the paper's established convention consistently. Five patterns occur in full texts.

### Pattern 1: Proposition, Complete Short Proof, Interpretation

Use this when the proof is short, self-contained, and helps the reader see the mechanism.

```text
Proposition 1.
[Formal statement.]

Proof.
[Two to four short paragraphs or displays that prove the claim.]

[Interpretation paragraph that explains what the result means for the model, benchmark, or decision.]
```

This pattern is common in compact theory sections and simple analytical models. The proof under `Proof.` must be a real proof, not only intuition. It should not rely on long hidden lemmas, repeated cases, or constants that belong in an appendix.

This is one legitimate use of `Proof.`, but it is not the only one.

### Pattern 2: Proposition, One-Line Formal Proof Pointer, Interpretation

Some MS papers use the proof environment only to record where verification appears.

```text
Lemma 1.
[Formal statement.]

Proof. All proofs appear in the appendix.

[Interpretation paragraph that explains the economic or operational content.]
```

This convention is legitimate when it matches the journal or manuscript format and is used consistently. The pointer is not a proof sketch and does not explain the result. Nearby ordinary prose must still tell the reader what the lemma changes and why it matters.

Do not "correct" a source-faithful one-line proof pointer into a complete body proof merely because the label says `Proof.`. Also do not invent this convention in an otherwise unlabeled manuscript without checking the target format.

### Pattern 3: Proposition, Interpretation, Appendix Pointer

Use this when the theorem is important but the proof is routine, algebraic, or long.

```text
Proposition 1.
[Formal statement.]

[Interpretation paragraph: what the proposition characterizes, which condition matters, and how it differs from the benchmark.] The proof is in Appendix A.
```

This is often the cleanest Management Science style because the body keeps result meaning and the appendix carries verification.

If all proofs are in the appendix, say that once in the model or analysis section only when helpful. Still give each proposition enough body interpretation that the reader can evaluate its role without opening the appendix.

### Pattern 4: Proposition, One Proof Move, Appendix Proof

Use this when the proof technique is part of the contribution or the result would otherwise feel like a black box.

```text
Proposition 1.
[Formal statement.]

[One short paragraph explaining the constructed object, hard term, and proof move.] Appendix A gives the complete proof.
```

Do not label this paragraph `Proof.` when the paper uses that label for complete proofs. Usually do not label it `Proof idea` either; write it as normal prose after the result. If the paper uses the one-line pointer convention in Pattern 2, keep the proof move outside that formal pointer so the reader can distinguish location from explanation.

This pattern is especially common when the body needs only the credibility bridge. For example, a lower-bound theorem may state the rate, then give one paragraph explaining the trade-off between expected queue length and revenue loss before sending the detailed coupling, Taylor expansion, and tail-probability work to the appendix.

### Pattern 5: Technical OR Body Proof

Use this in focused OR theory or algorithm papers when proof logic is the paper's main contribution and the journal expects technical development in the body.

```text
Theorem 1.
[Formal statement.]

Proof.
[Full proof, possibly with lemmas, but still signposted.]
```

Even here, auxiliary algebra, constants, and repeated cases can move to a regular appendix if the body proof gives the main argument.

## What Feels Weird

Proof placement often feels wrong when the label and content do not match.

- `Proof.` followed by intuition only: rename it as ordinary explanatory prose or complete the proof.
- One-line `Proof.` pointer treated as if it explained the result: keep the venue-style pointer if appropriate, but add a nearby interpretation paragraph.
- Proposition followed by an appendix pointer and then no interpretation before the section moves on: add a local result paragraph.
- Long appendix proof copied into the body: keep the theorem, one proof move, and interpretation; move verification out.
- Body proof idea after every proposition: use it only when reviewer trust needs it.
- Inconsistent local convention: do not alternate among full body proofs, one-line proof pointers, and unlabeled sketches without a reason the reader can infer.

## Body Proof Sketch Layout

A body proof sketch should be short and load-bearing.

Useful moves:

1. State what object is decomposed, relaxed, coupled, or bounded.
2. Show one displayed decomposition or inequality if the reader must see it.
3. Name the lemmas or appendix results that control the terms.
4. State how combining those terms yields the theorem.
5. Send full algebra, cases, constants, and auxiliary lemmas to the appendix.

For Management Science, proof-sketch prose should be literal. Use verbs such as define, decompose, construct, relax, bound, compare, combine, and apply. Do not make the proof sound like a story.

Observed proof-idea rhythm in strong MS/OR papers:

1. Fix the object or reduction: a sample path, Bellman objective, coupling, fluid benchmark, dual, or policy-improvement problem.
2. Name the difficult term: queue length, Bellman error, incentive response, revenue loss, rejection probability, or approximation error.
3. Name the proof move: decompose, compare, bound, condition, apply, or combine.
4. Close the loop: say how this yields the theorem and where the complete proof appears.

Use `we first...` only when the reader is inside a genuine proof roadmap. In polished body prose, a direct sentence is often better: `The proof couples arrivals across policies and bounds the expected queue length by comparing the process with a heavy-traffic M/M/1 queue.`

The body proof idea usually has zero or one display. Use a display only for the decomposition, inequality, or reduced system that the rest of the paper relies on. If a second display merely verifies the first, move it to the appendix.

Proof-idea language should be almost invisible. Good body prose says, for example, that the proof reduces the full information history to a hybrid belief state, decomposes regret into estimation and control terms, or compares a relaxed policy with the original policy. It usually does not announce `Proof idea:` unless the surrounding paper has a repeated formal proof-sketch convention.

## Appendix Proof Layout

Appendix proofs are denser, but they still have structure.

Typical appendix order:

1. Restate the theorem, proposition, or lemma target.
2. Fix the notation, assumptions, and events used in the proof.
3. Prove helper lemmas in the order they are used.
4. For each lemma, state the role before the algebra.
5. Use displayed equations for inequality chains, case splits, KKT systems, concentration events, or induction steps.
6. End by mapping the final inequality or construction back to the body result.

Appendix prose can say "We first show..." and "It remains to verify..." because the reader is following a technical argument. It should not say only "standard arguments" unless the exact standard result is cited and the mapping is clear.

For long appendices, organize sections by proof dependency or reviewer concern:

- definitions and notation before theorem proofs;
- proposition proofs in the same order as the body;
- closed-form or threshold expressions before figures that use them;
- robustness or alternative assumptions after the main proof;
- implementation and calibration details after the result they support.
- empirical details, variable construction, balance checks, placebo tests, and secondary robustness checks after the body has stated the main design and conclusion.

Start an appendix section with the section's job. A section that begins immediately with a symbol-heavy display often needs one orienting sentence.

## What Moves To Appendix

Move these out of the body:

- proof of auxiliary lemmas;
- equality verification for a displayed decomposition;
- constants and tuning parameters;
- repeated cases and boundary regimes;
- KKT verification and complementary slackness;
- concentration inequalities and summation bounds;
- algorithmic implementation details not needed to understand the policy;
- extra examples showing assumptions are satisfied;
- weaker or stronger variants of assumptions after the body explains the main condition.

Keep these in the body:

- the mathematical object the paper is about;
- the main optimization problem, estimator, policy, bound, or theorem;
- construct definitions, treatment contrasts, and measurement choices needed to interpret primary empirical results;
- one derivation checkpoint if it creates the object used later;
- one proof idea if the theorem otherwise looks like a black box;
- interpretation of the result and benchmark.

## Formula Placement Table

| Formula type | Body role | Appendix role |
|---|---|---|
| State evolution | Usually body if it defines the model | Boundary checks, variants |
| Objective/problem | Body when it defines the paper's formal object | Equivalent reformulations |
| Assumption inequality | Body if needed for theorem statement | Examples, sufficient conditions |
| Relaxation/lower bound | Body if it is the benchmark | Derivation and tightness proof |
| Regret decomposition | Body if it organizes the proof | Equality verification and term bounds |
| Key inequality | Body only if it explains proof idea | Full inequality chain |
| Algorithm rule | Body for decision logic and inputs | Pseudocode, tuning, runtime |
| KKT/FOC | Body only if it is the characterization | Verification and cases |
| Concentration bound | Body only if it is the named guarantee | Probability events and constants |
| Construct measure | Body if it defines the main estimand or mechanism | Alternative codings and validation tables |
| Regression or DID equation | Body if it is the primary empirical strategy | Robustness specifications and extra fixed-effect variants |
| Calibration or counterfactual equation | Body if it is the main comparison | Estimation details, standard errors, and sensitivity |

## Writing From A Rough Proof

When the user gives a rough mathematical proof, first identify:

- the formal object the reader must know before the proof;
- the theorem or proposition being proved;
- the one equation, decomposition, or inequality worth showing in the body;
- the lemmas that can be cited in the body and proved in the appendix;
- the algebra, constants, and cases that belong only in the appendix.

Then write two registers:

- **Body register**: selective, explanatory, equation-light, and interpretation-heavy.
- **Appendix register**: complete, sequential, notation-consistent, and proof-heavy.

Do not write the same proof twice. The body explains why the proof works; the appendix proves that it works.

For rough empirical-model notes, use the same split. The body defines the construct, identifies the comparison, and states the estimand; the appendix documents variable construction, balance, alternative specifications, and repeated robustness tables.

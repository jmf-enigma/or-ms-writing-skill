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

## What Main-Text Equations Do

Main-text displays usually perform one of five jobs:

1. **Define the system**: state variables, evolution equations, budget constraints, transition laws, utility/payoff, or feasibility.
2. **Define the decision problem**: objective, feasible policy class, benchmark, optimization problem, or estimand.
3. **Create the analysis object**: relaxation, lower bound, regret decomposition, implicit revenue, uncertainty set, estimator, or stochastic program.
4. **State the headline result**: theorem condition, approximation factor, regret bound, identification expression, threshold, or policy rule.
5. **Support a body proof idea**: one key inequality or decomposition that explains why the theorem is credible.

If a display does none of these jobs, it probably belongs in the appendix or should be prose.

## Body Formula Choreography

A body display should usually have three parts.

1. **Before the display**: say what the display is for. Examples: it defines the state evolution, states the firm problem, gives the lower-bound program, or decomposes regret.
2. **The display**: show only the object needed for later results. Number it if it is referenced later.
3. **After the display**: translate the central variables and explain why the display matters for the next theorem, policy, or proof step.

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

MS model narration usually proceeds in this order, but the exact order can vary by paper type:

1. Explain the operational or economic setting in prose.
2. Define agents, timing, state, information, and actions in the order they occur.
3. Introduce notation only after the corresponding object has been named in words.
4. Display system evolution or budget/utility only when it anchors later results.
5. Display the objective or decision problem after feasibility and information are clear.
6. State the benchmark, solution concept, or optimal value.
7. Interpret why the model is difficult or why the abstraction isolates the mechanism.

For technical algorithm papers, the model may start earlier, but it should still tell the reader what each state and control represents before the theorem.

## Theorem And Result Layout

A theorem in the body should be surrounded by prose.

- Before the theorem: remind the reader of the local setup and conditions.
- Theorem statement: include the exact assumption, policy class, benchmark, and conclusion.
- After the theorem: interpret the result in words before moving to proof or the next theorem.

For approximation and regret results, the post-theorem paragraph should say:

- what the comparator is;
- what parameter makes the problem hard;
- when the factor or rate is useful;
- how the result differs from the standard model.

For structural results, the post-theorem paragraph should say:

- what the policy/equilibrium/threshold looks like;
- which parameter or state determines the regime;
- what decision implication follows.

## Body Proof Sketch Layout

A body proof sketch should be short and load-bearing.

Useful sequence:

1. State what object is decomposed, relaxed, coupled, or bounded.
2. Show one displayed decomposition or inequality if the reader must see it.
3. Name the lemmas or appendix results that control the terms.
4. State how combining those terms yields the theorem.
5. Send full algebra, cases, constants, and auxiliary lemmas to the appendix.

For Management Science, proof-sketch prose should be literal. Use verbs such as define, decompose, construct, relax, bound, compare, combine, and apply. Do not make the proof sound like a story.

Observed proof-idea rhythm in strong MS/OR papers:

1. "We first..." fixes the object or reduction.
2. "The difficulty is..." names the term, constraint, strategic response, or stochastic error.
3. "We control/show/compare..." names the proof move.
4. "Combining..." closes the theorem and points to the appendix.

The body proof idea usually has zero or one display. Use a display only for the decomposition, inequality, or reduced system that the rest of the paper relies on. If a second display merely verifies the first, move it to the appendix.

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

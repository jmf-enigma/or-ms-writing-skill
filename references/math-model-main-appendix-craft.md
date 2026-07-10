# Mathematical Model, Derivation, And Appendix Craft

Use this when the user gives a mathematical proof, derivation, model sketch, theorem, proposition, or result list and asks for main-text writing, appendix writing, or paper organization. The goal is to decide what the reader must see in the body and what belongs in the appendix, then write both parts in native OR/MS style.

For Management Science-specific details about how body displays, theorem statements, proof-sketch equations, and appendix proof formulas are arranged on the page, also use `management-science-model-proof-equation-layout.md`.

## Source Signals

- Management Science asks papers to be succinct and focused, and says online-companion analytical proofs or data analysis should not contain material critical for evaluating the paper. Therefore the body needs the result, the model object, and enough interpretation to evaluate the contribution.
- Operations Research separates regular appendices needed for understanding from electronic companions that are optional supplemental material. In focused technical papers, proofs belong in the published paper rather than only in an EC.
- Recent MS/OR papers commonly put the decision environment, main model primitives, key assumptions, theorem statements, and result interpretation in the body. Long proofs, routine lemmas, repeated algebra, KKT checks, finite-sample demonstrations, and extra robustness usually move to an appendix or EC.
- Full-text close readings confirm that proof placement is contextual. Some technical OR papers carry complete proofs in the main paper; many MS/M&SOM papers state the theorem or proposition, interpret it, give one proof move if trust requires it, and then put complete proof verification in the appendix or online supplement.
- Model-heavy papers often keep one body-level proof idea or derivation checkpoint near an appendix pointer. The body tells the reader why the formal step works; the appendix supplies the formal details, cases, and constants the proof actually uses.
- Applied OM papers often introduce a parsimonious base model in the body and put partner-specific calibration, data estimation, extra operational features, and scenario grids in appendices. The body still states how the real system maps onto the base model.
- Baseline-plus-general-model theory papers often analyze the baseline model in the body and place the general model in an appendix. This works only when the body explains why the baseline carries the main mechanism and what the generalization preserves.
- Mechanism and market-design papers often state theorem regions, then immediately interpret the regions and visualize the comparison. Proofs move to appendices, but the body explains which parameter or uncertainty source favors which mechanism.
- Published MS papers also use more than one formal proof convention. A result may be followed by a complete short `Proof.`, a one-line `Proof.` pointer such as a global appendix notice, or ordinary proof-sketch prose with a cross-reference. The invariant is that the nearby body text interprets the result and the manuscript uses its convention consistently.

## Observed Paper-Appendix Pairing Patterns

Recent MS/OR papers tend to pair the body and appendix through a visible checkpoint:

- A model paper states the decision environment, formulation, and main proposition in the body, then sends only the proof and nonlinear or algebraic verification to the online appendix.
- A theory paper with many lemmas gives the theorem and a short proof mechanism in the body, then uses appendix subsections whose titles match proof dependencies: local reconfiguration, routing node, global bounds, algorithm proof, or example construction.
- A principal-agent or mechanism paper keeps benchmark definitions, equilibrium regions, and the economic comparison in the body. Closed-form expressions, geometric arguments, implicit-function steps, and long proposition proofs move to labeled appendix subsections.
- An empirical or ML paper states the preferred model, primary predictive or causal comparison, and practical interpretation in the body. Appendix sections collect notation, auxiliary baselines, alternative inputs, extra sample slices, and robustness checks; the body still says what those checks conclude.
- An applied optimization paper keeps the queueing, routing, capacity, or service model and the central reformulation in the body. Notation lists, acronym lists, proposition proofs, and computational or implementation details move to online appendices.

The common pattern is conclusion-first at the local result-package level. The body does not say only "see Appendix." It tells the reader what has been proved, estimated, checked, or preserved in nearby prose. A formal one-line proof pointer may precede that interpretation when the manuscript uses that convention.

## Main-Text Model Inventory

By the point the reviewer must rely on dense notation, make the relevant formal, empirical, or decision object recoverable. A canonical formulation may come first when its role is already active. Use only the inventory items the paper needs, and order them by mathematical or temporal dependency.

1. **Formal, empirical, or decision object**: the system, optimization problem, construct, estimator, policy class, or comparison the section establishes.
2. **Timing and information, when consequential**: what is observed before each action or realization and which uncertainty drives later claims.
3. **Actions, states, or feasible set**: the controls, policy class, allocation, threshold, estimator, recommendation, or mechanism being analyzed.
4. **Objective, estimand, and binding constraints**: the metric or target and the constraint that actually drives the result.
5. **Benchmark or solution concept, when used**: the oracle, current practice, relaxation, equilibrium concept, estimator target, or other reference point.
6. **Primitives and notation**: introduce symbols in an order the reader can track and translate consequential notation once.
7. **Assumption role**: explain an assumption when its role in identification, tractability, bounding, mechanism isolation, practice, or regularity matters.

The model is established when the items later claims depend on are available and their roles are intelligible. Absence of an unused inventory item is not a defect.

## How Much Mathematics Belongs In The Body

Keep a mathematical step in the main text when it changes how the reader understands the contribution.

- Keep the displayed formulation if it defines the paper's decision problem, objective, benchmark, or identifying estimand.
- Keep the main theorem, proposition, estimator, policy rule, or algorithm statement if it is used in the abstract, introduction, contribution paragraph, or headline result.
- Keep one derivation checkpoint when a transformation creates the object used in the theorem, such as original problem to relaxation, Bellman equation to threshold structure, primal to dual, regret to decomposed terms, estimator to plug-in form, or equilibrium constraints to reduced form.
- Keep a short proof idea when the proof technique is part of the methodological contribution, the result would otherwise look like a black box, or a skeptical reviewer needs to see why the key assumption matters.
- Keep any interpretation needed to evaluate a theorem in the local body passage. It may precede or follow the statement according to the manuscript's result convention.

Move mathematics out of the body when it only verifies the step the body has already motivated.

- Move repeated algebra, KKT verification, constants, concentration bounds, induction details, martingale calculations, coupling construction details, case splits, and auxiliary lemmas.
- Move long derivations after the body has shown the start point, the key transformed expression, and the reason the transformation matters.
- Move notation tables, implementation minutiae, helper algorithms, parameter grids, and finite-sample demonstrations unless they are the first evidence for the headline claim.

## Lane-Specific Placement Patterns

Different OR/MS papers distribute math differently. Use the paper's lane before deciding placement.

- **Stochastic optimization and inventory**: keep the network, state variables, decisions, costs, disruption or lead-time process, lower bound, heuristic policy, and primary benchmark in the body. Move demand decensoring, lead-time fitting, scenario grids, and long simulation designs.
- **Dynamic programming, POMDP, and optimal control**: keep state, belief, action, reward/cost, transition, information update, and any reformulation that makes the problem tractable. Move contraction, boundary verification, and discretization or computational details unless they are the contribution.
- **Threshold or structural policy papers**: keep the definition of the policy class and the theorem that characterizes the threshold or region. If a stronger result yields the theorem, keep the stronger result's meaning in the body and prove it in the appendix.
- **Baseline-plus-general-model theory**: keep the baseline model, baseline results, and main welfare or policy implications in the body. Put the general model in an appendix only if it preserves the core mechanism rather than replacing it.
- **Mechanism, market design, and principal-agent**: keep the institutional rule, contract or mechanism, benchmark such as first-best or second-best, equilibrium concept, and welfare comparison in the body. Move envelope calculations, implicit-function details, and repetitive equilibrium case checks.
- **Empirical or industry-partner applications**: keep the preferred specification or policy comparison in the body. Move data dictionaries, calibration tables, decensoring steps, extra datasets, and secondary robustness suites unless they protect the main validity claim.

## Derivation Depth Rule

The main text should usually show three levels and stop.

1. **Start point**: the original objective, Bellman equation, estimating equation, regret definition, equilibrium constraint, or optimization problem.
2. **Key move**: relaxation, decomposition, dual, coupling, exchange argument, conditioning step, plug-in construction, or structural monotonicity.
3. **Resulting object**: the theorem condition, policy class, bound, rate, estimator, threshold, or comparison that the rest of the section uses.

The appendix gives the missing algebra between these levels. Do not write five pages of algebra in the body. Do not write zero mathematics in the body when the paper's object is mathematical.

## Main-Text Proof Sketch

A main-text proof sketch should not be a miniature appendix. It should expose the part of the argument that explains why the result is credible.

Before writing a proof paragraph, distinguish three jobs. A complete short proof may appear directly under the theorem or proposition with `Proof.`. A venue-style one-line `Proof.` may only record that proof verification appears in the appendix. A credibility bridge explains the proof move in ordinary prose and points to the appendix. Do not confuse the pointer with the bridge, and do not label an incomplete sketch as a complete proof when the manuscript's convention would imply otherwise.

Depending on the proof, the bridge may name a reduction or constructed object, isolate a difficult term, show the key inequality or comparison, or identify the external result being applied and verify its consequential condition. Include only the pieces needed to connect the statement to the conclusion. Point to the appendix for formal verification when details move there.

Good body-level proof prose says, for example, that the proof takes the dual because the dual prices the scarce capacity, uses a coupling because it holds arrivals fixed across policies, or decomposes regret because only one term depends on learning error.

For Management Science, keep the proof-idea voice especially plain. It is not a place for authorial style. A useful bridge is usually four sentences or fewer and may include:

1. The sketch scope or simplifying assumption, if any.
2. A constructed object, decomposition, relaxation, reduction, or theorem application.
3. The lemma, inequality, comparison, or condition that carries the argument.
4. The connection back to the theorem and the appendix pointer.

Do not force all four sentences. A direct application may need only the cited result and verification of its condition; a simple monotonicity argument may need only the consequential derivative sign.

Use ordinary verbs: construct, decompose, bound, compare, apply, combine, show, imply. Avoid rhetorical verbs such as reveal, illuminate, uncover, or hinge on unless the sentence names the exact mathematical object.

Do not write "the key intuition is" when the next sentence is actually a proof step. In proof ideas, prefer "the key step is to..." or "the argument uses..." because this keeps the prose mathematical rather than motivational.

Close-reading rule: a proof idea is often not labeled. In recent full texts, the body may say that the proof hinges on a sample-path comparison, a closure property, a Bellman-type equation, or a trade-off between queue length and revenue loss, then point to an appendix. That is usually more native than a visible `Proof idea:` label.

For a theorem that gives a rate or bound, include the rate driver in the body. For example, state whether the proof balances waiting cost against rejection loss, translates a one-period improvement into a global optimality gap, or compares a strategic policy against a random benchmark. The appendix can then verify the inequalities.

## Appendix Proof And Derivation Voice

An appendix proof can be denser, but it still needs reader signposts.

- Begin by fixing any objects or assumptions that are not already active and make the theorem target clear.
- Before long algebra, state what the algebra is proving.
- Use lemma names by function, such as upper-bound lemma, threshold lemma, concentration lemma, feasibility lemma, or reduction lemma.
- Keep notation consistent with the body. If a new object is local to the proof, say so.
- End by mapping the proved technical statement back to the theorem, proposition, or displayed result in the body.

The appendix should verify the body, not replace it. If the appendix contains the first explanation of the theorem's meaning, the body is too thin.

Full-text appendix shape is usually more literal than elegant: `Proof of Proposition 1`, `Proof of Theorem 2`, `Auxiliary Lemmas`, `Additional Robustness Checks`. Long proof sections are allowed to use explicit sequencing because the reader is verifying a claim. What feels strange is not density; it is an appendix that introduces a new benchmark, new mechanism, or new interpretation that the body never prepared.

## Reviewer Calibration

Assume the reviewer knows one nearby field deeply and the rest only well enough to be skeptical.

- A theory reviewer should not have to infer the institutional meaning of the state, action, objective, or benchmark.
- An empirical reviewer should not have to infer whether a theorem is a characterization, identification result, estimator, bound, or approximation.
- An OM or MS reviewer should not have to infer whether a model is normative, descriptive, structural, equilibrium, learning, robust, or policy-evaluation.
- A domain expert should not see a familiar word used with a different technical meaning unless the local definition appears first.

When crossing fields, add a concise bridge near the formal object's first consequential use. It should map the unfamiliar construct into the reviewer's vocabulary, not apologize for the mathematics; it may precede or follow a compact definition according to dependency.

## Main Text And Appendix Map

Before writing from a proof or derivation, build this map internally.

| Object | Body role | Appendix role |
|---|---|---|
| Model primitives | the relevant environment, timing, information, action, objective, or benchmark | notation table, secondary variants |
| Assumptions | statement and analytic role | examples, boundary cases, weaker/stronger variants |
| Main theorem | formal statement and interpretation | complete proof |
| Central derivation | start point, key move, resulting object | algebra, constants, cases, lemmas |
| Proof idea | load-bearing mathematical move and why it works | formal inequalities and verification |
| Algorithm or policy | inputs, decision logic, benchmark, guarantee | pseudocode details, implementation, runtime checks |
| Empirical or numerical validation | preferred specification, headline comparison, main figure/table | extra metrics, sensitivity, parameter sweeps |

For a mechanical first pass from rough notes, run `scripts/plan_math_split.py`. Use the script output as a diagnostic map, not as the final prose. After the map, revise with reviewer judgment.

## Proof-Notes-To-Paper Workflow

When the user gives a proof process rather than polished text, do not start drafting immediately.

1. **Inventory** the notes into model object, formal result, central derivation, proof idea, appendix verification, interpretation, and gap notes.
2. **Recover the body spine**: keep the mathematical object, theorem or proposition, any derivation checkpoint on which the result depends, and the interpretation needed for first-pass reading.
3. **Recover the appendix spine**: supply the complete proof with the relevant fixed objects, assumptions, lemma dependencies, cases, constants, and verification details. Do not invent categories the proof does not use.
4. **Check for missing reader objects**: if the notes prove a theorem but never state the benchmark, policy class, information structure, or result type, mark the gap before writing.
5. **Draft in two registers**: body prose should be explanatory and selective; appendix prose should be precise, complete, and signposted.

If the notes contain phrases such as "obvious," "standard," "straightforward," or "omitted," replace them with the actual mathematical move. If the move is not recoverable, report a gap rather than writing around it.

The map is not the output unless the user asks for a map. For a body paragraph, hide the categories and write ordinary prose. For an appendix proof, use proof labels only where they help the reader follow a long argument. For a combined body-and-appendix answer, give a concise body passage first and then the appendix proof or derivation.

## Cross-Reference Language

- "The next display gives the optimization problem used throughout the analysis. Appendix A records the algebraic simplifications used in the proof."
- "The proof has two ingredients. The main text explains the relaxation that creates the benchmark, and Appendix B verifies the resulting inequalities."
- "We state the theorem here because it determines the policy comparison. The complete proof, including the case split, is in Appendix C."
- "This derivation is included in the body because it defines the estimator used in the empirical section. The remaining variance calculations are in Online Appendix EC.2."
- "The robustness check addresses the main validity concern, so the body reports the conclusion and Online Appendix EC.4 gives the full table."
- "The appendix does not introduce a new claim; it verifies the comparison stated above by expanding the two case splits."
- "Online Appendix EC.2 repeats the analysis under the alternative timing assumption. The characterization is unchanged except for the principal's ability to commit before the agent responds."

## Failure Modes To Avoid

- Body as symbol dump: primitives are defined but the decision environment is never explained.
- Body as appendix: every algebraic step appears before the reader knows what result it supports.
- Appendix as hiding place: the main theorem, benchmark, key assumption role, or proof idea appears only after the body sends the reader away.
- Generic proof pointer: "The proof follows from standard arguments" without naming the actual move.
- Uncalibrated model language: "optimal," "robust," "causal," "equilibrium," or "data-driven" without the objective, uncertainty set, design, strategy space, or observed data.

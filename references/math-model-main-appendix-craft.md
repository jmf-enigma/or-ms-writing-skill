# Mathematical Model, Derivation, And Appendix Craft

Use this when the user gives a mathematical proof, derivation, model sketch, theorem, proposition, or result list and asks for main-text writing, appendix writing, or paper organization. The goal is to decide what the reader must see in the body and what belongs in the appendix, then write both parts in native OR/MS style.

For Management Science-specific details about how body displays, theorem statements, proof-sketch equations, and appendix proof formulas are arranged on the page, also use `management-science-model-proof-equation-layout.md`.

## Source Signals

- Management Science asks papers to be succinct and focused, and says online-companion analytical proofs or data analysis should not contain material critical for evaluating the paper. Therefore the body needs the result, the model object, and enough interpretation to evaluate the contribution.
- Operations Research separates regular appendices needed for understanding from electronic companions that are optional supplemental material. In focused technical papers, proofs belong in the published paper rather than only in an EC.
- Recent MS/OR papers commonly put the decision environment, main model primitives, key assumptions, theorem statements, and result interpretation in the body. Long proofs, routine lemmas, repeated algebra, KKT checks, finite-sample demonstrations, and extra robustness usually move to an appendix or EC.
- Model-heavy papers often give one body-level proof idea or derivation checkpoint before pointing to an appendix. The body tells the reader why the formal step works; the appendix verifies every inequality, case, and constant.
- Applied OM papers often introduce a parsimonious base model in the body and put partner-specific calibration, data estimation, extra operational features, and scenario grids in appendices. The body still states how the real system maps onto the base model.
- Baseline-plus-general-model theory papers often analyze the baseline model in the body and place the general model in an appendix. This works only when the body explains why the baseline carries the main mechanism and what the generalization preserves.
- Mechanism and market-design papers often state theorem regions, then immediately interpret the regions and visualize the comparison. Proofs move to appendices, but the body explains which parameter or uncertainty source favors which mechanism.

## Main-Text Model Ladder

Write the model section so a reviewer can reconstruct the decision environment before parsing notation.

1. **Decision environment**: who chooses what, for whom, and why the decision is hard.
2. **Timing and information**: what is observed before each action, what remains uncertain, and whether decisions are static, dynamic, sequential, simultaneous, or adaptive.
3. **Actions and feasible set**: the control, policy class, allocation, price, threshold, estimator, recommendation, or mechanism being optimized or analyzed.
4. **Objective and constraint**: profit, welfare, cost, regret, service level, feasibility, identification target, or risk measure. State the constraint that actually drives the result.
5. **Benchmark or solution concept**: oracle, myopic policy, current practice, first-best, LP/fluid relaxation, clairvoyant benchmark, equilibrium, estimator target, or status quo.
6. **Primitives and notation**: introduce symbols in the same order as the decision environment. Translate every important symbol once.
7. **Assumption role**: say whether an assumption identifies, bounds, simplifies, preserves tractability, isolates a mechanism, matches practice, or rules out degeneracy.

If the body cannot answer these seven points, the model is not established. If it answers them through a notation dump without operational translation, it is not readable.

## How Much Mathematics Belongs In The Body

Keep a mathematical step in the main text when it changes how the reader understands the contribution.

- Keep the displayed formulation if it defines the paper's decision problem, objective, benchmark, or identifying estimand.
- Keep the main theorem, proposition, estimator, policy rule, or algorithm statement if it is used in the abstract, introduction, contribution paragraph, or headline result.
- Keep one derivation checkpoint when a transformation creates the object used in the theorem, such as original problem to relaxation, Bellman equation to threshold structure, primal to dual, regret to decomposed terms, estimator to plug-in form, or equilibrium constraints to reduced form.
- Keep a short proof idea when the proof technique is part of the methodological contribution, the result would otherwise look like a black box, or a skeptical reviewer needs to see why the key assumption matters.
- Keep the interpretation after a theorem. A theorem without a body-level interpretation forces the appendix to carry the paper's meaning.

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

A main-text proof sketch should not be a miniature appendix. It should contain the proof's job.

- Name the object constructed or reduced to.
- Name the hard term, constraint, or error source.
- State why the mathematical move controls it.
- Explain how this yields the theorem's policy, bound, characterization, or estimator.
- Point to the appendix for formal verification.

Good body-level proof prose says, for example, that the proof takes the dual because the dual prices the scarce capacity, uses a coupling because it holds arrivals fixed across policies, or decomposes regret because only one term depends on learning error.

For Management Science, keep the proof-idea voice especially plain. It is not a place for authorial style. A good MS proof idea usually has four sentences or fewer:

1. The sketch scope or simplifying assumption, if any.
2. The constructed object, decomposition, relaxation, or reduction.
3. The lemma, inequality, or comparison that controls the hard term.
4. The connection back to the theorem and the appendix pointer.

Use ordinary verbs: construct, decompose, bound, compare, apply, combine, show, imply. Avoid rhetorical verbs such as reveal, illuminate, uncover, or hinge on unless the sentence names the exact mathematical object.

Do not write "the key intuition is" when the next sentence is actually a proof step. In proof ideas, prefer "the key step is to..." or "the argument uses..." because this keeps the prose mathematical rather than motivational.

## Appendix Proof And Derivation Voice

An appendix proof can be denser, but it still needs reader signposts.

- Start each proof by restating the fixed objects, assumptions, and theorem target.
- Before long algebra, state what the algebra is proving.
- Use lemma names by function, such as upper-bound lemma, threshold lemma, concentration lemma, feasibility lemma, or reduction lemma.
- Keep notation consistent with the body. If a new object is local to the proof, say so.
- End by mapping the proved technical statement back to the theorem, proposition, or displayed result in the body.

The appendix should verify the body, not replace it. If the appendix contains the first explanation of the theorem's meaning, the body is too thin.

## Reviewer Calibration

Assume the reviewer knows one nearby field deeply and the rest only well enough to be skeptical.

- A theory reviewer should not have to infer the institutional meaning of the state, action, objective, or benchmark.
- An empirical reviewer should not have to infer whether a theorem is a characterization, identification result, estimator, bound, or approximation.
- An OM or MS reviewer should not have to infer whether a model is normative, descriptive, structural, equilibrium, learning, robust, or policy-evaluation.
- A domain expert should not see a familiar word used with a different technical meaning unless the local definition appears first.

When crossing fields, add one bridge sentence before the formal object. It should map the unfamiliar construct into the reviewer's vocabulary, not apologize for the mathematics.

## Main Text And Appendix Map

Before writing from a proof or derivation, build this map internally.

| Object | Body role | Appendix role |
|---|---|---|
| Model primitives | decision environment, timing, information, action, objective, benchmark | notation table, secondary variants |
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
2. **Recover the body spine**: the body needs the mathematical object, theorem or proposition, one derivation checkpoint if the result depends on a transformation, and an interpretation paragraph.
3. **Recover the appendix spine**: the appendix needs complete proof order, fixed objects and assumptions, lemma functions, case splits, constants, and verification details.
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

## Failure Modes To Avoid

- Body as symbol dump: primitives are defined but the decision environment is never explained.
- Body as appendix: every algebraic step appears before the reader knows what result it supports.
- Appendix as hiding place: the main theorem, benchmark, key assumption role, or proof idea appears only after the body sends the reader away.
- Generic proof pointer: "The proof follows from standard arguments" without naming the actual move.
- Uncalibrated model language: "optimal," "robust," "causal," "equilibrium," or "data-driven" without the objective, uncertainty set, design, strategy space, or observed data.

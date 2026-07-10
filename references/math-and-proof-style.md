# Mathematical And Proof Style

Use this for theorem statements, result sections, proof sketches, and appendix proofs.

## Model Setup And Theorem Prerequisites

- Make the formal or decision environment recoverable by the point a claim relies on it. Relevant objects may include agents or system, timing, information, action or state, uncertainty, objective, constraints, comparator, and solution concept; not every model needs all of them.
- Introduce primitives in temporal or mathematical dependency order. A technical subsection may define a symbol first and explain its operational meaning immediately afterward when that is the cleanest definition.
- Put the main formulation in the body when later results depend on the objective, feasible set, benchmark, or information structure.
- State assumptions with their analytic role. A useful assumption identifies, bounds, simplifies, preserves tractability, isolates a mechanism, or matches a standard setting.
- Explain the central variables and the formulation's analytical role near the display. A managerial or operational friction is needed only when the model actually isolates one.

## Result Statement

- Make conditions available by the point the conclusion is interpreted. Standing assumptions may precede the statement, appear in it, or be recalled immediately afterward when scope could be missed.
- Prefer bare result labels or short object-like descriptors when allowed: `Proposition 1`, `Theorem 2 (Regret Bound)`, or `Lemma 3 (Monotonicity)`. Put the full claim in the statement and surrounding prose.
- Keep theorem statements complete: primitives, parameter ranges, equilibrium/optimality concept, conclusion, uniqueness or boundary cases if needed.
- Keep needed interpretation in the local result package. It may precede a complete short proof, follow it, or surround a one-line appendix pointer according to the manuscript's convention; a self-interpreting result may need only one sentence.

## Main Text vs Appendix

- Main text: statement, mechanism, economic/operational interpretation, comparison to benchmark.
- Appendix: algebra, induction, KKT verification, coupling, concentration inequalities, case splits, technical lemmas.
- Main text derivation: show the start point, the key transformation, and the resulting formal object if that object is used by the theorem, estimator, algorithm, or benchmark.
- Appendix derivation: fill in omitted algebra, constants, boundary cases, auxiliary lemmas, and verification after the body has shown why the transformation matters.
- If the proof is long and reader trust requires it, include the one load-bearing proof move in the main text and send verification details to the appendix. Do not add a roadmap to every result.
- Keep proof details in the body when the proof technique is the contribution, the paper is a focused technical paper, or the result is short enough that the proof clarifies rather than distracts.
- A formal result may use a complete short body proof, a venue-style one-line `Proof.` pointer, or ordinary proof-sketch prose with an appendix reference. Whatever the convention, keep the decision meaning and any necessary credibility bridge in nearby body prose.
- Put auxiliary lemmas in the appendix unless the lemma is the conceptual object that readers need to understand the main theorem.

## Body-Level Derivation Checkpoints

Use the first three checkpoints when a transformation creates an object used later. Add translation or an appendix pointer only when the local reader job requires it.

1. **Original object**: define the optimization problem, Bellman equation, estimator, regret, equilibrium constraint, or benchmark.
2. **Load-bearing move**: name the relaxation, dual, decomposition, coupling, conditioning step, exchange argument, or monotonicity step.
3. **Resulting object**: state the bound, threshold, policy class, identifying expression, or simplified program that the theorem uses.
4. **Reader translation, when needed**: say what this object means for the formal problem, decision, or comparison.
5. **Appendix pointer, when details move**: send mechanical verification to the appendix after the body makes the logic recoverable.

## Management Science Proof-Idea Voice

MS proof ideas are concise, literal, and low-style. They explain why the theorem should be trusted without trying to sound elegant.

- Write in proof verbs: construct, decompose, bound, compare, apply, combine, show, imply.
- Make any extra simplifying assumption available before the sketch relies on it and give the complete-proof location when details move.
- Prefer "the key step is to bound..." over "the key intuition is..." when the sentence describes a proof move.
- Use a displayed inequality or decomposition only when it is an object the reader must understand. More than one may be appropriate when the proof technique itself requires a visible chain; routine verification still moves to the appendix.
- Do not call the proof elegant, subtle, delicate, or surprising. Let the theorem interpretation carry surprise if needed.
- Do not write a generic proof roadmap if the theorem only needs a one-sentence proof idea.

## Full-Proof Paragraph Moves

Select and order only the moves the proof uses.

1. **Setup**: fix parameters or define local objects not already active.
2. **Reduction**: show why it suffices to prove a simpler claim when the proof uses one.
3. **Key inequality, lemma, or theorem application**: isolate the load-bearing step.
4. **Cases**: split only on mathematically consequential thresholds or regimes.
5. **Conclusion**: map the proved statement back to the theorem when the connection is not immediate.

## OR/MS Proof Moves

- Optimization: feasibility, upper bound, candidate solution, KKT/duality, tightness.
- Dynamic programs: Bellman equation, monotonicity, contraction or induction, threshold structure, comparative statics.
- Mechanism design: IC/IR reduction, envelope/monotonicity, virtual surplus, allocation/payment construction.
- Revenue management/pricing: demand primitives, elasticity or hazard-rate conditions, threshold/markup characterization, welfare comparison.
- Learning/bandits: confidence event, regret decomposition, concentration, summation/tuning, lower bound or benchmark.

## Polishing Rules

- Do not bury a missing proof step behind "it is easy to see."
- Keep connected equations together and explain their role and consequential notation in nearby prose. That prose may come before, after, or on both sides of a display; do not require symmetrical framing.
- Use notation consistently; never reuse a symbol for a new object in the same proof.
- Name lemmas by function: "single-crossing lemma," "upper-bound lemma," "threshold lemma."
- If a key step is not proved, output `Gap Notes` and use an available proof-discovery workflow before polishing exposition.
- Do not let the appendix provide the first explanation of the theorem's meaning. The body needs the formal statement and whatever interpretation or proof checkpoint is required for first-pass understanding and trust.
- Avoid proof prose that sounds generated. Do not use colon-led roadmaps, dash pivots, semicolon chains, "we proceed as follows," or numbered steps when a linear proof reads better.
- For long proofs, paragraph labels are fine. For short proofs, use ordinary transitions such as "We first show," "It remains to verify," and "Combining these inequalities gives."

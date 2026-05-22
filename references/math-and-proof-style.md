# Mathematical And Proof Style

Use this for theorem statements, result sections, proof sketches, and appendix proofs.

## Model Setup Before Theorem

- Establish the decision environment before formal claims: agents, timing, information, action, uncertainty, objective, constraints, benchmark, and solution concept.
- Introduce primitives in the order the decision maker sees them. Do not define a symbol before the reader knows what operational object it represents.
- Put the main formulation in the body when later results depend on the objective, feasible set, benchmark, or information structure.
- State assumptions with their analytic role. A useful assumption identifies, bounds, simplifies, preserves tractability, isolates a mechanism, or matches a standard setting.
- After a formulation display, explain what the central variables mean and why the formulation captures the managerial or operational friction.

## Result Statement

- State conditions before conclusions.
- Use meaningful proposition titles when allowed: "Threshold Structure of the Optimal Policy" is better than "Main Result."
- Keep theorem statements complete: primitives, parameter ranges, equilibrium/optimality concept, conclusion, uniqueness or boundary cases if needed.
- After the statement, add one interpretation paragraph before moving to proof or next result.

## Main Text vs Appendix

- Main text: statement, mechanism, economic/operational interpretation, comparison to benchmark.
- Appendix: algebra, induction, KKT verification, coupling, concentration inequalities, case splits, technical lemmas.
- Main text derivation: show the start point, the key transformation, and the resulting formal object if that object is used by the theorem, estimator, algorithm, or benchmark.
- Appendix derivation: fill in omitted algebra, constants, boundary cases, auxiliary lemmas, and verification after the body has shown why the transformation matters.
- If the proof is long, include a proof roadmap in the main text and send details to the appendix.
- Keep proof details in the body when the proof technique is the contribution, the paper is a focused technical paper, or the result is short enough that the proof clarifies rather than distracts.
- Move complete proofs to the appendix only after the body has stated the formal result, named the proof idea, and explained the decision meaning.
- Put auxiliary lemmas in the appendix unless the lemma is the conceptual object that readers need to understand the main theorem.

## Body-Level Derivation Pattern

Use this pattern when the user gives a mathematical derivation and asks for main text.

1. **Original object**: define the optimization problem, Bellman equation, estimator, regret, equilibrium constraint, or benchmark.
2. **Load-bearing move**: name the relaxation, dual, decomposition, coupling, conditioning step, exchange argument, or monotonicity step.
3. **Resulting object**: state the bound, threshold, policy class, identifying expression, or simplified program that the theorem uses.
4. **Reader translation**: say what this object means for the decision or comparison.
5. **Appendix pointer**: send mechanical details to the appendix only after the body gives the logic.

## Management Science Proof-Idea Voice

MS proof ideas are concise, literal, and low-style. They explain why the theorem should be trusted without trying to sound elegant.

- Write in proof verbs: construct, decompose, bound, compare, apply, combine, show, imply.
- State any simplifying assumption before the sketch and give the complete-proof location.
- Prefer "the key step is to bound..." over "the key intuition is..." when the sentence describes a proof move.
- Use one displayed inequality or decomposition only when it is the object the reader must understand. Otherwise, summarize the move in prose and point to the appendix.
- Do not call the proof elegant, subtle, delicate, or surprising. Let the theorem interpretation carry surprise if needed.
- Do not write a generic proof roadmap if the theorem only needs a one-sentence proof idea.

## Proof Paragraph Pattern

1. **Setup**: fix parameters and define objects.
2. **Reduction**: show why it suffices to prove a simpler claim.
3. **Key inequality/lemma**: isolate the load-bearing step.
4. **Cases**: split only on economically meaningful thresholds or mathematical regimes.
5. **Conclusion**: explicitly map the proved statement back to the theorem.

## OR/MS Proof Moves

- Optimization: feasibility, upper bound, candidate solution, KKT/duality, tightness.
- Dynamic programs: Bellman equation, monotonicity, contraction or induction, threshold structure, comparative statics.
- Mechanism design: IC/IR reduction, envelope/monotonicity, virtual surplus, allocation/payment construction.
- Revenue management/pricing: demand primitives, elasticity or hazard-rate conditions, threshold/markup characterization, welfare comparison.
- Learning/bandits: confidence event, regret decomposition, concentration, summation/tuning, lower bound or benchmark.

## Polishing Rules

- Do not bury a missing proof step behind "it is easy to see."
- Prefer connected equations with a sentence before and after each display.
- Use notation consistently; never reuse a symbol for a new object in the same proof.
- Name lemmas by function: "single-crossing lemma," "upper-bound lemma," "threshold lemma."
- If a key step is not proved, output `Gap Notes` and route to `theory-proof-workbench`.
- Do not let the appendix provide the first explanation of the theorem's meaning. The body needs a formal statement, a proof idea when needed, and an interpretation paragraph.
- Avoid proof prose that sounds generated. Do not use colon-led roadmaps, dash pivots, semicolon chains, "we proceed as follows," or numbered steps when a linear proof reads better.
- For long proofs, paragraph labels are fine. For short proofs, use ordinary transitions such as "We first show," "It remains to verify," and "Combining these inequalities gives."

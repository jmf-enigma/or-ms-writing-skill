# Paper-Appendix Paired Patterns

Use this when the task involves a theorem, proof process, model derivation, robustness suite, calibration, appendix, online appendix, e-companion, or a body-versus-appendix split. These notes distill how recent OR/MS and adjacent INFORMS papers pair the main text with appendices. They are not templates; use them to decide what the reader must know before being sent out of the body.

## Paired Reading Signals

- INFORMS body text and appendices are paired by reader job. The body states the formal object, result, implication, and proof checkpoint; the appendix verifies details.
- Management Science guidance allows online appendices outside the page limit, but analytical proofs or data analysis in the companion should not be critical for evaluating the paper. Therefore the body must carry the evaluative spine.
- Operations Research treats e-companions as final-file supplements and asks main sections to remain readable and logically presented. Technical papers should not move the core proof idea or contribution-defining argument to an electronic companion.
- Recent M&SOM structured abstracts often preview the paper's appendix logic: problem definition, methodology/results, and managerial implications. The body then keeps the decision environment and headline results, while online appendices hold proofs, closed-form derivations, robustness, and calibration.
- Recent open INFORMS papers often use appendices with titles such as proofs, closed-form expressions, notation, robustness, or model extensions. The title tells the reviewer the appendix's job before the technical details begin.

## Core Pairing Rule

The body should answer: What is the object? What is the result? Why should the reviewer believe the result at first pass? What does it mean under the paper's benchmark or decision environment?

The appendix should answer: Is every algebraic, proof, calibration, implementation, and robustness detail sufficient to verify the body claim?

If the appendix contains the first explanation of the theorem, estimator, model, or managerial implication, the body is underwritten. If the body contains long verification after the reader already understands the result, the body is overstuffed.

## Main-Text Handoff Patterns

Use one of these patterns implicitly before an appendix pointer.

| Body job | Body content before pointer | Appendix job |
|---|---|---|
| Theorem | statement, condition, benchmark, interpretation | complete proof, lemmas, cases |
| Proof idea | constructed object, hard term, proof move | inequalities, constants, induction, concentration |
| Derivation | start object, transformation, resulting object | algebraic verification and boundary cases |
| Model formulation | agents, timing, information, actions, objective | notation table, equivalent forms, variants |
| Algorithm | decision logic, inputs, guarantee, benchmark | pseudocode, runtime, implementation checks |
| Robustness | concern addressed and conclusion | full table, alternate specs, extra slices |
| Calibration | mapping from data to model primitive | estimation details, parameter grids, sensitivity |
| Extension | what changes and whether mechanism survives | full extended model and proof |

Bad handoff: "The proof is in Appendix A." immediately after a theorem with no interpretation.

Better handoff logic: state why the theorem matters, name the proof move if needed, then point to the appendix for formal verification.

## Proof-Idea Register

In MS/OR writing, a body proof idea is usually plain and technical, not dramatic.

- Start from the theorem target or a simplification.
- Name the constructed object, relaxation, coupling, decomposition, or comparison.
- Name the difficult term, constraint, strategic response, stochastic error, or boundary case.
- State the exact move that controls it: duality, exchange argument, monotonicity, convexity, submodularity, induction, KKT conditions, concentration, envelope argument, or contradiction.
- End by saying how this gives the theorem and where the complete verification appears.

Avoid "the key intuition is" when the sentence is proving a bound or verifying a case. Use "the key step is to..." or "the argument..." for proof logic, and reserve intuition for economic or operational interpretation.

## Appendix Section Jobs

A strong appendix section is not a storage bin. Give each section one job.

- **Proof dependency**: proves the theorem, proposition, lemma, or corollary in the order needed by the body.
- **Notation and primitives**: records notation, acronyms, data-to-model mappings, and secondary definitions.
- **Algebraic derivation**: verifies a transformation already motivated in the body.
- **Reviewer threat**: addresses the obvious concern: identification, feasibility, endogeneity, misspecification, omitted mechanism, benchmark choice, or implementation realism.
- **Robustness suite**: reports repeated checks whose conclusions are summarized in the body.
- **Calibration and data construction**: documents sample restrictions, estimation, fitted primitives, scenario grids, and sensitivity.
- **Extension and scope**: shows the mechanism survives a variant without changing the main contribution.

Open appendix sections with the purpose, then the fixed object or design, then the details. For example, "This section proves Proposition 2 by reducing the equilibrium conditions to two threshold inequalities" is better than starting with algebra.

## Formula And Display Pairing

Body displays should do one of five jobs: define the system, define the decision problem, create the analysis object, state the headline result, or show one load-bearing proof step.

Appendix displays should verify: equality chains, repeated cases, KKT systems, concentration events, induction steps, auxiliary lemma proofs, calibration formulas, and implementation details.

When splitting formulas:

1. Body shows the original object.
2. Body shows only the transformation that will be reused.
3. Body names the resulting theorem, estimator, policy, or benchmark.
4. Appendix fills in omitted algebra and boundary cases.

Do not move the only displayed optimization problem, Bellman equation, equilibrium condition, identifying equation, or theorem condition to the appendix if later results depend on it.

## Empirical And ML Appendix Pairing

For empirical, ML, or industry-data papers:

- Body: preferred design, model architecture or estimator at the level needed to understand the result, primary comparison, main metric, and decision implication.
- Appendix: notation table, architecture or training details, auxiliary baselines, alternate outcomes, extra datasets, hyperparameters, sample construction, and lower-priority robustness.
- The body should summarize what an appendix baseline shows. Do not make the reader open the appendix to learn whether a robustness check passed, failed, or changed the interpretation.
- If appendix material defines a term that appears in the main result, pull the definition into the body or add a parenthetical local definition.

## Reviewer Calibration

The appendix split should anticipate a reviewer who is expert in one part of the paper and only adjacent to the others.

- A theory reviewer needs the institutional object before the proof machinery.
- An empirical reviewer needs to know whether a theorem is a characterization, guarantee, approximation, identification result, or estimator property.
- A model reviewer needs to know what is observed, optimized, assumed, and counterfactual before seeing robustness tables.
- A domain reviewer needs the body to use words such as demand, arrivals, conversion, welfare, surplus, engagement, survival chance, revenue, and profit in their narrow local senses.

When in doubt, keep a bridge sentence in the body and move the technical verification to the appendix.

## Common Failure Repairs

- **Body says too little**: add the formal object, theorem meaning, benchmark, and proof checkpoint before the appendix pointer.
- **Body says too much**: keep the result and one proof move; move constants, cases, and repeated displays.
- **Appendix starts cold**: add a first sentence stating the section's purpose and the fixed objects.
- **Proof idea sounds stylized**: replace motivational phrasing with constructed object, hard term, and proof move.
- **Robustness pointer is empty**: state the appendix check's conclusion in the body.
- **Appendix organization feels random**: regroup by proof dependency, reviewer threat, calibration, robustness, and extension.

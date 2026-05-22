# Paper-Appendix Paired Patterns

Use this when the task involves a theorem, proof process, model derivation, robustness suite, calibration, appendix, online appendix, e-companion, or body-versus-appendix split. The goal is not to impose a fixed structure; it is to make the body and appendix read as two parts of one argument.

## Paired Reading Logic

Good OR/MS papers do not treat appendices as overflow. The body gives the reader enough to evaluate the contribution at first pass. The appendix gives the reader enough to verify, reproduce, or stress-test that contribution.

Use this split:

- **Body**: formal object, result, benchmark, interpretation, and any proof or derivation checkpoint needed for trust.
- **Appendix**: complete proof, auxiliary lemmas, algebra, constants, repeated cases, notation tables, calibration, implementation details, robustness suites, and scope extensions.
- **Online supplement/e-companion**: secondary robustness, replication details, extra data cuts, extended variants, and material that supports but does not carry the main evaluation of the paper.

Management Science-style papers often rely on online appendices, but the body still needs the evaluative spine. Operations Research-style technical papers often keep essential proof material in a regular appendix rather than hiding it only in an e-companion.

## Body Handoff

An appendix pointer should usually be conclusion-first. Before sending the reader away, the body states what has been shown, why it matters, or what the appendix check preserves.

Natural handoffs vary by job:

- For a theorem, state the result type, condition, benchmark, and interpretation before the proof pointer.
- For a proof idea, name the constructed object, difficult term, and mathematical move before sending the formal details out.
- For a derivation, show the start object, key transformation, and resulting object used later.
- For robustness, state the threat and the conclusion, then put the full table or variant in the appendix.
- For calibration, map the data to the model primitive in the body; put fitting, grids, and sensitivity outside.
- For extensions, say whether the mechanism survives, strengthens, weakens, or changes before giving the full extended model.

The handoff should not become a visible template. Write it as ordinary prose near the theorem, figure, table, or model step.

## Proof-Idea Register

A body proof idea is not a miniature appendix and not a dramatic story. It is a credibility bridge.

Use one to four plain sentences unless the proof technique is itself the contribution:

1. Fix the object, reduction, or simplifying comparison.
2. Name the hard term, constraint, strategic response, stochastic error, or boundary case.
3. Name the proof move: relaxation, coupling, exchange argument, monotonicity, convexity, submodularity, induction, KKT conditions, concentration, envelope argument, or contradiction.
4. State how the move yields the theorem and where the complete verification appears.

If the theorem is intuitive and the proof is routine, one sentence may be enough. If the theorem looks surprising, include the proof checkpoint that prevents the result from feeling like a black box.

## Appendix Section Jobs

Each appendix section should have one reviewer-facing job. Do not group material only because it was cut from the body.

- **Proof dependency**: prove theorem, proposition, lemma, or corollary in the order needed by the body.
- **Notation and primitives**: record notation, acronyms, data-to-model mappings, and secondary definitions.
- **Algebraic derivation**: verify a transformation already motivated in the body.
- **Reviewer threat**: address identification, feasibility, endogeneity, misspecification, omitted mechanism, benchmark choice, or implementation realism.
- **Robustness suite**: report repeated checks whose conclusions are summarized in the body.
- **Calibration and data construction**: document sample restrictions, estimation, fitted primitives, scenario grids, and sensitivity.
- **Extension and scope**: show what survives under a variant without replacing the main mechanism.

Open an appendix section by stating its purpose and fixed objects. Then proceed to the proof, table, derivation, or implementation detail. A symbol-heavy appendix that starts cold often needs one orienting sentence.

## Formula Pairing

Body displays should define the system, define the decision problem, create the analysis object, state the headline result, or show one load-bearing proof step. Appendix displays should verify equality chains, repeated cases, KKT systems, concentration events, induction steps, auxiliary lemma proofs, calibration formulas, and implementation details.

When splitting a mathematical process:

1. Body shows the original object.
2. Body shows the transformation that later results use.
3. Body names the theorem, estimator, policy, or benchmark created by the transformation.
4. Appendix fills in omitted algebra and boundary cases.

Do not move the only displayed optimization problem, Bellman equation, equilibrium condition, identifying equation, or theorem condition to the appendix if later results depend on it.

## Empirical And ML Pairing

For empirical, ML, or industry-data papers, the body should include the preferred design, the model or estimator at the level needed to understand the result, the primary comparison, the main metric, and the decision implication. The appendix can carry notation, architecture or training details, auxiliary baselines, alternate outcomes, extra datasets, hyperparameters, sample construction, and lower-priority robustness.

The body should say what an appendix baseline or robustness check finds. Do not make the reader open the appendix to learn whether a check passed, failed, or changed the interpretation.

## Quick Repairs

- If the body only says "see Appendix," add the theorem meaning, benchmark, and proof checkpoint.
- If the body contains long verification, keep the result and one proof move; move constants, cases, and repeated displays.
- If the proof idea sounds stylized, replace motivational phrasing with constructed object, hard term, and proof move.
- If the appendix organization feels random, regroup by proof dependency, reviewer threat, calibration, robustness, and extension.
- If appendix material defines a term used in the main result, pull the definition into the body or add a local definition.

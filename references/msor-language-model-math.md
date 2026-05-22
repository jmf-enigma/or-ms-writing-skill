# MS/OR Language, Sentence, And Model-Math Notes

Use this when the user asks for more idiomatic MS/OR language, precise technical wording, model description, theorem interpretation, or proof exposition. The goal is not to imitate any author. The goal is to internalize field-level habits from full-text papers.

## Full-Text Signals Used

These notes extend the earlier full-text paper craft file with additional model-heavy and math-heavy readings, including assortment optimization with replacement options, causal transport DRO with side information, revenue-management pricing, demand estimation from managerial recommendation responses, dynamic pricing with nonstationarity, CMDP primal-dual algorithms, stochastic search with sequential inspections, and robust ranking.

## Word Choice Discipline

MS/OR papers use ordinary words with exact objects. The following pairings are safer than generic technical praise:

- `study` or `consider`: a canonical problem, setting, or decision environment.
- `formulate`: an optimization problem, decision rule, uncertainty set, objective, or model.
- `derive`: an expression, dual reformulation, closed-form condition, bound, or approximation.
- `establish`: a guarantee, convergence rate, regret bound, approximation ratio, monotonicity result, or characterization.
- `identify`: a condition, structural property, source of variation, policy class, mechanism, or tractable case.
- `show`: a formal result, empirical pattern, or comparison, when the evidence is already clear.
- `demonstrate` or `validate`: numerical, empirical, out-of-sample, or case-study evidence.
- `preserve`: information structure, feasibility, monotonicity, convexity, or incentive compatibility.
- `capture`: a modeling feature, demand response, substitution behavior, uncertainty, or information structure.
- `rule out`: degenerate policies, infeasible decisions, unsupported distributions, or alternative explanations.
- `reduce`: computational complexity, regret, conservatism, dimensionality, or an optimization problem.

Do not write "we develop a framework" unless the sentence says what decision the framework formulates and what existing formulation fails to capture. Do not write "we leverage data" unless the sentence says what the data reveal, what remains latent, and how the method uses that variation.

## Formal Adjectives Need Anchors

These words are useful only when anchored:

- `optimal`: state objective, feasible set, information structure, and benchmark.
- `robust`: state uncertainty set, perturbation, misspecification, or sensitivity comparison.
- `tractable`: state the reformulation, convex program, polynomial-time algorithm, decomposition, or approximation.
- `adaptive`: state what changes with observations, state, time, preferred option, or posterior information.
- `nonparametric`: state the decision-rule class or distributional object.
- `finite-sample`: state sample size object and probability/confidence statement.
- `near-optimal`: state regret, lower bound, oracle, or approximation benchmark.
- `minimax`: state risk, localization error, lower bound, or adversarial class.
- `data-driven`: state historical transactions, censored demand, contextual data, recommendation logs, or out-of-sample validation.

If the anchor is missing, replace the adjective with the actual object.

## Sentence-Level Patterns

Adapt these patterns, but do not paste them mechanically.

- Canonical problem to new feature: `We study [canonical problem] when [information, constraint, behavior, or data feature] changes the decision environment.`
- Practice to model: `[Actor] chooses [decision] before observing [uncertainty]. We model this as [formal object], where [key primitive] captures [operational feature].`
- Gap to object: `The difficulty is that [standard formulation] treats [object] as [simplifying feature], whereas in our setting [missing feature] affects [decision or benchmark].`
- Assumption role: `This assumption rules out [pathology] while preserving [standard case or operational feature].`
- Result interpretation: `Relative to [benchmark], the result shows that [policy or estimator] loses at most [bound] when [condition], so [decision consequence].`
- Proof crux: `The proof constructs [auxiliary object] and compares it with [relaxation, benchmark, or optimal policy]. The comparison isolates [single hard term].`

The best MS/OR sentences often put the formal novelty after the practical object. They do not start every paragraph with the method.

## Natural Rhythm And Local Rewrites

Field-style MS/OR prose is compact, but it is not maximally compressed. A polished passage should feel like a reader is being led through the decision, not like every diagnostic item has been inserted.

- Use one sentence for setup and one for force. Example structure: `[Actor] faces [decision/friction]. [Method/result] shows [conditioned consequence].`
- Keep the old object near the front of the sentence and place the new contribution, condition, or contrast near the end.
- Do not add a benchmark to every sentence. Add it where a result, guarantee, comparison, or contribution would otherwise be ambiguous.
- Do not add managerial implications to every paragraph. Some paragraphs only need to define the model, state a result, or explain a proof move.
- Avoid long prepositional chains such as "in the context of the optimization of the management of..." Replace them with an actor and a verb.
- If a sentence has more than one of these jobs, split it: motivating a setting, defining a variable, stating an assumption, announcing a theorem, interpreting a result.
- In revision, first fix the logical object, then the verb, then the rhythm. Do not polish a sentence whose object is still wrong.

## Chinese-To-English Drift Fixes

When text has been drafted from Chinese logic, rewrite the sentence rather than translating phrase by phrase.

- Replace "under the background of" with the actual setting or decision. Start with "In retail pricing..." only when the setting itself matters.
- Replace "with the development of" with the operational change. Say whether data became richer, platforms changed matching, or algorithms changed recommendation timing.
- Replace "according to the model" with a result subject. Use "The model predicts," "Proposition 2 shows," or "The estimate implies" depending on evidence.
- Replace "it can be seen/found that" with a concrete subject and verb. Usually the subject is a theorem, estimate, simulation, model, table, or comparison.
- Replace "has certain" and "to a certain extent" with the magnitude, condition, or caveat. If the magnitude is unknown, write a restrained qualitative claim.
- Replace "combined with" by naming the relationship. The method may use data, condition on covariates, impose a constraint, or compare a benchmark.
- Avoid "this paper starts from" and "make a research on." Native academic prose usually says "We study," "We examine," "We model," or simply names the decision.
- When a Chinese sentence starts from background and slowly reaches the claim, invert it for English. Put the main decision or result earlier, then add the condition.

## Model Narration

A model paragraph should read like a decision environment before it reads like a symbol list.

1. Name the decision maker.
2. Name the timing.
3. Name what is observed before the action.
4. Name the action or policy.
5. Name the uncertainty that remains.
6. Name the payoff, cost, revenue, welfare, regret, or feasibility criterion.
7. Name the benchmark or solution concept.
8. Introduce notation in the same order.

For example, a contextual optimization model should first say that the decision maker observes covariates before choosing an action and then faces random problem parameters. Only after that should it define the decision rule, distribution, loss function, and uncertainty set.

For assortment, pricing, queueing, search, and inventory models, translate each primitive into an operational object. A utility parameter, stockout probability, opening cost, Lagrangian multiplier, change point, regret benchmark, and replacement option each need one plain-language interpretation.

## Displays And Equations

Do not drop an equation into prose without a job.

- The sentence before a display should say whether the display defines an objective, gives a benchmark, states a relaxation, describes a policy, or decomposes a proof term.
- The sentence after a display should identify the central variables and explain the modeling choice.
- If a display uses a conditional expectation, say what information is conditioned on and why that is the decision maker's information.
- If a display is a max-min or minimax problem, say what the outer decision maker chooses and what the inner adversary or worst-case distribution changes.
- If a display is a relaxation, say what constraint or dynamic feature it drops and why it provides an upper or lower bound.

## Main-Text Derivation Depth

MS/OR body prose should reveal the mathematical object without making the reader work through the whole proof.

- For a model formulation, keep the objective, core constraints, information structure, and benchmark in the body. Move notation tables and secondary variants.
- For a Bellman equation, include the state, action, transition, objective, and the structural property the equation will support. Move contraction, induction, or boundary verification if routine.
- For a relaxation or dual, say what is relaxed or priced and why the resulting value is an upper or lower bound. Move KKT checks and complementary slackness details unless they are the central characterization.
- For a regret proof, show the regret definition, the decomposition, and which term carries the learning error. Move concentration constants and summation details.
- For an estimator or identification derivation, show the identifying expression and the variation or assumption that makes it valid. Move variance calculations, nuisance-estimator details, and repeated robustness tables.
- For an equilibrium or mechanism result, show the incentive or feasibility constraint that drives the reduction. Move repeated IC/IR cases and payment algebra.

The body usually needs one important display before the theorem and one interpretation paragraph after the theorem. If the proof idea is central, add one short proof paragraph that names the mathematical move. Then let the appendix do the verification.

## Assumptions And Examples

Assumptions should not appear as unexplained legal clauses. For each important assumption, add one of the following roles:

- It identifies the parameter.
- It makes the optimization problem convex or polynomially solvable.
- It preserves the conditional information structure.
- It rules out degenerate empirical rules.
- It isolates the mechanism of interest.
- It matches a standard model or a common operational practice.
- It gives a benchmark that makes the result interpretable.

For nonstandard definitions, examples are part of the argument. A good example shows why the standard object fails or why the new object captures the feature that matters.

## Result And Theorem Language

Strong result paragraphs usually draw from these moves. The local result decides the order and depth:

1. Local setup and condition.
2. The formal statement.
3. Benchmark or standard intuition.
4. Interpretation of the mathematical object.
5. Mechanism or proof idea.
6. Decision consequence or implementation meaning.

For rates, say what parameter drives difficulty. For example, dimension, sparsity, inventory, number of products, number of change points, uncertainty radius, and sample size should be tied to the operational burden they represent.

For approximation results, state both the factor and the comparator. For regret results, state the oracle or clairvoyant benchmark. For robust optimization, state the nominal distribution and uncertainty set. For empirical identification, state the source of variation and the threat it addresses.

## Comparative And Magnitude Language

Comparative language must be reviewable.

- `outperforms`: name the comparator, metric, setting, and whether the support is theorem, simulation, experiment, or case study.
- `improves`: name what metric improves and relative to what baseline. Avoid "improves performance" by itself.
- `dominates`: use only for a formal dominance relation or a complete empirical comparison over the stated set.
- `significant`: specify statistically significant, economically significant, or substantively large. If none applies, use a measured magnitude or a qualitative pattern.
- `substantial`, `large`, `meaningful`: use only with a magnitude, rate, estimate, confidence interval, or clearly bounded comparison.
- `robustly`: say robust across what perturbations, samples, assumptions, or uncertainty sets.

If the user's draft does not provide the comparator or metric, write a narrower sentence and flag the missing support only if the omission affects validity.

## Proof And Appendix Voice

Main-text proof exposition should name the strategy. Appendix proof prose can be denser, but it still needs signposts at load-bearing steps.

- Instead of "some algebra shows," name the algebraic role: rearranging the Bellman equation, applying convexity, taking the dual, telescoping regret, or bounding the relaxation.
- Instead of "it is easy to see," state the one fact that makes it easy, such as monotonicity, feasibility, conditional independence, or nonnegativity.
- When a proof uses a constructed instance, say what the instance is designed to show, such as tightness, hardness, or separation between policy classes.
- When a proof uses a coupling, state what is held fixed across policies and what is allowed to differ.
- When a proof uses a dual, say which primal object the dual prices, such as constraints, uncertainty, or future opportunity cost.

## What To Avoid

- "Important managerial implications" without an action, condition, and mechanism.
- "Novel framework" without the decision object and the missing feature it captures.
- "Robust result" without the perturbation, benchmark, or uncertainty set.
- "Efficient algorithm" without runtime, tractable reformulation, approximation, or empirical scaling.
- "Optimal policy" without objective, information structure, feasibility conditions, or benchmark.
- "Data-driven method" without observed data, latent object, and validation.
- "We can see" or "it is obvious" in proof prose.

## Reviewer Calibration For Math

A reviewer should not have to infer what kind of claim is being made. Label the claim in the prose:

- Structural characterization.
- Approximation guarantee.
- Regret bound.
- Convex reformulation.
- Identification result.
- Numerical validation.
- Empirical estimate.
- Policy implication.

Then keep the claim inside its assumptions. If a theorem is for affine decision rules, do not write as though it holds for all policies. If a numerical case study validates performance on one application, do not write as though it establishes universal dominance.

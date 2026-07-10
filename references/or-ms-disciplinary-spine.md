# OR/MS Disciplinary Spine

Use this reference when a passage needs to sound more like OR/MS in language, structure, model narration, or mathematical exposition. The core rules are already embedded in `SKILL.md`; this file gives more detailed patterns. Use these patterns diagnostically. Do not copy them as templates unless the user asks for a template.

## OR/MS Object Test

A full paragraph or section should answer only the questions relevant to its burden.

1. Who makes the decision?
2. What friction makes the decision nontrivial?
3. What formal object captures the decision?
4. What benchmark makes the result meaningful?
5. What mechanism or condition changes the decision?

The goal is not to recover all five items. The goal is to avoid prose that could fit any paper because it never names the central object, asserted relation, support, or relevant comparator. A theorem or measurement paragraph may need no decision maker, friction, or mechanism.

## Language

Prefer nouns that create formal traction.

- Decision objects: price, capacity, schedule, allocation, ranking, recommendation, disclosure, replenishment, routing, admission, inspection, sampling, treatment, procurement.
- Formal objects: policy, threshold, regime, constraint, objective, state, action, information structure, equilibrium, relaxation, benchmark, bound, approximation ratio, regret, estimator, counterfactual.
- Frictions: uncertainty, limited information, censoring, delayed feedback, congestion, capacity, incentives, strategic response, fairness, externality, nonstationarity, misspecification.
- Metrics: profit, revenue, cost, welfare, surplus, waiting time, fill rate, stockout risk, service level, regret, approximation gap, throughput, utilization, match quality, forecast error.

Avoid generic shells.

- Weak: "We develop a novel framework."
- Stronger: "We characterize when a platform should withhold demand information from sellers because disclosure intensifies price competition."
- Weak: "The model provides managerial insights."
- Stronger: "The threshold policy gives the retailer a testable rule: expand the assortment only when the demand lift exceeds the margin loss from cannibalization."
- Weak: "The algorithm improves performance."
- Stronger: "The policy reduces regret relative to the myopic benchmark by delaying exploitation until high-margin demand states are separated."

## Section Structure

### Abstract

Select the minimum burdens needed to compress the paper accurately. Common burdens include the central object, relevant departure or question, evidence type, headline result, comparator or metric, and boundary. No fixed four-move order or final implication is required.

- Decision or formal object, when needed for orientation.
- Friction, counterexample, or missing evidence, when it motivates the contribution.
- Model, empirical design, algorithm, simulation, or hybrid evidence.
- Headline result with the metric, comparator, and condition needed for accuracy.
- Implication only when the result changes a supported action, comparison, interpretation, or later analytical choice.

### Introduction

Choose an entry point that fits the evidence lane: operational setting, standard model, empirical pattern, counterexample, technical obstacle, construct, or portable formal object. Then order the remaining passages by prerequisite, warrant, and emphasis. The introduction should make the focal object, paper-level claim, source of credibility, and any consequential departure or boundary legible by the point each is needed; it need not follow an eight-step arc.

If the introduction uses a gap, state the exact unresolved comparison, evidence limit, formal obstacle, construct problem, or decision issue rather than saying only that no one has studied the topic. A gap paragraph is not mandatory.

### Model Section

The reader should understand the formal or empirical environment before relying on dense notation. Use the following as an inventory and introduce objects in the order imposed by timing or mathematical dependency; not every model needs every item.

1. Agents and institutional setting.
2. Timing.
3. State variables and information.
4. Decisions or controls.
5. Demand, payoff, cost, transition, or arrival primitives.
6. Objective and constraints.
7. Assumptions and their role.
8. Benchmark or solution concept.
9. What the model isolates.

### Results Section

Keep the formal or empirical result close to the support and interpretation it needs. A result unit may be claim-first or evidence-first. Add benchmark intuition, mechanism, comparative statics, condition, or implication only when they change how the result should be understood.

### Proof Exposition

Name the proof architecture.

- Monotonicity proof: say which object is monotone and which order is used.
- Threshold proof: show how the value difference crosses zero once.
- Approximation proof: state the relaxation, rounding, and loss bound.
- Regret proof: state the exploration event, concentration argument, and decomposition.
- Equilibrium proof: state existence, best response, fixed point, and uniqueness or multiplicity argument.
- Structural estimation proof: state identification, moment condition, or likelihood argument.

## Model Narration

Good OR/MS model narration does more than announce "we consider a model." It lets the reader recover the abstraction's role in the paper's claim.

Use a flexible content inventory:

- decision maker, system, construct, or formal object;
- timing, information, state, or observations;
- control, action, estimator, or feasible set;
- objective, payoff, transition, or constraints;
- comparator, benchmark, solution concept, or target estimand;
- abstraction, identification, computation, or mechanism role.

Select only the items the local passage needs and order them by dependency. An actor and friction are not mandatory. A queueing or control model may begin with the state; a theorem-driven subsection may begin with the policy class; an empirical model may begin with what is observed and latent.

For empirical or structural models, make the relation among observed data, latent object, identifying variation or structure, target estimand, and permitted claim strength recoverable. For algorithmic models, make the input or information, action or output, feasibility conditions, comparator, and performance criterion recoverable. These are content checks, not sentence molds.

## Mathematical Result Language

Match the verb to the result.

- Existence: "there exists" or "admits."
- Uniqueness: "is unique" or "the unique equilibrium."
- Characterization: "has a threshold structure," "is increasing in," "takes the form."
- Comparative static: "increases with," "decreases with," "can reverse when."
- Bound: "is bounded by," "achieves an approximation ratio of," "incurs regret of order."
- Convergence: "converges to," "with probability at least," "as the sample size grows."
- Identification: "is identified from," "is point identified under," "is partially identified by."
- Welfare comparison: "dominates," "can reduce welfare relative to," "improves total surplus when."

Never make the prose stronger than the theorem. If the theorem is asymptotic, local, under complete information, for two sellers, or under monotone demand, keep that qualifier in the sentence.

## Mathematical Intuition

After formal statements, use intuition that explains the mathematical force.

- Explain what becomes more expensive, more informative, more constrained, or more strategic.
- Explain why a marginal comparison changes sign.
- Explain which constraint binds and why.
- Explain what benchmark fails to account for.
- Explain why the policy form is simple despite a complicated environment.

Avoid intuition that only repeats the theorem.

- Weak: "The result shows that the optimal policy is threshold-based."
- Stronger: "The threshold arises because waiting has option value only while the posterior remains sufficiently diffuse. Once the posterior crosses the cutoff, the marginal value of another observation is lower than the margin lost from delaying the sale."

## Revision Checklist

- For ordinary paragraph rewrites, does the passage make its primary object or claim recoverable at the point where it is needed?
- For model paragraphs, is the model described as an environment rather than a list of symbols?
- For technical terms, is each loaded term tied to a definition, benchmark, or role?
- For result paragraphs, is the result paired with a benchmark intuition when a comparison matters?
- For managerial implications, is the action conditional?
- For theorem claims, are the assumptions or regimes close enough to the claim?
- For proof narratives, does the text name the mathematical move?
- For closing sentences, does the ending complete, qualify, interpret, or advance the paragraph's actual burden rather than summarize generically?

# OR/MS Disciplinary Spine

Use this reference when a passage needs to sound more like OR/MS in language, structure, model narration, or mathematical exposition. The core rules are already embedded in `SKILL.md`; this file gives more detailed patterns. Use these patterns diagnostically. Do not copy them as templates unless the user asks for a template.

## Five-Part OR/MS Test

A full paragraph or section should usually answer the questions that are relevant to its job.

1. Who makes the decision?
2. What friction makes the decision nontrivial?
3. What formal object captures the decision?
4. What benchmark makes the result meaningful?
5. What mechanism or condition changes the decision?

The goal is not to mention all five items in every sentence. The goal is to avoid prose that could fit any paper because it never names the decision, friction, or mechanism.

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

Use four moves: decision, friction, method, result. End with a conditional implication.

- Decision: name the actor and choice.
- Friction: name uncertainty, information, capacity, incentives, or behavior.
- Method: model, empirical design, algorithm, simulation, or hybrid design.
- Result: mechanism and condition, not only effect direction.
- Implication: who should do what, when.

### Introduction

Use an OR/MS arc.

1. Operational setting and decision.
2. Standard intuition or current practice.
3. Hidden friction.
4. Why existing models, data, or policies miss the friction.
5. Formal approach.
6. Main findings by mechanism.
7. Contributions by literature stream.
8. Managerial or policy consequence.

The gap should be a problem in decision logic, not a statement that no one has studied the topic.

### Model Section

The reader should understand the decision environment before the notation becomes dense.

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

Use a stable result unit.

1. Local setup reminder.
2. Formal proposition, theorem, or result claim.
3. Benchmark intuition.
4. Mechanism.
5. Comparative static, condition, or regime.
6. Managerial, algorithmic, or theoretical implication.

### Proof Exposition

Name the proof architecture.

- Monotonicity proof: say which object is monotone and which order is used.
- Threshold proof: show how the value difference crosses zero once.
- Approximation proof: state the relaxation, rounding, and loss bound.
- Regret proof: state the exploration event, concentration argument, and decomposition.
- Equilibrium proof: state existence, best response, fixed point, and uniqueness or multiplicity argument.
- Structural estimation proof: state identification, moment condition, or likelihood argument.

## Model Narration

Good OR/MS model narration is not "we consider a model." It is a compressed explanation of why the abstraction is useful.

Useful internal pattern:

`Actor + decision + friction. To isolate this friction, model [agents] who observe [information] and choose [actions] over [timing]. The objective is [objective] subject to [constraints]. The benchmark is [benchmark], which makes [metric or mechanism] interpretable.`

Do not write the pattern verbatim if it makes the prose stiff. It is a completeness check for model paragraphs, not a required sentence shape.

For empirical or structural models:

`The data reveal [observed object] but not [latent object]. The design/model uses [variation, instrument, moment, or structure] to recover [primitive or effect]. This supports [descriptive, causal, structural, or counterfactual] claims, but not [unsupported stronger claim].`

For algorithmic models:

`The algorithm uses [information] to choose [action] under [constraint]. Its performance is measured against [oracle, relaxation, offline optimum, or myopic benchmark]. The key difficulty is [coupling, adaptivity, nonconvexity, online arrivals, delayed feedback, or limited samples].`

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

- For ordinary paragraph rewrites, does the first sentence name a decision, tension, or claim?
- For model paragraphs, is the model described as an environment rather than a list of symbols?
- For technical terms, is each loaded term tied to a definition, benchmark, or role?
- For result paragraphs, is the result paired with a benchmark intuition when a comparison matters?
- For managerial implications, is the action conditional?
- For theorem claims, are the assumptions or regimes close enough to the claim?
- For proof narratives, does the text name the mathematical move?
- For closing sentences, does the sentence change a decision, policy, or belief rather than summarize generically?

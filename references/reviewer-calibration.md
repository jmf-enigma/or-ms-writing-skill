# Reviewer Calibration

Use this for cross-field OR/MS writing, referee-facing revisions, and passages where terminology could be read differently by different expert communities.

## Reviewer Model

Assume one reviewer is an expert in the closest technical field and another is an expert in the application or empirical setting. Each may be unfamiliar with the other field's conventions. The prose must let both reviewers understand the object, claim, evidence, and boundary of the claim.

## Overloaded Terms

- Causal. Use only with a design, identification argument, exogenous variation, experiment, instrument, or clearly stated causal model.
- Optimal. State the objective, constraints, information set, benchmark, and class of policies.
- Equilibrium. Name players, strategies, beliefs or expectations, timing, and solution concept when needed.
- Robust. Say robust to what: specification, sample, benchmark, parameter, stress test, distributional assumption, or out-of-sample environment.
- Fairness. Define the fairness notion. Do not let fairness mean welfare, equality, equity, nondiscrimination, procedural fairness, or consumer protection without saying which.
- Welfare. Distinguish consumer surplus, producer surplus, platform profit, total welfare, and distributional effects.
- Efficiency. Distinguish operational efficiency, allocative efficiency, productive efficiency, and welfare improvement.
- Learning. Say who learns, from what signal, at what timing, and how learning changes decisions.
- Platform. Say which side participates, what the platform controls, and which decisions remain decentralized.
- Data-driven. Say what data are observed, what is missing, and how the data map into decisions.

## Bridge Sentences

Use a bridge sentence when a passage crosses fields.

- For empirical readers reading a model: state the real-world object represented by the primitive.
- For theory readers reading empirical work: state the source of variation and what it identifies.
- For OM readers reading economics: state the operational lever and the performance metric.
- For economics readers reading OM: state the incentive or equilibrium force.
- For application reviewers reading algorithms: state the decision input, output, benchmark, and implementation constraint.

## Claim Narrowing

Narrow claims before polishing.

- Replace "improves performance" with the specific metric and comparison.
- Replace "solves the problem" with the decision it clarifies.
- Replace "is robust" with the stress test or assumption class.
- Replace "has important implications" with action, condition, mechanism, and caveat.
- Replace "identifies the effect" with the design or identifying variation.

## Claim Strength Ladder

Use the strongest verb that the evidence supports, not the strongest verb that sounds polished.

- Theory with proof can "establish," "characterize," "bound," or "prove" a formal claim under stated assumptions.
- A model analysis can "show," "suggest," or "imply" a mechanism within the model. It does not by itself establish external empirical validity.
- A simulation can "illustrate," "validate numerically," or "compare performance" in the tested instances. It does not establish universal dominance unless the design proves it.
- An observational estimate can "estimate," "document," or "is consistent with" a mechanism. It should not become causal without identification.
- A case study can "illustrate" or "demonstrate feasibility" in that setting. It should not become broad validation.

For any comparative claim, keep three items visible: comparator, metric, and condition. "Outperforms existing methods" is too broad. "Reduces regret relative to a static policy in nonstationary simulations" is reviewable.

## Evidence Preservation In Rewrites

When polishing existing text, preserve the author's evidence and scope.

- Do not add numerical magnitudes, significance, robustness, dominance, optimality, or causality.
- Do not remove qualifiers such as under Assumption 1, in the finite-horizon setting, for affine policies, in our sample, or in the numerical study.
- If a sentence feels weak because support is missing, narrow the claim rather than making it sound more confident.

## Final Reviewer Pass

Before finalizing, ask:

1. Could an expert in a nearby field attach a different meaning to a key term?
2. Is the evidence type clear enough to support the claim's strength?
3. Is the model's objective or empirical estimand explicit?
4. Is the benchmark clear?
5. Is any cross-field object translated once into the reviewer's likely vocabulary?

# OR/MS Word Choice And Collocations

Use this when the user's complaint is that the wording sounds odd, unnatural, translated, nonnative, over-polished, or not like Management Science / Operations Research prose. This reference is about word choice and collocation: which words naturally go together in OR/MS writing.

The main rule is simple: do not choose a word because it is more academic. Choose the word that normally governs the object in this field.

## Core Preference

Prefer the plain field word when it is exact.

- `study` a decision problem, setting, model, question, or behavior.
- `examine` behavior, adoption, response, heterogeneity, or mechanism evidence.
- `estimate` an effect, elasticity, parameter, counterfactual, or demand curve.
- `document` descriptive patterns.
- `find` empirical estimates or experimental effects.
- `show` direct analytical, empirical, or numerical results.
- `characterize` policy forms, equilibria, thresholds, regimes, and comparative statics.
- `derive` expressions, bounds, reformulations, first-order conditions, and sufficient conditions.
- `establish` theorem-backed guarantees, rates, bounds, and optimality claims.
- `bound` regret, value loss, error, welfare loss, probability, and approximation gaps.
- `compare` policies, algorithms, treatments, regimes, benchmarks, and objectives.
- `evaluate` interventions, field implementations, algorithms, and policies.

Do not upgrade these verbs into ornate substitutes. `Utilize`, `facilitate`, `delve into`, `illuminate`, `underscore`, and `showcase` usually make the sentence less native unless they are the exact word needed.

## Words That Often Sound Translated

These phrases are not merely "bad style"; they usually point to the wrong English object.

| Awkward wording | Better direction |
|---|---|
| `managerial enlightenment` | `managerial implications`, or better, the action and condition |
| `has important influence on` | `affects`, `changes`, `shifts`, `alters`, or `is associated with` |
| `optimize the strategy` | `choose a policy`, `set a price`, `design a mechanism`, `select an assortment` |
| `conduct research on` | `study`, `examine`, `estimate`, `model`, or `characterize` |
| `make a research` | `study` or `examine` |
| `according to the model` | `the model shows`, `the proposition implies`, `the estimate suggests` |
| `it can be found that` | `we find`, `the estimate shows`, or make the table/theorem the subject |
| `certain extent` | a metric, condition, magnitude, or explicit caveat |
| `provide theoretical basis` | `provide a condition`, `derive a benchmark`, `establish a guarantee` |
| `practical significance` | the decision, metric, action, or operating condition |
| `optimize decision-making` | `improve profit`, `reduce waiting time`, `choose disclosure precision`, etc. |
| `put forward a model` | `develop a model`, `study a model`, or name what the model captures |
| `analyze the mechanism of` | `show how`, `separate`, `identify evidence for`, or `trace the channel through` |

When a phrase sounds translated, do not search for a fancier synonym. Ask what the object is: decision, metric, theorem, estimate, policy, mechanism, or condition.

## Verb-Object Fit

Many awkward sentences use a good verb with the wrong object.

Use:

- `a policy improves profit`, not `a policy improves decision making`;
- `an estimator recovers demand`, not `an estimator obtains insights`;
- `a theorem establishes a bound`, not `a theorem provides understanding`;
- `a model captures a friction`, not `a model considers practical significance`;
- `a design separates a mechanism from selection`, not `a design solves endogeneity` unless it truly does;
- `data record behavior`, `data reveal variation`, or `data make units comparable`, not `we leverage data`;
- `a robustness check preserves the sign and magnitude`, not `robustness is good`;
- `an appendix verifies cases`, not `an appendix shows the whole story`.

If the verb cannot take the object naturally, change the object first.

## Preposition Choices

Small prepositions often decide whether a sentence sounds native.

- `effect on` an outcome, subgroup, or behavior.
- `increase in` a metric; `increase by` an amount; `increase for` a subgroup; `increase when` a condition holds.
- `improve relative to` or `compared with` a named benchmark.
- `robust to` a specification, perturbation, or assumption change.
- `sensitive to` a parameter, assumption, or data choice.
- `under` an assumption, policy class, information structure, cost condition, or regime.
- `in` a setting, market, sample, experiment, model, or regime.
- `among` a subgroup; `for` a decision maker or unit.
- `driven by` a mechanism; `arises from` a source; `hinges on` a condition.
- `consistent with` mechanism evidence; `hard to reconcile with` an alternative explanation.
- `abstract from` secondary details; `allow for` a feature; `allow X to affect Y`.

Avoid:

- `influence to`;
- `impact for` when the object is an outcome;
- `robust for`;
- `sensitive for`;
- `based on the above`;
- `under the background of`;
- `with the development of`.

## Evidence Verbs

A sentence sounds off when the verb claims more than the evidence.

- Use `find` for empirical estimates and experimental effects.
- Use `document` for descriptive facts.
- Use `estimate` for parameter or effect recovery.
- Use `suggest` for interpretation that is plausible but not fully identified.
- Use `is consistent with` for mechanism evidence.
- Use `show` when the evidence directly supports the claim.
- Use `establish` when a theorem or proof supports the claim.
- Use `identify` only when the design, model, or variation supports identification.
- Use `validate` for out-of-sample, implementation, simulation, or empirical checks.

Avoid:

- `prove` for empirical results;
- `identify` for any interesting pattern;
- `validate` for a theoretical example;
- `demonstrate` when the evidence only suggests;
- `significant` without saying statistical, economic, or substantive.

## Nouns That Need Anchors

These nouns can be useful, but they sound generic without a local object.

- `framework`: only if the paper truly provides a reusable conceptual or formal framework. Otherwise use `model`, `formulation`, `policy class`, `estimator`, or `algorithm`.
- `mechanism`: say what behavior or mathematical channel links cause and effect.
- `insight`: usually replace with result, condition, estimate, implication, or mechanism.
- `implication`: say who should do what under what condition.
- `strategy`: use only when the actor chooses a strategic action over time. Otherwise use `policy`, `rule`, `decision`, `price`, `assortment`, `allocation`, or `disclosure precision`.
- `efficiency`: define whether it means cost, welfare, throughput, matching efficiency, computational efficiency, or statistical efficiency.
- `robustness`: say robust to what.

## Common OR/MS Collocations

Use these only when the content supports them.

- `decision problem`, `policy class`, `solution concept`, `information structure`;
- `state variable`, `belief state`, `arrival process`, `transition probability`;
- `objective function`, `capacity constraint`, `incentive constraint`, `feasible set`;
- `benchmark policy`, `myopic policy`, `oracle policy`, `current practice`, `status quo`;
- `approximation guarantee`, `regret bound`, `lower bound`, `upper bound`;
- `threshold policy`, `priority rule`, `base-stock policy`, `index policy`;
- `field experiment`, `quasi-experimental variation`, `identifying variation`;
- `treatment effect`, `heterogeneous effect`, `mechanism evidence`;
- `primary metric`, `countervailing metric`, `out-of-sample performance`;
- `robustness check`, `alternative specification`, `placebo test`;
- `managerial implication`, but only after the action and condition are explicit.

## More Natural Rewrites

Weak:

`This paper puts forward a decision-making framework that provides important managerial enlightenment for platform information strategy optimization.`

Better:

`We study how a platform should choose disclosure precision when sellers set prices after observing the disclosed signal.`

Weak:

`The model has practical significance for improving decision-making efficiency.`

Better:

`The model identifies the regimes in which reducing disclosure precision raises platform profit without lowering match quality.`

Weak:

`According to the analysis, the algorithm has good performance.`

Better:

`The algorithm achieves the same order as the lower bound under the complete-pooling condition.`

Weak:

`We leverage transaction data to explore the impact of AI.`

Better:

`We use transaction-level data to estimate how AI recommendations change managers' pricing decisions.`

Weak:

`The robustness proves the validity of the conclusion.`

Better:

`The estimate preserves its sign and magnitude under the alternative demand specification.`

## Final Word-Choice Pass

Before finalizing, check:

1. Does each verb naturally govern its object?
2. Is any abstract noun replacing a decision, metric, theorem, estimate, or policy?
3. Does each preposition match the relation: effect on, robust to, compared with, under, among, driven by?
4. Does the evidence verb match the support?
5. Is a translated phrase being polished instead of rebuilt?
6. Could a simpler field word carry the sentence more naturally?

When in doubt, choose the ordinary word that lets the object do the work.

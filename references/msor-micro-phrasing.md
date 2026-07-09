# OR/MS Micro-Phrasing

Use this when the user asks for very fine wording, sentence-level idiom, native expression, or prose that should feel closer to Management Science, Operations Research, or M&SOM without copying an author's personal style. These are sentence mechanics distilled from public abstracts and full-text passages. Transfer the logic, not the wording.

If the prose sounds stiff, difficult, or over-engineered, load `msor-natural-prose.md` first. This file is a diagnostic bank, not a phrasebook. Do not assemble final sentences by filling every slot in a pattern.

## Source Readings

Recent language calibration used two layers.

First, a broad Crossref scan of recent abstracts:

- 80 Management Science article records from 2022-2026, 74 with abstracts.
- 80 Operations Research article records from 2022-2026, 75 with abstracts.
- 80 M&SOM article records from 2020-2026, 75 with abstracts.

The broad scan is for expression frequency and sentence function, not for copying wording. It showed especially frequent use of `we study`, `we find`, `we show`, `when`, `under`, `whereas`, `without`, `relative to`, and, in M&SOM, structured abstract labels such as problem definition, methodology/results, and managerial implications.

Second, closer reading used these public pages:

- Federgruen, Liu, and Lu, "Sourcing with Demand Updates," Management Science, 2026.
- Feng, Li, and Shanthikumar, "Transfer Learning, Cross Learning and Co-Learning with Operational Data Analytics," Management Science, 2026.
- DeValve and Myles, "Approximation Algorithms for Dynamic Inventory Management on Networks," Management Science, 2024.
- Manshadi, Rodilitz, Saban, and Suresh, "Redesigning VolunteerMatch's Search Algorithm," Management Science, 2025.
- Brahm, Lafortune, Magelssen, and Tessada, "Collaboration, Workplace Practice Adoption, and Performance," Management Science, 2026.
- Cui et al., "The Effects of Generative AI on High-Skilled Work," Management Science, 2026.
- Li, Belo, and Li, "Can Reward Uncertainty Encourage Social Referrals?," Management Science, 2026.
- Kanazawa, Kawaguchi, Shigeoka, and Watanabe, "AI, Skill, and Productivity," Management Science, 2025.
- Garcia, Tolvanen, and Wagner, "Demand Estimation Using Managerial Responses to Automated Price Recommendations," Management Science, 2022.
- Levi, Paulson, and Perakis, "Designing Inclusive Offerings," Management Science, 2025.
- Wang, Song, Yousefi, and Jiang, "Optimal Learning and Management of Threatened Species," Management Science, 2024.
- Gong and Png, "Automation Enables Specialization: Field Evidence," Management Science, 2023.
- Tsirtsis et al., "Optimal Decision Making Under Strategic Behavior," Management Science, 2024.
- Witkowski, Freeman, Vaughan, Pennock, and Krause, "Incentive-Compatible Forecasting Competitions," Management Science, 2022.
- Chen, He, Rong, and Wang, "An Integer Programming Approach for Quick-Commerce Assortment Planning," Management Science, 2026.
- Varma, Bumpensanti, Maguluri, and Wang, "Dynamic Pricing and Matching for Two-Sided Queues," Operations Research, 2022.
- Yuan, Du, and Hu, "Dynamic Pricing Under Self-Exciting Arrival Processes," Operations Research, 2026.
- Bhandari and Russo, "Global Optimality Guarantees for Policy Gradient Methods," Operations Research, 2024.
- Crimmins, Halderman, and Sturt, "Improving the Security of United States Elections with Robust Optimization," Operations Research, 2024.
- Segev, "Near-Optimal Adaptive Policies for Serving Stochastically Departing Customers," Operations Research, 2024.
- Hu and Zhou, "Dynamic Type Matching," M&SOM, 2021.
- Dong, Shi, Zheng, and Jin, "Capacity Management in Networks," M&SOM, 2026.
- Yan, Castro, Frazier, Ma, and Nazerzadeh, "Matching Queues, Flexibility, and Incentives," M&SOM, 2026.
- Roels, Smirnov, Tsetlin, and Wait, "You, Me, or We? Coproductive Principal-Agent Dynamics," M&SOM, 2026.
- Dong and Kouvelis, "Impact of Tariffs on Global Supply Chain Network Configuration," M&SOM, 2020.
- Bastani and Cachon, "The Human-AI Contracting Paradox," M&SOM, 2026.

## Original-Text Micro Observations

These observations come from original abstract/introduction/model/result passages, not only metadata.

- **AI and worker skill papers** often move from a broad projection to the empirical condition needed to test it. Useful micro-move: "testing this assumption requires [microdata/object] in settings where [technology] is actually adopted." Then the setting is justified by measurement: individual productivity is measured by [duration/output], workers make comparable decisions, and the tool assists by [mechanism].
- **Demand-estimation papers** often introduce identification as a behavioral delay or institutional feature. Useful micro-move: "the identification strategy rests on the ability to observe [decision] adjusting with delay to [shock]." The intuition sentence holds one object fixed and lets one variable move.
- **Queueing and dynamic matching papers** build the model sentence by sentence. They name the system, then the graph or state representation, then arrivals, controls, objective, and scaling regime. The strongest abstract sentences do not say the model is complex; they show what enters, what the operator controls, and what rate or bound follows.
- **M&SOM structured abstracts** use labels, but the underlying prose is still decision-centered. `Problem definition` names the intermediary's decision; `Methodology` names the formal object; `Results` names sufficient conditions or policy structure; `Managerial implications` translates the structural property into a simpler decision.
- **Field-experiment papers** often make the experiment credible by saying the intervention was run in the ordinary operational environment, which units were randomized, and which metric changes without a countervailing loss.
- **Theory-to-implementation platform papers** often use an "inspired by theory yet mindful of practice" move: the formal result motivates a simpler implementable rule, and field evidence then checks whether the rule preserves the key metric.
- **Applied conservation, health, and public-sector OR papers** do not start with "optimization is important." They start with a resource-constrained decision in a domain the reader can see, then show why uncertainty, false negatives, hidden state, or implementation constraints make the standard approach insufficient.
- **Technical OR papers** often state the model in one compressed sentence and then immediately identify the state variable, sufficient statistic, or objective that carries the rest of the paper. The abstract may include a behavioral implication, but the implication is anchored to a formal regime or comparison.
- **Learning and ML-adjacent OR/MS papers** often begin by acknowledging that a popular method works broadly, then expose the narrow failure mode the paper resolves. This makes the theorem feel motivated rather than ornamental.
- **Strategic-behavior and mechanism papers** use concrete decision domains before notation. They name the decision maker's objective, the agent's response, and the induced distribution or equilibrium object before giving the formal game.
- **Appendix proof pages** use plain labels such as `Appendix D. Proof of Theorem 1` and `Proof.`. They do not dress up technical verification as "proof idea." In the body, `Proof.` may hold a complete short proof or a venue-style one-line pointer; explanatory sketches are normally ordinary prose.

## Original-Page Close-Reading Ledger

Use these as transferable sentence logic. Do not copy the wording.

- **Threatened-species learning** begins with a scarce-resource public problem, then adds the information constraint: managers must allocate survey and protection resources while the species' presence, detectability, and dynamics are uncertain. The model sentence earns its notation by saying what the POMDP learns, what it controls, and why the reformulation is lower-dimensional.
- **Automation and specialization** starts from an established theory of specialization, asks what impedes it, and then changes one element of the theory: workers coordinate with machines rather than with other workers. The field evidence is introduced only after the proposition tells the reader what mechanism the experiment tests.
- **Strategic decision making under behavioral response** opens with familiar high-stakes domains, separates the predictive model from the decision policy, and then makes transparency the source of strategic response. The model is introduced as a Stackelberg game after the reader already knows who moves first and why.
- **Forecasting competitions** defines the scoring object before the theorem, shows why the natural deterministic mechanism fails, and then introduces the randomized mechanism as a repair. The appendix proofs are literal and sequential; each starts by fixing the mechanism, reports, or distribution used in the argument.
- **Dynamic pricing under self-exciting arrivals** builds the abstract in an OR style: stochastic process, operational phenomenon, sufficient state, policy structure, comparative static by regime, and a performance-loss guarantee.
- **Policy-gradient guarantees** does not oversell nonconvexity. It first says why policy gradients are used, then names the limitation, gives a simple failure mode, and states the structural property that removes bad stationary points.
- **Hospital capacity networks in M&SOM** makes the feedback loop the central friction: routing depends on congestion, and congestion is affected by routing. The structured abstract then splits method into two components before naming what the approach improves relative to alternatives.
- **Matching-queue and incentive papers in M&SOM** put the conventional wisdom in the first few lines and then show when it backfires because agents respond strategically. The policy contribution is not merely "new"; it is simple, robust to private information, and implementable without exact parameters.
- **Coproductive principal-agent papers** make the decision menu explicit before equilibrium analysis. The reader sees the operating modes first, then learns which modes occur too often or too rarely under second-best or linear contracts.
- **Election security robust optimization** starts from an existing institutional procedure, explains why the manual alternative is costly, and frames optimization as a low-cost improvement rather than an abstract algorithmic advance.
- **Quick-commerce assortment planning** makes the physical linkage do the conceptual work: online assortments depend on local-store inventory, so online personalization and store assortment cannot be optimized separately.
- **M&SOM tariff and supply-chain-network papers** often close the body with a managerial or policy reading before the appendix. The appendix then begins directly with `Proof of Proposition 1` and verifies concavity, sign, or case conditions.

The recurring movement is one-step progression: a visible operating object, then the friction, then the formal or empirical object that resolves it. Use that movement when it fits; do not reproduce it as an arrow list in final prose.

## Model And Formula Narration From Original Pages

Model prose in MS/OR is usually narrow and cumulative. It rarely dumps all notation at once.

1. **Name the operating system.** Say whether the object is a platform, queueing network, inventory system, Stackelberg game, POMDP, scoring mechanism, assortment model, or field experiment.
2. **Name the state or primitive that will carry the model.** For a dynamic model, this might be congestion, excitement level, belief state, inventory vector, backlog, type distribution, or feature distribution.
3. **Name the control.** The operator prices, routes, matches, audits, allocates capacity, selects an assortment, chooses a disclosure policy, or chooses a decision rule.
4. **State the objective and benchmark close together.** A result is easier to trust when the reader can see whether the comparison is to a deterministic relaxation, open-loop policy, classic revenue-management model, pooled estimator, deterministic mechanism, or current operational procedure.
5. **Display only the load-bearing object in the body.** The body display should define the optimization problem, transition, decomposition, or sufficient statistic used later. Constants, repeated cases, and verification details move to the appendix.
6. **Interpret after the display.** The sentence after an equation should tell the reader what the equation makes possible: a state reduction, a decomposition, a monotonicity result, an identification expression, a comparison, or a guarantee.

Useful body-model sentence moves:

- `The state variable records [operational object], so the policy can depend on [information] without tracking [irrelevant history].`
- `The formulation keeps [constraint or feedback loop] in the objective and moves [secondary detail] to the extension.`
- `The benchmark solves the same decision problem without [friction], which isolates the value of [mechanism].`
- `The relaxation separates [hard coupling] across [periods/types/resources], leaving [object] to be optimized or bounded directly.`
- `The induced distribution is the object the decision maker optimizes over after agents respond to the published policy.`
- `The deterministic problem provides an implementable policy; the dynamic problem provides the performance benchmark.`

## Proof And Appendix Habits From Original Pages

Original papers use fewer proof labels than AI drafts tend to use.

- A `Proof.` directly below a proposition is normal when it contains a short complete proof or follows a consistent one-line appendix-pointer convention. It is strange when an incomplete intuitive sketch is presented as if it were the proof.
- A body proof idea is usually unlabeled prose after the result. It names the constructed object, the hard term, and the move that controls it, then points to the appendix if the proof is long.
- Appendix headings are literal: `Proof of Theorem 1`, `Proof of Proposition 3`, `Proof of Lemma I.4`, `Additional Results`, `Model Extensions`, or `Robustness Checks`. They do not need elegant titles.
- Appendix proof openings fix objects before manipulating them: the policy, reports, distribution, event, queue state, or parameter regime is specified first.
- Long appendix proofs move through small obligations: establish form, verify feasibility, prove monotonicity or concavity, split cases, combine inequalities, then map back to the stated result.
- The body should not say only "see Appendix." It should first state what the theorem, estimate, or robustness check means for the decision, benchmark, or mechanism.

Useful proof-idea sentence moves:

- `The proof first reduces the problem to [object], then shows that [hard term] is bounded by [comparison].`
- `The coupling keeps [state] ordered across systems, which lets the argument compare [cost/reward/probability] period by period.`
- `The lower bound follows by considering policies that cannot distinguish [states/types]; the proposed policy matches this order by [move].`
- `The argument is easiest to see in the two-type case. The appendix extends the same comparison to the full type space.`
- `The displayed decomposition is the only step needed in the body; the appendix verifies the remaining cases.`

## Corpus-Level Micro-Signals

Across the broad scan, the best transferable signals are small.

- MS empirical abstracts often move from a concrete context to a measured effect, then to mechanism, heterogeneity, or a bounded implication. `We find` is common, but the good sentence attaches the finding to a metric or subgroup.
- MS theory/model abstracts often use `we show`, `we develop`, or `we provide`, but the stronger sentences quickly name the formal object, condition, benchmark, or guarantee.
- OR abstracts rely more on `under`, `when`, lower bounds, approximation, and asymptotic language. The useful habit is to attach every rate or guarantee to a scaling regime, policy class, or lower bound.
- M&SOM abstracts often organize content by problem definition, methodology/results, and managerial implications. The surface structure is formal, but the best sentences remain decision-centered: who chooses what, under what uncertainty, and with what operational consequence.
- Across all three, `without` is a compact way to state tradeoff preservation, and `whereas` is useful only when two comparable objects are being contrasted.

## The Small Sound

Native OR/MS sentences often feel good because small relation words do real work.

- `where` introduces the model or setting: a system where information, timing, incentives, or constraints differ from the benchmark.
- `when` introduces a regime: the policy matters when a condition holds and may not matter otherwise.
- `whereas` contrasts two objects that play parallel roles.
- `relative to` and `compared with` require a named comparator.
- `without` is useful for tradeoffs: one metric improves without sacrificing another.
- `consistent with` is for mechanism evidence that supports but does not prove a channel.
- `rather than` separates the mechanism the paper studies from a tempting but wrong explanation.
- `under` attaches a claim to an assumption, cost condition, information structure, or policy class.
- `given that` is useful when a decision is made under carryover, constraints, or partial observability.
- `only to` limits the recipient of an effect and is often cleaner than a second caveat sentence.
- `by` should name the mechanism, not merely the method. Write `by shortening cruising time`, not `by using our framework`.
- `to fill this gap` is acceptable only when the gap has just been made specific.

Do not use these words as decoration. Each should name the relation it creates.

## Entry Sentences

Choose the verb by the object.

- `We study` fits a setting, decision problem, model, or empirical question.
- `We examine` fits managerial behavior, adoption, response, or empirical mechanisms.
- `We evaluate` fits a field implementation, algorithm, intervention, or policy.
- `We compare` fits policies, treatments, benchmarks, algorithms, or regimes.
- `We characterize` fits policy structure, equilibrium regions, thresholds, comparative statics, or regimes.
- `We establish` fits theorem-backed guarantees, bounds, rates, or sufficient conditions.
- `We derive` fits expressions, reformulations, first-order conditions, bounds, or decompositions.
- `We document` fits descriptive empirical patterns.
- `We find` fits empirical estimates or experimental effects.

Avoid `we propose` for an implication and `we leverage` for data. Say what the data identify, reveal, miss, or make comparable.

## Fine Verb-Object Choices

Many awkward paragraphs come from a verb that does not govern the right object.

| Verb | Good objects | Watch-outs |
|---|---|---|
| `assist` | decision makers with a task | Follow with `by` plus the mechanism. |
| `encourage` | adoption, referrals, exploration, reporting | Name who responds and through which incentive. |
| `narrow` | a gap, disparity, confidence set, performance loss | State the baseline gap. |
| `separate` | mechanism from alternative, treatment from selection, aggregate from subsystem performance | Do not use it for unrelated lists. |
| `recover` | latent demand, elasticity, counterfactual, parameter | Name the source of variation. |
| `ensure` | feasibility, suitability, service level, incentive compatibility | Avoid for vague benefits. |
| `reduce to` | a simpler choice, comparison, policy class, tradeoff | Use only when the model/proof actually simplifies the object. |
| `arise from` | bound, effect, heterogeneity, bias | Pair with a concrete source. |
| `hinge on` | condition, inequality, tradeoff, identification assumption | Use sparingly and only with the exact hinge. |

## Tiny Sentence Moves

Use these as sentence logic, not templates.

After using a move, rewrite the sentence in the paper's own nouns. The final prose should not sound like it was generated from a form with fields for actor, decision, benchmark, mechanism, and implication.

### Setting And Friction

- `A platform/firm/manager must [decision] before [uncertainty or response] is known.`
- `The standard policy treats [object] as fixed. In the focal setting, [object] changes between decisions.`
- `The usual benchmark captures [known force], but it misses [friction].`
- `The difficulty is not [obvious issue] alone; it is that [decision consequence] depends on [hidden state, incentive, or information].`
- `Many [practices/interventions/policies] require [coordination/cooperation/adoption] between [actors], but [misaligned incentives/information frictions] make this difficult.`
- `[Technology/tool/algorithm] assists [actor] with [task] by [mechanism].`
- `In this context, [outcome] is observed at [granularity], and [decision maker] has discretion over [choice].`
- `To fill this gap, we study [decision/effect] in a setting where [key object] is observed rather than projected.`

### Method Enters Naturally

- `The model isolates this force by allowing [primitive] to affect [decision object].`
- `The design separates [mechanism] from [alternative explanation].`
- `The estimator uses [institutional behavior or timing] to recover [latent object].`
- `The algorithm changes [ranking/allocation/control] while keeping [countervailing metric] visible.`
- `The decomposition turns [hard object] into [comparison, bound, or policy class] that can be analyzed directly.`
- `The problem is modeled as [formal object], where [state/action/edge] represents [operational object].`
- `The objective is to choose [control] to maximize/minimize [metric] given that [carryover, constraint, or uncertainty].`
- `The treatment varies [practice or information] while holding fixed [environment, timing, or decision context].`
- `The empirical strategy compares [period/group] with [period/group] before [confound or implementation change] occurs.`
- `The formulation keeps [essential constraint] and abstracts from [detail] that is stress-tested later.`

### Result With Benchmark

- `When [condition] is high/low, [policy] improves [metric] relative to [benchmark].`
- `Otherwise, [simpler benchmark] is close to optimal, sufficient, or asymptotically optimal.`
- `[Theorem/proposition] characterizes [object] as a function of [state, signal, parameter, or constraint].`
- `The comparison shows that [mechanism] matters in [regime], whereas [benchmark intuition] is enough in [regime].`
- `The field implementation increases [primary metric] without reducing [countervailing metric].`
- `The gain accrues only to [subgroup], narrowing [gap] relative to [baseline].`
- `The treatment increases [desired behavior] and reduces [bad outcome], without increasing [resource input].`
- `The algorithm achieves [rate/ratio] under [condition], and the rate matches [lower bound or benchmark].`
- `The solution is asymptotically optimal for [aggregate system] and for [subsystem], unlike [pooling/default] that optimizes only [aggregate metric].`
- `The optimal policy takes a simple form: [assignment, threshold, priority, or base-stock rule].`

### Mechanism And Boundary

- `The effect is concentrated among [units/regime], consistent with [mechanism].`
- `The result is muted when [boundary condition] weakens [mechanism].`
- `The pattern is hard to reconcile with [alternative channel] because [diagnostic evidence].`
- `After this result, the relevant decision is no longer [old decision] alone; it is [new decision] under [condition].`
- `The result supports [bounded action] when [condition], but it does not support [overbroad claim].`
- `The asymmetric effect is driven by [mechanism for one actor] and [different mechanism for another actor].`
- `The mechanism operates through [intermediate behavior], not through [nearby alternative].`
- `The effect persists after [robustness check], suggesting that [threat] is unlikely to explain the result.`
- `The condition is mild in [practical regime] but rules out [pathological case].`
- `[Actor] should [action] when [observable condition], but [caveat] when [condition fails].`

### Proof And Theory

- `The proof constructs [auxiliary object] and compares it with [benchmark or relaxation].`
- `The key step bounds [hard term] by [tractable object].`
- `The lower bound captures [tradeoff], whereas the upper bound is induced by [policy class].`
- `Combining the two bounds yields [guarantee] under [condition].`
- `The theorem converts [opaque optimization] into [policy form, threshold, or computable condition].`
- `Under [resource pooling, convexity, monotonicity, or cost] condition, [policy] achieves [rate/ratio].`
- `The proof shows that any policy in [class] must incur [lower bound], so the proposed policy is rate optimal.`
- `The priority property reduces the within-period decision to [simpler tradeoff].`
- `The relaxation preserves [constraint or metric] while making [comparison] separable across [states/types/periods].`
- `The argument balances [current cost] against [future cost], which is the term missed by the simpler bound.`

### Related Work And Positioning

- `This stream studies [object]. It typically treats [feature] as [assumption], whereas our setting makes [feature] endogenous to [decision].`
- `Closest to our setting are papers on [stream], which capture [shared element] but do not allow [missing feature].`
- `Relative to this literature, the paper contributes [result type] for [more general class, finite regime, different information structure].`
- `Our result is tangential to [method stream] in technique but central to [decision stream] in object.`
- `The paper differs from [stream] in the source of variation, not only in the application.`

### Data, Measurement, And Empirical Design

- `The data record [behavior] at the [unit-time] level, allowing the analysis to distinguish [mechanism] from [alternative].`
- `The treatment was implemented in [operational setting], so the estimate reflects [real decision context] rather than stated preferences.`
- `The design compares [treated units] with [control units] facing the same [market, platform, or timing].`
- `The identifying variation comes from [timing, recommendation delay, randomization, institutional rule], not from cross-sectional differences alone.`
- `We interpret the heterogeneity as a boundary condition because [subgroup] changes [mechanism].`

### Appendix And Robustness Pointers

- `The appendix gives the full derivation; the body uses the resulting [bound, threshold, or expression] to interpret [decision].`
- `The robustness checks preserve the sign and magnitude of [main estimate] under [alternative specification].`
- `Additional checks rule out [threat] but do not change the interpretation of [main mechanism].`
- `The online appendix reports [secondary tables], whereas the body focuses on [primary metric or comparison].`
- `The extension changes [assumption] but leaves [main mechanism] intact.`

## Micro-Revisions

Prefer exact local wording:

- Weak: `The model provides valuable insights.`
  Better: `The model shows when the adjusted policy improves expected profit relative to the classic benchmark.`
- Weak: `This has important managerial implications.`
  Better: `Managers should use the adjusted rule only when the demand signal is noisy enough to justify the second order.`
- Weak: `We leverage data to study the problem.`
  Better: `The data record delayed responses to recommendations, which creates variation in the prices managers would otherwise choose.`
- Weak: `The algorithm performs well.`
  Better: `The algorithm increases access without reducing total matches in the field implementation.`
- Weak: `The proof is based on standard arguments.`
  Better: `The proof couples the original process with a monotone benchmark and bounds the value-function gap.`
- Weak: `We use an experiment to study collaboration.`
  Better: `The experiment varies whether managers and workers receive a joint prompt to coordinate safety practices.`
- Weak: `The AI tool improves productivity.`
  Better: `The tool shortens the time low-skilled drivers spend searching for customers, which narrows the productivity gap.`
- Weak: `Our method is better than pooling.`
  Better: `Pooling improves aggregate fit, whereas the proposed rule preserves the decision structure of each subsystem.`
- Weak: `The inclusive offering framework is useful.`
  Better: `The formulation asks for the smallest set of offerings that keeps every user within the suitability threshold.`

## Compact Expression Bank

Use these fragments only when the user's content supports them.

- `in the presence of [constraint, overlap, uncertainty, competition]`
- `in settings where [tradeoff or information problem] matters`
- `in a setting in which [object] is observed/varied/randomized`
- `given that [state, demand, or supply] may carry over`
- `as part of the ordinary course of business`
- `before [decision, recommendation, or implementation] occurs`
- `after [intervention, adoption, or recommendation] is implemented`
- `among [subgroup] rather than in the full sample`
- `for stocks/firms/users/products with the largest [change/exposure]`
- `is revealed between the two decisions`
- `is observed before the action is chosen`
- `is carried over to the next period`
- `is predicted to be high`
- `is faster or easier to measure than [true outcome]`
- `shortens the search/cruising/waiting time`
- `narrows the gap between high- and low-[type] units`
- `increases [metric] the most for [units with largest treatment intensity]`
- `diminishes over time`
- `becomes stronger over time`
- `without a meaningful decrease in [countervailing metric]`
- `without an increase in [resource input]`
- `under a mild [cost/information/regularity] condition`
- `under a complete resource pooling condition`
- `takes a simple [threshold/priority/base-stock] form`
- `captures the tradeoff between [current decision] and [future consequence]`
- `falls in a subclass of [broader object]`
- `approaches the parametric/oracle solution asymptotically`
- `is suboptimal for individual subsystems`
- `rules out [alternative explanation] as the main driver`
- `is consistent across [experiments/samples/settings]`
- `is robust when controlling for [threat]`
- `is robust to [alternative specification/check]`
- `depends only on [cost/demand/information] parameters`
- `is independent of [lead time/network size/sample size]`
- `generalizes the benchmark by allowing [feature]`
- `keeps [essential friction] visible`
- `abstracts from [secondary detail]`
- `stress-tests [assumption] in the appendix`

## Function-Word Pairings

These pairings are often more important than vocabulary.

- `increase/decrease ... for` subgroup or treated unit.
- `increase/decrease ... by` amount or percentage.
- `increase/decrease ... when` condition or regime.
- `improve ... relative to` explicit benchmark.
- `improve ... without` countervailing loss.
- `is driven by` mechanism.
- `is concentrated among` heterogeneous effect group.
- `is muted when` boundary condition.
- `is consistent with` mechanism evidence.
- `is hard to reconcile with` alternative explanation.
- `arises from` source of bound, effect, or policy.
- `reduces to` simplified tradeoff or choice.
- `is equivalent to` formal transformation.
- `is asymptotically optimal for` system, subsystem, or policy class.
- `matches the lower bound` rate or order.

## Richer Replacement Patterns

Use these to convert rough Chinese-English notes into native OR/MS sentences.

- `X 很重要` -> `[Actor] must [decision] because [constraint/information/timing] changes [metric].`
- `模型考虑了 Y` -> `The model allows [Y] to affect [decision/objective], which is the channel absent from [benchmark].`
- `结果很好` -> `[Policy/intervention] improves [metric] relative to [benchmark] when [condition].`
- `机制是 Z` -> `The effect operates through [Z], rather than [alternative channel].`
- `鲁棒性都成立` -> `The estimate preserves its sign and magnitude under [specific alternative specification/check].`
- `有管理启示` -> `[Actor] should [action] when [observable condition], but [caveat] when [condition fails].`
- `证明思路是构造 A` -> `The proof constructs [A] to bound [hard term] and then compares the resulting objective with [benchmark].`

## Sentence Endings

The end of a sentence carries emphasis. End on a local object, not filler.

Good endings:

- the benchmark being beaten;
- the condition under which the result holds;
- the metric that changes;
- the mechanism being isolated;
- the boundary that prevents overclaiming.

Weak endings:

- `important implications`;
- `valuable insights`;
- `in practice`;
- `for managers`;
- `in the real world`;
- `for future research`.

## Fine-Grained Checks

Before finalizing a sentence, ask:

1. Does the verb take the right object?
2. Does any comparison name the comparator?
3. Does any improvement name the metric?
4. Does any mechanism claim identify the alternative explanation it rules out or weakens?
5. Does any `when`, `whereas`, `relative to`, `without`, or `consistent with` express a real relation?
6. Does the sentence end on the thing the reader should remember?

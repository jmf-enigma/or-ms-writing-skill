# General Topic Story Engine

Use this for any OR/MS, OM, econ, mechanism, empirical, learning, or policy topic when the right story is not obvious. This is the general layer above author-specific or topic-specific references.

## Universal Research Story

Every strong OR/MS paper can usually be explained through eight questions.

1. Who makes the decision?
2. What do they control?
3. What friction makes the decision hard?
4. What standard policy, intuition, or literature misses that friction?
5. What model, data, experiment, or algorithm isolates the friction?
6. What benchmark makes the result interpretable?
7. What changes under the result?
8. Who should act differently, when, and with what caveat?

If one of these questions has no answer, the writing should expose that gap rather than hide it.

## First-Pass Classifier

Before choosing a topic lens, classify the paragraph or section by what it must prove to the reader.

- Practice paper: a real decision is common, but the usual practice fails under a hidden friction.
- Theory paper: a benchmark is incomplete, and a characterization, impossibility result, or comparative static changes the logic.
- Empirical paper: a pattern or managerial belief needs evidence, identification, magnitude, and a decision consequence.
- Algorithm paper: a decision is hard because of scale, uncertainty, information, or timing, and the method changes the feasible benchmark.
- Policy paper: a rule affects welfare, distribution, incentives, or implementation, and the result is conditional.
- Review or positioning paragraph: the goal is not to list papers, but to show which gap each stream leaves open.

If the topic is unfamiliar, use the universal fallback. Name the actor, decision, friction, evidence type, benchmark, implication, and caveat. Then draft in the language of that local setting rather than importing words from platform, pricing, or social operations papers.

## Topic Lenses

### Healthcare And Service Operations

- Actor: hospital, clinic, physician network, dispatcher, case manager, patient.
- Decision: schedule, triage, route, allocate capacity, open slots, use overtime, coordinate services.
- Friction: access delays, no-shows, stochastic service times, patient heterogeneity, coordination across stations.
- Benchmark: independent scheduling, myopic scheduling, deterministic service times, current practice.
- Evidence: queueing model, stochastic program, simulation, real hospital data, deployment result.
- Story move: make the operational constraint concrete before introducing the optimization model.

### Supply Chain, Inventory, And Sustainability

- Actor: manufacturer, retailer, supplier, logistics planner, regulator.
- Decision: source, stock, replenish, nearshore, expedite, recover, emit, hedge.
- Friction: lead time, disruption, demand uncertainty, capacity, emissions, cost-service tradeoff.
- Benchmark: lean supply chain, efficient supply chain, offshore sourcing, fixed-price or base-stock policy.
- Evidence: structural result, numerical study, counterfactual, field data, lifecycle or emissions model.
- Story move: show how a familiar efficiency policy changes when resilience or sustainability enters the objective.

### Platforms, Marketplaces, And Digital Operations

- Actor: platform, seller, buyer, worker, creator, user, regulator.
- Decision: price, rank, match, recommend, disclose, subsidize, moderate, rotate content.
- Friction: two-sided choice, incentives, fairness, churn, information, herding, congestion, trust.
- Benchmark: status quo platform rule, no regulation, myopic matching, standard assortment, uniform pricing.
- Evidence: mechanism model, matching model, experiment, field data, counterfactual, simulation.
- Story move: start from a product or policy readers recognize, then reveal the hidden state or incentive.

### Empirical And Behavioral OM

- Actor: manager, employee, consumer, supplier, platform, experimental subject.
- Decision: order, forecast, disclose, price, comply, adopt, exert effort.
- Friction: behavioral bias, information asymmetry, incentives, limited attention, trust, transparency.
- Benchmark: rational benchmark, no-treatment group, prior theory, existing policy.
- Evidence: field experiment, lab experiment, observational design, replication, structural estimate.
- Story move: state the behavioral or empirical puzzle before the identification or estimation design.

### Algorithms, Optimization, And Stochastic Systems

- Actor: decision maker, planner, algorithm, platform operator.
- Decision: allocate, match, schedule, route, learn, stop, accept, reject, price.
- Friction: online arrival, uncertainty, combinatorial complexity, limited information, coupling, nonconvexity.
- Benchmark: LP relaxation, myopic policy, batching, greedy heuristic, clairvoyant optimum, known bound.
- Evidence: approximation guarantee, regret bound, lower bound, computational study, real-data simulation.
- Story move: make the algorithmic bottleneck managerial by naming the operational decision and benchmark.

### Mechanism Design, Econ Theory, And Policy

- Actor: designer, regulator, platform, seller, bidder, agent.
- Decision: choose rules, payments, allocation, disclosure, regulation, information design.
- Friction: incentives, private information, participation, collusion, fairness, welfare tradeoff.
- Benchmark: first-best, no regulation, standard auction, posted price, Myerson, efficient allocation.
- Evidence: theorem, impossibility result, characterization, comparative statics, counterexample.
- Story move: translate the theorem into what the rule can and cannot achieve.

### Learning, Bandits, And Data-Driven Decisions

- Actor: algorithm, platform, seller, physician, recommender, experimenter.
- Decision: explore, exploit, recommend, price, treat, allocate samples, stop learning.
- Friction: uncertainty, adaptive data, regret, customer attrition, delayed feedback, fairness or safety.
- Benchmark: oracle, classical UCB/Thompson, static policy, unconstrained learner, no-learning policy.
- Evidence: regret bound, confidence event, simulation, field deployment, counterfactual.
- Story move: connect the learning objective to the cost of bad decisions during learning.

### Finance, Marketing, Accounting, And Information Systems

- Actor: investor, lender, consumer, advertiser, auditor, analyst, firm, regulator.
- Decision: disclose, price, target, allocate capital, lend, report, audit, adopt technology.
- Friction: information asymmetry, agency, attention, privacy, bias, strategic reporting, network effects.
- Benchmark: rational benchmark, no disclosure, uniform targeting, standard risk model, status quo policy.
- Evidence: empirical design, structural model, experiment, theory, counterfactual.
- Story move: translate the business object into the belief, incentive, or constraint that changes the decision.

### Energy, Transportation, Environment, And Public Infrastructure

- Actor: grid operator, utility, transit agency, city, regulator, logistics planner, community.
- Decision: dispatch, route, price, invest, locate capacity, ration, repair, decarbonize.
- Friction: congestion, reliability, intermittency, emissions, equity, resilience, spatial spillovers.
- Benchmark: deterministic planning, current operations, no policy, shortest path, least-cost dispatch.
- Evidence: optimization model, simulation, field data, counterfactual, policy evaluation.
- Story move: keep the physical constraint visible so the social or environmental implication does not float free.

### Education, Labor, Public Policy, And Organizations

- Actor: school, worker, employer, agency, household, regulator, nonprofit, platform.
- Decision: admit, assign, incentivize, train, monitor, disclose, target, comply.
- Friction: selection, incentives, fairness, capacity, incomplete information, behavior, compliance.
- Benchmark: current rule, random assignment, no treatment, first-best, equal allocation.
- Evidence: causal estimate, field experiment, mechanism model, administrative data, theorem.
- Story move: separate what the result shows about behavior from what it recommends as policy.

## Transfer Rules

- Do not force platform language onto non-platform topics. Change the actor and friction first.
- Do not force Xiao Lei paper patterns onto topics where the core object is healthcare, infrastructure, finance, education, or policy. Transfer the structure, not the vocabulary.
- Do not force managerial implications onto a pure theorem. If the result is methodological, the implication may be for modelers or algorithm designers.
- If the paper is empirical, the story lives in the puzzle, identification, and decision consequence.
- If the paper is theoretical, the story lives in the benchmark, mechanism, and boundary condition.
- If the paper is algorithmic, the story lives in the operational bottleneck, guarantee, and implementability.
- If the paper is policy-facing, keep the implication conditional and name the welfare or distributional tradeoff.

## Paragraph Generator Map

Use this as an internal map, not visible labels.

Practice. Decision. Default. Friction. Lens. Result. Consequence. Caveat.

For method-heavy papers:

Bottleneck. Existing method. Missing feature. New formulation. Guarantee or estimate. Where it matters.

For empirical papers:

Puzzle. Setting. Data. Identification. Estimate. Mechanism. Decision consequence. External-validity caveat.

For theory papers:

Question. Benchmark. Assumptions. Characterization. Mechanism. Boundary case. Implication.

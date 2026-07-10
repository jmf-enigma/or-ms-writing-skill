# General Topic Argument And Story Logic

Use this for any OR/MS, OM, econ, mechanism, empirical, learning, or policy topic when the right story is not obvious. This is the general layer above author-specific or topic-specific references.

## Diagnostic Inventory

When the topic is unfamiliar, use these questions to recover the argument. They are not slots for every paper, section, or paragraph.

1. What burden does this passage carry: define, motivate, establish, compare, interpret, qualify, or connect?
2. What is its central object: decision, institution, construct, estimand, model, policy class, theorem object, algorithm, or empirical contrast?
3. Which definitions, timing facts, assumptions, or design facts are prerequisites?
4. What claim or distinction must the reader leave with?
5. What theorem, estimate, comparison, citation, proof move, or design feature warrants that claim?
6. Which comparator, metric, population, regime, or policy class controls its meaning?
7. What relation connects it to the surrounding passage?
8. What should receive emphasis, and what is verification or scope detail?

Ask only what the evidence lane needs. A practice paper may need an actor and decision; a pure theorem may not. A measurement paper may center a construct rather than a friction. A descriptive empirical result may not support a mechanism or recommendation. Missing support for a claim the paper actually makes is a gap; absence of an unused story beat is not.

## First-Pass Classifier

Before choosing a topic lens, classify the paragraph or section by what it must prove to the reader.

- Practice paper: make the decision or operating object, consequential constraint, comparison, and support legible. A failed incumbent practice is only one possible motivation.
- Theory paper: make the formal object, assumptions, result type, comparison, and scope legible. The entry point may be a benchmark, definition, counterexample, theorem, or application.
- Empirical paper: make the construct or estimand, evidence source, identifying or descriptive warrant, metric, and scope legible. A decision consequence is needed only when claimed.
- Algorithm paper: make the problem object, information and feasibility conditions, comparator, performance criterion, and guarantee or computational evidence legible.
- Policy paper: separate the rule or intervention, evidence type, welfare or distributional criterion, implementation condition, and supported conclusion.
- Review or positioning paragraph: synthesize what the cited work establishes and state the exact relation to the current object; a gap narrative is not mandatory.

If the topic is unfamiliar, first identify the passage's burden and evidence type. Then select only the central object, prerequisite, warrant, comparator, relation, implication, or caveat needed for that burden. Draft in the language of the local setting rather than importing words from platform, pricing, or social operations papers.

## Topic Lenses

### Healthcare And Service Operations

- Actor: hospital, clinic, physician network, dispatcher, case manager, patient.
- Decision: schedule, triage, route, allocate capacity, open slots, use overtime, coordinate services.
- Friction: access delays, no-shows, stochastic service times, patient heterogeneity, coordination across stations.
- Benchmark: independent scheduling, myopic scheduling, deterministic service times, current practice.
- Evidence: queueing model, stochastic program, simulation, real hospital data, deployment result.
- Possible relations: operating constraint to formulation, formulation to policy comparison, queueing result to service metric, or deployment evidence to scope.

### Supply Chain, Inventory, And Sustainability

- Actor: manufacturer, retailer, supplier, logistics planner, regulator.
- Decision: source, stock, replenish, nearshore, expedite, recover, emit, hedge.
- Friction: lead time, disruption, demand uncertainty, capacity, emissions, cost-service tradeoff.
- Benchmark: lean supply chain, efficient supply chain, offshore sourcing, fixed-price or base-stock policy.
- Evidence: structural result, numerical study, counterfactual, field data, lifecycle or emissions model.
- Possible relations: objective to tradeoff, information timing to inventory policy, disruption regime to sourcing comparison, or model result to emissions or service metric.

### Platforms, Marketplaces, And Digital Operations

- Actor: platform, seller, buyer, worker, creator, user, regulator.
- Decision: price, rank, match, recommend, disclose, subsidize, moderate, rotate content.
- Friction: two-sided choice, incentives, fairness, churn, information, herding, congestion, trust.
- Benchmark: status quo platform rule, no regulation, myopic matching, standard assortment, uniform pricing.
- Evidence: mechanism model, matching model, experiment, field data, counterfactual, simulation.
- Possible relations: platform rule to user response, incentive to equilibrium, ranking objective to distributional outcome, or experiment to mechanism. A recognizable product need not precede a formal object.

### Empirical And Behavioral OM

- Actor: manager, employee, consumer, supplier, platform, experimental subject.
- Decision: order, forecast, disclose, price, comply, adopt, exert effort.
- Friction: behavioral bias, information asymmetry, incentives, limited attention, trust, transparency.
- Benchmark: rational benchmark, no-treatment group, prior theory, existing policy.
- Evidence: field experiment, lab experiment, observational design, replication, structural estimate.
- Possible relations: construct to measure, institutional variation to estimand, estimate to magnitude, mechanism evidence to alternative explanation, or boundary to interpretation. The design may appear first when its object is already active.

### Algorithms, Optimization, And Stochastic Systems

- Actor: decision maker, planner, algorithm, platform operator.
- Decision: allocate, match, schedule, route, learn, stop, accept, reject, price.
- Friction: online arrival, uncertainty, combinatorial complexity, limited information, coupling, nonconvexity.
- Benchmark: LP relaxation, myopic policy, batching, greedy heuristic, clairvoyant optimum, known bound.
- Evidence: approximation guarantee, regret bound, lower bound, computational study, real-data simulation.
- Possible relations: formal problem to hardness, relaxation to guarantee, state structure to policy, algorithm to benchmark, or computation to operating scale. A canonical problem need not be given an artificial managerial wrapper.

### Mechanism Design, Econ Theory, And Policy

- Actor: designer, regulator, platform, seller, bidder, agent.
- Decision: choose rules, payments, allocation, disclosure, regulation, information design.
- Friction: incentives, private information, participation, collusion, fairness, welfare tradeoff.
- Benchmark: first-best, no regulation, standard auction, posted price, Myerson, efficient allocation.
- Evidence: theorem, impossibility result, characterization, comparative statics, counterexample.
- Possible relations: definition to implementability, incentive constraint to characterization, counterexample to impossibility, theorem to welfare comparison, or information regime to boundary.

### Learning, Bandits, And Data-Driven Decisions

- Actor: algorithm, platform, seller, physician, recommender, experimenter.
- Decision: explore, exploit, recommend, price, treat, allocate samples, stop learning.
- Friction: uncertainty, adaptive data, regret, customer attrition, delayed feedback, fairness or safety.
- Benchmark: oracle, classical UCB/Thompson, static policy, unconstrained learner, no-learning policy.
- Evidence: regret bound, confidence event, simulation, field deployment, counterfactual.
- Possible relations: feedback structure to regret, confidence event to guarantee, exploration rule to operating cost, data regime to policy comparison, or safety constraint to feasible learning.

### Finance, Marketing, Accounting, And Information Systems

- Actor: investor, lender, consumer, advertiser, auditor, analyst, firm, regulator.
- Decision: disclose, price, target, allocate capital, lend, report, audit, adopt technology.
- Friction: information asymmetry, agency, attention, privacy, bias, strategic reporting, network effects.
- Benchmark: rational benchmark, no disclosure, uniform targeting, standard risk model, status quo policy.
- Evidence: empirical design, structural model, experiment, theory, counterfactual.
- Possible relations: disclosure to belief, contract to incentive, information system to workflow, empirical variation to estimate, or estimate to bounded business interpretation.

### Energy, Transportation, Environment, And Public Infrastructure

- Actor: grid operator, utility, transit agency, city, regulator, logistics planner, community.
- Decision: dispatch, route, price, invest, locate capacity, ration, repair, decarbonize.
- Friction: congestion, reliability, intermittency, emissions, equity, resilience, spatial spillovers.
- Benchmark: deterministic planning, current operations, no policy, shortest path, least-cost dispatch.
- Evidence: optimization model, simulation, field data, counterfactual, policy evaluation.
- Possible relations: physical constraint to feasible policy, dispatch or routing decision to metric, model comparison to emissions or reliability, or policy result to distributional boundary.

### Education, Labor, Public Policy, And Organizations

- Actor: school, worker, employer, agency, household, regulator, nonprofit, platform.
- Decision: admit, assign, incentivize, train, monitor, disclose, target, comply.
- Friction: selection, incentives, fairness, capacity, incomplete information, behavior, compliance.
- Benchmark: current rule, random assignment, no treatment, first-best, equal allocation.
- Evidence: causal estimate, field experiment, mechanism model, administrative data, theorem.
- Possible relations: assignment rule to behavior, design to causal contrast, estimate to policy scope, incentive to compliance, or capacity constraint to distributional outcome.

## Transfer Rules

- Do not force platform language or its favored causal story onto non-platform topics. Replace the central objects, evidence relations, comparators, and scope with those of the actual setting.
- Do not force Xiao Lei paper patterns onto topics where the core object is healthcare, infrastructure, finance, education, or policy. Transfer the structure, not the vocabulary.
- Do not force managerial implications onto a pure theorem. If the result is methodological, the implication may be for modelers or algorithm designers.
- Empirical papers are often organized around a pattern or question, the support for the estimate, and its interpretation; identification and decision consequences enter only when claimed.
- Theoretical papers are often organized around a formal departure, characterization, comparison, or boundary; a managerial mechanism is not mandatory.
- Algorithmic papers are often organized around a decision object, computational obstacle, guarantee, and validation; the operating context can be brief when the formal problem is canonical.
- If the paper is policy-facing, keep the implication conditional and name the welfare or distributional tradeoff.

## Possible Dependency Paths

Use these only to diagnose a missing dependency. Do not fill every slot and do not use them to generate uniform paragraphs.

Practice may move from a decision to a constraint, comparison, or observed consequence.

For method-heavy papers:

A method-heavy passage may need the exact object before the bottleneck, or it may state the new formulation first and explain which bottleneck it resolves.

For empirical papers:

An empirical passage may move from design to estimate, estimate to interpretation, or an observed pattern to the design that can distinguish explanations.

For theory papers:

A theory passage may move from a benchmark to a formal departure, from a counterexample to sufficient conditions, or from a characterization to the comparison it enables.

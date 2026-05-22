# Expanded OR/MS Language Corpus

Use this when the user asks for very idiomatic OR/MS prose, a more native journal voice, or language calibrated to Management Science, Operations Research, or M&SOM. These notes summarize high-level genre patterns from public abstracts, submission guidelines, and article pages. Do not copy source sentences. Transfer the sentence logic, not author-specific wording. For Management Science specifically, use `management-science-language-corpus.md` first.

## Source Set

Core journal guidance:

- Operations Research submission guidelines. Abstracts and introductions should be expository, concise, readable to non-specialists in the exact topic, and clear about problem, results, and significance.
- Management Science submission guidelines. Papers should study scientific questions about the practice of management and connect to managerial, organizational, individual, or functional business decisions.
- M&SOM submission guidelines. Structured abstracts use Problem definition, Methodology/results, and Managerial implications, with little technical jargon.

Article signals used for language calibration:

1. Varma, Bumpensanti, Maguluri, and Wang, "Dynamic Pricing and Matching for Two-Sided Queues," Operations Research, 2022.
2. Chen, Liu, and Hong, "An Online Learning Approach to Dynamic Pricing and Capacity Sizing in Service Systems," Operations Research, 2023.
3. Hu and Zhou, "Dynamic Type Matching," M&SOM, 2021.
4. Bhaskaran, "Sequential Product Development and Introduction by Cash-Constrained Start-Ups," M&SOM, 2020.
5. Tuna and Swinney, "Sustainability Implications of Supply Chain Responsiveness," M&SOM, 2023.
6. "Disclosing Delivery Performance Information When Consumers Are Sensitive to Promised Delivery Time, Delivery Reliability, and Price," M&SOM, 2024.
7. "Data-Driven Optimization for Commodity Procurement Under Price Uncertainty," M&SOM, 2020.
8. "Inventory Productivity and Stock Returns in Manufacturing Networks," M&SOM, 2023.
9. "Assortment Optimization for a Multistage Choice Model," M&SOM, 2023.
10. "Better Together! The Consumer Implications of Delivery Consolidation," M&SOM, 2023.
11. "Operating Room Staffing and Scheduling," M&SOM, 2020.
12. Lobel, "Revenue Management and the Rise of the Algorithmic Economy," Management Science, 2020.
13. Ai, Chen, Mei, Ye, and Zhang, "Putting Teams into the Gig Economy," Management Science, 2023.
14. "Incentives, Framing, and Reliance on Algorithmic Advice: An Experimental Study," Management Science, 2025.

## What Native OR/MS Prose Sounds Like

Native OR/MS prose is concrete before it is technical. It names the decision maker, the decision, the friction, and the benchmark before asking the reader to care about a model or estimator.

Good openings usually do one of four jobs.

- Name a practice and the decision it creates.
- Name a standard policy and the force it misses.
- Name an operational bottleneck and the benchmark that fails.
- Name an empirical pattern and the managerial belief it challenges.

Avoid opening with importance alone. A sentence such as "X is increasingly important" feels unfinished unless it immediately says who must decide what and why the standard decision rule is strained.

## Journal-Specific Language

### Operations Research

Use a compact, result-forward style. OR readers tolerate technical objects early, but only after the operational problem is visible.

Typical modules:

1. Application class or operational system.
2. Decision controls and objective.
3. Model abstraction.
4. Policy, algorithm, characterization, or bound.
5. Benchmark comparison.
6. Scale, optimality, regret, approximation, or lower-bound statement.

Useful verbs:

- formulate, characterize, establish, derive, prove, show, compare, bound, approximate, decompose, construct, analyze.

Use "we propose" for an algorithm or policy, not for an implication. Use "we show" for a theorem-backed claim. Use "we demonstrate" for numerical or simulation evidence.

### Management Science

Use a broader management frame. The prose should make a manager, executive, platform operator, regulator, consumer, worker, investor, or organization visible.

Typical modules:

1. Managerial or organizational phenomenon.
2. Tension in practice.
3. Study design, model, experiment, or data.
4. Main estimate or mechanism.
5. Heterogeneity, persistence, welfare, or implementation consequence.

Useful verbs:

- examine, identify, estimate, test, document, compare, explain, quantify, evaluate, trace, distinguish.

Management Science abstracts often read naturally when magnitudes are concrete, heterogeneity is named, and the mechanism is not oversold. Avoid turning every result into a universal prescription.

### M&SOM

Use decision-centered structure and operational nouns. Structured abstracts often make the prose clearer even when the final target is not M&SOM.

Typical modules:

1. Problem definition. Name the operational decision and the choice set.
2. Methodology/results. Name the model or empirical design and the two or three results that matter.
3. Managerial implications. State who should act differently and under what condition.

Useful verbs:

- consider, investigate, study, model, formulate, solve, characterize, delineate, validate, implement, operationalize.

M&SOM style is comfortable with concrete managerial stakes. It should still avoid generic advice. A good implication says when a policy is valuable, when it backfires, and which observable condition separates the two.

## Sentence Moves To Reuse

Use these as structures, not as fixed wording.

### Motivation

- `[Practice] creates a decision problem for [actor], who must [choice].`
- `[Actor] often uses [standard policy]. This policy can fail when [friction] changes [state, incentive, or information].`
- `[Setting] is attractive because [benefit], but the same feature creates [operational risk].`

### Gap

- `Existing models capture [known force]. They leave open how [missing force] changes [decision or outcome].`
- `Prior work typically treats [object] as [assumption]. In our setting, [object] is endogenous to [decision].`
- `This distinction matters because [mechanism].`

### Method

- `We model [actor's] problem as [formal object] in which [key primitives].`
- `We use [method] to separate [mechanism] from [confound, benchmark, or alternative explanation].`
- `The formulation keeps [essential friction] while abstracting from [secondary detail].`

### Result

- `The analysis yields three findings. First, [result]. Second, [result]. Third, [condition or boundary].`
- `The result is driven by [mechanism], not by [plausible but wrong explanation].`
- `When [condition], [force A] dominates [force B]. When [condition fails], the ranking reverses.`
- `Compared with [benchmark], [policy] improves [metric] because [mechanism].`

### Managerial Or Policy Implication

- `[Actor] should use [policy] when [observable condition] is high, because [mechanism].`
- `The result cautions against [common action] when [condition].`
- `The policy is not uniformly beneficial. It improves [metric] only when [assumption or state] holds.`
- `For regulators, the main lesson is to choose [policy object] before imposing [constraint], because different constraints protect different stakeholders.`

## Native Verb Discipline

Prefer ordinary OR/MS verbs with exact objects.

- Use "study" when introducing the research problem.
- Use "consider" when the formal setting matters.
- Use "investigate" when exploring how characteristics change a decision.
- Use "examine" for empirical or behavioral questions.
- Use "formulate" for models and optimization problems.
- Use "characterize" for policy structure, equilibrium, thresholds, or optimal solutions.
- Use "identify" for mechanisms, conditions, causal effects, or managerial regimes.
- Use "derive" for analytical expressions and bounds.
- Use "establish" for theorem-backed claims.
- Use "validate" for simulation, field experiments, or out-of-sample tests.
- Use "delineate" sparingly for separating regimes or conditions.

Avoid verbs that sound polished but do no work.

- Replace "provides insights into" with "shows when," "identifies why," or "characterizes how."
- Replace "leverages" with "uses," unless the sentence names exactly what extra information becomes usable.
- Replace "enhances" with the metric that improves.
- Replace "facilitates" with the action it makes easier.
- Replace "underscores" with the result or condition.
- Replace "sheds light on" with the mechanism.

## Noun Discipline

Use nouns that belong to the setting.

- Pricing and revenue management: price, fee, demand, willingness to pay, capacity, arrival rate, assortment, surplus, welfare, margin.
- Matching and platforms: participant, user, driver, worker, customer, supply, demand, match quality, waiting time, abandonment, compatibility, engagement.
- Service operations: queue, delay, staffing, overtime, service rate, reliability, no-show, appointment, capacity.
- Supply chains: responsiveness, efficiency, lead time, sourcing, inventory, procurement, spot purchase, forward contract, emissions, disruption.
- Learning and algorithms: policy, oracle, regret, exploration, exploitation, feedback, confidence, benchmark, lower bound, approximation.
- Empirical and behavioral work: treatment, control, estimate, magnitude, persistence, heterogeneity, mechanism, identification, counterfactual.

Do not use a generic noun if the paper has a better local noun. "Performance" is weaker than profit, wait time, match rate, no-show rate, welfare, regret, inventory productivity, emissions, or return probability.

## Abstract Patterns

### Compact OR Or Management Science Abstract

Write one paragraph with five beats.

1. The operational decision.
2. The friction or missing force.
3. The model, data, experiment, or algorithm.
4. Two or three results in mechanism language.
5. The implication for the actor or literature.

Keep the first sentence readable without equations. If a method is technical, introduce the practical object before the notation.

### M&SOM Structured Abstract

Use the required labels only when the user asks for M&SOM or a structured abstract. Otherwise, borrow the order without labels.

- Problem definition. The first sentence should name the decision and choice set.
- Methodology/results. Combine method and findings. Do not let the method paragraph become a tool list.
- Managerial implications. State an action, a condition, and a caveat.

## Result-Interpretation Patterns

A polished OR/MS result paragraph usually follows this order.

1. State the formal result in words.
2. Name the benchmark intuition.
3. Explain the mechanism with because.
4. State the condition with when.
5. Translate the condition into an observable or managerial variable.

Weak result language:

- "This result is surprising and important."
- "This finding provides several managerial insights."
- "Our framework improves decision making."

Better result logic:

- "The result reverses the myopic ranking when waiting costs are low, because delaying matches thickens the market enough to offset abandonment risk."
- "The constraint increases consumer surplus only when the protected group is large enough for the seller to adjust the common price rather than exit the segment."
- "The learner should reduce exploration when bad recommendations shorten the horizon over which future learning can pay off."

## Related-Work Patterns

Related work should sound like a map, not a bibliography.

- Start each stream with what the stream explains.
- Spend one sentence on the limitation that matters for this paper.
- End the paragraph with this paper's distinct mechanism, data, or result.

Do not write "Our paper is the first to..." unless the claim is defensible. Prefer "Our paper differs by..." or "We depart from this stream by..."

## Field-Native Replacements

- Bad: "This study has important implications for managers."
  Better: `The result tells managers when [policy] should be used and when it should be avoided.`
- Bad: "The model captures the complexity of real-world operations."
  Better: `The model keeps [friction] and [constraint], which are the two features that change the policy ranking.`
- Bad: "The proposed algorithm significantly improves performance."
  Better: `The algorithm reduces [metric] relative to [benchmark] in [setting or regime].`
- Bad: "The paper fills a gap in the literature."
  Better: `Existing work assumes [assumption]. We allow [departure], which changes [result].`
- Bad: "The findings highlight the importance of considering customer behavior."
  Better: `Customer behavior changes the optimal policy because [mechanism].`
- Bad: "Our approach is robust and practical."
  Better: `The policy keeps its advantage when [stress test] changes, and it requires only [data or operational input].`

## Final Native-Language Pass

Before returning polished prose, check five things.

1. Does the first sentence name a real actor, decision, or tension?
2. Does each "we" verb have a specific object?
3. Does each result identify a mechanism or condition?
4. Does each implication name who acts and when?
5. Can any generic word be replaced by a local operational metric?

If the prose still sounds translated, simplify the sentence. OR/MS style is usually more native when the sentence is shorter, the actor is visible, and the mechanism is stated with because or when.

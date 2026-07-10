# MS/OR Full-Text Close Reading

Use this when prose still sounds strange after word-choice and sentence-craft passes, or when the user asks how MS/OR papers actually write the body, model, theorem, proof idea, or appendix. These notes come from reading full-text body sections and appendices, not only abstracts. They are style signals, not templates.

## Source Signals

Recent close-reading signals include full-text HTML or PDF versions of:

- Garcia, Tolvanen, and Wagner, "Demand Estimation Using Managerial Responses to Automated Price Recommendations," Management Science.
- Li, Belo, and Li, "Can Reward Uncertainty Encourage Social Referrals?", Management Science.
- Cowgill, Hernandez-Lagos, and Wright, "Does AI Cheapen Talk?", Management Science.
- Caplin, Dean, Glimcher, and Rutledge, "The ABCs of Who Benefits from Working with AI: Ability, Beliefs, and Calibration," Management Science.
- Kim, "The Value of Competitor Information: Evidence from a Field Experiment," Management Science.
- Gong and Png, "Automation Enables Specialization: Field Evidence," Management Science.
- Guo, "Gathering Information Before Negotiation," Management Science.
- Brown and Smith, "Unit Commitment Without Commitment," Operations Research.
- Wang, Song, Yousefi, and Jiang, "Optimal Learning and Management of Threatened Species," Management Science.
- Bird and Frug, "A Theory of Front-Line Management," full working-paper version with technical appendix.
- Varma, Bumpensanti, Maguluri, and Wang, "Dynamic Pricing and Matching for Two-Sided Queues," Operations Research.
- Yan, Castro, Frazier, Ma, and Nazerzadeh, "Matching Queues, Flexibility, and Incentives," M&SOM.
- Bhandari and Russo, "Global Optimality Guarantees for Policy Gradient Methods," Operations Research / arXiv.
- Recent empirical Management Science papers with theoretical background, data, empirical strategy, primary results, and limitations sections.
- Additional close readings from full-text INFORMS papers on human-centered AI field experiments, algorithmic advice incentives and framing, external data capabilities in search, on-demand delivery platforms, supply-chain blockchain design, food-delivery platform contracts, blockchain information provision, threatened-species optimal learning, drug-resistance optimal control, contractual screening, and cash-constrained nanostore experiments.
- Bertsimas and Kallus, "From Predictive to Prescriptive Analytics," Management Science.
- Ban and Rudin, "The Big Data Newsvendor," Operations Research.
- Elmachtoub and Grigas, "Smart Predict, then Optimize," Management Science.
- Besbes and Zeevi, "Dynamic Pricing Without Knowing the Demand Function," Operations Research.
- Ferreira, Lee, and Simchi-Levi, "Analytics for an Online Retailer," M&SOM.
- Buell, Kim, and Tsay, "Creating Reciprocal Value Through Operational Transparency," Management Science.
- Cachon and Swinney, "The Value of Fast Fashion," Management Science.
- DeValve and Myles, "Approximation Algorithms for Dynamic Inventory Management on Networks," Management Science.

Do not imitate any author's personal cadence. Extract field-level choices: where the sentence starts, how the model is introduced, how a result is interpreted, and where the proof is placed.

## What The Body Usually Does

Strong MS/OR body prose is plain but not flat. It gives the reader the next object at the moment the reader needs it.

- Introductions often begin with a concrete institutional or technical object, then show why the standard view, current practice, or existing model is insufficient.
- The turn is usually a real relation: a new technology changes signal cost, private information changes matching incentives, stochastic arrivals make pricing and matching inseparable, or a recommendation system creates useful quasi-experimental variation.
- The method enters only after the reader knows what it is for. `We model`, `we estimate`, or `we propose` should answer a question already visible in the paragraph.
- Result paragraphs keep the comparator and metric close: profit loss from the fluid benchmark, screening error relative to true expertise, throughput relative to random assignment, elasticity estimates relative to a preferred demand model.
- Boundaries are not apologies. They tell the reviewer what the claim is conditional on: a policy class, information structure, scaling regime, experiment, sample, or maintained behavioral assumption.

Full papers also show a useful discipline: a new section has a recoverable analytical or evidential role. A mechanism section may address an alternative explanation, a benchmark section may create a welfare comparison, an approximation section may replace an intractable object, and a behavioral experiment may distinguish channels left open by field data. Other sections define, replicate, validate, decompose, or extend. The prior section need not pose an explicit unresolved question.

The expanded close reading also shows that strong papers often make a durable object legible before asking a broad contribution claim to carry much weight. That object may be a decision loss, a coefficient, regret against a named benchmark, a lower bound, a policy class, or a sequence of experiments that separates mechanisms. Contribution order should follow actual dependency and emphasis; definition, obstacle, method, support, and relevance have no universal linear order.

Model notation is often earned by the setting. An implementation paper can describe the operating workflow, aggregation choice, and active managerial constraint before writing the optimization problem. A technical paper can formalize earlier when the new mathematical object itself is the contribution. The common test is whether the reader knows why each primitive or display is needed when it appears.

## Cross-Paper Motion And Language

The newer full-text comparisons add several finer-grained moves.

- **Question-led introductions** work when each question names a real unresolved decision and maps to a later analytical or empirical section. A list of rhetorical questions with no one-to-one payoff is weaker than a direct problem statement.
- **Contribution order** often mirrors dependency. A paper may define a loss or benchmark, show why direct optimization is difficult, derive a tractable object, establish its properties, and then evaluate it. Preserve that order only when each result uses the previous object.
- **Theorem progression** should make the relation among results recoverable. A later theorem may strengthen, specialize, generalize, decompose, contrast with, or run in parallel to an earlier result. If one theorem gives asymptotic optimality and the next gives a rate, the unresolved convergence speed is a useful relation; do not invent such a gap when the results are parallel.
- **Workflow-to-model transitions** explain the modeling unit, aggregation level, or implementation constraint before notation. This makes an abstraction look chosen rather than convenient.
- **Design limitations** belong near the design decision they qualify. If ideal randomization, measurement, or assignment was infeasible, state the operational reason and the remaining inferential limit before reporting the estimate.
- **Mechanism language** stays one step below the design. Use `consistent with` or `suggests` when a follow-up analysis narrows a channel without isolating it.
- **Result-to-conclusion transport** preserves the exact metric, comparator, magnitude, uncertainty, and population. The conclusion can interpret a 9.7% estimate or an approximation factor; it cannot rename revenue as profit or turn tested instances into universal dominance.
- **Practical interpretation** can translate a technical metric into an accessible comparison, but the translation must remain algebraically faithful to the original object.

Useful transition forms are quiet and local: `The first result establishes... The next result strengthens this conclusion by...`; `To isolate this channel, we...`; `Because the assignment could not be randomized at..., we...`; `The bound is informative when...`; `The numerical study compares the policy with...`. Use the relation, not the sentence shell.

## Lane-Specific Body Moves

Recent full texts show that "correct structure" is lane-specific, not a fixed sequence of `Model`, `Analysis`, and `Results`.

- **Controlled AI/human decision experiments** often define constructs before design. A natural order is introduction, construct definitions, measures, empirical framework, measurement challenges, experimental design, results, and conclusion. In this lane, a `Measures` or `Measurement Challenges` section can be the intellectual core because it explains why the experiment can separate ability, belief, calibration, and performance.
- **Strategy or platform field experiments** often use a conceptual motivation section before the design. The paper first states why the existing assumption is not observed, then lists plausible channels, then moves to experimental design and data. Results are organized by decision response, performance, mechanism evidence, heterogeneity, spillovers, or alternative explanations rather than by table number.
- **Automation and workplace field evidence** can start from a classic theory, introduce a new mechanism, show a small model, and then test the mechanism in the field. The theory is not a decorative preface; it fixes the mechanism the experiment must probe.
- **Analytical theory and bargaining papers** often use a base model, then sections named for variants or information regimes. Extensions are presented as changes in the economic object, not as a mechanical robustness list.
- **Applied OR and stochastic control papers** can put the model early, but still open with the operating process. The body keeps the main relaxation, theorem, policy, and performance comparison visible; pseudocode, proof details, network variants, and implementation details can move to the electronic companion after the body states their conclusion.
- **Theory papers with appendices** may say that all proofs are in the appendix, but the body still interprets each proposition and often gives the one equation or argument that makes the result believable.

If a draft feels strange, first ask whether it has forced the wrong lane. A paper about construct measurement should not be forced into a pure theorem rhythm; a theorem paper should not be padded with empirical-style robustness headings.

## Model Sections

Model sections usually climb from prose to notation.

1. Name the decision environment: who arrives, who chooses, who observes, and what the objective is.
2. Introduce the graph, state, signal, queue, price, policy, or belief only after its real-world object has been named.
3. State assumptions near the object they govern, then say what role the assumption plays if it could be questioned.
4. Define the objective or Bellman equation after actions and information are clear.
5. Add an example only when it helps the reader map the abstraction back to the setting.

Good model narration sounds like a careful researcher, not a notation manual. Instead of `We formulate a comprehensive framework`, write the local action: `The operator posts prices for each customer and server type and then chooses which compatible pair to match.`

In empirical and experimental papers, the "model" may be a construct or estimating object rather than a fully specified game. Define the construct in words, then give the formula, then say what a high or low value means empirically. A calibration measure, potential outcome, treatment contrast, or DID specification needs this same prose-to-notation-to-meaning sequence.

## Theorems And Propositions

Result captions are usually short. They name the result type or object, not the whole claim.

- Good: `Theorem 1 (Robust Performance of the FRfb Policy).`
- Good: `Proposition 2.`
- Risky: `Proposition 1: The Platform Should Reduce Disclosure Because Congestion Dominates Information Benefits.`

After a theorem or proposition, give the reader a sentence that explains what changed.

- For a structural result, say what the policy, threshold, or region looks like and why the condition matters.
- For a bound, say the metric, benchmark, rate, and parameter that drives the trade-off.
- For an empirical result, say what is estimated, what comparison identifies it, and what alternative explanation remains or is weakened.

Do not use `Key insight:` or `Proof idea:` as a default label. In full texts, proof sketches often appear as ordinary prose after the result or before the appendix pointer.

Theory papers also often make the proposition feel inevitable before the result statement. They introduce the relevant objective, constraint, or threshold, show the one equation that creates the comparison, and only then state the proposition. This is still main-text derivation, not appendix material, when the displayed equation defines the object the result characterizes.

## Proof Ideas In The Body

A body proof idea should earn trust, not decorate the theorem.

Use it when:

- the theorem would otherwise feel like a black box;
- the proof technique is part of the contribution;
- the condition in the theorem is unusual and the reader needs to see why it matters;
- the result is surprising relative to a benchmark.

The content should be concrete:

- constructed object: coupling, relaxation, dual, weighted policy iteration objective, sample path, upper bound, lower bound;
- hard term: queue length, Bellman error, incentive response, rejection probability, revenue loss, estimation error;
- move: decompose, bound, compare, apply, combine, condition, induct.

Full texts use three legitimate local conventions. A complete short proof can appear as `Proof.` below the result. A formal `Proof.` line can contain only an appendix pointer when the paper or venue uses that convention. A proof sketch can appear as ordinary prose with a cross-reference. The second convention records proof location; it does not supply proof logic or interpretation.

For a proposed new paragraph, the useful test is still whether it could stand as the proof if the appendix disappeared. If yes, a complete `Proof.` is appropriate. If no, write the reduction, bound, or comparison as ordinary prose unless the manuscript already uses a formal one-line pointer convention. In every case, keep the result's meaning in nearby body prose.

## Equations In The Body

Main-text displays do one job. They define the model, create the benchmark, state the result, or expose the key proof move.

- Make the display's role and consequential variables recoverable in nearby prose. A display may lead when the preceding passage has already made its role clear; avoid requiring identical framing around every equation.
- Keep a sequence of displays only when they form one object, such as a formulation with constraints or a short Bellman equation block.
- Move repeated algebra, constants, case splits, KKT verification, induction details, and concentration calculations to the appendix.

For derivations, show three levels in the body: starting object, load-bearing move, resulting object. The appendix fills in the algebra.

For empirical equations, make the sample, treatment or contrast, outcome, identifying comparison, and coefficient meaning available by the point the display is used as evidence. They may be established in prior prose, introduced immediately before the equation, or explained just after a compact specification when the design is already active.

For theory equations, main text usually contains the system definition, objective, benchmark, and one characterization equation. The appendix contains integration by parts, KKT verification, repeated casework, constants, and proofs of auxiliary lemmas.

## Appendix Shape

Appendices are dense but still guided.

- Use section titles that match proof dependencies or reviewer concerns, such as `Proof of Theorem 1`, `Auxiliary Lemmas`, `Additional Robustness Checks`, or `Details of the Estimation Procedure`.
- Start by fixing objects, assumptions, and notation used in the proof.
- State helper lemmas before they are used, and give each lemma a role.
- Long proofs can say `We first show`, `It remains to verify`, and `Combining the inequalities`, because the reader is following verification.
- End by mapping the final inequality, construction, or estimate back to the theorem or body claim.

The appendix verifies the body. It should not contain the first explanation of the model, theorem meaning, benchmark, or managerial conclusion.

Good appendices often start with an orienting sentence about the section's job before entering notation. Examples include defining the IC constraints used in the proof, giving the recursive representation that supports all propositions, or proving auxiliary lemmas before proposition proofs. The headings are plain and functional: `Proof of Proposition 1`, `Auxiliary Lemmas`, `Additional Robustness Checks`, `Data Construction`, or `Implementation Details`.

## Empirical And Experimental Result Prose

Empirical MS result sections usually earn trust in this order:

1. remind the reader of the outcome and treatment or comparison;
2. point to the table, figure, or design feature;
3. state sign, magnitude, and uncertainty at the right level;
4. translate the magnitude into the paper's metric;
5. separate interpretation from mechanism evidence;
6. handle alternatives, heterogeneity, spillovers, or robustness only when they answer a visible reviewer concern.

Use restrained phrases such as `I find evidence consistent with`, `the estimates suggest`, `the evidence points largely to`, and `although not conclusive` when the mechanism is not fully identified. If the result is a field experiment, distinguish the direct treatment effect from demand effects, spillovers, usage changes, learning, customer sorting, and selection.

When the design departs from ideal randomization, explain the operational constraint where the assignment is introduced. Do not wait until the conclusion to reveal a limitation that changes how the estimate should be read. In the conclusion, repeat the preferred magnitude and uncertainty only at the same scale and for the same outcome used in the results section.

## Theory And Model Prose

Theory prose is strongest when the formal object carries the story.

- Make the needed primitives available before relying on the equilibrium or optimization object. They may be defined in prior prose or immediately around the formulation.
- Place assumptions near the object they restrict, and say whether they rule out degeneracy, isolate a mechanism, preserve tractability, or match the setting.
- Create a comparison before a proposition only when the proposition is comparative. A definition, existence result, characterization, or impossibility result may have a different burden.
- Keep the interpretation needed to understand a proposition nearby. Use the benchmark, regime parameter, or condition only when it governs the result; interpretation may precede or follow a short proof or pointer.
- Use extensions to vary one economic object at a time: stochastic cost, seller information acquisition, joint information acquisition, imperfect protection, network constraints, or generalized price functions.

Avoid making the theory paragraph sound like suspense. The reader wants the object, condition, comparison, and implication.

## Native Word And Sentence Patterns

Useful plain patterns:

- `We study a ... system/problem/model in which ...`
- `We ask how ... can ... when ...`
- `We model ... as ...`
- `The objective is to ...`
- `The main challenge is ...`
- `This benchmark is useful because ...`
- `The result shows that ... under ...`
- `The proof uses ... to control ...`
- `The complete proof is in Appendix ...`
- `The estimates are consistent with ...`
- `These findings suggest ...`, only when the design does not fully identify the mechanism.

Use richer words only when the object supports them. Published papers may use `leverage`, `sheds light`, `crucial`, or `novel`, but those words sound native only when attached to a precise data source, mechanism, theorem, or decision. If the sentence still works after deleting the word, delete it.

## What To Avoid

- A fixed MS/OR outline imposed on every paper.
- A proposition title that reads like a conclusion sentence.
- `Proof.` followed by intuition in a manuscript where the label denotes a complete proof.
- A one-line formal proof pointer with no nearby interpretation of the result.
- Appendix pointers before the body states what the result means.
- Model paragraphs that open with `we propose a framework` before naming the decision.
- Contribution paragraphs that are only a list of `we first`, `we second`, `we third`.
- Punctuation-driven prose such as `Result:`, `Implication:`, or `Proof idea:`.
- "Story" language. Let coherence come from stable objects, analytical dependencies, evidence, comparison, and scope. Use setting, friction, mechanism, or implication only when the paper needs them.

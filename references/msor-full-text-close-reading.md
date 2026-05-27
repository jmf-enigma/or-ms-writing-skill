# MS/OR Full-Text Close Reading

Use this when prose still sounds strange after word-choice and sentence-craft passes, or when the user asks how MS/OR papers actually write the body, model, theorem, proof idea, or appendix. These notes come from reading full-text body sections and appendices, not only abstracts. They are style signals, not templates.

## Source Signals

Recent close-reading signals include full-text HTML or PDF versions of:

- Garcia, Tolvanen, and Wagner, "Demand Estimation Using Managerial Responses to Automated Price Recommendations," Management Science.
- Li, Belo, and Li, "Can Reward Uncertainty Encourage Social Referrals?", Management Science.
- Cowgill, Hernandez-Lagos, and Wright, "Does AI Cheapen Talk?", Management Science.
- Varma, Bumpensanti, Maguluri, and Wang, "Dynamic Pricing and Matching for Two-Sided Queues," Operations Research.
- Yan, Castro, Frazier, Ma, and Nazerzadeh, "Matching Queues, Flexibility, and Incentives," M&SOM.
- Bhandari and Russo, "Global Optimality Guarantees for Policy Gradient Methods," Operations Research / arXiv.
- Recent empirical Management Science papers with theoretical background, data, empirical strategy, primary results, and limitations sections.

Do not imitate any author's personal cadence. Extract field-level choices: where the sentence starts, how the model is introduced, how a result is interpreted, and where the proof is placed.

## What The Body Usually Does

Strong MS/OR body prose is plain but not flat. It gives the reader the next object at the moment the reader needs it.

- Introductions often begin with a concrete institutional or technical object, then show why the standard view, current practice, or existing model is insufficient.
- The turn is usually a real relation: a new technology changes signal cost, private information changes matching incentives, stochastic arrivals make pricing and matching inseparable, or a recommendation system creates useful quasi-experimental variation.
- The method enters only after the reader knows what it is for. `We model`, `we estimate`, or `we propose` should answer a question already visible in the paragraph.
- Result paragraphs keep the comparator and metric close: profit loss from the fluid benchmark, screening error relative to true expertise, throughput relative to random assignment, elasticity estimates relative to a preferred demand model.
- Boundaries are not apologies. They tell the reviewer what the claim is conditional on: a policy class, information structure, scaling regime, experiment, sample, or maintained behavioral assumption.

## Model Sections

Model sections usually climb from prose to notation.

1. Name the decision environment: who arrives, who chooses, who observes, and what the objective is.
2. Introduce the graph, state, signal, queue, price, policy, or belief only after its real-world object has been named.
3. State assumptions near the object they govern, then say what role the assumption plays if it could be questioned.
4. Define the objective or Bellman equation after actions and information are clear.
5. Add an example only when it helps the reader map the abstraction back to the setting.

Good model narration sounds like a careful researcher, not a notation manual. Instead of `We formulate a comprehensive framework`, write the local action: `The operator posts prices for each customer and server type and then chooses which compatible pair to match.`

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

If the proof is complete and short, use `Proof.` below the result. If it is only a sketch, write a normal paragraph and point to the appendix.

## Equations In The Body

Main-text displays do one job. They define the model, create the benchmark, state the result, or expose the key proof move.

- Before a display, say what the display defines or why it is needed.
- After a display, translate the important variables and tell the reader what the display will be used for.
- Keep a sequence of displays only when they form one object, such as a formulation with constraints or a short Bellman equation block.
- Move repeated algebra, constants, case splits, KKT verification, induction details, and concentration calculations to the appendix.

For derivations, show three levels in the body: starting object, load-bearing move, resulting object. The appendix fills in the algebra.

## Appendix Shape

Appendices are dense but still guided.

- Use section titles that match proof dependencies or reviewer concerns, such as `Proof of Theorem 1`, `Auxiliary Lemmas`, `Additional Robustness Checks`, or `Details of the Estimation Procedure`.
- Start by fixing objects, assumptions, and notation used in the proof.
- State helper lemmas before they are used, and give each lemma a role.
- Long proofs can say `We first show`, `It remains to verify`, and `Combining the inequalities`, because the reader is following verification.
- End by mapping the final inequality, construction, or estimate back to the theorem or body claim.

The appendix verifies the body. It should not contain the first explanation of the model, theorem meaning, benchmark, or managerial conclusion.

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
- `Proof.` followed by intuition only.
- Appendix pointers before the body states what the result means.
- Model paragraphs that open with `we propose a framework` before naming the decision.
- Contribution paragraphs that are only a list of `we first`, `we second`, `we third`.
- Punctuation-driven prose such as `Result:`, `Implication:`, or `Proof idea:`.
- "Story" language. Let the story come from the setting, friction, method, result, and boundary.

---
name: or-ms-writing
description: "Use for idiomatic, reviewer-calibrated OR/MS and adjacent academic writing at any granularity: sentence-level rewrites, phrases, titles, abstracts, paragraphs, introductions, contribution statements, related work, model/data/result narration, theorem intuition, proof exposition, managerial implications, referee responses, and full paper sections for Management Science, Operations Research, M&SOM, OM, econ, business analytics, mechanism, empirical, learning, and policy work; uses INFORMS genre patterns and Xiao Lei paper-pattern references without imitating a living author's personal style."
---

# OR/MS Paper Writing

Use this skill to produce stable, publication-style research prose at any useful granularity for Management Science, Operations Research, M&SOM, and adjacent OR/MS, econ, empirical, learning, policy, and business analytics papers. The task may be a phrase, sentence, title, abstract, paragraph, local section, proof explanation, referee response, or full paper section.

## Boundary

- Do not mimic a living scholar's personal wording or distinctive voice. Use field-level conventions and high-level paper architecture only.
- Do not hide missing logic in polished prose. If a theorem, proof, identification claim, or result is unsupported, mark the gap.
- Do not upgrade evidence while improving language. A rewrite may clarify, narrow, reorder, or make a claim more idiomatic, but it must not invent significance, dominance, optimality, robustness, causality, data, assumptions, or numerical magnitudes.
- For proof discovery or failed lemmas, route to `theory-proof-workbench`. For complete but rough proofs, pair with `math-proof-writing`.

## Operating Contract

Follow a lean skill style: keep the main skill as an operating guide, use references for paper-pattern detail, and use scripts only for diagnostics or planning.

- Draft the requested unit first. Do not expose the Writing Card, reference bundle, script labels, or checklist unless the user asks for diagnosis or planning.
- Load the smallest reference bundle that can solve the task. Default to one bundle; add another only when the request crosses language, story, math/proof, placement, or reviewer-calibration boundaries.
- Treat references as calibration, not templates. The final prose should be locally adapted to the user's model, data, theorem, notation, and evidence.
- If a script or reference conflicts with the user's supplied mathematics, evidence, notation, or journal constraints, preserve the user's content and narrow the wording.
- For long or technical requests, first decide the reader job, evidence support, and body-versus-appendix split; then write ordinary MS/OR prose rather than a visible plan.

## Writing Card

Before drafting, infer only the fields that matter for the requested unit:

- `target`: Management Science, Operations Research, M&SOM, working paper, referee response, or thesis.
- `section`: abstract, introduction, contribution, related work, model, main results, proof exposition, numerical/empirical section, managerial implications, discussion, conclusion.
- `unit`: phrase, sentence, title, bullet, paragraph, theorem intuition, model setup, result interpretation, table note, transition, referee response, or full section.
- `core claim`: one sentence that the paragraph or section must establish.
- `evidence`: model result, theorem, proposition, simulation, empirical estimate, mechanism, or example.
- `formal object` when relevant: decision variable, policy, equilibrium, estimator, algorithm, constraint, threshold, regime, bound, comparative static, or counterfactual.
- `result type` when relevant: descriptive pattern, causal estimate, structural estimate, theorem, characterization, comparative static, approximation guarantee, regret bound, simulation, or policy evaluation.
- `audience`: OR/MS theorist, OM/revenue-management reader, econ/mechanism-design reader, empirical reader, or manager/policymaker.
- `math level`: no equations, light notation, theorem statement, proof intuition, or full proof.
- `reviewer lens`: likely small-field reviewer and what they may not know, such as OM reading econometrics, empirical reader reading model, theory reader reading institutional details, or domain expert reading formal claims.
- `constraints`: length, tone, equations allowed, citations, journal style, whether to preserve existing wording.

If information is missing, make conservative assumptions internally. Mention assumptions after the draft only when they materially affect the wording, and use a plain sentence rather than a labeled note.

Use the Writing Card internally unless the user asks for diagnosis. For a phrase or sentence, do not force model, benchmark, or result-type fields that the sentence does not need. For a normal writing request, return the polished paragraph or section first. Do not prepend labels such as "Paragraph job" or "Assumptions."

## Granularity Rule

Do not assume the user wants a whole paper or even a whole section. Match the requested unit exactly.

- If the user asks for one sentence, return one sentence unless a brief alternative is clearly useful.
- If the user asks for wording, phrase choice, or "怎么说," give polished options and explain the difference only if it helps.
- If the user asks for a paragraph, make one paragraph do one job.
- If the user asks for a model, data, or result description, write the local passage in the correct section style instead of building a paper scaffold.
- If the user asks for a contribution, give contribution language that can be inserted into an introduction, not a generic outline.
- If the user asks for a referee response, write cautious response prose and separate promised revisions from completed changes.
- For local edits, preserve the surrounding claim, notation, and level of formality. Improve wording, logic, and reader order without inventing new results.

## OR/MS Disciplinary Spine

Use this spine as an internal feel for OR/MS prose, not as a visible checklist. It should make writing more precise and natural, not heavier. For short edits, apply only the relevant part. For model, result, proof, and implication passages, use it more strictly.

### Language

- Make decisions the grammatical center. Prefer "the platform chooses disclosure precision" over "disclosure precision is considered."
- Use OR/MS nouns when they clarify the formal claim: decision, policy, constraint, objective, benchmark, trade-off, regime, threshold, state, action, information, uncertainty, equilibrium, relaxation, bound, approximation, regret, counterfactual, feasibility, optimality.
- Use exact result verbs. "Characterizes" fits a policy form or equilibrium region. "Establishes" fits a theorem. "Bounds" fits approximation or regret. "Compares" fits a benchmark. "Quantifies" fits a magnitude. "Identifies" requires an empirical or structural source of variation.
- Prefer mechanism verbs over evaluation adjectives: increases, decreases, reverses, dampens, tightens, relaxes, screens, pools, rations, reallocates, accelerates, delays, amplifies, attenuates, improves, worsens.
- Do not let "framework," "approach," "method," or "model" carry the sentence by itself. Pair it with the decision, primitive, result, or mechanism it clarifies.

### Structure

- OR/MS sections usually move from problem to abstraction to result to decision consequence.
- The default long-form arc is operational setting, decision maker, friction, benchmark, model or design, result, mechanism, boundary condition, implication.
- A model section should earn abstraction before notation. Name what the abstraction preserves, why secondary details are omitted, and which benchmark makes the result interpretable.
- A result section should not start with intuition alone. State the formal result or local claim, then explain why it differs from the benchmark.
- A proof exposition should announce the proof idea before technical steps. Name the reduction, exchange argument, coupling, convexity, monotonicity, fixed point, concentration step, or induction structure.

### Naturalness

- Do not compress the whole OR/MS spine into one sentence unless the user asked for a summary sentence.
- Do not make every paragraph mention a benchmark. Add one when the result depends on a comparison or when the benchmark makes the contribution clear.
- Do not make prose sound like a planning card. Hide the scaffolding and let the sentence read as ordinary academic prose.
- If a sentence already has a clear actor, decision, and mechanism, do not add extra formal labels just to satisfy a checklist.

### Description

- Describe a model as a decision environment, not as a collection of symbols.
- Introduce primitives in this order when possible: agents, timing, state, information, actions, payoffs or costs, constraints, objective, benchmark, solution concept.
- Translate every important symbol once into an operational object.
- When describing data or experiments, separate what is observed, what is chosen, what is latent, and what is counterfactual.
- When describing an algorithm, state the optimization problem it approximates or solves, the information it uses, the benchmark it competes against, and the performance metric.

### Model Discipline

- Classify the model internally as normative, descriptive, structural, equilibrium, stochastic, dynamic, online, robust, data-driven, or behavioral.
- State whether the model predicts behavior, prescribes a policy, identifies a mechanism, estimates primitives, or evaluates a counterfactual.
- Tie each assumption to a role in the analysis. An assumption can simplify, identify, bound, preserve tractability, isolate a mechanism, or match institutional constraints.
- Name the benchmark near the result. Common benchmarks include first-best, myopic policy, static policy, oracle, fluid relaxation, LP relaxation, complete information, no information, current practice, or unconstrained optimum.
- For thresholds and regimes, state both the mathematical condition and the managerial interpretation.

### Mathematical Exposition

- Before a theorem, state the setup, assumptions, and object being characterized.
- In a theorem sentence, name the result type: existence, uniqueness, monotonicity, threshold structure, comparative static, approximation ratio, regret bound, convergence rate, welfare comparison, or identification result.
- After a theorem, give a one-paragraph interpretation that maps symbols to decisions and explains the force of the result.
- In proof sketches, avoid "by some algebra" unless the algebra is truly mechanical. Name the mathematical move: rearrangement, bounding, coupling, convexity, submodularity, martingale concentration, envelope argument, KKT conditions, fixed point, induction, or contradiction.
- Keep formal claims narrower than the theorem. If the theorem is under an assumption, benchmark, asymptotic regime, or information structure, keep that condition in the prose.

## MS/OR Paper Craft Core

Recent MS/OR papers write with compressed specificity. They do not sound grand. They name the decision environment, isolate the friction, state the method, and then move quickly to what is proven, estimated, or demonstrated.

- For abstracts, use the paper's actual sequence rather than a generic hook: setting, decision or canonical problem, friction, method, sharp result, validation or extension.
- For introductions, move from practical decision to modeling approach to specific technical gap. Do not keep the reader in broad motivation for long.
- For contribution paragraphs, group by contribution type. A good contribution sentence names the object, the guarantee or finding, and why the previous approach did not cover it.
- For related work, end each stream with the precise difference. The difference should be setting, information, constraint, performance criterion, proof technique, data source, or decision logic.
- For model sections, define the decision environment in prose before notation becomes dense. After assumptions, say what role they play or which standard examples satisfy them.
- For theorem/result sections, follow formal statements with a comment paragraph. Explain what the rate, bound, threshold, or structure says about the decision and implementation.
- For proof sketches, name the crux. Typical crux sentences identify the constructed policy, exchange/coupling argument, potential function, relaxation, reduction, or concentration step.
- For MS-leaning work, make the first half readable to a broad management scholar and the second half precise enough for the method expert.
- For OR-leaning work, make the formal object and performance criterion visible early, but still explain why the object matters operationally.
- When generalizing a canonical model, write "canonical object, new feature, new trade-off." This is often cleaner than starting from broad motivation.
- For algorithm papers, state what the algorithm uses, what benchmark it competes against, and what guarantee or empirical performance it achieves.
- For policy-structure papers, state the structure in words before decorating it with theorem language. A threshold, index, relaxation, decomposition, or competitive ratio should change how the reader understands the decision.
- End abstracts and result paragraphs with extension, validation, or implication only when it is substantive. Avoid a final sentence that merely announces "managerial insights."

## MS/OR Language And Model-Math Core

Use this core by default when polishing language, model narration, assumptions, results, proofs, or technical contributions.

- Make each verb govern the right object. Use "formulate" for a problem, objective, decision rule, or uncertainty set. Use "derive" for an expression, reformulation, or bound. Use "establish" for a theorem, guarantee, convergence rate, approximation ratio, or regret bound. Use "identify" for a condition, source of variation, policy class, structural property, or mechanism. Use "validate" for numerical, empirical, or out-of-sample evidence.
- Do not let formal adjectives float. Terms such as optimal, robust, tractable, adaptive, nonparametric, minimax, finite-sample, near-optimal, and data-driven need an object, benchmark, condition, or performance metric in the same sentence or the next one.
- Prefer sentence shapes that move from old object to new feature. Good technical prose often follows: canonical problem, new information or constraint, decision object, benchmark, result.
- In model paragraphs, introduce notation through the decision problem. First say who observes what and chooses what. Then define the random variable, decision rule, feasible set, objective, constraint, and benchmark.
- Around displays, use one sentence before and after. The sentence before tells the reader what the display does. The sentence after translates the central symbols and explains why this formulation is the right abstraction.
- Treat examples as part of mathematical exposition. For nonstandard definitions, give a simple example or counterexample that shows what the definition rules in or rules out.
- State assumptions with their analytic role. Say whether an assumption preserves conditional information, rules out degeneracy, gives tractability, identifies a parameter, bounds a value, or matches standard examples.
- For theorem interpretation, translate rates and constants into the decision environment. Say what changes when inventory grows, data are censored, demand shifts, action spaces expand, or the uncertainty set changes.
- In proofs, name the load-bearing move rather than narrating every algebraic step. Common moves include constructing an auxiliary solution, reducing the objective, coupling policies, applying convexity, deriving a dual, bounding a relaxation, and decomposing regret.

## Natural Rewrite Core

Use this core whenever the output should sound like a real MS/OR scholar rather than a checklist of MS/OR ingredients.

- Apply diagnostics invisibly. The final prose should not read as actor, decision, friction, benchmark, method, result, and implication packed into one sentence.
- For local rewrites, make the smallest change that fixes the claim, object, and rhythm. Do not recast the whole passage unless the logic is wrong.
- Add a benchmark, assumption role, managerial implication, or notation explanation only when it changes validity, contribution, or readability.
- Prefer two ordinary sentences over one over-complete sentence. A natural pair is often setup plus result, result plus mechanism, or formal claim plus interpretation.
- Keep one dominant job per sentence. If a sentence tries to define the setting, state the gap, introduce the model, and preview the result, split it.
- When prose feels translated, rebuild the English logic rather than polishing word by word. Put the decision object first, then the friction, then the evidence or result, then the condition.
- Avoid making every paragraph symmetrical. Real MS/OR prose varies sentence length according to logic. Dense formal sentences should be followed by shorter interpretation sentences.
- Preserve useful plain words. Do not replace "study," "show," "use," "price," "choose," or "bound" with more ornate verbs unless the technical object requires it.
- For micro-edits, return polished alternatives and a very short note only when helpful. Do not expose the full diagnostic scaffold.

## Anti-Mechanical Drafting Core

Use maps, scripts, and checklists as private prewriting. The final answer should not sound like a placement table unless the user explicitly asks for a plan, map, or diagnosis.

- Do not force every passage to mention actor, decision, friction, benchmark, theorem, mechanism, and implication. Include only the pieces needed for the passage's job.
- Do not turn every proof note into a body paragraph. The body needs the result, the object, the reason to trust it, and the interpretation. The appendix can carry the rest.
- Do not show `Writing Card`, `model ladder`, `proof-to-paper map`, `quality gate`, or script-style labels in polished prose unless the user asks for structure.
- If a user asks for a paragraph, give the paragraph first. Put any caveat after it only when a missing assumption, proof step, benchmark, or evidence type would change validity.
- If a user asks for正文和附录, first decide the split internally, then write a natural body passage and a complete appendix passage. Do not deliver only a meta-outline unless the user asks for one.
- Prefer one clean mathematical transition over many micro-signposts. A natural result paragraph often needs theorem statement, one interpretation sentence, and one benchmark or proof-idea sentence, not a full checklist.
- Treat story arcs, section blueprints, and diagnostic spines as flexible reader tests, not templates. Rearrange, omit, or compress beats when the paragraph's job, journal convention, or user's source material calls for it.

## Evidence Preservation Core

Use this core whenever revising, polishing, strengthening, or making text "sound like Management Science."

- Keep the evidence type fixed. Do not turn a simulation pattern into a theorem, a descriptive estimate into a causal effect, a model implication into an empirical finding, or an example into validation.
- Keep the comparison fixed. Do not add "outperforms," "dominates," "improves," "near-optimal," or "robust" unless the comparator, metric, and condition are present in the user's material.
- Keep magnitudes fixed. Do not add "substantial," "large," "significant," percentage improvements, rates, or orders unless they are supplied or can be read directly from the draft.
- Keep the policy class fixed. If a result holds for affine rules, a relaxation, a stationary policy, a finite horizon, or a specific sample regime, keep that qualifier near the claim.
- When the user asks for stronger writing with the same data or model, strengthen object, reader order, mechanism, and caveat. Do not strengthen the empirical or mathematical conclusion.
- If a needed support is missing, write the best supported version and add a short gap note only when the gap materially affects the claim.

## Argument-Evidence-Boundary Core

Use this core for abstracts, introductions, result narratives, model overviews, proof ideas, discussions, and major rewrites. It adapts the strongest useful kernel from Nature-style writing to OR/MS: write the argument before the sentences, keep claims near their evidence, and make the paper easy for a reviewer to judge.

- Reduce the passage internally to one chain: operational decision or field stake, unresolved friction or technical gap, proposed model/data/design, load-bearing evidence, decision consequence, and boundary condition.
- Every major claim needs a support type and a boundary. In OR/MS, support may be a theorem, proposition, proof idea, structural estimate, identification design, simulation, field experiment, numerical comparison, benchmark, or case evidence.
- Reason backward before writing forward. Start from what the paper actually proves, estimates, or demonstrates; then choose only the motivation and prior-work contrast needed to make that contribution legible.
- Use ambitious but bounded claims. A strong sentence names the object and contribution while keeping the assumption, benchmark, population, data regime, or policy class close enough to prevent overreading.
- For each paragraph, identify one message, the evidence or explanation supporting it, and its relation to the section thesis. Split a paragraph if it carries two messages.
- Draft from evidence outward. Put theorem statements, estimates, comparisons, or mechanisms near the claims they support instead of saving support for a later vague sentence.
- If claim, evidence, or boundary is missing, do not write around the gap. Produce the strongest supported version and flag the missing item only when it affects validity.
- For Chinese or mixed notes, translate intent rather than syntax: split long notes into claim, evidence, condition, comparison, implication, and limitation before drafting English in the section's natural order.

## Result Placement Core

Use this core whenever the user has results, theorem/proposition statements, simulations, robustness checks, empirical tables, extensions, or proof material and asks how to organize the paper.

- The main text must let a reviewer understand and evaluate the contribution without opening the appendix.
- Put headline results, main theorem statements, preferred empirical estimates, primary numerical comparisons, central figures, key assumptions, benchmarks, and result interpretations in the body.
- Put long proof details, routine algebra, auxiliary lemmas, repeated cases, extra robustness, alternative specifications, parameter sweeps, implementation details, data dictionaries, and replication materials in appendices or online supplements.
- Keep a proof idea in the body when the proof technique is part of the contribution or when the theorem would otherwise look like a black box.
- Keep a robustness check in the body when it protects the main identification, feasibility, or validity claim. Move repeated or secondary robustness checks to the appendix.
- For each result, decide placement by asking whether it is needed for first-pass understanding, reviewer trust, claim validity, or only verification and stress-testing.
- When reorganizing results, build a short placement map: result, evidence type, main-text role, appendix role, and cross-reference sentence.

## Model-Derivation And Proof Placement Core

Use this core whenever the user gives mathematical proof notes, derivations, model primitives, theorem logic, or asks what belongs in the body versus appendix.

- The body must establish the mathematical object, not merely point to the appendix. For a model, the body needs the decision environment, timing, information, action or policy class, objective, key constraints, assumptions, benchmark, and solution concept or estimand.
- The body should usually show a three-level derivation: the starting formal object, the load-bearing mathematical move, and the resulting object used by the theorem, estimator, policy, or comparison.
- Keep the displayed formulation, main theorem statement, result interpretation, and one proof idea or derivation checkpoint when they are needed for first-pass understanding or reviewer trust.
- Move routine verification to the appendix: algebra, constants, KKT checks, induction cases, concentration inequalities, auxiliary lemmas, repeated case splits, implementation details, and notation tables.
- A proof sketch in the body should name the constructed object, the hard term, and the mathematical move that controls it. It should not become a compressed full proof.
- For Management Science, proof-idea prose should be especially plain. Use proof verbs such as construct, decompose, bound, compare, apply, combine, show, and imply. Avoid stylish or metaphorical proof language.
- An appendix proof should verify the body, not carry the first explanation of the theorem's meaning. Start with fixed objects and assumptions, signpost long algebra, and map the final technical statement back to the body result.
- For focused technical Operations Research papers, do not hide proofs in an online EC. Keep essential proof material in the published paper and use a regular appendix for routine verification.

## Management Science Always-On Core

When the target is Management Science or the user asks for MS-level prose, use the following core by default. Do not wait to load a reference before applying it.

### Language

- When possible, write from the decision outward: actor, choice, friction, evidence, result, condition. For technical or theory-first papers, use the formal object as the entry point only after the reader can see why it matters.
- Prefer concrete management actors: firm, platform, seller, buyer, worker, manager, regulator, hospital, provider, customer, investor, borrower, algorithm, planner.
- Prefer MS evidence verbs with exact objects: study a decision, examine a mechanism, estimate an effect, identify a condition, characterize a policy, establish a bound, compare a benchmark, quantify a magnitude, validate a policy.
- Use mechanism verbs that carry causality: raises, reduces, shifts, reverses, disciplines, erodes, induces, attenuates, separates, amplifies, limits, screens, pools, displaces.
- Replace generic nouns with local metrics: profit, revenue, consumer surplus, welfare, adoption, reliance, adherence, match rate, purchase incidence, forecast error, regret, waiting time, overtime, lost demand, readmission, stockout risk, queue length.
- Let the story come from exact nouns and relations, not from story-like language. Prefer "the signal changes the first-stage sourcing decision" over "the model tells a compelling story about uncertainty."
- Avoid free-standing "important," "novel," "practical," "robust," "real-world," "framework," "insight," "performance," and "implication." Use them only when the same sentence names the metric, mechanism, or decision.

### Logic

- MS prose should make clear what the same data, model, experiment, or theorem changes about a management belief.
- A common diagnostic order is practice or decision, standard belief, hidden friction, method, result, mechanism, condition, and managerial or research consequence. This is a reader-order test, not a required sequence.
- A contribution should say what an audience learns, not only what the paper does. Put the core management insight before technical completeness.
- A result paragraph often moves from result to benchmark intuition to mechanism to condition to implication, but short results may need only the formal statement plus one interpretation sentence.
- A managerial implication should be conditional when it recommends action. Name who acts, what changes, when the action works, and why it can fail only when those details are supported by the paper.

### Model Narration

- Introduce the model only after the decision problem is clear unless the section is already technical.
- State the model in this order: agents, timing, information, controls, objective, constraints, benchmark, and the friction the abstraction isolates.
- Earn each abstraction. Say which real feature it keeps and which secondary detail it sets aside.
- Do not write "we consider a model" as the first meaningful sentence of an abstract or introduction. First name the decision and the friction.
- Translate every formal object once. For example, say what a fairness parameter, reference price, promotion value, state variable, or regret benchmark means operationally.
- When the model yields a threshold or regime, translate the threshold into an observable condition whenever possible.

### Data And Experiment Narration

- For field experiments, name the managerial practice being tested before describing randomization.
- For observational data, say what the data reveal, what they leave unidentified, and how the design or model bridges that gap.
- For human-algorithm papers, separate nominal algorithmic performance from realized performance after human adoption, override, delay, or strategic response.
- For data-driven operations, do not treat "data-driven" as a contribution. Say how the amount, relevance, granularity, timing, or censoring of data changes the decision.
- For behavioral experiments, distinguish behavior, belief, and performance. Explain which mechanism the design separates from which alternative explanation.

### Better Same-Model Writing

- Instead of "we develop a model," write what decision the model clarifies and what friction it isolates.
- Instead of "we use data," write what the data make visible and what remains latent.
- Instead of "we propose an algorithm," write what standard policy fails to learn, optimize, or implement.
- Instead of "we find significant effects," write which metric moves, for whom, and through what mechanism.
- Instead of "the result has managerial implications," write the action, condition, mechanism, and caveat.

## Reviewer Calibration Core

Assume the reviewer is a sharp expert in one nearby subfield, not an expert in every domain the paper touches. Write so that an OM reviewer can follow the econometrics, an empirical reviewer can follow the model, a theory reviewer can follow the institutional setting, and a domain reviewer can trust the formal language.

### Terminology Discipline

- Use field terms only in their field-accepted sense. If a term is overloaded across fields, define it locally before relying on it.
- Do not use a broader term when a narrower term is correct. For example, distinguish demand, arrival rate, purchase incidence, adoption, conversion, engagement, welfare, surplus, profit, and revenue.
- Do not use "causal," "optimal," "equilibrium," "robust," "identification," "efficiency," "fairness," "welfare," "learning," "platform," or "data-driven" loosely. Each must be backed by the correct design, model, definition, or benchmark.
- Keep notation and terminology aligned. If a model uses sellers and buyers, do not later switch to firms and consumers unless the mapping is explicit.
- Define the local meaning of new constructs such as fairness constraints, reference effects, algorithmic advice, strategic walk-ins, promotion value, leakage, or data relevance.

### Completeness For Cross-Field Reviewers

- Give the minimum setup needed before asking a reviewer to evaluate a result: actors, timing, information, decisions, objective, benchmark, and source of variation.
- When importing a method from another field, say what role it plays in this paper. Do not assume the reviewer knows why the method is appropriate.
- Explain what is observed and what is latent in empirical or data-driven work.
- Explain what is exogenous, endogenous, optimized, estimated, or assumed.
- For model paragraphs, state whether the result is a structural characterization, comparative static, equilibrium property, approximation, bound, or numerical finding.
- For empirical paragraphs, state whether the claim is descriptive, predictive, causal, structural, or counterfactual.

### Reviewer Misread Prevention

- Before finalizing, ask what a skeptical but fair reviewer could misunderstand.
- If a claim might sound stronger than the evidence, narrow it.
- If a term could trigger a different literature's definition, qualify it.
- If a result depends on an assumption, regime, or benchmark, state that dependency near the result.
- If the paper crosses domains, add one bridge sentence that maps the unfamiliar object into the reviewer's home vocabulary.
- Avoid novelty claims that invite easy objections. Prefer precise departure language: "we depart from this stream by..." or "this setting differs because..."

### Local Passage Test

Every local passage should be self-contained enough that a reviewer can answer three questions without searching elsewhere.

1. What object is being studied?
2. What is the claim and what evidence supports it?
3. Under what definition, assumption, benchmark, or empirical design is the claim valid?

## Academic Style And AI-Scent Core

Apply this core by default for every polished passage. It is drawn from public scientific writing guidance, academic writing skill guides, CARS-style introduction logic, and recent empirical work on LLM-associated academic vocabulary. Do not optimize for AI detectors. Optimize for reader comprehension, local substance, and field-correct wording.

### Reader Order

- Put old or contextual information before new information. Put the sentence's main emphasis at the end.
- Keep the grammatical subject close to its verb. Do not bury the action inside a long opening phrase.
- Make one sentence carry one main claim. Make one paragraph carry one main job.
- Start a paragraph with the local question, decision, tension, or claim. End it with the mechanism, condition, implication, or transition that the reader should remember.
- Keep related words together: actor with action, method with estimate, assumption with result, benchmark with comparison.
- Use signposting only when it changes the reader's expectation. Prefer "however," "therefore," "when," and "because" over ornamental transitions.

### Academic Claim Discipline

- Write clearly, concisely, and formally without making the prose ornate.
- Use active voice when the actor matters. Use passive voice only when the object, estimate, theorem, or institutional process should be foregrounded.
- Avoid empty metadiscourse such as "this paper aims to," "it is important to note," "the remainder of the paper," and "in conclusion" unless the venue requires it.
- Use hedging to match evidence, not to sound cautious. "Suggests" fits descriptive or correlational evidence, "estimates" fits an empirical design, "shows" fits a displayed result, and "establishes" fits a theorem or proof.
- Build introduction logic as territory, friction or niche, current paper, and findings. The gap must be a decision problem, empirical limitation, model limitation, or unresolved mechanism, not merely a missing citation.

### AI-Scent Resistance

- Recent studies find sharp post-ChatGPT increases in LLM-associated style words such as "delve," "underscore," "intricate," "pivotal," and "meticulous." Treat these as high-friction words. Use them only when they are the exact word, and never as a substitute for the local mechanism.
- Avoid formulaic AI rhythm: "rapidly evolving landscape," "multifaceted framework," "not only ... but also," "this underscores," "by leveraging," "comprehensive analysis," "valuable insights," and slogan-like final sentences.
- Do not stack abstract praise. Replace adjectives with observable objects, model primitives, estimates, regimes, or managerial actions.
- Do not create perfectly symmetric lists unless the argument truly has parallel parts. Vary sentence length according to logic, not decoration.
- Never use "humanizing" tricks that add errors or verbosity. The cure for AI-scent is substance: exact actors, decisions, assumptions, data features, model objects, estimates, mechanisms, and boundary conditions.
- Because AI detectors can be biased and unreliable, do not write to pass a detector. Write so a reviewer can verify the claim from the paper's evidence.

## Punctuation Discipline

Avoid punctuation that makes prose feel generated: colon-led roadmaps, semicolon chains, dash pivots, and repeated list-like sentence frames. For polished abstracts, introductions, related work, result interpretation, referee responses, and managerial implications, prefer periods, commas, parentheses, and direct because/when sentences.

Mathematical writing has more exceptions. Colons are acceptable in theorem titles, assumptions, definitions, proof labels, structured abstracts required by a venue, displayed-equation introductions, citation fields, tables, code, and appendix proof signposts. Semicolons can remain inside mathematical conditions, long theorem statements, or proof sentences when splitting would make the logic less clear. Do not remove useful formal punctuation merely to satisfy a style rule.

## References

- For topic-agnostic story structure across OR/MS, OM, econ, empirical, learning, and policy topics, read [references/general-topic-story-engine.md](references/general-topic-story-engine.md).
- For full paper and section structure, read [references/section-architecture.md](references/section-architecture.md).
- For paragraph-level wording, paragraph jobs, and flexible local structure, read [references/paragraph-style.md](references/paragraph-style.md).
- For plain-English storytelling, sentence rhythm, and anti-jargon checks, read [references/storytelling-language.md](references/storytelling-language.md).
- For the OR/MS disciplinary spine across language, structure, model description, and mathematical exposition, read [references/or-ms-disciplinary-spine.md](references/or-ms-disciplinary-spine.md), but apply the always-on spine above by default.
- For concrete MS/OR paper craft from full-text Management Science, Operations Research, and adjacent INFORMS papers, read [references/msor-paper-craft.md](references/msor-paper-craft.md).
- For precise MS/OR word choice, sentence rhythm, model notation, assumption roles, and theorem/proof narration, read [references/msor-language-model-math.md](references/msor-language-model-math.md).
- For Management Science-specific wording, comparable-data/model routing, and MS abstract/introduction rhythm, read [references/management-science-language-corpus.md](references/management-science-language-corpus.md).
- For Management Science verb-object pairings, sentence rhythm, clause-level discipline, abstract/result language, and Chinese-to-MS wording repair, read [references/management-science-language-rhythm.md](references/management-science-language-rhythm.md).
- For Management Science whole-paper storytelling, section-to-section continuity, native paragraph jobs, contribution logic, and complete manuscript arc, read [references/management-science-whole-paper-storycraft.md](references/management-science-whole-paper-storycraft.md).
- For deep Management Science lane calibration from at least 20 papers per lane, read [references/management-science-20x-lane-style.md](references/management-science-20x-lane-style.md) as background, but apply the always-on core above by default.
- For cross-field reviewer perspective, overloaded terminology, and claim narrowing, read [references/reviewer-calibration.md](references/reviewer-calibration.md).
- For academic style, reader-expectation prose, CARS logic, and AI-associated wording risks, read [references/academic-style-and-ai-writing.md](references/academic-style-and-ai-writing.md), but apply the always-on core above by default.
- For deciding whether results, proofs, robustness checks, extensions, figures, algorithms, or data/code details belong in the main text, appendix, or online supplement, read [references/main-text-appendix-placement.md](references/main-text-appendix-placement.md), but apply the Result Placement Core above by default.
- For deciding how much mathematical model setup, derivation, theorem explanation, proof sketch, and appendix proof detail belongs in the body versus appendix, read [references/math-model-main-appendix-craft.md](references/math-model-main-appendix-craft.md), but apply the Model-Derivation And Proof Placement Core above by default.
- For Management Science-specific model narration, body equation layout, proof-sketch displays, theorem surroundings, and appendix proof layout, read [references/management-science-model-proof-equation-layout.md](references/management-science-model-proof-equation-layout.md).
- For very idiomatic OR/MS language calibrated from a broader article corpus, read [references/expanded-or-ms-language-corpus.md](references/expanded-or-ms-language-corpus.md).
- For mathematical exposition, theorem statements, and proof writing, read [references/math-and-proof-style.md](references/math-and-proof-style.md).
- For high-level patterns drawn from Xiao Lei's public research profile and papers, read [references/xiao-lei-patterns.md](references/xiao-lei-patterns.md).
- For concrete paper-level style cards from multiple OR/MS/MSOM papers, read [references/article-corpus-style-notes.md](references/article-corpus-style-notes.md).

Use only the smallest bundle needed for the requested section. A short wording task should not load whole-paper architecture; a model/proof placement task should not rely only on paragraph style.

## Quick Reference Bundles

Use one bundle by default, then add only what the specific request makes necessary.

- **Native MS wording**: `management-science-language-rhythm.md` + `msor-language-model-math.md` for word choice, sentence rhythm, translated-English repair, technical verb-object fit, and same-model/same-data strengthening.
- **Whole-section story**: `management-science-whole-paper-storycraft.md` + `section-architecture.md` + `msor-paper-craft.md` for abstracts, introductions, contribution paragraphs, result-section flow, and full-paper arcs.
- **Model, theorem, equation, proof**: `management-science-model-proof-equation-layout.md` + `math-model-main-appendix-craft.md` + `math-and-proof-style.md` for model setup, formula placement, theorem surroundings, proof ideas, and appendix proof layout.
- **Body versus appendix**: `main-text-appendix-placement.md` + `math-model-main-appendix-craft.md`; run `plan_math_split.py` or `place_results.py` when the user gives rough proof notes or a list of results.
- **Reviewer calibration**: `reviewer-calibration.md` + the relevant model, empirical, or language bundle for cross-field papers, overloaded terminology, claim narrowing, and bridge sentences.
- **Paper-lane flavor**: `management-science-20x-lane-style.md` or `article-corpus-style-notes.md` only for difficult lane matching, complete sections, or when the user asks to imitate the feel of MS/OR papers without copying any personal voice.

## Reference Routing

- `phrase`, `sentence`, `title`, or `micro-rewrite`: use the Natural Rewrite Core, Management Science Always-On Core when relevant, and the Punctuation Discipline. Load `management-science-language-rhythm.md` when the target is MS or the user asks for native language, word choice, sentence rhythm, or Chinese-to-English repair. Load `msor-language-model-math.md` only when the phrase carries a model, theorem, assumption, proof, or technical contribution. Do not load full-section architecture unless the user asks for positioning or structure.
- `paragraph` or `rewrite`: load `paragraph-style.md` + `storytelling-language.md`; add `management-science-language-rhythm.md` when targeting MS or when language, sentence rhythm, or idiomatic wording is the main issue; add `msor-language-model-math.md` when the user asks for native, idiomatic, journal-like, less translated, model-aware, or mathematically precise prose; add `expanded-or-ms-language-corpus.md` for broader language calibration; add `general-topic-story-engine.md` if the prose feels generic or the topic is unfamiliar.
- `abstract`, `introduction`, `contribution`, `managerial`: load `general-topic-story-engine.md` + `section-architecture.md` + `storytelling-language.md` + `msor-paper-craft.md` + `msor-language-model-math.md`; add `management-science-whole-paper-storycraft.md` when targeting Management Science or when the user asks for story, native MS logic, or complete paper flow; add `expanded-or-ms-language-corpus.md` for native OR/MS language and `article-corpus-style-notes.md` for paper-level flavor.
- `related work`: load `section-architecture.md` + `paragraph-style.md`; use `citation-tools` when citations or exact publication fields matter.
- `model`, `model setup`, `formulation`, `mathematical model`, `derivation`, `推导`, `数学模型`, or `模型建立`: load `section-architecture.md` + `math-model-main-appendix-craft.md` + `math-and-proof-style.md` + `msor-paper-craft.md` + `msor-language-model-math.md`; add `management-science-model-proof-equation-layout.md` when the target is MS or the user asks how formulas should appear in the body. Build the model ladder and derivation-depth map before drafting.
- `results`, `theorem`, `proposition`, or `main result`: load `math-and-proof-style.md` + `math-model-main-appendix-craft.md` + `msor-paper-craft.md` + `msor-language-model-math.md`; add `management-science-model-proof-equation-layout.md` when theorem displays, body formulas, proof sketches, or appendix placement matter; add `storytelling-language.md` and `expanded-or-ms-language-corpus.md` for interpretation paragraphs.
- `proof-exposition`, `proof process`, `proof sketch`, `proof idea`, `proof notes`, `证明过程`, `appendix proof`, `正文和附录`, `formula layout`, `equation layout`, `公式`, or `式子`: load `math-model-main-appendix-craft.md` + `management-science-model-proof-equation-layout.md` + `math-and-proof-style.md` + `msor-paper-craft.md` + `msor-language-model-math.md`; add `management-science-language-corpus.md` when the target is Management Science; run `scripts/plan_math_split.py` when the user provides rough proof/model notes; pair with `math-proof-writing` if the proof already exists, or `theory-proof-workbench` if the proof is missing.
- `result placement`, `appendix`, `online appendix`, `e-companion`, `robustness placement`, or `paper organization after results`: apply the Result Placement Core and Model-Derivation And Proof Placement Core; load `main-text-appendix-placement.md` + `math-model-main-appendix-craft.md` + `section-architecture.md` + `math-and-proof-style.md`; add `reviewer-calibration.md` for cross-field or empirical/theory papers. If the user provides a list of completed results, tables, proofs, extensions, or checks, run `scripts/place_results.py` first to build a draft placement map.
- OR/MS disciplinary fit, model narration, theorem/result language, mathematical intuition, policy characterization, approximation/regret bounds, or stronger OR/MS flavor: apply the OR/MS Disciplinary Spine first; load `or-ms-disciplinary-spine.md` for longer sections or difficult local diagnosis.
- MS/OR abstract, introduction, result paragraph, model overview, algorithm contribution, policy-structure claim, or "make it sound like real MS/OR papers": apply the MS/OR Paper Craft Core; load `msor-paper-craft.md` when the prose still feels generic or mechanically checklisted.
- Native academic polish, AI-scent concerns, "make it less ChatGPT," reviewer-readable flow, introduction gap logic, translated-English repair, or a request to learn writing style: apply the Natural Rewrite Core and Academic Style And AI-Scent Core first; load `academic-style-and-ai-writing.md` for difficult diagnosis or longer drafting.
- Management Science target, "MS" wording, or a request to write better from the same data/model: apply the Management Science Always-On Core first; load `management-science-language-corpus.md`; load `management-science-language-rhythm.md` for language, sentence rhythm, verb choice, result wording, or translated-English repair; load `management-science-whole-paper-storycraft.md` for full sections, complete manuscript flow, introduction logic, story structure, or native MS paragraph rhythm; load `management-science-20x-lane-style.md` only for difficult lane matching or longer section drafting.
- Cross-field, interdisciplinary, empirical plus model, algorithm plus field data, policy plus theory, or reviewer-facing text: apply the Reviewer Calibration Core before polishing. Define overloaded terms, narrow claims to evidence, and add a bridge sentence when needed.
- Xiao Lei / digital platform / pricing / social operations flavor: load `general-topic-story-engine.md` first, then `xiao-lei-patterns.md` + `storytelling-language.md` + `expanded-or-ms-language-corpus.md` + `article-corpus-style-notes.md`.

## Stable Output Procedure

1. Build a one-line Writing Card and choose the smallest reference bundle that fits the requested unit.
2. Select the section blueprint only when the task is section-level or structurally unclear; if useful, run:

```bash
python3 /Users/mingfeijiang/.codex/skills/or-ms-writing/scripts/plan_section.py --section SECTION --target TARGET --topic "TOPIC"
```

For a result-placement task with a list of items, run:

```bash
python3 /Users/mingfeijiang/.codex/skills/or-ms-writing/scripts/place_results.py --target TARGET --paper-type "regular" < results.txt
```

For a proof-process, derivation, model-to-appendix, or main-text-versus-appendix task with rough notes, run:

```bash
python3 /Users/mingfeijiang/.codex/skills/or-ms-writing/scripts/plan_math_split.py --target TARGET --paper-type "regular" < proof_notes.txt
```

3. Draft the requested unit only. Keep it precise, low-flourish, contribution-driven, and locally insertable. Do not expose planning labels unless the user asks for them.
4. For model, result, and proof material, decide the mathematical split before drafting: body object, formal result, derivation checkpoint when needed, interpretation, proof idea, and appendix verification.
5. For model passages, establish agents, timing, information, actions, objective, constraints, assumptions, benchmark, and solution concept in prose before or alongside notation.
6. For derivations, show only the start point, key mathematical move, and resulting object in the body unless the proof technique itself is the contribution. Send routine algebra, constants, cases, KKT verification, and auxiliary lemmas to the appendix.
7. Apply the evidence-preservation and reviewer-calibration passes: keep evidence type, comparison, magnitude, policy class, assumption, benchmark, and validity condition no stronger than the user's material supports.
8. Apply the argument-evidence-boundary pass: check that each major claim has nearby support and an explicit enough boundary; split paragraphs whose topic sentence, evidence, or section role cannot be mapped cleanly.
9. Apply the naturalness and language passes: make each paragraph do one job, use old-to-new reader order, bind technical verbs to precise objects, earn notation before displays, and translate formal rates or structures into the decision environment.
10. Remove checklist residue, AI-scent filler, generic "This enables" sentences, over-parallel lists, and punctuation that creates colon-led or dash-led roadmaps. Preserve formal punctuation when it improves theorem, proof, or appendix clarity.
11. Finish with a short quality check when revising existing text: claim clarity, contribution signal, logical order, evidence support, overclaiming, notation, placement, and audience fit. For a mechanical check, run:

```bash
python3 /Users/mingfeijiang/.codex/skills/or-ms-writing/scripts/check_paragraph.py --fail-on-ai-scent < draft.txt
```

## Quality Gate

Before finalizing, make sure the output passes:

- **Story**: in substantive sections, the relevant actor, decision, friction, method, result, or consequence is visible without forcing all of them into every passage.
- **Logic**: the first sentence sets the paragraph's job; the last sentence teaches, qualifies, or transitions when the passage needs that move.
- **Evidence**: every claim is backed by a theorem, model, estimate, simulation, example, or citation.
- **Boundary**: major claims keep the relevant assumption, benchmark, population, data regime, policy class, or scope condition close enough to prevent overreading.
- **Evidence preservation**: rewrites do not add significance, dominance, causality, optimality, robustness, generality, or magnitude not supplied by the user's material.
- **Placement**: headline results, key assumptions, primary evidence, and interpretation are in the body; verification, long proofs, repeated robustness, implementation details, and replication materials are in appendices or supplements.
- **Derivation depth**: the body shows the start point, key mathematical move, and resulting object; the appendix carries algebra, constants, cases, KKT verification, auxiliary lemmas, and implementation details.
- **Specificity**: replace generic "important/novel/managerial implications" with the actual decision and condition.
- **OR/MS fit**: substantive model, result, and implication passages make the decision, formal object, benchmark, mechanism, and boundary condition clear when those pieces are needed.
- **MS fit**: when targeting Management Science, state what the same data/model changes about management theory, practice, or decision logic.
- **Model fit**: agents, timing, information, actions, objective, constraints, assumptions, benchmark, and solution concept are clear when a model is described.
- **Math fit**: theorem, proposition, approximation, regret, comparative-static, or equilibrium claims state the relevant assumptions and translate the formal object into words.
- **Language and model-math fit**: technical verbs govern the right objects, formal adjectives carry benchmarks or conditions, displays are introduced and interpreted, and assumptions state their analytic role.
- **Naturalness**: the prose does not expose the checklist. Long sentences are split, translated-English order is rebuilt, and unnecessary benchmarks or implications are left out.
- **Reviewer fit**: a small-field reviewer can identify the object, claim, evidence, benchmark, and validity conditions without importing the wrong definition from another literature.
- **Academic style**: sentences follow old-to-new order, important information lands at the end, claims are calibrated to evidence, and introduction gaps are substantive rather than citation-shaped.
- **Rhythm**: split long noun-heavy sentences; preserve technical precision without hiding the point.
- **No AI scent**: polished prose contains no LLM-associated filler words, dash pivot, template transition, over-symmetric list, colon-led roadmap, semicolon chain, or slogan-like summary unless formal mathematical writing needs it.
- **Reader order**: topic sentence first, one topic per paragraph, concrete actors before abstractions, and evidence before implication.
- **Word discipline**: prefer active voice, specific verbs, positive form, and concrete language; delete puffery, filler, weak intensifiers, and empty "-ing" phrases.

## Output Modes

- `micro-rewrite`: one to three polished alternatives for a phrase or sentence; keep explanations short.
- `paragraph`: one polished paragraph only; do not prepend a job label.
- `section`: multi-paragraph section with headings if appropriate.
- `local-insert`: a self-contained passage that can be pasted into a model, data, result, contribution, or implication section.
- `rewrite`: preserve content while improving OR/MS clarity and flow.
- `logic-map`: outline before prose; useful for introductions and result sections.
- `proof-exposition`: theorem/proposition statement plus readable proof narrative.
- `math-main-appendix-plan`: map model primitives, theorem statements, derivation checkpoints, proof ideas, appendix proofs, robustness checks, and cross-references before writing.
- `proof-to-paper-map`: table that converts rough proof/model notes into body skeleton, appendix skeleton, gap notes, and cross-reference language before drafting prose.
- `referee-ready`: crisp, cautious wording suitable for revision or response.
- `reviewer-calibrated`: prose that defines overloaded terms, narrows claims to evidence, and bridges fields for expert reviewers outside the paper's secondary domain.
- `result-placement-map`: table or bullet map deciding which results, proofs, robustness checks, extensions, figures, tables, and data/code details belong in the body, appendix, or online supplement.

## Default Style

Prefer analytical calm over rhetorical force. Use concrete claims, mechanism language, and conditional implications. Avoid generic praise, vague novelty claims, unsupported managerial advice, exposed checklists, and punctuation tricks that make prose feel generated. Use ordinary sentences. Keep formal punctuation when it improves theorem, proof, definition, or appendix clarity.

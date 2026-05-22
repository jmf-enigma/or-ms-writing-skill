# MS/OR Full-Text Paper Craft

Use this reference when a passage still sounds generic after applying the core OR/MS spine. These notes are not sentence templates. They are field-level writing moves distilled from full-text Management Science, Operations Research, and adjacent INFORMS papers across revenue management, learning algorithms, empirical pricing, human-AI field experiments, stochastic search, robust optimization, and OR/MS-AI integration.

## Corpus Used For This Update

- A primal-dual CMDP paper with queue scheduling and inventory applications.
- A high-dimensional dynamic pricing paper with nonstationarity and change-point detection.
- A static-calendar dynamic pricing and assortment paper.
- An empirical demand estimation paper using managerial responses to algorithmic price recommendations.
- A human-centered AI field experiment in Management Science.
- A Pandora's box paper with sequential inspections.
- An Operations Research robust ranking paper.
- An INFORMS Journal on Data Science paper on AI and OR/MS integration.
- An assortment optimization paper with replacement options and stockout risk.
- A causal transport DRO paper for decision making with side information.
- A multitier inventory network paper with a stochastic-program lower bound, partner data, expediting, and disruptions.
- A Bayes-adaptive POMDP paper for threatened-species management that reformulates an intractable dynamic program.
- A dynamic-programming healthcare paper on genetic testing policies with threshold structure and an online appendix.
- An online retail allocation paper that keeps definitions and main theorems in the body while moving most proofs to appendices.
- A privacy-management equilibrium paper that analyzes a baseline model in the body, places a more general model in the appendix, and sends missing proofs to the online appendix.
- A coproductive principal-agent paper that layers first-best, second-best, and contract benchmarks before welfare and managerial interpretation.
- An energy-market mechanism paper that states theorem regions in the body, visualizes them, then uses observations and simulations to interpret market-design consequences.
- A location and repairable-inventory paper for EV battery swapping that combines a model, algorithmic treatment, data files, and online appendices.

## What Full Text Adds Beyond Abstracts

- Abstracts compress the contract, but the body teaches the order of persuasion. Full texts move from decision environment to modeling or identification obstacle, then to the exact object the paper constructs.
- Introductions do not stay in broad motivation. They quickly name the canonical problem, the practical limitation, the technical gap, and the paper's object.
- Model sections earn notation. They first identify agents, timing, information, actions, objective, and benchmark in words, then introduce symbols.
- Assumptions are not decorative. Strong papers explain whether an assumption gives identification, tractability, a benchmark, a standard special case, or a practical approximation.
- Result sections use a two-step rhythm. State the theorem or proposition precisely, then interpret what the bound, rate, threshold, approximation ratio, or policy structure means for the decision.
- Proof sketches name the crux. They say whether the proof constructs a policy, couples sample paths, relaxes the problem, bounds a value function, decomposes the objective, or applies concentration.
- Empirical sections make the institutional fact do work. They show how a real workflow generates identifying variation, then defend why the variation is plausibly unrelated to the unobserved demand or outcome shock.
- Model-heavy papers often use examples as mathematical exposition. A toy example, platform screenshot, or feature-based newsvendor instance is not decoration. It explains why the formal object captures a real operational feature.
- Strong technical papers interpret formulations. They say what the outer decision rule chooses, what the inner adversary changes, what an uncertainty set preserves, and why a relaxation is a valid benchmark.
- Applied OM papers often keep the base model parsimonious in the body, then move partner-specific estimation, extra scenarios, and calibration details to appendices. The body says which real features the abstraction keeps and why that is enough for the main result.
- Theory papers with baseline and general models often analyze the baseline in the body and put the general model in an appendix. This is acceptable only when the body explains why the baseline carries the main mechanism and how the general model changes or preserves it.
- Papers with many theorem variants often state the theorem, give a comment or observation, and then move proof details to the online appendix. The body still names the hard step or stronger result when reviewer trust depends on it.
- Reviewer persuasion is usually built into the order of exposition. Strong papers do not append caveats only at the end; they introduce the trust device before the claim: a randomization, institutional delay, equilibrium condition, local-improvement argument, construct validation, matching design, approximation guarantee, or placebo logic.

## Section Moves

Before selecting a section order, classify the paper's lane: empirical experiment, archival/DID or construct-measurement empirical work, structural/ML/RM, theory/mechanism, theory/algorithm, or applied OR with field data. Headings should name manuscript objects, not the writer's diagnostic checklist. A Management Science field experiment and an Operations Research algorithm paper do not need the same body architecture.

### Abstract

Good MS/OR abstracts usually draw from these moves; the evidence lane determines emphasis:

- Canonical setting or managerial decision.
- New friction, information structure, constraint, data feature, or generalization.
- Method or formal object.
- Sharp result, guarantee, estimate, or characterization.
- Validation, numerical evidence, application, or conditional implication.

Do not start with a broad claim about importance when a precise decision is available. A better opening names the operational object, such as a firm pricing under nonstationary demand, a retailer planning a static calendar, a hotel manager responding to recommendations, or a decision maker inspecting alternatives at different costs.

### Introduction

Strong introductions draw from these modules. Their order depends on the lane and on the reviewer's next question:

- Define the decision environment in plain operational language.
- State the standard model, policy, belief, or literature default when the contrast matters.
- Explain the practical or technical feature that breaks the default.
- Name the trust device: the model feature, institutional variation, algorithmic guarantee, experiment, or construct validation that can answer the friction.
- State the paper's formal object, method, or empirical design after the reader understands the question it answers.
- Group contributions by type rather than chronology.
- Close each literature stream with the exact departure.

Contribution sentences should include object plus result plus difficulty. For example, the sentence should make clear that the paper develops an algorithm and proves a regret rate, constructs a relaxation and obtains an approximation guarantee, or uses behavioral delay in recommendations to identify demand.

### Related Work

Related work should not be a citation inventory. Each stream needs three pieces:

- What the stream studies.
- Why that stream is close.
- The exact difference in this paper.

The difference should be substantive. Use setting, information structure, constraints, performance criterion, proof technique, data source, decision timing, or behavioral mechanism. Avoid vague difference language such as "our paper is related but different."

### Model And Problem Formulation

Before notation becomes dense, give the reader a complete prose version of the decision problem:

- Who acts.
- What arrives over time.
- What is observed before the decision.
- What action is chosen.
- What uncertainty remains.
- What payoff, cost, revenue, welfare, regret, or constraint is optimized.
- What benchmark makes performance interpretable.

After formalizing, translate each central symbol once. If the model has a threshold, index, relaxation, Lagrangian multiplier, confidence set, change point, or latent demand shock, say what it means operationally.

Model narration should make the abstraction earn reviewer trust. Say which real feature is retained because it drives the result, which feature is simplified for tractability, and which concern is deferred to robustness, calibration, or an appendix extension.

For applied model papers, explicitly separate three layers:

- **Base model**: the smallest formal environment that carries the main mechanism.
- **Operational adaptation**: partner data, demand estimation, lead-time modeling, calibration, or implementation changes.
- **Stress tests**: extra scenarios, robustness checks, sensitivity, or alternative policies.

The base model usually belongs in the body. Operational adaptations belong in the body only when they change the main result or the reader's trust in implementation. Stress tests usually belong in the appendix or online supplement after the body reports the primary pattern.

### Theorem And Result Narration

The theorem is not the whole result paragraph. After a formal statement, add a comment paragraph that answers:

- What is being characterized or bounded.
- What benchmark the result is relative to.
- Which condition matters.
- Why the result differs from the standard intuition.
- What decision rule or implementation guidance follows.

Use precise result verbs. "Characterizes" fits a policy form, threshold, equilibrium region, or structural property. "Establishes" fits a theorem. "Bounds" fits regret, approximation, or optimality gaps. "Identifies" fits an empirical source of variation or a formal identification result.

When a theorem defines regions, thresholds, or cases, the body should not stop at the display. It should say what the regions mean, which uncertainty or parameter moves the decision across regions, and which benchmark each region favors. Figures can help only after the prose tells the reader what comparison the figure encodes.

### Proof Exposition

A good proof overview does not say that the proof follows from algebra. It names the mathematical move:

- Construct a policy or auxiliary instance.
- Couple two sample paths or information states.
- Relax a dynamic program to an LP or upper bound.
- Use primal-dual or Lagrangian structure.
- Decompose the regret or objective into interpretable terms.
- Apply concentration, induction, convexity, monotonicity, or exchange arguments.

When the proof is long, tell the reader where the hard step lives. Then map the end of the proof back to the theorem's decision object.

If the body states that a stronger result yields the displayed theorem, keep the stronger result or its definition in the body when it is conceptually useful. Move the proof to the appendix, but do not hide the reason the stronger result is introduced.

### Empirical And Data Sections

Empirical MS writing is strongest when the institutional detail carries identification. Use these modules, usually after the setting has made the decision process concrete:

- Decision process and data source.
- Observed action, latent object, and outcome.
- Institutional behavior that creates variation.
- Estimation equation or design.
- Identification assumption and why the setting supports it.
- Validation, robustness, or sensitivity.
- Interpretation of magnitudes for the decision.

Do not call a design causal unless the variation, assumptions, and threats are named. If power or external validity is limited, state that limitation near the result rather than burying it.

Strong empirical MS prose often treats validation as part of the story. After defining a text-derived, platform-derived, or model-derived measure, show why the measure is credible before using it as the main regressor or outcome. After reporting a main estimate, state the nearest alternative explanation and the check that addresses it.

### Numerical And Application Sections

Numerical evidence should connect to the theorem's promise. State what the numerical study tests:

- Approximation quality.
- Robustness to misspecification.
- Scalability or runtime.
- Performance relative to a benchmark policy.
- Value of a model feature such as nonstationarity, replacement options, or partial inspections.

Then report the pattern in decision terms rather than only percentage improvement.

For industry-partner or field-data applications, write the section in two passes. First, explain how the real system maps onto the base model. Second, report the primary comparison using the partner's current policy or standard heuristic as the benchmark. Put decensoring procedures, distribution fitting, extra scenarios, and long parameter tables in the appendix unless they are needed to evaluate the headline comparison.

## MS Versus OR Feel

- Management Science prose usually keeps the managerial or empirical object visible even when the paper is technical. It explains what the same model, data, or algorithm changes about a management belief or decision.
- Operations Research prose tolerates denser formal development, but it still names the formal object, benchmark, and performance criterion early.
- Revenue management papers often use a canonical problem plus operational constraint pattern. The writing makes the business constraint a modeling reason, not just motivation.
- Learning and algorithm papers introduce regret, benchmark, and information structure early. They state what the algorithm observes and which oracle or optimum it competes against.
- Empirical algorithm or human-AI papers separate tool capability from realized use. They distinguish the algorithm's technical performance from human adoption, workflow disruption, delays, overrides, or incentives.
- Robust optimization and data-driven decision papers state the information structure before the uncertainty set. The uncertainty set should not appear as a mathematical object detached from what the decision maker observes.
- Assortment and platform papers make customer choice operational before writing the choice model. Preferred option, replacement option, stockout risk, fulfillment, and revenue are introduced before the optimization problem.
- Healthcare and conservation papers often need one extra bridge sentence before the dynamic program. The bridge maps domain concepts, such as genetic risk, survey effort, protection effort, or species occupancy, into state, action, reward, and information.
- Energy-market and mechanism-design papers should make the market rule or contract benchmark visible before equilibrium conditions. Readers need to know what institutional rule is being compared before they can interpret regions or welfare rankings.

## Phrase-Level Tendencies To Learn

These are patterns to adapt, not copy.

- "We study [canonical problem] under [new information, constraint, or behavioral feature]."
- "The key challenge is that [standard method] cannot handle [specific obstacle]."
- "This setting differs from [stream] because [decision timing, information, constraint, or benchmark]."
- "Our analysis shows that [policy structure or bound] holds under [condition], relative to [benchmark]."
- "The result suggests [decision consequence] when [observable condition]."
- "The proof constructs [auxiliary object] and compares it with [benchmark or relaxation]."
- "The empirical strategy leverages [institutional behavior] to isolate [variation]."

Do not overuse these surfaces. The real skill is to preserve their logic while writing ordinary, local sentences.

## Use The Craft Without Sounding Mechanical

The paper-level moves above are a diagnostic sequence, not a surface template. A short passage should use only the move that its local job requires.

- In an abstract, all major moves should appear, but not necessarily with equal weight. The paper's sharpest contribution should get the cleanest sentence.
- In an introduction paragraph, do not include method, result, implication, and literature positioning unless the paragraph is designed to bridge into contributions.
- In a model paragraph, resist adding managerial advice. The job is often to make timing, information, controls, objective, and benchmark intelligible.
- In a result paragraph, do not repeat the full motivation. State the condition, formal claim, benchmark intuition, and decision meaning.
- In a proof paragraph, do not re-explain the application unless the proof move depends on an operational feature.
- When revising a sentence, ask what would make a reviewer trust the claim. Often the answer is a sharper object or condition, not a longer sentence.

## Reviewer Guardrails

- A reviewer in one small field may not know the secondary field. Define overloaded terms such as optimal, causal, robust, welfare, fairness, platform, learning, identification, and regret in the paper's local meaning.
- If the paper crosses theory and empirical work, say whether a claim is a theorem, a simulation finding, a reduced-form estimate, a structural counterfactual, or a managerial interpretation.
- If a model generalizes a canonical object, name both the canonical object and the new feature. Then say which old result no longer applies or which old proof breaks.
- Keep claims narrower than results. If the result depends on stationarity, sparsity, independence, a relaxation, an oracle benchmark, a small number of clusters, or an approximation regime, put that condition near the claim.
- A strong paragraph should let the reviewer answer: What is the object, what is the claim, what supports it, and under what condition is it valid?

# Management Science Whole-Paper Storycraft

Use this when the user asks for a full paper section, a complete manuscript arc, Management Science storytelling, native MS language, or a draft that should work from abstract through model, results, proof, and appendix. These are field-level patterns distilled from Management Science papers. Do not copy source sentences or imitate an author's personal voice.

## Core Reading

This file extends the MS corpus with additional whole-paper readings across field experiments, analytical models, empirical finance, algorithmic design, platform experiments, and reproducibility/meta-science:

- Li, Belo, and Li, "Can Reward Uncertainty Encourage Social Referrals? Evidence from a Large-Scale Field Experiment," Management Science, 2026.
- Brahm, Lafortune, Magelssen, and Tessada, "Collaboration, Workplace Practice Adoption, and Performance: Evidence from a Field Experiment," Management Science, 2026.
- Gu, Bapna, Chan, and Gupta, "Measuring the Impact of Crowdsourcing Features on Mobile App User Engagement and Retention," Management Science, 2022.
- Frick, Belo, and Telang, "Incentive Misalignments in Programmatic Advertising: Evidence from a Randomized Field Experiment," Management Science, 2023.
- Cui, Demirer, Jaffe, Musolff, Peng, and Salz, "The Effects of Generative AI on High-Skilled Work," Management Science, 2026.
- Orzach and Quist, "Managerial Intervention, Employee Motivation, and Collaboration," Management Science, 2026.
- Li, Liu, and Wei, "Credit Rating Purchases and S&P 500 Index Membership Decisions," Management Science, 2026.
- Levi, Paulson, and Perakis, "Designing Inclusive Offerings," Management Science, 2025.
- Hardwicke et al., "Reproducibility in Management Science," Management Science, 2023.
- Guo, "The Mnemonomics of Contractual Screening," Management Science, 2022.
- Kasy and Abebe, "Learning to Be Fair: A Consequentialist Approach to Equitable Decision Making," Management Science, 2024.
- DeValve and Myles, "Approximation Algorithms for Dynamic Inventory Management on Networks," Management Science, 2024.
- Federgruen, Liu, and Lu, "Sourcing with Demand Updates," Management Science, 2026.
- Feng, Li, and Shanthikumar, "Transfer Learning, Cross Learning and Co-Learning with Operational Data Analytics," Management Science, 2026.
- Manshadi, Rodilitz, Saban, and Suresh, "Redesigning VolunteerMatch's Search Algorithm," Management Science, 2025.
- Bapna, Ramaprasad, Shmueli, and Umyarov, "One-Way Mirrors in Online Dating," Management Science, 2016.
- Bird and Frug, "A Theory of Front-Line Management," Management Science, 2025.
- Greiner, Grunwald, Lindner, Lintner, and Wiernsperger, "Incentives, Framing, and Reliance on Algorithmic Advice," Management Science, 2025.
- Garcia, Tolvanen, and Wagner, "Demand Estimation Using Managerial Responses to Automated Price Recommendations," Management Science, 2022.
- Chen, van der Lans, and Trusov, "Efficient Estimation of Network Games of Incomplete Information," Management Science, 2021.
- Han, Chu, Sun, and Wu, "Commercializing the Package Flow," Management Science, 2025.
- "Collaborative Work Management Technologies and Managerial Intensity in U.S. Corporations," Management Science, 2026.
- Guasoni, Huberman, and Shikhelman, "Lightning Network Economics: Topology," Management Science, 2024.

## The MS Story Is Argument Architecture

MS storytelling is not flourish and not a sequence of required beats. It is the architecture by which a broad management audience can recover what the paper establishes, what supports that claim, how its objects relate, and where it stops applying.

A manuscript may need some of the following burdens:

- establish a practice, institution, decision, formal object, or received belief;
- expose a friction, counterexample, identification obstacle, or computational limit;
- define the experiment, model, estimator, algorithm, or benchmark used to study it;
- establish the main formal or empirical result;
- explain a mechanism, decomposition, or comparison;
- delimit the result by regime, population, policy class, or implementation condition;
- interpret the contribution for practice, theory, policy, or method.

These are an inventory, not an arc. A theorem paper may open with a counterexample or formal object. An empirical paper may open with an institution or an unexplained pattern. An implementation paper may need the operating workflow before the model. Some papers do not need a mechanism claim, managerial recommendation, or dramatic friction at all.

The stable requirement is dependency: later claims must have the definitions, comparisons, evidence, and boundaries they need. A local paragraph may only define notation, state a theorem, document a design choice, report a check, or connect two literatures.

## Story Logic Within And Across Paragraphs

Story logic includes several different problems that should not be collapsed into "flow."

1. **Referential logic**: the reader can track the paper's nouns, symbols, labels, and pronouns.
2. **Prerequisite logic**: definitions, assumptions, timing, comparators, and design facts appear before later claims depend on them.
3. **Inferential logic**: the theorem, estimate, comparison, citation, or proof move warrants the stated inference.
4. **Scope logic**: metric, population, policy class, evidence type, and boundary remain stable or change explicitly.
5. **Attention logic**: paragraph and section order gives the spine result more emphasis than supporting verification.

When diagnosing a paragraph, record only what is useful: its primary burden, active object, warrant, scope, and relation to adjacent passages. A forward handoff is optional. A paragraph may end by completing a definition or reporting a result, and the next heading or opening sentence may supply the transition.

Relations between passages include definition, elaboration, evidence, inference, contrast, mechanism, condition, consequence, decomposition, generalization, and change of evidence type. The reader does not need an explicit rhetorical question before every move. The relation only needs to be recoverable.

Common sequences remain useful as examples. A friction can motivate a method; a result can activate a mechanism test; a theorem can create the need for a benchmark; a design limitation can motivate a follow-up experiment. The reverse orders can also be legitimate when context is already active or when a result-first opening gives the right emphasis.

If the draft feels illogical, reverse-outline each paragraph by burden and warrant. Reorder only when the existing order uses an object before defining it, draws an inference before its support is available, hides the main result, repeats the same burden, or changes scope without notice.

## Recent MS Persuasion Patterns

Recent full-text MS papers reinforce that storytelling is reviewer persuasion, not decoration. Across the relevant passages, the paper turns a broad topic into a reviewable object and makes the source of credibility visible; the order and amount of setup vary by lane.

- **Human-AI and algorithmic-advice papers** separate tool quality from human reliance. They introduce the managerial decision, the behavioral friction, the experimental manipulation, and then interpret reliance, performance, incentives, or framing as distinct outcomes.
- **Revenue management and empirical pricing papers** move from the canonical pricing problem to an identification obstacle. They explain why ordinary demand estimation is hard, then show how an institutional behavior, such as delayed responses to recommendations, creates usable variation.
- **Structural model papers** state both obstacles early: computation and identification. The model section then reads as an answer to those obstacles, not as notation for its own sake.
- **Platform and field-experiment papers** make the intervention operational before the estimating equation. The design, matching, balance, and robustness checks are narrated as reasons a reviewer can trust the comparison.
- **Organization and strategy papers** often start with two competing mechanisms. The empirical design is persuasive because the chosen setting is expected to activate one mechanism more than the other.
- **Theory and network papers** use examples, local-improvement arguments, and algorithms to move the reader from a real constraint to a formal result. The theorem is followed by the intuition, complexity implication, or algorithmic consequence.

Across these lanes, by the time the introduction asks the reader to accept the findings, it usually has made three things legible: the focal object, the departure from the relevant benchmark or evidence, and the source of credibility. These need not occupy separate paragraphs or appear in that order.

## Close-Reading Story Paths

Recent full-text papers show that the right order follows analytical dependencies and active reviewer concerns, not a universal section skeleton.

- **Field experiment and algorithmic-advice papers** first separate the tool from the human decision around it. The story often moves from a broad belief about AI or decision aids, to a behavioral or organizational friction, to the manipulated design, to the main effect, and then to usage, qualitative evidence, learning, or sensitivity analyses that explain why the effect has that sign. The estimating equation appears after randomization, treatment, outcome, and unit of analysis are already clear.
- **Platform and data-capability experiments** often use a primary experiment to establish the effect, then use mechanism sections to rule out nearby explanations. The mechanism paragraph starts with the threat or alternative channel, introduces the finer-grained data or interaction, and ends by saying what that check does and does not establish.
- **Multimethod behavioral operations papers** give each method a distinct evidential role. A field study may establish effect size and external relevance, an analytical benchmark may define normative behavior, and an experiment may separate competing explanations. The relation need not be remedial: a later method can replicate, triangulate, decompose, validate, or extend an earlier result. Coherence comes from making that relation explicit, not from forcing each method to answer a rhetorical question left by the previous one.
- **Analytical platform and supply-chain papers** build the story around a comparison. The model gives the actors, timing, information, and objective; a proposition characterizes equilibrium; the interpretation explains the regions or strategic channels; the next theorem compares equilibrium with a benchmark or design alternative. The body often repeats `recall Proposition 1` only when the previous result is the object being compared.
- **Optimal control, learning, and applied OR papers** often proceed from formulation to approximation to guarantee to structure. The approximation is introduced only after the optimal object is shown to be costly or intractable. A performance-bound theorem earns computational credibility; structural theorems then interpret policy regions, stopping rules, or sample paths. Numerical examples usually enter after the theorem has told the reader what they should verify.
- **Technical theory papers** sometimes place a short complete proof in the body, but more often keep the result and needed interpretation in the body and send verification to an appendix or online companion. Before asking the reader to leave the main text, make the theorem's object, relation, and scope clear; a benchmark is needed only for a comparative result.

Use these paths as a diagnostic. If a draft says `we next conduct a robustness test`, identify the claim or threat the test bears on. If a model appears after descriptive results, identify whether it explains, measures, extrapolates, or merely restates them. If a proof or formula appears in the body, ask whether it supplies a definition, warrant, comparison, or interpretation needed on the first pass, or only routine verification.

## Elegance As Recoverable Movement

Recent MS papers that read well do not simply list problem, method, result, and implication. They make it clear why an object appears at that point and what changes once it is introduced.

- A platform-algorithm paper can move from the platform's original efficiency objective to the distributional harm that objective creates, and then to a ranking redesign that preserves total connections while changing access.
- A workplace field-experiment paper can move from the general puzzle of slow practice adoption to the specific collaboration failure between managers and workers, and then to an intervention that separates coordination from cooperation.
- A limited-data ODA paper can move from transfer learning and pooling as natural statistical defaults to the decision problem those defaults fail to protect, and then to co-learning as a decision-aligned alternative.
- A technical inventory paper can move from known single-product guarantees to the unresolved backlog-assignment problem in networks, and then to a lower-bound construction that makes a simple policy provably credible.

This is one kind of movement to learn at the field level, not a required plot. The paragraph should not sound dramatic; it should make the relation between objects easy to recover without announcing the relation as a writing device.

Useful relations include:

- **Old object -> missing feature**: what the standard model, policy, or literature assumes away.
- **Objective -> unintended consequence**: what the current algorithm, contract, or practice optimizes and what it distorts.
- **Method default -> decision mismatch**: why a familiar statistical or optimization tool is not enough for this decision.
- **Formal result -> operating condition**: when the theorem, estimate, or algorithm matters and when a simpler benchmark is enough.
- **Mechanism -> alternative mechanism**: why the result is attributed to one channel rather than a nearby explanation.
- **Definition -> use**: what a newly defined construct, state, or policy class lets the paper state precisely.
- **Evidence -> claim**: which estimate, theorem, comparison, or design fact warrants the inference.
- **Whole -> decomposition**: which components account for an aggregate result and which do not.
- **Claim -> qualification**: where the population, policy class, regime, or evidence type narrows the conclusion.

Use a contrastive relation only when the paper contains a real contrast. A definition, procedural step, replication, or direct result can advance the argument without a missing-feature or reversal narrative.

Do not overuse contrast markers. A single well-placed `but`, `whereas`, `when`, `because`, or `relative to` can do more than a paragraph of polished transitions.

## Do Not Overfit The Story

Different MS papers earn trust in different ways. Choose the entry point that matches the evidence, not the most complete-looking arc.

- **Technical algorithm papers** may start with the operational system and a known unsolved structural issue, then move quickly into policy class, lower bound, upper bound, guarantee, and numerical performance. The story is not "practice first, implication last" so much as "why the old structure breaks, what replacement object restores tractability, and what guarantee follows."
- **Applied stochastic-model papers** often start with a familiar operational problem and a new information timing. They may then alternate between model generalization, analytic characterization, heuristic, calibration, and benchmark comparison. The implication is conditional on observable regimes rather than a universal managerial rule.
- **ODA, learning, and data papers** can begin from a statistical or decision-theoretic limitation. The key story is what data can and cannot transfer across systems, and why decision quality depends on the relationship between data structure and decision structure.
- **Platform algorithm papers** often combine partner context, equity or welfare objective, theoretical algorithm, field implementation, and scale-up implication. Here the algorithm is not merely a method; it is also the intervention.
- **Behavioral field experiments** can start from a platform feature or interface affordance, then explain the competing mechanisms and identify which mechanism dominates. Results may be narrated as behavior, outcome, mechanism, subgroup, and quality rather than as a single headline effect.
- **Short theory papers** may have a compressed abstract and no long empirical-style story. Their native rhythm is received view, missing incentive or information channel, model, characterization, and conceptual implication.

The writer should therefore ask what makes the paper's main claim credible. It may be randomization, a theorem, an approximation guarantee, a calibrated model, a field implementation, a construct definition, or a decomposition. The section order should make that source of credibility legible.

## First-Page Logic

The first page has limited attention. Choose the burdens needed to make the paper's main claim legible.

- identify the focal decision, formal object, institution, or empirical pattern;
- establish the relevant benchmark, received view, or unresolved comparison;
- show the obstacle, counterexample, missing evidence, or new feature when one motivates the paper;
- state the question, contribution object, or headline claim at the point where the reader can interpret it;
- make the source of credibility visible before asking the reader to accept a strong conclusion.

No single order is required. A technical paper may begin with a counterexample, an impossibility, or a canonical formulation. A field paper may begin with an institution or treatment. A direct research question can appear early when its objects are already clear; it need not wait for a manufactured friction paragraph.

Field-experiment papers can begin with a broad managerial puzzle, but they quickly define the treated practice, the decision maker, the outcome metric, and the missing causal evidence. Theory papers can begin with a known theoretical view, but they quickly introduce the new strategic complementarity, information loss, fairness definition, or design constraint.

A method-first opening is weak only when the reader cannot tell what the method studies, why that object matters, or what limitation it addresses. If the model, estimator, or algorithm is itself the portable contribution, introduce it early and make its object and departure explicit.

For technical papers, a first page can legitimately use examples, figures, or a small network before the main theorem. In that case the example is not decoration; it explains the state variable, policy class, or operational ambiguity that makes the theorem necessary.

## Paragraph Jobs In The Introduction

Use these as internal jobs, not visible labels.

- **Practice paragraph**: who chooses what, in what organization or market, with what stakes.
- **Belief paragraph**: what the literature, firm, platform, or regulator would normally expect.
- **Friction paragraph**: why that belief may fail in this setting.
- **Question paragraph**: the precise question once its objects and comparison are interpretable.
- **Design paragraph**: data, experiment, model, or algorithm, with just enough detail to identify the causal or formal object.
- **Findings paragraph**: make the headline effect and its support legible; place mechanism, heterogeneity, or boundary before or after it according to the local evidential dependency.
- **Contribution paragraph**: what each audience learns that it could not learn from prior work.

If a paragraph tries to perform all seven jobs, it is probably overloaded. Split when the burdens compete, but allow linked work such as result plus interpretation or definition plus role. The burden can be expository, empirical, theoretical, or connective; it does not always need a friction or immediate implication.

## Methods Enter When Their Role Is Legible

Across MS field-experiment and empirical papers, the method becomes persuasive once the reader knows what comparison or inferential problem it addresses. This explanation may precede the method, appear in the same paragraph, or follow a concise method-first statement when prior context already supplies it.

Common modules:

- The empirical setting or partner organization.
- The decision or treatment being varied.
- The randomization, quasi-experimental variation, or identification contrast.
- The outcome metric.
- Which comparison, estimand, mechanism, or validity concern the design addresses, if that role is not already clear.

Avoid a methods paragraph that is only a sample-size announcement. Sample size matters when it identifies scale, power, external relevance, or operational realism.

## Result Narration

MS result narration usually uses these ingredients, but the paragraph's local job decides how much to include and in what order:

- State the headline effect, theorem, estimate, or algorithmic guarantee.
- Translate the result into the decision metric.
- Compare with the benchmark, common intuition, or prior result.
- Explain the mechanism or decomposition.
- Give the boundary condition or heterogeneity that prevents overclaiming.

For experiments, separate effect, mechanism, heterogeneity, and downstream quality when all are part of the claim. For theory, separate formal result, interpretation, and implication when the result would otherwise be opaque. For algorithms, separate guarantee, comparator, and empirical or operational validation when the paper has all three.

When a paper has several result types, do not force them into one paragraph. A theorem result can need a proof-idea sentence; a numerical result can need a benchmark sentence; an empirical result can need an identification sentence. The prose should switch register as the evidence type changes.

## Mechanism Language

MS mechanism prose is specific. It rarely says only "we provide insight."

Useful mechanism subjects:

- treatment effect, behavioral asymmetry, targeting strategy, contract incentive, baseline probability, incremental effect, collaboration, coordination, cooperation, psychological cost, fairness perception, information disclosure, strategic complementarity, discretion, suitability, inclusivity, reproducibility obstacle.

Useful mechanism verbs:

- increases, reduces, concentrates, attenuates, amplifies, shifts, separates, mitigates, induces, discourages, complements, substitutes for, explains, accounts for, reconciles, makes visible.

Mechanism sentence shape:

- `This effect is driven by [specific behavioral or mathematical channel], not by [nearby but incorrect channel].`
- `The comparison separates [baseline object] from [incremental object], which matters because [contract, policy, or algorithm] optimizes the former rather than the latter.`
- `The result is concentrated among [units/regime], consistent with [mechanism], and muted when [boundary condition] makes that mechanism weak.`

## Contributions

MS contribution paragraphs are strongest when organized around what changes for the reader, not around the order of tasks the authors performed.

Common contribution modules:

- Core management insight or causal/formal object.
- Mechanism or decomposition that explains the insight.
- Methodological or design contribution if it is reusable.
- Practical implication, bounded by observable conditions.

Avoid making the first contribution "we are the first." If novelty matters, attach it to the object: first causal evidence on a decision, first formal definition of a construct, first model that separates two mechanisms, first algorithm with a particular guarantee for a management setting.

## Related Work

A native MS related-work paragraph makes two things recoverable: what the cited stream establishes and the exact dimension on which the current paper relates to or departs from it. A stream-first paragraph can synthesize prior work before positioning the paper. A paper-first paragraph can state the paper's object and then identify the nearest streams. Choose the order that avoids citation-by-citation listing and keeps each citation attached to the claim it supports.

When a related-work paragraph positions the paper, replace "our paper is different" with the exact relation: treatment assignment, reward side, information structure, targeting space, decision timing, policy class, formal definition, data access, or performance metric. The paragraph may end elsewhere if its primary burden is synthesis rather than positioning.

## Model And Theory Sections

Theory papers often start from a standard setup and add one new feature. When that is the paper's departure, the prose should show both parts.

- Make the standard setup and new feature distinguishable; either may appear first when the local context makes the comparison clear.
- Explain why the new feature changes the managerial or economic logic.
- Define the base model before extensions.
- Use "base model" only when the base model carries the main mechanism.
- State simplifications honestly and say where generalizations appear.
- Keep enough interpretation near a proposition for the reader to understand its object, comparison, or regime. A complete short proof may follow immediately when that is the manuscript's convention; interpretation may precede or follow it according to what the reader needs to understand first.

For formal definitions, explain what the definition rules in and rules out when that distinction is consequential. For new measures, make the construct and analytical role legible before or immediately after the formula; the formula may come first when the notation itself is the cleanest definition.

For MS model writing, the model is persuasive when the reader can see how the abstraction supports the paper's claim. A live reviewer concern can organize that explanation:

- If the concern is **tractability**, explain which state, action, or equilibrium object creates the difficulty and which reformulation controls it.
- If the concern is **identification**, explain what is observed, what is latent, and which institutional feature or excluded variation supports the estimand.
- If the concern is **external validity**, explain which institutional details are retained in the base model and which are stress-tested later.
- If the concern is **behavioral interpretation**, separate the model's mechanical prediction from the behavioral mechanism that the data can test.
- If the concern is **implementation**, say what the algorithm, policy, or estimator takes as input, what it outputs, and what benchmark makes its performance meaningful.

Do not let the model section become only a list of primitives. A local definition paragraph can be brief or enumerative, but the surrounding prose should make clear why the consequential primitives are the right abstraction for the claim.

## Empirical And Field-Experiment Sections

MS empirical sections feel grounded because they keep the institution and outcome metric visible.

- Make the relevant setting, unit, treatment or variation, and outcome recoverable before asking the reader to interpret the estimating equation. They may be established in prior paragraphs rather than repeated immediately before the display.
- Say what is randomized or otherwise shifted, and what remains observational.
- Make the business metric interpretable before asking the reader to interpret a coefficient in that metric.
- Interpret heterogeneity as a boundary condition, not as a list of extra tables.
- Put treatment implementation, survey instruments, long balance tables, and secondary checks in the appendix after the body gives enough information to trust the design.

Do not let "causal evidence" float. State the causal contrast and the metric: treatment versus control, policy versus benchmark, ads versus public service announcements, uncertain sender reward versus certain sender reward, or collaboration treatment versus pure control.

For reviewer persuasion, audit each consequential empirical object against the live threat it must bear. Do not manufacture one threat per paragraph:

- Measurement: show how the construct is observed, validated, and bounded.
- Treatment or adoption: explain timing and why it is plausibly separated from the outcome shock.
- Matching or weighting: report balance and common support before interpreting estimates.
- DID or event study: name the counterfactual group and the timing assumption.
- Structural estimation: state what identifies the latent object and how model fit or external variation supports it.
- Robustness: summarize the conclusion in the body and place the repeated checks in the appendix.

## Abstract Rhythm

MS abstracts are dense but not ornamental.

Common successful modules, not a required sentence template:

- Practice or decision.
- Missing friction, definition, or evidence.
- Research design or model.
- Headline result in the management metric.
- Mechanism, heterogeneity, or boundary.
- Implication.

The sharpest result should get the cleanest sentence. Avoid ending with generic "valuable insights"; end with the action, design condition, or belief that changes.

## Sentence Rhythm

Native MS prose often uses ordinary sentence pairs.

- Setup then contrast: `Prior work emphasizes [standard channel]. In our setting, [missing friction] changes the decision because [reason].`
- Design then identification: `We use [setting/design] to compare [policy/treatment] with [benchmark]. This design isolates [mechanism] from [confound or adjacent channel].`
- Result then interpretation: `We find [effect/result]. The result implies [decision consequence] when [condition].`
- Mechanism then boundary: `[Mechanism] explains the main effect. The effect weakens when [observable condition] limits that mechanism.`

Avoid over-polished symmetry. MS sentences can be plain and uneven when the logic requires it.

## Language Discipline

Prefer:

- "standard view," "prior work," "existing evidence," "common practice," "published methodology," and "baseline model" when contrasting with a known object.
- "we examine," "we test," "we estimate," "we model," "we formulate," "we characterize," "we establish," and "we apply" with exact objects.
- "this effect is driven by," "this pattern is consistent with," "this comparison separates," and "this result suggests" when the claim is supported but not overgeneral.

Distrust:

- "complex dynamics," "novel insights," "sheds light," "robust framework," "significant implications," and "real-world impact" unless immediately tied to a decision, metric, or mechanism.
- "first empirical evidence" without the object and context.
- "managerial implications" without a named manager, action, and condition.

## Whole-Paper Continuity

Use the manuscript contract rather than a fill-in-the-blank story sentence. Record the central object, belief change, comparator, metric, evidence owner, and boundary in plain notes. A mechanism belongs in this record only if the paper actually establishes one.

Different sections transform the same contract differently. The abstract compresses it; the introduction makes the object and departure legible; the model or design defines what the claim means; the results supply support; the conclusion interprets the supported claim. Related work and appendices have their own burdens and need not restate the whole contract.

Continuity does not require repeated wording. It requires stable objects and explicit relations. Use the canonical term after definition, signal any change in comparator or evidence type, and do not let the conclusion become a stronger paper than the results.

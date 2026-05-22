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

## The MS Story Is A Flexible Reader Path

MS storytelling is not flourish. It is the reader path by which a broad management audience comes to trust a precise claim. Use the path as a diagnostic map, not as a fixed outline.

Common beats:

1. Existing practice, institution, decision, or belief.
2. Hidden friction that makes the standard belief incomplete.
3. Design object that isolates the friction: experiment, model, estimator, algorithm, or optimization problem.
4. Main evidence in the decision metric.
5. Mechanism that explains why the evidence has that sign.
6. Boundary condition, heterogeneity, benchmark, or regime.
7. Implication for management practice, theory, policy, or method.

The beats can be reordered, compressed, repeated, or omitted depending on the paper type. A field experiment may foreground the institution before theory. A theory paper may start from a standard model before the managerial setting. A methods paper may need the formal object early. The important test is whether the reader can recover the decision, friction, evidence, mechanism, and boundary where they matter.

The path should be visible across the manuscript, not crammed into every sentence. A local paragraph usually performs only one or two of these jobs, and some paragraphs only define notation, report a robustness check, or bridge literatures.

## Recent MS Persuasion Patterns

Recent full-text MS papers reinforce that storytelling is reviewer persuasion, not decoration. The paper first turns a broad topic into a reviewable object, then makes the trust device visible.

- **Human-AI and algorithmic-advice papers** separate tool quality from human reliance. They introduce the managerial decision, the behavioral friction, the experimental manipulation, and then interpret reliance, performance, incentives, or framing as distinct outcomes.
- **Revenue management and empirical pricing papers** move from the canonical pricing problem to an identification obstacle. They explain why ordinary demand estimation is hard, then show how an institutional behavior, such as delayed responses to recommendations, creates usable variation.
- **Structural model papers** state both obstacles early: computation and identification. The model section then reads as an answer to those obstacles, not as notation for its own sake.
- **Platform and field-experiment papers** make the intervention operational before the estimating equation. The design, matching, balance, and robustness checks are narrated as reasons a reviewer can trust the comparison.
- **Organization and strategy papers** often start with two competing mechanisms. The empirical design is persuasive because the chosen setting is expected to activate one mechanism more than the other.
- **Theory and network papers** use examples, local-improvement arguments, and algorithms to move the reader from a real constraint to a formal result. The theorem is followed by the intuition, complexity implication, or algorithmic consequence.

Across these lanes, the introduction usually answers three reviewer questions before listing results: why this setting matters, why the standard view or method is insufficient, and what feature of the model, data, or design makes the claim credible.

## Do Not Overfit The Story

Different MS papers earn trust in different ways. Choose the entry point that matches the evidence, not the most complete-looking arc.

- **Technical algorithm papers** may start with the operational system and a known unsolved structural issue, then move quickly into policy class, lower bound, upper bound, guarantee, and numerical performance. The story is not "practice first, implication last" so much as "why the old structure breaks, what replacement object restores tractability, and what guarantee follows."
- **Applied stochastic-model papers** often start with a familiar operational problem and a new information timing. They may then alternate between model generalization, analytic characterization, heuristic, calibration, and benchmark comparison. The implication is conditional on observable regimes rather than a universal managerial rule.
- **ODA, learning, and data papers** can begin from a statistical or decision-theoretic limitation. The key story is what data can and cannot transfer across systems, and why decision quality depends on the relationship between data structure and decision structure.
- **Platform algorithm papers** often combine partner context, equity or welfare objective, theoretical algorithm, field implementation, and scale-up implication. Here the algorithm is not merely a method; it is also the intervention.
- **Behavioral field experiments** can start from a platform feature or interface affordance, then explain the competing mechanisms and identify which mechanism dominates. Results may be narrated as behavior, outcome, mechanism, subgroup, and quality rather than as a single headline effect.
- **Short theory papers** may have a compressed abstract and no long empirical-style story. Their native rhythm is received view, missing incentive or information channel, model, characterization, and conceptual implication.

The writer should therefore ask: What is the paper's trust device? It may be randomization, a theorem, an approximation guarantee, a calibrated model, a field implementation, a construct definition, or a decomposition. The section order should make that trust device legible.

## First-Page Logic

Strong MS introductions often spend the first page doing some version of four things.

- Establish that the decision already matters in practice or theory.
- Name the standard explanation, policy, or modeling approach.
- Show why that standard view misses a friction in the focal setting.
- State the paper's question only after the friction is concrete.

Field-experiment papers can begin with a broad managerial puzzle, but they quickly define the treated practice, the decision maker, the outcome metric, and the missing causal evidence. Theory papers can begin with a known theoretical view, but they quickly introduce the new strategic complementarity, information loss, fairness definition, or design constraint.

Avoid beginning a full MS introduction with "We develop a model" when the reader does not yet know the decision or friction. If the model itself is the contribution, introduce the canonical object and the new feature before the full application story.

For technical papers, a first page can legitimately use examples, figures, or a small network before the main theorem. In that case the example is not decoration; it explains the state variable, policy class, or operational ambiguity that makes the theorem necessary.

## Paragraph Jobs In The Introduction

Use these as internal jobs, not visible labels.

- **Practice paragraph**: who chooses what, in what organization or market, with what stakes.
- **Belief paragraph**: what the literature, firm, platform, or regulator would normally expect.
- **Friction paragraph**: why that belief may fail in this setting.
- **Question paragraph**: the precise question after the friction is established.
- **Design paragraph**: data, experiment, model, or algorithm, with just enough detail to identify the causal or formal object.
- **Findings paragraph**: headline effect first, then mechanism, heterogeneity, or boundary.
- **Contribution paragraph**: what each audience learns that it could not learn from prior work.

If a paragraph tries to perform all seven jobs, split it. MS prose often sounds native because each paragraph has a narrow job. The job can be expository, empirical, theoretical, or connective; it does not always need an immediate implication.

## Methods Enter After The Tension

Across MS field-experiment and empirical papers, the method paragraph usually comes after the paper has explained why the managerial question is not already answered.

Common order:

1. The empirical setting or partner organization.
2. The decision or treatment being varied.
3. The randomization, quasi-experimental variation, or identification contrast.
4. The outcome metric.
5. Why the design addresses the earlier friction.

Avoid a methods paragraph that is only a sample-size announcement. Sample size matters when it identifies scale, power, external relevance, or operational realism.

## Result Narration

MS result narration often follows this sequence, but the paragraph's local job decides how much to include:

1. State the headline effect, theorem, estimate, or algorithmic guarantee.
2. Translate the result into the decision metric.
3. Compare with the benchmark, common intuition, or prior result.
4. Explain the mechanism or decomposition.
5. Give the boundary condition or heterogeneity that prevents overclaiming.

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

Common contribution order:

1. Core management insight or causal/formal object.
2. Mechanism or decomposition that explains the insight.
3. Methodological or design contribution if it is reusable.
4. Practical implication, bounded by observable conditions.

Avoid making the first contribution "we are the first." If novelty matters, attach it to the object: first causal evidence on a decision, first formal definition of a construct, first model that separates two mechanisms, first algorithm with a particular guarantee for a management setting.

## Related Work

A native MS related-work paragraph usually has this structure:

1. What the stream studies.
2. What it has established.
3. What object, mechanism, design, or setting it leaves unresolved.
4. What the current paper adds.

Do not end with "our paper is different." End with the exact difference: treatment assignment, reward side, information structure, two-dimensional targeting space, decision timing, policy class, formal definition, data access, or performance metric.

## Model And Theory Sections

Theory papers often start from a standard setup and add one new feature. The prose should show both parts.

- Name the standard setup first, then the new feature.
- Explain why the new feature changes the managerial or economic logic.
- Define the base model before extensions.
- Use "base model" only when the base model carries the main mechanism.
- State simplifications honestly and say where generalizations appear.
- After a proposition, give an interpretation paragraph before moving to proof or the next result.

For formal definitions, explain what the definition rules in and rules out. For new measures, state the decision problem the measure supports before giving the formula.

For MS model writing, the model is persuasive when it is introduced as the answer to a reviewer concern:

- If the concern is **tractability**, explain which state, action, or equilibrium object creates the difficulty and which reformulation controls it.
- If the concern is **identification**, explain what is observed, what is latent, and which institutional feature or excluded variation supports the estimand.
- If the concern is **external validity**, explain which institutional details are retained in the base model and which are stress-tested later.
- If the concern is **behavioral interpretation**, separate the model's mechanical prediction from the behavioral mechanism that the data can test.
- If the concern is **implementation**, say what the algorithm, policy, or estimator takes as input, what it outputs, and what benchmark makes its performance meaningful.

Do not make the model paragraph a list of primitives. A strong MS model paragraph says why these primitives are the right abstraction for the paper's trust device.

## Empirical And Field-Experiment Sections

MS empirical sections feel grounded because they keep the institution and outcome metric visible.

- Describe the partner, platform, firm, market, or data source before the estimating equation.
- Say what is randomized or otherwise shifted, and what remains observational.
- Define business metrics before reporting coefficients.
- Interpret heterogeneity as a boundary condition, not as a list of extra tables.
- Put treatment implementation, survey instruments, long balance tables, and secondary checks in the appendix after the body gives enough information to trust the design.

Do not let "causal evidence" float. State the causal contrast and the metric: treatment versus control, policy versus benchmark, ads versus public service announcements, uncertain sender reward versus certain sender reward, or collaboration treatment versus pure control.

For reviewer persuasion, pair each empirical object with its threat:

- Measurement: show how the construct is observed, validated, and bounded.
- Treatment or adoption: explain timing and why it is plausibly separated from the outcome shock.
- Matching or weighting: report balance and common support before interpreting estimates.
- DID or event study: name the counterfactual group and the timing assumption.
- Structural estimation: state what identifies the latent object and how model fit or external variation supports it.
- Robustness: summarize the conclusion in the body and place the repeated checks in the appendix.

## Abstract Rhythm

MS abstracts are dense but not ornamental.

Common successful order, not a required sentence template:

1. Practice or decision.
2. Missing friction, definition, or evidence.
3. Research design or model.
4. Headline result in the management metric.
5. Mechanism, heterogeneity, or boundary.
6. Implication.

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

Before drafting a full section, it can help to keep a private continuity line:

`This paper changes how [audience] thinks about [decision] because [method/evidence] shows [result] through [mechanism] under [condition].`

Use that line to test what belongs in each section, but do not force every section to restate every part:

- Abstract: the whole continuity line, compressed.
- Introduction: why the continuity line matters and why prior work could not show it.
- Related work: which parts of the continuity line each literature covers or misses.
- Model/data: how the design makes the continuity line verifiable.
- Results: the result and mechanism pieces.
- Proof/appendix: why the formal or empirical support is valid.
- Discussion: what the continuity line does and does not imply.

Do not expose the continuity line in the final unless the user asks for a logic map.

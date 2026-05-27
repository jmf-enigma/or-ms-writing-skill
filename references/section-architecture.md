# Section Architecture

Use this when drafting full sections, choosing headings, reorganizing a manuscript, or deciding where a paragraph belongs. The main rule is that MS/OR papers do not share one universal skeleton. The correct structure follows the paper's evidence lane and the order in which a reviewer needs to be persuaded.

## Journal Signals

- **Management Science**: broad management audience. The structure should keep the management object, evidence, mechanism, and boundary visible even when the paper is technical.
- **Operations Research**: methodological and analytical depth. The structure can foreground model, theorem, algorithm, and performance criterion earlier, but it should still identify the decision problem and benchmark before dense mathematics.
- **M&SOM**: operations-management audience. The abstract is often structured around problem definition, methodology/results, and managerial implications. The body normally keeps problem setting, methodology, and managerial interpretation close together.

## What Recent Full Texts Show

Use these as evidence that structure is conditional, not as formats to copy.

- A Management Science construct/DID paper can use `Introduction`, conceptual framework and propositions, `Data and Methods`, trend and DID results, robustness and alternative explanations, supplementary analyses, and discussion. Its subsections name constructs and threats, such as technology adoption, managerial hierarchy, alternative measurement, and alternative explanations.
- A Management Science reproducibility/meta-science paper can use `Introduction`, `Study Design and Procedures`, results by outcome and variation, and `Discussion and Conclusion`. The design section carries the source of credibility; the results section is organized around what was assessed.
- An Operations Research applied dynamic-programming paper can keep literature review inside the introduction, then move to system model, Lagrangian relaxation, optimality conditions and price models, unit models, policies, and computational study. Proofs and implementation details can go to an electronic companion after the body states theorem meaning and benchmark value.
- A Management Science structural or estimation paper often puts setting and data before identification, then model, estimation, validation, counterfactuals, and managerial interpretation. The model is not merely theory; it is the measurement and counterfactual device.
- A theory paper may be shorter and spare: base model, benchmark, characterization, comparative statics or regimes, extensions, and conclusion. It does not need an empirical-style data or robustness architecture.
- A Management Science AI experiment can use `Ability, Beliefs, and Calibration`, `Measures`, `Empirical Framework`, `Measurement Challenges`, `Experimental Design`, `Results`, and `Conclusion`. This is not loose structure: the construct and measurement sections are what make the treatment effects interpretable.
- A Management Science platform or strategy field experiment can use `Conceptual Motivation`, `Experimental Design and Data`, demand-effect or mechanism sections, placebo tests, heterogeneity, spillovers, and discussion. The conceptual section names the alternative channels before the design chooses among them.
- A Management Science automation field-evidence paper can move from a classic theory to a short model, then to field implementation, empirical strategy, results, alternative mechanisms, and validation. The model section fixes the mechanism the field evidence tests.
- A Management Science bargaining or information-acquisition theory paper can use `Base Model`, `Optimal Information Gathering`, `Stochastic Cost`, `Dual Case`, `Extensions`, and `Discussion`. Section names follow the economic variant, not a generic result list.
- An Operations Research stochastic-control or applied DP paper can use `Problem Description`, Lagrangian relaxation, price models, policies, numerical experiments, and electronic-companion sections for proofs, pseudocode, and network variants. The body still interprets each theorem before handing verification to the companion.
- A Management Science conservation or optimal-learning paper can state sufficient statistics and structural theorems in the body while putting all proofs and many numerical illustrations in the online appendix. The theorem paragraph still says what the statistic, threshold, or policy comparison means.

## Architecture Is Lane-Specific

Do not force every paper into introduction, related work, model/data, results, robustness, implications. Real papers use different architectures.

### Empirical Experiment Or Field Experiment

Common body architecture:

1. Introduction.
2. Literature, theory, or hypotheses when mechanisms are behavioral or conceptual.
3. Research setting, experimental design, data, and measures.
4. Main results organized by outcome or hypothesis.
5. Mechanism, heterogeneity, or downstream quality.
6. Robustness checks or alternative explanations.
7. Discussion and conclusion.

Typical heading language: `Research Setting`, `Experiment Design`, `Data`, `Measures`, `Results`, `Mechanism`, `Robustness Check`, `Discussion`.

Paragraph rhythm: setting or treatment first, design credibility second, table or figure third, interpretation and mechanism after the estimate. Do not begin a results paragraph with a coefficient if the reader has not been reminded of the outcome and contrast.

Recent AI and human-decision experiments often need construct headings such as `Measures`, `Empirical Framework`, and `Measurement Challenges`. Use them when the reader must understand how ability, belief, confidence, calibration, or performance is measured before the treatment result is meaningful. Do not hide these choices in an appendix if they are what makes the experiment credible.

### Archival, DID, Or Construct-Measurement Empirical Paper

Common body architecture:

1. Introduction.
2. Theoretical background and construct development.
3. Data and methods.
4. Measurement validation and sample construction.
5. Main empirical strategy and results.
6. Robustness tests, alternative measurement, and alternative explanations.
7. Supplementary analyses.
8. Discussion, limitations, and conclusion.

Typical heading language: `Theoretical Background`, `Data and Methods`, `Sample Construction`, `Dependent Variables`, `Estimation Strategy`, `Robustness Tests`, `Alternative Measurement`, `Alternative Explanations`, `Supplementary Analyses`, `Limitations`.

Paragraph rhythm: each measure is introduced by what it is meant to capture, how it is observed, why the proxy is credible, and where validation or examples appear. Robustness is part of persuasion, not an appendix afterthought.

### Structural, ML, Or Empirical Revenue-Management Paper

Common body architecture:

1. Introduction.
2. Setting and data, including the decision workflow that creates variation.
3. Identification or model.
4. Estimation procedure.
5. Main estimates or validation.
6. Alternative design or robustness.
7. Counterfactual, application, or managerial use.
8. Conclusion.

Typical heading language: `Data`, `Empirical Strategy`, `Identification`, `Model`, `Estimation`, `Validation`, `Counterfactuals`, `Managerial Implications`.

Paragraph rhythm: the institutional behavior that creates variation appears before the estimating equation. The model section distinguishes observed actions, latent demand or utility, exogenous variation, and the target estimand.

If the paper is about managers using available information, a `Conceptual Motivation` section can be more natural than a generic `Theory` section. It should define the assumed knowledge, the channel the experiment can move, and the alternative explanations the results later revisit.

### Theory, Mechanism, Or Analytical Model

Common body architecture:

1. Introduction.
2. Base model or problem setup.
3. Equilibrium, benchmark, or main characterization.
4. Comparative statics, regimes, or mechanism.
5. Extensions or general model.
6. Numerical illustration or application if used.
7. Conclusion.

Typical heading language: `The Model`, `Benchmark`, `Equilibrium Analysis`, `Main Results`, `Extensions`, `General Model`, `Numerical Analysis`.

Paragraph rhythm: define the standard setup and the new feature before notation becomes dense. After each proposition, interpret the region, threshold, or comparison before moving to the next result.

For information, contracting, or bargaining theory, headings can name information regimes or variants: `Base Model`, `Observable Opportunities`, `Concealable Opportunities`, `Stochastic Cost`, `Seller Information Acquisition`, `Joint Information Acquisition`, or `Organizational Implications`. These are often better than `Model 1`, `Model 2`, or `Robustness` because they tell the reader which economic object changed.

### Theory/Algorithm Or Technical OR Paper

Common body architecture:

1. Introduction, often with related work and contributions inside subsections.
2. Problem description or model.
3. Relaxation, lower bound, or structural results.
4. Algorithm or policy.
5. Performance guarantee.
6. Numerical study or application.
7. Conclusion.

Typical heading language: `Problem Description`, `The Model`, `Main Results`, `Algorithm`, `Analysis`, `Performance Bounds`, `Numerical Experiments`, `Computational Study`, `Appendix`.

Paragraph rhythm: the body may place model and theorem earlier than a Management Science empirical paper. The introduction still explains why the old formulation or standard policy is insufficient and what benchmark makes the new method meaningful.

### Applied OR With Industry Or Field Data

Common body architecture:

1. Introduction with operational setting and current practice.
2. System model or problem formulation.
3. Method, decomposition, algorithm, or policy.
4. Data, calibration, or implementation details needed for trust.
5. Computational or numerical study.
6. Benchmark comparison against current practice or a relaxation.
7. Discussion and conclusion.

Typical heading language: `System Model`, `Lagrangian Relaxation`, `Unit Model`, `Implementation`, `Numerical Experiments`, `Computational Results`, `Industrial-Scale Case Study`.

Paragraph rhythm: explain the current operating workflow before the model. Then say which current-practice constraint the model relaxes, retains, or replaces.

## Heading Practice

Headings should name the paper object, not the writer's prewriting checklist.

Prefer:

- `The Model`, `Research Setting`, `Data and Methods`, `Experimental Design`, `Main Results`, `Robustness Tests`, `Alternative Explanations`, `Algorithm`, `Numerical Experiments`, `Discussion and Conclusion`.
- Descriptive subheadings when they guide interpretation: `Measures`, `Empirical Framework`, `Measurement Challenges`, `Conceptual Motivation`, `Alternative Measurement`, `Customer Acquisition`, `Improving Effectiveness`, `Observable Opportunities`, `Concealable Opportunities`, `Organizational Implications`, `Bounds on the Global Minimal Cost`, `Adding a Routing Node`.

Avoid:

- Generic headings such as `Story`, `Motivation`, `Credibility Support`, `Contribution 1`, or `Reviewer Concern`.
- A separate `Managerial Implications` section when the implications are short and would read better in the result interpretation or conclusion.
- A separate `Related Literature` section when the target paper's lane naturally integrates literature into the introduction, unless the journal or field expects a standalone section.

## Heading Depth And When To Use Subheadings

Use a heading when it changes the reader's task. Do not use a heading merely because the writer has a new thought.

### No Subheading

Keep material in ordinary paragraphs when:

- The passage is a short transition, local intuition, or one robustness sentence.
- The same claim continues with a second piece of evidence.
- A theorem, estimate, figure, or table only needs interpretation, not a new evidence job.
- The paragraph is a bridge between two subsections.

Example: after a theorem statement, the intuition paragraph usually stays under the same result heading. Do not create `Intuition` unless the paper has several long intuition blocks or the target journal commonly separates them.

### Use A Subsection

Use a subsection when the reader should recognize a new object or credibility task:

- A new construct or measure: `Managerial Intensity`, `Decentralization`, `Demand Measures`.
- A new data or design component: `Data Sources`, `Sample Construction`, `Experimental Design`, `Estimation Strategy`.
- A new result family: `Main Treatment Effects`, `Mechanism`, `Heterogeneity`, `Alternative Explanations`.
- A new mathematical component: `System Model`, `Unit Models`, `Lagrangian Relaxation`, `Optimality Conditions`, `Price Models`.
- A new algorithm or computational task: `Algorithm`, `Implementation`, `Benchmark Policies`, `Simulation Design`.
- A new validity threat: `Alternative Specifications`, `Alternative Measurement`, `Placebo Tests`, `Pretreatment Trends`.

Recent full texts use subheadings this way. A Management Science DID/construct paper breaks robustness into `Alternative Specifications`, `Alternative Measurement`, and `Alternative Explanations` because each answers a different reviewer threat. An Operations Research applied DP paper separates `The System Model`, `Lagrangian Relaxations`, unit-level model properties, policies, and numerical experiments because each changes the mathematical object the reader must track.

### Use A Subsubsection Sparingly

Use a third-level heading only when the subsection contains parallel pieces that a reviewer may need to locate independently.

Good uses:

- Different dependent variables, outcomes, or mechanisms inside one results section.
- Different unit types, constraints, or basis functions inside one model section.
- Different datasets, operationalizations, or estimation samples inside one data section.
- Different policy benchmarks or scenarios inside one computational study.

Bad uses:

- `Motivation`, `Intuition`, `Discussion`, `Takeaway`, or `Interesting Result` as tiny headings.
- One-paragraph subsubsections that would read better as topic sentences.
- Symmetric heading stacks that make all material appear equally important when only one result is central.

Use subsubsections for parallel empirical jobs only when a reviewer will search for them independently: `Nonparametric Results`, `Main Parametric Results`, `Placebo Test`, `Heterogeneity`, `Spillovers`, or `Alternative Mechanisms`. If the content is a single interpretive paragraph after a table, keep it unheaded.

### Heading Names

Prefer noun phrases that identify objects: `Data Sources`, `Variable Construction`, `Treatment and Control Firms`, `The System Model`, `Benchmark Policies`, `Numerical Experiments`. Use claim-like subheadings only when the paper's style already supports them and the claim is narrow enough to be true.

Avoid exposing scaffolding: `Story`, `Problem`, `Why It Matters`, `Credibility Support`, `Reviewer Concern`, `Contribution 1`, `Proof Idea`. These can be internal planning labels, not manuscript headings.

### Theorem, Proposition, And Proof Local Headings

Around formal results, headings should be even plainer than section headings.

- Main-text theorem/proposition labels are usually bare: `Proposition 1.`, `Theorem 2.`, `Lemma 3.`, or `Corollary 1.`.
- If a descriptor is useful, keep it short and object-like: `Proposition 1 (Threshold Policy)`, `Theorem 2 (Regret Bound)`, or `Lemma 1 (Monotonicity)`. Avoid full-sentence labels such as `Proposition 1: Our Policy Is Better When Demand Is High`.
- Use the paragraph before the result to say what the result does. This is more natural than turning the proposition label into a mini-abstract.
- After the result, interpret in ordinary prose. Do not create tiny headings such as `Intuition`, `Key Insight`, `Takeaway`, `Proof Idea`, or `Managerial Meaning` unless the paper has several long parallel blocks that require navigation.
- Use `Proof.` only for a complete proof. If the paragraph only explains the proof move and points to an appendix, leave it unheaded.
- Appendix and e-companion headings can be functional and direct: `A.1. Proof of Theorem 1`, `Proof of Proposition 2`, `Auxiliary Lemmas`, `Additional Robustness Checks`, `Data Construction`.

Observed MS/OR papers use these local headings sparingly. A Management Science field-theory paper can put `Proof.` directly under a proposition when the proof is short and then continue with interpretation. A Management Science decision-theory paper can state lemmas, give short body explanations, and reserve `Proof of Lemma 5` for the appendix. A technical Operations Research paper can use headings such as `Proof of Theorem 1`, `Matrix Notation and Bellman Equations`, and `Analysis: Conservative Model-Based Planning` because these labels name proof objects rather than rhetorical moves.

### Subheading Rhythm By Section

- **Introduction**: usually no subheadings in Management Science unless the introduction contains a separate related-work/contributions architecture or the paper is very technical. Do not split the first-page story with miniature headings.
- **Related work**: subheadings are useful when streams are genuinely distinct; otherwise use paragraphs with clear opening sentences.
- **Data/methods**: subheadings are often helpful because readers need to locate data sources, sample construction, variable definitions, design, and estimation.
- **Model/theory**: subheadings should follow the formal object: environment, assumptions, benchmark, equilibrium/optimization, extensions.
- **Results**: subheadings should follow evidence jobs, not table order. Use them for main effect, mechanism, heterogeneity, validation, robustness, and alternative explanations.
- **Appendix/e-companion**: subheadings should follow proof dependency, table family, data documentation, robustness family, or implementation component.

## Paragraph Jobs

Each paragraph should usually perform one job. Choose the job that fits the section.

- **Opening paragraph**: establish the setting, decision, standard view, or formal object.
- **Friction paragraph**: explain what the standard view misses.
- **Design paragraph**: explain data, experiment, model, algorithm, or identification at the level needed for trust.
- **Measure paragraph**: say what the construct captures, how it is observed, and why the proxy is credible.
- **Model paragraph**: translate agents, timing, information, actions, objective, constraints, and benchmark into prose before notation.
- **Result paragraph**: state estimate, theorem, guarantee, or comparison; then interpret metric, benchmark, and condition.
- **Mechanism paragraph**: separate the channel that explains the result from nearby alternative channels.
- **Robustness paragraph**: name the threat, state the check, summarize whether the conclusion changes, and move full details to appendix if secondary.
- **Limitations paragraph**: narrow the claim without undermining the paper; say which limitation matters for interpretation.

## Introduction Architecture

An introduction is not a fixed sequence. Select the modules the paper needs and order them so that the next module answers the reviewer's next question.

Common modules:

- Setting or decision.
- Standard view, current practice, or canonical model.
- Hidden friction, empirical obstacle, or technical difficulty.
- Why existing work cannot answer this version of the question.
- Source of credibility: experiment, institutional variation, theorem, construct validation, model feature, algorithmic guarantee, or benchmark.
- Study design or model preview.
- Findings in the right evidence register.
- Contributions by audience or literature stream.
- Roadmap only when it helps the reader navigate a long or technically unusual paper.

Roadmaps are common but not mandatory. If used, keep them short and section-specific, not a paragraph of table-of-contents prose.

## Model And Data Sections

The right ordering depends on the lane:

- Theory and algorithm papers often put the model or problem formulation immediately after the introduction.
- Empirical papers often need setting and data before identification or estimation.
- Structural papers often interleave model, identification, and estimation because the model is the measurement device.
- Applied OR papers often put system description before the mathematical formulation so the reader understands the operating constraints.

Do not use a heading called `Model / Setting / Data` in final prose unless the paper actually uses a combined section. Choose the heading that matches the object: `The Model`, `Research Setting`, `Data and Methods`, `Empirical Strategy`, `Problem Description`, or `System Model`.

## Result Section Architecture

Result sections are organized by the evidence job, not by the order in which the analysis was run.

- Empirical experiment: main treatment effects, mechanism, heterogeneity, robustness.
- Archival/DID: main estimate, measurement validation if not earlier, robustness, alternative explanations, supplementary analyses.
- Theory: theorem or proposition, interpretation, proof idea when needed, comparative statics, extensions.
- Hybrid theory-field paper: model or conceptual mechanism, implementation, main field effect, mechanism evidence, alternative explanations, and external or survey validation.
- Applied OR paper: policy or relaxation result, algorithm or implementable rule, benchmark comparison, computational scale, sensitivity, and implementation details.
- Algorithm: structural result, algorithm, guarantee, computation, benchmark comparison.
- Applied OR: primary operational comparison, scalability or feasibility, sensitivity, benchmark or perfect-information bound.

Avoid a section titled only `Results` if the paper has several distinct result jobs. Use subsection titles that tell the reader what each result establishes.

## Main Text, Appendix, And Online Supplement

After results exist, organize by reader job.

- Main text is for first-pass understanding and contribution evaluation. Keep headline results, key theorem or proposition statements, preferred estimates, primary figures/tables, central algorithms, key assumptions, benchmark definitions, and result interpretations in the body.
- Regular appendix is for material required for verification but disruptive to the first pass: full proofs, auxiliary lemmas, routine algebra, KKT or induction details, extended derivations, and formal statements of secondary extensions.
- Online appendix or e-companion is for optional but useful support: secondary robustness checks, alternative specifications, parameter sweeps, extra datasets, data dictionaries, code details, computational settings, and replication notes.
- If a robustness check addresses the main threat to identification or validity, summarize it in the body and move the full table or repeated variants to the appendix.
- If an extension changes the main interpretation, give it a body paragraph. If it only shows scope, summarize the takeaway and move formulation and proof.
- Do not use the appendix as a substitute for interpretation. The body should still say why the result matters.

## Title And Subheading Style

Titles and headings should be informative but restrained.

- A title can name the object and mechanism: `Demand Estimation Using Managerial Responses to Automated Price Recommendations`.
- A title can name the application and method: `Unit Commitment Without Commitment`.
- A title can be slightly evocative when the subtitle clarifies the object, but do not sacrifice precision.
- Subheadings should be short noun phrases, not claims dressed as slogans.
- Avoid headings that reveal the author's workflow rather than the reader's object, such as `Our Approach`, `Interesting Results`, or `More Analysis`.

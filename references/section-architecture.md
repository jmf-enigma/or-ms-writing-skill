# Section Architecture

Use this when drafting full sections, choosing headings, reorganizing a manuscript, or deciding where a paragraph belongs. The main rule is that MS/OR papers do not share one universal skeleton. The correct structure follows the paper's evidence lane and the order in which a reviewer needs to be persuaded.

## Journal Signals

- **Management Science**: broad management audience. The structure should keep the management object, evidence, mechanism, and boundary visible even when the paper is technical.
- **Operations Research**: methodological and analytical depth. The structure can foreground model, theorem, algorithm, and performance criterion earlier, but it should still identify the decision problem and benchmark before dense mathematics.
- **M&SOM**: operations-management audience. The abstract is often structured around problem definition, methodology/results, and managerial implications. The body normally keeps problem setting, methodology, and managerial interpretation close together.

## What Recent Full Texts Show

Use these as evidence that structure is conditional, not as formats to copy.

- A Management Science construct/DID paper can use `Introduction`, conceptual framework and propositions, `Data and Methods`, trend and DID results, robustness and alternative explanations, supplementary analyses, and discussion. Its subsections name constructs and threats, such as technology adoption, managerial hierarchy, alternative measurement, and alternative explanations.
- A Management Science reproducibility/meta-science paper can use `Introduction`, `Study Design and Procedures`, results by outcome and variation, and `Discussion and Conclusion`. The design section carries the trust device; the results section is organized around what was assessed.
- An Operations Research applied dynamic-programming paper can keep literature review inside the introduction, then move to system model, Lagrangian relaxation, optimality conditions and price models, unit models, policies, and computational study. Proofs and implementation details can go to an electronic companion after the body states theorem meaning and benchmark value.
- A Management Science structural or estimation paper often puts setting and data before identification, then model, estimation, validation, counterfactuals, and managerial interpretation. The model is not merely theory; it is the measurement and counterfactual device.
- A theory paper may be shorter and spare: base model, benchmark, characterization, comparative statics or regimes, extensions, and conclusion. It does not need an empirical-style data or robustness architecture.

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
- Descriptive subheadings when they guide interpretation: `Alternative Measurement`, `Customer Acquisition`, `Improving Effectiveness`, `Bounds on the Global Minimal Cost`, `Adding a Routing Node`.

Avoid:

- Generic headings such as `Story`, `Motivation`, `Trust Device`, `Contribution 1`, or `Reviewer Concern`.
- A separate `Managerial Implications` section when the implications are short and would read better in the result interpretation or conclusion.
- A separate `Related Literature` section when the target paper's lane naturally integrates literature into the introduction, unless the journal or field expects a standalone section.

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
- Trust device: experiment, institutional variation, theorem, construct validation, model feature, algorithmic guarantee, or benchmark.
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

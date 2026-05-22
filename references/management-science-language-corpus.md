# Management Science Language Corpus

Use this when the target is Management Science, when the user says "MS," or when the user wants prose that sounds closer to Management Science articles rather than generic OR/MS writing. The goal is to learn the journal's contribution logic and sentence rhythm from comparable papers. Do not copy a source sentence or mimic one living author's distinctive voice. Borrow the field pattern, the evidence order, and the management framing.

## What Management Science Wants The Writing To Prove

Management Science is broad, but the common thread is analytical insight into management. A strong paragraph makes the reader see:

1. the managerial, organizational, market, or individual decision;
2. the friction that makes the usual decision rule incomplete;
3. the model, data, experiment, or algorithm that isolates the friction;
4. the mechanism or magnitude that changes the reader's belief;
5. the condition under which a manager, platform, firm, regulator, or researcher should think differently.

The prose should therefore sound less like "we solve a model" and more like "this model changes how a decision is understood."

## Source Set

Journal guidance:

- Management Science submission guidelines define the journal around scientific research on the practice of management across strategy, innovation, IT, organizations, accounting, finance, marketing, operations, and individual or organizational decision making.
- The Management Science editorial statement says acceptable papers must be relevant to management theory or practice, rigorous, broadly interesting to management science scholars, readable, well organized, and written in good style.

Management Science article signals:

1. Kawaguchi, "When Will Workers Follow an Algorithm? A Field Experiment with a Retail Business," 2020.
2. Sun, Zhang, Hu, and Van Mieghem, "Predicting Human Discretion to Adjust Algorithmic Prescription," 2021.
3. Ai, Chen, Mei, Ye, and Zhang, "Putting Teams into the Gig Economy," 2023.
4. Greiner, Grunwald, Lindner, Lintner, and Wiernsperger, "Incentives, Framing, and Reliance on Algorithmic Advice," 2025.
5. Kesavan, Kushwaha, and Steele, "Profit Implications of Judgmental Adjustments to Forecast Inputs," 2025.
6. Xu, Dai, and Yan, "Identity Disclosure and Anthropomorphism in Voice Chatbot Design," 2024.
7. Dargnies, Hakimov, and Kubler, "Aversion to Hiring Algorithms," 2024.
8. Gur, Macnamara, Morgenstern, and Saban, "Information Disclosure and Promotion Policy Design for Platforms," 2023.
9. Besbes and Mouchtaki, "How Big Should Your Data Really Be? Data-Driven Newsvendor," 2023.
10. Chen, Cire, Hu, and Lagzi, "Model-Free Assortment Pricing with Transaction Data," 2023.
11. Liu, van Jaarsveld, Wang, and Xiao, "Managing Outpatient Service with Strategic Walk-ins," 2023.
12. Cheung, Simchi-Levi, and Zhu, "Nonstationary Reinforcement Learning," 2023.
13. Gaur and Park, "Asymmetric Consumer Learning and Inventory Competition," 2007.
14. Govind, Chatterjee, and Mittal, "Segmentation of Spatially Dependent Geographical Units," 2017.
15. Cao, "Collaborative Learning and Decision Making on Pricing and Recommendation," 2025.
16. Li, Owen, and Zhu, "Estimating Effects of Long-Term Treatments," 2026.
17. Athey, Calvano, and Gans, "A Theory of the Effects of Privacy," 2025.
18. Brunnermeier, Simsek, and Xiong, "Relatively Robust Multicriteria Decisions," 2025.
19. Borodin, El-Yaniv, and authors, "The Competitive Ratio of Threshold Policies for Online Unit-Density Knapsack Problems," 2025.
20. "When Should the Off-Grid Sun Shine at Night? Optimum Renewable Generation and Energy Storage Investments," 2023.
21. Li, Belo, and Li, "Can Reward Uncertainty Encourage Social Referrals? Evidence from a Large-Scale Field Experiment," 2026.
22. Brahm, Lafortune, Magelssen, and Tessada, "Collaboration, Workplace Practice Adoption, and Performance," 2026.
23. Gu, Bapna, Chan, and Gupta, "Measuring the Impact of Crowdsourcing Features on Mobile App User Engagement and Retention," 2022.
24. Frick, Belo, and Telang, "Incentive Misalignments in Programmatic Advertising," 2023.
25. Cui, Demirer, Jaffe, Musolff, Peng, and Salz, "The Effects of Generative AI on High-Skilled Work," 2026.
26. Orzach and Quist, "Managerial Intervention, Employee Motivation, and Collaboration," 2026.
27. Li, Liu, and Wei, "Credit Rating Purchases and S&P 500 Index Membership Decisions," 2026.
28. Levi, Paulson, and Perakis, "Designing Inclusive Offerings," 2025.
29. Hardwicke et al., "Reproducibility in Management Science," 2023.
30. Guo, "The Mnemonomics of Contractual Screening," 2022.
31. Kasy and Abebe, "Learning to Be Fair," 2024.
32. DeValve and Myles, "Approximation Algorithms for Dynamic Inventory Management on Networks," 2024.
33. Federgruen, Liu, and Lu, "Sourcing with Demand Updates," 2026.
34. Feng, Li, and Shanthikumar, "Transfer Learning, Cross Learning and Co-Learning with Operational Data Analytics," 2026.
35. Manshadi, Rodilitz, Saban, and Suresh, "Redesigning VolunteerMatch's Search Algorithm," 2025.
36. Bapna, Ramaprasad, Shmueli, and Umyarov, "One-Way Mirrors in Online Dating," 2016.
37. Bird and Frug, "A Theory of Front-Line Management," 2025.

For full-section or whole-paper story logic, use `management-science-whole-paper-storycraft.md` together with this file. This file gives lane-specific vocabulary and section habits; the whole-paper file gives continuity across abstract, introduction, model or data, results, proof, and discussion.

## Comparable-Design Routing

Before writing, match the user's paper to the closest Management Science lane. If more than one lane fits, use the first for the abstract and the second for contribution positioning.

### Field Experiment With A Firm Or Platform

Use for retail, gig, warehouse, chatbot, advertising, platform launch, and operational intervention papers.

Writing order:

1. Start with a managerial practice or adoption problem.
2. Say what managers believe or what existing evidence misses.
3. Name the field setting and treatment.
4. Report the main magnitude in the business metric.
5. Explain heterogeneity or mechanism.
6. Close on what implementation would change.

Language tendencies:

- Use "we report the results from," "we conducted a field experiment," "orders were randomly assigned," "we find," and "the effect is stronger when."
- Tie every percentage to a business metric, such as revenue, profit, response probability, packing time, forecast accuracy, worker effort, or order acceptance.
- Do not let the treatment list dominate. The reader should know which managerial belief the experiment tests.

Native MS move:

`Although [literature/practice] has studied [intermediate metric], causal evidence is limited on whether [intervention] improves [bottom-line metric].`

### Human-Algorithm And Behavioral Operations

Use for algorithm aversion, worker discretion, forecast overrides, chatbot design, and AI-assisted decisions.

Writing order:

1. Algorithms are available, but human adoption or discretion determines realized value.
2. The paper separates algorithm quality from human response.
3. The design identifies when people follow, override, or reject the recommendation.
4. The result reports both behavior and operational performance.
5. The implication is about adoption design, not only algorithm design.

Language tendencies:

- Use "nominal performance" versus "actual performance" when the algorithm works on paper but adoption limits value.
- Use "human intervention," "algorithmic advice," "worker discretion," "forecast inputs," "reliance," "delegation," and "adherence" with specific outcomes.
- Prefer "the gap between algorithmic prescription and implementation" over vague "human factors."

Native MS move:

`The result shifts the design problem from improving the algorithm in isolation to improving the human-algorithm system that determines realized performance.`

### Data-Driven Revenue Management Or Operations

Use for pricing, assortment, newsvendor, transaction data, limited data, misspecification, and model-free methods.

Writing order:

1. Name the classical decision problem.
2. State what information is missing or unreliable.
3. Explain what the data contain and what they do not reveal.
4. State the mapping from data to decision.
5. Compare against an oracle, model-based approach, sample-average approximation, or heuristic.
6. Translate the performance result into value of data or robustness to misspecification.

Language tendencies:

- Use "map data to decisions," "limited data," "historical transactions," "out-of-sample performance," "model misspecification," "oracle," "worst-case regret," and "finite-sample."
- Avoid "data-driven" as a free-standing virtue. Say what the data allow the decision maker to infer or what they cannot infer.
- If the result is counterintuitive, state the usual data intuition first, then the regime where more data or a richer model can fail.

Native MS move:

`The main question is not whether data are useful, but how much data are needed before the decision improves relative to a simple benchmark.`

### Analytical Platform Or Market Design Model

Use for platforms, marketplaces, information disclosure, promotion, pricing, dispute resolution, certification, matching, and consumer surplus.

Writing order:

1. Name the platform's control and its objective.
2. Explain how sellers, buyers, users, or workers respond.
3. Identify the dynamic or strategic friction.
4. Introduce the policy class or equilibrium concept.
5. State the mechanism and welfare or surplus consequence.
6. Give a practical policy interpretation.

Language tendencies:

- Use "facilitating trade," "information revealed," "promotion policy," "seller learning," "consumer surplus," "myopic pricing," "equilibrium," and "policy design" only when the model contains those objects.
- Good MS platform prose makes the private response visible before the platform's objective is optimized.
- The implication should distinguish platform profit, seller revenue, consumer surplus, and welfare when they differ.

Native MS move:

`The platform can influence outcomes even when it does not set prices, because its information and promotion policies shape what sellers learn and how they respond.`

### Service Operations And Queueing With Strategic Customers

Use for outpatient care, appointments, walk-ins, staffing, scheduling, congestion, capacity, and access channels.

Writing order:

1. Start with the access or capacity choice faced by the provider.
2. Explain the customer's strategic choice or operational tradeoff.
3. Name the operational levers.
4. Use the model to compare systems that appear intuitively ranked.
5. State the two conditions that determine the ranking.
6. Close with "no one-size-fits-all" only if the result genuinely depends on observable conditions.

Language tendencies:

- Use "access channels," "appointment delay," "in-clinic waiting," "capacity allocation," "triage," "lost demand," "overtime," and "operational efficiency."
- Avoid generic "healthcare is complex." State the exact congestion or behavioral mechanism.

Native MS move:

`The ranking of the two systems hinges on [capacity-demand relation] and [willingness to wait], which are observable features of the practice environment.`

### Behavioral Experiment Or Survey

Use for online experiments, lab experiments, hiring algorithms, discrimination, disclosure, trust, incentives, framing, and decision aid adoption.

Writing order:

1. State the behavioral puzzle or managerial belief.
2. Name participant roles and the decision they make.
3. Describe treatments only enough to make identification clear.
4. Report behavioral response and performance consequence separately.
5. Explain the mechanism, such as overconfidence, trust, fairness concern, or information.

Language tendencies:

- Use "participants are in the role of," "choose whether," "we directly compare," "feedback increases," and "providing details does not increase" with restraint.
- Be precise about whose belief or action changes. Do not collapse workers, managers, consumers, and firms into "users."

Native MS move:

`The experiment separates aversion to the algorithm from aversion to the information the algorithm uses.`

### Theory Or Algorithm With Management Applications

Use for reinforcement learning, bandits, algorithms, optimization, and technical data science papers submitted to MS.

Writing order:

1. Motivate with management or OR applications.
2. Define the technical setting or a small illustrative example.
3. State what standard method, state variable, policy class, or principle fails.
4. Introduce the new technique, policy class, lower bound, or decomposition.
5. State the guarantee with its comparator and conditions.
6. Show the management application, implementation logic, numerical setting, or calibration.

Language tendencies:

- Use "motivated by applications such as," "we consider," "we develop," "we establish," "we propose," "dynamic regret," "variation budget," and "numerical experiments" with exact objects.
- Management Science tolerates technical language here, but the abstract still needs an application anchor and a sentence explaining why the technical obstacle matters.

Native MS move:

`The technical obstacle is not uncertainty alone, but uncertainty that changes over time in a way that makes historical data misleading.`

### Hybrid Algorithm-Field Implementation

Use for platform algorithms, equitable access, display ranking, search, matching, and nonprofit or marketplace collaborations.

Writing order:

1. Name the partner's existing algorithm and the metric it optimizes.
2. Explain the undesirable distributional or access consequence of that metric.
3. Define the second objective, such as equity, exposure, access, or coverage.
4. Present the algorithm as both theory object and intervention.
5. Report field implementation with causal or quasi-experimental evidence.
6. Translate the effect into the partner's operational scale.

Language tendencies:

- Use "efficiency," "equity," "display ranking," "connections," "access," "implementation," "difference-in-differences," and "scale" only with exact metrics.
- Do not write as if equity is self-defining. State the paper's operational definition before the algorithm.
- The best story is often not algorithmic novelty alone but the tension between the platform's old objective and the access outcome it unintentionally created.

Native MS move:

`The algorithm matters because it changes which opportunities receive access, not only how many total connections the platform creates.`

### Operational Data, Transfer, And Cross-Learning

Use for ODA, transfer learning, data pooling, limited data, related systems, and nonparametric operational decisions.

Writing order:

1. Start with the decision under limited data.
2. State the tempting statistical response, such as transfer learning or pooling.
3. Explain why decision optimality is not the same as predictive or aggregate performance.
4. Introduce the solution concept that matches data structure to decision structure.
5. State subsystem-level and aggregate-level guarantees separately.
6. End with the role of domain knowledge or operational structure.

Language tendencies:

- Use "related system," "focal system," "data pooling," "operational statistics," "decision performance," "subsystem," and "aggregate system" with care.
- Do not praise data sharing in general. Say when cross-system data helps and when it limits optimality.

Native MS move:

`The question is not whether related data are useful, but whether the way they are combined preserves the decision structure of the focal system.`

## How To Write Better Given The Same Data And Model

When the user gives data, model, or results, do this before drafting.

1. Identify the closest Management Science lane above.
2. Name the strongest managerial belief the evidence can change.
3. Choose the outcome metric that makes the evidence consequential.
4. Replace generic model language with the model's role in the argument.
5. Put the most decision-relevant result before technical completeness.
6. Save robustness, secondary heterogeneity, and auxiliary mechanisms for later paragraphs unless they change the headline.

Examples of stronger framing:

- Instead of "we develop a model of platform pricing," write around what the platform controls, what sellers learn, and why this changes consumer surplus.
- Instead of "we use transaction data," write around what the transactions reveal, what they leave unidentified, and how the policy performs despite that limitation.
- Instead of "we conduct a field experiment," write around the managerial practice being tested, the causal contrast, and the business metric that moves.
- Instead of "we propose an algorithm," write around the gap between the algorithm's nominal performance and the operational process that determines realized performance.

## Whole-Paper Story Logic

When writing more than a local paragraph, use the MS story as a diagnostic map:

`existing practice or belief -> hidden friction -> design object -> result -> mechanism -> boundary -> implication`

These beats are not a required outline. The method should appear where it resolves the friction. The result should appear in a metric that matters for the decision. The mechanism should explain why the result has the observed sign or condition when the mechanism is part of the claim. The implication should change a managerial, policy, methodological, or theoretical belief without overstating the evidence.

Do not make every paragraph tell the whole story. Let each paragraph do one job: establish the practice, expose the friction, introduce the design, report the result, explain the mechanism, state the boundary, or position the contribution.

## Management Science Model, Result, And Appendix Craft

Use this section when the target is Management Science and the passage involves model setup, theorem statements, proof intuition, estimators, appendices, or online appendices.

### Model Setup

MS model sections usually do not begin with a raw symbol list. They first name the managerial or experimental environment, then introduce notation in the order the reader experiences the problem.

- In algorithmic pricing and recommendation papers, the body first names the teams, their information, their decisions, the sequence of decisions, and why the other team's process is a black box. Only after that does it formulate the contextual bandit object.
- In empirical identification papers, the body first defines the experimenter's decision problem, observed periods, future periods, treatment assignment, outcomes, and missing future outcome. Tables and figures are used to make notation concrete before the theorem.
- In theory papers with broad constructs, such as privacy or robust multicriteria decisions, the body defines the welfare or performance object and then explains what the comparison means before stating propositions.
- In investment or energy papers, the body keeps the operational problem and approximation logic visible. A general model can be followed by tractable approximations if the approximations are the objects that generate analytical insights.

### Assumptions

MS papers tend to earn assumptions immediately.

- A strong assumption paragraph says what the assumption rules out or enables, then provides a simple example, equivalence, or special case.
- If an assumption is stronger than a standard condition, say why the stronger form is needed and what aspect of the decision process creates the need.
- If a new assumption is introduced only to simplify a more general identification or decision rule, state the practical reason, such as limited sample size or computational tractability.
- Put practical guidelines, extended comparisons, and weaker-condition variants in the Online Appendix after the body states the assumption's role.

### Result Paragraphs

MS result paragraphs usually have a three-part body rhythm.

1. State the result with conditions and object.
2. Explain what the object means for the decision, estimator, policy, or benchmark.
3. Compare to a standard intuition, benchmark, special case, or practical implication.

Do not stop after the theorem display. In MS, the sentence after a theorem often tells the reader why the rate, bound, identification expression, threshold, or welfare comparison matters. If the theorem is technical, the interpretation can be more important than the proof pointer.

### Proof Ideas In The Body

MS papers often keep proof ideas in the body when the idea explains why the result is credible or why the method is new.

- For regret or learning papers, the body may show the decomposition, define intermediate regret quantities, and explain how auxiliary lemmas control them. Detailed lemmas and equality proofs can move to Online Appendix EC sections.
- For identification papers, the body may show a special case first, then state the general theorem. This lets the reader see the mechanism before seeing the full expression.
- For robust or theoretical papers, the body may give a lemma proof sketch or intuitive proof paragraph when the argument clarifies existence, compactness, efficiency, or approximation. Routine contradictions, recursive case checks, and contour-set calculations can move to the appendix.
- For privacy or market-design papers, the body often decomposes the effect into interpretable forces and then uses applications to explain the sign. The appendix verifies expansions and case splits.

MS proof-idea prose is plain and functional. It should not have a distinctive "voice." Use ordinary proof verbs and exact mathematical objects.

- Start by saying what the sketch proves or why it is included.
- If the sketch uses an extra simplifying assumption, state it immediately and say where the complete proof appears.
- Name the first constructed object or reduction. Common starts are "We construct an upper bound," "We decompose the regret," "We first show," "It suffices to bound," or "The argument has two steps."
- After a displayed equation, say what the display removes, bounds, or transforms. Do not add rhetorical flourish.
- End by saying how the bound, decomposition, or lemma yields the theorem.

Bad proof-idea voice for MS:

- Too story-like: "The heart of the proof is a delicate dance between exploration and exploitation."
- Too vague: "The proof follows from standard arguments."
- Too grand: "This elegant insight reveals the deep structure of the problem."
- Too list-like for polished body prose: "Step 1 is..., Step 2 is..., Step 3 is..." unless the paper itself is presenting a technical roadmap.

Better MS proof-idea voice:

- "The proof constructs an upper bound on the optimal payoff and compares the proposed contract with this bound."
- "The regret decomposition separates the pricing error from the recommendation error. Lemma EC.x controls the first term by lower bounding the design matrix, and the remaining term is bounded by the sampling rule."
- "We give the proof under the monotone hazard-rate assumption. Appendix D proves the same bound without this assumption."

### Appendix And Online Appendix Pointers

MS appendix references are selective and informative. They do not replace interpretation.

- Point to the Online Appendix for proofs of auxiliary lemmas, special-case lower bounds, extended comparisons with prior work, practical guidelines, algorithm details, and model-misspecification extensions.
- Keep in the body the theorem statement, the object being transformed, the reason the transformation matters, and the implication for the decision.
- When using an appendix pointer, say what role the omitted material plays. For example, it proves a lemma, validates a sufficient condition, provides a lower bound under the same assumptions, or gives implementation details.
- Do not write only "see Appendix" after a theorem. MS papers usually give the theorem's meaning before sending the reader away.

### Punctuation And Format

MS uses formal punctuation naturally in technical sections. The problem is not the colon or semicolon itself; the problem is checklist rhythm.

- Colons are normal in theorem titles, assumptions, definitions, proof headings, examples, and structured results.
- Semicolons may appear in formal conditions or proof sentences when they keep linked conditions together.
- Avoid colon-led prose roadmaps in abstracts and result interpretations unless the journal format requires them.
- In technical sections, preserve punctuation that helps the reader parse assumptions, theorem conditions, or proof cases.

## Management Science Abstract Blueprint

For MS, prefer a single paragraph under 250 words unless the user asks otherwise.

1. Sentence 1. The practice, decision, or puzzle.
2. Sentence 2. The missing friction or evidence gap.
3. Sentence 3. Data, model, experiment, or algorithm.
4. Sentences 4 and 5. Main results with magnitudes or mechanisms.
5. Sentence 6. Heterogeneity, boundary condition, or benchmark comparison.
6. Final sentence. What the result changes for management theory or practice.

If the paper is theory-heavy, the final sentence can target modelers or algorithm designers rather than managers.

## Management Science Introduction Rhythm

First page:

- Start with a real decision, not a literature gap.
- Introduce the managerial belief or standard practice.
- Show why the belief may fail once the key friction is present.
- State the paper's question in terms a non-specialist management scholar can understand.

Middle of introduction:

- Introduce data/model only after the question is clear.
- Explain identification, equilibrium, or algorithm in one sentence before listing findings.
- State findings in a sequence that follows the reader's decision problem.

Contribution section:

- Organize by what each audience learns, not by what each method did.
- Make the first contribution the core management insight.
- Put technical contributions after the reader sees why the technical step is needed.

## Phrase Bank With Careful Use

Use these as safe building blocks. Adapt nouns to the user's setting.

- `The central challenge is that [actor] observes [signal] but must decide [action] before [uncertainty resolves].`
- `This distinction matters because [decision] changes [metric] only through [mechanism].`
- `The field experiment allows us to compare [practice] with [benchmark] in the same operational environment.`
- `The data reveal [behavior], but they do not directly identify [latent object]. Our model bridges this gap by [abstraction].`
- `The result cautions against evaluating [method] only by [intermediate metric], because [bottom-line metric] can move differently.`
- `The finding is conditional. [Policy] improves [metric] when [condition], but can reduce [metric] when [condition fails].`
- `The model clarifies why [common practice] can be optimal in one regime and harmful in another.`

## Words To Prefer

MS prose likes concrete verbs with exact objects.

- For empirical work: estimate, compare, document, test, identify, quantify, separate, evaluate.
- For field experiments: randomize, assign, implement, measure, report, examine heterogeneity.
- For theory: characterize, derive, establish, compare, show, identify, construct.
- For algorithms: develop, propose, tune, adapt, benchmark, validate.
- For managerial interpretation: cautions, suggests, shifts, clarifies, implies, distinguishes.

## Words To Distrust

These often make MS prose sound generic unless the sentence immediately specifies the metric or mechanism.

- important, novel, significant, practical, valuable, robust, effective, efficient, comprehensive, real-world, complex, dynamic, innovative.
- framework, insight, implication, performance, decision making, value, impact.

The fix is usually to name the exact object. Use profit, consumer surplus, match rate, response probability, acceptance intention, packing time, forecast error, regret, waiting time, overtime, lost demand, adoption, reliance, or revenue when that is what the paper measures.

## Final MS Pass

Before returning polished prose, ask:

1. Would a Management Science reader know the management question after the first two sentences?
2. Does the method appear because it is needed for the question, rather than because the authors want to advertise it?
3. Is the best result stated in the metric the reader cares about?
4. Does the mechanism explain why the result occurs?
5. Does the final sentence say what belief, policy, or research approach should change?

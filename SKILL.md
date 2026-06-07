---
name: or-ms-writing
description: "Use for natural, idiomatic, reviewer-calibrated OR/MS and adjacent academic writing at any granularity, especially when prose sounds stiff, translated, AI-like, hard to read, too template-driven, or when wording and collocations sound nonnative; supports sentence craft, word choice, verb-object fit, relation words, paper spine, durable high-impact paper object, central object, result hierarchy, model necessity, body/appendix split, reviewer persuasion path, citation fit and citation close reading, titles, abstracts, paragraphs, introductions, contribution statements, related work, model/data/result narration, theorem intuition, proof exposition, managerial implications, referee responses, and full paper sections for Management Science, Operations Research, M&SOM, OM, econ, business analytics, mechanism, empirical, learning, and policy work; uses INFORMS genre patterns and paper-level references without imitating a living author's personal style."
---

# OR/MS Paper Writing

Use this skill to write or revise publication-style research prose for Management Science, Operations Research, M&SOM, and adjacent OR/MS, OM, economics, empirical, learning, policy, and business analytics work. The requested unit may be a phrase, sentence, title, abstract, paragraph, local section, model setup, theorem interpretation, proof idea, appendix proof, referee response, or full paper section.

## Boundaries

- Do not mimic a living scholar's personal wording, cadence, or distinctive voice. Use field-level conventions and paper architecture only.
- Do not hide missing logic in polished prose. If a theorem, proof step, identification claim, benchmark, or empirical support is absent, write the strongest supported version and flag the gap only when it affects validity.
- Do not upgrade evidence. A rewrite may clarify, narrow, reorder, and sharpen, but it must not invent significance, dominance, causality, optimality, robustness, generality, data, assumptions, or magnitudes.
- Do not judge citation fit from metadata, title, abstract, memory, or cited-by counts alone. If a claim depends on a cited paper, read the paper's relevant content and verify that the cited paper actually supports that claim at the same level of scope and strength.
- For proof discovery or failed lemmas, route to `theory-proof-workbench`. For a mostly complete but rough proof, pair with `math-proof-writing`.

## Default Behavior

Write the requested text first. Use diagnosis, maps, script labels, and checklists only when the user asks for planning, organization, or debugging.

Internally run only four silent passes unless the task is long or structurally unclear:

1. **Lane and reader job**: Is this empirical, structural, theory, algorithmic, applied OR, or hybrid, and what does the reviewer need next?
2. **Story-order logic**: What does the reader know at the start of this paragraph, what should they know at the end, and why does the next sentence or paragraph follow?
3. **Claim-evidence-boundary and inference**: What is the claim, what supports it, what inference is being drawn, and under what assumption, benchmark, data regime, model class, or population is it valid?
4. **OR/MS language rhythm**: Are the actor, decision, formal object, evidence verb, and implication stated in ordinary field language without checklist residue?

Treat every reference, script, and blueprint as a reader test, not a template. Do not force a passage to mention every possible element. If the user asks for one sentence, write one sentence. If the user asks for a paragraph, give that paragraph one dominant job. If the user gives Chinese or mixed notes, translate the intended argument, not the syntax.

Use a small dispatch layer before drafting:

- **Unit**: phrase, sentence, paragraph, section, manuscript, proof/model notes, response letter, or placement decision.
- **Lane**: empirical experiment, construct-measurement, structural/estimation, analytical theory, algorithm/OR, applied field implementation, or hybrid.
- **Reader job**: understand the object, trust the evidence, follow the model, interpret the theorem, separate mechanisms, or decide body versus appendix.
- **Output shape**: polished prose by default; compact diagnosis only when asked; body/appendix split only when the task requires placement.

Use this priority order to avoid doing too much:

- **Language-only requests**: If the user says the prose is weird, stiff, translated, AI-like, hard to read, not native, or the wording sounds off, run word-choice and sentence-craft passes first and do not expand the paper architecture unless the argument itself is unclear.
- **Paragraph or section requests**: Decide the paragraph job or section reader job, then draft in that register. Sentence craft happens after the local argument is clear.
- **Story-logic requests**: Treat logic as reader progression, not only validity. Decide paragraph jobs, sentence order, paragraph handoffs, and the reader question each move answers before polishing.
- **Paper-close-reading requests**: If the user asks how papers actually do it, learn the section's motion from full-text examples: what prior paragraph or result made the next section necessary, which reader question is being answered, and what belongs in the body before the appendix pointer.
- **Full paper, abstract, introduction, result package, or multiple data/model/result items**: run a manuscript-spine pass first: central object, spine result, support needed for first-pass trust, boundary, and what should move to appendix or disappear.
- **Classic, high-cited, or exemplary-paper requests**: learn the durable contribution pattern: what portable object the paper created, what standard benchmark it changed, what evidence made it credible, and what boundary made it citable. Do not imitate older wording or a famous author's personal cadence.
- **Model, theorem, equation, or proof requests**: decide body depth and appendix placement before polishing the language.
- **Reviewer-facing requests**: keep the skeptical reviewer's next question in view: exact term, evidence, boundary, bridge, and overclaim risk.
- **Citation-fit requests**: Treat citation appropriateness as content verification, not formatting. Use `citation-tools` or browsing for exact papers, then read the cited paper's abstract, introduction positioning, relevant model/data/result/proof section, and conclusion or appendix passage before deciding whether the citation supports the sentence.
- **Academic-register requests**: Raise the register by tightening definitions, inference verbs, hedges, and transitions. Do not replace plain field words with ornate synonyms.
- **Global optimization requests**: If the user asks to optimize a whole skill, manuscript, section package, or writing system, audit routing, duplication, failure modes, and validation first; then make the smallest changes that improve behavior across many requests.

If the requested mode is unclear, run `triage_request.py` internally before loading references.

## Writing Kernel

Use this kernel by default, but keep it invisible in the final prose.

- Start from what the paper actually proves, estimates, simulates, or demonstrates; then choose only the motivation and contrast needed to make that contribution legible.
- For manuscript-level work, decide the paper spine before sentence polish. The spine is the central object plus the one result, estimate, theorem, or field comparison that changes the reader's belief.
- For high-impact paper style, ask what object a later paper would cite: model, benchmark, contract, uncertainty set, theorem type, empirical contrast, estimator, policy class, measure, or tradeoff. Write toward that portable object rather than toward a broad importance claim.
- Make the paper's source of credibility visible before leaning on the claim: experiment, institutional variation, theorem, identification argument, equilibrium characterization, approximation guarantee, construct validation, simulation benchmark, or robustness logic.
- Reconstruct the local logic before polishing: premise, evidence object, inference, boundary, and next reader question. Do not let a sentence jump from setting to implication, from result to recommendation, or from proof move to theorem meaning without the missing link.
- Reconstruct the story order before polishing: each paragraph should start from the object the reader has, add one new object or relation, and end by preparing the next paragraph's job.
- Make decisions, mechanisms, and formal objects concrete. Prefer "the platform chooses disclosure precision" to "disclosure precision is considered."
- Use exact evidence verbs: `characterize` for policy forms or equilibrium regions, `establish` for theorems and guarantees, `bound` for approximation or regret, `estimate` for empirical designs, `identify` only when the design or model supports identification, and `validate` for numerical, empirical, or out-of-sample evidence.
- Choose collocations, not dictionary synonyms. In OR/MS prose, a policy `improves` a metric, a theorem `establishes` a bound, an estimator `recovers` a latent object, data `record` behavior or `identify` variation, and a robustness check `preserves` sign and magnitude.
- Keep formal adjectives attached to an object and a condition. Terms such as `optimal`, `robust`, `tractable`, `adaptive`, `finite-sample`, `data-driven`, and `near-optimal` need a benchmark, metric, policy class, or assumption nearby.
- Put old or contextual information before new information. Keep the grammatical subject close to the verb. Prefer two clean sentences to one sentence that carries setting, gap, model, result, mechanism, and implication.
- Build each sentence around a working subject, verb, and object before adding qualifiers. A sentence that starts from `the analysis`, `the framework`, `the result`, or `this paper` often needs a more local subject: manager, platform, estimator, theorem, policy, queue, signal, treatment, benchmark, or proof.
- Avoid noun piles and preposition chains. Replace phrases such as "platform information disclosure strategy optimization framework" with the actual action: who discloses what, to whom, with what consequence, and under what condition.
- Keep punctuation quiet in polished prose. Do not use colons as a default way to announce claims, contributions, implications, proof ideas, or takeaways. Turn `The implication is: ...` and `Key result: ...` into ordinary sentences with a subject, verb, object, condition, and benchmark. Preserve colons only when they serve formal notation, definitions, assumptions, proof labels, tables, or venue-required structure.
- Avoid itinerary prose. Do not default to `we first...`, `we then...`, `finally...`, or perfectly parallel contribution sentences unless the section is explicitly a roadmap. In polished prose, let the order follow the research objects: setting, friction, method, result, mechanism, boundary, or benchmark.
- Make the story elegant by giving the reader a turn, not by adding flourish. A good MS paragraph often moves from an existing practice, belief, model, or benchmark to the friction that changes the question, then to the method or result that resolves that friction. Use quiet hinges such as `but`, `whereas`, `when`, `because`, `relative to`, `rather than`, and `consistent with` only when they express a real relation.
- For native phrasing requests, lean on original-paper close reading, not only abstract-frequency patterns. Use broad corpus signals to avoid odd wording, but let original introductions, model sections, theorem passages, and appendices decide the order, depth, and proof placement.
- Use full-text MS/OR rhythm rather than a fixed skeleton. Strong papers usually move from an operating object to the friction, then to the formal or empirical move that resolves it. Headings name objects or reader jobs (`Model and Preliminaries`, `Fluid Model`, `Empirical Strategy`, `Accuracy Loss`, `Main Results`) rather than slogans.
- Treat "story" as persuasion order. A paragraph is good when the reader can see why the next object must appear: a benchmark creates a comparison, a constraint creates the theorem, a design rules out an alternative, or a proof move controls the difficult term.
- Treat paragraph order as a sequence of reader states. A section should not merely contain the right parts; it should move from setting to friction, friction to method, method to evidence, evidence to mechanism, and mechanism to boundary in the order the lane requires.
- Treat section order as a sequence of unresolved reader questions. Mechanism follows a main effect because the reader asks why; robustness follows a threat because the reader asks whether the effect survives it; a benchmark follows an equilibrium because the reader asks relative to what; an appendix proof follows body interpretation because the reader asks for verification after understanding the claim.
- Do not turn reference notes into slot-filled prose. If a sentence sounds assembled from actor, decision, friction, benchmark, mechanism, and implication labels, split it into ordinary sentences and keep only the relation the reader needs now.
- Avoid decorative three-part lists. Phrases such as `robust, scalable, and efficient framework` or `important, novel, and practical implications` often sound AI-generated unless the three items are real constructs, mechanisms, or result branches. Collapse them to the exact object or split them into separate claims with evidence.
- Avoid overcorrection. A passage can be idiomatic without sounding like every MS/OR convention has been applied. If the local claim is simple, use the simple sentence and stop.
- Let the prose sound like a researcher explaining the result to a careful coauthor. Use `we` naturally, keep the subject close to the verb, and allow plain links such as `because`, `so`, and `this means` when they state the relation more clearly than heavier academic phrasing.
- Make the register academic by making the logic more precise, not by making the words larger. Academic prose earns its formality through exact terms, calibrated verbs, explicit assumptions, measured claims, and complete inference chains.
- For translated-English drafts, rebuild the English logic: decision or object, friction, method or formal move, evidence, condition, implication.
- Let the story come from exact nouns and relations, not from story-like language. Avoid empty phrases such as "important implications," "novel framework," "rapidly evolving landscape," "underscores," "delve," and slogan-like final sentences.
- Preserve useful plain words. `Study`, `show`, `use`, `choose`, `price`, `bound`, and `compare` are often better than ornate substitutes. Do not write `utilize`, `facilitate`, `illuminate`, `showcase`, or `optimize decision-making` when the paper can name the decision, metric, policy, estimate, theorem, or benchmark.

## Reviewer Calibration

Assume the reviewer is a sharp expert in one nearby subfield, not an expert in every domain the paper touches. Write so that an OM reviewer can follow the econometrics, an empirical reviewer can follow the model, a theory reviewer can follow the institutional setting, and a domain reviewer can trust the formal language.

- Define overloaded terms locally before relying on them: `causal`, `optimal`, `equilibrium`, `robust`, `identification`, `efficiency`, `fairness`, `welfare`, `learning`, `platform`, and `data-driven`.
- Use the narrow term when it is available. Distinguish demand, arrival rate, purchase incidence, adoption, conversion, engagement, welfare, surplus, profit, and revenue.
- Explain what is observed, latent, exogenous, endogenous, optimized, estimated, assumed, or counterfactual when those distinctions matter.
- For cross-field papers, add one bridge sentence that maps the unfamiliar object into the reviewer's home vocabulary.
- In introductions, model sections, and result sections, write toward the skeptical reviewer's next question: why this setting, why this model or design, what identifies or proves the claim, and what alternative explanation has been ruled out or bounded.
- Before finalizing, ask what a skeptical but fair reviewer could misunderstand. If a claim might sound stronger than the evidence, narrow it.

## Section Registers

Use the register that matches the requested unit. These are flexible patterns, not mandatory templates.

- **Micro rewrite**: Fix object, verb, qualifier, and rhythm. Return one to three polished options only when alternatives are useful.
- **Abstract**: Move quickly from setting and decision to friction, model/data/design, headline result, validation or implication. Avoid broad hooks and generic final managerial sentences.
- **Manuscript judgment**: Before drafting a full section or paper, choose the durable object, central object, spine result, result hierarchy, model necessity, credibility path, reviewer objections, and body/appendix split.
- **Section architecture**: Do not assume one MS/OR skeleton. First classify the paper lane, then choose headings that name the object: `Research Setting`, `Data and Methods`, `The Model`, `Empirical Strategy`, `Main Results`, `Algorithm`, `Numerical Experiments`, `Robustness Tests`, or `Discussion and Conclusion`. Add subheadings only when the reader job, evidence object, construct, model component, theorem family, or validity threat changes.
- **Whole-manuscript optimization**: Improve the decision path before rewriting language: central object, result hierarchy, lane-specific structure, proof/model depth, appendix allocation, and only then sentence rhythm.
- **Introduction**: Start from the entry point the lane needs: decision setting, standard model, institutional puzzle, technical obstacle, or empirical construct. Order the modules so each paragraph answers the reviewer's next question; a roadmap is optional.
- **MS storycraft**: Treat story as persuasion order, not a fixed arc. Make the decision, standard view, friction, credibility support, result, mechanism, and boundary recoverable across the manuscript without forcing every paragraph to carry the whole chain.
- **Story-order repair**: For a paragraph or section that feels illogical, map start state, paragraph job, sentence sequence, exit state, and handoff to the next paragraph before changing wording.
- **Contribution paragraph**: Group by contribution type. Each contribution should name the object, the evidence or guarantee, and the precise departure from prior work.
- **Related work**: End each stream with the difference that matters: setting, information, constraint, performance criterion, proof technique, data source, or decision logic.
- **Citation and literature claims**: Do not invent citations, author-year pairs, DOI, page numbers, or claims about a paper. If exact citation content matters, use `citation-tools` or browsing and read the relevant content of the cited paper. In prose, each citation should support the nearest claim, and each cited stream should be followed by the paper's precise departure.
- **Model setup**: Describe the decision environment before dense notation. Introduce agents, timing, information, actions or policy class, objective, constraints, assumptions, benchmark, and solution concept or estimand in the order the paper lane requires.
- **Construct and empirical framework setup**: In empirical or experimental papers, a measure, construct, potential outcome, treatment contrast, or estimating equation may be the model. Define what the construct means, how it is observed or elicited, and what the coefficient or contrast represents before polishing the prose.
- **Assumptions**: State what role each assumption plays: simplify, identify, bound, preserve tractability, isolate a mechanism, rule out degeneracy, or match institutional constraints.
- **Result interpretation**: State the formal result or local claim, then explain what changes relative to the benchmark and why the condition matters for the decision.
- **Empirical or numerical results**: Separate what is observed, what is estimated or simulated, what is counterfactual, and what the design or model can support.
- **Managerial implications**: Recommend action only conditionally. Name who acts, what changes, when it works, and why it can fail if those details are supported.
- **Referee responses**: Be precise, modest, and auditable. Separate completed revisions from promised revisions, and avoid arguing beyond the evidence.

## Model, Equation, And Proof Writing

For model and mathematical writing, the body should establish the object, not merely point to the appendix.

- Before a display, say what the display defines, relaxes, decomposes, bounds, or estimates. After the display, translate the central variables and explain why the display is used next.
- A main-text model passage usually needs the decision environment, timing, information, action or policy class, objective, key constraints, assumptions, benchmark, and solution concept.
- In empirical papers, the body may instead need construct definitions, measurement logic, treatment/control contrast, identifying variation, outcome definition, estimand, and coefficient interpretation. Do not force theorem vocabulary onto this lane.
- A main-text derivation usually needs only three levels: starting formal object, load-bearing mathematical move, and resulting object used by the theorem, estimator, policy, or comparison.
- A theorem paragraph should name the result type: existence, uniqueness, monotonicity, threshold structure, comparative static, approximation ratio, regret bound, convergence rate, welfare comparison, or identification result.
- Theorem and proposition captions should be spare. Prefer `Proposition 1.` or a short parenthetical/object label when useful; do not attach long claim-like titles. Surround the result with ordinary prose rather than headings such as `Key Insight`, `Proof Idea`, or `Takeaway`.
- Use a `Proof.` paragraph directly below a theorem or proposition only when the body contains a complete, short proof that helps the reader understand the result. If the body only gives intuition or a proof sketch, write it as ordinary explanatory prose and point to the appendix for the complete proof.
- After a theorem or proposition, do not rush to the appendix. First give the formal result a reader-facing sentence: what object is characterized, what benchmark changes, or why the condition matters. If the proof is long, add at most one load-bearing proof move before the appendix pointer.
- A proof idea in the body should name the constructed object, the hard term, and the mathematical move that controls it. Use plain proof verbs: construct, decompose, bound, compare, apply, combine, show, and imply.
- Keep proof ideas proportional. If the proof is routine, one precise sentence may be enough; if the result looks surprising or methodologically important, give the checkpoint that prevents the theorem from feeling like a black box.
- Do not write "by some algebra" or "standard arguments" unless the step is genuinely routine. Name the actual move: exchange argument, coupling, convexity, submodularity, KKT conditions, duality, fixed point, martingale concentration, induction, envelope argument, or contradiction.
- The appendix proof verifies the body; it should not carry the first explanation of what the theorem means. Start with fixed objects and assumptions, signpost long algebra, and map the final technical statement back to the body result.
- For empirical appendices, keep variable dictionaries, balance checks, alternative codings, placebo tests, repeated specifications, and secondary robustness tables there after the body states the measure, identification logic, and conclusion.

## Body Versus Appendix

Decide placement by reader job, not by length alone.

- Keep in the body: headline results, main theorem statements, preferred empirical estimates, primary numerical comparisons, central figures, key assumptions, benchmarks, result interpretations, and proof ideas needed for first-pass trust.
- Move to appendix or online supplement: long algebra, constants, KKT verification, repeated cases, auxiliary lemmas, secondary robustness checks, parameter sweeps, implementation details, data dictionaries, and replication materials.
- Every appendix pointer that supports a claim should be conclusion-first: the body states the result, interpretation, proof checkpoint, or robustness conclusion before sending the reader to the appendix. Fold this into natural prose rather than exposing labels such as "handoff" or "proof checkpoint."
- Organize appendices by proof dependency or reviewer concern, not by what was easiest to cut. A good appendix section has one job: verify a theorem, define notation, document calibration, stress-test a claim, or report secondary scope.
- Keep robustness in the body when it protects the main identification, feasibility, or validity claim. Move repeated or secondary robustness checks to the appendix.
- For focused technical Operations Research papers, do not hide essential proof material in an online supplement. Use a regular appendix for verification details.
- When the user gives rough proof notes and asks for 正文/附录, first create the split internally, then write a natural main-text passage and a complete appendix passage. Do not stop at a meta-outline unless asked.

## Reference Routing

Load the smallest bundle that can solve the request. One bundle is the default; add another only when the task crosses language, story, math/proof, placement, or reviewer-calibration boundaries.

For mixed or ambiguous requests, use `triage_request.py` first and then load only the first one or two bundles it recommends.

References are for fixing a specific failure mode, not for decorating the answer with more conventions. If a request asks how papers actually do something, start with the full-text close-reading or lane reference that matches the unit, then add language references only if the resulting prose still sounds unnatural.

When the problem is simply "this sounds strange" or "the wording is not native," load `msor-word-choice-collocations.md` and `msor-sentence-craft.md` first, then `msor-natural-prose.md` only if paragraph flow is also the problem. Too many references can pull the draft back toward checklist prose.

- **Word choice, collocation, and translated-English repair**: `references/msor-word-choice-collocations.md` + `references/msor-sentence-craft.md` + `references/msor-natural-prose.md`.
- **Natural wording and micro-phrasing**: `references/msor-word-choice-collocations.md` + `references/msor-sentence-craft.md` + `references/msor-natural-prose.md` + `references/msor-micro-phrasing.md` + `references/management-science-language-rhythm.md` + `references/msor-language-model-math.md` + `references/msor-full-text-close-reading.md`.
- **Manuscript judgment and paper spine**: `references/msor-manuscript-judgment.md` + `references/high-impact-msor-paper-patterns.md` + `references/management-science-whole-paper-storycraft.md` + `references/section-architecture.md` + `references/msor-paper-craft.md`.
- **Whole-section story**: `references/msor-manuscript-judgment.md` + `references/high-impact-msor-paper-patterns.md` + `references/management-science-whole-paper-storycraft.md` + `references/section-architecture.md` + `references/msor-paper-craft.md`.
- **Story logic, paragraph order, and section flow**: `references/management-science-whole-paper-storycraft.md` + `references/paragraph-style.md` + `references/msor-natural-prose.md` + `references/section-architecture.md`.
- **Model, theorem, equation, proof**: `references/msor-word-choice-collocations.md` + `references/msor-sentence-craft.md` + `references/management-science-model-proof-equation-layout.md` + `references/math-model-main-appendix-craft.md` + `references/paper-appendix-paired-patterns.md` + `references/math-and-proof-style.md` + `references/msor-full-text-close-reading.md`.
- **Body versus appendix**: `references/main-text-appendix-placement.md` + `references/paper-appendix-paired-patterns.md` + `references/math-model-main-appendix-craft.md`.
- **Reviewer calibration**: `references/reviewer-calibration.md` plus the relevant language, empirical, or math bundle.
- **Citation discipline and related-work support**: `references/citation-close-reading.md` + `references/msor-paper-craft.md` + `references/academic-style-and-ai-writing.md` + `citation-tools` or browsing when exact citation metadata, cited-by counts, BibTeX, DOI, author-year verification, or cited-paper content matters.
- **Paper-lane flavor**: `references/management-science-20x-lane-style.md` or `references/article-corpus-style-notes.md` only for difficult lane matching, complete sections, or requests to make a passage feel closer to recent MS/OR papers without copying personal style.
- **Classic or high-impact MS/OR paper pattern**: `references/high-impact-msor-paper-patterns.md` plus the relevant story, model/proof, empirical, or appendix bundle. Use this for "high-cited," "classic," "seminal," "excellent paper," "Nature-style writing core," or requests to learn how strong papers persuade reviewers.
- **General story or unfamiliar topics**: `references/general-topic-story-engine.md`, `references/storytelling-language.md`, and `references/paragraph-style.md`.
- **Detailed corpus/style archives**: `references/msor-word-choice-collocations.md`, `references/msor-sentence-craft.md`, `references/msor-natural-prose.md`, `references/msor-micro-phrasing.md`, `references/msor-full-text-close-reading.md`, `references/management-science-language-corpus.md`, `references/expanded-or-ms-language-corpus.md`, `references/or-ms-disciplinary-spine.md`, and `references/academic-style-and-ai-writing.md` for difficult diagnosis, corpus-level language calibration, micro-wording, readability, or AI-scent repair.
- **Xiao Lei / digital platform / pricing / social operations flavor**: `references/xiao-lei-patterns.md` plus a topic/story or language bundle, while avoiding personal-style imitation.

## Script Use

Use scripts for planning or diagnostics, not as visible prose formats.

```bash
python3 /Users/mingfeijiang/.codex/skills/or-ms-writing/scripts/triage_request.py --target TARGET --request "REQUEST" < draft.txt
python3 /Users/mingfeijiang/.codex/skills/or-ms-writing/scripts/plan_section.py --section SECTION --target TARGET --topic "TOPIC"
python3 /Users/mingfeijiang/.codex/skills/or-ms-writing/scripts/plan_manuscript.py --target TARGET < notes.txt
python3 /Users/mingfeijiang/.codex/skills/or-ms-writing/scripts/place_results.py --target TARGET --paper-type "regular" < results.txt
python3 /Users/mingfeijiang/.codex/skills/or-ms-writing/scripts/plan_math_split.py --target TARGET --paper-type "regular" < proof_notes.txt
python3 /Users/mingfeijiang/.codex/skills/or-ms-writing/scripts/check_paragraph.py --fail-on-ai-scent < draft.txt
```

Run `triage_request.py` when the task could be language, manuscript structure, math/proof, placement, or reviewer calibration and the order matters. Run `plan_manuscript.py` when the user gives multiple results, data facts, model components, or proof notes and the real question is what the paper should emphasize. Run `plan_section.py` only for section-level or structurally unclear tasks; use `--section headings` when deciding section depth or subheading names. Run `place_results.py` when the user gives a list of results, tables, proofs, robustness checks, extensions, or figures. Run `plan_math_split.py` for rough proof/model notes, derivations, formula layout, or body-versus-appendix decisions. Run `check_paragraph.py` only after drafting or when diagnosing a passage.

## Stable Procedure

Use this as a control loop, not a visible outline. Stop when the requested unit is genuinely handled.

1. **Scope**: identify the unit, lane, reader job, and output shape. If unclear, triage once and load at most one or two reference bundles.
2. **Reader path**: decide what the reader knows at entry, what must change, what question the paragraph or section answers, and what next object it prepares.
3. **Evidence and placement**: identify the theorem, estimate, table, proof move, benchmark, assumption, design feature, or cited-paper content that supports the claim. For manuscript-level work, identify the portable object that a later paper would cite. For model or proof material, decide body versus appendix before writing formulas.
4. **Draft**: write ordinary OR/MS prose at the requested granularity. Do not expose planning labels, scripts, or reference terminology.
5. **Preserve**: keep evidence type, comparator, magnitude, policy class, assumption, benchmark, and validity condition no stronger than the supplied material.
6. **Calibrate**: narrow overloaded terms, bridge unfamiliar methods for adjacent-field reviewers, and keep evidence and boundary near claims that could be overread.
7. **Polish language**: fix collocations, prepositions, local subjects, working verbs, sentence stress, relation words, and academic register. Prefer exact plain words to ornate synonyms.
8. **Remove residue**: delete checklist rhythm, colon-led roadmaps, itinerary prose, weak `This enables/allows` links, abstract noun piles, and appendix pointers that arrive before interpretation.
9. **Genre check**: compare the passage with the relevant full-text MS/OR pattern: empirical design, construct measurement, model setup, theorem interpretation, proof placement, result narration, or appendix handoff.
10. **Read aloud**: if the prose would sound odd in a seminar or coauthor conversation, rebuild it around the local object, action, condition, and benchmark.

## If The Draft Feels Weird

Repair by simplifying the operating logic, not by adding more genre markers.

- If it sounds like a checklist, remove one beat and give the paragraph one dominant job.
- If it contains a three-item list of abstract adjectives or nouns, ask whether the three items are analytically distinct. If not, replace the list with one exact object, metric, mechanism, or condition.
- If it sounds mechanically "OR/MS," stop adding genre markers. Keep the paper's actual nouns and write the next sentence as the simplest answer to the reader's next question.
- If it uses colon-led labels such as `Contribution:`, `Key insight:`, `Result:`, `Proof idea:`, or `Implication:`, rewrite them as ordinary manuscript sentences or section headings only when the journal style truly calls for a heading.
- If it moves by `we first`, `we then`, and `finally`, replace the itinerary with the objects being studied, compared, or proved. Use roadmaps only when the reader needs navigation across a long section.
- If it starts with `This enables`, `This allows`, or a `which allows` clause, name the mechanism, theorem, design, or data object that does the work.
- If it becomes dry after removing AI-scent, do not add polish words. Add a precise turn: old belief versus new friction, benchmark versus result, mechanism versus alternative mechanism, or condition versus boundary.
- If it is hard to read, split before polishing. A smooth paragraph often needs three ordinary sentences where a draft tried to write one impressive sentence.
- If the sentence has a noun pile, turn one noun into the subject and another into the verb. Do not polish "decision-making framework" when the paper can say who chooses what.
- If the sentence sounds under-thought, do not polish it yet. Identify the premise, evidence, inference, and boundary; then write the sentence that connects the missing step.
- If the section feels illogical, ask what the reader knows at the end of each paragraph. Reorder paragraphs by reader state, not by the order in which the author did the work.
- If a paragraph feels illogical, give it one dominant job and order sentences as known object, new relation, evidence or formal object, interpretation, and handoff.
- If the prose sounds too informal, make it more academic by naming the construct, estimand, theorem object, policy class, assumption, or benchmark. Do not add ornate adjectives.
- If a sentence has many `of`, `for`, `in`, `with`, or `under` phrases before the verb, move the decision maker, policy, theorem, estimator, or metric to the front.
- If it sounds like a grant pitch, replace praise with the decision, metric, theorem, estimate, mechanism, or condition.
- If it sounds translated, rebuild the sentence around the English subject and verb rather than polishing word by word.
- If the wording is odd, check collocation before style. Replace `managerial enlightenment`, `optimize strategy`, `has important influence`, `leverage data`, and `provide insights` with the local action, metric, estimate, theorem, or policy.
- If the proof idea sounds stylized, replace metaphor and suspense with the constructed object, hard term, and proof move.
- If the model passage is symbol-heavy, add one plain sentence before notation that says who chooses what, with what information, and against what benchmark.
- If the result paragraph is vague, move the theorem, estimate, simulation comparison, or benchmark closer to the claim.
- If the appendix is carrying the paper, move the formal object, headline theorem, interpretation, and proof idea back into the body.
- If the body is too technical, move routine verification, constants, repeated cases, and auxiliary lemmas to the appendix.

## Quality Gate

Before finalizing, check only what the requested unit needs:

- The object, claim, evidence, and boundary are identifiable.
- The answer stays at the user's requested granularity and does not turn a sentence repair into a paper redesign unless the argument requires it.
- For manuscript-level work, the central object, spine result, credibility path, and result hierarchy are identifiable.
- For high-impact or full-paper work, the durable object, benchmark, support, and boundary are identifiable.
- The passage does not overstate causality, optimality, robustness, dominance, magnitude, or generality.
- Each inference has a visible premise or evidence object and does not skip from result to implication.
- Paragraphs and sections have story-order logic: the first sentence establishes the local job, the middle develops one object, and the last sentence either interprets or hands off.
- New sections enter because a previous result, model object, empirical threat, or reviewer concern has made them necessary.
- The register is academic without being inflated: formal where precision requires it, plain where plain field language is clearer.
- Technical terms use field-accepted meanings and are defined when overloaded.
- Model passages make agents, timing, information, actions, objective, constraints, assumptions, benchmark, and solution concept clear when relevant.
- Result and proof passages state the formal object, result type, assumption or benchmark, interpretation, and proof idea at the right depth.
- Headings, subheadings, and paragraph order match the paper lane and the reader's persuasion path, not a generic MS/OR outline.
- Body/appendix placement lets a reviewer understand and evaluate the contribution without opening the appendix, while leaving routine verification out of the body.
- The language is concrete, calm, and insertable. It does not expose scaffolding, overuse colon-led roadmaps, semicolon chains, dash pivots, AI-associated filler, or perfectly symmetric list rhythm.
- Three-part lists are used only when the items are genuine constructs, mechanisms, result branches, or assumptions; decorative adjective/noun triplets are removed.
- Word choices are idiomatic for the object: effects are `on` outcomes, robustness is `to` specifications, policies improve metrics `relative to` benchmarks, and evidence verbs do not exceed the support.
- Citation and related-work claims are bounded: no invented references, no citation dumping, and no novelty claim without a precise literature stream, benchmark, or verified citation support.
- Citation fit has been checked against the cited paper's actual content when the sentence relies on that paper; if the paper was not read, mark the citation support as unverified instead of polishing around it.
- Sentences have local subjects and working verbs. They avoid abstract-noun stacks, long preposition chains, weak `This` openings, and relation words that do not name a real condition, benchmark, mechanism, or boundary.
- The paragraph can be read aloud without sounding like a template. Each sentence inherits one object from the prior sentence and adds one new object, relation, or caveat.

## Default Style

Prefer analytical calm over rhetorical force. Use ordinary sentences, concrete nouns, exact evidence verbs, and bounded claims. Make the same data, model, theorem, or design sound better by improving object, order, mechanism, and qualifier, not by strengthening the conclusion.

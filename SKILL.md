---
name: or-ms-writing
description: "Use for idiomatic, reviewer-calibrated OR/MS and adjacent academic writing at any granularity: sentence-level rewrites, phrases, titles, abstracts, paragraphs, introductions, contribution statements, related work, model/data/result narration, theorem intuition, proof exposition, managerial implications, referee responses, and full paper sections for Management Science, Operations Research, M&SOM, OM, econ, business analytics, mechanism, empirical, learning, and policy work; uses INFORMS genre patterns and Xiao Lei paper-pattern references without imitating a living author's personal style."
---

# OR/MS Paper Writing

Use this skill to write or revise publication-style research prose for Management Science, Operations Research, M&SOM, and adjacent OR/MS, OM, economics, empirical, learning, policy, and business analytics work. The requested unit may be a phrase, sentence, title, abstract, paragraph, local section, model setup, theorem interpretation, proof idea, appendix proof, referee response, or full paper section.

## Boundaries

- Do not mimic a living scholar's personal wording, cadence, or distinctive voice. Use field-level conventions and paper architecture only.
- Do not hide missing logic in polished prose. If a theorem, proof step, identification claim, benchmark, or empirical support is absent, write the strongest supported version and flag the gap only when it affects validity.
- Do not upgrade evidence. A rewrite may clarify, narrow, reorder, and sharpen, but it must not invent significance, dominance, causality, optimality, robustness, generality, data, assumptions, or magnitudes.
- For proof discovery or failed lemmas, route to `theory-proof-workbench`. For a mostly complete but rough proof, pair with `math-proof-writing`.

## Default Behavior

Write the requested text first. Use diagnosis, maps, script labels, and checklists only when the user asks for planning, organization, or debugging.

Internally run only three silent passes unless the task is long or structurally unclear:

1. **Lane and reader job**: Is this empirical, structural, theory, algorithmic, applied OR, or hybrid, and what does the reviewer need next?
2. **Claim-evidence-boundary**: What is the claim, what supports it, and under what assumption, benchmark, data regime, model class, or population is it valid?
3. **OR/MS language rhythm**: Are the actor, decision, formal object, evidence verb, and implication stated in ordinary field language without checklist residue?

Treat every reference, script, and blueprint as a reader test, not a template. Do not force a passage to mention every possible element. If the user asks for one sentence, write one sentence. If the user asks for a paragraph, make one paragraph do one job. If the user gives Chinese or mixed notes, translate the intended argument, not the syntax.

## Writing Kernel

Use this kernel by default, but keep it invisible in the final prose.

- Start from what the paper actually proves, estimates, simulates, or demonstrates; then choose only the motivation and contrast needed to make that contribution legible.
- Make the paper's source of credibility visible before leaning on the claim: experiment, institutional variation, theorem, identification argument, equilibrium characterization, approximation guarantee, construct validation, simulation benchmark, or robustness logic.
- Make decisions, mechanisms, and formal objects concrete. Prefer "the platform chooses disclosure precision" to "disclosure precision is considered."
- Use exact evidence verbs: `characterize` for policy forms or equilibrium regions, `establish` for theorems and guarantees, `bound` for approximation or regret, `estimate` for empirical designs, `identify` only when the design or model supports identification, and `validate` for numerical, empirical, or out-of-sample evidence.
- Keep formal adjectives attached to an object and a condition. Terms such as `optimal`, `robust`, `tractable`, `adaptive`, `finite-sample`, `data-driven`, and `near-optimal` need a benchmark, metric, policy class, or assumption nearby.
- Put old or contextual information before new information. Keep the grammatical subject close to the verb. Prefer two clean sentences to one sentence that carries setting, gap, model, result, mechanism, and implication.
- For translated-English drafts, rebuild the English logic: decision or object, friction, method or formal move, evidence, condition, implication.
- Let the story come from exact nouns and relations, not from story-like language. Avoid empty phrases such as "important implications," "novel framework," "rapidly evolving landscape," "underscores," "delve," and slogan-like final sentences.
- Preserve useful plain words. `Study`, `show`, `use`, `choose`, `price`, `bound`, and `compare` are often better than ornate substitutes.

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
- **Section architecture**: Do not assume one MS/OR skeleton. First classify the paper lane, then choose headings that name the object: `Research Setting`, `Data and Methods`, `The Model`, `Empirical Strategy`, `Main Results`, `Algorithm`, `Numerical Experiments`, `Robustness Tests`, or `Discussion and Conclusion`. Add subheadings only when the reader job, evidence object, construct, model component, theorem family, or validity threat changes.
- **Introduction**: Start from the entry point the lane needs: decision setting, standard model, institutional puzzle, technical obstacle, or empirical construct. Order the modules so each paragraph answers the reviewer's next question; a roadmap is optional.
- **MS storycraft**: Treat story as persuasion order, not a fixed arc. Make the decision, standard view, friction, credibility support, result, mechanism, and boundary recoverable across the manuscript without forcing every paragraph to carry the whole chain.
- **Contribution paragraph**: Group by contribution type. Each contribution should name the object, the evidence or guarantee, and the precise departure from prior work.
- **Related work**: End each stream with the difference that matters: setting, information, constraint, performance criterion, proof technique, data source, or decision logic.
- **Model setup**: Describe the decision environment before dense notation. Introduce agents, timing, information, actions or policy class, objective, constraints, assumptions, benchmark, and solution concept or estimand in the order the paper lane requires.
- **Assumptions**: State what role each assumption plays: simplify, identify, bound, preserve tractability, isolate a mechanism, rule out degeneracy, or match institutional constraints.
- **Result interpretation**: State the formal result or local claim, then explain what changes relative to the benchmark and why the condition matters for the decision.
- **Empirical or numerical results**: Separate what is observed, what is estimated or simulated, what is counterfactual, and what the design or model can support.
- **Managerial implications**: Recommend action only conditionally. Name who acts, what changes, when it works, and why it can fail if those details are supported.
- **Referee responses**: Be precise, modest, and auditable. Separate completed revisions from promised revisions, and avoid arguing beyond the evidence.

## Model, Equation, And Proof Writing

For model and mathematical writing, the body should establish the object, not merely point to the appendix.

- Before a display, say what the display defines, relaxes, decomposes, bounds, or estimates. After the display, translate the central variables and explain why the display is used next.
- A main-text model passage usually needs the decision environment, timing, information, action or policy class, objective, key constraints, assumptions, benchmark, and solution concept.
- A main-text derivation usually needs only three levels: starting formal object, load-bearing mathematical move, and resulting object used by the theorem, estimator, policy, or comparison.
- A theorem paragraph should name the result type: existence, uniqueness, monotonicity, threshold structure, comparative static, approximation ratio, regret bound, convergence rate, welfare comparison, or identification result.
- Use a `Proof.` paragraph directly below a theorem or proposition only when the body contains a complete, short proof that helps the reader understand the result. If the body only gives intuition or a proof sketch, write it as ordinary explanatory prose and point to the appendix for the complete proof.
- A proof idea in the body should name the constructed object, the hard term, and the mathematical move that controls it. Use plain proof verbs: construct, decompose, bound, compare, apply, combine, show, and imply.
- Keep proof ideas proportional. If the proof is routine, one precise sentence may be enough; if the result looks surprising or methodologically important, give the checkpoint that prevents the theorem from feeling like a black box.
- Do not write "by some algebra" or "standard arguments" unless the step is genuinely routine. Name the actual move: exchange argument, coupling, convexity, submodularity, KKT conditions, duality, fixed point, martingale concentration, induction, envelope argument, or contradiction.
- The appendix proof verifies the body; it should not carry the first explanation of what the theorem means. Start with fixed objects and assumptions, signpost long algebra, and map the final technical statement back to the body result.

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

- **Native wording**: `references/management-science-language-rhythm.md` + `references/msor-language-model-math.md`.
- **Whole-section story**: `references/management-science-whole-paper-storycraft.md` + `references/section-architecture.md` + `references/msor-paper-craft.md`.
- **Model, theorem, equation, proof**: `references/management-science-model-proof-equation-layout.md` + `references/math-model-main-appendix-craft.md` + `references/paper-appendix-paired-patterns.md` + `references/math-and-proof-style.md`.
- **Body versus appendix**: `references/main-text-appendix-placement.md` + `references/paper-appendix-paired-patterns.md` + `references/math-model-main-appendix-craft.md`.
- **Reviewer calibration**: `references/reviewer-calibration.md` plus the relevant language, empirical, or math bundle.
- **Paper-lane flavor**: `references/management-science-20x-lane-style.md` or `references/article-corpus-style-notes.md` only for difficult lane matching, complete sections, or requests to make a passage feel closer to recent MS/OR papers without copying personal style.
- **General story or unfamiliar topics**: `references/general-topic-story-engine.md`, `references/storytelling-language.md`, and `references/paragraph-style.md`.
- **Detailed corpus/style archives**: `references/management-science-language-corpus.md`, `references/expanded-or-ms-language-corpus.md`, `references/or-ms-disciplinary-spine.md`, and `references/academic-style-and-ai-writing.md` for difficult diagnosis, corpus-level language calibration, or AI-scent repair.
- **Xiao Lei / digital platform / pricing / social operations flavor**: `references/xiao-lei-patterns.md` plus a topic/story or language bundle, while avoiding personal-style imitation.

## Script Use

Use scripts for planning or diagnostics, not as visible prose formats.

```bash
python3 /Users/mingfeijiang/.codex/skills/or-ms-writing/scripts/plan_section.py --section SECTION --target TARGET --topic "TOPIC"
python3 /Users/mingfeijiang/.codex/skills/or-ms-writing/scripts/place_results.py --target TARGET --paper-type "regular" < results.txt
python3 /Users/mingfeijiang/.codex/skills/or-ms-writing/scripts/plan_math_split.py --target TARGET --paper-type "regular" < proof_notes.txt
python3 /Users/mingfeijiang/.codex/skills/or-ms-writing/scripts/check_paragraph.py --fail-on-ai-scent < draft.txt
```

Run `plan_section.py` only for section-level or structurally unclear tasks; use `--section headings` when deciding section depth or subheading names. Run `place_results.py` when the user gives a list of results, tables, proofs, robustness checks, extensions, or figures. Run `plan_math_split.py` for rough proof/model notes, derivations, formula layout, or body-versus-appendix decisions. Run `check_paragraph.py` only after drafting or when diagnosing a passage.

## Stable Procedure

1. Identify the requested unit and write at that granularity.
2. Choose one reference bundle only if the task needs it.
3. For full sections or manuscripts, classify the evidence lane before choosing headings, subheadings, or paragraph order.
4. For long, mathematical, or cross-field tasks, decide reader job, support type, and boundary before drafting.
5. Draft ordinary OR/MS prose. Do not expose prewriting labels.
6. For model or proof material, decide the body/appendix split before writing formulas or proof text.
7. Run the evidence-preservation pass: keep evidence type, comparator, magnitude, policy class, assumption, benchmark, and validity condition no stronger than the user's material.
8. Run the reviewer-calibration pass: define overloaded terms, bridge unfamiliar methods, and narrow claims that could be overread.
9. Run the naturalness pass: split overloaded sentences, remove checklist residue, use exact verb-object pairs, and delete filler.

## If The Draft Feels Weird

Repair by simplifying the operating logic, not by adding more genre markers.

- If it sounds like a checklist, remove one beat and make the paragraph do one job.
- If it sounds like a grant pitch, replace praise with the decision, metric, theorem, estimate, mechanism, or condition.
- If it sounds translated, rebuild the sentence around the English subject and verb rather than polishing word by word.
- If the proof idea sounds stylized, replace metaphor and suspense with the constructed object, hard term, and proof move.
- If the model passage is symbol-heavy, add one plain sentence before notation that says who chooses what, with what information, and against what benchmark.
- If the result paragraph is vague, move the theorem, estimate, simulation comparison, or benchmark closer to the claim.
- If the appendix is carrying the paper, move the formal object, headline theorem, interpretation, and proof idea back into the body.
- If the body is too technical, move routine verification, constants, repeated cases, and auxiliary lemmas to the appendix.

## Quality Gate

Before finalizing, check only what the requested unit needs:

- The object, claim, evidence, and boundary are identifiable.
- The passage does not overstate causality, optimality, robustness, dominance, magnitude, or generality.
- Technical terms use field-accepted meanings and are defined when overloaded.
- Model passages make agents, timing, information, actions, objective, constraints, assumptions, benchmark, and solution concept clear when relevant.
- Result and proof passages state the formal object, result type, assumption or benchmark, interpretation, and proof idea at the right depth.
- Headings, subheadings, and paragraph order match the paper lane and the reader's persuasion path, not a generic MS/OR outline.
- Body/appendix placement lets a reviewer understand and evaluate the contribution without opening the appendix, while leaving routine verification out of the body.
- The language is concrete, calm, and insertable. It does not expose scaffolding, overuse colon-led roadmaps, semicolon chains, dash pivots, AI-associated filler, or perfectly symmetric list rhythm.

## Default Style

Prefer analytical calm over rhetorical force. Use ordinary sentences, concrete nouns, exact evidence verbs, and bounded claims. Make the same data, model, theorem, or design sound better by improving object, order, mechanism, and qualifier, not by strengthening the conclusion.

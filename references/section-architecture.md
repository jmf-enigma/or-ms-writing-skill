# Section Architecture

Use this when drafting full sections or deciding where a paragraph belongs.

## Journal Signals

- **Management Science**: broad management scope; papers must be readable, well organized, and well written. Contributions should connect scientific analysis to management practice or decision making.
- **Operations Research**: values methodological depth across optimization, stochastic modeling, simulation, decision analysis, markets/platforms/revenue management, data/software/computation, and application domains.
- **M&SOM**: operations-management audience. Structured abstracts should cover problem definition, methodology/results, and managerial implications. Main text should be rigorous and practice-relevant; footnotes are discouraged.

## Full Paper Skeleton

1. **Title**: name the decision, mechanism, or tradeoff; avoid slogan titles.
2. **Abstract**: problem, method/model, main results, implications.
3. **Introduction**: phenomenon, tension, gap, approach, findings, implications, roadmap.
4. **Related Literature**: organize by intellectual gap, not by citation chronology.
5. **Model / Setting / Data**: primitives, timing, decision maker, objective, assumptions, notation.
6. **Main Results**: propositions/theorems, interpretation, comparative statics, boundary conditions.
7. **Extensions / Robustness**: what changes, what survives, what the extension teaches.
8. **Numerical / Empirical / Simulation Evidence**: design, benchmark, metric, result, interpretation.
9. **Managerial / Policy Implications**: action, condition, mechanism, caveat.
10. **Conclusion**: what was learned, where it applies, one or two future directions.
11. **Appendix / Online Supplement**: proofs, technical lemmas, extra robustness.

## Introduction Moves

1. Start from a real operational or market phenomenon.
2. Name the decision tension: efficiency vs fairness, revenue vs welfare, personalization vs regulation, engagement vs addiction, information vs manipulation, matching quality vs waiting time.
3. State the standard intuition or industry default.
4. Explain why that intuition may fail once the hidden friction is present.
5. State why existing work does not resolve the tension.
6. Introduce the model or empirical design only after the problem is clear.
7. State results as mechanisms, not only as theorem numbers.
8. Translate results into managerial/policy implications with conditions.
9. Close with a concise roadmap.

## Reader-Order Rule

Each section should answer the reader's next question before introducing new machinery.

- Introduction: what decision is hard, why now, what is missing, what this paper changes.
- Model: who decides, what they observe, what they choose, what objective or constraint governs the choice.
- Results: what the theorem says, why it is true, when it applies, what it changes relative to a benchmark.
- Empirical or numerical section: what was measured, how the design identifies the object, what changes in the decision.
- Managerial section: who should act, when, why, and what boundary condition limits the advice.

## Topic Adaptation

Use `general-topic-story-engine.md` when the topic is outside platform pricing, digital markets, or social operations, or when the section could fit several genres. The local story should change with the topic, but the order remains stable. First classify the job as practice, theory, empirical, algorithm, policy, or review. Then start from the actor and decision, name the default or benchmark, introduce the hidden friction, and explain what the model, data, or algorithm changes.

## Abstract Patterns

- **M&SOM-style structured abstract**: Problem definition; Methodology/results; Managerial implications. Keep technical jargon low.
- **Management Science / OR compact abstract**: one sentence problem, one sentence model/method, two to three sentences findings, one sentence implication.

## Related Literature

Use two to four streams. For each stream: what it studies, what it misses for this paper, and how this paper differs. Avoid exhaustive summaries.

## Model Section

Order primitives before assumptions: agents, choices, information, timing, payoffs/objectives, constraints, equilibrium/solution concept, performance metrics. Explain assumptions after stating them; do not apologize for every abstraction.

## Results Section

For each result block: setup reminder, formal statement, intuition, implication, comparison to benchmark, limitation or condition. Put algebraic derivations and routine cases in the appendix.

## Main Text, Appendix, And Online Supplement

After results exist, organize by reader job.

- Main text is for first-pass understanding and contribution evaluation. Keep headline results, key theorem or proposition statements, preferred estimates, primary figures/tables, central algorithms, key assumptions, benchmark definitions, and result interpretations in the body.
- Regular appendix is for material that is required for verification but would interrupt the first pass: full proofs, auxiliary lemmas, routine algebra, KKT or induction details, extended derivations, and formal statements of secondary extensions.
- Online appendix or e-companion is for optional but useful support: secondary robustness checks, alternative specifications, parameter sweeps, extra datasets, data dictionaries, code details, computational settings, and replication notes.
- If a robustness check addresses the main threat to identification or validity, summarize it in the body and move the full table or repeated variants to the appendix.
- If an extension changes the main interpretation, give it a body paragraph. If it only shows scope, summarize the takeaway and move formulation and proof.
- Do not use the appendix as a substitute for interpretation. The body should still say why the result matters.

## Managerial Implications

Make implications conditional and operational: "When condition X holds, decision maker Y should do Z because mechanism M dominates benchmark B." Avoid generic "managers should consider..." sentences.

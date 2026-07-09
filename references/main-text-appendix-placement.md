# Main Text, Appendix, And Online Supplement Placement

Use this when results exist and the task is to decide what belongs in the paper body, a regular appendix, an online appendix or e-companion, a robustness section, or replication materials. The goal is to preserve the reader's first-pass understanding while keeping every claim verifiable.

## Source Signals

- Management Science expects succinct, directed papers and excludes the online appendix from revision page limits. This creates room for support material, but the main paper still has to focus on the contribution.
- Operations Research distinguishes appendices that are crucial for understanding from electronic companions that are optional supplemental material. For focused technical papers, proofs should be in the published paper rather than hidden in an EC.
- Operations Research's reproducibility policy treats mathematical proofs as publicly available either in the main body or appendix, and expects code, scripts, data, and reproduction instructions for algorithmic and empirical work when applicable.
- Recent Management Science papers typically keep the formal object, main theorem, central algorithm, identifying variation, headline empirical or numerical result, and main managerial interpretation in the body. They move notation tables, routine derivations, proof details, helper algorithms, extra datasets, alternative metrics, robustness checks, and finite-sample demonstrations of technical lemmas to online EC sections.
- Empirical MS papers often put the preferred design and headline estimates in the body, then use the online appendix for simulations validating estimator behavior, heterogeneity slices, cross-price or secondary effects, and alternative specifications that do not change the main claim.

## Placement Principle

The main text should let a careful reviewer understand and evaluate the contribution without opening the appendix. The appendix should let the same reviewer verify, reproduce, or stress-test the contribution.

Appendix placement works best when each appendix section has a named reviewer job:

- **Proof verification**: complete proof, helper lemmas, cases, constants, boundary regimes.
- **Mathematical derivation**: algebra that verifies a body transformation, such as a reformulation, reduction, or decomposition.
- **Notation and reproduction**: notation table, acronym list, data construction, code or replication statement, computational details.
- **Validity threat**: identification concern, model misspecification, feasibility concern, endogeneity check, benchmark alternative, or policy implementation concern.
- **Scope extension**: generalized primitives, relaxed assumptions, extra operational features, or secondary settings whose takeaway is already summarized in the body.

The body-to-appendix handoff should carry a conclusion. A cross-reference that does not say what the appendix verifies, preserves, or changes is usually too thin.

## Mathematical Body Depth

For mathematical models and proofs, placement is not only about length. It is about the reader's ability to evaluate the formal contribution before opening the appendix.

- The body should establish the model object: decision maker, timing, information, action or policy class, objective, core constraints, assumptions, benchmark, and solution concept or estimand.
- The body should include the main displayed formulation when that formulation defines the paper's decision problem, estimator, policy, relaxation, or benchmark.
- The body should show a derivation checkpoint when a transformation creates the object used later. Examples include primal to dual, Bellman equation to policy structure, original problem to relaxation, regret definition to decomposition, equilibrium constraints to reduced form, or identifying assumptions to an estimand.
- The body should not include the full algebra unless the algebra is short or the proof technique is the contribution.
- The body should interpret every headline theorem, estimator, or algorithm. Appendix cross-references cannot substitute for this interpretation.

If the main paper only says "see Appendix" after naming a theorem, the placement is wrong. If the main paper spends several pages verifying constants or cases before saying what the result means, the placement is also wrong.

## Keep In The Main Text

- The result named in the abstract, introduction, or contribution paragraph.
- The theorem, proposition, estimate, algorithm, or figure that supports the paper's main claim.
- Definitions, assumptions, information structure, benchmarks, and objectives needed to interpret the result.
- The main theorem statement or empirical specification, even if the proof or auxiliary tables move to the appendix.
- A proof idea when the proof technique is part of the contribution or when the theorem would otherwise feel like a black box.
- The primary table or figure that establishes the headline effect, guarantee, approximation, regret rate, welfare comparison, or managerial conclusion.
- Robustness checks that protect identification or validity. If omitting the check would make a fair reviewer doubt the claim, keep at least the logic or a compact result in the body.
- The main managerial or policy implication, stated with the condition under which it applies.

## Move To Appendix Or Online Supplement

- Routine algebra, long derivations, repeated case checks, KKT verification, concentration details, induction cases, and auxiliary lemmas.
- Complete proofs when the main text states the result and gives the proof roadmap.
- Notation tables, implementation details, pseudocode for helper routines, simulation design minutiae, parameter grids, and computational resource details.
- Secondary robustness checks, alternative specifications, extra datasets, alternative metrics, placebo tests, sensitivity analyses, and additional heterogeneity cuts.
- Extensions that show scope but do not change the central contribution.
- Examples or counterexamples that clarify boundary cases but are not needed for the first-pass argument.
- Replication materials, code, data dictionaries, and README files. Mention their existence in the paper when the journal requires a data/code statement.

## Borderline Cases

- A proof belongs in the body if the proof idea is the contribution, the paper is a focused technical paper, or the result is short enough that moving it would create more friction than clarity.
- A derivation belongs in the body if it defines the object the result later analyzes. The appendix can supply the missing algebra after the body gives the start point, key move, and resulting object.
- A general model belongs in the appendix if the baseline model in the body already carries the main mechanism and the appendix generalization only verifies scope. If the general model changes the main mechanism, keep its takeaway in the body.
- A partner-specific calibration belongs in the body only when it is needed to trust the headline comparison. Detailed demand estimation, lead-time fitting, decensoring, extra disruption scenarios, and parameter grids usually move.
- A stronger technical result belongs in the body if it is conceptually useful and the stated theorem is only a corollary or specialization. The proof can still move.
- A theorem with regions or thresholds needs a nearby body interpretation of the regions. A formal one-line proof pointer may intervene, but the local result package cannot end with the display and pointer alone.
- A robustness check belongs in the body if it addresses the most obvious alternative explanation, endogeneity concern, feasibility concern, or implementation failure mode.
- An extension belongs in the body if it changes how the reader interprets the main result. If it only shows that the result survives a variant, summarize it in the body and put details in the appendix.
- An additional empirical table belongs in the body if it is the first evidence for a mechanism or heterogeneity result claimed in the introduction. If it repeats the same conclusion across extra cuts, move it.
- A simulation belongs in the body when it tests the theorem's promise, compares the main benchmark, or provides the only evidence for performance. Parameter sweeps and extra metrics can move.

## Result Placement Map

When the user has several results, build this map before drafting or reorganizing.

For a quick first pass, run `scripts/place_results.py` on a one-item-per-line list of results. Treat the script output as a diagnostic draft, then adjust using reviewer judgment.

| Result | Evidence type | Reader job | Main-text role | Appendix role | Cross-reference |
|---|---|---|---|---|---|
| Main theorem or estimate | theorem, estimate, simulation, case study | believe the core contribution | statement, interpretation, key metric | proof, extra tables, derivations | "Proof is in Appendix A"; "additional robustness appears in Online Appendix EC.x" |
| Model formulation | optimization, dynamic program, estimator, equilibrium, mechanism | understand the object | decision environment, objective, constraints, assumptions, benchmark | notation table, variants, omitted verification | "Appendix A gives notation details and auxiliary variants" |
| Central derivation | relaxation, dual, Bellman transformation, regret decomposition, identification step | trust the formal object | start point, key move, resulting object | algebra, constants, case splits, lemmas | "Appendix B verifies the derivation and boundary cases" |
| Mechanism | comparative static, mediation, proof idea, heterogeneity | understand why | concise mechanism paragraph | extra decompositions or heterogeneity cuts | "Online Appendix EC.x reports the full decomposition" |
| General model | extension, generalized primitives, relaxed assumptions | understand scope | only the takeaway if mechanism changes | full generalized formulation and proof | "Appendix C shows the mechanism survives the general model" |
| Calibration or implementation | industry data, fitted distributions, decensoring, runtime | trust application | mapping to base model and primary comparison | estimation details, parameter grids, extra scenarios | "Online Appendix EC.x describes calibration and additional scenarios" |
| Robustness | alternative spec, placebo, parameter sweep | check validity | only validity-critical check | full robustness suite | "The remaining checks are in Online Appendix EC.x" |
| Extension | model variant, empirical variant | understand scope | one-paragraph takeaway if scope changes | formal model, proof, additional numerics | "The formal extension is in Appendix B" |

## Cross-Reference Language

- "We state the result here because it is the basis for the policy comparison. The proof is in Appendix A."
- "The argument has two steps. The main text gives the reduction; Appendix B verifies the algebraic cases."
- "The body derives the relaxation because it defines the benchmark used in Theorem 1. Appendix B contains the KKT verification."
- "Section 5 reports the primary comparison. Online Appendix EC.6 repeats the analysis on additional datasets and metrics."
- "Because this robustness check addresses the main identification concern, we report it in the body and leave the remaining checks to the online appendix."
- "The extension does not change the main mechanism, so we summarize it here and provide the full formulation and proof in Appendix C."
- "The online appendix reports the auxiliary baselines; all preserve the ranking in Table 2, so they do not change the interpretation of the preferred model."
- "Appendix B gives the closed-form thresholds used in the figure. The body focuses on the region boundaries because those boundaries drive the operating-mode comparison."

## Do Not Do This

- Do not hide the only evidence for a headline claim in the appendix.
- Do not send every proof to the appendix if the proof technique is itself the methodological contribution.
- Do not keep every robustness table in the body. A body crowded with secondary tables makes the main result harder to see.
- Do not cite the appendix as a substitute for interpreting the result. The body still needs a sentence saying what the result means.
- Do not put data and code availability in an appendix only if the target journal requires a main-text data/code statement.

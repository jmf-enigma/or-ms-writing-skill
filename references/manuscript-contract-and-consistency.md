# Manuscript Contract And Cross-Section Consistency

Use this for whole-paper drafting, revision, or pre-submission review. It checks whether the abstract, introduction, model or empirical design, results, and conclusion are different versions of the same paper rather than locally polished sections that make different promises.

This is not a fixed outline. Theory, empirical, structural, algorithmic, field-implementation, and hybrid papers can use different section orders. The invariant is the paper's substantive contract, not its headings.

## The Paper Contract

Audit seven fields before rewriting the manuscript. Mark a field as not applicable rather than inventing a comparator, mechanism, or decision consequence the paper does not claim.

1. **Central object**: the decision, market, system, construct, estimator, loss, benchmark, policy class, or theorem object the paper studies.
2. **Headline claim**: the most consequential result the evidence lets a knowledgeable reviewer state accurately.
3. **Comparator**: current practice, a standard model, an oracle, first-best, full information, a baseline policy, treatment control, or another explicit reference point.
4. **Metric or estimand**: profit, cost, welfare, regret, approximation ratio, treatment effect, conversion, error, or another precisely defined outcome.
5. **Credibility source**: theorem and proof, identification argument, randomized variation, construct validation, out-of-sample comparison, simulation benchmark, or field implementation.
6. **Boundary**: the assumption, policy class, sample, regime, information structure, parameter range, or implementation condition under which the claim is supported.
7. **Consequence or use, when supported**: whose decision changes, what later analysis becomes possible, or which accepted comparison the result revises.

The contract is not a slogan. Each applicable field must be recoverable from the paper's formal or empirical content. If the evidence supports only a local result, the contract must remain local.

## How Sections Transport The Contract

Sections should not repeat identical sentences. They perform different operations on the same objects.

- **Abstract** compresses the contract. It names the object, method or evidence, headline result, metric or comparator, and the boundary needed to prevent overreading.
- **Introduction** makes the contract legible and worth examining. It establishes whichever setting, standard benchmark, construct, counterexample, technical obstacle, or prior evidence is needed to interpret the paper's claim and credibility source.
- **Model or empirical design** operationalizes the contract. It defines the relevant subset of actors or system, timing, information, action, objective, comparator, estimand, construct, or identifying variation that the headline claim requires.
- **Results** discharge the contract. They state the formal or empirical support, preserve the exact comparator and metric, and separate the headline result from mechanism, robustness, and scope.
- **Conclusion** interprets the contract. It may broaden the relevance, but it cannot silently broaden the population, policy class, evidence type, or claim strength.
- **Appendix** verifies the contract. It supplies proof, construction, robustness, measurement, or implementation details without becoming the first place where the central object or support is intelligible.

## Contract Drift

Treat drift as material when it changes what the paper claims or what supports the claim.

- **Object drift**: the introduction studies demand prediction, the model optimizes inventory, and the conclusion claims a general decision-support system without showing the connection.
- **Comparator drift**: the theorem compares with a static policy, but the abstract says the method outperforms existing approaches.
- **Metric drift**: the results concern revenue, while the conclusion says profit or welfare.
- **Evidence drift**: a simulation result becomes empirical validation, or an observational association becomes a causal effect.
- **Boundary drift**: a result for affine policies, one platform, one parameter regime, or one sample becomes an unrestricted claim.
- **Magnitude drift**: percentages, confidence intervals, approximation factors, sample sizes, or theorem rates change across sections.
- **Mechanism drift**: evidence consistent with a mechanism becomes proof that the mechanism caused the result.
- **Terminology drift**: the same object receives decorative synonyms, or nearby but non-equivalent objects are treated as interchangeable.
- **Appendix dependence**: the body claims credibility from a test or proof whose conclusion is never stated outside the appendix.

Local variation is not drift. The abstract can say `pricing policy` where the model later gives the policy's formal name. The introduction can use a plain-language bridge before the canonical technical term. Once the object is defined, however, preserve the canonical term instead of rotating synonyms for style.

## Reviewer Knowledge Boundary

For each important object, decide what the target reviewer can reasonably be expected to know.

1. **Assume** field-standard material that is genuinely common to the likely reviewer pool.
2. **Bridge once** when an adjacent-field reviewer needs the object's real-world meaning, estimand, benchmark, or role in the argument.
3. **Defer verification** when the definition, derivation, or implementation is too technical for the body but is not needed for first-pass understanding.

Do not repeatedly explain a canonical term after defining it. Do not replace it with loose synonyms. A reviewer should be able to follow the trust chain from object, to role, to evidence, to boundary without learning an entire neighboring field.

## Section-To-Section Handoffs

A section should begin because the prior section has created a live question.

- A mechanism section follows a main effect because the reader asks why it occurs.
- A benchmark follows a policy or equilibrium because the reader asks relative to what.
- An approximation follows the exact problem because the reader now sees the computational obstacle.
- A stronger theorem follows an asymptotic result because the reader asks for a rate or finite-sample guarantee.
- A follow-up experiment follows a field effect because the initial design cannot isolate the mechanism.
- Robustness follows a named threat, not merely because robustness is conventional.
- An appendix follows interpretation because the reader is ready to verify the claim. A journal may place a one-line proof pointer immediately below a formal result, but that pointer does not replace the nearby interpretation.

Headings should name the object or question that changes, not announce generic rhetorical jobs. A sequence such as `Lower Bound`, `Base-Stock Policy`, and `Performance Guarantee` can expose the proof architecture. A sequence of experiment headings can expose the evidence architecture. Neither should be imposed on a paper with a different argument.

## Evidence Ownership

Every central claim needs an identifiable owner.

- A theorem owns a formal guarantee only under its assumptions and policy class.
- An experiment owns the treatment contrast generated by its randomization.
- An observational design owns the estimand supported by its identifying variation.
- A simulation owns performance in the tested instances and benchmark design.
- A field implementation owns feasibility and realized outcomes in that setting.
- A citation owns only the claim supported by the cited paper's relevant model, data, result, or proof, not everything suggested by its title.

When a sentence combines claims with different owners, split it. Keep each citation beside the proposition it supports, and verify citation fit from the cited paper's relevant full text rather than metadata or abstract alone.

## Audit Procedure

Use this order for a full-manuscript review.

1. Extract one contract sentence from each major section without rewriting it.
2. Compare central object, claim, comparator, metric, credibility source, boundary, and decision relevance.
3. Mark material drift separately from harmless compression or terminology bridges.
4. Check headline numbers, theorem conditions, benchmark names, treatment definitions, and claim-strength verbs across sections.
5. Identify which section owns each central claim and whether the cited, mathematical, or empirical support is visible there.
6. Repair architecture first: choose the canonical object, comparator, metric, evidence type, and boundary.
7. Rewrite local prose only after the contract is stable.
8. Read the abstract and conclusion back to back. The conclusion may add interpretation, not a stronger paper.

Use `scripts/audit_manuscript_contract.py` as a diagnostic inventory when the manuscript is available as text. Its flags are prompts for close reading, not automatic errors.

## Paper-Derived Patterns

Full-text MS/OR papers show several legitimate ways to carry a contract.

- A predictive-prescriptive paper can create a named decision loss or prescriptiveness metric, then let that object organize method, theory, and application.
- A revenue-management paper can define regret against a full-information benchmark and use that same quantity as both a theorem metric and the economic value of prior information.
- An applied implementation paper can spend substantial space on the operating workflow before notation when the workflow determines aggregation, decisions, and constraints.
- An empirical paper can use a sequence of experiments as the argument: establish the effect, separate nearby explanations, test the customer-side mechanism, then test the worker-side mechanism.
- An algorithmic paper can order contribution headings by proof dependency: lower bound, policy construction, then guarantee.
- A theory paper can develop two opposing effects before the theorem so that the formal condition resolves a visible economic tension.

These are examples of reader logic, not reusable surface templates.

## Final Questions

- Would a reviewer describe the paper's central object with the same noun after reading the abstract and the model?
- Does every comparative result name the same comparator, metric, and condition used by the supporting evidence?
- Does the conclusion preserve the evidence type and boundary of the results?
- Can an adjacent-field reviewer understand each consequential object after one local bridge?
- Can the body be evaluated without opening the appendix?
- Does each appendix section verify a body claim rather than introduce a new central claim?

# OR/MS Manuscript Judgment

Use this when the task is larger than a local polish: full paper sections, introductions, abstracts, result architecture, model narration, proof/body split, or any request where the same data/model/results should be turned into a stronger Management Science, Operations Research, or M&SOM manuscript. This reference is about author judgment before prose.

The goal is to decide what the paper is really about, what the reader must believe first, which result carries the contribution, and what should be demoted, moved, or deleted. Do this before sentence-level polishing.

## The Core Judgment

A strong OR/MS manuscript has a spine. The spine is not the method, the dataset, or the complete list of results. It is the smallest claim that changes how the reader understands a decision, model, mechanism, or policy class.

Before writing, identify:

- **Central object**: the decision, system, market, policy class, estimator, theorem object, or mechanism the paper is actually about.
- **Reader belief shift**: what a knowledgeable reviewer would believe before reading the paper and what the paper changes.
- **Spine result**: the theorem, estimate, algorithmic guarantee, mechanism evidence, or field comparison that carries the paper.
- **Credibility path**: the model, design, identification, proof, validation, or implementation evidence that makes the spine result believable.
- **Boundary**: the assumption, regime, data setting, policy class, population, or benchmark that prevents the claim from becoming too broad.

If these five objects are unclear, do not start by improving language. First narrow the paper.

## The Manuscript Contract

Once the spine is chosen, write down the paper's contract: central object, headline claim, comparator, metric or estimand, credibility source, boundary, and decision relevance. Carry that contract across the manuscript without forcing identical wording.

- The abstract compresses it.
- The introduction motivates why it is needed.
- The model or design defines its objects and support.
- The results discharge the claim at the stated metric and comparator.
- The conclusion interprets it without broadening the evidence or boundary.
- The appendix verifies it without becoming the first intelligible statement of the object or result.

Check for object, comparator, metric, evidence, magnitude, mechanism, and boundary drift before polishing sentences. For a detailed audit procedure, use `manuscript-contract-and-consistency.md`.

## Whole-Manuscript Optimization Pass

Use this pass when the user says the paper, section package, or writing system still feels "weird" after local polishing.

1. **Choose the lane before the outline**: empirical experiment, construct-measurement, structural/estimation, analytical theory, algorithm/OR, applied field implementation, or hybrid.
2. **Name the central object in ordinary language**: the decision, mechanism, estimator, theorem object, policy class, platform rule, or empirical construct.
3. **Choose the spine result**: the one theorem, estimate, field comparison, or guarantee that the abstract must remember.
4. **Order support by reviewer trust**: model/design first when it creates credibility, mechanism next when it changes interpretation, robustness only where it protects validity.
5. **Assign placement**: body for first-pass trust and interpretation; appendix for verification, repeated robustness, implementation, and data dictionaries.
6. **Only then polish sentences**: repair subject-verb-object, collocations, relation words, and read-aloud rhythm.

For a whole manuscript, add one final pass after sentence polish: read the abstract, headline result passage, and conclusion together and verify that they still make the same claim at the same strength.

This prevents a common failure mode: a section with good sentences but no persuasion order.

## Result Hierarchy

Classify results by reader job, not by the order in which they were produced.

- **Spine result**: the result the abstract and introduction must make memorable. It belongs in the body and gets the cleanest prose.
- **Load-bearing support**: a theorem, identification argument, validation, benchmark, or empirical contrast needed for first-pass trust. It belongs in the body near the claim it supports.
- **Mechanism result**: explains why the spine result holds. It belongs in the body if the mechanism changes interpretation; otherwise summarize and move details.
- **Boundary result**: says when the result strengthens, weakens, reverses, or stops applying. It usually belongs in the body when it prevents overclaiming.
- **Robustness result**: protects validity or implementation. Keep validity-critical checks in the body; put repeated checks in the appendix.
- **Scope extension**: shows generality under a variant. Put it in the body only if it changes the main interpretation.
- **Technical verification**: algebra, constants, repeated cases, auxiliary lemmas, computation details, data dictionaries, and implementation checks. These usually belong in the appendix.

Do not give all results equal rhetorical weight. If every result is introduced as important, the reader will not know what the paper contributes.

## Choosing The Spine Result

When several results look publishable, choose the one that best satisfies four tests.

1. **Decision relevance**: Does it change an action, policy, comparison, or formal decision?
2. **Credibility**: Can the paper support it with the strongest evidence, proof, or design?
3. **Surprise with discipline**: Does it depart from a standard benchmark without sounding like a slogan?
4. **Transport across sections**: Can the same object organize the abstract, introduction, model, results, and implication?

If a result is technically impressive but cannot organize the manuscript, it may be a supporting theorem. If a result is managerially attractive but weakly supported, it may be a discussion point rather than the spine.

## Model Necessity

A model section should feel inevitable. Each modeling choice must answer a reader question.

Ask:

- Which decision would be ill-defined without this primitive?
- Which theorem, estimator, or comparison uses this state variable?
- Which assumption isolates the mechanism rather than merely simplifying notation?
- Which benchmark is needed to interpret the result?
- Which feature is realistic but not load-bearing and can move to an extension or appendix?

A model passage is weak when it says all primitives accurately but does not explain why the model has this structure. A strong model passage makes timing, information, action, objective, and benchmark appear in the order the decision maker or proof needs them.

## Data And Result Architecture

For empirical, field, or hybrid papers, do not report tables in the order they were run. Put them in the order a skeptical reviewer needs.

Common order:

- What is observed, measured, or randomized?
- What comparison identifies or supports the main claim?
- What is the main effect or structural estimate?
- What mechanism or heterogeneity explains it?
- What alternative explanation is weakened?
- What boundary or implementation condition remains?

If the data are rich, resist describing richness for its own sake. Say which variation, granularity, timing, or measurement feature makes the main comparison possible.

For construct-measurement papers, the measure may be part of the contribution. Keep the construct definition, elicitation, validation logic, and primary measurement equation in the body when they make the result interpretable. Move only alternative codings, repeated validation checks, and long variable dictionaries to the appendix.

## Proof And Theory Architecture

For theory or algorithmic papers, decide what the body must show so the theorem does not feel like a black box.

Keep in the body:

- formal object and benchmark;
- theorem statement and result type;
- one proof idea if it reveals the mechanism or prevents reviewer distrust;
- the key decomposition, relaxation, coupling, lower bound, or policy comparison if later interpretation depends on it.

Move to appendix:

- constants, boundary cases, repeated induction, KKT verification, helper lemmas, concentration details, and algebra that verifies an already understood move.

The body should say why the theorem is true at the right level. The appendix should verify that it is true.

## Reviewer Simulation

Before drafting a full section, simulate three readers.

- **Home-field reviewer**: knows the method and asks whether the result is technically or empirically new enough.
- **Adjacent-field reviewer**: understands the management problem but not every tool; needs bridges from notation, identification, or proof to the decision.
- **Skeptical editor or AE**: asks why this belongs in MS/OR rather than being a competent application.

For each main claim, ask what the reader would object to:

- Is the claim stronger than the design or theorem?
- Is the benchmark the right one?
- Is the mechanism separated from a nearby alternative?
- Are assumptions doing real work?
- Does the result change a decision, or merely describe a pattern?
- Is the implication conditional enough to be credible?

Answer these questions in the paper, not in visible meta-commentary.

## What To Delete Or Demote

Better MS writing often comes from removing correct but nonessential material.

Delete or demote:

- a motivation paragraph that does not lead to the central object;
- a literature contrast that is true but not needed for the paper's departure;
- a model feature that is not used by the spine result;
- a robustness check that repeats the same reassurance;
- an implication that is not supported by a theorem, estimate, or field comparison;
- a theorem interpretation that restates the theorem without changing the reader's understanding.

When unsure, ask whether a reader would miss the item if it disappeared from the body. If not, move it to the appendix or remove it.

## Writing After Judgment

Only after the spine is chosen should prose begin.

Good drafting order:

1. Write one sentence for the central object.
2. Write one sentence for the friction or belief shift.
3. Write one sentence for the evidence object that makes the claim credible.
4. Write the spine result in the strongest accurate form.
5. Add only the boundary needed to prevent overreading.
6. Place supporting results around the spine, not before it.

The final text should not expose this scaffold. It should read as if the paper naturally moves from object to friction to evidence to result.

## Failure Modes

- **Result catalog**: every result is described, but no result carries the paper.
- **Method-first manuscript**: the model or estimator appears before the reader knows why it is needed.
- **Over-calibrated prose**: every claim has a caveat, making the contribution feel smaller than the evidence supports.
- **Under-calibrated implication**: the prose jumps from a local result to a broad recommendation.
- **Appendix-dependent body**: the reader cannot understand the formal object, theorem, or primary comparison without opening the appendix.
- **Reviewer mismatch**: the passage speaks to one subfield but leaves another likely reviewer without the bridge sentence they need.
- **Contract drift**: the abstract, model or design, results, and conclusion change the object, comparator, metric, evidence type, magnitude, or boundary.

Repair these by changing the manuscript architecture before rewriting sentences.

# OR/MS Natural Prose

Use this when the draft is technically correct but sounds stiff, assembled, translated, or difficult to read. The goal is not to make the prose casual. It is to make it sound like a careful researcher explaining the paper to another researcher. If the sentence itself is malformed, noun-heavy, or translated word by word, use `msor-sentence-craft.md` before using this paragraph-flow reference.

Do not copy source wording. Transfer the movement of the paragraphs: what the sentence takes as known, what it adds, and why the next sentence follows.

## Source Reading Notes

These notes come from recent INFORMS original pages and abstracts, with attention to paragraphs that read smoothly rather than merely sounding "academic."

- Garcia, Tolvanen, and Wagner, "Demand Estimation Using Managerial Responses to Automated Price Recommendations," Management Science, 2022.
- Kanazawa, Kawaguchi, Shigeoka, and Watanabe, "AI, Skill, and Productivity," Management Science, 2025.
- Brahm, Lafortune, Magelssen, and Tessada, "Collaboration, Workplace Practice Adoption, and Performance," Management Science, 2026.
- Li, Belo, and Li, "Can Reward Uncertainty Encourage Social Referrals?," Management Science, 2026.
- Bhandari and Russo, "Global Optimality Guarantees for Policy Gradient Methods," Operations Research, 2024.
- Crimmins, Halderman, and Sturt, "Improving the Security of United States Elections with Robust Optimization," Operations Research, 2024.
- Varma, Bumpensanti, Maguluri, and Wang, "Dynamic Pricing and Matching for Two-Sided Queues," Operations Research, 2022.
- Recent M&SOM Articles in Advance pages, especially structured abstracts for matching queues, hospital capacity, healthcare delivery, inventory networks, and service operations.

## What Smooth OR/MS Prose Does

Smooth paragraphs are usually simpler than our drafts.

- They start from a recognizable object, not from a label. The object may be a manager, platform, queue, recommendation system, voting procedure, algorithm, or worker.
- They move one step at a time. A sentence rarely tries to introduce the setting, model, benchmark, theorem, mechanism, and implication all at once.
- They make the reader's question change gradually. First the reader sees why the question matters, then why the usual answer is incomplete, then why the paper's object is the right one.
- They use ordinary verbs. `Use`, `show`, `find`, `compare`, `estimate`, `choose`, `allow`, and `depend on` often read better than ornate verbs.
- They let specifics do the work. A concrete variable, metric, comparison, or field setting is smoother than a polished abstract noun.
- They include caveats without sounding defensive. A limitation is placed near the claim and written in the same calm register as the result.

The prose should feel almost spoken at the level of logic: "Here is the object. Here is why the usual approach is not enough. Here is what we observe or prove. Here is what changes." The final sentence can still be formal, but the path to it should not feel mechanical.

## Overall Repair Order

When a whole passage or section feels wrong, do not fix everything at once. Work in this order:

1. **Local object**: what noun should the reader carry from one sentence to the next?
2. **Reader turn**: what new question does the next sentence answer?
3. **Evidence verb**: does the verb match the support: estimate, show, characterize, establish, suggest, validate?
4. **Boundary**: is the assumption, sample, benchmark, policy class, or regime close enough to the claim?
5. **Inference chain**: can the reader see how the sentence follows from the previous one?
6. **Sentence rhythm**: split long sentences, remove noun piles, and put the subject near the verb.
7. **Academic register**: replace casual evaluation with constructs, metrics, assumptions, benchmarks, or calibrated inference verbs.
8. **Field texture**: add only the OR/MS collocation that the object needs.

Stop when the paragraph reads like a researcher explaining the result. Do not keep adding genre markers after the logic is already clear.

Academic register should not make the paragraph heavier than its logic. A paragraph becomes more scholarly when it states the inference more exactly: what evidence supports the claim, what condition limits it, and what alternative interpretation remains.

## The Natural Paragraph Test

Before finalizing a paragraph, silently ask:

1. Could a researcher say the paragraph out loud in a seminar without sounding like they are reading a checklist?
2. Does each sentence inherit one object from the previous sentence?
3. Does each sentence add one new thing, not three?
4. Is the main verb close to the subject?
5. Does the paragraph use the paper's nouns instead of generic labels such as insight, implication, framework, mechanism, and contribution?
6. If a sentence uses `when`, `whereas`, `relative to`, `without`, or `consistent with`, is that relation the reason the sentence exists?
7. Could one clause be moved to the next sentence and make the paragraph easier to read?
8. Does any `A, B, and C` list merely decorate a noun? If yes, keep only the item that carries the claim, or split the items into separate evidence-backed claims.

If the answer to any of these is no, simplify before polishing.

## Common Source-Like Movements

These are paragraph movements, not templates.

### From Big Claim To Testable Setting

Several empirical MS papers begin with a broad claim only long enough to make the empirical test legible. The next sentence immediately says what data or setting would be needed to test the claim. The third sentence explains why the chosen context provides that evidence.

Use this movement when the paper studies AI, behavioral adoption, field interventions, or managerial response:

- broad claim or debate;
- the empirical object needed to test it;
- the setting that supplies the object;
- the measure or treatment that makes the setting credible.

Do not linger on the broad claim. The reader should reach the paper's data within a few sentences.

### From Existing Method To Missing Variation

Demand-estimation and empirical-strategy papers often sound smooth because the identification problem is explained before the method. They say why the usual source of variation is unavailable, then point to a behavioral or institutional feature that creates usable variation.

Movement:

- standard challenge;
- why the focal setting makes it harder;
- institutional or behavioral feature that solves part of the problem;
- estimator or model that uses that feature.

Avoid opening with the estimator unless the reader already knows the identification problem.

### From Practice To Optimization Object

Applied OR papers often begin with an existing operational procedure, show how it can fail, and then introduce optimization as a direct repair. The smoothness comes from making the procedure concrete before naming the formulation.

Movement:

- existing procedure or rule;
- practical vulnerability or cost;
- formal object that captures the vulnerability;
- guarantee, implementation, or field comparison.

This movement is useful for public-sector, healthcare, logistics, and platform papers because it keeps the mathematical object attached to a real operating decision.

### From Popular Method To Structural Guarantee

Technical OR/ML papers often start with a method that is already familiar, then name the specific theoretical discomfort. The theorem enters as a response to that discomfort, not as an isolated achievement.

Movement:

- method widely used;
- limitation in the known theory;
- structural property or condition;
- guarantee and examples.

Do not oversell the theorem as surprising unless the paper itself gives the reader the counterexample or failure mode.

### From Result To Boundary

Good result paragraphs often make a result readable by immediately saying where it does and does not operate. The boundary is not an afterthought; it prevents the claim from sounding too broad.

Movement:

- local result or estimate;
- metric or formal object changed;
- subgroup, regime, or condition;
- interpretation that stays within that condition.

## Sentence-Level Smoothness

### Prefer Inherited Subjects

Let the subject of a sentence come from the prior sentence when possible.

Stiff:

`The model isolates the channel by allowing demand learning to affect the sourcing decision, which provides an important implication for inventory management.`

Smoother:

`The model lets demand learning enter the first sourcing decision. This is the channel missing from the classic benchmark, where the demand distribution is fixed before ordering.`

### Split Before You Polish

If one sentence contains setting, friction, method, and result, split it.

Stiff:

`In a setting where managers delay the implementation of automated price recommendations, we develop an estimator that leverages this delay to recover price elasticities and show that it performs well relative to traditional approaches.`

Smoother:

`Managers in our setting often implement automated price recommendations with a delay. That delay creates price variation after demand has shifted but before the posted price changes. We use this variation to estimate price elasticities.`

### Use Plain Causal Links

Academic prose does not become less rigorous because it uses `because`, `so`, or `this means` when the relation is clear.

Stiff:

`This enables the approach to obtain policy-relevant counterfactuals in a broad range of settings.`

Smoother:

`Because the variation comes from delayed implementation, the same idea can be used in other settings where managers act on algorithmic recommendations with some lag.`

### Avoid Over-Engineered Hinge Words

`Whereas`, `relative to`, `without`, and `consistent with` are useful, but a paragraph becomes hard to read when every sentence carries a formal hinge.

Stiff:

`When demand uncertainty is high, the policy improves profit relative to the benchmark without increasing inventory, whereas the effect is muted when the signal is precise.`

Smoother:

`The adjusted policy matters most when the demand signal is noisy. In that regime, it raises expected profit relative to the classic benchmark without requiring more inventory. When the signal is precise, the classic rule is already close to optimal.`

### Let `We` Sound Normal

Many OR/MS papers use `we` naturally. Do not remove it just to sound formal.

Use:

- `We study a setting in which...`
- `We use this delay to identify...`
- `We compare the policy with...`
- `We show that the guarantee is tight under...`

Avoid overusing impersonal shells:

- `It is shown that...`
- `The present study investigates...`
- `The proposed framework enables...`

## What To Delete When The Draft Feels Weird

Delete or simplify before rewriting.

- Remove one abstract noun if the sentence has more than two of these: `framework`, `insight`, `mechanism`, `implication`, `contribution`, `approach`, `perspective`.
- Remove one formal relation word if the sentence already has two of these: `whereas`, `relative to`, `under`, `when`, `without`, `consistent with`, `thereby`.
- Replace `This enables/allows/highlights/underscores` with the object that does the work.
- Replace `is useful because` with the direct relation. Say what the object separates, identifies, bounds, or compares.
- Replace `offers important implications` with the action, condition, or metric.
- Replace `we provide a framework` with the actual formal object unless the paper is genuinely a framework paper.
- Replace `we leverage data` with what the data record, vary, identify, or fail to observe.
- Replace a long proposition caption with a short label and a sentence after the result.

## Avoid Overcorrection

Some drafts become strange after too much "MS-style" repair. Watch for these signs:

- every sentence contains a benchmark, condition, and mechanism even when one relation is enough;
- every paragraph names a decision, friction, method, result, and implication;
- every proof paragraph announces the constructed object, hard term, and proof move even when the proof is routine;
- every result sentence hedges with `suggests`, `is consistent with`, and `under` until the contribution sounds smaller than the evidence;
- every heading is object-like but no longer readable as a normal paper heading.

Repair by removing one layer. A simple supported claim should remain simple: state the object, the evidence, and the condition that matters.

## Natural Model Prose

A model paragraph is smoother when it tells the reader what the model is for before listing all primitives.

Good order:

- who makes the decision;
- what information arrives before the decision;
- what control is chosen;
- what outcome or objective follows;
- which feature is abstracted from or added relative to the benchmark.

Natural prose does not need to define every symbol before the reader knows why the symbol matters.

Stiff:

`Let i index agents, t index periods, and x_it denote the state variable. The model considers a platform that chooses a matching policy.`

Smoother:

`The platform chooses which agents to match in each period after observing the current queue. We let x_it denote the state of type i in period t, which records the information the platform uses when making that choice.`

## Natural Proof Prose

Proof ideas in the body should sound like a researcher explaining the one step that matters.

Stiff:

`The proof idea is: we construct an auxiliary process and derive the desired bound.`

Smoother:

`The proof compares the original process with an auxiliary process that keeps the queue lengths ordered. This comparison bounds the value loss period by period; the appendix gives the induction and the remaining case checks.`

Use a labeled `Proof.` for a complete short proof or for a one-line appendix pointer when that is the manuscript's established convention. If the body gives only the reason the result is true, normally write it as ordinary prose after the theorem and point to the appendix for verification. A formal pointer does not replace that explanatory prose.

## Natural Result Prose

The result should usually be stated before its implication, but the implication should not wait until the end of the section.

Movement:

- state the estimate, theorem, or comparison;
- say how it differs from the benchmark;
- explain the mechanism or regime;
- give the bounded action or interpretation.

Stiff:

`The result changes what managers should ask about the algorithm.`

Smoother:

`The result suggests that adoption alone is not the main decision. The algorithm improves outcomes only when it is configured to protect the metric that the benchmark overlooks.`

## Final Read-Aloud Pass

Use this pass after all technical checks.

1. Read the paragraph once as if explaining the result to a coauthor.
2. Mark any sentence that would sound odd in conversation.
3. For each marked sentence, identify the local noun and the local verb.
4. Rewrite the sentence around that noun and verb.
5. Reinsert only the condition, benchmark, or caveat needed for accuracy.

The best final version should feel calm and ordinary. It should not announce that it is elegant, rigorous, reviewer-calibrated, or insightful. The reader should feel that because the objects are in the right order.

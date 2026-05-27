# OR/MS Sentence Craft

Use this reference when the user's main complaint is that the English sounds awkward, translated, stiff, too AI-like, or hard to read even after the claim and structure are correct. This file is about sentence construction, not paper architecture. If the words themselves sound odd or nonnative, use `msor-word-choice-collocations.md` before this file.

The goal is to make each sentence sound like it belongs in an OR/MS paper: plain enough to read, exact enough to trust, and narrow enough that a reviewer can see the object, relation, evidence, and boundary.

## The Sentence Job

Before rewriting a sentence, decide the one job it must do.

- Set up a decision environment.
- Name a friction.
- Introduce a model object.
- State a result.
- Compare against a benchmark.
- Explain a mechanism.
- Place a boundary.
- Give a proof move.
- Translate a formula.

If a sentence is doing more than one of these, split it before polishing. A good sentence is often modest. A good paragraph does the larger work.

## Build Around Subject, Verb, Object

Awkward OR/MS prose often hides the actor and delays the verb.

Prefer:

- a real actor: manager, platform, firm, regulator, queue, algorithm, policy, estimator, theorem, proof;
- a real verb: chooses, observes, compares, bounds, separates, estimates, characterizes, increases, reduces, preserves;
- a real object: price, assortment, information, regret, welfare, value loss, treatment effect, threshold, benchmark.

Avoid making the sentence subject a loose abstraction such as `the analysis`, `the framework`, `the results`, or `this paper` unless that noun is truly doing the work.

Weak:

`The analysis provides a comprehensive understanding of how uncertainty affects operational decisions.`

Better:

`The model lets the demand signal change between the two ordering decisions, so the first order must preserve flexibility for the second.`

Weak:

`This paper proposes a framework to improve decision making under strategic customer behavior.`

Better:

`We study a pricing problem in which customers time their purchases after observing the firm's posted policy.`

## Keep Old Information Before New Information

A sentence feels smooth when it starts from an object the reader already has and ends on the object the reader should carry forward.

Useful progression:

1. Prior sentence introduces `managerial delay`.
2. Next sentence begins with that delay.
3. The sentence ends on `price variation`.
4. The next sentence uses that variation as the source of identification.

Natural:

`Managers often delay the implementation of recommended prices. That delay creates price variation after demand has shifted but before the posted price changes. We use this variation to estimate elasticities.`

Less natural:

`We estimate elasticities by leveraging delayed implementation of recommended prices after demand shifts.`

The second version is not wrong, but it makes the reader unpack the setting, variation, and estimand in reverse order.

## Use Plain Verbs With Exact Objects

Field prose becomes more native when the verb governs the right object.

- `study` a setting, decision, model, or empirical question.
- `estimate` an effect, elasticity, parameter, demand curve, or treatment response.
- `identify` a source of variation, condition, mechanism, or parameter only when the design supports it.
- `characterize` a policy form, equilibrium region, threshold, comparative static, or regime.
- `derive` an expression, bound, reformulation, first-order condition, or sufficient condition.
- `establish` a theorem, guarantee, rate, bound, or optimality result.
- `bound` regret, value loss, approximation error, welfare loss, or probability.
- `compare` policies, benchmarks, treatments, regimes, or algorithms.
- `preserve` feasibility, incentive compatibility, service level, order, monotonicity, or a key metric.
- `separate` a mechanism from an alternative explanation, or a hard coupled problem into tractable pieces.

Avoid:

- `leverage data` when the point is what the data record or identify;
- `utilize a framework` when the model is choosing, estimating, bounding, or comparing something;
- `provide insights` when the sentence can name the policy, metric, condition, or theorem.

## Reduce Noun Piles

English research prose can carry technical nouns, but stacked abstractions make sentences sound translated or generated.

Warning signs:

- three or more abstract nouns in a row;
- a long phrase built from `framework`, `approach`, `mechanism`, `implication`, `strategy`, `analysis`, `perspective`;
- many `of` and `for` phrases before the verb;
- the main verb arrives after a pile of modifiers.

Weak:

`The proposed decision-making framework provides important managerial implications for platform information disclosure strategy optimization.`

Better:

`The model shows when the platform should reduce disclosure precision rather than reveal more information to sellers.`

Weak:

`The demand uncertainty learning mechanism analysis highlights the value of adaptive sourcing policy design.`

Better:

`Demand learning changes the first sourcing decision because the firm can revise the second order after observing the signal.`

## Keep Prepositions Under Control

Long prepositional chains make a sentence hard to parse.

Weak:

`The effect of the intervention on the adoption of the practice by workers in treated teams under the new policy is positive.`

Better:

`The intervention increases practice adoption among workers in treated teams.`

If a sentence has several `of`, `for`, `in`, `with`, `by`, `under`, or `through` phrases, turn one phrase into a subject or verb.

## Handle Relation Words Gently

Relation words make OR/MS prose precise only when each relation is real.

- Use `when` for regimes and conditions.
- Use `where` for model environments or empirical settings.
- Use `whereas` for parallel contrasts.
- Use `relative to` and `compared with` only with a named comparator.
- Use `without` for tradeoff preservation.
- Use `consistent with` for mechanism evidence that supports but does not prove.
- Use `because` when the causal or logical link is direct and supported.

Avoid stacking several relation words in one sentence.

Overloaded:

`When demand uncertainty is high, the policy improves profit relative to the benchmark without increasing inventory, whereas the effect is muted when the signal is precise.`

Smoother:

`The policy matters most when the demand signal is noisy. In that regime, it improves expected profit relative to the benchmark without requiring more inventory. When the signal is precise, the benchmark is already close to optimal.`

## Rebuild Chinese-Logic Drafts

Do not translate word by word. Rebuild the English sentence around the object and verb.

Chinese-like:

`Under the background of digital platforms, information disclosure has important influence on sellers' decision making.`

English OR/MS:

`On many digital platforms, sellers choose prices and inventory after observing the information disclosed by the platform.`

Chinese-like:

`According to the model, we can find that the mechanism has certain managerial enlightenment.`

English OR/MS:

`The model shows that disclosure is valuable only when the demand signal improves matching more than it intensifies seller competition.`

Chinese-like:

`The proof idea is to construct an auxiliary process, and then the conclusion can be obtained by mathematical derivation.`

English OR/MS:

`The proof compares the original process with an auxiliary process that keeps the queue lengths ordered. This comparison bounds the value loss period by period; the appendix gives the induction and case checks.`

## Result Sentences

A result sentence needs enough local structure for a reviewer to know what changed.

Prefer this order when it fits:

1. condition or regime;
2. object or policy;
3. metric or formal outcome;
4. benchmark;
5. boundary or mechanism.

Examples:

- `When the signal is noisy, the adjusted rule improves expected profit relative to the classic benchmark.`
- `The estimate is concentrated among low-experience workers, which is consistent with the tool substituting for local search knowledge.`
- `The algorithm increases access without reducing total matches in the field implementation.`
- `The policy is asymptotically optimal for the pooled system but can be suboptimal for individual subsystems.`

Do not end result sentences with `important implications`, `better outcomes`, or `improved decision making` when a metric, benchmark, or condition is available.

## Model Sentences

A model sentence should earn notation by saying what the notation lets the paper do.

Good sequence:

1. actor and timing;
2. information available;
3. action or policy class;
4. objective and constraint;
5. benchmark or friction.

Weak:

`Let x_t be the state variable. We consider a platform model with strategic agents.`

Better:

`The platform observes the current queue before choosing which agents to match. We let x_t denote the queue state, which is the information the matching policy can use at time t.`

Weak:

`The model incorporates demand learning and sourcing decisions.`

Better:

`The firm chooses an initial order before the demand signal is fully resolved and can revise the second order after observing the updated signal.`

## Equation Sentences

Before a display, say what the display defines or transforms. After a display, say what the object is used for.

Before:

- `The next display defines the benchmark policy that ignores the updated signal.`
- `The Bellman equation separates the current matching reward from the continuation value.`
- `The relaxation drops the within-period coupling while preserving the capacity constraint.`

After:

- `The first term is the immediate reward from the chosen match, and the second term is the value of the remaining queue.`
- `This relaxation is useful because it gives an upper bound against which the online policy can be compared.`
- `The estimator uses the residual variation after manager fixed effects are removed.`

Avoid dropping equations into the text with only `where` clauses. The reader needs to know why the display is present.

## Proof Sentences

Body proof language should be plain. It should not announce a "proof idea" unless that phrase is natural in context.

Good proof sentence:

`The proof couples the proposed policy with a benchmark policy that receives the same arrivals but has access to the relaxed capacity constraint.`

Good checkpoint:

`The key step is to show that the coupling preserves the queue order, which lets the argument compare rewards period by period.`

Good appendix pointer:

`The appendix proves the monotonicity claim and verifies the boundary cases.`

Avoid:

- `The heart of the proof is elegant.`
- `The proof idea is: ...`
- `By some algebra, we obtain...`
- `It is obvious that...`

## Paragraph Flow From Sentences

A paragraph usually reads well when each sentence inherits one object and adds one new relation.

Possible chain:

1. `The platform chooses disclosure precision before sellers set prices.`
2. `More precise disclosure helps sellers match prices to demand, but it also intensifies competition when sellers observe similar signals.`
3. `The model compares the resulting equilibrium with a benchmark in which sellers observe only a coarse signal.`
4. `The comparison shows that more information is not always valuable to the platform.`

Notice that the paragraph does not name every element in every sentence. The objects accumulate gradually.

## Final Sentence Pass

For each sentence, ask:

1. What is the grammatical subject?
2. What is the main verb?
3. What object does the verb govern?
4. What condition, benchmark, or caveat must stay nearby?
5. Does the sentence end on the term the reader should remember?
6. Is any phrase doing only decoration?
7. Would a careful researcher say this sentence aloud?

If the answer is not clear, rewrite around the local noun and verb. Add technical qualifiers back only after the sentence works as English.

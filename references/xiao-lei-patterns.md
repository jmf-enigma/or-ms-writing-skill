# Xiao Lei Paper Patterns

Use this as a high-level reference, not as a style imitation guide. Do not copy or mimic distinctive wording from Xiao Lei or coauthors.

## Public Research Context

Xiao Lei's public HKU and personal pages describe research in online marketplaces, revenue management and pricing, and social operations management. Publicly listed Management Science publications include papers on price discrimination with fairness constraints, loot box pricing and design, and matchmaking/player engagement in video games.

## Recurring Objects To Borrow

The reusable material is not an eight-step story or a sentence style. It is a set of objects and relations that recur in this platform-paper cluster.

1. **Recognized practice.** A familiar practice such as personalized pricing, loot boxes, player matchmaking, review incentives, dynamic pricing, or content rotation can be an entry point when the application matters.
2. **Stakeholder conflict.** Name the parties that care. Usually this includes a platform or seller, consumers or players, and sometimes regulators.
3. **Operational decision.** Translate the phenomenon into one decision the firm or platform controls. Examples include setting prices, choosing a design, assigning matches, offering incentives, or rotating content.
4. **Hidden friction.** Explain why the obvious or standard policy is incomplete. The missing force may be fairness, consumer surplus, engagement decay, losing streaks, herding, learning, ambiguity, addiction, or tacit collusion.
5. **Tractable isolation.** Introduce a simple model that isolates that force. Do not apologize for abstraction. Say what the abstraction lets the reader see.
6. **Sharp benchmark.** Compare against a memorable baseline such as no fairness, the industry status quo, a traditional design, a fixed-price policy, or a standard matching rule.
7. **Mechanism result.** State what changes and why. The result should connect a condition to a mechanism and then to a decision or welfare consequence.
8. **Conditional implication.** State who should act differently, when, and with what caveat only when the result supports actionable advice.

Select and reorder these objects by the paper's actual dependency. A formal definition, counterexample, theorem, or benchmark comparison may lead. Not every paper needs stakeholder conflict, hidden friction, a mechanism claim, or an implication.

## Paper-Level Story Cards

### Fairness In Pricing

- Practice: sellers can personalize prices using consumer data.
- Concern: the same technology can create disparate impact for protected groups.
- Reader tension: fairness sounds desirable, but different fairness notions may conflict.
- Modeling move: define fairness metrics as constraints on a pricing problem.
- Result shape: simultaneous fairness may be impossible; a small amount of one fairness notion can help, while too much or the wrong notion can hurt welfare.
- Story lesson: turn a broad normative concept into several operational definitions, then show that the choice of definition changes the managerial and regulatory conclusion.

### Loot Box Design

- Practice: video games sell random bundles of virtual items.
- Decision: the firm chooses both price and design of the random reward.
- Stakeholders: company revenue, player surplus, and regulator concern all matter.
- Modeling move: compare clean stylized designs rather than catalog every game feature.
- Result shape: one design can be nearly revenue optimal while leaving little player surplus; another may be less profitable but less extractive.
- Story lesson: use a familiar product and a sharp benchmark to make an abstract revenue-management result socially legible.

### Player Matchmaking And Engagement

- Practice: many platforms match users repeatedly, and video games often default to skill-based fairness.
- Tension: a fair one-shot match may not maximize long-run engagement.
- State variable: recent outcomes, losing streaks, and engagement risk change the value of a match.
- Modeling move: formulate dynamic matchmaking, then study a stylized case that exposes the mechanism.
- Result shape: the optimal policy protects players near churn risk and can outperform skill-based matching; it also clarifies the role of bots and pay-to-win features.
- Story lesson: challenge an industry default only after explaining the dynamic state that the default ignores.

### Review Incentives

- Practice: sellers and platforms use incentives to increase reviews.
- Tension: incentives change both review volume and what future consumers infer.
- Mechanisms: herding attracts consumers to popular products, while learning lets reviews signal quality.
- Modeling move: compare a small menu of incentive policies under a stochastic review process.
- Result shape: the best policy depends on product quality and margin.
- Story lesson: define behavioral mechanisms in plain language before introducing the process model.

## Paragraph-Level Use

Do not compress all recurring objects into one paragraph. Give the paragraph a primary burden and use only linked support. An introduction may connect practice to a formal object, a result paragraph may connect a theorem to a benchmark, and an implication paragraph may connect a supported condition to an action. Claim-first, definition-first, contrast-first, and result-first arrangements are all available.

## Sentence-Level Discipline

- Prefer short ordinary sentences over punctuation-heavy architecture.
- Use actors as subjects. Platforms set, sellers choose, players churn, consumers infer, regulators restrict.
- When a result overturns a standard intuition, make both the intuition and the overturning force clear; either may come first.
- Avoid calling a result surprising. Explain which force makes it different from the reader's first guess.
- Translate each technical object once in operational language.
- Use numbers only when they anchor a benchmark the reader will remember.
- Keep social implications conditional. A model can clarify a regulatory tradeoff without claiming to solve the policy problem.

## Result Interpretation Inventory

Use only the objects the result needs: condition, mechanism, benchmark, consequence, and caveat. There is no fixed order, and a direct characterization or impossibility result may need none of the managerial items.

Example structure without copying wording:

When a constraint is mild, it mainly transfers surplus or changes access at the margin. When it is strict, it can exclude some users or distort the decision. The policy implication therefore depends on which outcome the planner wants to equalize.

## Related Work Relations

Position the paper by the exact relation rather than by topic alone. The relation can concern mechanism, setting, information, timing, policy class, formal definition, evidence type, or metric.

- Existing stream studies the same object but not the focal friction.
- Existing stream studies the friction but in a different decision environment.
- This paper may connect the object and the friction through a tractable decision model, or relate to the stream through another exact dimension.

## What Not To Borrow

- Do not copy sentence rhythms, exact phrasing, or author-specific voice.
- Do not over-index on gaming/pricing examples if the user's paper is in another OR/MS domain.
- Do not claim social or regulatory implications unless the model/result supports them.
- Do not use "first formal treatment" style claims unless the literature search supports them.
- Do not force a social-operations frame onto a purely technical result. The story must remain faithful to what the theorem, estimate, or model establishes.

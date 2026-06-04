# Academic Style And AI Writing Notes

Use this reference when a passage needs deeper diagnosis for academic style, reader flow, introduction logic, or AI-scent. The default rules are already embedded in `SKILL.md`; this file records the reasoning and source-backed style heuristics.

## Source Backbone

- Gopen and Swan, "The Science of Scientific Writing." Core lesson: readers use structure to infer meaning. Put context before new information, keep subjects near verbs, give each discourse unit one job, and place emphasis at syntactic closure.
- Purdue OWL summary of Swales' CARS model. Core lesson: introductions typically establish a territory, establish a niche, and occupy the niche. Use this as logic, not as a visible template.
- University of Leeds academic language guide. Core lesson: academic writing should be clear, concise, formal, accurate, and precise. Formal prose does not require obscure vocabulary or needless complexity.
- Kobak et al., "Delving into LLM-assisted writing in biomedical publications through excess vocabulary." Core lesson: post-ChatGPT academic prose shows abrupt increases in certain style words. Avoid words that substitute polish for local mechanism.
- Liang et al., "GPT detectors are biased against non-native English writers." Core lesson: AI detectors can misclassify non-native writers and can be bypassed. Do not write for detectors. Write for verifiable substance.
- Kousha and Thelwall, "How much are LLMs changing the language of academic papers after ChatGPT?" Core lesson: terms such as "delve," "underscore," and "intricate" have risen sharply and increasingly co-occur. Repetition and clustering matter more than any single word.

## Reader-Expectation Rules

- Start with what the reader already knows or what the prior sentence established.
- End with the claim, mechanism, condition, or contrast that should carry emphasis.
- If a sentence has a long subject before the verb, split or move the modifier.
- If two clauses compete for the stress position, give each its own sentence.
- If a paragraph changes objects, start a new paragraph or add a bridge sentence.
- If a paragraph starts with method, ask whether the reader first needs the decision, tension, or question.

## Logic Before Academic Register

A sentence that has not thought through its logic cannot be repaired by making it sound more academic. Before polishing, reconstruct the chain:

1. **Premise**: what object, setting, assumption, or prior result is already available?
2. **Evidence**: what theorem, estimate, model comparison, design feature, table, or proof move supports the next claim?
3. **Inference**: what exactly follows from that evidence?
4. **Boundary**: under what condition, sample, benchmark, information structure, or policy class does it follow?
5. **Next reader question**: what must the next sentence answer?

Common logic jumps:

- moving from a broad setting directly to a managerial recommendation;
- stating that a result "implies" a mechanism when the evidence only supports consistency with that mechanism;
- using a proof move as if it already explained the theorem's economic meaning;
- putting a robustness check after a claim without naming the threat it addresses;
- using `therefore`, `thus`, or `suggests` when the prior sentence has not established the premise.

Repair logic before register. Often the academic version is one added clause that names the comparison or condition, not a fancier verb.

## Academic Register Without Inflation

More academic prose is more precise, not more ornate.

Use academic register to:

- define constructs and overloaded terms before relying on them;
- choose calibrated inference verbs: `shows`, `suggests`, `is consistent with`, `establishes`, `characterizes`, `bounds`;
- keep assumptions, samples, benchmarks, and policy classes close to claims;
- replace casual evaluation with measurable objects: magnitude, estimate, rate, bound, regime, or threshold;
- use discipline-specific nouns when they clarify the object: estimand, treatment contrast, equilibrium, policy class, value function, incentive constraint.

Avoid upgrading plain field language into inflated prose. `We estimate`, `the model shows`, and `the proof bounds` are often more academic than `we provide a comprehensive analysis`, because they tell the reviewer what kind of support the sentence has.

Casual words to repair in paper prose include `a lot`, `big`, `huge`, `things`, `stuff`, `kind of`, `sort of`, `really`, `very`, `basically`, and unsupported `clearly` or `obviously`. Replace them with the object, metric, condition, or proof fact.

## CARS Without Template Prose

For introductions and related motivation:

1. Territory: name the operational, market, empirical, or theoretical setting.
2. Niche: state the unresolved decision, identification problem, model limitation, behavioral mechanism, or policy tension.
3. Occupy: state what this paper does and what it finds.
4. Consequence: say what changes for theory, method, or managerial decision making.

Do not write generic gaps:

- Weak: "Prior work has not studied this important problem."
- Better: "Prior models treat the data stream as fully informative, which obscures how censoring changes the value of experimentation."
- Weak: "This paper fills a gap in the literature."
- Better: "We identify a regime in which the platform should deliberately limit information disclosure because additional precision intensifies seller competition."

## Evidence-Calibrated Verbs

- "documents" for descriptive patterns.
- "estimates" for empirical designs.
- "identifies" only when the design, instrument, variation, or model supports identification.
- "predicts" for out-of-sample or model-implied predictions.
- "shows" for direct empirical, analytical, or numerical results.
- "establishes" for theorem-backed claims.
- "characterizes" for structural properties, equilibrium regions, thresholds, or policy forms.
- "suggests" for interpretations that are plausible but not fully identified or proven.
- "is consistent with" for mechanism evidence that rules in but does not uniquely prove a channel.

## AI-Scent Triggers

Treat the following as diagnostic, not as a banned-word list. A word may stay if it is the exact technical word and the sentence names the local object.

- Overused style words: delve, intricate, underscore, pivotal, meticulous, multifaceted, comprehensive, robust, innovative, transformative, realm, landscape, tapestry, vital, crucial.
- Template phrases: rapidly evolving landscape, it is important to note, this highlights, this underscores, by leveraging, not only ... but also, valuable insights, practical implications, improve decision-making, enhance performance.
- Empty "-ing" pivots: highlighting, showcasing, underscoring, leveraging, utilizing, ensuring.
- Generic contribution shells: "This paper contributes to the literature by...", "Our framework provides insights...", "The results have important managerial implications..."
- Punctuation scaffolding: colon-led labels such as "Key insight:", "The implication is:", "Contribution:", "Result:", "Proof idea:", and "Takeaway:"; semicolon chains; dash pivots that create a reveal instead of a logical relation.
- Itinerary prose: repeated "we first," "we then," "we next," and "finally" when the paragraph should be organized by objects, results, or evidence.
- Weak antecedent links: "This enables/allows..." and ", which enables/allows..." when "this" or "which" points to an entire previous sentence rather than a named mechanism, theorem, design, or data feature.
- Decorative triplets: three abstract adjectives or nouns joined as `A, B, and C`, especially before words such as framework, approach, implications, insights, challenges, opportunities, or dynamics. These often sound like filler unless each item is a real construct or result branch.

Replacement rule:

- Replace the style word with a local noun, verb, metric, assumption, or condition.
- Replace "this underscores" with the specific object that changes the reader's belief.
- Replace "valuable insights" with the action and condition.
- Replace "comprehensive framework" with the model primitives or data design.
- Replace colon-led labels with direct syntax. For example, write "This comparison shows when the threshold policy improves profit relative to the myopic benchmark" rather than "Key implication: the threshold policy improves profit."
- Replace itinerary prose with research-object prose. "We first model the platform, then analyze equilibrium, and finally discuss implications" usually becomes a sentence about the platform's decision, the equilibrium object, and the condition that changes the implication.
- Replace decorative triplets with one precise object or with separate claims. `robust, scalable, and efficient framework` usually becomes the policy class, guarantee, runtime, or benchmark that the paper actually establishes.
- If removing AI-scent makes the paragraph flat, add a real hinge rather than a style word. The hinge should name a contrast, condition, mechanism, benchmark, or boundary.

## Reviewer-Readable Anti-AI Pass

Before finalizing, ask:

- Could the sentence be true for many papers? If yes, add local evidence or delete it.
- Does a claim use a field-loaded term without a definition or benchmark?
- Does the paragraph rely on a polished transition instead of a logical relation?
- Does the prose contain clusters of LLM-associated words?
- Does the prose rely on colons, semicolons, or dash pivots to create artificial structure?
- Does the paragraph move like a table of contents rather than an argument?
- Does a `This` or `which` clause have a precise antecedent?
- Does the paragraph have a reason for moving from one object to the next?
- Does the last sentence teach a mechanism, boundary condition, or implication?
- Can a reviewer identify the actor, decision, friction, evidence, and validity condition without searching elsewhere?

## Source URLs

- https://www.sci.utah.edu/~macleod/writing/sciwriting-gopen-swan.pdf
- https://owl.purdue.edu/owl/general_writing/the_writing_process/organization_CARS_Model.html
- https://library.leeds.ac.uk/info/14011/writing/221/language-and-style
- https://arxiv.org/abs/2406.07016
- https://arxiv.org/abs/2304.02819
- https://link.springer.com/article/10.1007/s11192-026-05601-5

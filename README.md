# OR/MS Writing Skill

Idiomatic, reviewer-calibrated academic writing support for Operations Research, Management Science, M&SOM, and adjacent empirical, theoretical, algorithmic, policy, and business analytics work.

This repository contains a Codex skill. It is designed to help draft, rewrite, diagnose, organize, and audit OR/MS research prose at many granularities: one sentence, one paragraph, a model description, a theorem interpretation, a proof idea, a response to a referee, a full paper section, or a complete manuscript.

## About

`or-ms-writing` is a Codex skill for turning rough research notes, model arguments, proof sketches, empirical results, and reviewer-facing revisions into natural OR/MS paper prose. It emphasizes idiomatic word choice and collocations, sentence-level English craft, full-text MS/OR close-reading patterns, manuscript-spine judgment, cross-section contract consistency, readable paragraph flow, claim-evidence-boundary control, lane-specific section architecture, model and theorem narration, proof exposition, and main-text versus appendix placement.

## English

### What This Skill Does

`or-ms-writing` helps Codex write like a careful OR/MS researcher rather than a generic academic assistant. It focuses on:

- precise claim, evidence, and boundary control;
- task triage: deciding whether the next pass should prioritize sentence craft, paragraph flow, paper spine, cross-section consistency, mathematical exposition, body/appendix placement, or reviewer calibration;
- idiomatic word choice: verb-object fit, prepositions, evidence verbs, and OR/MS collocations rather than dictionary synonyms;
- sentence craft: local subjects, exact verbs, concrete objects, controlled relation words, clean stress positions, and translated-English repair;
- manuscript-level judgment: central object, spine result, result hierarchy, credibility path, model necessity, and reviewer objections;
- Management Science and OR/MS style without imitating any living author's personal voice;
- full-text close-reading rhythm from recent MS/OR body sections: how papers introduce models, state results, explain proof moves, and hand off verification to appendices;
- natural paragraph flow, read-aloud smoothness, micro-level wording, sentence hinges, verb-object choices, and relation words such as `when`, `whereas`, `relative to`, `without`, and `consistent with`;
- template-residue repair for stiff prose, unresolved placeholders, slash-list planning remnants, and stock sentences that sound mechanically OR/MS;
- lane-specific paper structure, heading depth, and subheading decisions;
- model narration, notation setup, theorem/proposition captions, proof exposition, and appendix placement;
- reviewer-facing prose for interdisciplinary papers where a reviewer may know one subfield deeply but not the whole paper's toolkit;
- manuscript-contract auditing across the abstract, introduction, model or design, results, and conclusion: central object, claim, comparator, metric, evidence, boundary, terminology, and headline numbers;
- language repair for passages that feel translated, generic, overclaimed, or too AI-like.

### Recent Close-Reading Update

The latest update adds full-text signals from predictive-prescriptive analytics, data-driven newsvendor models, decision-focused prediction, dynamic pricing with unknown demand, online-retail implementation, operational-transparency experiments, fast-fashion theory, policy-gradient guarantees, network inventory algorithms, and their appendices. It strengthens guidance on:

- whole-task dispatch: unit, lane, reader job, and output shape before drafting;
- logic-before-style repair: prerequisites and definitions, claim and warrant, scope continuity, evidence-register shifts, and attention hierarchy;
- a hard-dependency versus presentation-choice distinction: definitions and warrants must be available when used, while claims, evidence, formulas, examples, and interpretations can be ordered in several legitimate ways;
- story-order repair without a fixed arc: claim-first, evidence-first, definition-first, contrast-first, and result-first orders are all available when their relations are clear;
- full-paper close-reading paths: how field experiments, platform models, multimethod studies, optimal-control papers, and appendix-heavy theory papers organize analytical dependencies without forcing every section into a question-and-answer handoff;
- workflow cleanup: a shorter control-loop procedure, tighter request triage for paper-close-reading prompts, and less noisy topic lenses in section planning;
- AI-scent list detection: catches decorative `A, B, and C` adjective/noun triplets and asks whether the items are real constructs or just filler;
- citation close reading: checks citation dumping, unsourced literature claims, and novelty claims, and requires reading the cited paper's actual model/data/result/proof content before judging whether a citation supports the sentence;
- high-impact paper craft: learns from classic and highly cited MS/OR papers by asking what portable object, benchmark, evidence, and boundary made the paper reusable;
- academic register calibration: more precise constructs, assumptions, benchmarks, and inference verbs without ornate wording;
- construct and measurement sections such as `Measures`, `Empirical Framework`, and `Measurement Challenges`;
- when an empirical measure, potential outcome, treatment contrast, or estimating equation is the paper's model;
- field-experiment result prose: treatment effect, demand effect, heterogeneity, spillovers, alternative mechanisms, and placebo checks;
- proposition placement: bare labels, short captions, complete short body proofs, venue-style one-line `Proof.` appendix pointers, and ordinary prose for proof moves, with a consistent convention and nearby interpretation;
- whole-manuscript consistency: the same central object, comparator, metric, evidence type, magnitude, and boundary must survive section-specific compression and formalization;
- appendix design: variable construction, balance checks, robustness tables, auxiliary lemmas, KKT verification, repeated cases, and implementation details.
- overcorrection control: stop adding OR/MS genre markers once the local object, evidence, and condition are clear.

### Best For

Use this skill for:

- abstracts, introductions, contribution paragraphs, related work, and discussion sections;
- deciding what the paper is really about before drafting: which result carries the manuscript, which results support it, and which items should move to the appendix;
- section architecture, headings, subheadings, and paragraph order;
- model setup, assumptions, formulations, theorem/proposition statements, local proof placement, result interpretations, and proof ideas;
- deciding what belongs in the main text, appendix, online appendix, or replication package;
- polishing Management Science, Operations Research, M&SOM, OM, mechanism design, empirical, learning, platform, healthcare, supply chain, policy, and business analytics writing;
- rewriting rough Chinese or mixed-language notes into natural academic English while preserving the original mathematical and empirical claims.

### Writing Principles

The skill is built around a few nonnegotiable writing principles:

- Do the right pass first: language-only requests should not be inflated into paper redesign, and manuscript-level requests should not be reduced to sentence polishing.
- Natural prose starts with natural word pairings: a theorem establishes a bound, a policy improves a metric, data record behavior, robustness checks preserve an interpretation, and effects are on outcomes.
- Every major claim needs nearby evidence and a clear boundary.
- A strong paper needs a spine: the central object and the result that carries the contribution.
- A high-impact paper usually gives later readers a portable object: a model, benchmark, contract, measure, theorem object, policy class, empirical contrast, or tradeoff that can be cited and extended.
- Results should not receive equal emphasis; distinguish spine result, load-bearing support, mechanism, boundary, robustness, extension, and appendix-only verification.
- Stronger prose should not mean stronger unsupported claims.
- A model should be introduced through its formal or decision object and analytical role, not as a collection of symbols.
- Theorem and proposition captions should stay spare; the paper should explain the result in the surrounding prose.
- Proof ideas should name the load-bearing mathematical move, not hide behind "by algebra."
- A proof idea is often ordinary prose, not a visible `Proof idea:` label. A formal `Proof.` may contain a complete short proof or, when the paper uses that convention, a one-line appendix pointer; the pointer never replaces interpretation.
- Proof ideas should be proportional: a routine proof may need one precise sentence; a surprising result may need a short proof checkpoint.
- Polished prose should avoid colon-led roadmaps such as "Key insight:", "Result:", or "Managerial implication:" unless the mark is required by a formal label, table, definition, theorem condition, or venue format.
- Avoid itinerary prose such as "we first..., we then..., finally..." and weak links such as "This enables..." or ", which allows..." unless the antecedent is precise.
- Elegant OR/MS storytelling comes from recoverable analytical relations, warranted claims, and controlled changes in scope or emphasis, not a required sequence of tension, method, result, and implication.
- The main text must let a reviewer understand and trust the contribution without opening the appendix. At the local result-package level, an appendix pointer needs nearby prose saying what is established, why it matters, or what the appendix verifies.
- References and scripts are diagnostic tools. The final prose should read naturally, not like a checklist.
- When prose sounds stiff, the skill now prioritizes sentence craft: ordinary subject-verb-object movement, fewer noun piles, shorter preposition chains, and one-step paragraph progression before adding more OR/MS markers.

### Installation

Clone this repository into your Codex skills directory under the skill name `or-ms-writing`:

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/jmf-enigma/or-ms-writing-skill.git ~/.codex/skills/or-ms-writing
```

If the skill is already installed and you want to update it:

```bash
git -C ~/.codex/skills/or-ms-writing pull
```

### Example Prompts

```text
Use $or-ms-writing to rewrite this model paragraph in Management Science style.
```

```text
Use $or-ms-writing to turn these proof notes into a main-text proof idea and an appendix proof plan.
```

```text
Use $or-ms-writing to decide which of these results should be in the body versus the appendix.
```

```text
Use $or-ms-writing to make this abstract more native, less generic, and more precise about evidence and boundary conditions.
```

```text
Use $or-ms-writing to audit this manuscript for claim, terminology, number, and boundary drift across sections.
```

### Repository Structure

```text
.
├── SKILL.md                 # Main skill instructions and routing logic
├── agents/openai.yaml       # Codex UI metadata
├── references/              # Detailed OR/MS writing, model, proof, and paper-style references
├── scripts/                 # Lightweight planning and diagnostic scripts
└── templates/               # Reusable planning templates
```

### Useful Scripts

```bash
python3 scripts/triage_request.py --target "Management Science" --request "make this proof idea less weird" < draft.txt
```

```bash
python3 scripts/plan_section.py --section headings --target "Management Science" --topic "DID construct validation"
```

```bash
python3 scripts/plan_manuscript.py --target "Management Science" < notes.txt
```

```bash
python3 scripts/audit_manuscript_contract.py --target "Management Science" < manuscript.txt
```

```bash
python3 scripts/plan_math_split.py --target "Management Science" < proof_notes.txt
```

```bash
python3 scripts/check_paragraph.py --section results --fail-on-ai-scent < draft.txt
```

### Boundaries

This skill does not invent missing theory, data, causal identification, robustness, numerical magnitude, or empirical significance. It improves wording, structure, reader order, and reviewer calibration while preserving the supplied evidence. If a proof is missing rather than rough, use a proof-discovery workflow before asking this skill to polish it.

### License

MIT License. See [LICENSE](LICENSE).

## 中文

### 简介

`or-ms-writing` 是一个面向 OR/MS 论文写作的 Codex skill，用来把 rough notes、model 叙述、proof sketch、实证结果和审稿回复整理成更自然的 Management Science / Operations Research 风格论文语言。它重点处理 manuscript spine、跨章节 paper contract、claim、evidence、boundary、section architecture、小标题层级、model/proof 叙述、theorem/proposition caption、全文 close reading 里看到的正文节奏，以及正文和附录的分工。

### 这是什么

`or-ms-writing` 是一个面向 OR/MS 论文写作的 Codex skill。它的目标不是写得花，而是写得像真正的 Management Science / Operations Research / M&SOM 论文: 观点清楚，证据贴近，边界不虚，模型和数学叙述能被审稿人顺着读下去。

最新版本把“用词搭配”和“句子英文”放得更靠前，也补上了对全文正文和 appendix 的 close reading：先看 verb-object fit、preposition、evidence verb、OR/MS collocation，再让每句话围绕清楚的 local object 和 relation 展开，只在论证需要时加入 condition、benchmark 或 scope；遇到 model、theorem、proof idea、appendix handoff 时，会按真实 MS/OR 正文的写法判断深度，而不是套一个固定模板。它会尽量避免把诊断标签直接写进成稿。

它也加入了一个前置 triage：先判断当前任务到底是语言问题、段落问题、整篇文章主线问题、跨章节一致性问题、数学/证明问题、正文/附录分工问题，还是 reviewer calibration 问题。这样不会把一个简单的句子改写膨胀成整篇 paper redesign，也不会在整篇文章问题上只做表面润色。

它可以处理很小的任务，也可以处理很大的任务。你可以让它改一句话、润色一段 model、写 theorem intuition、判断正文小标题、拆正文和附录、组织 proof idea、改 abstract、写 referee response，或者整理一整节。

### 适合做什么

适合用它来处理:

- abstract、introduction、contribution、related work、discussion；
- 先判断当前任务该优先修语言、结构、数学叙述、正文/附录分工还是审稿人理解；
- 判断一篇文章真正要讲什么：哪个 result 是 spine，哪些是 support，哪些只是 robustness 或 appendix verification；
- 检查摘要、引言、模型或研究设计、结果和结论是不是在讲同一篇 paper：central object、comparator、metric、evidence type、claim strength、boundary 和关键数字有没有漂移；
- section architecture、headings/subheadings、paragraph order；
- 段落之间和段落内的逻辑：定义是否在使用前可得、claim 是否有 warrant、comparator 和 scope 是否稳定、证据类型变化是否明确；区分硬依赖和展示顺序，不再强制每段段尾都交给下一段；
- 真实 paper 的 section 推进：mechanism、benchmark、approximation、replication、decomposition 和 appendix 各自承担什么分析或证据作用，而不是强行让上一节先提出一个问题；
- 更干净的内部流程：少一点 checklist，多一点 scope、reader path、evidence/placement、language polish 的控制循环；
- 新的 AI 味检测：抓 `A, B, and C` 这种三连抽象形容词/名词，尤其是接 framework、insights、implications 这类词的时候；
- 引用 close reading：检查 citation dumping、没有 citation 的 literature claim、没有文献边界的 novelty claim；判断引用是否合适时必须看被引文章的具体 model/data/result/proof 内容，DOI/BibTeX/作者年份核验交给 citation tools；
- 高引/经典论文写法：不是模仿名家措辞，而是学它们怎样让一个 model、benchmark、contract、measure、policy class、theorem object、empirical contrast 或 tradeoff 变成后续文献可以引用和扩展的 portable object；
- model setup、assumption、formulation、theorem/proposition statement、result interpretation；
- proof idea、proof sketch、appendix proof、正文和附录的数学分工；
- proposition/theorem 后面什么时候直接写完整短 `Proof.`，什么时候按全文惯例只放一行 `Proof.` 附录指针，什么时候用普通正文解释 proof move；
- Management Science 风格的语言、用词、句子节奏和故事逻辑；
- 真实正文里的 model/proof/appendix 写法：什么时候正文给完整 proof，什么时候只给承重 proof move，什么时候把完整验证放进 appendix；
- 实证论文里的 construct 和 measurement 写法：什么时候 `Measures`、`Empirical Framework`、`Measurement Challenges` 本身就是正文核心，而不是附录细节；
- field experiment 结果段：treatment effect、demand effect、heterogeneity、spillovers、alternative mechanisms、placebo checks 怎么分层写；
- 理论文里的 proposition 摆法：什么时候 proposition 前要先推到 threshold 或 comparison，什么时候 proposition 下面写完整短 `Proof.`，什么时候按全文惯例只放一行 `Proof.` 附录指针，什么时候用普通正文解释 proof move；
- 用词和搭配：比如 `effect on`、`robust to`、`relative to a benchmark`、`establish a bound`、`estimate an effect`，以及避开 `managerial enlightenment`、`optimize decision-making`、`provide insights` 这类翻译腔；
- 句子级英文修复：弱主语、抽象名词堆、介词链、中文直译、relation words 滥用、proof idea 句子过硬；
- 段落读起来顺不顺、像不像研究者在自然解释一个问题，而不是把诊断标签硬塞进一句话；
- 检查和修掉 `[policy]` 这类未替换 placeholder、slash-list planning residue、以及 stock theorem-usefulness 这类机械句；
- 很细的 expression 和 sentence move，比如 `when` 写 regime、`relative to` 写 benchmark、`without reducing` 写 tradeoff、`consistent with` 写机制证据；
- 同一个 model / data 下更好的表达，而不是更强的、不被支持的结论；
- 中文 rough notes 到自然英文论文段落的转换。

### 写作内核

这个 skill 的核心判断很简单，但执行时很严格:

- 先做正确的 pass：语言任务先修句子，全文任务先定主线，数学任务先定正文/附录深度。
- 先修自然搭配，再修句子结构；不要把奇怪的词组用更华丽的词包装起来。
- 一个大 claim 附近必须有 evidence。
- 一个强 claim 附近必须有 boundary。
- 一篇强文章必须有 spine：读者应记住的 central object，以及真正承载贡献的 result。
- 高质量 MS/OR 文章通常还有一个 durable object：后续论文会引用的 model、benchmark、measure、contract、policy class、theorem object、empirical contrast 或 tradeoff。
- 一句强英文要先有清楚的 subject、verb、object；不要用 abstract noun pile 和空泛主语去遮住真正的 actor、policy、model、estimate 或 proof move。
- 不是所有 result 都应该同等展开；正文要围绕 spine result 组织，附录负责验证、重复检查和二级扩展。
- 语言可以更地道，但结论不能被偷偷加强。
- model 要让读者在依赖符号之前理解 central formal/decision object 和 display 的作用；实践导向论文可以先讲 operating process，技术论文也可以先给 canonical formulation，再紧接着解释变量和关系。
- theorem/proposition 的标题要克制，通常只用编号或很短的 object label；真正的意思放在前后正文里讲清楚。
- `Proof idea:` 通常不要作为正文里的可见标签。`Proof.` 可以承载完整短证明，也可以按期刊或全文惯例只承载附录指针；但附录指针不是 proof idea，也不能替代 proposition 后面的结果解释。
- proof idea 要说清楚真正承重的数学动作，比如 relaxation、coupling、decomposition、KKT、concentration、fixed point、exchange argument。
- proof idea 要按难度写：routine proof 可以一句话说清楚；surprising theorem 才需要更明确的 proof checkpoint。
- 少用冒号式的 AI 节奏，比如 `Key insight:`、`Result:`、`Managerial implication:`。除非是 definition、assumption、table、theorem condition 或期刊格式需要，成稿里应改成自然句子。
- 避免 `we first..., we then..., finally...` 这种流水账，也避免没有明确 antecedent 的 `This enables...` 或 `which allows...`。
- 优雅的 OR/MS 叙事来自可恢复的分析关系、有根据的 claim，以及受控的 scope 和 emphasis 变化，而不是固定的 friction–method–result–implication 顺序；claim-first、evidence-first、definition-first 和 result-first 都可以成立。
- 正文要让审稿人第一遍就理解贡献和可信度；附录负责完整验证、长证明、重复 robustness、implementation details。附录指针前后必须有邻近正文说清结果意义和附录验证什么，但形式化的 `Proof.` 指针可以按全文惯例直接放在命题下面。
- 全文允许不同章节使用不同压缩程度，但不能偷换 central object、comparator、metric、evidence、magnitude 或 boundary；结论可以解释结果，不能把结果升级成一篇更强的 paper。

### 安装

把这个 repo clone 到 Codex 的 skills 目录，并把文件夹命名为 `or-ms-writing`:

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/jmf-enigma/or-ms-writing-skill.git ~/.codex/skills/or-ms-writing
```

已经安装过的话，更新即可:

```bash
git -C ~/.codex/skills/or-ms-writing pull
```

### 使用示例

```text
Use $or-ms-writing to polish this proof idea for a Management Science paper.
```

```text
Use $or-ms-writing to rewrite this model setup so the notation is earned before the display.
```

```text
Use $or-ms-writing to decide which results, proofs, and robustness checks belong in the body versus the appendix.
```

```text
Use $or-ms-writing to make this paragraph more native, less translated, and more reviewer-calibrated.
```

```text
Use $or-ms-writing to check whether the abstract, introduction, results, and conclusion preserve the same claim, metric, evidence, and boundary.
```

### 文件结构

```text
.
├── SKILL.md                 # skill 主入口和 reference routing
├── agents/openai.yaml       # Codex 展示信息
├── references/              # MS/OR 语言、结构、模型、证明、附录分工等参考
├── scripts/                 # 规划和诊断脚本
└── templates/               # 可复用的规划模板
```

### 注意边界

这个 skill 不会替论文发明定理、数据、显著性、因果识别、robustness 或数值大小。它能做的是把已有内容写得更清楚、更地道、更像 OR/MS 论文，并且让 claim、evidence、assumption、benchmark、policy class、data regime 这些东西放在审稿人需要的位置。

如果证明本身还没有成立，应该先做 proof discovery 或 proof debugging；如果证明已经有了，只是写得粗糙，这个 skill 才适合把它变成正文 proof idea 和附录 proof。

### License

MIT License。见 [LICENSE](LICENSE)。

# OR/MS Writing Skill

Idiomatic, reviewer-calibrated academic writing support for Operations Research, Management Science, M&SOM, and adjacent empirical, theoretical, algorithmic, policy, and business analytics work.

This repository contains a Codex skill. It is designed to help draft, rewrite, diagnose, and organize OR/MS research prose at many granularities: one sentence, one paragraph, a model description, a theorem interpretation, a proof idea, a response to a referee, or a full paper section.

## About

`or-ms-writing` is a Codex skill for turning rough research notes, model arguments, proof sketches, empirical results, and reviewer-facing revisions into natural OR/MS paper prose. It emphasizes idiomatic word choice and collocations, sentence-level English craft, manuscript-spine judgment, readable paragraph flow, claim-evidence-boundary control, Management Science and Operations Research language, lane-specific section architecture, heading and subheading choices, model and theorem narration, proof exposition, and main-text versus appendix placement.

## English

### What This Skill Does

`or-ms-writing` helps Codex write like a careful OR/MS researcher rather than a generic academic assistant. It focuses on:

- precise claim, evidence, and boundary control;
- task triage: deciding whether the next pass should prioritize sentence craft, paragraph flow, paper spine, mathematical exposition, body/appendix placement, or reviewer calibration;
- idiomatic word choice: verb-object fit, prepositions, evidence verbs, and OR/MS collocations rather than dictionary synonyms;
- sentence craft: local subjects, exact verbs, concrete objects, controlled relation words, clean stress positions, and translated-English repair;
- manuscript-level judgment: central object, spine result, result hierarchy, credibility path, model necessity, and reviewer objections;
- Management Science and OR/MS style without imitating any living author's personal voice;
- natural paragraph flow, read-aloud smoothness, micro-level wording, sentence hinges, verb-object choices, and relation words such as `when`, `whereas`, `relative to`, `without`, and `consistent with`;
- template-residue repair for stiff prose, unresolved placeholders, slash-list planning remnants, and stock sentences that sound mechanically OR/MS;
- lane-specific paper structure, heading depth, and subheading decisions;
- model narration, notation setup, theorem/proposition captions, proof exposition, and appendix placement;
- reviewer-facing prose for interdisciplinary papers where a reviewer may know one subfield deeply but not the whole paper's toolkit;
- language repair for passages that feel translated, generic, overclaimed, or too AI-like.

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
- A strong paper needs a spine: the central object and the result that changes the reader's belief.
- Results should not receive equal emphasis; distinguish spine result, load-bearing support, mechanism, boundary, robustness, extension, and appendix-only verification.
- Stronger prose should not mean stronger unsupported claims.
- A model should be introduced as a decision environment, not as a collection of symbols.
- Theorem and proposition captions should stay spare; the paper should explain the result in the surrounding prose.
- Proof ideas should name the load-bearing mathematical move, not hide behind "by algebra."
- Proof ideas should be proportional: a routine proof may need one precise sentence; a surprising result may need a short proof checkpoint.
- Polished prose should avoid colon-led roadmaps such as "Key insight:", "Result:", or "Managerial implication:" unless the mark is required by a formal label, table, definition, theorem condition, or venue format.
- Avoid itinerary prose such as "we first..., we then..., finally..." and weak links such as "This enables..." or ", which allows..." unless the antecedent is precise.
- Elegant OR/MS storytelling comes from a real reader turn: old belief to missing friction, current objective to unintended consequence, method default to decision mismatch, benchmark to result, or result to boundary.
- The main text must let a reviewer understand and trust the contribution without opening the appendix, and appendix pointers should first say what the appendix verifies, preserves, or changes.
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

`or-ms-writing` 是一个面向 OR/MS 论文写作的 Codex skill，用来把 rough notes、model 叙述、proof sketch、实证结果和审稿回复整理成更自然的 Management Science / Operations Research 风格论文语言。它重点处理 manuscript spine、claim、evidence、boundary、section architecture、小标题层级、model/proof 叙述、theorem/proposition caption，以及正文和附录的分工。

### 这是什么

`or-ms-writing` 是一个面向 OR/MS 论文写作的 Codex skill。它的目标不是写得花，而是写得像真正的 Management Science / Operations Research / M&SOM 论文: 观点清楚，证据贴近，边界不虚，模型和数学叙述能被审稿人顺着读下去。

最新版本把“用词搭配”和“句子英文”放得更靠前：先看 verb-object fit、preposition、evidence verb、OR/MS collocation，再让每句话有清楚的 subject、verb、object、condition、benchmark 和 emphasis，最后才考虑 paper spine、micro-expression 和 journal flavor。它会尽量避免把诊断标签直接写进成稿。

它也加入了一个前置 triage：先判断当前任务到底是语言问题、段落问题、整篇文章主线问题、数学/证明问题、正文/附录分工问题，还是 reviewer calibration 问题。这样不会把一个简单的句子改写膨胀成整篇 paper redesign，也不会在整篇文章问题上只做表面润色。

它可以处理很小的任务，也可以处理很大的任务。你可以让它改一句话、润色一段 model、写 theorem intuition、判断正文小标题、拆正文和附录、组织 proof idea、改 abstract、写 referee response，或者整理一整节。

### 适合做什么

适合用它来处理:

- abstract、introduction、contribution、related work、discussion；
- 先判断当前任务该优先修语言、结构、数学叙述、正文/附录分工还是审稿人理解；
- 判断一篇文章真正要讲什么：哪个 result 是 spine，哪些是 support，哪些只是 robustness 或 appendix verification；
- section architecture、headings/subheadings、paragraph order；
- model setup、assumption、formulation、theorem/proposition statement、result interpretation；
- proof idea、proof sketch、appendix proof、正文和附录的数学分工；
- proposition/theorem 后面什么时候直接写 `Proof.`，什么时候只写正文解释并把完整 proof 放到 appendix；
- Management Science 风格的语言、用词、句子节奏和故事逻辑；
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
- 一篇强文章必须有 spine：读者应记住的 central object，以及真正改变信念的 result。
- 一句强英文要先有清楚的 subject、verb、object；不要用 abstract noun pile 和空泛主语去遮住真正的 actor、policy、model、estimate 或 proof move。
- 不是所有 result 都应该同等展开；正文要围绕 spine result 组织，附录负责验证、重复检查和二级扩展。
- 语言可以更地道，但结论不能被偷偷加强。
- model 要先让读者知道谁在什么信息下做什么决定，再进入符号。
- theorem/proposition 的标题要克制，通常只用编号或很短的 object label；真正的意思放在前后正文里讲清楚。
- proof idea 要说清楚真正承重的数学动作，比如 relaxation、coupling、decomposition、KKT、concentration、fixed point、exchange argument。
- proof idea 要按难度写：routine proof 可以一句话说清楚；surprising theorem 才需要更明确的 proof checkpoint。
- 少用冒号式的 AI 节奏，比如 `Key insight:`、`Result:`、`Managerial implication:`。除非是 definition、assumption、table、theorem condition 或期刊格式需要，成稿里应改成自然句子。
- 避免 `we first..., we then..., finally...` 这种流水账，也避免没有明确 antecedent 的 `This enables...` 或 `which allows...`。
- 优雅的 OR/MS 叙事来自真实转弯：旧观点到新 friction，现有目标到意外后果，默认方法到 decision mismatch，benchmark 到 result，或者 result 到 boundary。
- 正文要让审稿人第一遍就理解贡献和可信度；附录负责完整验证、长证明、重复 robustness、implementation details。正文提到附录前，要先说清楚附录验证、保留或改变了什么。

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

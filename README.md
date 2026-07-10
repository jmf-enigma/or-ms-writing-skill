# OR/MS Writing

> A Codex skill that turns technical OR/MS material into natural prose while preserving claims and anticipating reviewer questions.

[English](#english) · [中文](#中文) · [Installation](#installation) · [安装](#安装)

[![License: MIT](https://img.shields.io/badge/license-MIT-2f6f4e.svg)](LICENSE)

`or-ms-writing` turns rough notes, mathematical arguments, empirical results, and partial drafts into prose that reads like an OR/MS paper rather than a generic academic template. It works at the scale of a phrase, paragraph, proof idea, section, or complete manuscript.

It does not imitate an individual author. It learns field-level choices about wording, argument order, model exposition, proof placement, and reviewer persuasion while preserving the evidence actually supplied.

## English

### Why This Skill Exists

Good OR/MS writing is not produced by adding formal words to a correct result. The reader must be able to recover the paper's object, the support for each consequential claim, and the conditions under which the claim is valid. Mathematical material must also be divided intelligently between the main text and the appendix.

This skill handles those judgments together:

| Layer | What it handles |
|---|---|
| Language | Idiomatic collocations, evidence verbs, prepositions, sentence rhythm, and translated-English repair |
| Argument | Paragraph burden, prerequisites, claim-warrant fit, inference, scope, and transitions between analytical objects |
| Manuscript | Central object, spine result, result hierarchy, section architecture, headings, and cross-section consistency |
| Mathematics | Model setup, display narration, theorem statements, proposition captions, proof ideas, and derivation depth |
| Placement | Main text, regular appendix, online appendix or e-companion, and replication materials |
| Review | Cross-field terminology, overclaim control, citation fit, and likely reviewer misunderstandings |

### How It Works

The skill chooses the smallest useful writing pass instead of applying every convention at once.

1. **Scope the request.** Identify the requested unit, evidence lane, reader job, and output shape.
2. **Recover the logic.** Make definitions, warrants, comparisons, and boundaries available when later claims rely on them.
3. **Decide placement.** Keep first-pass understanding and trust in the body; move routine verification and repetition out.
4. **Write at the requested scale.** Return polished prose by default, not an exposed planning card.
5. **Audit the result.** Check claim strength, terminology, mathematical meaning, citation support, and AI-like residue.

References are routed compactly. A normal request starts from two to four primary references rather than loading every corpus archive into context.

### What Makes It Different

- **Flexible paper architecture.** Empirical, structural, analytical, algorithmic, and applied papers can organize evidence differently.
- **Dependency-based paragraph order.** Claim-first, evidence-first, definition-first, and result-first passages are all legitimate when their relations are clear.
- **Equation prose that follows the mathematics.** Explanation may appear before, after, or on both sides of a display.
- **Proof-specific credibility bridges.** A proof idea may expose a reduction, construction, comparison, key inequality, or direct theorem application. It need not force the same three ingredients into every proof.
- **Body-first evaluation.** The main text retains the formal object, headline result, needed interpretation, and any checkpoint required for reviewer trust.
- **Full-text citation checks.** Citation fit is judged against the cited paper's relevant model, data, result, proof, or appendix content.
- **Plain academic register.** Stronger prose means more exact objects, verbs, comparisons, and conditions, not stronger unsupported conclusions.
- **Field-level style.** The skill uses disciplinary patterns without copying a living scholar's distinctive voice.

### Best Uses

- Rewrite a sentence or paragraph that sounds stiff, translated, or AI-generated.
- Organize an abstract, introduction, contribution statement, related-work section, or discussion.
- Decide what the paper is really about before drafting the full manuscript.
- Explain a model, assumption, formulation, theorem, proposition, or empirical estimand.
- Turn rough proof notes into body-level exposition and a complete appendix plan.
- Decide which results, robustness checks, figures, and proofs belong in the body.
- Audit a manuscript for claim, terminology, number, comparator, and boundary drift.
- Write for reviewers who know one component of a cross-field paper better than the others.

### Installation

On macOS or Linux, clone the repository into the Codex skills directory:

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/jmf-enigma/or-ms-writing-skill.git ~/.codex/skills/or-ms-writing
```

If the skill was installed by cloning this repository, update it with:

```bash
git -C ~/.codex/skills/or-ms-writing pull
```

### Example Prompts

```text
Use $or-ms-writing to rewrite this paragraph in natural Management Science English without strengthening the claim.
```

```text
Use $or-ms-writing to reorganize these results around the paper's spine result and explain the paragraph-to-paragraph logic.
```

```text
Use $or-ms-writing to turn these proof notes into the main-text explanation and a complete appendix proof.
```

```text
Use $or-ms-writing to decide whether this proposition needs a short body proof, a proof bridge, or an appendix pointer.
```

```text
Use $or-ms-writing to audit the abstract, introduction, results, and conclusion for claim and boundary drift.
```

```text
Use $or-ms-writing to verify whether each citation actually supports the nearest literature claim.
```

### Diagnostic Scripts

The scripts are planning and checking tools. Their labels should not appear in final manuscript prose.

| Script | Purpose |
|---|---|
| `triage_request.py` | Choose the writing mode and a compact reference route |
| `plan_section.py` | Build a flexible section-level writing card |
| `plan_manuscript.py` | Identify the central object, spine result, and result hierarchy |
| `audit_manuscript_contract.py` | Check consistency across manuscript sections |
| `plan_math_split.py` | Separate body mathematics from appendix verification |
| `place_results.py` | Place results, proofs, robustness checks, and supporting materials |
| `check_paragraph.py` | Detect language, logic, overclaim, citation, and AI-scent problems |

Example:

```bash
python3 scripts/check_paragraph.py --section results --fail-on-ai-scent < draft.txt
```

Run the regression suite with:

```bash
python3 -m unittest discover -s tests
```

### Repository Layout

```text
.
├── SKILL.md                 # Core workflow and reference routing
├── agents/openai.yaml       # Codex interface metadata
├── references/              # Language, story, model, proof, and placement guidance
├── scripts/                 # Planning and diagnostic tools
├── templates/               # Internal writing and placement cards
└── tests/                   # Routing and false-positive regression tests
```

### Boundaries

The skill does not invent theorems, proof steps, data, identification, statistical significance, robustness, or numerical magnitudes. It can narrow, reorder, clarify, and improve supported claims. When a proof is missing rather than merely rough, proof discovery or debugging should come before prose polishing.

## 中文

### 为什么做这个 Skill

好的 OR/MS 论文语言，不是把正确结果换成更正式的词。审稿人需要顺着文章看清楚研究对象、主要结论、证据来源，以及结论成立的条件。涉及 model、theorem 和 proof 时，还要判断哪些数学内容必须留在正文，哪些验证细节适合放进附录。

`or-ms-writing` 把这些判断放在同一个写作流程里：

| 层次 | 处理内容 |
|---|---|
| 语言 | 地道搭配、证据动词、介词、句子节奏和翻译腔修复 |
| 论证 | 段落任务、定义与前提、claim-warrant 对应、推理、scope 和段落衔接 |
| 全文 | central object、spine result、结果层级、章节结构、小标题和跨章节一致性 |
| 数学 | model setup、公式叙述、theorem、proposition 标题、proof idea 和推导深度 |
| 分工 | 正文、普通附录、online appendix/e-companion 和复现材料 |
| 审稿 | 跨领域术语、过度表述、引用匹配和潜在误解 |

### 工作方式

这个 skill 不会一次套用所有写作规则，而是先选择当前任务真正需要的 pass。

1. **确定任务范围。** 判断要处理的是一句话、一个段落、一节、数学笔记还是整篇文章。
2. **恢复论证逻辑。** 在读者需要之前准备好定义、证据、比较对象和适用边界。
3. **决定正文与附录。** 正文保留第一遍理解和信任所需的内容，附录承担完整验证和重复材料。
4. **按要求的尺度写作。** 默认直接返回可用正文，不把内部 writing card 暴露在成稿里。
5. **完成审计。** 检查 claim strength、术语、数学含义、引用支持和 AI 写作痕迹。

内部 reference 采用紧凑路由。普通任务通常只从两到四份核心参考开始，不会把所有语料库同时塞进上下文。

### 关键特点

- **论文结构按证据类型调整。** 实证、结构模型、理论、算法和应用型论文可以采用不同的证据顺序。
- **段落顺序服从论证依赖。** Claim-first、evidence-first、definition-first 和 result-first 都可以成立。
- **公式解释服从数学过程。** 解释可以放在 display 前、后或两侧，不要求对称句式。
- **Proof idea 按具体证明写。** 正文可以解释 reduction、construction、comparison、关键不等式或直接应用已有定理，不必每次都虚构 constructed object 和 hard term。
- **正文承担第一遍理解。** 正文保留 formal object、headline result、必要解释和审稿人建立信任所需的 proof checkpoint。
- **引用判断基于原文。** 判断 citation 是否合适时，需要查看被引文章相关的 model、data、result、proof 或 appendix 内容。
- **学术感来自精确。** 对象、动词、比较和条件要准确，但不能把结论偷偷加强。
- **只学习领域惯例。** 不复制在世作者的个人腔调。

### 适合处理

- 修复不地道、翻译腔、僵硬或 AI 味明显的句子和段落。
- 组织 abstract、introduction、contribution、related work 和 discussion。
- 在动笔前判断整篇 paper 的 central object 和 spine result。
- 解释 model、assumption、formulation、theorem、proposition 或 empirical estimand。
- 把 rough proof notes 写成正文解释，并规划或完成附录证明。
- 判断 result、robustness、figure 和 proof 应该放在正文还是附录。
- 检查 abstract、introduction、results 和 conclusion 是否发生 claim、术语、数字、comparator 或 boundary 漂移。
- 为跨领域论文补足审稿人真正需要的桥接说明。

### 安装

在 macOS 或 Linux 上运行：

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/jmf-enigma/or-ms-writing-skill.git ~/.codex/skills/or-ms-writing
```

如果是通过 `git clone` 安装的，可以这样更新：

```bash
git -C ~/.codex/skills/or-ms-writing pull
```

### 使用示例

```text
Use $or-ms-writing to rewrite this model paragraph in natural Management Science English without strengthening the result.
```

```text
Use $or-ms-writing to explain the logic between these paragraphs and reorder them only where a dependency is missing.
```

```text
Use $or-ms-writing to turn these proof notes into a concise body explanation and a complete appendix proof.
```

```text
Use $or-ms-writing to decide which results and robustness checks belong in the main text.
```

```text
Use $or-ms-writing to audit this manuscript for claim, terminology, comparator, number, and boundary drift.
```

### 诊断脚本

| 脚本 | 用途 |
|---|---|
| `triage_request.py` | 判断任务模式并给出紧凑的 reference 路由 |
| `plan_section.py` | 生成可调整的 section writing card |
| `plan_manuscript.py` | 判断 central object、spine result 和结果层级 |
| `audit_manuscript_contract.py` | 检查跨章节一致性 |
| `plan_math_split.py` | 拆分正文数学叙述与附录验证 |
| `place_results.py` | 安排 result、proof、robustness 和补充材料 |
| `check_paragraph.py` | 检查语言、逻辑、过度表述、引用和 AI 味 |

这些脚本只用于内部规划和诊断，输出标签不应直接进入论文正文。

### 文件结构

```text
.
├── SKILL.md                 # 核心流程和 reference 路由
├── agents/openai.yaml       # Codex 展示信息
├── references/              # 语言、故事、模型、证明和正文/附录参考
├── scripts/                 # 规划和诊断工具
├── templates/               # 内部 writing card 和 placement card
└── tests/                   # 路由和误报回归测试
```

### 能力边界

这个 skill 不会替论文发明定理、证明步骤、数据、因果识别、显著性、robustness 或数值大小。它可以在不加强证据的前提下缩小、重排、澄清和改写已有结论。如果证明本身还没有成立，应先进行 proof discovery 或 debugging，再处理正文表达。

## License

MIT License. See [LICENSE](LICENSE).

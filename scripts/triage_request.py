#!/usr/bin/env python3
"""Choose the right OR/MS writing mode before drafting."""

from __future__ import annotations

import argparse
import re
import sys


MODE_TERMS = {
    "sentence": {
        "awkward", "stiff", "weird", "strange", "translated", "translation",
        "native", "idiomatic", "wording", "phrase", "sentence", "smooth",
        "word choice", "collocation", "preposition", "verb-object", "academic",
        "scholarly", "formal register", "register",
        "ai-like", "ai scent", "colon", "noun pile", "不顺", "奇怪",
        "怪怪", "别扭", "地道", "翻译腔", "语言", "用词", "措辞",
        "搭配", "句子", "ai", "ai味", "冒号", "学术", "更学术",
    },
    "paragraph": {
        "paragraph", "flow", "story", "narrative", "transition", "logic",
        "premise", "inference", "logical chain", "argument", "story logic",
        "paragraph order", "section flow", "reader flow", "between paragraphs",
        "within paragraph",
        "introduction", "abstract", "related work", "contribution", "discussion",
        "段落", "段落之间", "段落内", "故事", "逻辑", "顺序", "推进",
        "承接", "转折", "推理", "论证", "引言", "摘要", "贡献",
    },
    "manuscript": {
        "full paper", "whole paper", "manuscript", "spine", "central object",
        "result hierarchy", "paper structure", "section structure", "headings",
        "full-text", "close reading", "paper close reading", "how papers do it",
        "how papers write", "paper writing",
        "subheadings", "完整", "整篇", "全文", "结构", "标题", "小标题",
        "主线", "文章", "整体", "全局", "优化一遍", "整体优化",
        "论文怎么写", "论文咋写", "paper咋写", "paper怎么写", "别人怎么写",
        "别人咋写", "paper是咋做", "paper怎么做",
    },
    "math": {
        "model", "equation", "derivation", "formula", "theorem", "proposition",
        "lemma", "proof", "proof idea", "appendix proof", "证明", "模型",
        "数学", "公式", "推导", "命题", "定理", "proof idea",
        "proposition", "正文证明",
    },
    "placement": {
        "appendix", "supplement", "e-companion", "body", "main text",
        "online appendix", "placement", "where to put", "正文", "附录",
        "放哪", "正文附录", "正文和附录", "正文/附录",
    },
    "reviewer": {
        "reviewer", "referee", "editor", "objection", "calibration",
        "overclaim", "misunderstand", "citation", "citations", "reference",
        "references", "related work citation", "literature citation",
        "审稿", "审稿人", "反驳", "质疑", "引用", "文献", "参考文献",
    },
}

MODE_REFS = {
    "sentence": [
        "msor-word-choice-collocations.md",
        "msor-sentence-craft.md",
        "msor-natural-prose.md",
        "msor-micro-phrasing.md",
        "msor-full-text-close-reading.md",
        "academic-style-and-ai-writing.md",
    ],
    "paragraph": [
        "msor-natural-prose.md",
        "management-science-whole-paper-storycraft.md",
        "paragraph-style.md",
        "msor-micro-phrasing.md",
        "msor-full-text-close-reading.md",
    ],
    "manuscript": [
        "msor-manuscript-judgment.md",
        "section-architecture.md",
        "msor-paper-craft.md",
        "main-text-appendix-placement.md",
        "msor-full-text-close-reading.md",
    ],
    "math": [
        "msor-word-choice-collocations.md",
        "msor-sentence-craft.md",
        "management-science-model-proof-equation-layout.md",
        "math-model-main-appendix-craft.md",
        "paper-appendix-paired-patterns.md",
        "msor-full-text-close-reading.md",
    ],
    "placement": [
        "main-text-appendix-placement.md",
        "paper-appendix-paired-patterns.md",
        "math-model-main-appendix-craft.md",
        "msor-full-text-close-reading.md",
    ],
    "reviewer": [
        "reviewer-calibration.md",
        "academic-style-and-ai-writing.md",
    ],
}

MODE_SCRIPTS = {
    "sentence": ["check_paragraph.py"],
    "paragraph": ["check_paragraph.py", "plan_section.py"],
    "manuscript": ["plan_manuscript.py", "plan_section.py", "place_results.py"],
    "math": ["plan_math_split.py", "check_paragraph.py"],
    "placement": ["place_results.py", "plan_math_split.py"],
    "reviewer": ["check_paragraph.py"],
}

MODE_RULES = {
    "sentence": "Repair English before adding structure: word choice, collocation, subject, verb, object, condition, benchmark.",
    "paragraph": "Give each paragraph one dominant job and move by reader questions, not by checklist order.",
    "manuscript": "Choose the central object, spine result, support hierarchy, and section architecture before polishing.",
    "math": "Keep the body focused on object, theorem, interpretation, and proof checkpoint; move verification details out.",
    "placement": "Keep first-pass trust in the body and move routine verification, repetitions, and implementation details out.",
    "reviewer": "Narrow overloaded terms and keep evidence, boundary, and bridge sentences near the claims reviewers could overread.",
}


def score_modes(text: str) -> dict[str, int]:
    lower = text.lower()
    scores = {mode: 0 for mode in MODE_TERMS}
    for mode, terms in MODE_TERMS.items():
        for term in terms:
            if re.search(r"\b" + re.escape(term) + r"\b", lower) or term in lower:
                scores[mode] += 1
    if len(text.split()) > 220:
        scores["paragraph"] += 1
        scores["manuscript"] += 1
    if any(marker in text for marker in {"$", "\\(", "\\[", "≤", "≥", "∑", "="}):
        scores["math"] += 2
    if any(term in lower for term in {"整体", "全局", "完整优化", "优化一遍", "整体优化"}):
        scores["manuscript"] += 2
    if any(term in lower for term in {"paper是咋做", "paper怎么做", "paper怎么写", "paper咋写", "论文怎么写", "论文咋写", "别人怎么写", "别人咋写", "full-text", "close reading"}):
        scores["manuscript"] += 3
        scores["paragraph"] += 1
    if any(term in lower for term in {"逻辑", "推理", "论证", "logic", "inference", "premise"}):
        scores["paragraph"] += 2
        scores["reviewer"] += 1
    if any(term in lower for term in {"段落之间", "段落内", "顺序", "推进", "承接", "story order", "reader flow", "paragraph order", "section flow"}):
        scores["paragraph"] += 3
        scores["manuscript"] += 1
    if any(term in lower for term in {"学术", "更学术", "academic", "scholarly", "formal register"}):
        scores["sentence"] += 2
        scores["reviewer"] += 1
    if any(term in lower for term in {"citation", "citations", "reference", "references", "引用", "文献", "参考文献"}):
        scores["reviewer"] += 2
        scores["paragraph"] += 1
    if any(term in lower for term in {"怪怪", "别扭", "不地道", "ai味", "冒号"}):
        scores["sentence"] += 2
    if "appendix" in lower and any(word in lower for word in {"proof", "derivation", "theorem", "proposition"}):
        scores["math"] += 1
        scores["placement"] += 1
    if any(term in lower for term in {"正文", "附录"}) and any(term in lower for term in {"证明", "推导", "命题", "定理", "公式"}):
        scores["math"] += 1
        scores["placement"] += 1
    return scores


def choose_sequence(scores: dict[str, int]) -> list[str]:
    positives = [mode for mode, score in scores.items() if score > 0]
    if not positives:
        return ["sentence", "paragraph"]
    priority = ["sentence", "manuscript", "math", "placement", "reviewer", "paragraph"]
    ordered = [mode for mode in priority if mode in positives]
    if "paragraph" in ordered and "sentence" in ordered and scores["paragraph"] >= scores["sentence"]:
        ordered = ["paragraph", "sentence"] + [mode for mode in ordered if mode not in {"paragraph", "sentence"}]
    if "paragraph" in ordered and "manuscript" in ordered and scores["paragraph"] >= scores["manuscript"]:
        ordered = ["paragraph", "manuscript"] + [mode for mode in ordered if mode not in {"paragraph", "manuscript"}]
    if "sentence" in ordered and "manuscript" in ordered:
        ordered = ["manuscript", "sentence"] + [mode for mode in ordered if mode not in {"manuscript", "sentence"}]
    if "manuscript" in ordered and "math" in ordered and "placement" in ordered:
        ordered = ["manuscript", "math", "placement"] + [mode for mode in ordered if mode not in {"manuscript", "math", "placement"}]
    if "math" in ordered and "placement" in ordered:
        ordered = [mode for mode in ordered if mode != "placement"] + ["placement"]
    return ordered[:4]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", default="working paper")
    parser.add_argument("--request", default="", help="user request or task description")
    args = parser.parse_args()

    stdin_text = "" if sys.stdin.isatty() else sys.stdin.read()
    text = "\n".join(part for part in [args.request, stdin_text] if part.strip()).strip()
    if not text:
        print("No request or draft provided. Pass --request or pipe the text to triage.")
        return 1

    scores = score_modes(text)
    sequence = choose_sequence(scores)

    print(f"OR/MS triage card: target={args.target}")
    print("Use this internally. Do not copy these labels into polished prose.\n")
    print("Priority sequence")
    for mode in sequence:
        print(f"- {mode}: {MODE_RULES[mode]}")

    print("\nRecommended references")
    seen = set()
    for mode in sequence:
        for ref in MODE_REFS[mode]:
            if ref not in seen:
                seen.add(ref)
                print(f"- {ref}")

    print("\nUseful scripts")
    seen_scripts = set()
    for mode in sequence:
        for script in MODE_SCRIPTS[mode]:
            if script not in seen_scripts:
                seen_scripts.add(script)
                print(f"- {script}")

    print("\nDrafting guardrail")
    if sequence[0] == "sentence":
        print("- Do not expand the argument unless the user asked for structure; fix the English while preserving the claim.")
    elif sequence[0] == "manuscript":
        print("- Do not polish all results equally; identify the spine result before writing section prose.")
    elif sequence[0] == "math":
        print("- Do not hide proof or derivation gaps in smooth prose; name the mathematical move or flag the gap.")
    elif sequence[0] == "placement":
        print("- Do not use appendix pointers as substitutes for body interpretation.")
    else:
        print("- Keep the claim, evidence, and boundary close before adding style.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

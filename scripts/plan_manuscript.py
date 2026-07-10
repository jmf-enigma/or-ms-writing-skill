#!/usr/bin/env python3
"""Plan the OR/MS manuscript spine from rough notes."""

from __future__ import annotations

import argparse
import re
import sys


SPINE_TERMS = {
    "main", "primary", "headline", "theorem", "proposition", "estimate",
    "effect", "guarantee", "bound", "characterize", "identification",
    "field experiment", "implementation", "policy", "threshold",
    "主要", "核心", "主结果", "核心结果", "主定理", "定理", "命题",
    "估计", "效应", "保证",
}
DURABLE_TERMS = {
    "model", "benchmark", "tradeoff", "contract", "policy class", "uncertainty set",
    "estimator", "measure", "construct", "mechanism", "algorithm", "relaxation",
    "bound", "index", "threshold", "treatment contrast", "identification strategy",
    "模型", "基准", "权衡", "合约", "合同", "政策类", "策略类", "不确定集",
    "估计量", "度量", "指标", "构念", "机制", "算法", "松弛", "界", "阈值",
    "处理对照", "识别策略",
}
DURABLE_INTENT_TERMS = {
    "new", "named", "general", "reusable", "portable", "canonical", "extends",
    "captures", "develop", "develops", "propose", "proposes", "formulate",
    "formulates", "introduce", "introduces", "define", "defines",
    "新的", "命名", "一般", "可复用", "可引用", "经典", "扩展", "刻画",
    "提出", "建立", "构建", "定义", "捕捉",
}
MECHANISM_TERMS = {
    "mechanism", "channel", "driven by", "because", "heterogeneity",
    "mediates", "explains", "consistent with", "why",
}
BOUNDARY_TERMS = {
    "when", "if", "under", "condition", "regime", "only", "except",
    "assumption", "boundary", "fails", "reverses", "robust",
}
APPENDIX_TERMS = {
    "appendix", "proof detail", "kkt", "constant", "case", "lemma",
    "derivation", "calibration", "data dictionary", "implementation detail",
    "robustness", "sensitivity", "auxiliary",
}
MODEL_TERMS = {
    "model", "state", "timing", "information", "action", "objective",
    "constraint", "benchmark", "assumption", "equilibrium", "estimator",
    "relaxation", "bellman", "policy class",
}
CONSTRUCT_TERMS = {
    "construct", "measure", "measurement", "calibration", "belief",
    "confidence", "ability", "skill", "potential outcome", "treatment contrast",
    "estimand", "coefficient", "empirical framework", "elicitation",
    "measurement challenge",
}
DATA_TERMS = {
    "data", "experiment", "random", "identification", "variation",
    "estimate", "table", "sample", "field", "panel", "instrument",
    "difference-in-differences", "event study",
}


def has_any(text: str, terms: set[str]) -> bool:
    lower = text.lower()
    for term in terms:
        if any(ord(char) > 127 for char in term) or " " in term or "-" in term:
            if term in lower:
                return True
        elif re.search(r"\b" + re.escape(term) + r"\b", lower):
            return True
    return False


def clean_notes(raw: str) -> list[str]:
    notes: list[str] = []
    for line in raw.splitlines():
        line = re.sub(r"^\s*[-*0-9.)]+\s*", "", line).strip()
        if line:
            notes.append(line)
    return notes


def classify(note: str) -> str:
    lower = note.lower()
    explicit_appendix = has_any(
        lower,
        {
            "appendix", "online appendix", "e-companion", "proof detail",
            "kkt verification", "case split", "case splits", "data dictionary",
            "implementation detail", "robustness table", "robustness tables",
        },
    )
    if explicit_appendix and not has_any(lower, {"main", "primary", "headline", "spine"}):
        return "Appendix or verification"
    if has_any(lower, SPINE_TERMS):
        return "Spine candidate"
    if has_any(lower, DURABLE_TERMS) and has_any(lower, DURABLE_INTENT_TERMS):
        return "Durable object"
    if has_any(lower, CONSTRUCT_TERMS):
        return "Construct or measure"
    if has_any(lower, APPENDIX_TERMS):
        return "Appendix or verification"
    if has_any(lower, MECHANISM_TERMS):
        return "Mechanism support"
    if has_any(lower, BOUNDARY_TERMS):
        return "Boundary or scope"
    if has_any(lower, MODEL_TERMS):
        return "Model object"
    if has_any(lower, DATA_TERMS):
        return "Credibility support"
    return "Unassigned"


def choose_spine(notes: list[str]) -> str:
    scored: list[tuple[int, int, str]] = []
    for index, note in enumerate(notes):
        lower = note.lower()
        score = 0
        score += 3 if has_any(lower, SPINE_TERMS) else 0
        score += 2 if has_any(lower, MODEL_TERMS | DATA_TERMS | CONSTRUCT_TERMS) else 0
        score += 1 if has_any(lower, BOUNDARY_TERMS | MECHANISM_TERMS) else 0
        score += 1 if re.search(r"\b(profit|welfare|cost|revenue|regret|accuracy|waiting|access|match|conversion|service)\b", lower) else 0
        score -= 2 if has_any(lower, APPENDIX_TERMS) else 0
        scored.append((score, -index, note))
    scored.sort(reverse=True)
    return scored[0][2] if scored and scored[0][0] > 0 else "Not clear from notes. Choose the claim the manuscript most strongly establishes and that the abstract should make memorable."


def choose_durable_object(notes: list[str]) -> str:
    scored: list[tuple[int, int, str]] = []
    for index, note in enumerate(notes):
        lower = note.lower()
        score = 0
        score += 3 if has_any(lower, DURABLE_TERMS) else 0
        score += 2 if has_any(lower, DURABLE_INTENT_TERMS | {"benchmark", "relative to", "compared with", "generalizes", "基准", "相对于", "相比"}) else 0
        score += 1 if has_any(lower, MODEL_TERMS | CONSTRUCT_TERMS | DATA_TERMS) else 0
        score -= 2 if has_any(lower, APPENDIX_TERMS) else 0
        scored.append((score, -index, note))
    scored.sort(reverse=True)
    return scored[0][2] if scored and scored[0][0] > 0 else "Not clear from notes. Name the model, benchmark, measure, treatment contrast, policy class, theorem object, or tradeoff that later papers would cite."


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", default="working paper", help="Management Science, Operations Research, M&SOM, or working paper")
    parser.add_argument("--lane", default="", help="optional paper lane, e.g. empirical, theory, algorithm, field experiment")
    args = parser.parse_args()

    notes = clean_notes(sys.stdin.read())
    if not notes:
        print("No notes provided. Give one result/model/data/proof item per line.")
        return 1

    print(f"Manuscript judgment card: target={args.target}" + (f"; lane={args.lane}" if args.lane else ""))
    print("Use this as a judgment aid, not prose. Revise with domain knowledge before drafting.\n")

    print("Likely spine result")
    print(f"- {choose_spine(notes)}\n")

    print("Likely durable object")
    print(f"- {choose_durable_object(notes)}\n")

    buckets: dict[str, list[str]] = {}
    for note in notes:
        buckets.setdefault(classify(note), []).append(note)

    order = [
        "Durable object",
        "Spine candidate",
        "Model object",
        "Construct or measure",
        "Credibility support",
        "Mechanism support",
        "Boundary or scope",
        "Appendix or verification",
        "Unassigned",
    ]
    print("Result hierarchy")
    for bucket in order:
        items = buckets.get(bucket, [])
        if not items:
            continue
        print(f"- {bucket}:")
        for item in items:
            print(f"  - {item}")

    print("\nBefore drafting, answer")
    questions = [
        "What model, benchmark, measure, treatment contrast, policy class, theorem object, or tradeoff would a later paper cite?",
        "What is the central object the reader should remember?",
        "What paper-level claim does the spine result let a knowledgeable reviewer make?",
        "Which result earns inclusion in both the abstract and introduction?",
        "What exact comparator and metric or estimand does that result use?",
        "What theorem, design, identification argument, validation, or implementation evidence owns the claim?",
        "Which support item is needed for first-pass trust?",
        "If this is empirical, which construct or measurement choice must stay in the body?",
        "Which condition or setting keeps the claim from becoming too broad?",
        "Will the abstract, introduction, model or design, results, and conclusion preserve the same object, claim strength, comparator, metric, evidence type, and boundary?",
        "Which correct but secondary items should move to the appendix?",
    ]
    for question in questions:
        print(f"- {question}")

    print("\nDrafting instruction")
    print("- Write toward the durable object; do not turn the manuscript into a catalog of tasks completed.")
    print("- Write the central object and spine result before polishing sentences.")
    print("- Place support around the spine; do not write a result catalog.")
    print("- If the model or data item does not support the spine, demote it or make its role explicit.")
    print("- If a construct, measure, or treatment contrast makes the result interpretable, keep its definition in the body and move only repeated validation to the appendix.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

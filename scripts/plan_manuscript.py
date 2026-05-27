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
DATA_TERMS = {
    "data", "experiment", "random", "identification", "variation",
    "estimate", "table", "sample", "field", "panel", "instrument",
    "difference-in-differences", "event study",
}


def has_any(text: str, terms: set[str]) -> bool:
    lower = text.lower()
    return any(term in lower for term in terms)


def clean_notes(raw: str) -> list[str]:
    notes: list[str] = []
    for line in raw.splitlines():
        line = re.sub(r"^\s*[-*0-9.)]+\s*", "", line).strip()
        if line:
            notes.append(line)
    return notes


def classify(note: str) -> str:
    lower = note.lower()
    if has_any(lower, APPENDIX_TERMS):
        return "Appendix or verification"
    if has_any(lower, SPINE_TERMS):
        return "Spine candidate"
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
        score += 2 if has_any(lower, MODEL_TERMS | DATA_TERMS) else 0
        score += 1 if has_any(lower, BOUNDARY_TERMS | MECHANISM_TERMS) else 0
        score += 1 if re.search(r"\b(profit|welfare|cost|revenue|regret|accuracy|waiting|access|match|conversion|service)\b", lower) else 0
        score -= 2 if has_any(lower, APPENDIX_TERMS) else 0
        scored.append((score, -index, note))
    scored.sort(reverse=True)
    return scored[0][2] if scored and scored[0][0] > 0 else "Not clear from notes. Choose the claim that changes the main decision, benchmark, or belief."


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

    buckets: dict[str, list[str]] = {}
    for note in notes:
        buckets.setdefault(classify(note), []).append(note)

    order = [
        "Spine candidate",
        "Model object",
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
        "What is the central object the reader should remember?",
        "What belief or benchmark does the spine result change?",
        "Which one result must appear in the abstract and introduction?",
        "Which support item is needed for first-pass trust?",
        "Which condition or setting keeps the claim from becoming too broad?",
        "Which correct but secondary items should move to the appendix?",
    ]
    for question in questions:
        print(f"- {question}")

    print("\nDrafting instruction")
    print("- Write the central object and spine result before polishing sentences.")
    print("- Place support around the spine; do not write a result catalog.")
    print("- If the model or data item does not support the spine, demote it or make its role explicit.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

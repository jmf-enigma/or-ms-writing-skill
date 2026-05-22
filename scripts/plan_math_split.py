#!/usr/bin/env python3
"""Build a main-text and appendix plan from rough OR/MS proof or model notes."""

from __future__ import annotations

import argparse
import re
import sys


MODEL_SETUP = {
    "model", "primitive", "state", "action", "decision", "timing",
    "information", "objective", "constraint", "feasible", "benchmark",
    "assumption", "definition", "solution concept", "estimand",
}
RESULT = {
    "theorem", "proposition", "corollary", "lemma", "result",
    "characterization", "guarantee", "regret", "approximation",
    "convergence", "bound", "optimality", "identification",
}
CENTRAL_DERIVATION = {
    "derive", "derivation", "reformulation", "reformulate", "relaxation",
    "lp relaxation", "fluid relaxation", "dual", "duality", "bellman",
    "decomposition", "decompose", "regret decomposition", "upper bound", "lower bound",
    "fixed point", "threshold", "index", "identifying expression",
    "plug-in", "reduction", "value function",
}
PROOF_IDEA = {
    "proof idea", "proof sketch", "roadmap", "construct", "coupling",
    "exchange argument", "monotonicity", "convexity", "concavity",
    "submodularity", "martingale", "concentration", "induction",
    "kkt", "envelope", "implicit function", "contradiction",
}
APPENDIX_DETAIL = {
    "proof", "algebra", "routine", "straightforward", "case", "cases",
    "case split", "boundary", "constant", "constants", "technical lemma",
    "auxiliary lemma", "verification", "kkt verification", "summation",
    "variance calculation", "calibration", "parameter grid", "data dictionary",
}
INTERPRETATION = {
    "means", "implies", "intuition", "interpretation", "managerial",
    "policy implication", "operational", "relative to", "compared with",
    "mechanism",
}
VALIDITY = {
    "robustness", "sensitivity", "validity", "identification", "endogeneity",
    "exogenous", "misspecification", "feasibility", "main threat",
}
GAP_WORDS = {
    "obvious", "easy to see", "trivial", "omitted",
    "left to the reader", "straightforward", "standard argument",
    "standard arguments", "standard proof", "standard technique",
}


def clean(line: str) -> str:
    line = line.strip()
    line = re.sub(r"^\s*(?:[-*+]|\d+[.)])\s*", "", line)
    return line.strip()


def has_any(text: str, terms: set[str]) -> bool:
    lower = text.lower()
    return any(term in lower for term in terms)


def classify(note: str) -> tuple[str, str, str]:
    lower = note.lower()

    if has_any(lower, GAP_WORDS):
        return (
            "Risk note",
            "Body or appendix, after repair",
            "Do not hide a step behind generic proof language. Name the exact mathematical move or mark a proof gap.",
        )
    if any(term in lower for term in {"kkt verification", "case split", "case splits", "complete proof", "proof details"}):
        return (
            "Verification detail",
            "Appendix",
            "Use for routine proof details, algebra, constants, cases, calibration, or implementation support.",
        )
    if any(term in lower for term in {"evolution equation", "evolution equations", "state equation", "state equations"}):
        return (
            "Model object",
            "Main text",
            "Use to establish agents, timing, information, actions, objective, constraints, assumptions, and benchmark.",
        )
    if any(term in lower for term in {"theorem", "proposition", "corollary"}):
        return (
            "Formal result",
            "Main text",
            "State the theorem, proposition, bound, policy structure, or estimand and add an interpretation paragraph.",
        )
    if has_any(lower, CENTRAL_DERIVATION):
        return (
            "Derivation checkpoint",
            "Main text summary plus appendix",
            "Show start point, key move, and resulting object in the body. Put algebra and verification in the appendix.",
        )
    if has_any(lower, PROOF_IDEA):
        return (
            "Proof idea",
            "Main text summary plus appendix",
            "Keep the constructed object, hard term, and load-bearing move in the body. Put formal details in the appendix.",
        )
    if has_any(lower, INTERPRETATION):
        return (
            "Interpretation",
            "Main text",
            "Use after the formal result to map symbols to the decision, benchmark, mechanism, or condition.",
        )
    if "proof" in lower and ("appendix" in lower or "complete proof" in lower):
        return (
            "Verification detail",
            "Appendix",
            "Use for the complete proof after the body states the theorem, proof idea, and interpretation.",
        )
    if has_any(lower, MODEL_SETUP):
        return (
            "Model object",
            "Main text",
            "Use to establish agents, timing, information, actions, objective, constraints, assumptions, and benchmark.",
        )
    if has_any(lower, RESULT):
        return (
            "Formal result",
            "Main text",
            "State the theorem, proposition, bound, policy structure, or estimand and add an interpretation paragraph.",
        )
    if has_any(lower, VALIDITY):
        return (
            "Validity support",
            "Main text summary plus appendix",
            "Summarize if it protects the main claim. Put full checks, tables, and variants in the appendix.",
        )
    if has_any(lower, APPENDIX_DETAIL):
        return (
            "Verification detail",
            "Appendix",
            "Use for routine proof details, algebra, constants, cases, calibration, or implementation support.",
        )
    return (
        "Needs judgment",
        "Decide by reader job",
        "Keep in the body if needed for first-pass understanding or reviewer trust. Otherwise move to appendix.",
    )


def read_notes(args: argparse.Namespace) -> list[str]:
    raw = list(args.item or [])
    if not sys.stdin.isatty():
        raw.extend(sys.stdin.read().splitlines())
    return [note for line in raw if (note := clean(line))]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", default="working paper")
    parser.add_argument("--paper-type", default="regular")
    parser.add_argument("--item", action="append", help="proof/model note; can be repeated")
    args = parser.parse_args()

    notes = read_notes(args)
    if not notes:
        print("No notes provided. Pass --item repeatedly or pipe one note per line.")
        return 1

    rows = []
    seen = set()
    for note in notes:
        role, placement, reason = classify(note)
        rows.append((note, role, placement, reason))
        seen.add(role)

    print(f"Math split plan: target={args.target}; paper_type={args.paper_type}")
    print("\n| Note | Role | Placement | Writing implication |")
    print("|---|---|---|---|")
    for note, role, placement, reason in rows:
        print(f"| {note} | {role} | {placement} | {reason} |")

    print("\nMain-text skeleton")
    skeleton = [
        ("Model object", "Open with the decision environment and the formal object."),
        ("Formal result", "State the theorem or proposition that carries the contribution."),
        ("Derivation checkpoint", "Show start point, key move, and resulting object if the result depends on a transformation."),
        ("Interpretation", "Translate the result into the decision, benchmark, mechanism, and condition."),
        ("Proof idea", "Add only the constructed object, hard term, and proof move when reviewer trust needs it."),
        ("Validity support", "Summarize only validity-critical robustness or feasibility checks."),
    ]
    for role, advice in skeleton:
        marker = "present" if role in seen else "missing"
        print(f"- {role}: {marker}. {advice}")

    print("\nDisplay layout hints")
    print("- Body displays: use for the model object, objective, benchmark, theorem statement, key decomposition, or one proof-sketch inequality.")
    print("- Sentence before display: tell the reader what the display defines, relaxes, decomposes, or bounds.")
    print("- Sentence after display: translate the central variables and say why the display is used next.")
    print("- Appendix displays: use for algebra, constants, KKT checks, concentration steps, case splits, and auxiliary lemma proofs.")

    print("\nAppendix skeleton")
    appendix_items = [note for note, role, _, _ in rows if role in {"Verification detail", "Derivation checkpoint", "Proof idea", "Validity support"}]
    if appendix_items:
        for note in appendix_items:
            print(f"- Verify or expand: {note}")
    else:
        print("- No obvious appendix items detected. Check whether proof details, cases, constants, or robustness are missing.")

    if "Risk note" in seen:
        print("\nRisk notes")
        print("- Repair generic proof language before drafting. If the missing step is real, mark a gap instead of polishing around it.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

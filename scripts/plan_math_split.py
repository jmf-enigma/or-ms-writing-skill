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
    "construct", "measure", "measurement", "potential outcome",
    "treatment contrast", "estimating equation", "empirical framework",
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
    "closed form", "closed-form", "notation table", "online appendix", "appendix",
    "e-companion", "implementation detail", "hyperparameter", "runtime",
    "variable construction", "balance check", "balance checks", "placebo",
    "placebo test", "alternative specification", "alternative specifications",
    "robustness table", "robustness tables", "repeated boundary cases",
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

APPENDIX_JOBS = [
    (
        "Proof verification",
        {"Verification detail", "Proof idea"},
        "complete proofs, helper lemmas, algebra, constants, cases, concentration, KKT checks",
    ),
    (
        "Derivation support",
        {"Derivation checkpoint"},
        "algebra that verifies a body transformation, reduction, relaxation, or decomposition",
    ),
    (
        "Reviewer-threat support",
        {"Validity support"},
        "robustness, sensitivity, feasibility, identification, misspecification, or benchmark checks",
    ),
    (
        "Notation/calibration support",
        {"Model object", "Needs judgment"},
        "notation tables, data-to-model mapping, calibration, implementation, and reproduction details when they are not needed for first-pass understanding",
    ),
]


def clean(line: str) -> str:
    line = line.strip()
    line = re.sub(r"^\s*(?:[-*+]|\d+[.)])\s*", "", line)
    return line.strip()


def has_any(text: str, terms: set[str]) -> bool:
    lower = text.lower()
    for term in terms:
        if any(ord(char) > 127 for char in term) or " " in term or "-" in term:
            if term in lower:
                return True
            continue
        if re.search(r"\b" + re.escape(term) + r"(?:s|es|ed|ing)?\b", lower):
            return True
    return False


def classify(note: str) -> tuple[str, str, str]:
    lower = note.lower()

    if has_any(lower, GAP_WORDS):
        return (
            "Risk note",
            "Body or appendix, after repair",
            "Do not hide a step behind generic proof language. Name the exact mathematical move or mark a proof gap.",
        )
    if lower.startswith(("appendix", "online appendix", "e-companion", "supplement")) or any(
        term in lower
        for term in {
            "kkt verification", "case split", "case splits", "repeated cases",
            "complete proof", "proof details", "concentration constants", "constant tracking",
        }
    ):
        return (
            "Verification detail",
            "Appendix",
            "Use for routine proof details, algebra, constants, cases, calibration, or implementation support.",
        )
    if any(term in lower for term in {"evolution equation", "evolution equations", "state equation", "state equations"}):
        return (
            "Model object",
            "Main text",
            "Make the relevant system or decision object and the primitives used by later claims recoverable. Include timing, information, actions, objective, constraints, assumptions, or a benchmark only when consequential.",
        )
    if any(term in lower for term in {"proof idea", "proof sketch", "proof roadmap", "roadmap"}):
        return (
            "Proof idea",
            "Main text summary plus appendix",
            "Keep only the load-bearing route in the body, such as a reduction, construction, comparison, key inequality, or theorem application. One sentence is enough if the proof is routine. Use ordinary prose unless the manuscript has an established formal proof-pointer convention. Put verification details in the appendix.",
        )
    if re.search(r"\b(?:apply|applies|applying|invoke|invokes|invoking)\b.*\b(?:theorem|proposition|lemma|corollary)\b", lower):
        return (
            "Proof idea",
            "Main text summary plus appendix",
            "Name the result being applied and verify the condition that makes the application valid. Keep routine verification in the appendix.",
        )
    if any(term in lower for term in {"theorem", "proposition", "corollary"}):
        return (
            "Formal result",
            "Main text",
            "State the theorem, proposition, bound, policy structure, or estimand and keep any interpretation needed to read it accurately nearby.",
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
            "Keep only the load-bearing route in the body, such as a reduction, construction, comparison, key inequality, or theorem application. One sentence is enough if the proof is routine. Use ordinary prose unless the manuscript has an established formal proof-pointer convention. Put verification details in the appendix.",
        )
    if has_any(lower, INTERPRETATION):
        return (
            "Interpretation",
            "Main text",
            "Place near the formal result to map symbols to the relevant object, comparison, mechanism, or condition. It may precede or follow the statement.",
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
            "Make the relevant system or decision object and the primitives used by later claims recoverable. Include timing, information, actions, objective, constraints, assumptions, or a benchmark only when consequential.",
        )
    if has_any(lower, RESULT):
        return (
            "Formal result",
            "Main text",
            "State the theorem, proposition, bound, policy structure, or estimand and keep any interpretation needed to read it accurately nearby.",
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


def has_appendix_hint(note: str, role: str) -> bool:
    lower = note.lower()
    return role in {"Verification detail", "Derivation checkpoint", "Proof idea", "Validity support"} or (
        "appendix" in lower and has_any(lower, APPENDIX_DETAIL | PROOF_IDEA | VALIDITY | CENTRAL_DERIVATION)
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

    print("\nMain-text modules")
    modules = [
        ("Model object", "Make the relevant formal, empirical, or decision object recoverable before later claims rely on it; a formulation may come first when its role is already active."),
        ("Formal result", "State the theorem or proposition that carries the contribution."),
        ("Derivation checkpoint", "Show start point, key move, and resulting object if the result depends on a transformation."),
        ("Interpretation", "Translate the result into the relevant object, comparison, mechanism, or condition at the depth the reader needs."),
        ("Proof idea", "Add only the reduction, comparison, inequality, theorem application, or other proof move needed for reviewer trust. Keep routine proof ideas to one precise sentence and distinguish this prose from a complete proof or a formal one-line proof pointer."),
        ("Validity support", "Summarize only validity-critical robustness or feasibility checks."),
    ]
    print("Select only the modules needed for first-pass trust; do not treat this as paragraph order.")
    for role, advice in modules:
        marker = "present" if role in seen else "missing"
        print(f"- {role}: {marker}. {advice}")

    print("\nDisplay layout hints")
    print("- Body displays: use for the model object, objective, benchmark, theorem statement, key decomposition, or one proof-sketch inequality.")
    print("- Nearby prose: make the display's role and consequential notation recoverable. Put that prose before, after, or on both sides according to dependency.")
    print("- A display may open a technical subsection when prior context already supplies its role; avoid requiring symmetrical framing sentences.")
    print("- Appendix displays: use for algebra, constants, KKT checks, concentration steps, case splits, and auxiliary lemma proofs.")
    print("\nProof label rule")
    print("- Follow one manuscript convention: a complete short `Proof.`, a formal one-line `Proof.` appendix pointer, or ordinary proof-sketch prose with a cross-reference.")
    print("- A one-line pointer records proof location; a proof idea explains the mathematical move. Neither replaces the nearby result interpretation.")
    print("- Keep theorem/proposition captions short; put any needed meaning in the surrounding local result package.")

    print("\nAppendix modules")
    appendix_items = [note for note, role, _, _ in rows if has_appendix_hint(note, role)]
    if appendix_items:
        for note in appendix_items:
            print(f"- Verify or expand: {note}")
    else:
        print("- No obvious appendix items detected. Check whether proof details, cases, constants, or robustness are missing.")

    print("\nAppendix section jobs")
    print("- Each appendix section should have one job, and its local body result package should state the conclusion and interpretation around the cross-reference.")
    for job, roles, description in APPENDIX_JOBS:
        matching = [note for note, role, _, _ in rows if role in roles]
        status = "candidate" if matching else "check if needed"
        print(f"- {job}: {status}. Use for {description}.")

    if "Risk note" in seen:
        print("\nRisk notes")
        print("- Repair generic proof language before drafting. If the missing step is real, mark a gap instead of polishing around it.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

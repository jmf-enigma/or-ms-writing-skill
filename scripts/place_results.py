#!/usr/bin/env python3
"""Suggest main-text, appendix, and supplement placement for OR/MS results."""

from __future__ import annotations

import argparse
import re
import sys


BODY_SIGNALS = {
    "main", "primary", "headline", "core", "central", "key", "preferred",
    "contribution", "abstract", "introduction", "managerial", "policy implication",
}
FORMAL_RESULT_SIGNALS = {
    "theorem", "proposition", "corollary", "main result", "regret bound",
    "approximation", "guarantee", "characterization", "optimality", "lower bound",
}
PROOF_DETAIL_SIGNALS = {
    "proof", "derivation", "algebra", "kkt", "induction", "case", "cases",
    "concentration", "lemma", "technical lemma", "duality", "coupling details",
}
PROOF_IDEA_SIGNALS = {
    "proof idea", "proof sketch", "roadmap", "reduction", "key lemma",
    "proof technique", "coupling", "relaxation", "decomposition",
}
CENTRAL_DERIVATION_SIGNALS = {
    "central derivation", "main derivation", "key derivation", "derivation checkpoint",
    "reformulation", "reformulate", "relaxation", "lp relaxation", "fluid relaxation",
    "dual", "duality", "primal-dual", "bellman", "dynamic program", "dynamic programming",
    "value function", "regret decomposition", "decomposition", "identifying expression",
    "identification formula", "plug-in estimator", "structural transformation",
    "reduced form", "upper bound", "lower bound", "policy structure",
    "threshold derivation", "equivalent randomized policy",
}
ROUTINE_DERIVATION_SIGNALS = {
    "routine algebra", "algebraic details", "mechanical algebra", "omitted algebra",
    "kkt verification", "constant tracking", "constants", "boundary case",
    "boundary cases", "case split", "case splits", "repeated cases",
    "concentration constants", "summation details", "variance calculation",
    "complementary slackness", "induction details", "technical verification",
}
ROBUSTNESS_SIGNALS = {
    "robustness", "robust", "sensitivity", "placebo", "alternative specification",
    "alternative spec", "additional specification", "parameter sweep", "stress test",
}
VALIDITY_SIGNALS = {
    "identification", "endogeneity", "exogenous", "instrument", "validity",
    "main threat", "feasibility", "external validity", "confounder", "causal",
    "misspecification", "model misspecification",
}
EXTENSION_SIGNALS = {
    "extension", "variant", "generalization", "reversible", "heterogeneity",
    "cross-price", "secondary effect", "additional model",
}
NUMERICAL_SIGNALS = {
    "simulation", "numerical", "experiment", "case study", "application",
    "real data", "data application", "benchmark comparison",
}
EXTRA_SIGNALS = {
    "additional", "extra", "secondary", "supplementary", "all remaining",
    "full set", "complete list", "parameter grid", "implementation detail",
}
REPLICATION_SIGNALS = {
    "code", "data", "readme", "replication", "dictionary", "variable definition",
    "computational resource", "cpu", "package",
}
FIGURE_TABLE_SIGNALS = {"table", "figure", "plot", "appendix table", "appendix figure"}
ALGORITHM_SIGNALS = {"algorithm", "pseudocode", "implementation", "routine", "procedure"}
MODEL_SETUP_SIGNALS = {
    "assumption", "definition", "benchmark", "objective", "information structure",
    "feasible set", "uncertainty set", "notation", "primitive",
}
BASE_MODEL_SIGNALS = {
    "base model", "baseline model", "parsimonious model", "problem formulation",
    "model formulation", "distribution network", "state variable", "decision environment",
    "timing", "action", "cost function", "reward function", "transition",
}
GENERAL_MODEL_SIGNALS = {
    "general model", "generalized model", "generalization", "relaxes the baseline",
    "relaxing baseline", "extended model", "model extension", "general values",
}
CALIBRATION_SIGNALS = {
    "calibration", "calibrate", "fitting", "fit", "decensoring", "lead-time distribution",
    "lead time distribution", "demand estimation", "data cleaning", "parameter table",
    "scenario grid", "extra scenarios", "simulation scenario", "implementation detail",
    "distribution fitting", "estimate dealer", "estimated directly from data",
}


def has_any(text: str, signals: set[str]) -> bool:
    return any(signal in text for signal in signals)


def clean_item(line: str) -> str:
    line = line.strip()
    line = re.sub(r"^\s*(?:[-*+]|\d+[.)])\s*", "", line)
    return line.strip()


def crossref(placement: str, item: str) -> str:
    lower = item.lower()
    if placement == "Main text":
        return "Interpret in the body near the result."
    if placement == "Main text summary plus appendix":
        if has_any(lower, CENTRAL_DERIVATION_SIGNALS):
            return "State what the derivation creates before the pointer; put algebraic verification in Appendix A."
        if "proof" in lower or has_any(lower, PROOF_DETAIL_SIGNALS | PROOF_IDEA_SIGNALS):
            return "Keep the proof move in nearby body prose and put complete verification in Appendix A; preserve any established formal proof-pointer convention."
        if has_any(lower, ROBUSTNESS_SIGNALS | VALIDITY_SIGNALS):
            return "State the robustness conclusion in the body; put full tables and variants in Online Appendix EC.x."
        return "Keep the takeaway in the local body passage around the appendix pointer; put details in Appendix B."
    if placement == "Regular appendix":
        return "Keep the reference beside the relevant result package, which must also contain interpretation or any needed proof checkpoint."
    if placement == "Online appendix or e-companion":
        return "Keep nearby body prose stating what the supplement verifies, preserves, or changes."
    if placement == "Replication package":
        return "Mention in the data/code availability statement."
    return "Check whether the body still carries the main claim."


def classify_item(item: str, target: str, paper_type: str) -> tuple[str, str, str]:
    lower = item.lower()
    focused = "focused" in paper_type.lower()
    target_lower = target.lower()

    if has_any(lower, REPLICATION_SIGNALS):
        return (
            "Replication package",
            "Code, data, README, dictionaries, and computational details support reproducibility rather than first-pass contribution.",
            crossref("Replication package", item),
        )

    if has_any(lower, MODEL_SETUP_SIGNALS) and not has_any(
        lower, NUMERICAL_SIGNALS | FIGURE_TABLE_SIGNALS | ROBUSTNESS_SIGNALS
    ):
        if has_any(lower, GENERAL_MODEL_SIGNALS) and not has_any(lower, BODY_SIGNALS):
            return (
                "Main text summary plus appendix",
                "A general model usually verifies scope. Keep the takeaway in the body and put the full generalized formulation and proof in the appendix unless it changes the main mechanism.",
                crossref("Main text summary plus appendix", item),
            )
        if "notation" in lower and not has_any(lower, BODY_SIGNALS):
            return (
                "Regular appendix",
                "Long notation tables can move, but definitions needed to interpret a main result should remain in the body.",
                crossref("Regular appendix", item),
            )
        return (
            "Main text",
            "Assumptions, objectives, benchmarks, and information structure are needed to interpret the result.",
            crossref("Main text", item),
        )

    if has_any(lower, BASE_MODEL_SIGNALS) and not has_any(lower, CALIBRATION_SIGNALS | GENERAL_MODEL_SIGNALS):
        return (
            "Main text",
            "The base model establishes the formal or decision environment and the states, actions, objective, assumptions, or comparator that the headline results actually use.",
            crossref("Main text", item),
        )

    if has_any(lower, GENERAL_MODEL_SIGNALS):
        if has_any(lower, BODY_SIGNALS) or any(term in lower for term in {"changes mechanism", "main mechanism", "headline"}):
            return (
                "Main text summary plus appendix",
                "If the general model changes interpretation, keep the body takeaway and move technical details.",
                crossref("Main text summary plus appendix", item),
            )
        return (
            "Online appendix or e-companion",
            "A general model that only verifies scope usually belongs in the supplement after the baseline mechanism is explained.",
            crossref("Online appendix or e-companion", item),
        )

    if has_any(lower, CALIBRATION_SIGNALS):
        if has_any(lower, BODY_SIGNALS | VALIDITY_SIGNALS) or any(term in lower for term in {"primary comparison", "headline comparison", "trust"}):
            return (
                "Main text summary plus appendix",
                "Calibration needed for reviewer trust should be summarized in the body, with full fitting and scenario details in the appendix.",
                crossref("Main text summary plus appendix", item),
            )
        return (
            "Online appendix or e-companion",
            "Detailed calibration, fitting, decensoring, parameter tables, and extra scenarios support implementation rather than first-pass contribution.",
            crossref("Online appendix or e-companion", item),
        )

    if has_any(lower, ROUTINE_DERIVATION_SIGNALS) and not has_any(lower, BODY_SIGNALS | CENTRAL_DERIVATION_SIGNALS):
        return (
            "Regular appendix",
            "Routine derivation details verify the body result after the body states the object, key move, and interpretation.",
            crossref("Regular appendix", item),
        )

    if has_any(lower, CENTRAL_DERIVATION_SIGNALS):
        if has_any(lower, ROUTINE_DERIVATION_SIGNALS) and not has_any(lower, BODY_SIGNALS):
            return (
                "Regular appendix",
                "KKT checks, constants, repeated cases, and mechanical verification belong in an appendix unless they define the main object.",
                crossref("Regular appendix", item),
            )
        if focused:
            return (
                "Main text summary plus appendix",
                "The derivation creates a formal object used by the result. In a focused technical paper, keep the derivation logic in the published paper and move only mechanical checks.",
                crossref("Main text summary plus appendix", item),
            )
        return (
            "Main text summary plus appendix",
            "A central derivation should appear in the body as a start point, key move, and resulting object, with algebra and verification in the appendix.",
            crossref("Main text summary plus appendix", item),
        )

    if has_any(lower, PROOF_DETAIL_SIGNALS):
        if focused:
            if not (has_any(lower, PROOF_IDEA_SIGNALS | BODY_SIGNALS) or "main theorem" in lower):
                return (
                    "Regular appendix",
                    "Focused technical papers should keep proofs in the published paper, but auxiliary lemmas and routine verification can sit in a regular appendix rather than an online companion.",
                    crossref("Regular appendix", item),
                )
            return (
                "Main text summary plus appendix",
                "Focused technical papers should not hide proofs in an online companion. Keep the essential proof in the published paper and move only routine details.",
                crossref("Main text summary plus appendix", item),
            )
        if has_any(lower, PROOF_IDEA_SIGNALS) or has_any(lower, BODY_SIGNALS):
            return (
                "Main text summary plus appendix",
                "The proof idea helps reviewers trust the theorem, but routine verification can move.",
                crossref("Main text summary plus appendix", item),
            )
        return (
            "Regular appendix",
            "Full proofs, auxiliary lemmas, algebra, and case checks verify the body result without carrying the first-pass story.",
            crossref("Regular appendix", item),
        )

    if has_any(lower, FORMAL_RESULT_SIGNALS):
        return (
            "Main text",
            "The formal result supports the paper's contribution and should be stated and interpreted in the body.",
            crossref("Main text", item),
        )

    if has_any(lower, ROBUSTNESS_SIGNALS | VALIDITY_SIGNALS):
        if has_any(lower, VALIDITY_SIGNALS) or has_any(lower, BODY_SIGNALS):
            return (
                "Main text summary plus appendix",
                "Validity-critical checks should be visible in the body, with full variants moved to the appendix.",
                crossref("Main text summary plus appendix", item),
            )
        return (
            "Online appendix or e-companion",
            "Secondary robustness and sensitivity checks stress-test the claim after the primary result is clear.",
            crossref("Online appendix or e-companion", item),
        )

    if has_any(lower, EXTENSION_SIGNALS):
        if has_any(lower, BODY_SIGNALS) or "changes" in lower or "mechanism" in lower:
            return (
                "Main text summary plus appendix",
                "An extension that changes interpretation deserves a body takeaway and appendix details.",
                crossref("Main text summary plus appendix", item),
            )
        return (
            "Online appendix or e-companion",
            "Scope extensions that do not change the main mechanism usually belong in the supplement.",
            crossref("Online appendix or e-companion", item),
        )

    if has_any(lower, NUMERICAL_SIGNALS | FIGURE_TABLE_SIGNALS):
        if has_any(lower, BODY_SIGNALS) or "preferred" in lower or "headline" in lower:
            return (
                "Main text",
                "Primary figures, tables, simulations, and applications establish the headline evidence.",
                crossref("Main text", item),
            )
        if has_any(lower, EXTRA_SIGNALS | ROBUSTNESS_SIGNALS):
            return (
                "Online appendix or e-companion",
                "Extra tables, parameter sweeps, and secondary metrics support rather than carry the claim.",
                crossref("Online appendix or e-companion", item),
            )
        if "management science" in target_lower:
            return (
                "Main text",
                "Management Science readers need the primary empirical or numerical pattern in the body.",
                crossref("Main text", item),
            )
        return (
            "Main text summary plus appendix",
            "Report the primary comparison in the body and put design minutiae or extra settings in the appendix.",
            crossref("Main text summary plus appendix", item),
        )

    if has_any(lower, ALGORITHM_SIGNALS):
        if "implementation" in lower or "helper" in lower or "pseudocode" in lower:
            return (
                "Regular appendix",
                "Helper routines and implementation details verify reproducibility after the body explains the algorithm.",
                crossref("Regular appendix", item),
            )
        return (
            "Main text",
            "A central algorithm should be named and explained in the body, with implementation details moved out.",
            crossref("Main text", item),
        )

    return (
        "Needs judgment",
        "Classify by reader job. Keep it in the body if it is needed for first-pass understanding or reviewer trust.",
        "Decide after identifying the claim, evidence type, and role in the paper.",
    )


def read_items(args: argparse.Namespace) -> list[str]:
    raw_items = list(args.item or [])
    stdin_text = "" if sys.stdin.isatty() else sys.stdin.read()
    raw_items.extend(stdin_text.splitlines())
    return [clean_item(line) for line in raw_items if clean_item(line)]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", default="working paper", help="Management Science, Operations Research, M&SOM, or working paper")
    parser.add_argument("--paper-type", default="regular", help="regular, focused technical, empirical, theory, algorithm, or hybrid")
    parser.add_argument("--item", action="append", help="result item; can be repeated. If omitted, read one item per line from stdin")
    args = parser.parse_args()

    items = read_items(args)
    if not items:
        print("No result items provided. Pass --item repeatedly or pipe one item per line.")
        return 1

    print("| Item | Suggested placement | Reason | Body cross-reference |")
    print("|---|---|---|---|")
    for item in items:
        placement, reason, cref = classify_item(item, args.target, args.paper_type)
        print(f"| {item} | {placement} | {reason} | {cref} |")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

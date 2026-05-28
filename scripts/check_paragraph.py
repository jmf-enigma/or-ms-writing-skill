#!/usr/bin/env python3
"""Lightweight OR/MS paragraph quality check."""

from __future__ import annotations

import argparse
import re
import sys


ACTORS = {
    "platform", "seller", "firm", "regulator", "manager", "customer", "consumer",
    "player", "policymaker", "algorithm", "service provider", "decision maker",
    "hospital", "clinic", "patient", "physician", "manufacturer", "retailer",
    "supplier", "planner", "school", "worker", "employer", "agency", "investor",
    "lender", "auditor", "analyst", "utility", "city", "operator", "community",
    "platforms", "sellers", "firms", "regulators", "managers", "customers",
    "consumers", "players", "policymakers", "algorithms", "service providers",
    "decision makers", "hospitals", "clinics", "patients", "physicians",
    "manufacturers", "retailers", "suppliers", "planners", "schools", "workers",
    "employers", "agencies", "investors", "lenders", "auditors", "analysts",
    "utilities", "cities", "operators", "communities", "users",
    "volunteer", "volunteers", "opportunity", "opportunities", "nonprofit",
    "nonprofits", "cashier", "cashiers", "employee", "employees", "worker",
    "workers", "buyer", "buyers", "conservation planner", "species",
    "decision maker", "decision makers",
}
DECISIONS = {
    "price", "pricing", "match", "allocate", "recommend", "learn", "regulate",
    "design", "choose", "set", "offer", "assign", "optimize", "inspect",
    "schedule", "triage", "route", "source", "stock", "replenish", "disclose",
    "target", "lend", "report", "audit", "dispatch", "invest", "admit",
    "train", "monitor", "comply", "explore", "exploit",
    "acquire", "accept", "refer", "share", "invite", "engage",
    "sourcing", "ordering", "order", "procure", "procurement",
    "disclosure", "measure", "elicit", "standardize", "implement",
    "rank", "display", "scan", "survey", "protect", "front-load",
}
FRICTIONS = {
    "fairness", "uncertain", "ambiguity", "capacity", "churn", "disengagement",
    "uncertainty", "unknown", "forecast", "signal", "demand uncertainty",
    "learning", "herding", "incentive", "constraint", "trade-off", "externality",
    "strategic", "delay", "risk", "welfare",
    "no-show", "selection", "bias", "privacy", "agency", "congestion",
    "reliability", "emissions", "equity", "resilience", "attrition",
    "delayed feedback", "information asymmetry", "compliance",
    "competition", "cannibalization", "margin loss", "limited information",
    "online arrival", "online arrivals", "censoring", "censored",
    "nonstationary", "non-stationarity", "change point", "change-point",
    "demand shift", "demand shifts", "misspecification",
    "managerial inattention", "measurement error", "measurement challenge",
    "calibration", "coordination cost", "coordination costs",
    "information acquisition", "false negatives", "skill disparity",
}
MECHANISM_MARKERS = {"because", "therefore", "thus", "when", "whereas", "while", "however"}
ELEGANCE_HINGES = {
    "although", "but", "because", "despite", "however", "instead", "otherwise",
    "rather than", "relative to", "compared with", "consistent with", "whereas",
    "while", "when", "yet",
}
EVIDENCE = {
    "theorem", "proposition", "lemma", "model", "simulation", "experiment", "data",
    "estimate", "result", "proof", "benchmark", "case study", "numerical",
    "counterfactual", "identification", "field", "administrative data", "regret bound",
    "approximation", "characterization", "optimization", "formulation",
    "coefficient", "regression", "estimating equation", "table", "figure",
    "potential outcome", "treatment contrast", "calibration measure",
}
FORMAL_OBJECTS = {
    "policy", "threshold", "regime", "constraint", "objective", "state", "action",
    "equilibrium", "relaxation", "bound", "approximation", "regret", "estimator",
    "counterfactual", "allocation", "pricing", "schedule", "assortment", "inventory",
    "ranking", "matching", "routing", "disclosure", "decision variable", "solution",
    "decision rule", "construct", "measure", "coefficient", "regression",
    "estimating equation", "potential outcome", "treatment effect", "treatment contrast",
    "calibration", "belief state", "sufficient statistic", "recursive representation",
    "incentive constraint", "continuation utility",
}
BENCHMARKS = {
    "benchmark", "first-best", "first best", "oracle", "myopic", "static policy",
    "current practice", "status quo", "fluid", "lp relaxation", "complete information",
    "no information", "unconstrained", "offline optimum", "clairvoyant", "baseline",
    "existing ranking", "existing algorithm", "current algorithm", "incumbent policy",
    "incumbent algorithm", "incumbent rule", "current policy", "relaxed problem",
    "relaxed policy", "original policy class",
}
RESULT_TYPES = {
    "existence", "unique", "uniqueness", "threshold", "comparative static",
    "monotone", "monotonicity", "approximation ratio", "regret", "bound",
    "converges", "convergence", "identification", "welfare", "characterization",
    "dominates", "optimality", "equilibrium",
}
MATH_MOVES = {
    "coupling", "convexity", "concavity", "submodular", "submodularity",
    "monotonicity", "kkt", "fixed point", "induction", "contradiction",
    "concentration", "martingale", "duality", "relaxation", "rounding",
    "exchange argument", "envelope", "decomposition", "bounding",
    "couple", "couples", "coupled", "compare", "compares", "compared",
    "bound", "bounds", "bounded", "condition", "conditions", "conditioned",
}
DERIVATION_TERMS = {
    "derive", "derives", "derivation", "reformulate", "reformulates",
    "reformulation", "relax", "relaxes", "relaxation", "dual", "duality",
    "bellman", "decompose", "decomposes", "decomposition", "kkt",
    "first-order condition", "identifying expression", "plug-in estimator",
}
DERIVATION_START_MARKERS = {
    "objective", "constraint", "optimization problem", "program", "formulation",
    "bellman equation", "value function", "regret", "equilibrium constraint",
    "incentive constraint", "estimator", "estimating equation", "identifying expression",
    "definition", "benchmark", "first-order condition",
}
DERIVATION_MOVE_MARKERS = {
    "relaxation", "dual", "duality", "reformulation", "decomposition",
    "coupling", "conditioning", "exchange argument", "monotonicity",
    "convexity", "concavity", "bound", "upper bound", "lower bound",
    "plug-in", "threshold", "reduction", "kkt", "martingale", "concentration",
}
ROUTINE_DETAIL_TERMS = {
    "routine algebra", "algebraic details", "kkt verification", "constant tracking",
    "constants", "case split", "case splits", "boundary cases",
    "concentration constants", "summation details", "variance calculation",
    "technical lemma", "auxiliary lemma", "induction details",
}
ASSUMPTION_ROLE_WORDS = {
    "identify", "identification", "tractable", "tractability", "bound", "benchmark",
    "isolate", "simplify", "standard", "satisfy", "example", "examples", "ensures",
    "guarantees", "approximation", "relaxation", "regularity", "feasible",
}
INTERPRETATION_MARKERS = {
    "means", "implies", "suggests", "intuition", "in words", "operationally",
    "managerial", "decision", "policy", "because", "when", "relative to",
    "compared with", "benchmark",
}
EMPIRICAL_DESIGN_MARKERS = {
    "variation", "identification", "instrument", "exogenous", "random", "treatment",
    "control", "difference-in-differences", "diff-in-diff", "event study", "fixed effect",
    "robustness", "sensitivity", "placebo", "measurement error", "balance",
    "randomly assign", "randomly assigned", "potential outcome", "treatment contrast",
    "empirical framework", "follow-up experiment", "heterogeneous treatment",
    "spillover", "spillovers", "customer sorting",
}
FORMAL_WORD_SUPPORTS = {
    "near-optimal": {"regret", "bound", "rate", "lower bound", "oracle", "benchmark", "approximation"},
    "minimax": {"risk", "rate", "lower bound", "localization", "optimality", "class"},
    "tractable": {"convex", "program", "polynomial", "reformulation", "decomposition", "approximation"},
    "robust": {"uncertainty", "worst-case", "misspecification", "sensitivity", "out-of-sample", "transport", "ball", "benchmark"},
    "adaptive": {"policy", "algorithm", "assortment", "decision", "replacement", "state", "posterior", "observation"},
    "nonparametric": {"decision rule", "function", "policy class", "distribution", "estimator"},
    "finite-sample": {"sample", "probability", "confidence", "bound", "guarantee"},
    "data-driven": {"sample", "transaction", "historical", "censored", "contextual", "recommendation", "out-of-sample", "validation"},
}
TECHNICAL_VERB_OBJECTS = {
    "formulate": {"problem", "model", "objective", "decision rule", "policy", "mapping", "uncertainty set", "program", "optimization", "formulation"},
    "formulates": {"problem", "model", "objective", "decision rule", "policy", "mapping", "uncertainty set", "program", "optimization", "formulation"},
    "derive": {"expression", "bound", "guarantee", "reformulation", "condition", "ratio", "rate", "dual"},
    "derives": {"expression", "bound", "guarantee", "reformulation", "condition", "ratio", "rate", "dual"},
    "establish": {"theorem", "bound", "guarantee", "rate", "ratio", "characterization", "optimality", "convergence"},
    "establishes": {"theorem", "bound", "guarantee", "rate", "ratio", "characterization", "optimality", "convergence"},
    "identify": {"condition", "variation", "mechanism", "channel", "channels", "source", "class", "property", "case", "structure"},
    "identifies": {"condition", "variation", "mechanism", "channel", "channels", "source", "class", "property", "case", "structure"},
}
MODEL_MATH_MARKERS = {
    "denote", "denotes", "represent", "represents", "where", "objective",
    "constraint", "feasible", "decision", "random", "observe", "observes",
    "conditional", "benchmark", "policy", "rule",
}
MODEL_TERMS = {
    "model", "framework", "algorithm", "policy", "theorem", "proposition",
    "equilibrium", "optimization", "regret", "bound", "estimator",
}
STRICT_MATH_TERMS = {
    "theorem", "proposition", "lemma", "optimal", "optimality", "equilibrium",
    "regret", "approximation", "bound", "convergence", "identification",
}
MODEL_NARRATION_MARKERS = {
    "agent", "seller", "buyer", "firm", "platform", "manager", "customer", "patient",
    "timing", "information", "observe", "observes", "choose", "chooses", "control",
    "objective", "constraint", "benchmark", "friction", "trade-off", "tradeoff",
    "mechanism", "when", "because", "under", "condition",
}
OVERLOADED_TERMS = {
    "causal": {"random", "instrument", "identification", "exogenous", "difference", "experiment", "estimate", "transport"},
    "optimal": {"objective", "constraint", "benchmark", "policy", "first-best", "proof", "theorem"},
    "equilibrium": {"agent", "strategy", "belief", "market", "seller", "buyer", "response"},
    "robust": {"sensitivity", "specification", "benchmark", "stress", "out-of-sample", "across", "uncertainty", "worst-case", "transport", "ball"},
    "fairness": {"constraint", "definition", "group", "protected", "welfare", "equity"},
    "welfare": {"consumer", "surplus", "profit", "social", "total", "definition"},
    "efficiency": {"cost", "wait", "throughput", "welfare", "productive", "operational", "objective", "connection", "connections", "access", "ranking"},
    "learning": {"belief", "demand", "feedback", "regret", "sample", "algorithm", "posterior"},
    "platform": {"seller", "buyer", "customer", "consumer", "user", "worker", "volunteer", "opportunity", "two-sided", "marketplace", "intermediary", "ranking", "display", "algorithm"},
    "data-driven": {"sample", "transaction", "censored", "limited data", "historical", "contextual", "out-of-sample", "misspecification"},
}
IMPLICATIONS = {
    "should", "implies", "suggests", "therefore", "manager", "policy", "regulator",
    "platform", "seller", "condition", "when", "if",
}
METRICS = {
    "profit", "revenue", "cost", "welfare", "consumer surplus", "producer surplus",
    "total surplus", "regret", "loss", "error", "forecast error", "waiting time",
    "delay", "queue length", "throughput", "service level", "fill rate", "stockout",
    "stockout risk", "conversion", "conversion rate", "purchase", "purchase incidence",
    "adoption", "reliance", "accuracy", "runtime", "complexity", "feasibility",
    "price", "demand", "sales", "market share", "match rate", "utilization",
    "objective value", "optimality gap", "approximation ratio", "bound", "rate",
    "estimate", "magnitude", "effect size", "connections", "access", "coverage",
    "exposure", "engagement", "retention", "calibration", "net confidence",
    "belief", "beliefs", "accuracy", "skill", "scan speed", "customer flow",
    "presence probability", "detection probability", "protection effort",
    "survey effort",
}
STRONG_COMPARISON_TERMS = {
    "outperform", "outperforms", "outperformed", "outperforming",
    "dominate", "dominates", "dominated", "dominance",
    "uniformly better", "strictly better", "superior",
}
SOFT_COMPARISON_TERMS = {
    "improve", "improves", "improved", "improving",
    "reduce", "reduces", "reduced", "reducing",
    "increase", "increases", "increased", "increasing",
    "lower", "lowers", "lowered", "higher",
}
VAGUE_MAGNITUDE_WORDS = {
    "substantial", "substantially", "large", "largely", "meaningful", "meaningfully",
    "considerable", "considerably", "dramatic", "dramatically", "material", "materially",
}
MAGNITUDE_SUPPORT_WORDS = {
    "percent", "percentage", "estimate", "estimated", "confidence interval", "standard error",
    "statistically", "economically", "magnitude", "effect size", "rate", "bound", "ratio",
    "regret", "approximation", "sample", "simulation", "table", "figure",
}
EMPTY_PHRASES = {
    "rapidly evolving landscape",
    "evolving landscape",
    "plays a crucial role",
    "is very important",
    "in today's",
    "in the modern era",
    "in recent years",
    "rapidly evolving",
    "increasingly important",
    "growing importance",
    "growing need",
    "great significance",
    "real-world applications",
    "real world applications",
    "complex and dynamic",
    "intricate",
    "meticulous",
    "comprehensive analysis",
    "comprehensive framework",
    "comprehensive approach",
    "complexities of",
    "wide range of applications",
    "many managerial implications",
    "important managerial implications",
    "practical implications",
    "it is worth noting",
    "it is important to note",
    "it should be noted",
    "it is crucial to",
    "it is essential to",
    "this highlights",
    "this underscores",
    "this paper aims to",
    "this paper contributes to the literature",
    "the remainder of this paper",
    "not only",
    "but also",
    "by doing so",
    "in order to",
    "the fact that",
    "provides insights",
    "provides valuable insights",
    "novel insights",
    "managerial insights",
    "deeper insights",
    "broader understanding",
    "complex dynamics",
    "compelling story",
    "rich narrative",
    "compelling narrative",
    "paints a picture",
    "tells a story",
    "managerial enlightenment",
    "management enlightenment",
    "reveals important insights",
    "uncovers complex dynamics",
    "highlights the importance",
    "shed light",
    "sheds light",
    "deep dive",
    "delve",
    "leverage",
    "utilize",
    "underscore",
    "underscores",
    "pivotal",
    "crucial",
    "vital",
    "groundbreaking",
    "cutting-edge",
    "seamless",
    "multifaceted",
    "foster",
    "realm",
    "landscape",
    "navigating",
    "tapestry",
    "at the forefront",
    "state-of-the-art",
    "novel framework",
    "improve decision-making",
    "improve decision making",
    "enhance performance",
    "enhances performance",
    "better outcomes",
    "real-world",
    "valuable",
    "impactful",
    "performance improvements",
    "decision-making framework",
}

ANCHOR_SENSITIVE_WEAK_PHRASES = {
    "leverage",
    "sheds light",
    "shed light",
    "underscore",
    "underscores",
    "crucial",
    "novel insights",
    "managerial insights",
    "managerial implications",
    "practical implications",
    "state-of-the-art",
    "real-world",
    "valuable",
}

TRANSLATION_DRIFT_PHRASES = {
    "under the background of": "name the actual setting or decision instead of using a background frame.",
    "with the development of": "state the operational change, such as richer data, new platform rules, or algorithmic recommendations.",
    "according to the model": "make the model, proposition, estimate, table, or simulation the subject of the sentence.",
    "it can be seen that": "replace the empty observer with the result, comparison, theorem, estimate, or table.",
    "it can be found that": "replace the empty observer with the result, comparison, theorem, estimate, or table.",
    "it is found that": "name the empirical estimate, simulation, or theorem that supports the finding.",
    "based on the above analysis": "state the result or implication directly.",
    "this paper starts from": "use `we study`, `we examine`, `we model`, or name the decision directly.",
    "make a research": "use `study`, `examine`, `estimate`, `model`, or `characterize` with a concrete object.",
    "carry out research": "use `study`, `examine`, `estimate`, `model`, or `characterize` with a concrete object.",
    "has certain": "replace with a magnitude, condition, or restrained qualitative claim.",
    "to a certain extent": "replace with a magnitude, condition, or explicit caveat.",
    "combined with": "state whether the method uses data, imposes a constraint, conditions on covariates, or compares a benchmark.",
    "managerial enlightenment": "name who should act, what changes, and when; MS uses conditional implications, not enlightenment language.",
    "management enlightenment": "name who should act, what changes, and when; MS uses conditional implications, not enlightenment language.",
    "the model tells a story": "let the model show a relation between formal objects; name the decision, mechanism, metric, or condition.",
    "the results tell a story": "state the result, comparator, metric, and condition directly.",
}

ODD_COLLOCATIONS = {
    "managerial enlightenment": "Use `managerial implications` only if needed, and preferably name the action and condition directly.",
    "management enlightenment": "Use `managerial implications` only if needed, and preferably name the action and condition directly.",
    "optimize decision-making": "Name the decision and metric: choose a policy, set a price, reduce waiting time, improve profit, etc.",
    "optimize decision making": "Name the decision and metric: choose a policy, set a price, reduce waiting time, improve profit, etc.",
    "optimize the strategy": "Use `choose/design a policy`, `set a price`, `select an assortment`, or name the actual control.",
    "strategy optimization": "Use `policy choice`, `pricing decision`, `assortment choice`, `allocation rule`, or the actual control.",
    "has important influence on": "Use `affects`, `changes`, `shifts`, `alters`, or `is associated with`, depending on evidence.",
    "has a significant influence on": "Use `affects` or state the estimated effect; specify statistical or economic significance if needed.",
    "provide theoretical basis": "Name the theorem, condition, benchmark, or guarantee the paper actually provides.",
    "provides theoretical basis": "Name the theorem, condition, benchmark, or guarantee the paper actually provides.",
    "put forward a model": "Use `develop a model`, `study a model`, or name what the model captures.",
    "puts forward a model": "Use `develops a model`, `studies a model`, or name what the model captures.",
    "conduct research on": "Use `study`, `examine`, `estimate`, `model`, or `characterize` with a concrete object.",
    "carry out research on": "Use `study`, `examine`, `estimate`, `model`, or `characterize` with a concrete object.",
    "good performance": "Name the metric, benchmark, rate, guarantee, or field comparison.",
    "robustness proves": "Robustness checks support or preserve an interpretation; they rarely `prove` it.",
    "proves the validity": "Use `supports`, `preserves`, or name the validity threat ruled out.",
}

ODD_PREPOSITION_PATTERNS = {
    r"\beffect to\b": "Use `effect on` an outcome or behavior.",
    r"\bimpact to\b": "Use `impact on` an outcome or behavior, or simply `affects`.",
    r"\brobust for\b": "Use `robust to` a specification, perturbation, or assumption change.",
    r"\bsensitive for\b": "Use `sensitive to` a parameter, assumption, or data choice.",
    r"\bcompare to the benchmark\b": "Use `compare with` or `relative to` when making an analytical benchmark comparison.",
    r"\bimprove .* than\b": "Use `improve relative to` or `perform better than`, with a named metric.",
    r"\bbased on the above\b": "State the result or implication directly instead of referring to `the above`.",
}

EMPTY_ING = {
    "ensuring",
    "showcasing",
    "highlighting",
    "underscoring",
    "leveraging",
    "utilizing",
    "navigating",
}

PROOF_IDEA_STYLE_WORDS = {
    "elegant", "delicate", "subtle", "beautiful", "deep", "illuminates",
    "reveals", "uncovers", "heart of the proof", "dance", "surprisingly simple",
}

LLM_ASSOCIATED_WORDS = {
    "delve", "delves", "delving", "underscore", "underscores", "underscoring",
    "intricate", "pivotal", "meticulous", "multifaceted", "comprehensive",
    "realm", "landscape", "showcasing", "commendable", "transformative",
    "innovative", "crucial", "vital",
}

GENERIC_GAP_PATTERNS = {
    "fills a gap",
    "fill a gap",
    "gap in the literature",
    "underexplored",
    "limited attention",
    "little is known",
    "has not been studied",
}

METHOD_FIRST_OPENERS = {
    "using", "by using", "by leveraging", "leveraging", "utilizing", "through",
    "based on", "drawing on", "with a",
}

CLAIM_VERB_SUPPORTS = {
    "establish": {"theorem", "proof", "proposition", "lemma", "bound", "show"},
    "establishes": {"theorem", "proof", "proposition", "lemma", "bound", "show"},
    "prove": {"theorem", "proof", "proposition", "lemma"},
    "proves": {"theorem", "proof", "proposition", "lemma"},
    "demonstrate": {"experiment", "estimate", "data", "simulation", "theorem", "proof", "result"},
    "demonstrates": {"experiment", "estimate", "data", "simulation", "theorem", "proof", "result"},
}

WEAK_THIS_VERBS = {
    "allows",
    "enables",
    "ensures",
    "highlights",
    "underscores",
    "showcases",
    "demonstrates",
}

ROADMAP_MARKERS = {
    "we first",
    "we then",
    "we next",
    "we finally",
    "finally, we",
    "first, we",
    "second, we",
    "third, we",
    "in the first step",
    "in the second step",
}

COLON_ROADMAP_LABELS = {
    "approach",
    "contribution",
    "finding",
    "implication",
    "intuition",
    "key finding",
    "key implication",
    "key insight",
    "key result",
    "managerial implication",
    "mechanism",
    "proof idea",
    "result",
    "takeaway",
}

STORYCRAFT_SHELLS = {
    "this paper provides insights",
    "our study provides insights",
    "this study sheds light",
    "our study sheds light",
    "the model tells a story",
    "the results tell a story",
    "compelling story",
    "rich narrative",
    "managerial enlightenment",
    "managerial implications",
    "practical implications",
    "important implications",
    "novel insights",
}

TEMPLATE_SIGNAL_PHRASES = {
    "is useful because",
    "the theorem is useful because",
    "the result changes the managerial question",
    "the managerial implication is conditional",
    "the proof first reduces the problem",
    "the key step bounds",
    "the appendix gives the full derivation",
    "the displayed decomposition is the only step",
    "this does not imply",
    "good move",
}

ABSTRACT_NOUNS = {
    "framework", "insight", "insights", "mechanism", "mechanisms",
    "implication", "implications", "contribution", "contributions",
    "approach", "perspective", "paradigm", "lens", "narrative",
}
NOUN_PILE_HEADS = {
    "analysis", "approach", "design", "framework", "implication", "implications",
    "mechanism", "model", "optimization", "policy", "process", "strategy",
    "structure", "system",
}
WEAK_SUBJECT_PATTERNS = {
    r"there (?:is|are|exists|exist)\b": "empty `there` opener; name the actor, object, theorem, estimate, or mechanism that exists or changes.",
    r"it is (?:important|necessary|worth noting|clear|obvious|shown|found|seen)\b": "empty `it is` opener; make the result, condition, estimate, model, or proof step the subject.",
    r"this paper (?:aims to|seeks to|attempts to|tries to|provides|offers|contributes)\b": "`this paper` opener is weak here; use `we study`, `we estimate`, `we characterize`, or name the decision/model directly.",
    r"this study (?:aims to|seeks to|attempts to|tries to|provides|offers|contributes)\b": "`this study` opener is weak here; make the empirical design, setting, or result the subject.",
    r"the (?:analysis|framework|approach) (?:provides|offers|enables|allows|highlights|underscores)\b": "abstract subject with a weak verb; name the policy, model, estimator, theorem, or metric that does the work.",
}
PREPOSITION_CHAIN_TERMS = {
    "of", "for", "in", "with", "by", "under", "through", "between", "among",
    "from", "to", "on", "over",
}
NOMINALIZATION_SUFFIXES = ("tion", "sion", "ment", "ity", "ance", "ence", "ship", "ness")

HEAVY_RELATION_WORDS = {
    "whereas", "relative to", "compared with", "without", "consistent with",
    "thereby", "under", "conditional on", "in contrast", "moreover",
}

PAPER_OBJECT_OPENERS = {
    "the model", "the theorem", "the result", "the results", "the proof",
    "the analysis", "the framework", "the approach", "the algorithm",
    "this model", "this result", "this theorem", "this analysis",
}

RESULT_CATALOG_MARKERS = {
    "we show", "we find", "we establish", "we characterize", "we derive",
    "we prove", "we also", "we further", "we next", "our first",
    "our second", "our third",
}

STRONG_CLAIM_TRIGGERS = {
    "show", "shows", "showing", "find", "finds", "finding",
    "establish", "establishes", "established", "prove", "proves", "proved",
    "demonstrate", "demonstrates", "demonstrated", "identify", "identifies",
    "identified", "characterize", "characterizes", "characterized",
    "outperform", "outperforms", "dominate", "dominates", "optimal",
    "robust", "causal", "significant", "contribution", "contributes",
}

BOUNDARY_MARKERS = {
    "under", "when", "if", "only when", "provided that", "assuming",
    "given", "conditional on", "relative to", "compared with", "benchmark",
    "baseline", "policy class", "finite horizon", "asymptotic", "sample",
    "population", "data regime", "setting", "settings", "regime", "case",
    "condition", "assumption", "constraint", "information structure",
    "within", "among", "in our setting",
}

INFERENCE_MARKERS = {
    "therefore", "thus", "hence", "consequently", "implies", "imply",
    "suggests", "suggest", "indicates", "indicate", "should", "recommend",
    "recommendation", "managerial implication", "policy implication",
}
PREMISE_MARKERS = {
    "because", "as", "given", "under", "when", "if", "relative to",
    "compared with", "from", "based on", "consistent with", "in the model",
    "in the experiment", "the estimate", "the theorem", "the proposition",
    "the comparison", "the proof", "the table", "the figure",
}
CASUAL_REGISTER_PHRASES = {
    "a lot": "replace with a magnitude, frequency, or qualitative scope.",
    "lots of": "replace with a magnitude, frequency, or qualitative scope.",
    "big": "name the metric or use `large` only with magnitude support.",
    "huge": "name the metric or use `large` only with magnitude support.",
    "things": "name the construct, decision, metric, assumption, or result.",
    "stuff": "name the construct, decision, metric, assumption, or result.",
    "kind of": "state the relation precisely or remove the hedge.",
    "sort of": "state the relation precisely or remove the hedge.",
    "basically": "remove or replace with the exact simplification.",
    "really": "remove or replace with a measurable qualifier.",
    "very": "remove or replace with a measurable qualifier.",
}


def normalize_section(section: str) -> str:
    return section.strip().lower().replace("_", "-")


def core_checks_for_section(section: str) -> list[tuple[str, set[str], str]]:
    normalized = normalize_section(section)
    common = {
        "actor": (ACTORS, "Name the actor: hospital, platform, firm, agency, regulator, customer, etc."),
        "decision": (DECISIONS, "Name the decision: schedule, price, match, allocate, disclose, regulate, etc."),
        "friction": (FRICTIONS, "Name the friction: uncertainty, capacity, incentives, fairness, learning, delay, etc."),
        "mechanism": (MECHANISM_MARKERS, "Add a because/when/therefore sentence to show mechanism or condition."),
        "evidence": (EVIDENCE, "Tie the claim to a theorem, model, simulation, estimate, benchmark, or case study."),
        "implication": (IMPLICATIONS, "Say what follows for the actor, decision, or interpretation."),
        "formal object": (FORMAL_OBJECTS, "Name the policy, threshold, equilibrium, constraint, bound, estimator, or counterfactual."),
        "benchmark": (BENCHMARKS, "Name the comparator: oracle, first-best, current practice, relaxation, baseline, etc."),
        "proof move": (MATH_MOVES, "Name the load-bearing proof move: coupling, convexity, duality, relaxation, concentration, etc."),
    }
    if normalized in {"phrase", "sentence", "title", "micro", "micro-rewrite"}:
        return []
    if normalized in {"model", "modeling", "formulation"}:
        names = ["actor", "decision", "friction", "formal object"]
    elif normalized in {"result", "results", "theorem", "proposition"}:
        names = ["evidence", "formal object", "benchmark", "mechanism"]
    elif normalized in {"proof", "proof-exposition", "appendix-proof"}:
        names = ["evidence", "formal object", "proof move"]
    elif normalized in {"placement", "appendix", "online-appendix", "e-companion", "supplement"}:
        names = ["evidence", "formal object", "benchmark"]
    elif normalized in {"related", "related-work", "literature"}:
        names = ["decision", "friction", "evidence"]
    elif normalized in {"managerial", "managerial-implications", "implications"}:
        names = ["actor", "decision", "mechanism", "implication"]
    else:
        names = ["actor", "decision", "friction", "mechanism", "evidence", "implication"]
    return [(name, *common[name]) for name in names]


def contains_any(text: str, items: set[str]) -> bool:
    lower = text.lower()
    return any(item in lower for item in items)


def contains_term(text: str, items: set[str]) -> bool:
    lower = text.lower()
    for item in items:
        pattern = r"\b" + re.escape(item).replace(r"\ ", r"\s+") + r"\b"
        if re.search(pattern, lower):
            return True
    return False


def long_sentences(text: str) -> list[str]:
    sentences = re.split(r"(?<=[.!?])\s+", text.strip())
    return [s for s in sentences if len(s.split()) > 42]


def sentence_openers(text: str) -> list[str]:
    sentences = re.split(r"(?<=[.!?])\s+", text.strip())
    openers = []
    for sentence in sentences:
        match = re.search(r"\b[A-Za-z]+\b", sentence)
        if match:
            openers.append(match.group(0).lower())
    return openers


def repeated_openers(text: str) -> list[str]:
    openers = sentence_openers(text)
    repeats = []
    for i in range(len(openers) - 2):
        if openers[i] == openers[i + 1] == openers[i + 2]:
            repeats.append(openers[i])
    return sorted(set(repeats))


def repeated_object_openers(text: str) -> list[str]:
    sentences = [sentence.strip().lower() for sentence in re.split(r"(?<=[.!?])\s+", text.strip()) if sentence.strip()]
    hits = []
    for sentence in sentences:
        for opener in PAPER_OBJECT_OPENERS:
            if sentence.startswith(opener):
                hits.append(opener)
                break
    if len(hits) >= 3:
        return sorted(set(hits))
    return []


def weak_this_sentences(text: str) -> list[str]:
    hits = []
    sentences = re.split(r"(?<=[.!?])\s+", text.strip())
    pattern = re.compile(r"^\s*This\s+(" + "|".join(sorted(WEAK_THIS_VERBS)) + r")\b", flags=re.I)
    precise_antecedents = ACTORS | DECISIONS | EVIDENCE | FORMAL_OBJECTS | BENCHMARKS | MATH_MOVES
    for idx, sentence in enumerate(sentences):
        match = pattern.search(sentence)
        if match:
            previous = sentences[idx - 1] if idx else ""
            if not previous or not contains_term(previous, precise_antecedents):
                hits.append(match.group(1).lower())
    return hits


def weak_subject_warnings(text: str) -> list[str]:
    warnings = []
    sentences = [sentence.strip() for sentence in re.split(r"(?<=[.!?])\s+", text.strip()) if sentence.strip()]
    for sentence in sentences:
        lower = sentence.lower()
        for pattern, advice in WEAK_SUBJECT_PATTERNS.items():
            if re.match(pattern, lower):
                warnings.append(advice)
                break
    return sorted(set(warnings))


def preposition_chain_warnings(text: str) -> list[str]:
    warnings = []
    sentences = [sentence.strip() for sentence in re.split(r"(?<=[.!?])\s+", text.strip()) if sentence.strip()]
    for sentence in sentences:
        words = re.findall(r"\b[A-Za-z][A-Za-z-]*\b", sentence.lower())
        if len(words) < 24:
            continue
        prep_count = sum(1 for word in words if word in PREPOSITION_CHAIN_TERMS)
        of_count = sum(1 for word in words if word == "of")
        if prep_count >= 6 or of_count >= 3:
            warnings.append(
                "preposition chain: a long sentence carries too many `of/for/in/with/by/under` phrases. Turn one phrase into the subject or main verb."
            )
            break
    return warnings


def noun_pile_warnings(text: str) -> list[str]:
    lower = text.lower()
    warnings = []
    head_pattern = "|".join(sorted(re.escape(head) for head in NOUN_PILE_HEADS))
    pile_pattern = re.compile(
        rf"\b(?:[a-z][a-z-]{{2,}}\s+){{3,}}(?:{head_pattern})\b",
        flags=re.I,
    )
    noun_pile_false_verbs = {
        "shows", "show", "compares", "compare", "uses", "use", "bounds", "bound",
        "constructs", "construct", "estimates", "estimate", "characterizes",
        "characterize", "proves", "prove", "derives", "derive", "reduces", "reduce",
        "improves", "improve", "interprets", "interpret", "identifies", "identify",
    }
    hits = []
    for match in pile_pattern.finditer(lower):
        hit = match.group(0)
        if any(re.search(rf"\b{verb}\b", hit) for verb in noun_pile_false_verbs):
            continue
        hits.append(hit)
    hits = sorted(set(hits))
    if hits:
        warnings.append(
            "noun pile detected: "
            + ", ".join(f"`{hit}`" for hit in hits[:3])
            + ". Rewrite as actor + verb + object, then add the condition or benchmark."
        )
    sentences = [sentence.strip() for sentence in re.split(r"(?<=[.!?])\s+", text.strip()) if sentence.strip()]
    for sentence in sentences:
        words = re.findall(r"\b[A-Za-z][A-Za-z-]*\b", sentence.lower())
        if len(words) < 24:
            continue
        nominalizations = [
            word for word in words
            if word in ABSTRACT_NOUNS or (len(word) > 6 and word.endswith(NOMINALIZATION_SUFFIXES))
        ]
        if len(nominalizations) >= 5:
            warnings.append(
                "nominalization density: "
                + ", ".join(f"`{word}`" for word in sorted(set(nominalizations))[:6])
                + ". Convert at least one abstraction into a subject or verb."
            )
            break
    return warnings


def template_residue_warnings(text: str, section: str) -> list[str]:
    normalized_section = normalize_section(section)
    if normalized_section in {"appendix-proof"}:
        return []
    lower = text.lower()
    warnings = []
    phrase_hits = sorted(phrase for phrase in TEMPLATE_SIGNAL_PHRASES if phrase in lower)
    if phrase_hits:
        warnings.append(
            "template residue detected: "
            + ", ".join(f"`{hit}`" for hit in phrase_hits)
            + ". Rewrite around the paper's local noun and verb instead of using a stock move."
        )

    abstract_hits = [
        noun for noun in ABSTRACT_NOUNS
        if re.search(rf"\b{re.escape(noun)}\b", lower)
    ]
    if len(abstract_hits) >= 4 and not has_number(text):
        warnings.append(
            "abstract-noun stack: "
            + ", ".join(f"`{hit}`" for hit in sorted(set(abstract_hits))[:6])
            + ". Replace at least one with the local object, metric, policy, estimate, or theorem."
        )

    relation_hits = [
        word for word in HEAVY_RELATION_WORDS
        if re.search(rf"\b{re.escape(word)}\b", lower)
    ]
    sentences = [sentence for sentence in re.split(r"(?<=[.!?])\s+", text.strip()) if sentence]
    if len(relation_hits) >= max(3, len(sentences) + 1):
        warnings.append(
            "over-engineered relation words: "
            + ", ".join(f"`{hit}`" for hit in sorted(set(relation_hits))[:6])
            + ". Keep only the relation that explains the next step."
        )

    object_openers = repeated_object_openers(text)
    if object_openers:
        warnings.append(
            "stiff sentence openings: "
            + ", ".join(f"`{hit}`" for hit in object_openers)
            + ". Vary the flow by letting one sentence inherit the prior object and the next add the new action, condition, or evidence."
        )

    return warnings


def placeholder_residue_warnings(text: str) -> list[str]:
    warnings = []
    bracket_slots = re.findall(r"\[[A-Za-z][^\[\]]{1,60}\]", text)
    if bracket_slots:
        shown = ", ".join(f"`{slot}`" for slot in bracket_slots[:5])
        warnings.append(f"unresolved placeholder(s) {shown}; replace slots with the paper's actual objects before finalizing.")
    if re.search(r"\b(actor|decision|friction|mechanism|benchmark|implication)\s*/\s*", text, flags=re.I):
        warnings.append("slash-list planning residue; convert diagnostic labels into ordinary prose.")
    return warnings


def result_catalog_warnings(text: str, section: str) -> list[str]:
    normalized_section = normalize_section(section)
    if normalized_section not in {"abstract", "introduction", "intro", "contribution", "results", "paragraph"}:
        return []
    lower = text.lower()
    hits = [marker for marker in RESULT_CATALOG_MARKERS if marker in lower]
    if len(hits) < 3:
        return []
    has_spine_signal = any(marker in lower for marker in {"main result", "primary result", "headline", "central", "spine", "we focus", "the key result"})
    if has_spine_signal:
        return []
    return [
        "result-catalog rhythm detected; choose the spine result and arrange other findings as support, mechanism, boundary, or robustness instead of giving every result equal weight."
    ]


def roadmap_rhythm_warnings(text: str, section: str) -> list[str]:
    normalized_section = normalize_section(section)
    if normalized_section in {"roadmap", "outline", "response", "referee-response"}:
        return []
    lower = text.lower()
    hits = sorted(marker for marker in ROADMAP_MARKERS if marker in lower)
    warnings = []
    if len(hits) >= 2:
        warnings.append(
            "itinerary rhythm detected: "
            + ", ".join(f"`{hit}`" for hit in hits)
            + ". In polished prose, organize by research objects, evidence, benchmarks, or mechanisms rather than the author's work order."
        )
    if re.search(r"\bfirst\b.*\bsecond\b.*\bthird\b", lower, flags=re.S) and normalized_section not in {"roadmap", "outline"}:
        warnings.append("numbered rhetorical sequence detected; use only when the reader needs an explicit roadmap.")
    return warnings


def weak_relative_clause_warnings(text: str) -> list[str]:
    warnings = []
    weak_which = re.findall(
        r",\s*which\s+(?:allows|enables|helps|ensures|highlights|underscores|demonstrates)\b",
        text,
        flags=re.I,
    )
    if weak_which:
        warnings.append("weak `which` clause; name the theorem, estimator, design, comparison, or mechanism that allows/enables the next claim.")
    return warnings


def passive_scent(text: str) -> int:
    return len(re.findall(r"\b(?:is|are|was|were|be|been|being)\s+\w+(?:ed|en)\b", text, flags=re.I))


def empty_ing_hits(text: str) -> list[str]:
    lower = text.lower()
    return sorted(word for word in EMPTY_ING if re.search(rf"\b{re.escape(word)}\b", lower))


def has_number(text: str) -> bool:
    return bool(re.search(r"\b\d+(?:\.\d+)?\b|[%$]", text))


def claim_strength_warnings(text: str) -> list[str]:
    lower = text.lower()
    warnings = []
    strong_hits = [term for term in STRONG_COMPARISON_TERMS if re.search(rf"\b{re.escape(term)}\b", lower)]
    soft_hits = [term for term in SOFT_COMPARISON_TERMS if re.search(rf"\b{re.escape(term)}\b", lower)]
    if strong_hits and not contains_any(text, BENCHMARKS):
        warnings.append(
            "strong comparison needs a comparator; name the baseline, oracle, current practice, relaxation, or policy class."
        )
    if (strong_hits or soft_hits) and not contains_any(text, METRICS):
        warnings.append(
            "comparative claim needs a metric; say whether profit, regret, welfare, cost, runtime, accuracy, or another outcome changes."
        )
    vague_hits = [word for word in VAGUE_MAGNITUDE_WORDS if re.search(rf"\b{re.escape(word)}\b", lower)]
    if vague_hits and not has_number(text) and not any(word in lower for word in MAGNITUDE_SUPPORT_WORDS):
        warnings.append(
            "vague magnitude word(s) "
            + ", ".join(f"`{word}`" for word in sorted(vague_hits))
            + " need a number, estimate, bound, confidence statement, or explicit qualitative caveat."
        )
    if "significant" in lower and not any(word in lower for word in {"statistically", "economically", "substantively", "magnitude", "percentage", "p-value", "standard error", "confidence interval"}):
        warnings.append("`significant` is ambiguous; specify statistical significance, economic magnitude, or substantive importance.")
    return warnings


def argument_evidence_boundary_warnings(text: str, section: str) -> list[str]:
    normalized_section = normalize_section(section)
    if normalized_section in {"phrase", "sentence", "title", "micro", "micro-rewrite"}:
        return []

    lower = text.lower()
    warnings = []
    has_strong_claim = any(re.search(rf"\b{re.escape(term)}\b", lower) for term in STRONG_CLAIM_TRIGGERS)
    if not has_strong_claim:
        return warnings

    has_support = (
        contains_any(text, EVIDENCE | RESULT_TYPES | MATH_MOVES)
        or contains_any(text, {"table", "figure", "appendix", "experiment", "estimate"})
        or has_number(text)
    )
    has_boundary = (
        contains_term(text, BOUNDARY_MARKERS | BENCHMARKS)
        or any(term in lower for term in {"sample of", "data from", "in the model", "in the experiment"})
    )

    if not has_support:
        warnings.append("argument-evidence-boundary: strong claim lacks a nearby support signal; name the theorem, estimate, simulation, table, benchmark, proof idea, or comparison that carries it.")
    if not has_boundary:
        warnings.append("argument-evidence-boundary: strong claim lacks a boundary; keep the assumption, benchmark, sample, setting, information structure, regime, or policy class near the claim.")

    sentences = [sentence for sentence in re.split(r"(?<=[.!?])\s+", text.strip()) if sentence]
    if len(sentences) >= 4:
        evidence_sentences = [sentence for sentence in sentences if contains_any(sentence, EVIDENCE | RESULT_TYPES | BENCHMARKS) or has_number(sentence)]
        if evidence_sentences and not any(contains_any(sentences[i], EVIDENCE | RESULT_TYPES | BENCHMARKS) or has_number(sentences[i]) for i in range(min(2, len(sentences)))):
            warnings.append("argument-evidence-boundary: evidence arrives late; consider moving the theorem, estimate, comparison, or benchmark closer to the claim it supports.")

    return warnings


def translation_drift_warnings(text: str) -> list[str]:
    lower = text.lower()
    return [
        f"`{phrase}` sounds translated; {advice}"
        for phrase, advice in TRANSLATION_DRIFT_PHRASES.items()
        if phrase in lower
    ]


def weak_phrase_warnings(text: str) -> list[str]:
    lower = text.lower()
    warnings = []
    anchor_terms = ACTORS | DECISIONS | METRICS | EVIDENCE | FORMAL_OBJECTS | BENCHMARKS | MATH_MOVES | FRICTIONS
    has_anchor = contains_term(text, anchor_terms)
    for phrase in sorted(EMPTY_PHRASES):
        if phrase not in lower:
            continue
        if phrase in ANCHOR_SENSITIVE_WEAK_PHRASES and has_anchor:
            warnings.append(
                f"anchor-sensitive phrase `{phrase}`; keep only if it is attached to a precise data source, theorem, mechanism, metric, or action."
            )
        else:
            warnings.append(f"replace `{phrase}` with the actual decision or implication.")
    return warnings


def word_choice_warnings(text: str) -> list[str]:
    lower = text.lower()
    warnings = [
        f"`{phrase}` is an odd collocation; {advice}"
        for phrase, advice in ODD_COLLOCATIONS.items()
        if phrase in lower
    ]
    for pattern, advice in ODD_PREPOSITION_PATTERNS.items():
        if re.search(pattern, lower):
            warnings.append(f"preposition/collocation issue: {advice}")
    if "leverage data" in lower or "leverages data" in lower or "leveraging data" in lower:
        warnings.append("`leverage data` is vague; say what the data record, reveal, identify, or make comparable.")
    if "provide insights" in lower or "provides insights" in lower:
        warnings.append("`provide insights` is vague; name the result, condition, metric, policy, theorem, or estimate.")
    if "practical significance" in lower:
        warnings.append("`practical significance` sounds translated; name the decision, metric, action, or operating condition.")
    return warnings


def overloaded_sentence_warnings(text: str) -> list[str]:
    sentences = re.split(r"(?<=[.!?])\s+", text.strip())
    categories = [
        ("actor", ACTORS),
        ("decision", DECISIONS),
        ("friction", FRICTIONS),
        ("evidence", EVIDENCE),
        ("formal object", FORMAL_OBJECTS),
        ("benchmark", BENCHMARKS),
        ("result type", RESULT_TYPES),
    ]
    warnings = []
    for sentence in sentences:
        words = re.findall(r"\b[\w-]+\b", sentence)
        if len(words) < 34:
            continue
        hits = [name for name, items in categories if contains_any(sentence, items)]
        if len(hits) >= 5 or (len(words) > 46 and len(hits) >= 4):
            warnings.append(
                "overloaded MS/OR sentence; split it into setup, result, and interpretation instead of packing "
                + ", ".join(hits)
                + " into one sentence."
            )
            break
    return warnings


def model_narration_warnings(text: str, section: str = "paragraph") -> list[str]:
    if normalize_section(section) in {
        "result", "results", "theorem", "proposition", "proof", "proof-exposition",
        "appendix-proof", "phrase", "sentence", "title", "micro", "micro-rewrite",
    }:
        return []
    lower = text.lower()
    if not contains_term(text, MODEL_TERMS):
        return []
    warnings = []
    marker_hits = [marker for marker in MODEL_NARRATION_MARKERS if marker in lower]
    if len(marker_hits) < 3:
        warnings.append("model narration is thin; name agents, timing/information, controls, objective, benchmark, or the friction the model isolates.")
    if re.search(r"\bwe (?:consider|develop|propose|study) (?:a|an|the)?\s*(?:stylized )?(?:model|framework|algorithm)\b", lower):
        first_sentence = re.split(r"(?<=[.!?])\s+", text.strip())[0].lower()
        if "decision" not in first_sentence and not contains_any(first_sentence, ACTORS):
            warnings.append("method-first opening; introduce the management decision and friction before `we consider/develop/propose a model`.")
    if "data-driven" in lower and not any(word in lower for word in {"sample", "transaction", "censored", "limited data", "historical", "contextual", "out-of-sample", "misspecification"}):
        warnings.append("data-driven claim is generic; say what the data reveal, what they miss, or how data quality/quantity changes the decision.")
    return warnings


def or_ms_spine_warnings(text: str) -> list[str]:
    lower = text.lower()
    warnings = []
    has_strict_math = any(term in lower for term in STRICT_MATH_TERMS)
    has_algorithm = re.search(r"\balgorithm\b", lower) is not None
    has_model_intro = re.search(r"\bwe (?:consider|develop|propose|study|model)\b", lower) is not None or has_algorithm
    if (has_strict_math or has_model_intro) and not contains_any(text, FORMAL_OBJECTS):
        warnings.append("formal object is missing; name the policy, threshold, equilibrium, constraint, bound, estimator, or counterfactual being studied.")
    if (has_strict_math or has_algorithm) and not contains_any(text, BENCHMARKS):
        warnings.append("benchmark is missing; compare against first-best, oracle, myopic, current practice, relaxation, baseline, or another explicit reference point.")
    if has_strict_math and not any(term in lower for term in {"under", "if", "when", "condition", "assumption", "benchmark", "asymptotic", "relative to"}):
        warnings.append("mathematical claim lacks a validity condition; state the assumption, regime, information structure, or benchmark near the claim.")
    if any(term in lower for term in {"theorem", "proposition", "lemma"}) and not contains_any(text, RESULT_TYPES):
        warnings.append("result type is implicit; say whether the result proves existence, uniqueness, a threshold, monotonicity, a bound, convergence, or a characterization.")
    if has_algorithm and not (
        any(term in lower for term in BENCHMARKS | {"performance", "regret", "approximation", "runtime", "complexity", "optimality gap"})
        or contains_any(text, METRICS)
    ):
        warnings.append("algorithm narration is thin; state the benchmark and performance metric.")
    if "proof" in lower and not contains_any(text, MATH_MOVES):
        warnings.append("proof narration is generic; name the mathematical move such as coupling, convexity, relaxation, concentration, fixed point, induction, or exchange argument.")
    return warnings


def msor_paper_craft_warnings(text: str, section: str) -> list[str]:
    lower = text.lower()
    normalized_section = section.lower().replace("_", "-")
    warnings = []
    is_result_context = normalized_section in {"result", "results", "proof"} or any(
        term in lower for term in {"theorem", "proposition", "lemma"}
    )
    has_formal_claim = any(term in lower for term in STRICT_MATH_TERMS | RESULT_TYPES)
    if is_result_context and has_formal_claim and not any(marker in lower for marker in INTERPRETATION_MARKERS):
        warnings.append("full-text craft issue; add a short comment sentence that translates the formal result into the decision, benchmark, or operational condition.")
    if normalized_section in {"model", "results", "paragraph"} and re.search(r"\bassum(?:e|es|ption|ptions)\b", lower):
        if not any(word in lower for word in ASSUMPTION_ROLE_WORDS):
            warnings.append("assumption is stated but not earned; say whether it identifies, simplifies, preserves tractability, bounds, isolates a mechanism, or matches standard examples.")
    if any(term in lower for term in {"causal", "identify", "identification"}) and "causal transport" not in lower:
        if not any(marker in lower for marker in EMPIRICAL_DESIGN_MARKERS):
            warnings.append("empirical design is underspecified; name the identifying variation, treatment/control comparison, robustness check, or institutional behavior supporting the claim.")
    return warnings


def ms_storycraft_warnings(text: str, section: str) -> list[str]:
    lower = text.lower()
    normalized_section = normalize_section(section)
    warnings = []
    if normalized_section in {"phrase", "sentence", "title", "micro", "micro-rewrite"}:
        return warnings
    if any(shell in lower for shell in STORYCRAFT_SHELLS):
        if not contains_term(text, ACTORS | DECISIONS | METRICS | FRICTIONS):
            warnings.append("MS story shell is generic; replace insight/implication language with the actor, decision, metric, friction, or condition that changes.")
    if normalized_section in {"abstract", "introduction", "intro", "paragraph"}:
        has_method = contains_any(text, EVIDENCE) or re.search(r"\bwe (?:use|conduct|run|develop|formulate|estimate|propose)\b", lower)
        has_decision_or_actor = contains_term(text, ACTORS | DECISIONS)
        has_friction = contains_term(text, FRICTIONS) or any(word in lower for word in {"however", "although", "whereas", "yet", "despite", "but"})
        if has_method and not has_decision_or_actor:
            warnings.append("MS story starts from method; first name the management decision, institution, actor, or metric the method is meant to explain.")
        if has_method and not has_friction:
            warnings.append("MS story lacks tension; say what standard practice, belief, model, or evidence cannot explain before presenting the method.")
    if normalized_section in {"abstract", "introduction", "intro", "contribution", "paragraph"}:
        if any(term in lower for term in {"we contribute", "contributes to", "contribution"}) and not any(
            marker in lower for marker in {"relative to", "whereas", "unlike", "prior", "existing", "standard", "benchmark", "literature", "stream"}
        ):
            warnings.append("contribution is unpositioned; state the prior stream, benchmark, design, or mechanism the paper departs from.")
    return warnings


def elegance_warnings(text: str, section: str) -> list[str]:
    normalized_section = normalize_section(section)
    if normalized_section in {
        "phrase", "sentence", "title", "micro", "micro-rewrite",
        "proof", "proof-exposition", "appendix-proof", "placement",
    }:
        return []
    lower = text.lower()
    sentences = [sentence for sentence in re.split(r"(?<=[.!?])\s+", text.strip()) if sentence]
    if len(sentences) < 2:
        return []
    has_research_object = (
        contains_term(text, ACTORS | DECISIONS | FRICTIONS | FORMAL_OBJECTS | BENCHMARKS)
        or contains_any(text, EVIDENCE | RESULT_TYPES)
    )
    has_method_or_result = (
        contains_any(text, EVIDENCE | RESULT_TYPES)
        or re.search(r"\bwe (?:study|develop|introduce|estimate|show|find|characterize|derive|propose|evaluate|compare)\b", lower)
    )
    has_hinge = any(marker in lower for marker in ELEGANCE_HINGES)
    if has_research_object and has_method_or_result and not has_hinge:
        return [
            "story feels flat; add one real hinge that explains the turn from old object to friction, method to result, benchmark to comparison, or result to boundary."
        ]
    return []


def language_model_math_warnings(text: str, section: str) -> list[str]:
    lower = text.lower()
    normalized_section = section.lower().replace("_", "-")
    warnings = []
    for word, supports in FORMAL_WORD_SUPPORTS.items():
        if re.search(rf"\b{re.escape(word)}\b", lower) and not any(support in lower for support in supports):
            warnings.append(f"`{word}` needs an anchor; add the object, benchmark, condition, uncertainty set, or performance metric.")
    for verb, objects in TECHNICAL_VERB_OBJECTS.items():
        if re.search(rf"\b{re.escape(verb)}\b", lower) and not any(obj in lower for obj in objects):
            warnings.append(f"`{verb}` needs a precise object; bind it to a problem, reformulation, bound, condition, source of variation, or policy class.")
    has_display_like_math = bool(re.search(r"[$=∈≤≥∑\\]|\b(?:min|max|argmin|argmax|inf|sup)\b", text))
    if normalized_section in {"model", "results", "proof", "paragraph"} and has_display_like_math:
        if not any(marker in lower for marker in MODEL_MATH_MARKERS):
            warnings.append("notation is under-explained; introduce what the display defines and translate the central variable, objective, constraint, or benchmark.")
    if "uncertainty set" in lower and not any(word in lower for word in {"preserve", "capture", "hedge", "conditional", "misspecification", "worst-case", "nominal"}):
        warnings.append("uncertainty set is floating; say what information structure, perturbation, or misspecification it captures.")
    if "it is easy to see" in lower or "it is obvious" in lower:
        warnings.append("proof prose hides a step; name the fact that makes it easy, such as monotonicity, feasibility, nonnegativity, convexity, or conditional independence.")
    if "some algebra" in lower:
        warnings.append("proof prose is too generic; say whether the step rearranges a Bellman equation, takes a dual, telescopes regret, or bounds a relaxation.")
    return warnings


def derivation_depth_warnings(text: str, section: str) -> list[str]:
    lower = text.lower()
    normalized_section = normalize_section(section)
    if normalized_section in {"phrase", "sentence", "title", "micro", "micro-rewrite"}:
        return []
    if not contains_term(text, DERIVATION_TERMS):
        return []
    warnings = []
    has_start = any(marker in lower for marker in DERIVATION_START_MARKERS)
    has_move = any(marker in lower for marker in DERIVATION_MOVE_MARKERS) or contains_any(text, MATH_MOVES)
    has_resulting_object = contains_any(text, FORMAL_OBJECTS | BENCHMARKS | RESULT_TYPES) or any(
        marker in lower for marker in {"resulting object", "policy class", "estimator", "bound", "rate", "threshold", "formula"}
    )
    mentions_appendix = any(term in lower for term in {"appendix", "online appendix", "e-companion", "supplement"})
    routine_detail = any(term in lower for term in ROUTINE_DETAIL_TERMS)

    if not has_start:
        warnings.append("derivation depth is thin; name the starting object, such as the objective, Bellman equation, estimator, regret definition, equilibrium constraint, or benchmark.")
    if not has_move:
        warnings.append("derivation lacks the load-bearing move; say whether the step uses a relaxation, dual, decomposition, coupling, conditioning argument, KKT conditions, or concentration bound.")
    if not has_resulting_object:
        warnings.append("derivation does not identify the resulting object; state the bound, policy, estimator, threshold, reformulation, or benchmark that the paper uses next.")
    if mentions_appendix and not has_move:
        warnings.append("appendix pointer is premature; give the proof idea or derivation checkpoint in the body before sending details to the appendix.")
    if routine_detail and not mentions_appendix and normalized_section not in {"appendix", "appendix-proof", "online-appendix", "e-companion", "supplement", "placement"}:
        warnings.append("routine verification appears body-bound; consider moving constants, KKT verification, case splits, or auxiliary lemmas to an appendix after a body-level checkpoint.")
    return warnings


def proof_idea_voice_warnings(text: str, section: str) -> list[str]:
    lower = text.lower()
    normalized_section = normalize_section(section)
    if normalized_section not in {"proof", "proof-exposition", "appendix-proof", "results", "theorem", "proposition"} and "proof" not in lower:
        return []
    warnings = []
    if re.search(r"\bproof idea\s*:", lower):
        warnings.append("avoid `Proof idea:` as a visible label in polished body prose; write the proof move as ordinary prose unless the venue or section structure requires the label.")
    if re.search(r"\bkey insight\s*:", lower):
        warnings.append("avoid `Key insight:` after a theorem; state what the result changes relative to the benchmark or condition.")
    style_hits = sorted(word for word in PROOF_IDEA_STYLE_WORDS if word in lower)
    if style_hits:
        warnings.append(
            "proof-idea voice is too stylized for MS; replace "
            + ", ".join(f"`{hit}`" for hit in style_hits)
            + " with plain proof verbs such as construct, decompose, bound, compare, apply, combine, show, or imply."
        )
    if any(term in lower for term in {"intuition behind the proof", "key intuition"}) and not contains_any(text, MATH_MOVES):
        warnings.append("proof idea sounds motivational; name the actual proof move, such as a relaxation, decomposition, coupling, concentration step, or upper bound.")
    return warnings


def appendix_placement_warnings(text: str, section: str) -> list[str]:
    lower = text.lower()
    normalized_section = normalize_section(section)
    mentions_appendix = any(term in lower for term in {"appendix", "online appendix", "e-companion", "supplement", "supplemental material"})
    warnings = []
    if not mentions_appendix and normalized_section not in {"placement", "appendix", "online-appendix", "e-companion", "supplement"}:
        return warnings
    has_formal_result = any(term in lower for term in {"theorem", "proposition", "lemma", "result", "estimate", "table", "figure"})
    if has_formal_result and not any(marker in lower for marker in INTERPRETATION_MARKERS):
        warnings.append("appendix reference cannot replace interpretation; keep the result's meaning, benchmark, or decision consequence in the body.")
    if "proof" in lower and "appendix" in lower and not contains_any(text, MATH_MOVES):
        warnings.append("before sending the proof to the appendix, give the main proof idea or load-bearing mathematical move in the body.")
    if any(term in lower for term in {"identification", "causal", "validity", "endogeneity", "robustness"}) and "appendix" in lower:
        if not any(term in lower for term in {"main text", "body", "section", "summarize", "report"}):
            warnings.append("validity-critical robustness or identification checks should be summarized in the body, with full tables in the appendix.")
    return warnings


def reviewer_calibration_warnings(text: str) -> list[str]:
    lower = text.lower()
    warnings = []
    for term, supports in OVERLOADED_TERMS.items():
        if term in lower and not any(support in lower for support in supports):
            warnings.append(f"`{term}` is overloaded; define it locally or add the evidence, benchmark, or design that supports this use.")
    novelty_hit = (
        re.search(r"\bnovel\b|\bnew\b|\bfirst\b", lower)
        and not re.search(r"\bfirst\s+(?:inequality|term|step|case|constraint|order|stage|period|round|line)\b", lower)
    )
    if novelty_hit and not any(word in lower for word in {"differs", "depart", "relative to", "benchmark", "literature", "stream"}):
        warnings.append("novelty claim may invite reviewer objections; state the precise departure from a benchmark or literature stream.")
    return warnings


def logical_inference_warnings(text: str, section: str) -> list[str]:
    normalized_section = normalize_section(section)
    if normalized_section in {"phrase", "title", "micro", "micro-rewrite"}:
        return []
    lower = text.lower()
    warnings = []
    inference_hit = any(re.search(rf"\b{re.escape(marker)}\b", lower) for marker in INFERENCE_MARKERS)
    if not inference_hit:
        return warnings

    has_premise = (
        contains_any(text, PREMISE_MARKERS | EVIDENCE | RESULT_TYPES | MATH_MOVES | BENCHMARKS)
        or has_number(text)
    )
    has_boundary = (
        contains_term(text, BOUNDARY_MARKERS | BENCHMARKS)
        or any(term in lower for term in {"in the model", "in the experiment", "in our sample"})
    )
    if not has_premise:
        warnings.append("logic jump: inference marker appears without a visible premise or evidence object; name the estimate, theorem, comparison, design feature, or proof move that supports it.")
    if any(term in lower for term in {"should", "recommend", "managerial implication", "policy implication"}) and not has_boundary:
        warnings.append("logic jump: recommendation lacks a condition; state when, for whom, or relative to which benchmark the implication follows.")

    sentences = [sentence.strip() for sentence in re.split(r"(?<=[.!?])\s+", text.strip()) if sentence.strip()]
    if sentences:
        first = sentences[0].lower()
        first_has_inference = any(re.search(rf"\b{re.escape(marker)}\b", first) for marker in INFERENCE_MARKERS)
        first_has_support = contains_any(first, EVIDENCE | RESULT_TYPES | MATH_MOVES | BENCHMARKS) or has_number(first)
        if first_has_inference and not first_has_support and len(sentences) > 1:
            warnings.append("logic order: the paragraph opens with an inference before giving the evidence; consider moving the theorem, estimate, comparison, or premise first.")
    return warnings


def academic_style_warnings(text: str) -> list[str]:
    lower = text.lower()
    warnings = []
    sentences = re.split(r"(?<=[.!?])\s+", text.strip())
    first_sentence = sentences[0].strip().lower() if sentences else ""
    if re.match(r"^(in recent years|with the rapid|in today's|in the modern era)\b", first_sentence):
        warnings.append("generic opener; start with the local decision, tension, setting, or claim.")
    if any(first_sentence.startswith(opener) for opener in METHOD_FIRST_OPENERS):
        warnings.append("method-first opener; consider naming the decision or friction before the method.")
    if any(pattern in lower for pattern in GENERIC_GAP_PATTERNS) and not contains_any(text, DECISIONS | FRICTIONS | EVIDENCE):
        warnings.append("generic gap; turn the gap into a decision problem, evidence limit, model limit, or unresolved mechanism.")
    if lower.count(" this ") + lower.startswith("this ") > 2:
        warnings.append("repeated `This`; name the object or mechanism instead of relying on pronoun flow.")
    for phrase, advice in CASUAL_REGISTER_PHRASES.items():
        if re.search(rf"\b{re.escape(phrase)}\b", lower):
            warnings.append(f"academic register: `{phrase}` is too casual; {advice}")
    if re.search(r"\b(?:clearly|obviously)\b", lower) and not contains_any(text, EVIDENCE | MATH_MOVES | RESULT_TYPES):
        warnings.append("academic register: `clearly/obviously` needs the proof fact, estimate, or assumption that makes the claim clear.")
    for verb, supports in CLAIM_VERB_SUPPORTS.items():
        if re.search(rf"\b{re.escape(verb)}\b", lower) and not any(support in lower for support in supports):
            warnings.append(f"`{verb}` is strong; add theorem/proof/estimate/simulation support or use a weaker evidence verb.")
    return warnings


def llm_style_warnings(text: str) -> list[str]:
    lower = text.lower()
    hits = sorted(word for word in LLM_ASSOCIATED_WORDS if re.search(rf"\b{re.escape(word)}\b", lower))
    warnings = []
    if hits:
        warnings.append("LLM-associated wording: " + ", ".join(f"`{hit}`" for hit in hits) + ". Keep only exact technical uses; otherwise replace with local objects, mechanisms, metrics, or conditions.")
    if len(hits) >= 2:
        warnings.append("LLM-associated word cluster; recent corpus studies show these words increasingly co-occur in AI-assisted academic prose.")
    return warnings


def punctuation_scent(text: str, allow_structured: bool = False) -> list[str]:
    warnings = []
    lower = text.lower()
    colon_count = text.count(":")
    em_dash_count = text.count("\u2014")
    en_dash_count = text.count("\u2013")
    double_dash_count = text.count(" -- ")
    spaced_hyphen_count = len(re.findall(r"\s-\s", text))
    semicolon_count = text.count(";")
    colon_labels = sorted(
        label for label in COLON_ROADMAP_LABELS
        if re.search(rf"\b{re.escape(label)}\b\s*:", lower)
    )
    formal_colons = len(re.findall(
        r"\b(?:assumption|definition|lemma|proposition|theorem|corollary|proof|case|step|table|figure|appendix)\s*(?:[A-Z]|\d+(?:\.\d+)*)?\s*:",
        lower,
    ))
    if colon_labels:
        warnings.append(
            "colon-led roadmap label(s) "
            + ", ".join(f"`{label}:`" for label in colon_labels)
            + "; rewrite as ordinary prose unless this is an actual section heading."
        )
    if colon_count and not allow_structured:
        warnings.append(f"{colon_count} colon(s); rewrite as ordinary manuscript sentences unless the colon marks a definition, assumption, proof label, display, table, or venue-required structure.")
    elif colon_count > max(1, formal_colons + 1):
        warnings.append(f"{colon_count} colon(s); keep structured punctuation rare, even when formal material is allowed.")
    if em_dash_count or en_dash_count or double_dash_count or spaced_hyphen_count:
        warnings.append("dash pivot detected; replace with a period, comma, parenthesis, or direct causal sentence.")
    if semicolon_count and not allow_structured:
        warnings.append(f"{semicolon_count} semicolon(s); split chained prose claims unless the semicolon clarifies a theorem condition, proof step, or formal list.")
    elif semicolon_count > 1:
        warnings.append(f"{semicolon_count} semicolon(s); split chained claims into sentences.")
    if len(re.findall(r"\bwhich\b", text, flags=re.I)) > 2:
        warnings.append("repeated `which` clauses; vary sentence structure.")
    return warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--section", default="paragraph", help="optional section name for reporting")
    parser.add_argument("--allow-structured-punctuation", action="store_true", help="allow limited colons/semicolons for structured abstracts, theorem titles, or formal fields")
    parser.add_argument("--fail-on-ai-scent", action="store_true", help="return a nonzero exit code when AI-scent wording or punctuation is detected")
    args = parser.parse_args()

    text = sys.stdin.read().strip()
    if not text:
        print("No paragraph provided.")
        return 1

    print(f"OR/MS paragraph diagnostic: section={args.section}")
    checks = core_checks_for_section(args.section)
    if not checks:
        print("- diagnostic signals: skipped for micro-level wording; inspect object, verb, and rhythm instead.")
    else:
        print(f"- diagnostic signals: adapted for {normalize_section(args.section)}; absence is a prompt, not a hard requirement.")
    for name, items, advice in checks:
        ok = contains_term(text, items)
        print(f"- {name}: {'present' if ok else 'absent'}" + ("" if ok else f" | Consider only if this paragraph's job needs it: {advice}"))

    lower = text.lower()
    for warning in weak_phrase_warnings(text):
        print(f"- weak phrase: {warning}")

    for word in empty_ing_hits(text):
        print(f"- empty -ing phrase: replace `{word}` with a concrete verb and object.")

    for warning in translation_drift_warnings(text):
        print(f"- translated-English drift: {warning}")

    word_choice_scent = word_choice_warnings(text)
    for warning in word_choice_scent:
        print(f"- word choice: {warning}")

    for warning in overloaded_sentence_warnings(text):
        print(f"- naturalness: {warning}")

    roadmap_scent = roadmap_rhythm_warnings(text, args.section)
    for warning in roadmap_scent:
        print(f"- naturalness: {warning}")

    weak_relative_scent = weak_relative_clause_warnings(text)
    for warning in weak_relative_scent:
        print(f"- naturalness: {warning}")

    template_scent = template_residue_warnings(text, args.section)
    for warning in template_scent:
        print(f"- read-aloud naturalness: {warning}")

    placeholder_scent = placeholder_residue_warnings(text)
    for warning in placeholder_scent:
        print(f"- template residue: {warning}")

    catalog_scent = result_catalog_warnings(text, args.section)
    for warning in catalog_scent:
        print(f"- manuscript judgment: {warning}")

    this_hits = weak_this_sentences(text)
    if this_hits:
        verbs = ", ".join(sorted(set(this_hits)))
        print(f"- weak `This` opener: `{verbs}`. Name the actor, mechanism, or result instead.")

    sentence_craft_scent = (
        weak_subject_warnings(text)
        + noun_pile_warnings(text)
        + preposition_chain_warnings(text)
    )
    for warning in sentence_craft_scent:
        print(f"- sentence craft: {warning}")

    for warning in model_narration_warnings(text, args.section):
        print(f"- MS model/data narration: {warning}")

    for warning in or_ms_spine_warnings(text):
        print(f"- OR/MS spine: {warning}")

    for warning in msor_paper_craft_warnings(text, args.section):
        print(f"- MS/OR full-text craft: {warning}")

    for warning in ms_storycraft_warnings(text, args.section):
        print(f"- MS whole-paper storycraft: {warning}")

    for warning in elegance_warnings(text, args.section):
        print(f"- MS elegance: {warning}")

    for warning in language_model_math_warnings(text, args.section):
        print(f"- MS/OR language-model-math: {warning}")

    for warning in derivation_depth_warnings(text, args.section):
        print(f"- derivation depth: {warning}")

    for warning in proof_idea_voice_warnings(text, args.section):
        print(f"- proof idea voice: {warning}")

    for warning in claim_strength_warnings(text):
        print(f"- claim strength: {warning}")

    for warning in argument_evidence_boundary_warnings(text, args.section):
        print(f"- {warning}")

    for warning in logical_inference_warnings(text, args.section):
        print(f"- logic and inference: {warning}")

    for warning in appendix_placement_warnings(text, args.section):
        print(f"- appendix placement: {warning}")

    for warning in reviewer_calibration_warnings(text):
        print(f"- reviewer calibration: {warning}")

    for warning in academic_style_warnings(text):
        print(f"- academic style: {warning}")

    llm_scent = llm_style_warnings(text)
    for warning in llm_scent:
        print(f"- AI-scent wording: {warning}")

    repeats = repeated_openers(text)
    if repeats:
        print(f"- repeated sentence opener: {', '.join(repeats)}. Vary the sentence starts.")

    passive_count = passive_scent(text)
    if passive_count > 2:
        print(f"- passive voice scent: {passive_count} likely passive construction(s). Use active voice unless the object matters more.")

    punctuation = punctuation_scent(text, allow_structured=args.allow_structured_punctuation)
    if punctuation:
        for warning in punctuation:
            print(f"- AI-scent punctuation: {warning}")
    else:
        print("- AI-scent punctuation: ok")

    too_long = long_sentences(text)
    if too_long:
        print(f"- long sentence: {len(too_long)} sentence(s) exceed 42 words; split before polishing.")
    else:
        print("- sentence length: ok")

    if args.fail_on_ai_scent and (
        punctuation
        or llm_scent
        or roadmap_scent
        or weak_relative_scent
        or template_scent
        or placeholder_scent
        or catalog_scent
        or this_hits
        or sentence_craft_scent
        or word_choice_scent
    ):
        return 2

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

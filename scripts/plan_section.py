#!/usr/bin/env python3
"""Print a compact OR/MS writing blueprint for a requested section."""

from __future__ import annotations

import argparse
import re
import textwrap


BLUEPRINTS = {
    "abstract": [
        "Decision: name the actor, choice, and operational stakes.",
        "Friction: name uncertainty, information, capacity, incentives, behavior, or constraints.",
        "Method: state analytical model, empirical design, algorithm, simulation, or hybrid approach.",
        "Result: give mechanisms and conditions, not theorem numbers alone.",
        "Implication: say who can act on the result and under what condition.",
    ],
    "introduction": [
        "Entry point: decision setting, standard model, institutional puzzle, technical obstacle, or empirical construct.",
        "Contrast object: current practice, canonical model, prior evidence, or literature default when it matters.",
        "Friction: why the contrast object cannot answer this version of the question.",
        "Trust device: experiment, institutional variation, theorem, model feature, construct validation, algorithmic guarantee, or benchmark.",
        "Study object: model, data, design, estimator, algorithm, policy, or formal problem after the question is legible.",
        "Findings in the right evidence register: estimate, theorem, guarantee, characterization, validation, or counterfactual.",
        "Contributions by audience or literature stream, grouped by what the reader learns.",
        "Implications and roadmap only when they help the lane and target journal.",
    ],
    "related": [
        "Stream 1: what it studies and the precise gap.",
        "Stream 2: contrast method or mechanism.",
        "Stream 3: position contribution without overclaiming.",
        "End with one sentence stating this paper's distinct angle.",
    ],
    "model": [
        "Lane choice: theory/problem formulation, empirical model, structural measurement device, or applied system model.",
        "Agents, timing, information, decisions.",
        "State/action, demand/payoff/transition primitives.",
        "Objective and constraints.",
        "Assumptions with short rationale.",
        "Reviewer concern the model answers: tractability, identification, mechanism isolation, implementation, or external validity.",
        "Benchmark, solution concept, and what the abstraction isolates.",
        "Main formulation display and one sentence translating the objective, constraints, and benchmark.",
    ],
    "results": [
        "Reminder of local setup.",
        "Formal proposition/theorem.",
        "Benchmark or standard intuition.",
        "Trust checkpoint: identification contrast, proof move, validation, placebo, approximation benchmark, or robustness conclusion when needed.",
        "Derivation checkpoint when the result depends on a relaxation, dual, Bellman equation, regret decomposition, or identifying expression.",
        "Intuition paragraph.",
        "Comparative static, regime, threshold, or mechanism.",
        "Managerial or policy implication.",
    ],
    "proof": [
        "If the input is rough proof notes, run plan_math_split.py before drafting.",
        "Plain proof idea with the constructed object, hard term, and load-bearing mathematical move; use one sentence if the proof is routine.",
        "Reduction, coupling, relaxation, or key lemma.",
        "Main inequality, optimality, fixed-point, concentration, or exchange argument.",
        "Cases or induction if needed.",
        "Conclusion mapped back to theorem.",
    ],
    "placement": [
        "List the completed results, tables, figures, proofs, robustness checks, extensions, and replication materials.",
        "Mark which items support the headline claim, which protect validity, and which only verify or stress-test.",
        "Assign each item to body, regular appendix, online appendix/e-companion, or replication package.",
        "For mathematical material, keep the model object, theorem statement, interpretation, and central derivation checkpoint in the body.",
        "Write the body cross-reference for each appendix item only after the body states what the appendix verifies, preserves, or changes.",
        "Check that the body still lets a reviewer understand the contribution without opening the appendix.",
    ],
    "headings": [
        "Classify the evidence lane before choosing section depth.",
        "Use a top-level heading when the paper moves to a new reader task: setting, data, model, results, robustness, computation, or discussion.",
        "Use a subsection when the object, construct, model component, result family, algorithm, benchmark, or validity threat changes.",
        "Keep theorem and proposition labels spare: Proposition 1, Theorem 2, or a short parenthetical object label when needed.",
        "Put the result's meaning in the surrounding prose, not in long proposition captions or tiny headings such as Key Insight or Proof Idea.",
        "Avoid a subheading for a transition, one-paragraph intuition, local caveat, or second piece of evidence for the same claim.",
        "Use third-level headings only for parallel items a reviewer may need to locate independently.",
        "Name objects, not scaffolding: Data Sources, Variable Construction, Alternative Measurement, Benchmark Policies, Numerical Experiments.",
    ],
    "managerial": [
        "Decision maker and observable condition.",
        "Recommended action.",
        "Mechanism from the result.",
        "Boundary condition or caveat.",
        "Implementation metric.",
    ],
    "discussion": [
        "What the paper establishes.",
        "What the result does not imply.",
        "Robustness or external validity.",
        "Next research question.",
    ],
    "conclusion": [
        "Restate problem and approach.",
        "Two main takeaways.",
        "Conditional managerial/policy implication.",
        "One restrained future direction.",
    ],
}

REFS = {
    "abstract": ["management-science-whole-paper-storycraft.md", "section-architecture.md", "msor-paper-craft.md"],
    "introduction": ["management-science-whole-paper-storycraft.md", "section-architecture.md", "msor-paper-craft.md"],
    "related": ["section-architecture.md", "paragraph-style.md", "citation-tools when exact citations matter"],
    "model": ["management-science-model-proof-equation-layout.md", "math-model-main-appendix-craft.md", "paper-appendix-paired-patterns.md", "msor-language-model-math.md"],
    "results": ["management-science-model-proof-equation-layout.md", "math-model-main-appendix-craft.md", "paper-appendix-paired-patterns.md", "msor-language-model-math.md"],
    "proof": ["management-science-model-proof-equation-layout.md", "math-model-main-appendix-craft.md", "paper-appendix-paired-patterns.md", "math-and-proof-style.md", "math-proof-writing for complete proofs", "theory-proof-workbench for missing proofs"],
    "placement": ["main-text-appendix-placement.md", "paper-appendix-paired-patterns.md", "math-model-main-appendix-craft.md", "reviewer-calibration.md"],
    "headings": ["section-architecture.md", "management-science-whole-paper-storycraft.md", "msor-paper-craft.md"],
    "managerial": ["management-science-language-rhythm.md", "msor-paper-craft.md", "storytelling-language.md"],
    "discussion": ["paragraph-style.md", "storytelling-language.md"],
    "conclusion": ["paragraph-style.md", "storytelling-language.md"],
}

TOPIC_LENSES = {
    "healthcare": "Actor: hospital or clinic. Decision: schedule, triage, route, or allocate capacity. Friction: access delay, no-shows, stochastic service times, and coordination across stations. Benchmark: current practice or myopic scheduling.",
    "supply": "Actor: manufacturer, retailer, supplier, or logistics planner. Decision: source, stock, replenish, expedite, recover, or emit. Friction: lead time, disruption, demand uncertainty, emissions, and cost-service tradeoffs. Benchmark: lean, efficient, offshore, fixed-price, or base-stock policy.",
    "platform": "Actor: platform, seller, buyer, worker, creator, user, or regulator. Decision: price, rank, match, recommend, disclose, subsidize, moderate, or rotate content. Friction: two-sided choice, incentives, fairness, churn, information, herding, congestion, or trust. Benchmark: status quo platform rule or no regulation.",
    "empirical": "Actor: manager, employee, consumer, supplier, platform, or experimental subject. Decision: order, forecast, disclose, price, comply, adopt, or exert effort. Friction: behavioral bias, information asymmetry, incentives, attention, trust, or transparency. Benchmark: rational model, no-treatment group, prior theory, or existing policy.",
    "algorithm": "Actor: planner, algorithm, or platform operator. Decision: allocate, match, schedule, route, learn, stop, accept, reject, or price. Friction: online arrival, uncertainty, combinatorial complexity, limited information, coupling, or nonconvexity. Benchmark: LP relaxation, myopic policy, batching, greedy heuristic, or clairvoyant optimum.",
    "mechanism": "Actor: designer, regulator, platform, seller, bidder, or agent. Decision: choose rules, payments, allocation, disclosure, regulation, or information design. Friction: incentives, private information, participation, collusion, fairness, or welfare tradeoff. Benchmark: first-best, no regulation, standard auction, posted price, Myerson, or efficient allocation.",
    "learning": "Actor: algorithm, platform, seller, physician, recommender, or experimenter. Decision: explore, exploit, recommend, price, treat, allocate samples, or stop learning. Friction: uncertainty, adaptive data, regret, attrition, delayed feedback, fairness, or safety. Benchmark: oracle, classical learner, static policy, unconstrained learner, or no-learning policy.",
    "human_ai": "Actor: manager, worker, expert, user, or human decision maker. Decision: accept, reject, rely on, override, frame, or incentivize algorithmic advice. Friction: trust, algorithm aversion, incentives, framing, accountability, workflow fit, or expertise. Benchmark: unaided human judgment, expert advice, algorithmic advice, or hybrid human-algorithm decision making.",
    "data_driven_rm": "Actor: firm, seller, retailer, platform, or operations manager. Decision: price, stock, assort, recommend, procure, or allocate capacity. Friction: limited, censored, contextual, nonstationary, or misspecified data. Benchmark: oracle, sample-average approximation, model-based policy, model-free policy, static policy, or simple heuristic.",
    "robust_optimization": "Actor: decision maker, planner, firm, or algorithm. Decision: choose a policy, action, decision rule, or uncertainty set before the realized distribution or parameters are known. Friction: distributional ambiguity, misspecification, side information, ambiguity radius, or limited samples. Benchmark: nominal policy, oracle policy, sample-average approximation, worst-case optimum, or out-of-sample performance.",
    "business": "Actor: investor, lender, consumer, advertiser, auditor, analyst, firm, or regulator. Decision: disclose, target, lend, report, audit, adopt technology, or allocate capital. Friction: information asymmetry, agency, attention, privacy, bias, strategic reporting, or network effects. Benchmark: rational benchmark, no disclosure, uniform targeting, or status quo policy.",
    "infrastructure": "Actor: grid operator, utility, transit agency, city, logistics planner, community, or regulator. Decision: dispatch, route, price, invest, locate capacity, ration, repair, or decarbonize. Friction: congestion, reliability, intermittency, emissions, equity, resilience, or spatial spillovers. Benchmark: deterministic planning, current operations, no policy, shortest path, or least-cost dispatch.",
    "policy": "Actor: school, worker, employer, agency, household, regulator, nonprofit, or platform. Decision: admit, assign, incentivize, train, monitor, disclose, target, or comply. Friction: selection, incentives, fairness, capacity, incomplete information, behavior, or compliance. Benchmark: current rule, random assignment, no treatment, first-best, or equal allocation.",
}


def topic_lens(topic: str) -> str:
    lower = topic.lower()
    matches = []
    keyword_map = {
        "healthcare": (
            {"healthcare", "hospital", "clinic", "physician", "surgery"},
            {"health", "patient", "appointment"},
        ),
        "supply": (
            {"supply chain", "inventory", "manufacturer", "sourcing", "logistics", "nearshore"},
            {"supply", "retail", "sustainability", "emission"},
        ),
        "platform": (
            {"platform", "marketplace", "creator economy"},
            {"pricing", "review", "match", "recommend", "content", "creator", "seller"},
        ),
        "empirical": (
            {"empirical", "experiment", "identification", "replication", "behavioral", "panel data", "administrative data", "field data", "did", "difference-in-differences", "construct validation"},
            {"field", "dataset", "estimate"},
        ),
        "human_ai": (
            {"algorithmic advice", "human-ai", "human algorithm", "algorithm aversion", "automated advice", "managerial reliance", "reliance on algorithmic advice"},
            {"trust", "framing", "incentive", "expert advice", "human", "advice"},
        ),
        "algorithm": (
            {"algorithm", "approximation algorithm", "online algorithm", "dynamic programming", "lagrangian relaxation", "computational study", "numerical experiments", "computational experiments"},
            {"online", "matching", "scheduling", "routing", "lp"},
        ),
        "mechanism": (
            {"mechanism", "auction", "incentive compatible", "information design"},
            {"incentive", "ic", "ir", "private", "regulation", "policy", "welfare"},
        ),
        "learning": (
            {"learning", "bandit", "regret"},
            {"recommendation", "exploration", "adaptive", "prediction"},
        ),
        "data_driven_rm": (
            {"data-driven", "transaction data", "limited data", "contextual data", "model-free", "demand learning", "demand estimation", "price recommendation", "price recommendations", "model misspecification", "newsvendor", "dynamic pricing", "assortment pricing"},
            {"pricing", "price", "assortment", "inventory", "sample", "historical", "nonstationary", "censored", "recommendation"},
        ),
        "robust_optimization": (
            {"distributionally robust", "robust optimization", "dro", "uncertainty set", "wasserstein", "causal transport", "transport distance", "side information", "ambiguity set"},
            {"robust", "misspecification", "worst-case", "ambiguity", "out-of-sample"},
        ),
        "business": (
            {"finance", "accounting", "marketing", "advertising", "disclosure", "lending", "credit", "audit", "investor", "information system", "technology adoption", "collaborative work management", "managerial hierarchy", "managerial intensity"},
            {"consumer"},
        ),
        "infrastructure": (
            {"energy", "electricity", "grid", "transportation", "traffic", "transit", "environment", "climate", "carbon", "infrastructure", "unit commitment"},
            {"routing", "emission"},
        ),
        "policy": (
            {"education", "school", "labor", "employment", "nonprofit", "welfare program"},
            {"worker", "public", "agency", "compliance"},
        ),
    }
    for name, (strong_keywords, weak_keywords) in keyword_map.items():
        strong_hit = any(has_keyword(lower, keyword) for keyword in strong_keywords)
        weak_hits = sum(1 for keyword in weak_keywords if has_keyword(lower, keyword))
        if strong_hit or weak_hits >= 2:
            matches.append((name, TOPIC_LENSES[name]))
    if not matches:
        return "Use the general lens. First classify the job as practice, theory, empirical, algorithm, policy, or review. Then identify the actor, decision, hidden friction, benchmark, evidence type, consequence, and caveat before drafting."
    matched_names = {name for name, _ in matches}
    if {"human_ai", "data_driven_rm"} & matched_names:
        matches = [(name, lens) for name, lens in matches if name != "algorithm"]
    if "algorithm" in matched_names and ("numerical experiment" in lower or "computational experiment" in lower):
        matches = [(name, lens) for name, lens in matches if name != "empirical"]
    return " ".join(lens for _, lens in matches[:2])

QUALITY = {
    "abstract": "decision, friction, method, result, implication, boundary; avoid jargon before the problem is clear",
    "introduction": "lane-specific entry point, decision or formal object, contrast, friction, credibility support, findings, boundary, contribution; roadmap only if useful",
    "related": "stream, limitation, this paper's difference; no citation dumping",
    "model": "agents, timing, information, actions, primitives, objective, constraints, assumptions, benchmark, solution concept, and translated formulation display",
    "results": "formal result, benchmark intuition, derivation checkpoint when needed, mechanism, condition, implication",
    "proof": "setup, plain proof idea, constructed object, hard term, mathematical move, key lemma or inequality, validity condition, conclusion mapped back; avoid stylized proof language",
    "placement": "body for first-pass contribution, model object, theorem statement, interpretation, and central derivation checkpoint; appendix for verification, robustness, implementation, and replication",
    "headings": "section depth follows reader task; subheadings mark new objects, result families, model components, or validity threats; theorem/proposition captions stay short",
    "managerial": "decision maker, observable condition, action, mechanism, caveat, metric",
    "discussion": "established claim, limitation, robustness, next question",
    "conclusion": "two takeaways and one restrained future direction",
}


TARGET_NOTES = {
    "management science": "Broad management audience; emphasize what the data/model changes about management theory, practice, or decision logic.",
    "operations research": "Methodological audience; foreground model rigor, proof logic, and benchmark value.",
    "msom": "OM audience; emphasize problem definition, methodology/results, and managerial implications.",
    "working paper": "Use journal-neutral OR/MS style; make contribution and evidence explicit.",
}

TARGET_REFS = {}


def normalize(value: str) -> str:
    return value.strip().lower().replace("&", "and")


def has_keyword(text: str, keyword: str) -> bool:
    if " " in keyword:
        return keyword in text
    suffix = r"(?:s|es|ing|ed|al)?"
    return re.search(rf"\b{re.escape(keyword)}{suffix}\b", text) is not None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--section", required=True, help="abstract, introduction, related, model, results, proof, placement, headings, managerial, discussion, conclusion")
    parser.add_argument("--target", default="working paper", help="Management Science, Operations Research, M&SOM, or working paper")
    parser.add_argument("--topic", default="", help="optional paper topic for a topic-specific story lens")
    args = parser.parse_args()

    section = normalize(args.section)
    if section in {"intro"}:
        section = "introduction"
    if section in {"lit", "literature", "related literature"}:
        section = "related"
    if section in {"managerial implications", "implications"}:
        section = "managerial"
    if section in {"appendix", "online appendix", "e-companion", "supplement", "supplemental", "result placement", "results placement"}:
        section = "placement"
    if section in {"heading", "subheading", "subheadings", "section headings", "sectioning", "structure"}:
        section = "headings"
    if section not in BLUEPRINTS:
        raise SystemExit(f"Unknown section: {args.section}")

    target = normalize(args.target)
    if target in {"m&soms", "m and som", "mandsom", "m and s om", "manufacturing and service operations management"}:
        target = "msom"

    print(f"Writing Card: target={args.target}; section={section}")
    print(f"Target note: {TARGET_NOTES.get(target, TARGET_NOTES['working paper'])}")
    print("Planning output only. Do not copy this card's labels or punctuation into polished prose.")
    if args.topic.strip():
        print("Topic lens:")
        print(textwrap.fill(topic_lens(args.topic), width=88))
    print("\nSection modules:")
    print("Select, omit, and reorder by evidence lane; do not copy this order into polished prose.")
    for item in BLUEPRINTS[section]:
        print(f"- {item}")
    print("\nRecommended references:")
    print("- Load one bundle by default; add another only if the draft still has a specific language, story, math, placement, or reviewer problem.")
    seen_refs = set()
    for ref in TARGET_REFS.get(target, []) + REFS.get(section, []):
        ref_key = ref.split(" for ", 1)[0]
        if ref_key in seen_refs:
            continue
        seen_refs.add(ref_key)
        print(f"- {ref}")
    if target == "management science":
        print("\nManagement Science comparable-design lane:")
        print(textwrap.fill("Apply the always-on MS core first as a diagnostic, not a template: decision, belief, friction, method, result, mechanism, condition, consequence. Then match the paper to field experiment, human-algorithm, data-driven revenue management, analytical platform model, hybrid algorithm-field implementation, operational-data transfer/cross-learning, service queueing, behavioral experiment, or theory/algorithm with management applications.", width=88))
    print("\nArchitecture note:")
    print(textwrap.fill("MS/OR papers do not share one universal skeleton. Choose headings that name the paper object, such as Research Setting, Data and Methods, The Model, Empirical Strategy, Main Results, Algorithm, Numerical Experiments, Robustness Tests, or Discussion and Conclusion. Add subheadings only when the reader job, evidence object, model component, theorem family, or validity threat changes.", width=88))
    print("\nDiagnostic signals:")
    print(textwrap.fill(QUALITY.get(section, "actor, decision, friction, method, result, consequence"), width=88))
    print("\nOR/MS spine:")
    print(textwrap.fill("Use as an internal diagnostic, not a sentence template: decision maker, formal object, benchmark, result type, mechanism, validity condition, and decision consequence. Include only the pieces the section needs.", width=88))
    print("\nNaturalness rule:")
    print(textwrap.fill("Do not force every diagnostic item into one sentence or paragraph. Use ordinary setup-result and result-interpretation pairs, and rebuild translated-English order around the decision object before polishing words.", width=88))
    print("\nEvidence preservation rule:")
    print(textwrap.fill("Do not strengthen the evidence while improving the prose. Keep the evidence type, comparator, metric, magnitude, policy class, and validity condition no stronger than the user's material supports.", width=88))
    print("\nArgument-evidence-boundary rule:")
    print(textwrap.fill("Before drafting forward, reason backward from what the paper proves, estimates, or demonstrates. Keep each major claim close to its theorem, estimate, simulation, benchmark, proof idea, or table, and keep the assumption, setting, policy class, population, or data regime close enough to prevent overreading.", width=88))
    print("\nPlacement rule:")
    print(textwrap.fill("The body must contain what a reviewer needs for first-pass understanding and trust: headline result, object, assumptions, benchmark, primary evidence, and interpretation. Appendices carry verification, long proofs, repeated robustness, implementation details, and replication materials.", width=88))
    print("\nParagraph rule:")
    print(textwrap.fill("Each paragraph should have one job: claim, support, interpretation, and bridge. If a claim lacks evidence, mark it as a gap instead of polishing around it.", width=88))
    print("\nStory prompts:")
    print("actor / decision / standard intuition / hidden friction / method / result / consequence")
    print(textwrap.fill("Use these as prompts, not a fixed order. Omit pieces that the local paragraph does not need.", width=88))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

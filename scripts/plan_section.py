#!/usr/bin/env python3
"""Print a compact OR/MS writing blueprint for a requested section."""

from __future__ import annotations

import argparse
import re
import textwrap


BLUEPRINTS = {
    "abstract": [
        "Central object: decision, system, construct, estimator, policy class, theorem object, or empirical contrast.",
        "Departure or question: include the friction, counterexample, missing evidence, or new feature only when it is needed to interpret the contribution.",
        "Evidence owner: analytical model, empirical design, algorithm, theorem, simulation, field implementation, or hybrid support.",
        "Headline result: preserve its actual metric, comparator, evidence strength, and minimum boundary.",
        "Interpretation or implication: include only when supported and more informative than another result or boundary.",
    ],
    "manuscript": [
        "Central object: name the decision, system, policy class, estimator, theorem object, or mechanism the paper is about.",
        "Paper-level claim: state what the manuscript lets a knowledgeable reviewer assert; include a prior belief only when the paper genuinely changes one.",
        "Spine result: choose the theorem, estimate, guarantee, field comparison, or mechanism result that carries the paper.",
        "Credibility path: identify the proof, design, benchmark, validation, or implementation evidence needed for first-pass trust.",
        "Result hierarchy: separate spine, load-bearing support, mechanism, boundary, robustness, extension, and appendix-only verification.",
        "Model necessity: say which assumptions, states, timing, controls, and benchmarks are forced by the spine result.",
        "Reviewer objections: anticipate the strongest home-field, adjacent-field, and skeptical-editor objections.",
        "Deletion/demotion: mark correct but secondary items that should move to appendix or disappear.",
    ],
    "story": [
        "Primary burden: define, motivate, establish, compare, interpret, qualify, or connect.",
        "Prerequisites: definitions, timing, assumptions, benchmark, and design facts needed before later claims rely on them.",
        "Warrant: theorem, estimate, comparison, citation, proof move, or design feature that supports the inference.",
        "Relation: definition, elaboration, evidence, inference, contrast, mechanism, condition, consequence, decomposition, or scope change.",
        "Scope continuity: metric, population, policy class, evidence type, and boundary remain stable or change explicitly.",
        "Attention: central claims receive more space and stronger placement than supporting verification.",
        "Paragraph boundary: start a new paragraph only when burden, evidence object, analytical level, or scope changes enough to justify a reset.",
    ],
    "introduction": [
        "Entry object: decision setting, institution, standard model, construct, counterexample, theorem object, technical obstacle, or empirical pattern.",
        "Relevant departure: current practice, canonical model, prior evidence, missing comparison, or new feature only when it is needed to interpret the claim.",
        "Question, contribution object, or headline claim at the point where its terms and comparison are legible.",
        "Credibility role: what the experiment, variation, theorem, model feature, validation, guarantee, or benchmark lets the paper establish.",
        "Study object: enough model, data, design, estimator, algorithm, policy, or formal-problem detail to make the evidence relation clear.",
        "Findings in the right evidence register: estimate, theorem, guarantee, characterization, validation, or counterfactual.",
        "Contributions by audience or literature stream, grouped by what the reader learns.",
        "Implications and roadmap only when they help the lane and target journal.",
    ],
    "related": [
        "Synthesize what each relevant stream establishes rather than listing papers one by one.",
        "Identify the exact dimension of relation or departure: setting, information, timing, design, mechanism, policy class, or metric.",
        "Choose stream-first or paper-first order according to emphasis; do not force every paragraph to end with the current paper.",
        "Keep each citation attached to the claim it actually supports.",
    ],
    "model": [
        "Central object and lane: theory problem, empirical model, structural measurement device, applied system model, estimator, or algorithm.",
        "Relevant primitives: agents or system, timing, information, state, action, demand, payoff, transition, feasible set, objective, and constraints.",
        "For empirical lanes: construct meaning, observation or elicitation, identifying contrast, target estimand, and permitted coefficient interpretation.",
        "Assumptions and their role in definition, tractability, identification, mechanism isolation, implementation, or scope.",
        "Benchmark or solution concept needed by the paper's comparison.",
        "What the abstraction, formulation, or estimator lets the paper establish and what it deliberately leaves out.",
        "Main display with enough nearby prose to translate the variables, objective or estimand, constraints, and comparator that later claims use.",
    ],
    "results": [
        "Formal result, estimate, comparison, or estimand at the point where its setup is active.",
        "Evidence owner or credibility checkpoint: theorem, proof move, identifying variation, validation, benchmark, simulation, placebo, or robustness check when needed.",
        "Metric, comparator, magnitude, uncertainty, condition, or policy class needed to read the claim accurately.",
        "Interpretation through the relation the result establishes: characterization, comparison, mechanism, decomposition, regime, or boundary.",
        "Mechanism, heterogeneity, spillovers, robustness, or implication only when it answers a live claim or threat.",
        "Explicit register signal when moving among theorem, estimate, simulation, counterfactual, and managerial interpretation.",
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
        "Use construct headings such as Measures, Empirical Framework, Measurement Challenges, or Conceptual Motivation when they are the reader's next job.",
        "Keep theorem and proposition labels spare: Proposition 1, Theorem 2, or a short parenthetical object label when needed.",
        "Put the result's meaning in the surrounding prose, not in long proposition captions or tiny headings such as Key Insight or Proof Idea.",
        "Avoid a subheading for a transition, one-paragraph intuition, local caveat, or second piece of evidence for the same claim.",
        "Use third-level headings only for parallel items a reviewer may need to locate independently.",
        "Name objects, not scaffolding: Measures, Empirical Framework, Data Sources, Variable Construction, Alternative Measurement, Benchmark Policies, Numerical Experiments.",
    ],
    "managerial": [
        "Supported decision consequence or warning; omit a recommendation when the evidence does not earn one.",
        "Decision maker, policy designer, or methodological user only when the implication has one.",
        "Observable condition, comparator, and metric needed to act on or interpret the result.",
        "Mechanism only when established; otherwise state the pattern or formal relation at the available evidence strength.",
        "Boundary, implementation constraint, or caveat that prevents overreading.",
    ],
    "discussion": [
        "Primary burden: synthesis, interpretation, scope, theory relation, practice relation, or limitation.",
        "What the paper establishes at the same evidence strength, metric, comparator, and population or model class used in the results.",
        "Relation to theory, practice, policy, or method only where the body supplies the warrant.",
        "Boundary, external-validity issue, unresolved alternative, or robustness qualification when it changes interpretation.",
        "Future question only when it follows from a real limit or new object rather than genre convention.",
    ],
    "conclusion": [
        "Return to the central object and supported paper-level claim without replaying the introduction.",
        "Interpret the headline result at the same metric, comparator, evidence strength, and boundary used in the results.",
        "Include an implication, limitation, or future direction only when it adds something the body has earned.",
        "End on the paper's most consequential supported point rather than a mandatory future-research sentence.",
    ],
}

REFS = {
    "abstract": ["msor-manuscript-judgment.md", "msor-word-choice-collocations.md", "msor-sentence-craft.md", "msor-natural-prose.md", "msor-micro-phrasing.md", "msor-full-text-close-reading.md", "management-science-whole-paper-storycraft.md", "section-architecture.md", "msor-paper-craft.md"],
    "manuscript": ["manuscript-contract-and-consistency.md", "msor-manuscript-judgment.md", "management-science-whole-paper-storycraft.md", "section-architecture.md", "msor-paper-craft.md", "main-text-appendix-placement.md"],
    "story": ["management-science-whole-paper-storycraft.md", "paragraph-style.md", "msor-natural-prose.md", "section-architecture.md"],
    "introduction": ["msor-manuscript-judgment.md", "msor-word-choice-collocations.md", "msor-sentence-craft.md", "msor-natural-prose.md", "msor-micro-phrasing.md", "msor-full-text-close-reading.md", "management-science-whole-paper-storycraft.md", "section-architecture.md", "msor-paper-craft.md"],
    "related": ["msor-word-choice-collocations.md", "msor-sentence-craft.md", "section-architecture.md", "paragraph-style.md", "an available citation lookup or browsing tool when exact citations matter"],
    "model": ["msor-word-choice-collocations.md", "msor-sentence-craft.md", "msor-natural-prose.md", "msor-full-text-close-reading.md", "management-science-model-proof-equation-layout.md", "math-model-main-appendix-craft.md", "paper-appendix-paired-patterns.md", "msor-language-model-math.md"],
    "results": ["msor-manuscript-judgment.md", "msor-word-choice-collocations.md", "msor-sentence-craft.md", "msor-natural-prose.md", "msor-micro-phrasing.md", "msor-full-text-close-reading.md", "management-science-model-proof-equation-layout.md", "math-model-main-appendix-craft.md", "paper-appendix-paired-patterns.md", "msor-language-model-math.md"],
    "proof": ["msor-word-choice-collocations.md", "msor-sentence-craft.md", "msor-natural-prose.md", "msor-full-text-close-reading.md", "management-science-model-proof-equation-layout.md", "math-model-main-appendix-craft.md", "paper-appendix-paired-patterns.md", "math-and-proof-style.md", "a proof-writing workflow for rough complete proofs", "a proof-discovery workflow for missing proofs"],
    "placement": ["main-text-appendix-placement.md", "paper-appendix-paired-patterns.md", "math-model-main-appendix-craft.md", "msor-full-text-close-reading.md", "reviewer-calibration.md"],
    "headings": ["section-architecture.md", "management-science-whole-paper-storycraft.md", "msor-paper-craft.md"],
    "managerial": ["msor-word-choice-collocations.md", "msor-sentence-craft.md", "msor-natural-prose.md", "msor-micro-phrasing.md", "management-science-language-rhythm.md", "msor-paper-craft.md", "storytelling-language.md"],
    "discussion": ["msor-word-choice-collocations.md", "msor-sentence-craft.md", "msor-natural-prose.md", "paragraph-style.md", "storytelling-language.md"],
    "conclusion": ["msor-word-choice-collocations.md", "msor-sentence-craft.md", "msor-natural-prose.md", "paragraph-style.md", "storytelling-language.md"],
}

TOPIC_LENSES = {
    "healthcare": "Possible objects: patient flow, appointment system, queue, staffing rule, capacity policy, or care network. Relevant relations may involve delay, no-shows, service uncertainty, coordination, current practice, or a policy comparison. Select only what the passage establishes.",
    "supply": "Possible objects: inventory policy, sourcing portfolio, replenishment rule, disruption regime, emissions objective, or service metric. Relevant relations may involve lead time, demand uncertainty, resilience, cost-service tradeoffs, or benchmark policies. Select only what the passage establishes.",
    "platform": "Possible objects: ranking rule, matching policy, price, disclosure design, user response, seller behavior, or welfare criterion. Relevant relations may involve incentives, information, congestion, fairness, trust, or a status quo comparison. Select only what the passage establishes.",
    "empirical": "Possible objects: construct, treatment, outcome, behavioral pattern, estimand, coefficient, or institutional comparison. Make the observation, design warrant, metric, and scope recoverable; include a decision or mechanism only when claimed.",
    "algorithm": "Possible objects: formal problem, state, information set, feasible action, relaxation, policy, guarantee, or runtime. Make the comparator and performance criterion recoverable; an operational actor or friction is optional for a canonical problem.",
    "mechanism": "Possible objects: allocation rule, payment, information structure, incentive constraint, equilibrium, welfare criterion, or implementability result. Make the formal relation, comparator, and regime recoverable without forcing a first-best narrative.",
    "learning": "Possible objects: feedback process, policy, confidence event, regret, sample allocation, stopping rule, or safety constraint. Make the information structure, comparator, performance criterion, and horizon or data regime recoverable.",
    "human_ai": "Possible objects: advice, reliance, override, performance, confidence, calibration, workflow, or incentive treatment. Keep tool quality, human response, outcome, and mechanism evidence distinct; include only the relations the design identifies.",
    "data_driven_rm": "Possible objects: demand data, estimator, policy, censoring process, model class, price or inventory decision, and out-of-sample metric. Make the data limitation, comparator, and decision criterion explicit only where they bear on the claim.",
    "robust_optimization": "Possible objects: uncertainty or ambiguity set, decision rule, nominal model, side information, worst-case objective, and out-of-sample guarantee. Make the perturbation class, comparator, and protected metric recoverable.",
    "business": "Possible objects: disclosure, audit, lending rule, targeting policy, technology adoption, investor belief, consumer response, or capital allocation. Make the evidence relation, incentive or information channel, metric, and scope recoverable.",
    "infrastructure": "Possible objects: dispatch, routing, investment, capacity, reliability, emissions, resilience, or spatial distribution. Keep the physical feasibility relation and the relevant social, environmental, or operating metric connected.",
    "policy": "Possible objects: assignment rule, intervention, compliance behavior, capacity constraint, welfare criterion, causal contrast, or distributional outcome. Separate what the evidence establishes from any recommendation.",
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
            {"empirical", "experiment", "identification", "replication", "behavioral", "panel data", "administrative data", "field data", "did", "difference-in-differences", "construct validation", "measurement challenge", "calibration experiment", "field experiment"},
            {"field", "dataset", "estimate", "calibration", "treatment", "coefficient", "belief"},
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
        return "Use the general lens. First classify the passage's burden and evidence type. Then identify only the central object, prerequisite, warrant, comparator, relation, scope, or consequence needed for that burden."
    matched_names = {name for name, _ in matches}
    if {"human_ai", "data_driven_rm"} & matched_names:
        matches = [(name, lens) for name, lens in matches if name != "algorithm"]
    if "algorithm" in matched_names and ("numerical experiment" in lower or "computational experiment" in lower):
        matches = [(name, lens) for name, lens in matches if name != "empirical"]
    primary_name, primary_lens = matches[0]
    if len(matches) == 1:
        return primary_lens
    secondary_name = matches[1][0]
    return (
        f"Primary lens ({primary_name}): {primary_lens} "
        f"Secondary signal: also check {secondary_name} only if the paragraph's reader job genuinely crosses lanes."
    )

QUALITY = {
    "abstract": "central object, departure or question when needed, evidence type, headline result, comparator or metric, and the minimum boundary needed for accurate compression",
    "manuscript": "central object, paper-level claim, spine result, credibility path, result hierarchy, model necessity, reviewer objections, deletion/demotion",
    "story": "primary burden, prerequisites, warrant, relation between adjacent units, scope continuity, evidence-register shifts, and attention hierarchy; no fixed first-middle-last shape",
    "introduction": "lane-specific entry object, relevant departure when needed, question or claim, credibility role, findings, boundary, contribution; no mandatory friction or roadmap",
    "related": "what the stream establishes, exact relation to the current paper, and claim-citation fit; no mandatory gap ending or citation dumping",
    "model": "central formal or empirical object, prerequisites, relevant primitives, assumption roles, target claim or estimand, comparator, and enough display translation for later use",
    "results": "formal result or empirical estimand, visible warrant, metric and comparator, magnitude or condition when relevant, evidence-register signal, and only supported interpretation",
    "proof": "setup, plain proof idea, constructed object, hard term, mathematical move, key lemma or inequality, validity condition, conclusion mapped back; avoid stylized proof language",
    "placement": "body for first-pass contribution, model object, theorem statement, interpretation, and central derivation checkpoint; appendix for verification, robustness, implementation, and replication",
    "headings": "section depth follows reader task; subheadings mark new objects, result families, model components, or validity threats; theorem/proposition captions stay short",
    "managerial": "supported decision consequence or warning, user when relevant, observable condition, metric, evidence strength, and boundary; no mandatory recommendation or mechanism",
    "discussion": "primary burden, established claim, warranted relation, scope or limitation when consequential, and no mandatory future question",
    "conclusion": "central object, supported paper-level claim, stable metric/comparator/boundary, and only earned implications or limitations",
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
    parser.add_argument("--section", required=True, help="abstract, manuscript, story, introduction, related, model, results, proof, placement, headings, managerial, discussion, conclusion")
    parser.add_argument("--target", default="working paper", help="Management Science, Operations Research, M&SOM, or working paper")
    parser.add_argument("--topic", default="", help="optional paper topic for a topic-specific story lens")
    args = parser.parse_args()

    section = normalize(args.section)
    if section in {"intro"}:
        section = "introduction"
    if section in {"paper", "full paper", "paper spine", "spine", "manuscript spine", "whole paper"}:
        section = "manuscript"
    if section in {"story logic", "story-order", "story order", "paragraph logic", "paragraph order", "flow", "reader flow", "section flow"}:
        section = "story"
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
        print(textwrap.fill("Apply the MS core as a dependency audit, not a story template: central object, relevant departure, support, comparator, and boundary. Add decision, friction, mechanism, or consequence only when the paper actually relies on them. Then match the evidence lane.", width=88))
    print("\nArchitecture note:")
    print(textwrap.fill("MS/OR papers do not share one universal skeleton. Choose headings that name the paper object, such as Research Setting, Data and Methods, The Model, Empirical Strategy, Main Results, Algorithm, Numerical Experiments, Robustness Tests, or Discussion and Conclusion. Add subheadings only when the reader job, evidence object, model component, theorem family, or validity threat changes.", width=88))
    print("\nDiagnostic signals:")
    print(textwrap.fill(QUALITY.get(section, "primary burden, central object, warrant, relation, scope, and evidence register"), width=88))
    print("\nOR/MS spine:")
    print(textwrap.fill("Use as an internal diagnostic, not a sentence template: central object, spine result, credibility support, benchmark, mechanism, validity condition, and decision consequence. Include only the pieces the section needs.", width=88))
    print("\nNaturalness rule:")
    print(textwrap.fill("Do not force every diagnostic item into one sentence or paragraph. Use ordinary sentence relations that fit the local burden, split overloaded sentences before polishing, keep the subject close to the verb, and rebuild translated-English order around the paper's local object and action, with any needed condition or benchmark expressed through a natural verb-object collocation.", width=88))
    print("\nEvidence preservation rule:")
    print(textwrap.fill("Do not strengthen the evidence while improving the prose. Keep the evidence type, comparator, metric, magnitude, policy class, and validity condition no stronger than the user's material supports.", width=88))
    print("\nArgument-evidence-boundary rule:")
    print(textwrap.fill("Before drafting forward, reason backward from what the paper proves, estimates, or demonstrates. Keep each major claim close to its theorem, estimate, simulation, benchmark, proof idea, or table, and keep the assumption, setting, policy class, population, or data regime close enough to prevent overreading.", width=88))
    print("\nPlacement rule:")
    print(textwrap.fill("The body must contain what a reviewer needs for first-pass understanding and trust: the central object, headline result, primary support, needed interpretation, and any assumption or comparator on which the claim depends. Appendices carry verification, long proofs, repeated robustness, implementation details, and replication materials.", width=88))
    print("\nParagraph rule:")
    print(textwrap.fill("Each paragraph should have a recoverable primary burden, with linked support or interpretation where needed. Split only when burdens compete. If a claim lacks evidence, mark it as a gap instead of polishing around it.", width=88))
    print("\nReader-flow reminder:")
    print(textwrap.fill("Make a claim's prerequisites and warrant available by the point the reader must rely on them, without forcing a question-and-answer rhythm. Claim-first, evidence-first, definition-first, contrast-first, exception-first, procedure-first, and result-first orders are all legitimate. A heading, repeated canonical term, or direct scope signal may carry the transition. Omit anything the local burden does not need.", width=88))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

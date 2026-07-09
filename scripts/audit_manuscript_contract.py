#!/usr/bin/env python3
"""Audit cross-section claim, term, number, and boundary consistency in an OR/MS manuscript."""

from __future__ import annotations

import argparse
from collections import defaultdict
import re
import sys


SECTION_ORDER = [
    "abstract",
    "introduction",
    "model_or_design",
    "results",
    "discussion_or_conclusion",
    "appendix",
    "other",
]

SECTION_LABELS = {
    "abstract": "Abstract",
    "introduction": "Introduction",
    "model_or_design": "Model or design",
    "results": "Results or analysis",
    "discussion_or_conclusion": "Discussion or conclusion",
    "appendix": "Appendix or supplement",
    "other": "Other or unclassified",
}

CLAIM_TERMS = {
    "prove", "proves", "establish", "establishes", "show", "shows",
    "find", "finds", "estimate", "estimates", "document", "documents",
    "demonstrate", "demonstrates", "characterize", "characterizes",
    "identify", "identifies", "guarantee", "guarantees", "bound", "bounds",
    "improve", "improves", "reduce", "reduces", "increase", "increases",
    "hold", "holds", "apply", "applies",
    "outperform", "outperforms", "dominate", "dominates", "suggest", "suggests",
    "consistent with", "we provide", "we develop", "we propose",
    "证明", "建立", "表明", "发现", "估计", "刻画", "识别", "保证",
    "改进", "提高", "降低", "优于", "一致",
}

STRONG_TERMS = {
    "prove", "proves", "establish", "establishes", "identify", "identifies",
    "causal", "causes", "optimal", "optimality", "guarantee", "guarantees",
    "dominate", "dominates", "uniformly", "universal", "universally",
    "always", "all settings", "all instances", "solve", "solves",
    "证明", "因果", "最优", "保证", "支配", "所有情形", "普遍",
}

MEDIUM_TERMS = {
    "show", "shows", "find", "finds", "demonstrate", "demonstrates",
    "characterize", "characterizes", "outperform", "outperforms",
    "improve", "improves", "reduce", "reduces", "increase", "increases",
    "hold", "holds", "apply", "applies",
    "表明", "发现", "刻画", "优于", "提高", "降低",
}

SOFT_TERMS = {
    "suggest", "suggests", "consistent with", "may", "might", "can",
    "evidence of", "evidence consistent", "可能", "或许", "与", "一致",
    "we provide", "we develop", "we propose", "本文提出", "本文构建",
}

BOUNDARY_TERMS = {
    "under", "when", "whenever", "if", "for the class", "within", "among",
    "in our sample", "in the sample", "in the experiment", "in our experiment",
    "in simulations", "in our simulations", "in the tested", "on average",
    "subject to", "assuming", "conditional on", "provided that", "for affine",
    "for any", "in the regime", "in this setting", "under assumption",
    "在", "当", "若", "条件下", "样本中", "实验中", "模拟中", "对于",
}

COMPARATOR_TERMS = {
    "relative to", "compared with", "compared to", "versus", "benchmark",
    "baseline", "current practice", "status quo", "first-best", "first best",
    "oracle", "full information", "complete information", "static policy",
    "control group", "treatment group", "相对于", "相比", "基准", "对照组",
}

OVERLOADED_TERMS = {
    "causal", "optimal", "optimality", "equilibrium", "robust", "robustness",
    "efficiency", "efficient", "welfare", "fairness", "learning", "platform",
    "data-driven", "performance", "因果", "最优", "均衡", "稳健", "效率",
    "福利", "公平", "学习", "平台", "数据驱动", "表现",
}

TERM_FAMILIES = {
    "financial outcome": ["profit", "revenue", "sales", "margin", "welfare", "surplus"],
    "market behavior": ["demand", "arrival", "arrivals", "purchase", "purchases", "conversion", "adoption", "engagement"],
    "predictive quality": ["accuracy", "prediction error", "forecast error", "loss", "performance"],
    "decision quality": ["regret", "objective value", "cost", "profit", "optimality gap", "approximation ratio"],
    "evidence strength": ["causal", "causes", "associated with", "consistent with", "suggests", "identifies"],
    "Chinese financial outcome": ["利润", "收入", "销售额", "福利", "剩余"],
    "Chinese market behavior": ["需求", "到达", "购买", "转化", "采用", "参与"],
}

POINTER_PATTERNS = (
    "see appendix", "refer to appendix", "in the appendix", "online appendix",
    "electronic companion", "all proofs appear", "proof is provided in",
    "proof appears in", "details are provided in", "附录中", "见附录",
)

INTERPRETATION_TERMS = {
    "means", "implies", "shows", "suggests", "characterizes", "condition",
    "benchmark", "relative to", "compared with", "because", "when", "policy",
    "decision", "result", "proposition", "theorem", "estimate", "effect",
    "意味着", "表明", "说明", "条件", "基准", "相对于", "策略", "决策",
    "结果", "命题", "定理", "估计", "效应",
}


def contains_term(text: str, term: str) -> bool:
    lower = text.lower()
    if any(ord(char) > 127 for char in term) or " " in term or "-" in term:
        return term in lower
    return bool(re.search(r"\b" + re.escape(term) + r"\b", lower))


def canonical_section(title: str) -> str | None:
    clean = re.sub(r"[{}*_:#]", " ", title).strip().lower()
    clean = re.sub(r"^\s*(?:\d+(?:\.\d+)*[.)]?|[ivxlcdm]+[.)]|[一二三四五六七八九十]+[、.])\s*", "", clean)
    if any(term in clean for term in {"appendix", "supplement", "electronic companion", "online companion", "附录", "补充材料"}):
        return "appendix"
    if clean in {"abstract", "summary", "摘要"} or clean.startswith("abstract "):
        return "abstract"
    if any(term in clean for term in {"conclusion", "concluding", "discussion", "结论", "讨论"}):
        return "discussion_or_conclusion"
    if any(term in clean for term in {"result", "findings", "analysis", "numerical experiment", "computational experiment", "empirical evidence", "实证结果", "研究结果", "数值实验", "计算实验", "结果与分析"}):
        return "results"
    if any(term in clean for term in {"introduction", "motivation", "overview", "引言", "绪论", "研究背景"}):
        return "introduction"
    if any(term in clean for term in {
        "model", "problem formulation", "research setting", "institutional setting",
        "empirical strategy", "research design", "experimental design", "data and method",
        "data", "methods", "methodology", "framework", "measure", "measurement", "identification strategy",
        "模型", "问题描述", "问题定义", "研究设计", "实证策略", "实验设计",
        "数据与方法", "研究方法", "理论框架", "测量",
    }):
        return "model_or_design"
    return None


def heading_title(line: str) -> str | None:
    stripped = line.strip()
    if not stripped:
        return None
    markdown = re.match(r"^#{1,6}\s+(.+?)\s*#*$", stripped)
    if markdown:
        return markdown.group(1).strip()
    latex = re.match(r"^\\(?:section|subsection|subsubsection)\*?\{(.+?)\}\s*$", stripped)
    if latex:
        return latex.group(1).strip()
    if stripped == "\\appendix":
        return "Appendix"
    numbered = re.match(
        r"^(?:\d+(?:\.\d+)*[.)]?|[IVXLCDM]+[.)]|[一二三四五六七八九十]+[、.])\s+(.{2,100})$",
        stripped,
        flags=re.IGNORECASE,
    )
    if numbered and canonical_section(numbered.group(1)):
        return numbered.group(1).strip()
    if re.search(r"[.!?。！？]$", stripped) or re.match(r"^(?:proof|note)\s*[.:]", stripped, flags=re.IGNORECASE):
        return None
    if len(stripped) <= 80 and canonical_section(stripped):
        return stripped
    return None


def parse_sections(raw: str) -> tuple[dict[str, str], list[tuple[str, str]]]:
    chunks: dict[str, list[str]] = defaultdict(list)
    headings: list[tuple[str, str]] = []
    current = "other"
    in_abstract = False

    for line in raw.splitlines():
        stripped = line.strip()
        if re.match(r"^\\begin\{abstract\}", stripped):
            current = "abstract"
            in_abstract = True
            headings.append(("abstract", "LaTeX abstract environment"))
            continue
        if re.match(r"^\\end\{abstract\}", stripped):
            in_abstract = False
            current = "other"
            continue
        title = heading_title(line)
        if title:
            category = canonical_section(title)
            if category:
                current = category
                headings.append((category, title))
                continue
        chunks[current].append(line)
        if in_abstract:
            current = "abstract"

    return {key: "\n".join(value).strip() for key, value in chunks.items() if "".join(value).strip()}, headings


def sentences(text: str, min_chars: int = 18) -> list[str]:
    normalized = re.sub(r"\s+", " ", text).strip()
    if not normalized:
        return []
    parts = re.split(r"(?<=[.!?。！？])\s*", normalized)
    return [part.strip() for part in parts if len(part.strip()) >= min_chars]


def rough_token_count(text: str) -> int:
    return len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'’-]*|[\u4e00-\u9fff]", text))


def claim_strength(sentence: str) -> int:
    if any(contains_term(sentence, term) for term in STRONG_TERMS):
        return 3
    if any(contains_term(sentence, term) for term in MEDIUM_TERMS):
        return 2
    if any(contains_term(sentence, term) for term in SOFT_TERMS):
        return 1
    return 0


def has_boundary(sentence: str) -> bool:
    return any(contains_term(sentence, term) for term in BOUNDARY_TERMS | COMPARATOR_TERMS)


def candidate_claims(text: str) -> list[str]:
    return [
        sentence
        for sentence in sentences(text)
        if any(contains_term(sentence, term) for term in CLAIM_TERMS)
    ]


def extract_numbers(text: str) -> list[str]:
    pattern = re.compile(
        r"(?<![A-Za-z])(?:[$€£¥]\s*)?\d+(?:,\d{3})*(?:\.\d+)?"
        r"(?:\s*(?:%|percent(?:age points?)?|pp|times|fold))?",
        flags=re.IGNORECASE,
    )
    seen: set[str] = set()
    found: list[str] = []
    formal_reference = re.compile(
        r"(?:assumption|theorem|proposition|lemma|corollary|equation|figure|table|appendix|section|ec)\s*$",
        flags=re.IGNORECASE,
    )
    for match in pattern.finditer(text):
        prefix = text[max(0, match.start() - 24):match.start()]
        if formal_reference.search(prefix):
            continue
        clean = re.sub(r"\s+", " ", match.group(0).strip())
        if clean not in seen:
            seen.add(clean)
            found.append(clean)
    return found


def normalize_number(value: str) -> str:
    clean = value.lower().replace(",", "").replace("percentage points", "pp")
    clean = clean.replace("percentage point", "pp").replace("percent", "%")
    return re.sub(r"\s+", "", clean)


def shorten(text: str, limit: int = 230) -> str:
    clean = re.sub(r"\s+", " ", text).strip()
    return clean if len(clean) <= limit else clean[: limit - 3].rstrip() + "..."


def print_section_inventory(sections: dict[str, str], headings: list[tuple[str, str]]) -> None:
    print("Detected manuscript regions")
    for section in SECTION_ORDER:
        if section not in sections:
            continue
        title_list = [title for category, title in headings if category == section]
        suffix = f"; headings={'; '.join(title_list[:4])}" if title_list else ""
        print(f"- {SECTION_LABELS[section]}: about {rough_token_count(sections[section])} word/character tokens{suffix}")


def print_claim_inventory(sections: dict[str, str], max_claims: int) -> dict[str, list[str]]:
    print("\nCandidate contract claims")
    print("- Heuristic strength: 0=descriptive, 1=qualified, 2=substantive, 3=formally or rhetorically strong. Read every score in context.")
    inventory: dict[str, list[str]] = {}
    for section in SECTION_ORDER[:5]:
        if section not in sections:
            continue
        claims = candidate_claims(sections[section])
        inventory[section] = claims
        if not claims:
            print(f"- {SECTION_LABELS[section]}: no evidence-verb sentence detected; read manually")
            continue
        print(f"- {SECTION_LABELS[section]}:")
        for claim in claims[:max_claims]:
            print(f"  - [strength {claim_strength(claim)}] {shorten(claim)}")
    return inventory


def print_diagnostics(sections: dict[str, str], claims: dict[str, list[str]]) -> None:
    print("\nReview candidates")
    flags: list[str] = []

    for section in ("abstract", "discussion_or_conclusion"):
        for sentence in claims.get(section, []):
            if claim_strength(sentence) >= 3 and not has_boundary(sentence):
                flags.append(
                    f"{SECTION_LABELS[section]} uses a strong claim without a local comparator or boundary: {shorten(sentence)}"
                )

    result_strength = max((claim_strength(item) for item in claims.get("results", [])), default=0)
    conclusion_strength = max((claim_strength(item) for item in claims.get("discussion_or_conclusion", [])), default=0)
    if conclusion_strength > result_strength and conclusion_strength >= 2 and "results" in sections:
        flags.append(
            "The strongest detected conclusion verb is stronger than the strongest detected results verb. Check the passages in context; this may be legitimate, but it often signals claim-strength drift."
        )

    result_numbers = {normalize_number(item) for item in extract_numbers(sections.get("results", ""))}
    for section in ("abstract", "discussion_or_conclusion"):
        numbers = extract_numbers(sections.get(section, ""))
        unmatched = [item for item in numbers if normalize_number(item) not in result_numbers]
        if unmatched and result_numbers:
            flags.append(
                f"{SECTION_LABELS[section]} numbers not repeated in the detected results region: {', '.join(unmatched[:12])}. Verify magnitudes, intervals, rates, and sample counts manually."
            )

    for section in SECTION_ORDER[:5]:
        section_sentences = sentences(sections.get(section, ""), min_chars=1)
        for index, sentence in enumerate(section_sentences):
            lower = sentence.lower()
            if any(pattern in lower for pattern in POINTER_PATTERNS):
                neighbors = section_sentences[max(0, index - 2):index] + section_sentences[index + 1:index + 3]
                has_local_explanation = any(
                    any(contains_term(neighbor, term) for term in CLAIM_TERMS | INTERPRETATION_TERMS)
                    for neighbor in neighbors
                )
                if not has_local_explanation:
                    flags.append(
                        f"Appendix handoff with no detected nearby interpretation in {SECTION_LABELS[section]}: {shorten(sentence)}"
                    )

    if flags:
        for flag in flags[:20]:
            print(f"- {flag}")
    else:
        print("- No obvious cross-section claim, number, or appendix-handoff flag was detected. This is not a substantive validation.")


def print_term_inventory(sections: dict[str, str]) -> None:
    print("\nTerminology review")
    family_flags = 0
    for family, terms in TERM_FAMILIES.items():
        present: dict[str, list[str]] = {}
        for term in terms:
            locations = [
                SECTION_LABELS[section]
                for section in SECTION_ORDER[:5]
                if section in sections and contains_term(sections[section], term)
            ]
            if locations:
                present[term] = locations
        if len(present) >= 2:
            family_flags += 1
            rendered = "; ".join(f"{term} ({', '.join(locations)})" for term, locations in present.items())
            print(f"- Review {family}: {rendered}")
    if not family_flags:
        print("- No predefined near-neighbor term family contains multiple detected terms.")

    overloaded: dict[str, list[str]] = {}
    for term in sorted(OVERLOADED_TERMS):
        locations = [
            SECTION_LABELS[section]
            for section in SECTION_ORDER[:5]
            if section in sections and contains_term(sections[section], term)
        ]
        if locations:
            overloaded[term] = locations
    if overloaded:
        rendered = "; ".join(f"{term} ({', '.join(locations)})" for term, locations in overloaded.items())
        print(f"- Overloaded terms to define and preserve carefully: {rendered}")
    print("- Multiple terms in one family are not automatic errors. Check whether they denote distinct constructs or accidental synonym cycling.")


def print_number_inventory(sections: dict[str, str]) -> None:
    print("\nHeadline-number inventory")
    found = False
    for section in ("abstract", "results", "discussion_or_conclusion"):
        numbers = extract_numbers(sections.get(section, ""))
        if numbers:
            found = True
            print(f"- {SECTION_LABELS[section]}: {', '.join(numbers[:20])}")
    if not found:
        print("- No numbers detected in the abstract, results, or conclusion regions.")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", default="working paper")
    parser.add_argument("--max-claims", type=int, default=3, help="candidate claims shown per section")
    args = parser.parse_args()

    raw = sys.stdin.read()
    if not raw.strip():
        print("No manuscript text provided. Pipe Markdown, LaTeX source, or plain text into this script.")
        return 1

    sections, headings = parse_sections(raw)
    print(f"OR/MS manuscript-contract audit: target={args.target}")
    print("Diagnostic only. Confirm every flag by close reading before revising.\n")
    print_section_inventory(sections, headings)

    detected_contract_sections = [section for section in SECTION_ORDER[:5] if section in sections]
    if len(detected_contract_sections) < 2:
        print("\n- Fewer than two contract sections were detected, so cross-section comparisons are limited. Check heading syntax or provide a fuller manuscript.")

    claims = print_claim_inventory(sections, max(1, args.max_claims))
    print_diagnostics(sections, claims)
    print_term_inventory(sections)
    print_number_inventory(sections)

    print("\nManual contract questions")
    questions = [
        "Do all sections preserve the same central object and canonical term?",
        "Does every headline comparison use the same comparator and metric as its supporting theorem, estimate, or experiment?",
        "Does the conclusion preserve the evidence type, magnitude, population or policy class, and boundary of the results?",
        "Can a reviewer identify what proves, estimates, validates, or merely illustrates each central claim?",
        "Does each cross-field object receive one useful bridge and then keep its canonical name?",
        "Does the body state the meaning and credibility checkpoint before relying on appendix verification?",
        "Have citations been checked against the relevant full-text model, data, result, or proof passage rather than title or abstract alone?",
    ]
    for question in questions:
        print(f"- {question}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Regression tests for routing and diagnostic false positives."""

from __future__ import annotations

import importlib.util
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


def load_script(name: str):
    path = ROOT / "scripts" / f"{name}.py"
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


check_paragraph = load_script("check_paragraph")
audit_manuscript_contract = load_script("audit_manuscript_contract")
place_results = load_script("place_results")
plan_manuscript = load_script("plan_manuscript")
plan_math_split = load_script("plan_math_split")
plan_section = load_script("plan_section")
triage_request = load_script("triage_request")


class TokenBoundaryTests(unittest.TestCase):
    def test_place_results_avoids_substring_false_positives(self) -> None:
        self.assertEqual(
            place_results.classify_item("showcase result", "working paper", "regular")[0],
            "Needs judgment",
        )
        self.assertEqual(
            place_results.classify_item("benefit estimate", "working paper", "regular")[0],
            "Needs judgment",
        )
        self.assertEqual(
            place_results.classify_item("all remaining experiments", "working paper", "regular")[0],
            "Online appendix or e-companion",
        )

    def test_math_split_distinguishes_case_from_showcase(self) -> None:
        self.assertEqual(plan_math_split.classify("showcase only")[0], "Needs judgment")
        self.assertEqual(plan_math_split.classify("a short case split")[0], "Verification detail")

    def test_math_split_allows_direct_theorem_application_as_proof_idea(self) -> None:
        role, _, advice = plan_math_split.classify(
            "apply Theorem 2 after verifying Lipschitz continuity"
        )
        self.assertEqual(role, "Proof idea")
        self.assertIn("condition", advice)
        self.assertEqual(
            plan_math_split.classify("Theorem 2 establishes monotonicity")[0],
            "Formal result",
        )

    def test_manuscript_new_does_not_match_newsvendor(self) -> None:
        self.assertEqual(
            plan_manuscript.classify("newsvendor model with censored demand"),
            "Model object",
        )


class RoutingTests(unittest.TestCase):
    def test_triage_reference_and_script_caps(self) -> None:
        request = "rewrite the model and proof idea, repair the logic, and check the citations"
        sequence = triage_request.choose_sequence(triage_request.score_modes(request))
        refs = triage_request.recommended_references(sequence)
        scripts = triage_request.recommended_scripts(sequence)
        self.assertLessEqual(len(refs), 4)
        self.assertLessEqual(len(scripts), 3)
        self.assertIn("management-science-model-proof-equation-layout.md", refs)

    def test_section_routes_remain_compact(self) -> None:
        self.assertTrue(plan_section.REFS)
        self.assertTrue(all(len(refs) <= 4 for refs in plan_section.REFS.values()))

    def test_classical_optimization_does_not_trigger_classic_paper_mode(self) -> None:
        scores = triage_request.score_modes("polish this classical optimization sentence")
        self.assertEqual(scores["impact"], 0)


class DiagnosticTests(unittest.TestCase):
    def test_metadata_heading_is_not_misclassified_as_data(self) -> None:
        sections, headings = audit_manuscript_contract.parse_sections(
            "## Metadata\nRepository details.\n## Results\nWe report the estimate."
        )
        self.assertNotIn(("model_or_design", "Metadata"), headings)
        self.assertIn(("results", "Results"), headings)
        self.assertIn("other", sections)

    def test_formal_colon_math_url_and_numeric_range_are_not_ai_punctuation(self) -> None:
        text = (
            "Definition A: Let $A:=\\{x:x>0\\}$. "
            "The period 2019–2020 defines the sample. https://example.com"
        )
        self.assertEqual(check_paragraph.punctuation_scent(text), [])

    def test_colon_led_label_and_spaced_dash_are_flagged(self) -> None:
        text = "Key insight: the policy improves profit — but only in one regime."
        warnings = check_paragraph.punctuation_scent(text)
        self.assertTrue(any("colon-led" in warning for warning in warnings))
        self.assertTrue(any("dash pivot" in warning for warning in warnings))

    def test_decorative_triplet_is_detected(self) -> None:
        warnings = check_paragraph.decorative_triplet_warnings(
            "We propose a robust, scalable, and efficient framework."
        )
        self.assertTrue(warnings)


if __name__ == "__main__":
    unittest.main()

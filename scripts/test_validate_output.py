#!/usr/bin/env python3
"""Regression tests for the generated-output release gate."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from validate_output import validate_output


ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = (ROOT / "template.html").read_text(encoding="utf-8")


class OutputValidatorTests(unittest.TestCase):
    def validate_text(self, text: str):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "review.html"
            path.write_text(text, encoding="utf-8")
            return validate_output(path)

    def assert_rejected(self, text: str, expected: str) -> None:
        report = self.validate_text(text)
        self.assertFalse(report.ok)
        self.assertTrue(any(expected in item for item in report.errors), report.errors)

    def test_template_is_compliant(self) -> None:
        report = self.validate_text(TEMPLATE)
        self.assertTrue(report.ok, report.errors)

    def test_missing_contract_is_rejected(self) -> None:
        broken = TEMPLATE.replace('id="courseReviewContract"', 'id="removedContract"', 1)
        self.assert_rejected(broken, "Missing #courseReviewContract")

    def test_pass_guarantee_is_rejected(self) -> None:
        broken = TEMPLATE.replace("</main>", "<p>保证及格</p></main>", 1)
        self.assert_rejected(broken, "pass guarantee")

    def test_generic_frequency_claim_is_rejected(self) -> None:
        broken = TEMPLATE.replace("</main>", "<p>这是必考高频考点</p></main>", 1)
        self.assert_rejected(broken, "Generic-evidence output")

    def test_generic_mock_exam_claim_is_rejected(self) -> None:
        broken = TEMPLATE.replace("</main>", "<p>开始本课程模拟考试</p></main>", 1)
        self.assert_rejected(broken, "Generic-evidence output")

    def test_ai_mastery_influence_is_rejected(self) -> None:
        broken = TEMPLATE.replace('"affectsMastery": false', '"affectsMastery": true', 1)
        self.assert_rejected(broken, "externalAI.affectsMastery")

    def test_ai_error_evidence_guard_is_required(self) -> None:
        broken = TEMPLATE.replace(
            "event.userConfirmedErrorCategory = category;\n        if(event.affectsMastery){",
            "event.userConfirmedErrorCategory = category;\n        if(true){",
            1,
        )
        self.assert_rejected(broken, "Practice-only AI errors")

    def test_single_answer_mastery_is_rejected(self) -> None:
        broken = TEMPLATE.replace("apState[node.id] = 'provisional';", "apState[node.id] = 'mastered';", 1)
        self.assert_rejected(broken, "direct path action")

    def test_mastery_clamp_is_required(self) -> None:
        broken = TEMPLATE.replace(
            "successSpan >= STABLE_MASTERY_GAP_MS",
            "successSpan >= 0",
            1,
        )
        self.assert_rejected(broken, "successSpan >= STABLE_MASTERY_GAP_MS")

    def test_direct_mastery_request_must_recompute_evidence(self) -> None:
        broken = TEMPLATE.replace(
            "if(state === 'mastered'){\n      recomputeState(concept);",
            "if(state === 'mastered'){\n      concept.state = 'mastered';",
            1,
        )
        self.assert_rejected(broken, "recomputed from stored evidence")

    def test_long_first_action_is_rejected(self) -> None:
        broken = TEMPLATE.replace('"durationMinutes": 8', '"durationMinutes": 15', 1)
        self.assert_rejected(broken, "between 5 and 10")

    def test_mastery_gap_contract_must_match_runtime(self) -> None:
        broken = TEMPLATE.replace('"stableGapMinutes": 30', '"stableGapMinutes": 45', 1)
        self.assert_rejected(broken, "Runtime stable mastery gap")

    def test_teacher_review_claim_is_rejected(self) -> None:
        broken = TEMPLATE.replace("</main>", "<p>本题库已通过老师审核</p></main>", 1)
        self.assert_rejected(broken, "teacher review")

    def test_contract_must_cover_every_path_node(self) -> None:
        broken = TEMPLATE.replace("{ id: 'c8', name: '曲线积分'", "{ id: 'c9', name: '曲线积分'", 1)
        self.assert_rejected(broken, "must match every knowledgeGraph node")

    def test_contract_prerequisites_must_match_path(self) -> None:
        broken = TEMPLATE.replace("{ id: 'c7', name: '三重积分', chapter: 7, prereqs: ['c6']", "{ id: 'c7', name: '三重积分', chapter: 7, prereqs: ['c5']", 1)
        self.assert_rejected(broken, "prerequisites must match")

    def test_string_chapter_labels_are_supported(self) -> None:
        adapted = TEMPLATE.replace("chapter: 8, prereqs: ['c7']", "chapter: 'Unit 8', prereqs: ['c7']", 1)
        report = self.validate_text(adapted)
        self.assertTrue(report.ok, report.errors)

    def test_contract_rejects_extra_fields(self) -> None:
        broken = TEMPLATE.replace('"contractVersion": "1.0",', '"contractVersion": "1.0",\n  "unexpected": true,', 1)
        self.assert_rejected(broken, "unsupported keys")


if __name__ == "__main__":
    unittest.main()

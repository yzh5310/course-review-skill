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

    def test_unescaped_angle_bracket_in_math_is_rejected(self) -> None:
        broken = TEMPLATE.replace("</main>", "<p>$P(a<X<b)$</p></main>", 1)
        self.assert_rejected(broken, "unescaped")

    def test_pass_guarantee_is_rejected(self) -> None:
        broken = TEMPLATE.replace("</main>", "<p>保证及格</p></main>", 1)
        self.assert_rejected(broken, "pass guarantee")

    def test_one_day_pass_guarantee_is_rejected(self) -> None:
        broken = TEMPLATE.replace("</main>", "<p>考前1天保证通过</p></main>", 1)
        self.assert_rejected(broken, "pass guarantee")

    def test_no_fail_claim_is_rejected(self) -> None:
        broken = TEMPLATE.replace("</main>", "<p>跟着学就不挂科</p></main>", 1)
        self.assert_rejected(broken, "pass guarantee")

    def test_ai_preview_uses_text_nodes(self) -> None:
        self.assertIn("container.replaceChildren();", TEMPLATE)
        self.assertIn("question.textContent", TEMPLATE)
        self.assertNotIn("container.innerHTML = questions.map", TEMPLATE)

    def test_ai_explanation_uses_text_nodes(self) -> None:
        self.assertIn("renderStructuredExplanation(explanation, q.explanation", TEMPLATE)
        self.assertIn("document.createTextNode(part)", TEMPLATE)
        self.assertIn("badge.textContent = badgeText;", TEMPLATE)
        self.assertIn(".exp-row.exp-conclusion", TEMPLATE)
        self.assertIn(".exp-row.exp-tip", TEMPLATE)
        self.assertIn("wb-exp-slot", TEMPLATE)
        self.assertNotIn("(q.explanation || '查看解析') + '</div>'", TEMPLATE)

    def test_mobile_tooltips_are_viewport_bounded(self) -> None:
        self.assertIn("position: fixed;", TEMPLATE)
        self.assertIn("left: 16px;", TEMPLATE)
        self.assertIn("right: 16px;", TEMPLATE)
        self.assertIn(".term:hover .term-tooltip { visibility: visible; }", TEMPLATE)

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
        broken = TEMPLATE.replace("LearningMemory.recordMastery(node.id, 'provisional', 'micro-check');", "apState[node.id] = 'mastered';", 1)
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
            "else recomputeState(concept);",
            "else concept.state = state;",
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

    def test_handoff_cannot_require_return_by_default(self) -> None:
        broken = TEMPLATE.replace('"defaultWorkflow": "external-dialogue-no-return"', '"defaultWorkflow": "return-and-import"', 1)
        self.assert_rejected(broken, "externalAI.defaultWorkflow")

    def test_handoff_cannot_claim_automatic_sync(self) -> None:
        broken = TEMPLATE.replace('"externalActivityAutoSynced": false', '"externalActivityAutoSynced": true', 1)
        self.assert_rejected(broken, "externalAI.externalActivityAutoSynced")

    def test_template_derives_default_depth_from_coverage_mode(self) -> None:
        self.assertIn("COURSE_META.coverageMode", TEMPLATE)
        self.assertNotIn("var saved = lsGet('depth', 'standard');", TEMPLATE)

    def test_template_escapes_excerpts_and_exports_srs(self) -> None:
        self.assertIn("escapeHTML(e.text)", TEMPLATE)
        self.assertIn("'srs'", TEMPLATE)

    def test_template_options_define_selected_and_dark_text_styles(self) -> None:
        self.assertIn(".diag-opt.selected", TEMPLATE)
        self.assertIn(".qb-opt.selected::after", TEMPLATE)
        self.assertIn("background: var(--card); color: var(--text);", TEMPLATE)
        self.assertIn("body.dark select", TEMPLATE)

    def test_ascii_matrix_subscript_is_rejected_in_quantitative_course(self) -> None:
        broken = TEMPLATE.replace("</main>", "<p>若矩阵 A_(3×4) 经过初等行变换</p></main>", 1)
        self.assert_rejected(broken, "ASCII parenthesized subscript")

    def test_nested_bracket_matrix_is_rejected_in_quantitative_course(self) -> None:
        target = "hint: '提示：把y当常数，y³也是常数，导数为0的是常数项。'"
        broken = TEMPLATE.replace(target, "hint: '矩阵 [[3, 2], [4, 3]] 的伴随矩阵'", 1)
        self.assertNotEqual(broken, TEMPLATE)
        self.assert_rejected(broken, "nested-bracket matrix literal")

    def test_ascii_parenthesized_exponent_is_rejected_in_quantitative_course(self) -> None:
        target = "hint: '提示：把y当常数，y³也是常数，导数为0的是常数项。'"
        broken = TEMPLATE.replace(target, "hint: '系数为 (-1)^(n(n-1)/2) 与 k^(n-1)'", 1)
        self.assertNotEqual(broken, TEMPLATE)
        self.assert_rejected(broken, "ASCII parenthesized exponent")

    def test_non_quantitative_course_allows_nested_arrays(self) -> None:
        adapted = TEMPLATE.replace("courseType: 'quantitative'", "courseType: 'programming'", 1).replace(
            "</main>", "<p>二维数组示例 [[1, 2], [3, 4]]</p></main>", 1
        )
        report = self.validate_text(adapted)
        self.assertTrue(report.ok, report.errors)

    def test_quantitative_dynamic_math_requires_quiz_katex_hook(self) -> None:
        target = "hint: '提示：把y当常数，y³也是常数，导数为0的是常数项。'"
        broken = TEMPLATE.replace(
            target,
            "hint: '计算 $A_{3\\\\times 4}$ 的秩'",
            1,
        ).replace("renderMath(document.getElementById('qbCard'));", "", 1)
        self.assertNotEqual(broken, TEMPLATE)
        self.assert_rejected(broken, "re-rendering KaTeX in QuizSystem.renderQuestion")

    def test_template_wires_dynamic_katex_rendering(self) -> None:
        self.assertIn("function renderMath(el)", TEMPLATE)
        self.assertIn("renderMath(box);", TEMPLATE)
        self.assertIn("renderMath(document.getElementById('qbCard'));", TEMPLATE)
        self.assertIn("renderMath(fb);", TEMPLATE)
        self.assertIn("renderMath(list);", TEMPLATE)

    def test_template_includes_progress_pills_and_intentional_view_hooks(self) -> None:
        self.assertIn('id="aiProgressPills"', TEMPLATE)
        self.assertIn(".ai-prog-pill.is-done", TEMPLATE)
        self.assertIn(".ai-prog-pill.is-current", TEMPLATE)
        self.assertIn("markViewed:markViewed", TEMPLATE)
        self.assertIn("setSelfProgress:setSelfProgress", TEMPLATE)
        self.assertIn("entryPoint: 'section-help'", TEMPLATE)


if __name__ == "__main__":
    unittest.main()

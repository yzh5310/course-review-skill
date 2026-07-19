#!/usr/bin/env python3
"""Fail-closed validation for generated course-review HTML artifacts."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass, field
from html.parser import HTMLParser
from pathlib import Path
from typing import Any


EVIDENCE_LEVELS = {"exam-grounded", "course-grounded", "generic"}
COVERAGE_MODES = {"minimum-core", "standard-coverage", "extended-improvement"}
SOURCE_TYPES = {"past-paper", "scope", "rubric", "slide", "assignment", "textbook", "topic-list", "other"}


@dataclass
class ValidationReport:
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.errors

    def fail(self, message: str) -> None:
        self.errors.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)


class ArtifactParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: list[str] = []
        self.visible_text: list[str] = []
        self.contract_parts: list[str] = []
        self._hidden_depth = 0
        self._in_contract = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = dict(attrs)
        value = attrs_dict.get("id")
        if value:
            self.ids.append(value)
        if tag in {"script", "style", "template"}:
            self._hidden_depth += 1
        if tag == "script" and value == "courseReviewContract":
            self._in_contract = True

    def handle_endtag(self, tag: str) -> None:
        if tag == "script" and self._in_contract:
            self._in_contract = False
        if tag in {"script", "style", "template"} and self._hidden_depth:
            self._hidden_depth -= 1

    def handle_data(self, data: str) -> None:
        if self._in_contract:
            self.contract_parts.append(data)
        elif not self._hidden_depth and data.strip():
            self.visible_text.append(data.strip())


def _expect_mapping(value: Any, name: str, report: ValidationReport) -> dict[str, Any]:
    if not isinstance(value, dict):
        report.fail(f"Contract field '{name}' must be an object")
        return {}
    return value


def _expect_nonempty(value: Any, name: str, report: ValidationReport, minimum: int = 1) -> None:
    if not isinstance(value, str) or len(value.strip()) < minimum:
        report.fail(f"Contract field '{name}' must be a non-empty explanatory string")


def _expect_exact_keys(
    value: dict[str, Any], name: str, keys: set[str], report: ValidationReport
) -> None:
    missing = sorted(keys - set(value))
    extra = sorted(set(value) - keys)
    if missing:
        report.fail(f"Contract field '{name}' is missing keys: {', '.join(missing)}")
    if extra:
        report.fail(f"Contract field '{name}' has unsupported keys: {', '.join(extra)}")


def _validate_contract(contract: dict[str, Any], report: ValidationReport) -> None:
    _expect_exact_keys(
        contract,
        "root",
        {"contractVersion", "skill", "course", "evidence", "coverage", "path", "learningMemory", "externalAI", "claims"},
        report,
    )
    if contract.get("contractVersion") != "1.0":
        report.fail("contractVersion must be '1.0'")

    skill = _expect_mapping(contract.get("skill"), "skill", report)
    _expect_exact_keys(skill, "skill", {"name", "version"}, report)
    if skill.get("name") != "course-review":
        report.fail("skill.name must be 'course-review'")
    if not re.fullmatch(r"5\.\d+(?:\.\d+)?", str(skill.get("version", ""))):
        report.fail("skill.version must be a v5 version")

    course = _expect_mapping(contract.get("course"), "course", report)
    _expect_exact_keys(course, "course", {"name", "slug"}, report)
    _expect_nonempty(course.get("name"), "course.name", report)
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", str(course.get("slug", ""))):
        report.fail("course.slug must contain lowercase letters, digits, or hyphens")

    evidence = _expect_mapping(contract.get("evidence"), "evidence", report)
    _expect_exact_keys(evidence, "evidence", {"level", "summary", "sources"}, report)
    level = evidence.get("level")
    if level not in EVIDENCE_LEVELS:
        report.fail("evidence.level must be exam-grounded, course-grounded, or generic")
    _expect_nonempty(evidence.get("summary"), "evidence.summary", report, minimum=8)
    sources = evidence.get("sources")
    if not isinstance(sources, list):
        report.fail("evidence.sources must be an array")
        sources = []
    for index, source in enumerate(sources, start=1):
        if not isinstance(source, dict):
            report.fail(f"evidence.sources[{index}] must be an object")
            continue
        _expect_exact_keys(source, f"evidence.sources[{index}]", {"type", "label"}, report)
        if source.get("type") not in SOURCE_TYPES:
            report.fail(f"evidence.sources[{index}].type is invalid")
        _expect_nonempty(source.get("label"), f"evidence.sources[{index}].label", report)
    if level in {"exam-grounded", "course-grounded"} and not sources:
        report.fail(f"{level} output must list at least one evidence source")
    if level == "exam-grounded":
        source_types = {item.get("type") for item in sources if isinstance(item, dict)}
        if "past-paper" not in source_types:
            report.fail("exam-grounded output must cite a past-paper source")
        if not source_types.intersection({"scope", "rubric"}):
            report.fail("exam-grounded output must cite an exam scope or rubric")

    coverage = _expect_mapping(contract.get("coverage"), "coverage", report)
    _expect_exact_keys(coverage, "coverage", {"mode", "remainingMinutes"}, report)
    if coverage.get("mode") not in COVERAGE_MODES:
        report.fail("coverage.mode is invalid")
    remaining = coverage.get("remainingMinutes")
    if remaining is not None and (not isinstance(remaining, int) or isinstance(remaining, bool) or remaining < 1):
        report.fail("coverage.remainingMinutes must be null or a positive integer")

    path = _expect_mapping(contract.get("path"), "path", report)
    _expect_exact_keys(path, "path", {"objectives", "nextAction", "cutoffRule"}, report)
    objectives = path.get("objectives")
    if not isinstance(objectives, list) or not objectives:
        report.fail("path.objectives must contain at least one objective")
        objectives = []
    objective_ids: set[str] = set()
    prerequisite_sets: list[tuple[int, str | None, list[Any]]] = []
    for index, objective in enumerate(objectives, start=1):
        if not isinstance(objective, dict):
            report.fail(f"path.objectives[{index}] must be an object")
            continue
        _expect_exact_keys(
            objective,
            f"path.objectives[{index}]",
            {"id", "title", "priorityReason", "evidenceBasis", "uncertainty", "prerequisiteIds"},
            report,
        )
        objective_id = objective.get("id")
        if not isinstance(objective_id, str) or not objective_id:
            report.fail(f"path.objectives[{index}].id is required")
        elif objective_id in objective_ids:
            report.fail(f"Duplicate objective id: {objective_id}")
        else:
            objective_ids.add(objective_id)
        for key, minimum in (("title", 1), ("priorityReason", 8), ("evidenceBasis", 4), ("uncertainty", 4)):
            _expect_nonempty(objective.get(key), f"path.objectives[{index}].{key}", report, minimum)
        prerequisites = objective.get("prerequisiteIds")
        if not isinstance(prerequisites, list):
            report.fail(f"path.objectives[{index}].prerequisiteIds must be an array")
        else:
            prerequisite_sets.append((index, objective_id if isinstance(objective_id, str) else None, prerequisites))

    for index, objective_id, prerequisites in prerequisite_sets:
        for prerequisite in prerequisites:
            if not isinstance(prerequisite, str) or prerequisite not in objective_ids:
                report.fail(f"path.objectives[{index}] references an unknown prerequisite")
            if prerequisite == objective_id:
                report.fail(f"path.objectives[{index}] cannot require itself")

    next_action = _expect_mapping(path.get("nextAction"), "path.nextAction", report)
    _expect_exact_keys(next_action, "path.nextAction", {"objectiveId", "label", "durationMinutes"}, report)
    if next_action.get("objectiveId") not in objective_ids:
        report.fail("path.nextAction.objectiveId must reference a declared objective")
    _expect_nonempty(next_action.get("label"), "path.nextAction.label", report, minimum=4)
    duration = next_action.get("durationMinutes")
    if not isinstance(duration, int) or isinstance(duration, bool) or not 5 <= duration <= 10:
        report.fail("path.nextAction.durationMinutes must be between 5 and 10")
    _expect_nonempty(path.get("cutoffRule"), "path.cutoffRule", report, minimum=8)

    memory = _expect_mapping(contract.get("learningMemory"), "learningMemory", report)
    _expect_exact_keys(
        memory,
        "learningMemory",
        {"storageKeySuffix", "masteryRequiresMultipleSignals", "singleAnswerCanMaster", "provisionalGapMinutes", "stableGapMinutes"},
        report,
    )
    if memory.get("storageKeySuffix") != "learning_profile":
        report.fail("learningMemory.storageKeySuffix must be 'learning_profile'")
    if memory.get("masteryRequiresMultipleSignals") is not True:
        report.fail("learningMemory.masteryRequiresMultipleSignals must be true")
    if memory.get("singleAnswerCanMaster") is not False:
        report.fail("learningMemory.singleAnswerCanMaster must be false")
    if not isinstance(memory.get("provisionalGapMinutes"), int) or memory.get("provisionalGapMinutes") < 5:
        report.fail("learningMemory.provisionalGapMinutes must be at least 5")
    if not isinstance(memory.get("stableGapMinutes"), int) or memory.get("stableGapMinutes") < 30:
        report.fail("learningMemory.stableGapMinutes must be at least 30")

    external = _expect_mapping(contract.get("externalAI"), "externalAI", report)
    _expect_exact_keys(
        external,
        "externalAI",
        {"enabled", "practiceOnly", "teacherReviewed", "promptPreviewRequired", "anonymousByDefault", "affectsMastery"},
        report,
    )
    if not isinstance(external.get("enabled"), bool):
        report.fail("externalAI.enabled must be a boolean")
    if external.get("practiceOnly") is not True:
        report.fail("externalAI.practiceOnly must be true")
    if external.get("teacherReviewed") is not False:
        report.fail("externalAI.teacherReviewed must be false")
    if external.get("promptPreviewRequired") is not True:
        report.fail("externalAI.promptPreviewRequired must be true")
    if external.get("anonymousByDefault") is not True:
        report.fail("externalAI.anonymousByDefault must be true")
    if external.get("affectsMastery") is not False:
        report.fail("externalAI.affectsMastery must be false")

    claims = _expect_mapping(contract.get("claims"), "claims", report)
    _expect_exact_keys(claims, "claims", {"scorePrediction", "passGuarantee", "inferredFrequencyClaims"}, report)
    for key in ("scorePrediction", "passGuarantee", "inferredFrequencyClaims"):
        if claims.get(key) is not False:
            report.fail(f"claims.{key} must be false")


def _check_forbidden_claims(visible_text: str, evidence_level: str | None, report: ValidationReport) -> None:
    pass_patterns = {
        "pass guarantee": r"(?:稳过|保过|包过|必过|及格绝对没问题|(?<!不)保证.{0,12}(?:及格|通过))",
        "score prediction": r"(?:预测分数|预计.{0,8}(?:得分|分数|考到)\s*\d+|通过率\s*\d+%|predicted score|will score\s*\d+)",
    }
    for label, pattern in pass_patterns.items():
        if re.search(pattern, visible_text, re.I):
            report.fail(f"Visible content contains a prohibited {label} claim")

    if evidence_level == "generic":
        generic_patterns = {
            "unsupported frequency": r"(?:高频考点|高频题型|high[- ]frequency)",
            "must-test claim": r"(?:必考|一定会考|must[- ]test)",
            "exam prediction": r"(?:押题|预测题|模拟考试|模拟卷|predicted exam|mock exam)",
        }
        for label, pattern in generic_patterns.items():
            if re.search(pattern, visible_text, re.I):
                report.fail(f"Generic-evidence output contains an {label}")

    positive_review = r"(?:已通过.{0,10}(?:教师|老师).{0,6}(?:审阅|审核)|经(?:教师|老师).{0,6}(?:审阅|审核)|teacher[- ]reviewed)"
    if re.search(positive_review, visible_text, re.I):
        report.fail("Visible content claims teacher review")


def _validate_javascript(text: str, report: ValidationReport) -> None:
    scripts = re.findall(r"<script(?![^>]*(?:\bsrc=|\btype=[\"']application/json))[^>]*>(.*?)</script>", text, re.I | re.S)
    if not scripts:
        report.fail("No executable inline JavaScript found")
        return
    node = shutil.which("node")
    if not node:
        report.warn("Node.js not found; skipped JavaScript syntax validation")
        return
    for index, script in enumerate(scripts, start=1):
        with tempfile.NamedTemporaryFile("w", suffix=".js", encoding="utf-8", delete=False) as handle:
            handle.write(script)
            temp_path = Path(handle.name)
        try:
            result = subprocess.run([node, "--check", str(temp_path)], capture_output=True, text=True)
            if result.returncode:
                report.fail(f"Inline script {index} has invalid JavaScript: {result.stderr.strip()}")
        finally:
            temp_path.unlink(missing_ok=True)


def validate_output(path: Path) -> ValidationReport:
    report = ValidationReport()
    try:
        text = path.read_text(encoding="utf-8")
    except Exception as exc:
        report.fail(f"Cannot read artifact as UTF-8: {exc}")
        return report

    parser = ArtifactParser()
    try:
        parser.feed(text)
    except Exception as exc:
        report.fail(f"Cannot parse HTML: {exc}")
        return report

    duplicates = sorted({value for value in parser.ids if parser.ids.count(value) > 1})
    if duplicates:
        report.fail("Duplicate HTML ids: " + ", ".join(duplicates))

    contract_text = "".join(parser.contract_parts).strip()
    contract: dict[str, Any] = {}
    if not contract_text:
        report.fail("Missing #courseReviewContract application/json manifest")
    else:
        try:
            loaded = json.loads(contract_text)
            if not isinstance(loaded, dict):
                report.fail("courseReviewContract must contain a JSON object")
            else:
                contract = loaded
                _validate_contract(contract, report)
        except json.JSONDecodeError as exc:
            report.fail(f"courseReviewContract is invalid JSON: {exc}")

    required_tokens = [
        "learning_profile",
        "var LearningMemory",
        "var REVIEW_CONTRACT",
        "PromptGeneratorV5",
        "aiPromptPreview",
        "diagnosticUse: false",
        "affectsMastery",
        "if(event.affectsMastery){",
        "PROVISIONAL_MASTERY_GAP_MS",
        "STABLE_MASTERY_GAP_MS",
        "successSpan >= STABLE_MASTERY_GAP_MS",
        "contractObjective.priorityReason",
        "evidenceSources: REVIEW_CONTRACT.evidence.sources",
        'id="nextActionCard"',
        'id="coverageNotice"',
    ]
    for token in required_tokens:
        if token not in text:
            report.fail(f"Generated artifact is missing invariant: {token}")

    evidence_level = contract.get("evidence", {}).get("level") if contract else None
    visible_text = " ".join(parser.visible_text)
    _check_forbidden_claims(visible_text, evidence_level, report)

    if contract:
        course = contract.get("course", {})
        evidence = contract.get("evidence", {})
        coverage = contract.get("coverage", {})
        summary = evidence.get("summary")
        if isinstance(summary, str) and summary not in visible_text:
            report.fail("Evidence summary in the contract is not visible in the artifact")
        course_name = re.search(r"courseName:\s*['\"]([^'\"]+)", text)
        course_slug = re.search(r"courseSlug:\s*['\"]([^'\"]+)", text)
        if not course_name or course_name.group(1) != course.get("name"):
            report.fail("COURSE_META courseName does not match the contract")
        if not course_slug or course_slug.group(1) != course.get("slug"):
            report.fail("COURSE_META courseSlug does not match the contract")
        meta_level = re.search(r"evidenceLevel:\s*['\"]([^'\"]+)", text)
        if not meta_level or meta_level.group(1) != evidence_level:
            report.fail("COURSE_META evidenceLevel does not match the contract")
        meta_mode = re.search(r"coverageMode:\s*['\"]([^'\"]+)", text)
        if not meta_mode or meta_mode.group(1) != coverage.get("mode"):
            report.fail("COURSE_META coverageMode does not match the contract")
        meta_minutes = re.search(r"remainingMinutes:\s*(null|\d+)", text)
        parsed_minutes = None if meta_minutes and meta_minutes.group(1) == "null" else (
            int(meta_minutes.group(1)) if meta_minutes else "missing"
        )
        if parsed_minutes != coverage.get("remainingMinutes"):
            report.fail("COURSE_META remainingMinutes does not match the contract")
        visible_evidence = re.search(r'id="evidenceNotice"[^>]*data-evidence-level="([^"]+)"', text)
        if not visible_evidence or visible_evidence.group(1) != evidence_level:
            report.fail("Visible evidence notice does not match the contract")
        visible_coverage = re.search(r'id="coverageNotice"[^>]*data-coverage-mode="([^"]+)"', text)
        if not visible_coverage or visible_coverage.group(1) != coverage.get("mode"):
            report.fail("Visible coverage notice does not match the contract")
        next_action = contract.get("path", {}).get("nextAction", {})
        action_id = re.search(r'id="nextActionCard"[^>]*data-objective-id="([^"]+)"', text)
        action_duration = re.search(r'id="nextActionCard"[^>]*data-objective-id="[^"]+"[^>]*data-duration-minutes="(\d+)"', text)
        if not action_id or action_id.group(1) != next_action.get("objectiveId"):
            report.fail("Visible next action objective does not match the contract")
        if not action_duration or int(action_duration.group(1)) != next_action.get("durationMinutes"):
            report.fail("Visible next action duration does not match the contract")
        if next_action.get("label") not in visible_text:
            report.fail("Visible next action label does not match the contract")

        graph_match = re.search(r"var knowledgeGraph\s*=\s*\[(.*?)\n\];", text, re.S)
        graph_nodes = re.findall(
            r"\{\s*id:\s*['\"]([^'\"]+)['\"],\s*name:\s*['\"]([^'\"]+)['\"],\s*chapter:\s*(?:\d+|['\"][^'\"]+['\"]),\s*prereqs:\s*\[([^\]]*)\]",
            graph_match.group(1),
        ) if graph_match else []
        parsed_graph = [
            (node_id, title, re.findall(r"['\"]([^'\"]+)['\"]", prerequisite_text))
            for node_id, title, prerequisite_text in graph_nodes
        ]
        contract_nodes = [
            (item.get("id"), item.get("title"), item.get("prerequisiteIds"))
            for item in contract.get("path", {}).get("objectives", [])
            if isinstance(item, dict)
        ]
        if not parsed_graph:
            report.fail("Cannot isolate knowledgeGraph objectives")
        elif parsed_graph != contract_nodes:
            report.fail("Contract objectives, titles, and prerequisites must match every knowledgeGraph node in order")

        memory_contract = contract.get("learningMemory", {})
        provisional_gap = re.search(r"PROVISIONAL_MASTERY_GAP_MS\s*=\s*(\d+)\s*\*\s*60\s*\*\s*1000", text)
        stable_gap = re.search(r"STABLE_MASTERY_GAP_MS\s*=\s*(\d+)\s*\*\s*60\s*\*\s*1000", text)
        if not provisional_gap or int(provisional_gap.group(1)) != memory_contract.get("provisionalGapMinutes"):
            report.fail("Runtime provisional mastery gap does not match the contract")
        if not stable_gap or int(stable_gap.group(1)) != memory_contract.get("stableGapMinutes"):
            report.fail("Runtime stable mastery gap does not match the contract")

    prompt_match = re.search(r"var PromptGeneratorV5\s*=\s*\{(.*?)\n\};\s*\n\s*var PromptGenerator", text, re.S)
    if not prompt_match:
        report.fail("Cannot isolate PromptGeneratorV5 privacy boundary")
    else:
        prompt_code = prompt_match.group(1)
        for personal_token in ("studentName", ".school", ".major", "rawWrongQuestions", "excerpts"):
            if personal_token in prompt_code:
                report.fail(f"PromptGeneratorV5 includes personal/raw field: {personal_token}")

    if "independentCorrect >= 3" not in text:
        report.fail("Stable mastery must require at least three independent correct attempts")
    record_mastery_match = re.search(
        r"function recordMastery\(.*?\n\s*function summary", text, re.S
    )
    if not record_mastery_match or "recomputeState(concept)" not in record_mastery_match.group(0):
        report.fail("Direct mastery requests must be recomputed from stored evidence")
    confirm_error_match = re.search(
        r"function confirmError\(.*?\n\s*function recordMastery", text, re.S
    )
    if not confirm_error_match or "if(event.affectsMastery){" not in confirm_error_match.group(0):
        report.fail("Practice-only AI errors can still influence confirmed concept evidence")
    if re.search(r"apState\s*\[[^\]]+\]\s*=\s*['\"]mastered['\"]", text):
        report.fail("A direct path action can still mark mastery")

    _validate_javascript(text, report)
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("artifact", type=Path, help="Generated course-review HTML file")
    parser.add_argument("--json", action="store_true", dest="as_json", help="Emit a machine-readable report")
    args = parser.parse_args()

    report = validate_output(args.artifact.resolve())
    if args.as_json:
        print(json.dumps({"ok": report.ok, "errors": report.errors, "warnings": report.warnings}, ensure_ascii=False, indent=2))
    else:
        for message in report.warnings:
            print(f"WARNING: {message}")
        for message in report.errors:
            print(f"ERROR: {message}")
        if report.ok:
            print(f"Output validation passed: {args.artifact}")
        else:
            print(f"Output validation failed with {len(report.errors)} error(s): {args.artifact}")
    return 0 if report.ok else 1


if __name__ == "__main__":
    sys.exit(main())

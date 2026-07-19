#!/usr/bin/env python3
"""Validate the course-review skill without third-party dependencies."""

from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
import tempfile
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []
WARNINGS: list[str] = []


def fail(message: str) -> None:
    ERRORS.append(message)


def warn(message: str) -> None:
    WARNINGS.append(message)


def validate_json_files() -> None:
    for path in sorted(ROOT.rglob("*.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:  # pragma: no cover - diagnostic path
            fail(f"Invalid JSON: {path.relative_to(ROOT)}: {exc}")
            continue
        if path.name.endswith(".schema.json"):
            if data.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
                fail(f"Schema does not declare draft 2020-12: {path.relative_to(ROOT)}")
            if data.get("type") != "object":
                fail(f"Top-level schema type must be object: {path.relative_to(ROOT)}")


def validate_skill() -> None:
    path = ROOT / "SKILL.md"
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
    if not match:
        fail("SKILL.md is missing YAML frontmatter")
        return
    keys = []
    for line in match.group(1).splitlines():
        if ":" in line and not line.startswith((" ", "\t")):
            keys.append(line.split(":", 1)[0].strip())
    if keys != ["name", "description"]:
        fail(f"SKILL.md frontmatter must contain only name and description; got {keys}")
    if len(text.splitlines()) > 500:
        fail("SKILL.md exceeds the 500-line progressive-disclosure limit")

    for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
        if re.match(r"^[a-z]+://", target):
            continue
        resolved = (ROOT / target).resolve()
        if not resolved.exists():
            fail(f"Broken local link in SKILL.md: {target}")


class IdCollector(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        for key, value in attrs:
            if key == "id" and value:
                self.ids.append(value)


def validate_template() -> None:
    path = ROOT / "template.html"
    text = path.read_text(encoding="utf-8")

    required = [
        "learning_profile",
        "var LearningMemory",
        "var PromptGeneratorV5",
        "evidenceLevel",
        "diagnosticUse",
        "aiPromptPreview",
        "prefers-reduced-motion",
    ]
    for token in required:
        if token not in text:
            fail(f"template.html missing v5 invariant: {token}")

    forbidden = ["LS('adaptive_path')", "LS('qb_progress')"]
    for token in forbidden:
        if token in text:
            fail(f"template.html still reads deprecated state directly: {token}")

    score_promises = [
        "补考救命(60分)",
        "稳过及格(80分)",
        "冲刺高分(90+)",
        "及格绝对没问题",
        "祝考试顺利，一次过",
        "选择你的目标档位",
    ]
    for token in score_promises:
        if token in text:
            fail(f"template.html still contains a score-promise coverage label: {token}")

    legacy_prompt_tokens = ["你是一位资深的", "历史正确率约：", "以考试常见题型为准"]
    for token in legacy_prompt_tokens:
        if token in text:
            fail(f"template.html still contains the retired v4 prompt generator: {token}")

    parser = IdCollector()
    parser.feed(text)
    duplicates = sorted({item for item in parser.ids if parser.ids.count(item) > 1})
    if duplicates:
        fail("Duplicate HTML ids: " + ", ".join(duplicates))

    scripts = re.findall(
        r"<script(?![^>]*(?:\bsrc=|\btype=[\"']application/json))[^>]*>(.*?)</script>",
        text,
        re.I | re.S,
    )
    if not scripts:
        fail("No inline scripts found in template.html")
        return
    node = shutil.which("node")
    if not node:
        warn("Node.js not found; skipped JavaScript syntax validation")
        return
    for index, script in enumerate(scripts, start=1):
        with tempfile.NamedTemporaryFile("w", suffix=".js", encoding="utf-8", delete=False) as handle:
            handle.write(script)
            temp_path = Path(handle.name)
        try:
            result = subprocess.run([node, "--check", str(temp_path)], capture_output=True, text=True)
            if result.returncode:
                fail(f"Inline script {index} has invalid JavaScript: {result.stderr.strip()}")
        finally:
            temp_path.unlink(missing_ok=True)


def validate_metadata() -> None:
    data = json.loads((ROOT / "skill.json").read_text(encoding="utf-8"))
    if data.get("version") != "5.1.0":
        fail("skill.json version must be 5.1.0")
    for relative in data.get("references", []):
        if not (ROOT / relative).exists():
            fail(f"skill.json references missing file: {relative}")
    for relative in [
        "agents/openai.yaml",
        "schemas/learning-profile.schema.json",
        "schemas/question.schema.json",
        "schemas/review-plan.schema.json",
        "references/output-contract.md",
        "scripts/validate_output.py",
        "scripts/test_validate_output.py",
    ]:
        if not (ROOT / relative).exists():
            fail(f"Missing required v5 file: {relative}")

    openai_yaml = (ROOT / "agents/openai.yaml").read_text(encoding="utf-8")
    if "$course-review" not in openai_yaml:
        fail("agents/openai.yaml default_prompt must invoke $course-review")
    if "\ufffd" in openai_yaml:
        fail("agents/openai.yaml contains replacement characters from broken encoding")

    entrypoints = ["AGENTS.md", "CLAUDE.md", ".cursorrules", ".windsurfrules", ".clinerules/course-review.md"]
    for relative in entrypoints:
        text = (ROOT / relative).read_text(encoding="utf-8")
        if "scripts/validate_output.py" not in text or "references/output-contract.md" not in text:
            fail(f"AI entrypoint does not enforce generated-output validation: {relative}")


def validate_generated_output_gate() -> None:
    commands = [
        [sys.executable, str(ROOT / "scripts/validate_output.py"), str(ROOT / "template.html")],
        [sys.executable, str(ROOT / "scripts/test_validate_output.py")],
    ]
    for command in commands:
        result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
        if result.returncode:
            output = (result.stdout + "\n" + result.stderr).strip()
            fail(f"Generated-output release gate failed: {' '.join(command[1:])}: {output}")


def main() -> int:
    validate_json_files()
    validate_skill()
    validate_template()
    validate_metadata()
    validate_generated_output_gate()

    for message in WARNINGS:
        print(f"WARNING: {message}")
    if ERRORS:
        for message in ERRORS:
            print(f"ERROR: {message}")
        print(f"Validation failed with {len(ERRORS)} error(s).")
        return 1
    print("Validation passed: metadata, references, schemas, HTML ids, and JavaScript syntax are valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

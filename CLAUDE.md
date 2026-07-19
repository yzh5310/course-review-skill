# Course Review Skill v5.0

The authoritative entrypoint is `SKILL.md`. Read it before generating or modifying a course review application.

Load only the references required by the task:

- Path, evidence, coverage, or mastery decisions: `references/path-generation.md`
- Learning memory and migration: `references/learning-profile.md`
- External-AI question prompts or imports: `references/question-generation.md`
- Course-specific learning loops: `references/course-profiles.md`
- UI and accessibility: `references/accessibility.md`
- HTML/JavaScript implementation: `references/implementation-guardrails.md`

Use `schemas/learning-profile.schema.json` and `schemas/question.schema.json` as normative data contracts.

Mandatory boundaries:

1. Do not predict scores or promise a pass.
2. Do not call inferred content high-frequency, must-test, or predicted.
3. Do not require teacher review; this version produces personal practice material.
4. Do not mark mastery from one answer.
5. Keep unverified AI questions practice-only.
6. Preview and minimize data before copying a prompt to an external AI.
7. Preserve attempt history when a wrongbook item is resolved.

Validate repository changes with:

```bash
python scripts/validate_repo.py
```

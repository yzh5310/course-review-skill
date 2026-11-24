# Course Review Skill v5.3.1

The authoritative entrypoint is `SKILL.md`. Read it before generating or modifying a course review application.

Load only the references required by the task:

- Path, evidence, coverage, or mastery decisions: `references/path-generation.md`
- Learning memory and migration: `references/learning-profile.md`
- External-AI tutoring handoffs or optional Agent imports: `references/question-generation.md`
- Course-specific learning loops: `references/course-profiles.md`
- UI and accessibility: `references/accessibility.md`
- HTML/JavaScript implementation: `references/implementation-guardrails.md`
- Generated artifact contract and release gate: `references/output-contract.md`
- Visual, interaction, and source-fidelity checks before delivery: `references/visual-qa.md`

Use `schemas/learning-profile.schema.json`, `schemas/question.schema.json`, and `schemas/review-plan.schema.json` as normative data contracts.

Mandatory boundaries:

1. Do not predict scores or promise a pass.
2. Do not call inferred content high-frequency, must-test, or predicted.
3. Do not require teacher review; this version produces personal practice material.
4. Do not mark mastery from one answer.
5. Default to external conversational tutoring without returning/importing; keep optional unverified imported AI questions practice-only.
6. Preview and minimize data before copying a prompt to an external AI.
7. Preserve attempt history when a wrongbook item is resolved.
8. Embed `#courseReviewContract` and keep it synchronized with visible evidence, coverage, and the next action.
9. Do not deliver a generated artifact until its output validator passes.
10. Verify claims about the learner's materials against those materials; never generalize about a problem set without enumerating it.
11. Run the visual and interaction checks in `references/visual-qa.md`; structural validation alone does not prove a control responds or a formula rendered.
12. For quantitative courses, use textbook LaTeX (`$...$` / `$$...$$`) matching the course's notation across static HTML and dynamic JS quiz/micro-quiz/wrongbook strings, call `renderMath(el)` on dynamic updates, and never leak ASCII shorthands such as `A_(3×4)`, `[[1,2],[3,4]]`, or `k^(n-1)`.

Validate repository changes with:

```bash
python scripts/validate_repo.py
python scripts/validate_output.py path/to/generated-review.html
python scripts/test_validate_output.py
node scripts/test_runtime.cjs
```

Platform adapters must defer to this file instead of copying its rules. Generated HTML remains releasable only after deterministic validation; an Agent saying it self-checked is not sufficient.

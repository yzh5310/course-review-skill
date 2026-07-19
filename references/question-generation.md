# AI question generation

## Contents

- Product boundary
- Evidence-aware modes
- Prompt context
- Output contract
- Import and trust
- Feedback loop safety

## Product boundary

Generate personal practice material. Do not present the feature as teacher-reviewed item authoring, formal assessment generation, score prediction, or exam forecasting.

The current skill does not implement a teacher review workflow. If educator review is later required, generate a separate Markdown, CSV, or JSON review pack instead of asking a teacher to review the full HTML application.

## Evidence-aware modes

| Evidence level | Allowed generation | Prohibited implication |
|---|---|---|
| `exam-grounded` | Source questions, bounded variations, exam-format practice | That a topic will appear again |
| `course-grounded` | Objective-aligned concept and application practice | That difficulty matches the real exam |
| `generic` | Foundation checks and common disciplinary practice | High-frequency, must-test, predicted, or mock-exam claims |

When evidence is generic, set `diagnosticUse` to `false` for imported AI questions.

## Prompt context

Build the prompt from a compact, previewable summary:

- course, evidence level, and evidence limitations;
- coverage mode and remaining time;
- 1-3 target learning objectives;
- concept-level recent attempts, independent accuracy, hint use, recency, and confirmed misconceptions;
- excluded topics;
- requested count and type mix.

Do not send a single overall accuracy when concept-level evidence exists. Do not label unobserved concepts as weak.

## Output contract

Use `schemas/question.schema.json`. Require:

- `conceptIds` and `learningObjective`;
- `sourceBasis` and `diagnosticUse`;
- `difficulty` and `difficultyReason`;
- `question`, answer, explanation, and hint;
- `suggestedErrorCategory`, never a confirmed category;
- `targetsMemory`, explaining the observed learning need;
- a `selfCheck` object for sufficient conditions, answer recalculation, and uniqueness.

Ask the external AI to generate and then independently solve each question. Self-check reduces risk but is not human review.

## Import and trust

1. Parse JSON without executing content.
2. Validate required fields and type-specific answer rules.
3. Reject topics outside the declared scope.
4. Detect structural duplicates using concept IDs, method, type, and structure in addition to exact text.
5. Store provenance and import time.
6. Put unverified AI questions in a practice-only pool.
7. Provide a visible report-problem action. Reported questions do not affect the learning profile.

## Feedback loop safety

- An AI question cannot alone mark a concept mastered.
- Record an external-AI attempt with `affectsMastery:false`; correctness and selected error categories must not change concept evidence or error-history targeting even after repeated use.
- An AI-suggested error category cannot become confirmed memory automatically.
- Removing an item from the wrongbook must not delete its attempt history.
- Low-confidence questions cannot lock or unlock prerequisites.
- Repeated AI questions must not dominate a concept's evidence.

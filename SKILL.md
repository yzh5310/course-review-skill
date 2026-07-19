---
name: course-review
description: Generate and validate evidence-aware, time-constrained, interactive course review applications for learners with limited preparation time or weak foundations. Use when an AI needs to turn a course name, chapter scope, available materials, exam date, or learner history into a single-file review app, a minimum effective learning path, active-recall practice, or privacy-aware prompts for external AI question generation. Do not use it for score prediction, formal exam authoring, or teacher review workflows.
---

# Course Review Skill v5.1

Build the smallest useful learning loop for the learner's remaining time. Produce a learning application, not a long static document.

## Product promise

Given incomplete evidence, limited time, and a learner's observed history:

1. state what is known and uncertain;
2. generate an evidence-aware coverage path;
3. show one immediate next action;
4. use retrieval practice and feedback;
5. preserve learning events in a canonical profile;
6. generate privacy-aware prompts for optional external AI practice questions.

Never predict a score, promise a pass, call inferred topics high-frequency, or represent AI-generated questions as teacher-reviewed.

## Direct and ultimate users

- Direct user: an AI agent creating or adapting the review application.
- Ultimate user: a learner with weak foundations, exam anxiety, incomplete materials, or roughly 1-3 days to prepare.

Treat teachers and formal item-review workflows as out of scope for this version.

## Core workflow

### 1. Collect only decision-critical input

Ask for or infer, in this order:

1. course name and chapter scope;
2. remaining time and realistic available study time;
3. available evidence: past papers, scope, slides, assignments, textbook chapters, or a topic list;
4. assessment behavior: calculation, explanation, case analysis, code, essay, or mixed;
5. learner history, if an existing application or profile is available;
6. desired coverage mode.

Do not block when materials are absent. Continue conservatively and label uncertainty.

### 2. Classify evidence and choose coverage

Read [references/path-generation.md](references/path-generation.md) before generating the path.

Use one evidence level:

- `exam-grounded`
- `course-grounded`
- `generic`

Use one coverage mode:

- `minimum-core`
- `standard-coverage`
- `extended-improvement`

A target score may inform the user's ambition but must not become a prediction or UI promise.

### 3. Select the course profile

Read [references/course-profiles.md](references/course-profiles.md). Choose the closest assessment behavior and add only modules that support it.

Do not copy quantitative-course structures into law, humanities, language, laboratory, or other unsuitable courses.

### 4. Build the learning path

Rank objectives using evidence-supported relevance, prerequisite leverage, observed need, transfer value, time cost, and uncertainty.

Output:

- an evidence notice;
- a coverage mode notice;
- ordered objectives with reasons;
- a 5-10 minute first action;
- a cutoff rule for running out of time;
- one visible next action at a time.

Do not mark a concept mastered from one answer. Use the mastery states and signals in the path reference.

### 5. Build the application

Read [references/output-contract.md](references/output-contract.md). Adapt `template.html` rather than reconstructing its state and trust boundaries from memory. Default to one self-contained HTML file with progressive enhancement.

Embed and complete `#courseReviewContract` using [schemas/review-plan.schema.json](schemas/review-plan.schema.json). Keep it synchronized with `COURSE_META`, the visible evidence notice, and the immediate next-action card.

Include only the minimum core:

- evidence and uncertainty notice;
- short diagnostic when useful;
- next-action card;
- active-recall practice with feedback;
- minimal wrongbook backed by permanent attempt history;
- concise final review sheet;
- export, import, and reset for the learning profile;
- AI-content disclaimer.

Conditionally enable knowledge graphs, spaced practice, detailed error analytics, knowledge exclusion, AI question generation, Canvas, or complex dashboards.

Read [references/accessibility.md](references/accessibility.md) and [references/implementation-guardrails.md](references/implementation-guardrails.md) before writing UI or code.

### 6. Persist learning memory

Read [references/learning-profile.md](references/learning-profile.md). Use [schemas/learning-profile.schema.json](schemas/learning-profile.schema.json) as the normative shape.

Use the course-prefixed `learning_profile` localStorage key as the canonical state. Record attempts, hint use, recency, concept links, source basis, and user-confirmed error categories.

Treat the wrongbook as a current queue. Resolving a wrongbook item must not erase its historical attempt.

### 7. Generate optional external-AI question prompts

Read [references/question-generation.md](references/question-generation.md) and validate imported objects against [schemas/question.schema.json](schemas/question.schema.json).

Before copying a prompt:

1. summarize only 1-3 target objectives;
2. include evidence limitations;
3. use concept-level history instead of a single overall score;
4. preview what will be shared;
5. exclude personal data and raw wrong questions by default.

Imported AI questions are unverified practice material. They must not alone mark mastery, lock a path, confirm an error cause, or claim exam authenticity.

### 8. Validate

Validate the skill repository:

```bash
python scripts/validate_repo.py
```

Validate every generated HTML artifact before delivery:

```bash
python scripts/validate_output.py path/to/generated-review.html
```

Do not deliver an artifact when the output validator fails. Report the command and pass result with the generated file.

Also open the template in a browser and verify:

- the first useful action is reachable within 60 seconds;
- legacy learning state migrates without deletion;
- attempts persist after refresh;
- prompt preview matches the canonical profile;
- generic evidence produces no exam-frequency or score claims;
- imported AI questions remain practice-only;
- keyboard, reduced-motion, dark, mobile, and print behavior work.

## Mandatory rules

1. Prefer time budget over target score.
2. Separate evidence, inference, and user preference.
3. Do not infer weakness from missing data.
4. Show one next action, not the whole system at once.
5. Keep AI-suggested and user-confirmed error categories separate.
6. Preserve historical attempts when current queues change.
7. Preview data before sending it to an external AI.
8. Keep unverified AI questions out of high-impact path decisions.
9. Provide quiet, encouraging, and sprint feedback modes.
10. Use course-specific learning loops.
11. Embed the generated-output contract and keep it synchronized with visible behavior.
12. Treat `validate_output.py` as a mandatory release gate.

## Acceptance criteria

- Works with no reference material.
- Makes no score or pass guarantee.
- Explains every path priority and uncertainty.
- Starts a useful 5-10 minute task within 60 seconds.
- Uses a versioned canonical learning profile.
- Produces concept-level, privacy-aware question prompts.
- Labels provenance and trust on every imported AI question.
- Does not require teacher review.
- Embeds a valid, synchronized review-plan contract.
- Passes repository validation, generated-output validation, regression tests, and browser smoke checks.

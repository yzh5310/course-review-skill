---
name: course-review
description: Generate and validate evidence-aware, time-constrained, interactive course review applications for learners with limited preparation time or weak foundations. Use when an AI needs to turn a course name, chapter scope, available materials, exam date, or learner history into a single-file review app, a minimum effective learning path, active-recall practice, or privacy-aware external-AI tutoring handoffs. Do not use it for score prediction, formal exam authoring, or teacher review workflows.
---

# Course Review Skill v5.3.1

Build the smallest useful learning loop for the learner's remaining time. Produce a learning application, not a long static document. The product supports attention by reducing choice and shortening actions; it does not diagnose or guarantee attention, learning gains, scores, or passing.

## Product promise

Given incomplete evidence, limited time, and a learner's observed history:

1. state what is known and uncertain;
2. generate an evidence-aware coverage path;
3. show one immediate next action;
4. use retrieval practice and feedback;
5. preserve learning events in a canonical profile;
6. generate previewable prompts for optional external AI tutoring without requiring a return trip.

Never predict a score, promise a pass, call inferred topics high-frequency, or represent AI-generated questions as teacher-reviewed.

## Direct and ultimate users

- Direct user: an AI agent creating or adapting the review application.
- Ultimate user: a learner with weak foundations, exam anxiety, incomplete materials, or roughly 1-3 days to prepare.

Treat teachers and formal item-review workflows as out of scope for this version.

## Core workflow

### 1. Collect only decision-critical input

Read [references/learner-intake.md](references/learner-intake.md) before first-time generation or when the learner's circumstances change.

Treat a learner-provided Chaoxing (学习通) assignment or chapter-quiz link as course material. Before asking questions the page may answer, follow [references/chaoxing-intake.md](references/chaoxing-intake.md) and use the available browser to attempt a read of the student's visible questions regardless of completion status. Visible question stems alone can support course review; access to answers is optional.

If the user supplies only a course name or a broad request, ask up to three short question groups and wait for the reply before generating the HTML:

1. purpose, deadline, and realistic available study time;
2. current preparation, familiar topics, and specific difficulties;
3. chapter scope, assessment tasks, and available course or exam materials.

Ask only for missing information that would change the plan. Reuse explicit answers already in context; do not repeat intake or ask the learner to choose technical coverage modes. Follow up only on consequential ambiguity, then briefly summarize the situation and proceed without a routine second confirmation.

If the user says they do not know, has no materials, declines questions, or explicitly requests immediate generation, continue with visible assumptions and unknowns. Silence is not permission to invent a deadline, time budget, exam scope, or ability level. Do not infer weak foundations from missing information.

### 1a. Evidence source priority (user materials first)

Treat the learner's own materials as the primary and highest-authority source. Never let an external source override or redefine what the learner has actually been given or has actually studied.

Priority order:

1. materials the learner supplied (exercise sheets, the teacher's scope statement, slides, past papers, notes);
2. scope or structure the learner states in conversation (which chapters are in scope, where the class has reached);
3. the named textbook's table of contents, **only if the learner supplied or confirmed the book**;
4. public web search — last resort.

Before searching the web for textbook contents, chapter structure, or scope:

1. ask the learner directly whether they have any other materials (textbook TOC photo, syllabus, teacher's notice, slides) that would settle the question;
2. wait for the answer or an explicit "no, nothing else";
3. only then search, and label anything found as unverified inference unless the learner confirms it.

A book's table of contents can never tell you which chapters the class has reached, nor which chapters the exam covers. Never infer exam scope or learner progress from a textbook's structure. Ask the learner, or read it from material they supplied.

Do not claim to have confirmed the learner's textbook without an identifier they supplied (ISBN, title page, or TOC excerpt).

### 2. Classify evidence and choose coverage

Read [references/path-generation.md](references/path-generation.md) before generating the path.

Use the learner's own teacher's slides, class exercises, and assignments as the primary basis for taught content and practice. When the web lacks a matching course or conflicts with those materials, follow the course materials for scope, notation, and expected methods. Keep outside explanations supplementary and label unsupported scope as unknown.

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

Apply the intake-to-HTML decisions in `references/learner-intake.md`: adapt scope, required workload, explanation depth, practice difficulty, and session length to the actual answers. Personalization must change the learning activities, not just the heading or introductory text. Keep self-reported preparation separate from demonstrated mastery.

When the source is a set of questions, infer the concepts, skills, and prerequisite links before scheduling review. Use representative worked examples and practice with feedback where useful. Generate full item-by-item solutions only when the learner separately requests that output and it is appropriate for the assignment state.

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

### 7. Hand off optional tutoring to an external AI

Read [references/question-generation.md](references/question-generation.md). Default to a conversational handoff: explain a stuck step, repair prerequisites, or practice one question at a time entirely in the external AI. No API, JSON, return trip, or import is required. External activity does not automatically update the HTML profile. Offer structured imports only as an explicit advanced option for capable Agent/file-editing workflows; validate those objects against [schemas/question.schema.json](schemas/question.schema.json).

Before copying a prompt:

1. summarize only 1-3 target objectives;
2. include evidence limitations;
3. use concept-level history instead of a single overall score;
4. preview what will be shared;
5. exclude personal data, unrelated excerpts, and full history; include the current question only in a disclosed contextual handoff that the learner chooses to copy.

Prepare prompts automatically from the current question/selected text or local task. Show a short sharing summary and expandable full preview. Remember the preferred AI and combine copying/opening into one action; do not require retyping the question, selecting its concept, checking a sharing box, or clicking generate and confirm separately. Keep optional controls collapsed. Provide honest clipboard/popup fallbacks and leave paste/send to the learner.

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

- the first useful action is reachable within 60 seconds of opening the generated HTML (this is not a limit on intake);
- legacy learning state migrates without deletion;
- attempts persist after refresh;
- prompt preview matches finite concept-level data in every range and excludes excluded topics;
- explanation/prerequisite/practice handoffs work without JSON or importing a reply;
- a paused learner can resume the last section or question and feedback mode;
- next actions and the knowledge map read the same canonical profile;
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
9. Default to quiet feedback, expose quiet/encouraging/sprint controls, and never auto-open a timed micro-quiz. Offer checks at learner-selected stopping points.
10. Use course-specific learning loops.
11. Embed the generated-output contract and keep it synchronized with visible behavior.
12. Treat `validate_output.py` as a mandatory release gate.
13. Treat Agent instructions as adapters, not enforcement; use the same contract and validator on every platform.

## Acceptance criteria

- Works with no reference material.
- A course-name-only request triggers concise intake before HTML generation, unless the user explicitly skips it.
- The HTML reflects the learner's time, purpose, preparation, and known scope; unconfirmed assumptions remain visible.
- Required task estimates fit the known study budget, with optional work and a clear cutoff when coverage does not fit.
- Makes no score or pass guarantee.
- Explains every path priority and uncertainty.
- Starts a useful 5-10 minute task within 60 seconds of opening the HTML, after intake.
- Uses a versioned canonical learning profile.
- Produces concept-level, privacy-aware tutoring prompts; normal learners finish the session in the external AI.
- Does not claim automatic cross-platform memory or verified attention/score gains.
- Passes `node scripts/test_runtime.cjs` for prompt ranges, history boundaries, and learner-controlled flow.
- Labels provenance and trust on every imported AI question.
- Does not require teacher review.
- Embeds a valid, synchronized review-plan contract.
- Passes repository validation, generated-output validation, regression tests, and browser smoke checks.

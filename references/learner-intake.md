# Learner intake and HTML adaptation

## First conversation

Use existing context and supplied materials first. When only the course name is known, ask about the three groups below and wait for a reply. Explain briefly that the answers change the workload, content, and difficulty. Offer plain-language choices without requiring a long questionnaire.

Example for a Chinese-speaking learner:

> 为了让复习内容、每天任务和难度适合你，先了解三点；不知道的可以直接说不知道：
> 1. 你是准备考试、补基础还是系统重学？什么时候考或希望学完，每天实际能学多久？
> 2. 目前是基本没学、学过但忘了，还是概念懂但不会做题？哪些章节比较熟、哪些最困难？
> 3. 你手头有哪些这门课的资料？老师发的考试范围、复习提纲、课件、习题、往年题或学习通作业链接都可以。有这次考试专用的资料可以优先发。你发过的资料我会先看，再问影响安排的问题。

Omit answered questions and adapt the wording to non-exam purposes. Ask for the course name only if missing. Do not require personal identifiers, grades, diagnoses, or a target score. Do not ask the user to pick a framework, course profile, or internal coverage mode.

If a Chaoxing link is already supplied, attempt to read its visible questions using [chaoxing-intake.md](chaoxing-intake.md). Use readable material before asking the learner to identify chapters or question types. Ask only for material gaps that would change the plan.

Ask a follow-up only if the answer would materially change the output: for example, whether calculus covers single-variable or multivariable topics, or whether “three hours” means per day or in total. Resolve conflicts between the learner's current statement and older records before using the disputed information. Otherwise summarize the confirmed purpose, available time, preparation, scope, and assumptions in a few sentences and generate; the summary is not an approval gate.

## Unknowns and skipping intake

- “No materials” is a complete answer. Do not repeatedly ask for uploads or block delivery; use `generic` evidence where appropriate and state that exam relevance is unknown.
- “I do not know” is also an answer. Keep that field unknown and ask again only if proceeding would be materially misleading.
- An explicit request to skip questions or generate immediately bypasses intake. Show the limits of personalization in the HTML.
- If time is unknown, use an ordered sequence with estimated task durations, not an invented calendar or total time. Keep `coverage.remainingMinutes` null. Label any illustrative schedule as optional and assumed.
- If preparation is unknown, do not call the learner a beginner or weak. Offer a brief optional diagnostic only when its result changes where to start; otherwise provide accessible explanations with optional prerequisite help.
- If scope is unknown, clearly label the common-disciplinary scope as provisional. A known course boundary must not be silently replaced with a broader generic syllabus.
- While awaiting a required reply, inspect available materials if useful, but do not generate a supposedly personalized final HTML from unanswered questions. Elapsed time and silence are not answers.

## Turn answers into learning decisions

| Confirmed situation | Required effect in the HTML |
|---|---|
| Little time and self-reported weak foundations | Reduce required coverage, teach necessary prerequisites, and use short scaffolded tasks; expose what is deferred. |
| Previously studied but forgotten | Use brief retrieval checks to choose review versus relearning; do not repeat all introductory teaching by default. |
| Concepts understood but application difficult | Emphasize worked examples, independent variations, and explanatory feedback on errors. |
| Known chapters and assessment tasks | Match objectives and practice formats to that scope; do not force calculation exercises into essay or language courses. |
| Reliable course or exam materials | Follow the [course source rules](path-generation.md#course-sources-and-conflicts). Use the teacher's materials to shape the actual lessons, examples, and practice, and distinguish source facts from inferred priorities. |
| No course materials | Offer a conservative foundation path and mark scope and exam relevance as unverified. |
| Irregular or short study sessions | Use resumable short tasks with required and optional work rather than an inflexible daily quota. |
| Systematic relearning rather than exam preparation | Organize by prerequisites and understanding; do not impose an invented exam deadline or sprint. |

Self-reports guide initial depth and task selection; they are not proof of mastery or a permanent ability label. Use existing relevant learning records when available, with current corrections taking priority. An optional diagnostic must be short, skippable, and connected to a concrete path decision; one answer cannot establish stable mastery.

Budget required learning, practice, and recap together. Keep their estimated total within the known available time and respect daily/session limits when provided. Estimates are estimates, not guarantees. If the requested scope does not fit, explain the tradeoff, prioritize a useful core, and separate optional extension work; ask the user only when choosing what to omit would override a material stated preference.

If the learner identifies attention as a difficulty, adapt short-session length and interruption behavior without requesting a diagnosis. Avoid adding questions whose answers would not change the plan.

Show a concise, non-blocking “本方案依据” summary in the HTML: purpose, time budget when known, self-reported preparation, known scope/materials, and material assumptions or unknowns. Keep details secondary to the next action. Make unsupported assumptions easy to identify and explain what information would allow revision; do not claim live replanning unless implemented.

Keep this summary consistent with the actual objectives, task durations, explanation depth, examples, practice, cutoff rule, `COURSE_META`, and `courseReviewContract`. Use the existing contract fields for evidence, time, priorities, and uncertainties; do not add undeclared fields to the strict schema. Do not replace an existing learning profile or erase attempts when adapting the plan.

## Behavioral review cases

These are review scenarios, not claims of a completed model evaluation. Evaluate the conversation and resulting activities, not exact wording:

| Input | Expected observable behavior |
|---|---|
| “帮我生成线性代数复习方案。” | Ask concise questions covering the missing groups, then wait; do not deliver HTML yet. |
| “线代，两天，每天一小时，基本没学，只考矩阵和方程组，以计算为主，没有资料。” | Proceed without repeating intake; required task estimates total at most 120 minutes and fit 60-minute days; teach necessary prerequisites and defer unrelated content. |
| Same scope and assessment, but two weeks at one hour daily, previously studied | Use retrieval checks and broader practice/variations appropriate to the 840-minute budget. Activities must differ meaningfully from the two-day beginner case. |
| “不用问，直接生成高数复习页。” | Generate with visible unknown time, preparation, and scope; no invented exam date or confirmed beginner label. |
| “时间还没定，基础不知道，也没有资料。” | Continue without repeated intake; offer a provisional ordered path and optional useful diagnostic, with no fabricated calendar. |
| User has already supplied full details or later corrects one field | Reuse the details, update only affected decisions, preserve history, and do not restart the questionnaire. |
| The teacher's linear algebra slides use row reduction, assignments practice it, and a same-name online course emphasizes Cramer's rule. | Use row reduction and the class's notation in the required path and practice. Only include the outside method as clearly marked optional context if useful. Cite the slides and assignments and keep exam frequency unknown. |

Before delivery, compare the learner summary against the actual required workload, scope, and learning activities. The deterministic output validator checks structural and trust boundaries; passing it alone does not prove that intake occurred or the HTML suits the learner.

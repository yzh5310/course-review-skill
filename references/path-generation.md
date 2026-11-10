# Path generation

## Contents

- Evidence levels
- Course sources and conflicts
- Coverage modes
- Priority model
- Mastery states
- Output contract
- Acceptance checks

## Evidence levels

Classify the available evidence before building a path.

| Level | Available evidence | Allowed claims |
|---|---|---|
| `exam-grounded` | Past papers plus an exam scope, rubric, or reliable format description | Rank topics by observed exam relevance. Do not predict a score. |
| `course-grounded` | This course's slides, class exercises, assignments, assigned textbook scope, or chapter list | Rank topics by course relevance and prerequisite leverage. Do not call topics high-frequency exam topics unless the material says so. |
| `generic` | Course name, a few concepts, or no course material | Build a conservative foundation path from common disciplinary structure. Label all exam relevance as unknown. |

Never invent frequency, marks, pass probability, or a predicted score. Record the evidence level and a short evidence summary in the generated application.

## Course sources and conflicts

- Use the teacher's confirmed exam scope and requirements to decide exam coverage. Use this class's slides and worked examples for taught definitions, notation, and methods, and its assignments, class exercises, and quizzes for representative tasks and solution expectations. A course with no matching online resources can still be course-grounded from these sources.
- When a same-name course, textbook, or web resource differs from this class, use the local teaching materials for the main path, worked examples, practice formats, and feedback. Use compatible external explanations to fill conceptual gaps or offer clearly marked optional enrichment. Keep web-only topics out of required coverage unless the user confirms they belong.
- If materials are partial, use them for the topics they cover and label the rest as provisional. If two local sources materially conflict, prefer the source that explicitly applies to this class and assessment. Ask one focused question if the conflict remains consequential. Flag apparent errors separately from differences in course conventions.
- The visible evidence notice and existing contract fields should identify the course material behind decisions and distinguish supplemental or AI-generated practice. Regular exercises support alignment with the class. Claims about exam relevance still require the applicable evidence level above.

## Coverage modes

Use coverage names instead of score promises.

| Mode | Purpose | Typical content |
|---|---|---|
| `minimum-core` | Establish the smallest useful framework within severe time constraints | Prerequisites with high leverage, core concepts, one representative task per major objective |
| `standard-coverage` | Cover the normal course core | Core concepts, representative tasks, common variations, common errors |
| `extended-improvement` | Extend transfer and integration after the core is stable | Cross-topic problems, less common variations, deeper explanations |

A user may provide a target score as a preference. Treat it as an aspiration only and never as an outcome forecast.

## Priority model

Estimate a relative priority, not a score probability.

```text
priority =
  evidence-supported relevance
  + prerequisite leverage
  + observed learning need
  + transfer value
  + goal alignment
  - time cost
  - uncertainty penalty
```

Apply these rules:

1. Put remaining time and available study time ahead of the requested score.
2. When evidence is weak, lower the relevance term and raise prerequisite leverage, transfer value, and uncertainty penalty.
3. Prefer one topic that unlocks several later topics over an isolated hard topic.
4. Produce a sequence of 5-10 minute next actions. Show one next action prominently; update it using canonical concept evidence and the last local task. Prerequisite hints guide learners without blocking direct chapter access.
5. Recompute priorities after meaningful new evidence, not after every click.
6. Apply [learner-intake.md](learner-intake.md) to make preparation, purpose, scope, and session limits change the actual activities. Fit the estimated required workload, including practice and recap, to the known budget; separate optional extension work. Unknown time must not become an invented deadline or calendar.

## Mastery states

Use multiple signals. One correct micro-question is insufficient for stable mastery.

| State | Meaning | Question policy |
|---|---|---|
| `unseen` | No evidence yet | Use a low-cost diagnostic |
| `learning` | Initial study or mixed evidence | Use scaffolded foundation practice |
| `unstable` | Recent errors or hint dependence | Use close variations and delayed retrieval |
| `provisional` | Recent independent success | Use one delayed confirmation |
| `mastered` | Repeated independent success over time | Use sparse maintenance questions |
| `excluded` | User says it is not examined | Do not generate questions |
| `insufficient-data` | Evidence cannot support a judgment | Do not label it weak or mastered |

Consider first-attempt correctness, hint use, recent results, recency, confidence when available, and performance on a variation.

In the reference implementation, require at least two independent successes separated by 5 minutes for `provisional`, and at least three separated across a 30-minute window for `mastered`. These are minimum guards, not proof of durable long-term retention.

## Output contract

For every generated path, include:

- evidence level and evidence summary;
- coverage mode and remaining study time;
- ordered learning objectives with prerequisite links;
- the reason each objective is prioritized;
- an uncertainty note for inferred topics;
- one immediate next action;
- a cutoff rule explaining what to skip if time runs out.

## Acceptance checks

- A path can be generated with no reference material.
- No path makes score or pass guarantees.
- A user can begin a useful activity within 60 seconds of opening the generated HTML, after intake.
- The actual scope, required workload, explanation depth, and practice reflect the intake answers; a personalized title alone is insufficient.
- The first activity fits in 5-10 minutes.
- Every priority can be explained using stored evidence.
- Low-confidence AI questions cannot alone mark a concept mastered or block a path.

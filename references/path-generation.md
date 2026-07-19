# Path generation

## Contents

- Evidence levels
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
| `course-grounded` | Slides, assignments, textbook scope, or a chapter list | Rank topics by course relevance and prerequisite leverage. Do not call topics high-frequency exam topics unless the material says so. |
| `generic` | Course name, a few concepts, or no course material | Build a conservative foundation path from common disciplinary structure. Label all exam relevance as unknown. |

Never invent frequency, marks, pass probability, or a predicted score. Record the evidence level and a short evidence summary in the generated application.

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
4. Produce a sequence of 5-15 minute next actions. Show one next action prominently.
5. Recompute priorities after meaningful new evidence, not after every click.

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
- A user can begin a useful activity within 60 seconds.
- The first activity fits in 5-10 minutes.
- Every priority can be explained using stored evidence.
- Low-confidence AI questions cannot alone mark a concept mastered or block a path.

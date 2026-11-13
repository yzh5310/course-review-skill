# Generated review output contract

Every generated review application must embed a machine-readable contract in a script element:

```html
<script type="application/json" id="courseReviewContract">
{ ... }
</script>
```

Use `schemas/review-plan.schema.json` as the normative shape. Keep the manifest synchronized with the visible application and its JavaScript configuration.

## Required decisions

The contract must record:

- skill and contract versions;
- course name and stable slug;
- evidence level, evidence summary, and source list;
- coverage mode and remaining study minutes when known;
- ordered objectives with a priority reason, evidence basis, uncertainty note, and prerequisites;
- one immediate 5-10 minute action and a time-cutoff rule;
- canonical learning-memory rules;
- external-AI boundaries, including `defaultWorkflow: "external-dialogue-no-return"` and `externalActivityAutoSynced: false` for v5.3;
- explicit false values for score prediction, pass guarantees, and unsupported frequency claims.

## Synchronization rules

1. The visible evidence notice must agree with the manifest.
2. The initial visible next action must use the same objective ID and duration as the manifest. At runtime, local canonical evidence and the saved task may advance this action; keep its displayed objective consistent with that runtime recommendation.
3. Every knowledge-graph node must have a manifest objective in the same order, and the UI must expose its priority reason and uncertainty.
4. `COURSE_META` must use the same course, evidence level, coverage mode, and remaining time.
5. If external-AI help is enabled, default to conversational tutoring with no required return. Prompt preview, anonymous sharing, and no automatic cross-platform memory are mandatory. Optional structured imports remain practice-only with no concept-evidence impact.
6. Stable mastery must require repeated independent success across a time gap; immediate repeated answers are insufficient.
7. A generic-evidence application must not use high-frequency, must-test, predicted-exam, or mock-exam language.
8. Do not deliver an artifact that fails `python scripts/validate_output.py <artifact.html>`.

## Generation handoff

When another AI adapts the template:

1. copy `template.html` instead of rebuilding its state model from memory;
2. replace the demo course data and the embedded contract together;
3. preserve the canonical profile and external-AI trust boundaries;
4. run the output validator;
5. report the validation command and result with the delivered file.

The validator is a release gate, not optional advice.

## Learner-fit review

Before delivery, also perform the semantic checks in [learner-intake.md](learner-intake.md): the visible learner summary must agree with the real scope, required workload, explanations, and practice. Use the existing evidence summary, remaining time, objective reasons, uncertainty notes, and cutoff fields to reflect those decisions. Keep unknown remaining time null; do not add undeclared contract fields.

For an exam-specific plan, check every active surface against the confirmed scope, including the first task, lessons, diagnostics, quiz bank, formula sheet, and optional tutoring targets. Treat a necessary prerequisite as a brief aid to an in-scope skill. Keep out-of-scope topics out of the exam path. Check that scope uncertainty is visible when the plan is provisional.

Check that labels and counts match the generated material. On a fresh browser profile, use the primary start link to reach the next action and open the lesson. The learner can optionally use the diagnostic and help after starting.

The output validator does not verify the conversation or prove personalization. Report learner-fit review separately from structural validation and do not imply that an automated pass establishes suitability.

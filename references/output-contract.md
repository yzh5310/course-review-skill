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
- external-AI practice boundaries;
- explicit false values for score prediction, pass guarantees, and unsupported frequency claims.

## Synchronization rules

1. The visible evidence notice must agree with the manifest.
2. The visible next action must use the same objective ID and duration as the manifest.
3. Every knowledge-graph node must have a manifest objective in the same order, and the UI must expose its priority reason and uncertainty.
4. `COURSE_META` must use the same course, evidence level, coverage mode, and remaining time.
5. If external-AI generation is enabled, prompt preview, anonymous sharing, practice-only imports, and no concept-evidence impact are mandatory.
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

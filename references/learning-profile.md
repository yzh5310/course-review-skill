# Learning profile

## Contents

- Purpose
- Canonical store
- Concept evidence
- Attempt events
- Migration
- Privacy

## Purpose

Use one versioned learning profile as the canonical memory. Treat the wrongbook as a current work queue, not as the historical record.

Store the profile under the course-prefixed `learning_profile` localStorage key. Keep legacy keys only for migration and backward compatibility.

The normative shape is `schemas/learning-profile.schema.json`.

## Canonical store

The profile contains:

- course and evidence metadata;
- remaining time and coverage preference;
- one record per concept;
- append-only attempt events with a bounded retention limit;
- confirmed error history;
- review schedule and UI preferences.

Do not infer weakness from absence. An untouched concept is `unseen` or `insufficient-data`, not weak.

## Concept evidence

Track at least:

- attempts;
- first-attempt correct count;
- independent correct count;
- hint-use count;
- recent results;
- timestamps for independent successes used to verify delayed retrieval;
- last-practiced time;
- confirmed error-category counts;
- current mastery state;
- the evidence supporting that state.

Prefer concept IDs over chapter names. A question may target one or two primary concepts.

## Attempt events

Record an attempt after the result is known. Include:

- question ID and concept IDs;
- correctness;
- first-attempt flag;
- hint use;
- difficulty and source basis;
- whether the event is eligible to affect mastery;
- timestamp;
- suggested and user-confirmed error categories separately.

AI-suggested error categories must not become confirmed memory without user confirmation or repeated behavioral evidence.

Require a time gap between independent successes before raising mastery state. The reference template uses at least 5 minutes for `provisional` and 30 minutes for `mastered`; never compress three immediate answers into stable mastery.

Set `affectsMastery` to `false` for every external-AI question attempt. Preserve the attempt event and the learner's selected category for transparency, but do not update concept attempts, independent-correct counts, recent results, confirmed concept-error counts, error-history targeting, or mastery state from that event.

## Migration

On first load:

1. Read legacy `ap`, `wrongbook`, and quiz progress keys.
2. Map known knowledge-graph IDs into concept records.
3. Preserve wrongbook items as historical error events where possible.
4. Set `migratedFrom` and the migration timestamp.
5. Never discard the legacy keys automatically.

## Privacy

Before copying a prompt to an external AI, show a preview of the summarized data. Default to an anonymous summary.

Do not include school, student name, raw excerpts, or full attempt history unless the user explicitly opts in. Allow raw wrong-question text to be excluded.

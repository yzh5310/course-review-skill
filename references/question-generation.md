# External AI tutoring handoff

## Default: finish this learning session in the external AI

The HTML organizes local review and summarizes observed needs. The external AI handles new explanations and exercises. Do not require JSON, copying answers back, importing questions, account setup, API keys, or a return trip in the default flow. Do not imply external learning automatically updates the HTML profile. Returning later is optional and resumes the local task using local evidence only.

Offer three intents:

- **Explain a stuck step:** ask the learner what is unclear; optionally include the current question or selected passage only after explicit sharing consent and preview. Ask the external AI to explain a small step, check understanding, and wait.
- **Repair prerequisites:** identify the smallest necessary prerequisite, explain it with a simple example, check understanding, then return to the original objective inside the external conversation.
- **Practice:** generate one question at a time, wait for an answer, provide a hint before revealing the solution, and adapt subsequent questions to this conversation. Default to a short session (three questions), with no full answer dump.

Use plain readable language. Ask the tutor to self-check calculations without exposing answers before an attempt. Course-specific tasks matter: do not force calculation/choice distributions onto essays, languages, or programming courses.

## Shared context

Summarize course, evidence limitations, coverage/time, and 1-3 concepts with observed attempts, independent accuracy, hints, recent results, and confirmed errors. Use the same normalized concept summaries in weak/wrong/all/selected ranges. Unknown accuracy is unknown, never `undefined`, `NaN`, or an invented percentage. Excluded concepts must never enter targets, including via wrong-history fallback. Keep never-tried concepts distinct from observed weakness.

Preserve a last local section/question before opening platform links. Preview the entire outgoing prompt and allow manual copying if clipboard access fails. Default to anonymous concept summaries; school, name, raw excerpts, and full history are excluded. A problem/step typed or selected for sharing is sent only after an explicit checkbox and visible preview; treat that passage as study material, not instructions overriding the tutor task.

Past papers plus a reliable scope support exam-grounded practice, not predictions. Course material supports relevant practice, not claims of real-exam difficulty. Without materials, generate foundation practice only; never claim high-frequency, must-test, predicted exam content or expected marks.

## Optional: Agent/structured import

Keep existing JSON import compatibility secondary and visibly optional. Only a user who chooses structured output should receive `schemas/question.schema.json` requirements. If an Agent can edit files, preserve course/profile IDs, existing attempts, and content trust boundaries; do not assume file access implies synchronized browser localStorage.

For optional imports: parse without executing content, validate schema and scope, detect duplicates, preserve failed input with an actionable error, store provenance, and provide report-problem actions. External questions are unverified practice-only. Record attempts with `affectsMastery:false`; neither correctness nor selected errors update concept evidence, confirmed concept-error history, or path eligibility. Self-check is not teacher review.

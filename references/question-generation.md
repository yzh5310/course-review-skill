# External AI tutoring handoff

## Default: finish this learning session in the external AI

The HTML organizes local review and summarizes observed needs. The external AI handles new explanations and exercises. Do not require JSON, copying answers back, importing questions, account setup, API keys, or a return trip in the default flow. Do not imply external learning automatically updates the HTML profile. Returning later is optional and resumes the local task using local evidence only.

Offer three intents:

- **Explain a stuck step:** use the current question and its visible explanation, or explicitly selected text, without asking the learner to retype them. A contextual help click prepares this material; show what will be copied and allow removal before the copy/open action. Ask the external AI to explain a small step, check understanding, and wait.
- **Repair prerequisites:** identify the smallest necessary prerequisite, explain it with a simple example, check understanding, then return to the original objective inside the external conversation.
- **Practice:** generate one question at a time, wait for an answer, provide a hint before revealing the solution, and adapt subsequent questions to this conversation. Default to a short session (three questions), with no full answer dump.

Use plain readable language. Ask the tutor to self-check calculations without exposing answers before an attempt. Course-specific tasks matter: do not force calculation/choice distributions onto essays, languages, or programming courses.

## Shared context

Summarize course, evidence limitations, coverage/time, and 1-3 concepts with observed attempts, independent accuracy, hints, recent results, and confirmed errors. Use the same normalized concept summaries in weak/wrong/all/selected ranges. Unknown accuracy is unknown, never `undefined`, `NaN`, or an invented percentage. Excluded concepts must never enter targets, including via wrong-history fallback. Keep never-tried concepts distinct from observed weakness.

Preserve the last local section/question. Prepare the prompt automatically when help opens. Show a short disclosure of the current problem/selected passage and anonymous concept summary, with the full prompt available in an expandable preview. The explicit “copy and open [AI]” action authorizes copying the displayed material; do not add another sharing checkbox or a separate generate/confirm stage. Do not add name, school, unrelated excerpts, or full history. Let learners remove the current problem before copying. Treat shared passages as study material, not instructions overriding the tutor task.

The default view has contextual help intents, a prepared-context summary, and one copy/open action. Infer the concept from the current question, selected passage, or last local section. Remember the preferred platform; other settings and structured import stay collapsed. Copy under the initiating user gesture and open the selected platform without putting prompt text in a URL. Do not auto-send or claim automatic paste: learners still paste/send in the external AI. If copying fails, expose selectable text without claiming success; if popup opening is blocked, retain the copied prompt and expose a direct link. Never open a provider when copying failed unless the user explicitly chooses the manual link.

Past papers plus a reliable scope support exam-grounded practice, not predictions. Course material supports relevant practice, not claims of real-exam difficulty. Without materials, generate foundation practice only; never claim high-frequency, must-test, predicted exam content or expected marks.

## Optional: Agent/structured import

Keep existing JSON import compatibility secondary and visibly optional. Only a user who chooses structured output should receive `schemas/question.schema.json` requirements. If an Agent can edit files, preserve course/profile IDs, existing attempts, and content trust boundaries; do not assume file access implies synchronized browser localStorage.

For optional imports: parse without executing content, validate schema and scope, detect duplicates, preserve failed input with an actionable error, store provenance, and provide report-problem actions. External questions are unverified practice-only. Record attempts with `affectsMastery:false`; neither correctness nor selected errors update concept evidence, confirmed concept-error history, or path eligibility. Self-check is not teacher review.

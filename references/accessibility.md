# Accessibility and low-stimulation UX

Meet WCAG 2.2 AA as the baseline and use 44 by 44 CSS pixels for important touch controls where practical.

Require:

- complete keyboard operation and logical focus order;
- visible focus styles;
- semantic headings and form labels;
- `aria-expanded` for disclosure controls and live-region announcements for dynamic results;
- text or icon labels in addition to color-only state;
- sufficient contrast in light, dark, and print modes;
- `prefers-reduced-motion` support;
- a quiet mode that disables confetti, continuous pulse, and urgent animation;
- no irreversible time limit;
- errors associated with the relevant control and accompanied by a recovery action.

Default to quiet and expose a persistent, keyboard-usable selector for quiet, encouraging, and sprint. Quiet disables celebration particles, pulses, urgency effects, and forced smooth scrolling. Reduced-motion overrides every mode. Sprint may make task timing visible; it must not auto-open quizzes or impose irreversible time pressure.

At the end of a short section, offer “check understanding”, “continue reading”, and “ask for help”. Checks start only on learner action and can be postponed or dismissed. Never interrupt reading after a fixed number of seconds. Restore the last local objective/section/question without erasing attempts. Next-action recommendations must update from the canonical profile; prerequisite hints are guidance, not hard locks. Small-screen users must be able to tap or keyboard-focus term explanations as well as hover them.

Validate with real generated output: time-to-first-action, pause/resume, stuck-step help, external handoff without import, mobile/keyboard operation, and whether feedback itself distracts. Report usage observations without diagnosing attention or claiming measured gains when none were measured.

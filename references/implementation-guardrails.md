# Implementation guardrails

## Architecture

- Produce one self-contained HTML file unless the user requests another form.
- Keep the core useful without a network connection. Treat CDN rendering as progressive enhancement.
- Prefix localStorage keys with the course slug and wrap access in `try/catch`.
- Use `learning_profile` as the canonical state and migrate legacy keys without deleting them.
- Keep modules isolated and expose only deliberate public methods.

## Content safety

- Label material as source, derived, or generic.
- Never claim an inferred topic is high-frequency or guaranteed to appear.
- Keep AI-imported questions practice-only until independently verified.
- Escape imported text before inserting it into HTML.
- Do not use `innerHTML` with untrusted question content.

## Interaction

- Show one prominent next action computed from the canonical profile and resume context.
- Let the learner start from that action on first open. Use inline guidance and keep settings optional.
- Never schedule a micro-quiz popup on a reading timer.
- Default to quiet feedback; expose all feedback modes and honor reduced motion.
- Default external help to one-question-at-a-time dialogue; structured import is opt-in.
- Keep the first useful task under 10 minutes.
- Respect reduced motion and quiet mode.
- Preserve attempt history when wrongbook items are resolved.
- Allow users to export, import, and reset their profile.
- Every state a control gains by script (`selected`, `pressed`, `active`, `flipped`, `known`, `correct`, marking a choice) must have a visibly distinct style. A control whose state changes with no visible difference reads as broken and users stop trying. Before delivery, diff the computed style of one control before and after clicking it, in light and dark mode, desktop and mobile.
- For choices, also expose progress in words ("3 / 8 answered"), so state is legible even at a glance and for users who cannot rely on colour.

## Validation

- Validate `SKILL.md` frontmatter.
- Validate JSON files and example objects against their schemas.
- Parse every inline script in the template.
- Check that all local references from `SKILL.md` exist.
- Search for legacy score-promise labels and document intentional compatibility uses.
- Embed `#courseReviewContract` and keep it synchronized with the visible artifact.
- Run `python scripts/validate_output.py <generated.html>` for every generated application.
- Escape `<` and `>` inside inline math in the HTML source (`&lt;`, `&gt;`). A raw `<` followed by a letter is parsed as a tag opener and silently truncates the formula, so `$P(a<X<b)$` renders as the literal text `$P(a`. After rendering, assert that no visible text still contains a `$` delimiter and that no `.katex-error` nodes exist.
- Do not deliver, publish, or describe an artifact as complete when output validation fails.

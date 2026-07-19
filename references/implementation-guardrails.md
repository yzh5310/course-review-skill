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

- Show one prominent next action.
- Keep the first useful task under 10 minutes.
- Respect reduced motion and quiet mode.
- Preserve attempt history when wrongbook items are resolved.
- Allow users to export, import, and reset their profile.

## Validation

- Validate `SKILL.md` frontmatter.
- Validate JSON files and example objects against their schemas.
- Parse every inline script in the template.
- Check that all local references from `SKILL.md` exist.
- Search for legacy score-promise labels and document intentional compatibility uses.
- Embed `#courseReviewContract` and keep it synchronized with the visible artifact.
- Run `python scripts/validate_output.py <generated.html>` for every generated application.
- Do not deliver, publish, or describe an artifact as complete when output validation fails.

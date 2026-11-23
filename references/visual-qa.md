# Visual and interaction QA

Run this before delivery. `validate_output.py` checks structure and trust boundaries; it cannot see a control that does nothing, a formula cut in half, or a tooltip hidden behind a card. Every item below is a defect class that has shipped in a real generated app.

## When to run

After `validate_output.py` passes, on the final HTML, in a real browser (Playwright or manual). Repeat on desktop (≈1280×900) and mobile (≈390×844), light and dark, with the accordions open, because most defects only appear once content becomes visible.

## Automated checks

Any of these can run as `page.evaluate` after the page loads:

**1. A control's state must change visibly.** Compute styles before and after the click; if nothing differs, the learner will read it as broken.

```js
const snap = () => getComputedStyle(document.querySelector('.diag-opt')).cssText;
```

Use `backgroundColor`, `borderColor`, `color`, `fontWeight`, `transform`, `opacity`, plus `className`. A class added without a matching CSS rule is the most common cause.

**2. Nothing covers an interactive control.** Hit-test its centre.

```js
const r = el.getBoundingClientRect();
const top = document.elementFromPoint(r.left + r.width / 2, r.top + r.height / 2);
return top === el || el.contains(top);
```

Run it on choices, submit buttons, accordion headers, flip cards, nav links, and checkboxes. A transformed 3D card or an unpositioned popover is the usual culprit; `overflow: hidden` on the card fixes the former.

**3. No formula is left unrendered.**

```js
// visible text still holding a delimiter means KaTeX never matched it
[...document.querySelectorAll('.katex-error')].length === 0
&& !/\$/.test(document.body.innerText)
```

A raw `<` inside `$...$` is parsed as a tag and silently truncates the formula, leaving `$P(a` on the page. Escape `<` and `>` as `&lt;` and `&gt;` inside math spans in the HTML source.

**4. A canvas is actually drawn and correctly sized.**

```js
const d = ctx.getImageData(0, 0, canvas.width, canvas.height).data;
let painted = 0; for (let i = 3; i < d.length; i += 4) if (d[i]) painted++;
painted > 0 && Math.abs(canvas.width - canvas.getBoundingClientRect().width) < 4
```

A canvas inside a collapsed accordion measures 0 wide at load; redraw on open and on resize, and set the CSS width to 100% before measuring.

**5. A tooltip stays inside the viewport.** Hover a term, then check `rect.left >= 0 && rect.right <= innerWidth` and the same vertically, including terms near an edge and the last term before the fold. `position: fixed` plus script clamping is required; absolute positioning inside a card gets clipped by ancestor `overflow`.

**6. Every hover affordance tells the truth.** A dashed underline and a help cursor must produce a definition. Terms without one should not look interactive.

## Source-fidelity checks

The same discipline applies to claims about the learner's materials:

- Never write "all N problems are type X" without enumerating them. In one course, 4 of 10 problems in a set gave the distribution function while 6 gave the density; one template did not fit both.
- Never state a count ("30 problems") that you have not recounted.
- Do not use score-adjacent phrasing ("背下来就能拿分"); prefer "照套即可". No score prediction, no pass guarantee, no exam-frequency claim.

## Manual checks

- First useful action reachable within about a minute, and it is the visible next action.
- Keyboard: Tab to every control, Enter/Space activates, focus ring visible.
- Dark mode: text and annotations remain readable; annotations on coloured headers inherit the header colour instead of staying on their own colour.
- Print: navigation and floating controls hidden, content not clipped.
- Reload: attempts, answers, and position restored without duplicated counts.

## Failure → cause → fix

| Symptom | Cause | Fix |
|---|---|---|
| Clicking a choice does nothing | state class has no CSS rule | add a selected style with a checkmark, and a text counter |
| Unselected options unreadable in dark mode | `<button>` missing explicit `color: var(--text)` | set `color: var(--text)` on `.diag-opt` and `.qb-opt` |
| Formula shows `$P(a` | raw `<` inside math | escape to `&lt;` in the source |
| LaTeX `\times`, `\bmod`, `\ne`, `\text` vanish | generator script used non-raw string literal | use raw strings (`r"""..."""`) in build scripts and verify in DOM |
| Tooltip clipped at a card edge | absolute positioning inside `overflow` | `position: fixed` + clamp in script |
| Tooltip stuck at `(0, 0)` on keyboard focus or tap | positioning script only listened to `mouseover` | bind `focusin`, `focusout`, `click`, and `Escape` in the same delegated handler |
| Tooltip covers content after scroll | stale position | hide on scroll and resize |
| `minimum-core` plan flips to `standard` on load | depth selector defaulted to hardcoded `'standard'` | derive default depth from `COURSE_META.coverageMode` |
| Chart blank | canvas measured while collapsed | measure inside `draw()`, redraw on accordion open and resize |
| Grey blurred block reads as broken | mask also blurred its hint | draw the hint outside the blurred element |
| Annotated word disappears | term colour equals header background | inherit colour on coloured surfaces |
| Layout jumps to 4+1 cards | grid `minmax` too small | raise the minimum so the row balances |
| Student ID or email leaks into source list | raw lab filename or slide header copied verbatim | sanitize source labels to neutral titles before writing HTML |

# Independent responsive route capture review

Inspected all nine boards in routes-v2: 1440/820/390 × top/middle/end, covering eleven inner/error routes. Inspected both rebuild-mobile boards and enlarged contact-us-820-top, auto-glass-repair-390-end, guides-390-middle and auto-glass-replacement-1440-top. These are captures of the pre-final-fix revision; parent reports subsequent tablet-grid and orbit/contrast repairs. Those repairs are not certified by these older frames.

## Additional findings

- **P2 — Desktop replacement illustration is cropped and enlarged too far.** The original exploded-car diagram is a portrait illustration. In the 1440px opening its cover-filled wide frame cuts the top/bottom and makes the remaining cabin/glazing visibly soft. Use a contained diagram or a designed opaque backing within the wide composition; this does not require new generation.
- **P2 — Mobile footer controls are too small for comfortable touch.** Full-size repair390end shows footer route pills approximately 28px high and contact/review/motion links approximately one 17px text line. Increase the hit area, particularly for adjacent review/reduce controls. Main-page buttons are much better spaced.
- **P2 — Initial phone homepage provides no scroll cue.** The supplied first phone frame shows the static car image and header while staged copy is hidden. CSS hides `.hero-copy .cue` on phones. Retain a visible mobile scroll affordance without changing the approved staged text progression.
- **P2 — Reduced proof rail still clips later commitments.** Current source sets proof q=0 in reduced mode, leaving a wide track at its beginning within an overflow-hidden section. Normal scroll travel has been repaired, but reduced/no-JS modes still need wrapping or native horizontal access. This is a source follow-up, not a finding derived from the normal-mode screenshots.
- **P3 — Header overlaps legible content in scrolled phone states.** The unbacked fixed logo visibly crosses the “How do I get a quote?” row in repair390end and the Information card in guides390middle. A subtle settled header backing and appropriate anchor/focus offset would improve separation. This is a visual reading issue, not a claim that the FAQ is unreachable.

The known tablet detail/Information overflow appears in the old boards; parent reports minmax/grid/type fixes after capture, so it requires fresh verification rather than duplicate diagnosis. The previously reported orbit overlap and white assembly title also appear in old phone frames; they are not evidence against the newer fixes.

## Scope and result

Apart from the known tablet overflow, no new route-level missing content, broken layout or horizontally clipped main prose was apparent in these samples. Contact card email fits at 820px; phone quote/tracking controls remain visible before optional embeds; phone detail metadata fits and footer routes are present. Large whitespace in boards is the montage layout, not a website defect. Form submission, expanded FAQs, menu scrolling, focus order, real touch behavior and moving transitions are not established by these boards. This review makes no claim of exact Windsor fidelity or publication acceptance.

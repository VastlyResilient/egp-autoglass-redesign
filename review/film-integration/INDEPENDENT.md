# Independent integration review — pending responsive evidence

Scope: local integration at `http://127.0.0.1:4213/index.html`, source `windsor.js`/`windsor.css`, and primary agent browser captures. No publication or owner acceptance is implied.

The independent reviewer's CUA browser inventory was empty. Binding browser `2`/tab `23` and opening `iab` both failed as unavailable. Consequently this is independent screenshot/source inspection, not an independent interactive browser run. The primary agent supplies browser interaction evidence separately.

Inspected valid captures: desktop-end.png and current phone-start.png, phone-middle.png, phone-end.png, phone-reverse.png. Initial phone-named files were desktop 1280x720 captures; this was flagged and the primary agent recaptured a 390px iframe. Current responsive captures include the test harness outside the site frame.

No pane/technician cropping or headline/action overlap is visible in the valid end captures. Phone preserves the full landscape frame above facts and copy. Reverse capture shows the raised pane and earlier headline staging. This demonstrates sampled state differences, not continuous motion quality.

Remaining findings:
- Phone opening reserves approximately 219px for film at 390px wide and leaves roughly 480px of dark space below it. This preserves composition but makes hand/contact detail small and the opening markedly less immersive than desktop. Owner judgment is needed on the visual tradeoff; do not claim identical cinematic impact.
- Desktop logo has weak contrast over the workshop; phone's light backing is clearer. Consistent backing would improve desktop branding.
- At the time of inspection, phone-menu.png did not show an open menu; phone-reduced.png showed the footer; short-phone-end.png showed FAQ/orbit. These files do not establish their named hero/menu states. Tablet, short-phone hero, reduced hero, and menu evidence remain pending.

Source observations: the canvas uses the same 192-frame progression on both widths, selects lower-resolution mobile images, keeps a bounded cache and three concurrent requests, and retains the poster if frames cannot load. Reduced mode skips canvas loading and exposes the HTML beats. These source properties are not substitutes for simulated failure, interaction, or hardware testing.

Gate status: no blocking layout defect in the valid inspected states, but the requested responsive/menu/reduced-motion integration review is incomplete. No hardware iOS, network-failure, complete moving-sequence, deployed revision, or owner-acceptance claim.

## Final captured-state gate

PASS for the inspected integration layouts and fallback appearance, with the scope limits below. The pending-state paragraph above records an intermediate evidence failure, now corrected; it is not the final status.

Subsequently inspected corrected `short-phone-end.png`, `phone-menu.png`, `phone-reduced.png`, plus `tablet-start.png`, `tablet-end.png` and `media-fallback.png`. The primary agent reports actual iframe sizes of 390×844, 390×600 and 820×1180; some harness screenshots display the iframe at 70% scale. These are real browser responsive iframe captures, not physical-device tests.

Short-phone film end fits the complete film, three facts, headline and both actions. Reduced hero exposes the poster and all text/actions without overlap. Open menu shows the close control and route links; the motion control is below the visible area, so its reachability is a primary-agent interaction claim, not established by that still. Tablet start/end preserve the full scene with letterboxing; facts and headline/actions do not collide. Large dark areas remain a composition tradeoff on portrait screens. The new pale logo backing is visible in tablet and fallback captures and resolves the earlier contrast finding.

The media-fallback screenshot shows a valid poster. Primary agent separately reports `poster-fallback` canvas status and all six text beat opacities equal to 1 with the animation script removed. Those runtime results were reported to this reviewer, not independently executed here. Primary agent also reports desktop forward/reverse frame progression (126, 191, then 38 at its tested scroll positions).

No remaining concrete blocking crop, overlap, or hidden-action defect was found in these captured states. Continuous scroll smoothness, physical touch, hardware iOS, keyboard menu operation, exact network failure behavior and post-promotion/deployed assets were not independently verified. Tablet intermediate/reverse states were not captured in the inspected set. This is a bounded independent visual/source review, not a whole-site regression signoff, private-reference fidelity assertion, owner acceptance, or deployment authorization.

# Windsor rebuild — independent source review

Scope: current windsor.js, windsor.css, rebuild.py and all 12 generated route HTML files. No rendered fidelity judgment in this pass. Earlier generated-film approval/review is superseded by the owner's rejection; current rebuild has no active film renderer.

## Findings needing repair or verification

1. **P1 — Short-screen navigation can become unreachable.** The mobile menu contains ten route links plus motion control and 110px vertical padding, but `.menu` has no viewport max-height or vertical scrolling. Its fixed positioning can place lower controls beyond short-phone/landscape viewports while main/footer are inert. Bound it to the viewport with scrolling and verify the last item is keyboard/touch reachable.
2. **P2 — Most mobile commitment cards cannot be seen.** Four 290px cards plus three 24px gaps create a 1232px proof track. At 390px viewport with 20px gutters, approximately 882px of travel is needed to reveal the final card. Current transform is limited to 180px and the parent clips overflow. On a phone the later cards cannot be fully reached. Calculate actual overflow or supply native horizontal scrolling/stacking, including reduced/no-JS modes.
3. **P2 — Invisible orbit CTA remains interactive.** `.orbit-copy` has opacity zero until its late scroll reveal, but its button explicitly has pointer-events:auto and remains tabbable. Orbit thumbnail links similarly remain focusable while positioned outside the clipped pin. Gate interactive visibility with inert and restore it at the visible hold, or ensure keyboard navigation intentionally exposes the focused item.
4. **P2 — Hero image uses lazy loading.** Shared `img()` gives the above-the-fold homepage image `loading=lazy`. It should be eager with appropriate fetch priority; otherwise the initial image-only opening can stay blank longer under load.
5. **P2 verification — Short landscape / minimum heights.** Hero min-height is 650px desktop / 700px mobile; other pins min-height650px. There is no short-landscape override. On a 390px-high landscape screen the bottom-anchored message/CTAs can remain outside the visible portion of the pinned region. Check a real short viewport and provide an intentional layout that keeps semantic copy and useful controls reachable without silently changing the approved normal-viewport staging.
6. **P3 copy — Internal assurance leaks into customer heading.** “Straightforward information. No invented promises.” describes the authoring process and introduces an unprompted doubt. Replace with a customer-relevant heading while retaining factual commitments and qualification notes.

## Route and semantic checks

All 12 routes (home, services, information, about, replacement, repair, insurance, quote, tracking, contact, privacy, 404) have exactly one h1 and one main. Every local href destination resolves. Main/footer are made inert while the menu opens; Escape closes and focus returns to the toggle. Form inputs have labels and relevant types; the email-draft behavior is accurately described. Quote/tracking expose external/call options before optional embeds. Source is a static-image scroll composition; no paid-film replacement is currently integrated.

Desktop navigation provides About, Services, Information and Contact; there is no visible desktop menu toggle. Remaining routes remain reachable through page links and footer. This is not a broken route but should be checked against the chosen reference and owner navigation requirement.

## Motion math and failure-path limitations

Hero uses one normalized scroll value; all six beats finish by p=.77 and retain an end hold. Mobile assembly's four entries finish by p=.75; preceding cards exit at subsequent .2 boundaries, leaving intentional periods with no fully active card during transitions. Verify readable holds and reverse behavior in motion. Horizontal travel is computed from actual track width, while proof travel is not. Failed JS preserves most text/cards with the noscript override; orbit is intentionally hidden. Manual reduced motion retains all hero text and stacks cards, but the proof travel limitation remains. Review reduced orbit and short-height pin layout in-browser.

This pass does not certify reference fidelity, geographic factual evidence, full interaction behavior or deployed acceptance. Compare the upcoming rendered captures to the measured reference and then run the targeted states above.

# Independent mobile motion parity audit

Status: source audit complete; independent rendered review pending primary-agent captures. No full parity pass yet. Scope is the 12 root HTML routes, windsor.css and windsor.js. Uses cinematic-company-websites/references/mobile-motion-parity.md requirements. Browser connection unavailable in this reviewer session; do not attribute primary-agent interactions to this reviewer.

## Concrete findings to repair or verify

1. **Reduced ticker loses locations.** Global reduced mode removes the animation but leaves `.ticker-row` at max-content width inside overflow:hidden. Only the first few towns can be seen; there is no static wrap or horizontal browsing. The duplicate sequence should not become duplicated visible content in the repaired static layout.
2. **Ticker has hover-only pause.** Its children are plain nonfocusable spans and the only pause rule is `.ticker:hover`. A touchscreen/keyboard visitor lacks an equivalent local pause/resume action. Global reduced mode is available but currently loses content as above. Provide a discoverable control or suitable equivalent; verify timed advancement stops and resumes.
3. **Reduced orbit retains clipping geometry.** It unpins but preserves absolute ring tiles, radius175 on phones, rotated70×90 tiles and overflow:hidden. At390px width some tile edges exceed the viewport; at320px the loss is greater. With the ring frozen at its final state, there is no scrolling choreography to reveal the missing portions. Use a complete static presentation for the explicit alternative, and capture all eight links plus central CTA.
4. **No-JavaScript proof rail hides cards.** The noscript rules fix assembly/horizontal scenes but not proof-track. On index/about, the max-content row remains clipped in its overflow:hidden parent and cannot travel. Match the complete reduced static proof presentation.
5. **Small assembly action targets.** `Explore service` links remain13px text without minimum target height; mobile card paragraphs grow but action hit area does not. Verify actual rectangles and make the touch action comfortable without losing card content.

Potential focus gap requiring interaction evidence: orbit marks only fully offscreen tiles inert; partly clipped tiles remain keyboard-focusable, with no focus handler to bring their full bounds into view. Assembly links can become inert as the user scrolls a focused card out. Test focus during/reversing motion and ensure the focused action remains visible/reachable; source alone cannot establish a failure in every state.

## Animation-family inventory

| Family | Routes | Normal mobile source | Explicit reduced/source fallback | Required browser evidence |
| --- | --- | --- | --- | --- |
| 192-frame film + six HTML beats | index | Same scroll progress; mobile-resolution frames, fullscreen left crop | Poster and all beats | Cold load, early/mid/end, fast/reverse, pause, resize, failed media |
| General opacity/vertical text reveal | All12 | Same viewport-derived reveal calculation | Full opacity/no transform | Stop mid reveal, reverse, headings/body readable, direct anchors |
| Time-based town ticker | index | Same34s loop, smaller tiles | Animation stops but content clipped | Pause/touch/focus; complete static towns |
| Globe rotation and tagged reveals | index | Same canvas rotation with smaller geometry | Rotation variable0; tags reveal fully | Time advances while scroll stopped, explicit reduction freezes, restored motion resumes |
| Four-card assembly | index, services | Same entry transforms; sequential opacity exit makes phone stack navigable | Unpinned static cards onphone | Everycard entry/hold/exit, reverse, eachlink click/focus, short landscape |
| Horizontal feature rail + image expansion/color change | index | Same scroll travel/fill; viewport-size cards | Wrapped static cards, full fills | All four cards, no cutoff copy, stopped/reverse scroll |
| Proof rail translation | index, about-us | Same measured travel | Reduced wrap; no-JS currently incomplete | All four proofs normal/reduced/no-JS |
| Orbit expansion/spin/background interpolation/CTA | index | Same arc/curl/spin with smaller radius/tiles | Frozen final ring, currently potential clipping | Initial/arc/ring/CTA, reverse, all8links and focused bounds |
| Project image hover zoom | index, services, repair, replacement, insurance | Hover remains; keyboard focus-visible equivalent | CSS transition/zoom not disabled | Touch equivalent/document decorative difference; no hidden content |
| Button hover lift/color, focus outline, nav underline | All12 | Hover plus button focus-visible; native taps navigate | Small transitions remain | Tap destinations, keyboard focus, no sticky-hover obstruction |
| Menu open/close/focus/body lock | All12 | Phone-only control; scrollable overlay | Same control | Short landscape, lastlink/motioncontrol, Escape, Tab/ShiftTab, resize whileopen |
| FAQ/provider disclosures | All except about, privacy,404 | Native details, no JS-dependent reveal of body | Same native details | Touch/keyboard open/close, provider actionable |
| Contact feedback | contact-us | mailto draft + status | Same | Validinput, status and actualdestination; no silent send |

## Route coverage from source

All12 routes include windsor.js, semantic reveal nodes, and two motion preference buttons (menu/footer).

- index:21 general reveals; hero, assembly, horizontal, proof, orbit scenes; ticker and globe;5 details.
- about-us:12 reveals; proof scene.
- services:10 reveals; assembly scene;5 details.
- auto-glass-repair and auto-glass-replacement:11 reveals each;5 details each.
- insurance-claims:12 reveals;5 details.
- guides:9 reveals;5 details.
- contact-us:8 reveals;5 details and contact form.
- instant-quote and order-status:8 reveals each;6 details each including provider disclosure.
- privacy and404:2 reveals each.

No normal-mobile breakpoint entirely disables a major animation family in this source snapshot. That is an inventory result, not proof of rendered parity. Film cache/failed-frame handling, saved explicit motion choice, default OS preference handling and static poster exist. The globe has no local pause control; the global explicit reduced-motion choice freezes its rotation, which should be checked for discoverability/restoration. Reduced CSS suppresses keyframes, but small hover transitions remain; assess whether they are acceptable intentional reduced behavior.

Final acceptance requires captures and interaction results for all families, the reported repairs, short landscape, focus, and deployed revision. Responsive iframe testing must be distinguished from physical-device testing.

## Repair review — intermediate, not final acceptance

Source repairs now add explicit ambient pause controls, a reduced ticker with only the first15 unique towns wrapping, a labeled two-column reduced orbit grid, no-JS proof/ticker wrapping,44px assembly links, touch-active project/button effects, and dark feature cards with white text. These address the original source findings in design intent.

Independently inspected assembly-first/fourth, horizontal-middle-fixed, globe-paused, orbit-middle, original orbit-end, orbit-end-fixed and orbit-reduced screenshots. Assembly copy and actions fit in the portrait captures. Feature text is readable during image expansion. Reduced orbit visibly contains all8 labeled links. Globe capture visibly offers Resume ambient motion; actual phase pause remains primary-agent runtime evidence.

**Remaining blocker:** orbit-end-fixed reduces the radius enough to fit tiles onscreen but the upper diagonal tiles now collide with the central headline. Phone320 is tighter still. Preserve the animation but reserve genuine text clearance, for example by placing the revealed copy below the ring in narrow layouts. Recheck320/390 and short landscape.

Parsed primary-agent JSON results (not independently executed): phone390 and844×390 landscape each list12routes,114fullyrevealed nodes, no pageoverflow; phone320 lists12routes and114fullyrevealed nodes but index overflow:true. This requires investigation. These metrics do not prove child/control bounds, visual contrast, or moving/focus accessibility.

Focus requirement remains open: partly clipped orbit links are focusable and no focus-reveal handler is present. Verify keyboard focus in the early arc/intermediate states, not just the final ring. The new44px assembly targets also need short-landscape visual check within the fixed215px card height.

## Final independent captured-state/source gate

**PASS for the repaired states inspected, with the explicit evidence limits below.** The earlier blocker paragraphs document intermediate failures and are superseded by these repair results.

Viewed `orbit320-final.png`, `orbit-landscape-final.png` and `assembly-landscape-final.png`. Narrow-phone orbit text and CTA now sit below the ring with clear separation. Landscape places the copy beside the ring; it no longer collides with the images. All four landscape assembly cards, body copy and service actions fit in the captured viewport. The previously inspected reduced orbit grid exposes all eight labeled links; the reduced ticker wraps the fifteen unique towns into readable rows. No remaining material crop, overlap, or hidden-action defect was found in these captured repaired layouts.

The updated phone320.json reports320×568, all12routes with overflow:false,114reveal nodes at opacity1. Earlier phone390.json and landscape.json likewise reported114visible reveal nodes and no route overflow. These are primary-agent browser audit outputs independently parsed here, not tests executed by this reviewer. They establish the recorded measurements, not universal device correctness or complete visual coverage of every route/state.

Source confirmation: narrow globe width is bounded by its container; normal orbit radius is responsive; reduced orbit uses a static grid; explicit ambient pause controls exist; no-JS proof/ticker static wrapping exists; assembly links have44px minimum height. Orbit links now become inert unless their full bounds are within the viewport with5px margin, addressing the earlier partially clipped focus-entry concern. Actual keyboard navigation while scrolling a focused element remains an interaction limit; no independent claim of focus-retention behavior is made.

The normal mobile implementations retain film scrubbing, staged text, general reveals, ticker, globe, assembly entry/exit, feature rail/image fill, proof travel and orbit choreography. Geometry changes, explicit reduced alternatives and touch-active equivalents are documented in the source/inventory. The independent source/capture review found no remaining missing normal-mobile animation family. It did not directly observe all moving sequences.

Limits retained: screenshots came from the primary agent's real-browser iframe harness, not physical phones. This reviewer had no usable CUA browser binding. No independently observed continuous playback, touch hardware, every keyboard journey, no-JS rendered proof capture, all intermediate states at every width, live resize/orientation sequence, or deployed verification is claimed. Publication verification and owner acceptance are separate. Do not convert this bounded pass into a claim that every animation is permanently correct on every mobile device.

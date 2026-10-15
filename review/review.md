# Independent rendered QA — EGP Windsor preview

Scope: inspected all 18 supplied mobile opening/middle PNGs for nine inner/error routes and desktop-repair.png / desktop-services.png. Reviewed relevant HTML, CSS and app.js. No live browser interaction or moving sequence observed by this reviewer. Homepage film remains an explicitly incomplete preview; this review is not publication acceptance.

## Findings

1. **P1 — Quote and order tracking lack visible working provider UI.** mobile-instant-quote-middle.png and mobile-order-status-middle.png show large entirely white embed regions. The quote region consumes almost a full phone viewport. Both fallback actions exist but follow the blank region; a visitor can mistake this for a broken page. Show external-service and call options before the embed, add a visible persistent explanation, and verify provider loading and external destination on an actual device. Frames establish a blank captured state, not the cause or permanent provider failure.
2. **P2 — Insurance assistance CTA reloads its current page.** insurance-claims.html contains “Explore insurance assistance” linking to insurance-claims.html. It appears in mobile-insurance-claims-middle.png. Replace with a useful next step, such as the contact page or an anchored insurance-specific process.
3. **P2 — Operating-system reduced-motion preference is not honored.** app.js initializes reduced solely from localStorage; style.css has no prefers-reduced-motion rule. Manual menu preference is useful but does not satisfy automatic support for an existing accessibility preference. Initialize from matchMedia when no saved explicit choice exists, then verify simplified mobile cards and visible text.
4. **P2 — Entry text is visibly low contrast in several captured intermediate states.** The insurance title near the bottom of mobile-insurance-claims.png and footer headings in contact/order/404 frames are substantially faded. Source maps scroll position directly to text opacity, so a user who stops at that position keeps faded text. Verify readable contrast while content is on screen; consider movement or clipping while maintaining readable text opacity.

## Positive observations and limits

At the captured 390px width, all reviewed main headings and paragraph columns fit without evident horizontal clipping. The common header keeps quote/menu controls visible, and the service process rows and contact inputs have comfortable spacing. Repair desktop composition and image crop are coherent. The contact form accurately says that it prepares an email draft rather than submitting remotely.

The desktop services capture is at a boundary state with card headings above the viewport/header; it cannot establish whether the held cards or transitions work. Footer email fits at 390px but is close enough to the edge to warrant a 320px/360px check. Tablet, complete desktop route coverage, full footer captures, keyboard/menu/form behavior, external providers, slow/fast/reverse scrolling, touch, JavaScript failure, media failure, and full motion must be verified by the parent browser pass. No claim of cinematic/mobile motion parity or exact Windsor fidelity is made from these frames.

## Follow-up review after repairs

Inspected mobile-quote-fixed.png and updated quote, order, insurance and JavaScript source. The quote screenshot now shows immediate call/external-service actions and a collapsed optional embed; the large default blank region is removed. Source confirms the same arrangement for order tracking. Provider operation itself remains unverified. The insurance CTA now reads “Talk to EGP” and points to contact-us.html, resolving the self-link.

The general reveal now completes within the bottom 12% of the viewport. The updated quote footer heading is fully readable in the new frame. This narrows the faded-entry interval; previous intermediate insurance/footer states have not all been recaptured by this reviewer.

Parent supplied owner context: full mobile motion by default plus a deliberate manual reduction control was explicitly requested. Therefore the earlier system-preference finding is an intentional owner tradeoff, not an undisclosed implementation defect. The current site still does not automatically honor the operating-system preference; this remains accurately documented here without recommending silent alteration of the approved behavior.

Menu source now makes main/footer inert while open. Interaction remains to be verified in-browser. The added noscript fallback has a concrete selector typo: `.services-pin` does not match the actual `.service-pin`, so its intended unpinning/auto-height rules do not apply. Correct this and verify a mobile JavaScript-disabled capture. This is the remaining concrete source defect identified in this follow-up.

## Desktop and tablet opening review

Independently inspected newly supplied desktop openings: home hero, repair, about, contact, quote, insurance, order, privacy and 404; and all ten tablet opening captures including replacement. Also inspected mobile-hero.png and mobile-services.png. Desktop replacement opening was not present as a separate capture in this directory at review time; tablet and mobile replacement are reviewed.

No new horizontal overflow, heading collisions or illegible main-content layout found in these desktop/tablet opening frames. Tablet repair's tighter image crop retains the repair mechanism and visible damage. Tablet replacement preserves its full exploded-car illustration. Quote/order actions are visible ahead of the optional provider disclosure on desktop and tablet. Contact labels, fields and draft explanation fit in the tablet two-column arrangement. Insurance's corrected “Talk to EGP” CTA is visible in the tablet frame.

Verified the noscript selector is now `.service-pin`, resolving the source typo. This source check does not establish the actual JavaScript-disabled rendered outcome.

The homepage tablet frame is an initial image-only staged state with menu and scroll cue; desktop hero is a later text-visible state. These captures are different scroll states and therefore cannot establish matching motion behavior. Both explicitly disclose “Film production pending · visual preview.” No final-film approval or cinematic-motion parity is claimed. Faint entry text still exists at the lowest edge of some desktop captures, consistent with the narrowed reveal interval; content higher in the viewport is readable.

This expanded review supports handing over a clearly identified visual preview. It does not replace final-film generation/approval, moving-sequence comparison, provider testing or whole-site deployed regression acceptance. Earlier findings and repairs remain preserved above as an audit trail.

Additional captured-state caution: mobile-services.png shows a faint outgoing replacement card behind the incoming repair card; the repair card and link are also partially faded. This is an intermediate transition frame, not a verified hold state. Check that each service receives a fully opaque, usable hold and that fast/reverse scrolling does not leave a visitor unable to choose a service. Mobile hero’s reviewed text-visible state fits its title and two CTAs within the viewport.

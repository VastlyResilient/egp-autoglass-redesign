# Independent phone-startup source review

Status: **actual-phone failure remains unconfirmed and unresolved by this review.** Reviewed the local diff from8f38d4d for windsor.js/CSS and all12 generated route references. This is source review, not physical-device reproduction. Prior iframe parity results do not contradict the owner's report that no animations work on their phone.

## Finding requiring repair

The new reduced-mode notice is fixed at bottom16px across the viewport with z-index34 and no dismiss action. It can cover the reduced hero's actions and other content at the bottom of the screen. A user intentionally retaining reduced motion must enable full motion to remove it. Provide a dismissal that preserves reduced mode, or place the notice in flow; verify short-phone actions and footer remain reachable. The notice is outside the main/footer inert regions, so consider its focus behavior while the menu is open as well.

## What these changes establish

- A recognized `?motion=full` or `?motion=reduced` parameter overrides the saved choice and OS-derived initial value, attempts to persist it, and exposes the chosen mode in the root data attribute.
- The motion buttons set the URL parameter before navigation, so the explicit current-page choice can work even when storage writes are denied. Cross-route persistence still depends on working localStorage because normal links do not propagate the parameter.
- All12 HTML routes reference CSS/JS version10, reducing ordinary stale asset reuse once the new HTML is received.
- All11 svh declarations now have preceding vh equivalents, giving a fallback when svh is unsupported. This is targeted compatibility work, not proof that viewport units caused the owner's failure. Other modern features, including menu dvh, remain.
- pageshow calls renderMotion directly. The scroll listener schedules renderMotion through requestAnimationFrame; it is NOT an independent synchronous fallback if animation frames are unavailable/suspended. On a working RAF loop it adds another render pass during scrolling, which may add work but is not a demonstrated blocker.
- Scheduling the next RAF before rendering prevents a rendering exception from permanently ending scheduling. It does not remove the exception or guarantee completion of the affected render pass.

## Causal limits / next evidence

A saved or OS-derived reduced choice is one plausible cause, not the established cause. A missing/blocked/failed script, runtime exception, stale page, browser limitation or device-specific scheduling problem would not be diagnosed by this patch alone. The override and notice themselves require JavaScript to initialize; they cannot repair a script that never executes. If storage is blocked, switching to a different route can return to the OS preference despite a successful current-page override. A BFCache-restored page also retains its captured reduce variable; pageshow currently repaints without re-reading a preference changed on another page.

Recovery UI browser tests should distinguish: stored-reduced + explicitfull; OS-reduced + explicitfull; explicitreduced; deniedstorage currentpage versus crossroute; back/forward restore; directload of version10; and actual frame/scene advancement after scrolling. Record the affected phone's browser/version, selected mode, script execution/error state and changing frame/progress if obtainable. Until the owner's device reproduces recovery, describe this as a targeted startup/recovery change with browser evidence, not 'mobile animations fixed.'

## Final bounded source verdict

PASS for the reviewed recovery implementation after repair; actual-phone failure remains unresolved. All12routes now offer “Keep reduced motion.” Its handler hides the notice without changing the selected motion mode, so the earlier forced-choice obstruction is addressed. The primary agent reports browser confirmation of hidden notice with mode still reduced; this reviewer verified the handler/source rather than executing that interaction. The redundant scroll-triggered RAF pass has been removed; the normal RAF loop and direct pageshow repaint remain.

Primary agent reports the390px twelve-route audit passed reveal and overflow checks. No new material source blocker was found in this narrow change. The earlier causal limits still apply: no physical-phone reproduction, no proven cause, and no claim that URL override repairs missing script execution. Cross-route behavior with denied storage and stale BFCache preference state remain limits, not demonstrated causes of the owner's report. Describe the delivered work as a tested recovery option and compatibility changes pending confirmation on the affected phone.

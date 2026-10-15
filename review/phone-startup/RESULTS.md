# Phone startup investigation

The owner reports that all animation is absent on their phone. The device/browser and its motion preference have not yet been supplied. This report does not claim the actual phone failure is reproduced or resolved.

Confirmed code path: system prefers-reduced-motion or saved egp-reduce=true disables the film and every scroll scene. Previously, the only indication/recovery was buried in menu/footer controls. Reproduced reduced state in browser, then clicked the new visible Enable full motion control: html[data-motion-mode] became full and film[data-status] became ready. Explicit ?motion=full persists the selected mode across routes; ?motion=reduced and the original controls retain accessible reduced motion.

Added vh fallbacks before svh scene heights for older engines. Re-synchronize on pageshow for restored browser pages. Assets bumped to v10. The provided full-motion link is a diagnostic/recovery route, not evidence about the owner's device.

Physical phone confirmation remains outstanding. Prior responsive tests are not sufficient to close this issue by themselves.

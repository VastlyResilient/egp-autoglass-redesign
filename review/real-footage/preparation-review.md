# Independent preparation-script review

Scope: static review of scripts/prepare-film.py and the recorded rejected-input test. Python syntax parsed successfully without executing the preparation workflow. No accepted video was processed and no site asset was changed.

## Finding

**P2 — The claimed separation from live assets is not enforced.** `--output` may be any non-existing path. If `assets/film` is absent, passing it as the output directly creates the live film directory despite the help text and completion message claiming the website remains unchanged. Resolving the output path and rejecting destinations inside the live assets tree (or requiring a dedicated staging root outside it) would make that guarantee true. Existing-directory rejection protects current files but does not protect an absent live destination. This matters because a deliberately disabled film directory may be absent.

## Otherwise

The rejected-status, exact source hash, required pass checks and evidence-file checks execute before staging output. The old hardcoded rejected clip is gone. Both viewport sequences use the same 24fps extraction and their nonzero counts are compared. Work is built inside a temporary directory and renamed into the requested new destination only after successful conversion, so a failed ffmpeg/Pillow stage does not publish partial output. Manifest duration comes from ffprobe and records the reviewed source hash.

No additional material conversion defect found for the intended short, single-video-stream clip workflow. Relative clip/evidence paths currently resolve against the command working directory, not the review file; use absolute paths in review records or document/change that convention to prevent avoidable rejected runs. The existing rejected-input test supports the failure gate only; successful conversion was intentionally not exercised.

Result: **one staging-boundary fix recommended before treating “live website unchanged” as an unconditional guarantee.** The normal explicitly external staging workflow is otherwise reviewable.

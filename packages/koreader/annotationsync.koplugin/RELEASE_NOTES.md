# v2.1.0 · 2026-10-21

# AnnotationSync v2.1.0

A new public API that lets other plugins sync their data through
AnnotationSync, plus smoother, non-blocking reading progress sync.

## ✨ New Features

- **Extractor API (`pushExtractorData`)** — other KOReader plugins can
  now push their own data (as keyed records) through AnnotationSync and
  get it safely merged across devices via the new **Keyed Merge**.
  Extractors can hook the new `AnnotationSyncRequested` event to sync
  alongside every annotation sync. See
  [Writing an Extractor](https://github.com/dani84bs/AnnotationSync.koplugin/blob/main/docs/writing-an-extractor.md).
- **Sync in background** — reading progress is now pushed from a
  separate process, so page turns no longer stall while syncing. On by
  default on Linux devices (Kobo, Kindle, PocketBook, desktop Linux);
  off by default on macOS and Android. Available with WebDAV or Dropbox
  destinations, and can be toggled in the progress sync settings.

## 🐛 Fixes

- Input used to interrupt a background progress sync is now passed
  through to the reader instead of being swallowed (#100).
- Background progress push times out on elapsed time rather than poll
  count, and the push process no longer holds the reader's listeners
  (#107, #108).
- Extractor sync is skipped when offline, and persistent merge conflicts
  are bounded by retries instead of looping.

## 🏗️ Under the Hood

- New end-to-end regression test for background progress push, and unit
  tests driving the real subprocess poll.
- Extra debug logging around provider sync boundaries.

## 📖 Docs

- README documents the **Sync in background** setting.
- New guide: **Writing an Extractor**.
- Updated the minimum KOReader version needed for some features.

## 🙏 Thanks

Thanks to @Tsukumi233 and @JeffShih-wiwynn for their contributions to
this release!

---

**Full Changelog**: https://github.com/dani84bs/AnnotationSync.koplugin/compare/v2.0.0...v2.1.0

# v2.0.0 · 2026-08-18

# AnnotationSync v2.0.0 🎉

The biggest release yet — new sync capabilities, a major internal
refactor, a hardened end-to-end test suite, and a new translation.

## ✨ New Features

- **Full Library Sync** — scan your entire library for books with
  annotations that were never synced (not just the currently dirty
  ones) and sync them all in one pass.
- **Device Purging** — remove a stale or retired device's entries from
  reading progress sync, with a one-click undo.

## 🌍 Localization

- Added **Simplified Chinese (zh_CN)** translation.
- Refreshed and completed existing translations.

## 🐛 Fixes

- Fixed a WebDAV `sync_server` reference bug that could corrupt state
  when handed to the storage provider.
- Bounded retries on persistent sync conflicts to prevent runaway
  loops.
- No-op resyncs no longer trigger a broadcast, keeping sync idempotent.
- Settings exclusion filters are now enforced at the push boundary.

## 🏗️ Under the Hood

- Major refactor of the sync orchestration: extracted dedicated modules
  for settings sync, the changed-documents queue, UI suppression, and
  provider adaptation — smaller, more testable, more maintainable code.
- A sprawling new **real-WebDAV end-to-end test harness** covering
  two-device sync, progress sync, merge conflicts, bookmark restore,
  highlight resizing, the pending queue, network reconnects, and more —
  dozens of new scenarios guarding against regressions.
- CI bumped to KOReader v2026.07.2.

## 📖 Docs

- README now documents Full Library Sync and Device Purging.
- Added a from-scratch guide for setting up a KOReader dev environment.

---

**Full Changelog**: https://github.com/dani84bs/AnnotationSync.koplugin/compare/v1.9.9999...v2.0.0

# v1.9.9999 · 2026-07-25

## v1.9.9999

  ### Fixes
  - Stop false-positive same-page deletions in annotation sync — highlights sharing a page could be wrongly marked deleted; the scan now uses fine-grained position ranges instead of page numbers.
  (#87)
  - Eliminate O(n²) scan in annotation sync — syncing books with hundreds of annotations could take up to ~20 minutes; the scan is now linear. (#69)

  ### Features
  - Make plugin menu location configurable, with a new Menu location settings submenu.
  - Add user-defined directory exclude list for automatic progress sync (manual push/pull unaffected).

  ### Other
  - Test suite hardening (real XPointers in bookmark deletion tests, flushed nested sync schedules in integration tests) — no user-facing changes.

# v1.9.99 · 2026-06-30

**Full Changelog**: https://github.com/dani84bs/AnnotationSync.koplugin/compare/v1.9.9...v1.9.99

# v1.9.9 · 2026-06-19

## What's Changed
* Feature/progress name by @dani84bs in https://github.com/dani84bs/AnnotationSync.koplugin/pull/64
* Feature/settings sync by @dani84bs in https://github.com/dani84bs/AnnotationSync.koplugin/pull/65
* feat: show currently selected cloud in settings menu by @dani84bs in https://github.com/dani84bs/AnnotationSync.koplugin/pull/66
* perf(restore): batch restoration to optimize performance by @dani84bs in https://github.com/dani84bs/AnnotationSync.koplugin/pull/69
* feat(i18n): add dynamic localization support and Italian translations by @dani84bs in https://github.com/dani84bs/AnnotationSync.koplugin/pull/70
* Add Hungarian translation by @koma52 in https://github.com/dani84bs/AnnotationSync.koplugin/pull/71
* fix: handle asynchronous cloud storage sync outside books by @dani84bs in https://github.com/dani84bs/AnnotationSync.koplugin/pull/75
* Feature/progress action by @dani84bs in https://github.com/dani84bs/AnnotationSync.koplugin/pull/77

## New Contributors
* @koma52 made their first contribution in https://github.com/dani84bs/AnnotationSync.koplugin/pull/71

**Full Changelog**: https://github.com/dani84bs/AnnotationSync.koplugin/compare/v1.1.1...v1.9.9

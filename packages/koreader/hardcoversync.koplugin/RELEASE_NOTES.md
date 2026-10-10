# v1.7.0 · 2026-10-09

## Your library now lives on your device

Until now, most screens downloaded everything again each time they opened, even when nothing had changed, and lists didn't work offline at all. From 1.7.0 the plugin keeps your **lists, shelves, books, their details and covers** on the device. It asks Hardcover only **what changed**, and anything that hasn't changed opens from the device with no download at all.

This release is everything from the four 1.7.0 betas.

### What's new

- **Every list and every shelf is kept on your device**, including lists you follow and ones you've never opened.
  - Home checks them all inside the requests it was already making, and downloads only what changed.
  - A changed shelf or list downloads only which books it holds, plus any books the device doesn't have yet. Finishing a book no longer reloads your whole Read shelf.
  - Moving, rating or removing a book updates the saved shelf straight away.
- **Everything works offline:** shelves, lists, Stats, and every book on your shelves and lists with its **full synopsis**. The old saved shelves kept only the first 600 characters.
- **Book details open instantly.** A book you've opened before, that's out and complete, opens with no loading screen and no request for the book. The series is kept for a week and works offline. Books not out yet are checked again once a week.
- **Stats and For you** reload only when something they depend on changed, or once a week.
- **Sharper, smaller covers.**
  - Covers now come from Hardcover's image service at the size they're shown, instead of as uploaded. A cover uploaded at **1.9 MB** now arrives as **30 KB** in a list.
  - A book's details page gets its cover at exactly the size of its box, at higher JPEG quality.
  - Covers are drawn with e-ink dithering, so photos no longer turn into flat bands.
- **Settings › Download covers for offline** keeps the cover of every book on your shelves and lists, so offline shelves aren't a wall of blank boxes.
  - It tells you how many covers and roughly how much before it starts.
  - It shows progress with a **Stop** button and keeps the device awake while it runs. Running it again picks up where it stopped.
- **Refresh** in a shelf's or list's menu, and a reload icon on a book's details page, download them again in full if anything looks out of date.
- **A fresher look:** rounded pill buttons, bold serif headings and figures, and solid progress bars.

### Measured on a real account (9 lists, 4 shelves, 758 books)

| | 1.6.3 | 1.7.0 |
|---|---|---|
| Opening a shelf or list that hasn't changed | the whole thing, every time | **no request** |
| Read shelf (611 books) after one book changed | 840 KB in 7 requests | **51 KB, 1 request** |
| A 25-book list that gained one book | ~32 KB | **~3 KB** |
| Reopening a book you've opened before | 4 requests, loading screen | **no request for the book** |
| A cover in a list | up to 1.9 MB | **30 KB** |
| Checking everything for changes | — | one request, ~1 KB |
| Offline | shelves only, synopses cut short | **lists, shelves, details, covers you've kept** |

### Good to know

- **Updating is automatic.** The first Home open after updating saves your whole library in the background. That was about 1.1 MB in under half a minute on the account above. After that, only changes are downloaded.
- **Your saved shelves carry over** from 1.6.3 the first time Home or a shelf opens.
- **Storage:** everything is kept in a small database, `hardcoversync_library.sqlite3` in KOReader's settings folder, using the SQLite KOReader already ships. The library above takes 1.5 MB. Covers you've seen get 30 MB of space, and covers you download for offline are kept separately. Signing out clears the library.
- **Known:** reordering a ranked list on hardcover.app may not show up on the device until you tap Refresh.

---

## What's Changed
* theme.lua: pill buttons, serif headings, solid black progress bars, hatching and icon helpers by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/51
* Bundle plugin icons by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/52
* Lists kept on the device: offline, and downloaded only when they change by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/53
* Shelves, book details and covers kept on the device (stacked on #53) by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/57
* Release 1.7.0 by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/60


**Full Changelog**: https://github.com/CaptainCamin/HardcoverSync.koplugin/compare/1.6.3...v1.7.0

# 1.6.3 · 2026-10-06

## What's Changed
* Split DialogManager: pure loaders and decision modules for Home, Shelf, Lists and Goals by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/40
* Keep open screens in a registry and remove the unused done_callback by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/41
* Fix Scheduler:clear(), which cancelled no retry loops by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/42
* Give the three offline queues a shared base by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/43
* Extract the book details flows from DialogManager by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/44
* Make charts' atan2 work on Lua 5.3+ as well as LuaJIT by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/45
* API layer: generate async wrappers, move the UI and HTTP out of hardcover_api by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/46
* Fix stale emulator reviews scenario (spoiler is on page 2) by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/47
* Bring 1.6.3-beta.3 into main: update-check fixes and changelog by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/48
* Order hardcover_api.lua by area, async wrappers last by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/49
* Release 1.6.3 by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/50


**Full Changelog**: https://github.com/CaptainCamin/HardcoverSync.koplugin/compare/v1.6.2...1.6.3

# v1.6.2 · 2026-10-05

## What's Changed
* 1.6.2: Home goals fix, wifi switch-off delay, shared detail query fields, one text helper by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/39


**Full Changelog**: https://github.com/CaptainCamin/HardcoverSync.koplugin/compare/v1.6.1...v1.6.2

# v1.6.1 · 2026-10-05

## What's Changed
* 1.6.1: more book details, ratings breakdown on Reviews, fix for books without an edition by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/38


**Full Changelog**: https://github.com/CaptainCamin/HardcoverSync.koplugin/compare/v1.6.0...v1.6.1

# v1.6.0 · 2026-10-04

## What's Changed
* 1.6.0: Stats, and what readers say on a book's details by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/37


**Full Changelog**: https://github.com/CaptainCamin/HardcoverSync.koplugin/compare/v1.5.0...v1.6.0

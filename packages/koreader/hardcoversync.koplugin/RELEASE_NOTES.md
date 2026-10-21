# v2.1.0 · 2026-10-21

Bulk linking is the big change in this release: link every book on your device in one go, and get guesses for books that don't match exactly.

✨ **New**
Link all books on this device, 25 at a time (#149). Details and shelves are saved afterwards (#153).
Guess unmatched books from title and author, then review the guesses before they're applied (#154)
Hardcover details button in the file dialog (#142)
Goal and stats cards for Bookshelf micro-modules (#151)
Set a page by hand on a book set to Reading while offline (#145)
New UI components: button sizes, a round button and a floating action button (#157, #158)
🐛 **Fixes**
Progress is now sent to the read Hardcover already has (#147)
Book details no longer does the cover work twice or runs full refreshes when it opens (#141)
Lists now page correctly while covers are loading (#155, #159)
"Add to lists" changes are applied when you press Done (#160)
🛠 **For developers**
Install from branch: new developer option (#143)


## What's Changed
* Run the emulator scenarios in CI by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/140
* Hardcover details button in the file dialog by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/142
* Install from branch (developer option) by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/143
* Book details: fix doubled cover work and full refreshes on open by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/141
* Emulator: un-park the two offline scenarios by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/144
* Add a nightly live check against the real Hardcover API by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/146
* Send progress to the read Hardcover already has by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/147
* Allow setting a page by hand on a book set to Reading offline by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/145
* Emulator: fix the last three parked scenarios by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/148
* Link all books on this device, 25 at a time by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/149
* Tests: one shared check helper, totals in run_all, a spec README by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/150
* Lint with luacheck in CI by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/152
* Save details and shelves after "Link all books" by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/153
* Hardcover goal and stats cards for Bookshelf micro-modules by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/151
* Snackbar passthrough and list paging while covers load (for testing together) by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/159
* Fix lists not paging while covers load by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/155
* Button sizes and a round button by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/157
* Apply Add to lists changes when Done is pressed by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/160
* Guess unmatched books from title and author, and review the guesses by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/154
* Floating action button component by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/158


**Full Changelog**: https://github.com/CaptainCamin/HardcoverSync.koplugin/compare/v2.0.0...v2.1.0

# v2.0.0 · 2026-10-13

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
* theme.lua: pill buttons, serif headings, solid black progress bars, hatching and icon helpers by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/51
* Bundle plugin icons by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/52
* Beta 1.7.0-beta.1: lists kept on the device by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/54
* Beta 1.7.0-beta.2: shelves, book details and covers kept on the device by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/56
* Fix list covers drawn too small or spilling out of their row by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/58
* Sharper covers: details at their exact size and quality 90, all covers dithered by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/59
* Lists kept on the device: offline, and downloaded only when they change by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/53
* Shelves, book details and covers kept on the device (stacked on #53) by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/57
* Release 1.7.0 by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/60
* Sync beta with main after 1.7.0 by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/61
* Stats: a genres donut, a Pace line for a year, and a range for book length by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/73
* MMD design overhaul on the beta, nav bar indicator at the bottom by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/74
* Scroll control on every long screen by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/62
* Design tokens: secondary text setting, dotted rule, MMD metrics by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/63
* Ship Lato and install it into KOReader's fonts folder by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/65
* Merge main into beta after the 2.0.0 betas by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/75
* Merge beta into main (move to trunk-based) by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/76
* Hardcover shelves and lists as Bookshelf sources by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/78
* Scroll control: rounded track, inset bar by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/79
* Setting to choose the book search plugin by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/80
* Shelf and list changes work offline by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/83
* Settings: grouped options with folding headings by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/81
* Reader sheet: Change status; radios for single choices in Settings by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/82
* Publish any tag containing beta as a pre-release by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/84
* Number betas automatically when a beta is typed without one by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/85
* Bookshelf sources: make sorting work by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/89
* Leave Finished and Did not finish books alone at the end of a book by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/90
* Archive goals from the goal screen, offline too by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/86
* Bookshelf: cheaper shelf sorting on slow devices by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/92
* Reading a Want to Read or unshelved book puts it on Currently Reading by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/93
* Answer user actions with the snackbar by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/97
* No grey for unavailable buttons and rules by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/101
* MMD search field for Home and search results by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/103
* One MMD chip for goal and shelf state by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/105
* Docs: which MMD components are used, and why the rest are not by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/107
* docs: Home shows one reading card by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/100
* No goals reads the same saved or fresh by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/99
* Drop Bookshelf's shelves only when a book's status really changes by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/98
* Shape shelf rows only for the page on screen by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/102
* Home's Sync now works in every language by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/94
* A tab that fails to load says so instead of loading for good by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/95
* Sync opens the pending changes; Home's sync box opens them too by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/87
* Shelf counts on Home and Shelves follow a moved book by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/96
* Bookshelf: open a saved shelf without decoding every book by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/108
* Bookshelf: open a saved list without decoding every book by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/109
* perf_screens: reader panel fixture and budget match the real sheet by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/112
* Stretch shelf rows to fill the page by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/111
* perf_home: allow 4 full-panel refreshes on the cold open by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/115
* Emulator scenarios: skip the snackbar when finding the top window by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/114
* book_rating scenario: hold the dialog the call returns, skip unnamed windows by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/117
* Reader panel: where the book is and how far, Read again beside it by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/110
* Ask before starting to track a book that is not Currently Reading by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/113
* Emulator: wipe the screen between scenario cases by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/118
* Search results: flash the panel as they appear so covers do not ghost on Home by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/119
* Scroll bar: hold the up or down triangle to jump to the start or end by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/120
* Book and edition pickers on the shelf screen by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/121
* Change a linked book's edition from the reader panel by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/122
* One Add button replaces Shelf and Lists on the book details screen by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/123
* Edition button on the book details screen by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/124
* Reader panel: look the book up in the saved shelves by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/126
* Reader status changes update the saved shelves by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/127
* Fix Edition button crash on the book details screen by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/128
* Remove the old Home screen by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/129
* Book details: use the full width when the page does not scroll by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/131
* Open the home screen with a full refresh by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/130
* Home: fit the Read shelf on a small screen by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/125
* Fix offline Currently Reading shelf after cancel and for uncached books by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/133
* Open every full-screen screen with a full refresh by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/134
* Release 2.0.0 by @CaptainCamin in https://github.com/CaptainCamin/HardcoverSync.koplugin/pull/132


**Full Changelog**: https://github.com/CaptainCamin/HardcoverSync.koplugin/compare/v1.6.2...v2.0.0

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

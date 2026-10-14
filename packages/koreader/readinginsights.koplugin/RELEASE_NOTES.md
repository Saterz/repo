# v7.9.0 · 2026-10-14

### Changed

- Book info: tap the stars to open the rating popup (long press still works).
- Ratings changed outside the plugin (e.g. in the file manager) now show up in Book info and the book lists right away instead of after the cache expires. Book info reads the rating straight from the book's own sidecar when its file is known.
- Opening Book info or a book list no longer restarts the slow sidecar-folder scan, which could take seconds on an e-ink reader.
- Rating a book from a list now writes to the book's own sidecar when its file is known, so the file manager and status page agree. The old plugin-only override no longer shadows it.
- Rating a book from a list now shows a message when the rating couldn't be saved, instead of showing stars that were never stored. Save failures are also written to the log.
- Rating popup rebuilt on KOReader's ButtonDialog, so it matches the plugin's other popups.
- Ratings changed outside the plugin (e.g. in the file manager) now show up right away in Book info when the book's file is known, because it reads the rating straight from the book's own sidecar. Book lists pick such changes up when the short rating cache expires.
- Menu: "Progress bars" renamed to "Progress bar" (all translations updated).

# v7.8.9 · 2026-10-14

### Changed 
Removed the progress bar from the "This chapter" row in the Book progress popup. 
_Note: That row shows the time left rather than a percentage, so a bar under it looked out of place. The bar is now only shown under the book's read percentage._

# v7.8.8 · 2026-10-14

### Changed 
In the Book progress popup, the "This book" section now shows the read percentage row first again, with its progress bar directly under the percentage (inside that cell only, matching the chapter bar), This makes it more consistent across the plugin.

# v7.8.7 · 2026-10-14

### Changed

- In the Last 7 days comparison row (pages view), when a long value leaves no room for the full labels, both cells switch to shorter ones (“pg vs prev. 7d” / “daily avg pg”) instead of wrapping onto two lines.
Added: short label translations for all languages (en, hu, fr, de, pt_PT, uk, zh_CN).

# v7.8.6 · 2026-10-14

### Fixed

- The “vs previous 7 days” row in Last 7 days now respects KOReader’s duration format (classic / modern / letters) and the “long durations as days” option.

### Changed

- The time label is now “time vs prev. 7d” (translated in all languages). It automatically falls back to the shorter “vs prev. 7d” when a long value leaves no room for it.
- With the “letters” duration format, the monthly reading time chart shows compact labels in the 12-month single-row layout: decimal hours (1.9h / 1,9h) from one hour up, minutes (45m) below that. The 2×6 layout keeps the full duration.

# v.7.9.4 · 2026-10-15

### Changed

- Ratings file cache: star ratings are cached in reading_insights_ratings_cache.lua. A rebuild only re-opens sidecars that changed (checked by modification time and size), so book lists open faster after a restart or after closing a book.
- Sidecar scan persisted: the sidecar-folder scan result is saved too and no longer repeated on every restart.
- Reload data: the insights title-bar reload now wipes the ratings cache completely. The “Mark book finished” list’s “Reload data” refreshes ratings from the cache.
- Faster finished-books list: books ticked as finished by hand are looked up individually (and cached) instead of re-querying the whole year.
- No more “Loading ratings…” popup when opening book lists.

# v7.9.3 · 2026-10-15

### Changed

- Settings menu reorganized into General, Date & time, Appearance and one group per view.
- Book progress options grouped into Chapters, This book and Pace; bar chart heights moved next to their views.

# v7.9.2 · 2026-10-14

### Fixes

- Book info popup opens faster.
- Rating lists load faster and refresh less often.
- Ratings are never saved to the wrong book.

# v7.9.1 · 2026-10-14

### Changed
- Faster Book info from lists: no more library-wide file search for books
  without a sidecar; books are matched by checksum, then by title and author
  among the known sidecar books. The sidecar scan is cached for one hour.

### Fixed
- The "Reading insight popup" settings order: the "Last 7 days" options
  are grouped together again.

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

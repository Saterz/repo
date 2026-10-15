# v8.0.0 · 2026-10-15

## Changes

**Sleep screen**
- New Sleep screen settings: you can choose what is shown (Reading insights, heatmap, streak, Book progress, Book progress calendar, Book info, Records), the background (book cover, follow theme, or your own image / random from a folder) and the image fit (Fit, Stretch, Zoom).
- A Use as sleep screen switch in the same menu.
- The book popups (Book progress, calendar, Book info) also work when going to sleep from the file manager. The plugin keeps a snapshot of the last book’s data when you close it.
- Removed the old “(sleeping…)” title indicator.

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

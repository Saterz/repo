# v8.1.0 · 2026-10-16

### New

- Streak calendar covers: each day cell now shows the cover of that day’s most-read book, with the runner-up behind it. Covers are cached on disk, so the calendar opens faster. Books without a cover get a placeholder card.
- Image export (Settings > Image export): saves the sleep screen as a PNG, JPG or BMP file that refreshes itself on a timer (5 min to 1 hour), when a book is opened or closed, and on suspend. It is drawn offscreen, so nothing flashes while reading.
  - Android: use the file as your wallpaper, or copy it to a shared folder for a wallpaper-changer app.
  - PocketBook: optionally write it as the power-off / boot logo.
Includes a “Save image now” button.
- Sleep screen preview (Sleep screen > Preview): try your settings without putting the device to sleep. Tap, swipe or press any key to close it.
Streak calendar covers: each day cell now shows the cover of that day’s most-read book, with the runner-up behind it. Covers are cached on disk, so the calendar opens faster. Books without a cover get a placeholder card.

### Fixed

- The sleep screen message and the “Exit sleep screen” gesture now stay on top of the Reading insights popups. #84 
- The sleep screen closes only when KOReader’s own sleep screen is really over, which fixes it closing too early on a delayed wake-up. #84

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

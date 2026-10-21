# v8.5.8 · 2026-10-21

### Fixed

- Better cover cache handling.

# v8.5.7 · 2026-10-21

### Fixed

- Speed up book info popup with added file caching
- Reading shelf is opening faster a bit

# v8.5.6 · 2026-10-21

### Fixed

- Reading calendar and Year shelf open faster

# v8.5.5 · 2026-10-21

### Internal cleanup
- Code that was copy-pasted across several screens (cover thumbnails, common text and layout helpers, month handling) now lives in one place each.
- The Insights screen's code is split into smaller parts (charts and headers), which makes it easier to maintain.
- Added a checker script for translation files.

# v8.5.4 · 2026-10-21

### Changed
- Heatmap bar charts: the "Reading by time of day" and "Reading by weekday" captions now name the active view (time / pages / share), and the view list shows the same full names, e.g. "Reading time by weekday", "Pages read by time of day", "Share of reading time by weekday".

# v8.5.5 · 2026-10-21

### Internal cleanup
- Code that was copy-pasted across several screens (cover thumbnails, common text and layout helpers, month handling) now lives in one place each.
- The Insights screen's code is split into smaller parts (charts and headers), which makes it easier to maintain.
- Added a checker script for translation files.

# v8.5.4 · 2026-10-21

### Changed
- Heatmap bar charts: the "Reading by time of day" and "Reading by weekday" captions now name the active view (time / pages / share), and the view list shows the same full names, e.g. "Reading time by weekday", "Pages read by time of day", "Share of reading time by weekday".

# v8.5.3 · 2026-10-21

### Changed
- Tapping a chart caption now opens a view picker (✓ marks the active view) instead of cycling views; long press no longer does anything on the heatmap charts.
- Book calendar: the cell view (progress / reading time / pages) is chosen from a caption under the month title; tapping a day does nothing. Page cells show the bare count (no "+" / "p" suffix).
- Trend popup: caption and chart now sit above the totals row.

### Added
- 8-week trend popup: four views (weekly time / pages, total / daily average), picked from the caption and remembered.
- Streak history popup: four views (daily / weekly × time / pages) picked from a caption; weekly rows show date ranges and a weekly streak summary; 14 rows per page.

# v8.5.2 · 2026-10-21

### Changed
- Long-press the "Last 7 days" header (or the date in the Current week view) to pick the week view from a list. A plain tap on the "Last 7 days" header no longer does anything.
- Long-press the monthly and daily chart captions to choose their view from a list, with a ✓ on the active one.
- The heatmap's weekday and time-of-day charts now have a pages view. The order is time, pages, percent, both when tapping the caption and in the long-press list.

# v8.5.1 · 2026-10-20

### Fixed

- Swipe gestures in the insights popup: horizontal swipes now change the year only within the year zone  and the week only on the weekly section, and are ignored elsewhere.

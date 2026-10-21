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

# v8.5.0 · 2026-10-20

### New
- **Current week view** (Settings ▸ Reading insight popup ▸ Week ▸ View): the weekly section can show the current calendar week instead of the rolling last 7 days. Page back and forth with the previous/next week labels or a swipe; tapping the shown week's label jumps back to the current week. Totals, averages, chart and the comparison with the previous week all cover the shown week.
- Pages per month chart: the monthly chart now cycles: time → pages → days → books.

### Changed
- Weekly chart: today / the newest day is on the right by default
- Charts show page counts as plain numbers, without a unit suffix.

### Fixed
- The book list popup no longer resets the shown week on return.

# v8.4.1 · 2026-10-20

### Changed

- Some Hungarian translation changed.

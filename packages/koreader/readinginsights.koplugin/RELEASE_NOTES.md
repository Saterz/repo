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

# v8.4.0 · 2026-10-20

### Added
- Sleep screen: new "Random" content option. Shows a different view on every sleep. Choose which views are in the draw under Content > Random views. If a view can't be drawn (e.g. no open book), the next one is tried.
- Reading habits: new "Every 2 hours" time-of-day view (12 bars, one per two hours), now the default. "By part of day" (4 bars) and "Heatmap" remain selectable.

### Changed
- "Reading heatmap" renamed to "Reading habits".
- Reading habits section captions: "Reading by day", "Reading by time of day", "Reading by weekday".
- Peak hour line is hidden in the "Every 2 hours" view, as the bars already
  show it.

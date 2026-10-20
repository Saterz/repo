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

# v8.3.0 · 2026-10-19

### New

- **Reading shelf:** the covers of the books you read in a year, laid out like books on a shelf. Open it from *Tools → Reading insights → Reading shelf* or assign the new "Reading insights: reading shelf" gesture action.
- **Cover shadow color:** the shadow color can be set under *Settings → Appearance → Colors* (50% black by default).

### Changed

- **Reading calendar:** when several books were read on one day, the first sits at the top left and the others peek out behind it at the bottom right; only the backmost cover casts a shadow.
- Books without a cover now get the same frame, rounded corners and shadow as real covers (Reading calendar and Reading shelf).

# v8.2.9 · 2026-10-19

### Changed

- Added configurable heights for the two heatmap bar charts (Time of day, Weekdays).
  - Default height matches the chapter bar (46).
  - New menu entry: Settings > Heatmap & time of day > Bar chart height.
  - If the popup doesn’t fit the screen (mostly in landscape), both charts shrink together automatically, down to a minimum of 10.

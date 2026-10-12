# v7.7.0 · 2026-10-12

### New
**Reading insights: "Last 7 days"**
- **Comparison with the previous week** (new, off by default): below the chart, after a thin divider, shows how the total and the daily average changed compared to the 7 days before, e.g. `+01:20 vs prev. week | +00:18 daily avg time`. When the chart is in pages mode it shows pages instead, e.g. `-115 pages vs prev. week | +16 daily avg pages`.
- **Time and pages row** (new, off by default): a second row with the other metric (pages when the chart shows time, and vice versa).
- The compact row (total + daily average) is now always shown. The *Compact / Full* layout choice is removed; the Full layout's extra values are covered by the new "time and pages row" option.
- Both new options are in the Reading insight popup settings and can be toggled independently.

### Fixed

The gap between bars for 7-day and Monthly chart is now the same.

# v7.6.5 · 2026-10-12

### Changed
- **Reading insights popup (portrait):** the automatic font-size reduction that previously only ran in landscape now also applies in portrait. If the page is still taller than the screen after the bar charts have been sized, all fonts are scaled down together (down to 50%) so the scroll bar is no longer needed. Layouts that already fit keep their configured font sizes.
- **Months chart layout:** the default is now "12 months in one row" instead of "2 rows of 6 months". The layout is still switchable under Settings > Reading insight popup > Months chart layout.

# v7.6.4 · 2026-10-11

### Changed 

- Months chart now defaults to bars
With only a few months of reading data the bar chart looks better than the line with dots, so bars should be the default. The line style is still available under Settings > Advanced settings > Reading insight popup > Months chart style, and an already saved choice is kept.

# v7.6.3 · 2026-10-11

### Fixed

- **Yearly chart:** months before the first reading data are left empty instead of showing "00:00".

# v7.6.2 · 2026-10-11

### Added
- **Goal check mark:** the Daily goal and Weekly goal values show a ✓ once the goal is reached (e.g. `00:45 / 00:30 ✓`).
- **Yearly goal pace:** in the current year, the "% of yearly goal" cell now shows how far ahead of or behind the pace you are, e.g. **3** books ahead of pace or **1** book behind pace.
  - Shows "On track" when you are less than one book off pace.
  - Shows "Goal reached" once the yearly goal is met.
  - Pace is based on the day of the year and counts whole books only.
- **Closed years:** past years show "Goal reached" or "Goal not reached" instead of the percentage (only if a goal was set for that year).

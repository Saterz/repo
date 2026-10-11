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

# v7.6.1 · 2026-10-11

### Changed
- Yearly chart: months that haven't happened yet are cut off. The line ends at the current month, and the bar style no longer shows "00:00" for upcoming months. Their month names stay on the axis, and past years still show all 12 months.

# v7.6.0 · 2026-10-11

### New
- **Yearly (months) chart is now a smooth line chart by default.** A monotone-cubic curve passes through one dot per month. The curve never overshoots below zero or above the peak.
  - **Values sit above the dots.** A value moves up one row only if it would overlap its neighbour, so compact formats like `0:04` never move.
  - **The current month's dot uses the active colour.** Tapping a month still opens its books.
- **"Last 7 days" chart can also be shown as a line with dots**, with the same smooth curve. Today is highlighted and still opens the timeline. The "Today on the left/right" order and the time/pages toggle keep working. Bars remain the default here.

### Changed

- **"Days read" view is now scaled to the length of each month.** Every fully read month stands equally high, whether it has 28, 29, 30 or 31 days, and the label still shows the real day count. This applies to both the bar and line styles. The Hours and Books views are unchanged.
- Some settings reorganized

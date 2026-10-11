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

# v7.5.4 · 2026-10-10

Changed
- "Typical chapter length": Books with very many short chapters no longer have half of their
  real chapters discarded, and books where a few huge chapters hold most of the
  text are no longer dragged down by a pile of tiny entries.

# v7.5.3 · 2026-10-10

### Changed
- "Last week" is now "Last 7 days" in all languages, since the section shows a rolling 7-day window, more clear what doest this show
- "Annual goal" is now "Yearly goal"
- Finished books counter now reads "27 / 30" instead of "27/30"

# v7.5.2 · 2026-10-10

### Changed
- Daily/weekly goal popup: the “default values” button now shows a readable value (e.g. “Default: 00:30/30m” / “Default: 05:00/5h”) instead of KOReader’s raw “Default values: 0 : 30” / “5 : 0”.
  - The value follows KOReader’s duration format setting.

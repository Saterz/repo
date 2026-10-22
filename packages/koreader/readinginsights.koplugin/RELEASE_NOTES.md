# v8.6.3 · 2026-10-22

### Changed
- The yearly reading goal is now edited with a spin picker (+/− buttons, hold to step by 5), matching the daily/weekly goal popup but with a single number (1–999).

### Fixed
- Tapping the number in the reading goal and daily/weekly goal pickers opens the keyboard entry field above the popup instead of behind it.

# v8.6.2 · 2026-10-22

### Fixed
- Daily/weekly goal no longer shows e.g. `00:30 / 00:30` without a check mark when the goal is missed by a few seconds. Durations shown without seconds are now rounded down to the whole minute (29m 40s reads `00:29`), so the displayed value and the check mark always match.
  - Applies consistently to all minute-resolution durations (charts, trend view, heatmap, records, calendars, book statistics) and follows KOReader's "Duration format" setting.
- Reading under one minute still shows `<00:01` (`<1'` / `<1m` in the other formats); exactly zero stays a plain zero.

### Unchanged
- Durations that include seconds (e.g. the book lists) are displayed as before.

# v8.6.1 · 2026-10-22

### Fixed
- Reading time under one minute is now shown as `<00:01` instead of an empty `00:00`. The marker follows KOReader's "Duration format" setting (`<00:01` classic, `<1'` modern, `<1m` letters).
- Applies everywhere durations are displayed without seconds: weekly, monthly and trend charts, goals, calendars and book statistics.
- Exactly zero reading time still shows as a plain zero.

# v8.6.0 · 2026-10-22

### Changed

- Tapping a day’s column in the weekly chart (“Last 7 days” / “Current week”, bar and line styles) now opens the list of books read on that day, the same list the streak calendar shows. Long-pressing today’s column opens the day timeline.
- “Current week” view: the columns are now labelled with the date (no year, in the configured date format, e.g. 10. 20.) instead of the weekday.
- Today (“Today” label / today’s date), the current month and the current week in the 8-week trend are now shown in bold.
- Reorganize plugin files into readinginsights/{data,cache}, cap cover cache at 25 MB, move settings cleanup to lib/cleanup.lua

### Fixed
- Heatmap: all seven weekday labels are shown on the left when the rows are tall enough (e.g. 6 months); otherwise only Mon/Wed/Fri as before.
- Fixed missing space in the short date of the 8-week trend (09.30. → 09. 30.).
- Drop redundant caption long-presses

# v8.5.8 · 2026-10-21

### Fixed

- Better cover cache handling.

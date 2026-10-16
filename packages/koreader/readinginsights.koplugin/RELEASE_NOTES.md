# v8.1.5 · 2026-10-16

### Fixed

- Faded previous/next-month days in the calendars being too bright in night mode; they now fade towards the dark background.

# v8.1.4 · 2026-10-16

### Changes
- Some more minor padding fix.

# v8.1.3 · 2026-10-16

### Changed

- Heatmap: the "Days of the week" bar chart now uses the same maximum bar height as "When you read" (was 60%).
- Compact layout: popup sections, headers and chart labels now use small,uniform vertical spacing
- Streak history popup: new bottom block showing the streak length in days and weeks, each with its date range ("123 days | from – to"). It replaces the old separate info message.
- Book progress calendar: tapping a day with reading data cycles the cell content (percent → time → pages) and remembers the last choice; the tap no longer opens the day detail popup. The separate settings menu is removed.

# v8.1.2 · 2026-10-16

### Changed

- Reading streak is now called Reading calendar.

### Added

- Reading calendar settings submenu (Settings > Reading calendar).
  - Show streak bar under covers option in the new Reading calendar settings. Default off. Covers already shows the streaks beginning and end.
- Long-pressing the “Reading calendar” title reloads the covers (clears the cover cache and loads them again).
- A third stacked cover in calendar day cells. Each cover sits one step up and to the right of the one in front, and covers are slightly smaller when three are shown.
  - A +1, +2, … tag on the front cover when a day has more than three books, counting the books beyond the third.

# v8.1.1 · 2026-10-16

### Changed

- Book progress calendar style matches more the Reading Streak.

### Fixed

- Day number alignment on Book progress calendar: the day number sat at a different height on days with a progress bar than on days without one.
- Percentages not always adding up to 100% on Book progress calendar.

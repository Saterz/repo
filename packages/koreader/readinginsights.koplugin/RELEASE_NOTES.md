# v8.7.2 · 2026-10-23

### Changed
- Column separators now use the same spacing as the left screen-edge margin on the Reading insights page, the Book progress popup and the Streaks popup. The right-hand column sits closer to its separator than before.
- The inner separators (days | weeks, time | pages) use the same spacing as the outer ones.

# v8.7.1 · 2026-10-23

### Changed
- "Fewer, thin" divider style now draws horizontal dividers at most Size.line.medium thick (previously Size.line.thin), as the thinnest lines don't look good on e-ink.

# v8.7.0 · 2026-10-23

### Added
- Settings > Appearance > Divider lines, with four styles:
  - Normal (default): classic look, a line under every header.
  - Fewer: only the lines between sections.
  - Fewer, thin: like Fewer, with 1px horizontal lines.
  - Off: no lines at all, vertical ones included.

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

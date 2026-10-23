# v8.7.4 · 2026-10-23

### Fixed

- Some places still didn't used proper ISO date format.

# v8.7.3 · 2026-10-23

### Changed

- ISO date format matches KOReader's ISO dates better when there is a day after the date

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

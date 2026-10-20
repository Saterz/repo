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

# v8.2.8 · 2026-10-18

### Fixed

- Book info popup: the small cover is now exactly as tall as the text beside it (rating, title, author, series, pages / reading time); the description is hidden at this size.
- Book info popup: the large cover now grows as big as the popup allows while all the text still fits, with no cut-off lines.

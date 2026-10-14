# v7.8.9 · 2026-10-14

### Changed 
Removed the progress bar from the "This chapter" row in the Book progress popup. 
_Note: That row shows the time left rather than a percentage, so a bar under it looked out of place. The bar is now only shown under the book's read percentage._

# v7.8.8 · 2026-10-14

### Changed 
In the Book progress popup, the "This book" section now shows the read percentage row first again, with its progress bar directly under the percentage (inside that cell only, matching the chapter bar), This makes it more consistent across the plugin.

# v7.8.7 · 2026-10-14

### Changed

- In the Last 7 days comparison row (pages view), when a long value leaves no room for the full labels, both cells switch to shorter ones (“pg vs prev. 7d” / “daily avg pg”) instead of wrapping onto two lines.
Added: short label translations for all languages (en, hu, fr, de, pt_PT, uk, zh_CN).

# v7.8.6 · 2026-10-14

### Fixed

- The “vs previous 7 days” row in Last 7 days now respects KOReader’s duration format (classic / modern / letters) and the “long durations as days” option.

### Changed

- The time label is now “time vs prev. 7d” (translated in all languages). It automatically falls back to the shorter “vs prev. 7d” when a long value leaves no room for it.
- With the “letters” duration format, the monthly reading time chart shows compact labels in the 12-month single-row layout: decimal hours (1.9h / 1,9h) from one hour up, minutes (45m) below that. The 2×6 layout keeps the full duration.

# v7.8.5 · 2026-10-14

## Changed

- **Default colors now follow KOReader's own palette.** Tried to match the colors KOReader uses for its thin status bar, so the plugin looks consistent with the rest of the UI:
  - Active columns and progress indicators (bar charts, skim bar, donut chart, daily streak days): `#555555` (`COLOR_GRAY_5`)
  - Inactive columns and remaining/unread portions (bar charts, skim bar, donut chart, weekly streak gap days): `#AAAAAA` (`COLOR_GRAY`)
  - Separator lines: `#888888` (`COLOR_DARK_GRAY`)
- The heatmap scale, trend line and text colors are unchanged.

## Notes

- Colors you have already customized under the Colors menu are kept. To switch to the new defaults, use "Reset to default" on the respective color.

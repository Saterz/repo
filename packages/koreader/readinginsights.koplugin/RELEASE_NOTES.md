# v7.8.5 · 2026-10-14

## Changed

- **Default colors now follow KOReader's own palette.** Tried to match the colors KOReader uses for its thin status bar, so the plugin looks consistent with the rest of the UI:
  - Active columns and progress indicators (bar charts, skim bar, donut chart, daily streak days): `#555555` (`COLOR_GRAY_5`)
  - Inactive columns and remaining/unread portions (bar charts, skim bar, donut chart, weekly streak gap days): `#AAAAAA` (`COLOR_GRAY`)
  - Separator lines: `#888888` (`COLOR_DARK_GRAY`)
- The heatmap scale, trend line and text colors are unchanged.

## Notes

- Colors you have already customized under the Colors menu are kept. To switch to the new defaults, use "Reset to default" on the respective color.

# v7.8.4 · 2026-10-13

### Changed

- Book progress popup: in the "This book" section, the remaining reading time now comes before the time read so far (classic and donut chart styles).

# v7.8.3 · 2026-10-13

### Changed
- Shortened the "Last 7 days" popup labels to fit wider values: `daily avg time/pages`, `vs prev. 7d`, `pages vs prev. 7d`.

# v7.8.2 · 2026-10-13

### Fixed
- Unified the "daily average" labels. The "Last 7 days" popup and the book stats popup now share the same strings: `daily average time` and `daily average page(s)` (previously `daily avg ...` and `avg time/day` / `avg pages/day`).

# v7.8.1 · 2026-10-13

### Changed
- **Chapter progress:** the first page of a chapter now counts as 0%, not as progress. The percentage only starts to grow once you turn to the next page.
- **Chapter bar chart:** the chapters now follow your e-reader's own table of contents, so the chart and the chapter percentage always agree. Books with a multi-level contents list may show more columns.

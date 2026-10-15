# v1.7.3 · 2026-10-15

### Changed
- Added a new **Appearance** menu grouping Layout, Cover, Background, Colors, Fonts and Margins
- Moved **Updates** and **About** below Advanced Settings, with a separator above About
- Advanced Settings now only contains Orientation, Image export and Clear cached data

# v1.7.2 · 2026-10-15

### Changed
- The Statistics submenu was removed: Configure statistics items and Reading goal settings now sit directly in the Card elements menu, with a separator line between them.

# v1.7.1 · 2026-10-15

### Changed
- Removed the hamburger (A-Z / Z-A sort) menu from the Configure statistics items dialog, as it does not apply to this list.

# v1.7.0 · 2026-10-15

### Added
- **Daily Goal / Weekly Goal** statistics rows: time read today / this calendar week (all books) against a goal, e.g. `12 min / 30 min`, with a ✓ once the goal is met.
  - Goals are set in Card elements > Statistics > Reading goal settings (hours + minutes).
  - They use Reading Insights' own settings (`reading_insights_daily_goal_min`, `reading_insights_weekly_goal_min`), so changing a goal in either plugin changes it in both. Without Reading Insights, the key is created when a goal is first set.
- **Pages Read Today (This Book)** and **Pages Read Today (All Books)** statistics rows.
- **Separator lines** for the statistics column: long-press a row in Statistics > Configure statistics items to add a thin line below it, long-press again to remove it. Rows with a line are underlined in the list.
- **Separator line color** under Colors (default `#888888`).

### Changed
- **Statistics > Configure statistics items** (formerly "Reorder") is now the one place to manage the statistics rows: drag to reorder, tap the checkbox on the left to show or hide a row, long-press to toggle a separator line.
- The per-row on/off toggles were removed from the Statistics menu, since the configure dialog covers them.
- The daily and weekly goal settings moved into a new **Reading goal settings** submenu, the last entry of the Statistics menu.
- The author line is now regular instead of italic by default (still configurable under Fonts).

All new statistics rows are off by default.

# v1.6.0 · 2026-10-08

### Added
- New "Stats per row (centered cover only)" setting (Advanced Settings → Layout) that controls how many statistics appear side by side in the centered-cover layout's grid. Range is 1–5, default 2 (the previous fixed behavior).
- The setting is greyed out unless the "Cover centered, statistics grid below" layout is selected.

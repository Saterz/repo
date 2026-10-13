# v2.0.0 · 2026-06-27

## v2.0.0 — Fast Clone, UI Fixes, and Ignore Patterns

### New Features
- **Fast clone via tarball download** — cloning repos is now ~10x faster by downloading the tarball archive instead of running git clone or downloading file-by-file
- **Real-time clone progress** — shows file count and current filename during clone
- **.ghbrowser.json added to default ignore patterns** — local config file is no longer visible in file listings

### Bug Fixes
- **Fix progress dialog stacking** — progress dialog now correctly appears above the overwrite confirmation dialog when cloning to an existing directory
- **Remove external unzip dependency** — switched from zipball to tarball extraction since `tar` is universally available on all KOReader devices via BusyBox, while `unzip` often is not

### Changes
- Updated version to 2.0.0

# v1.0.1 · 2026-05-24

- "Fixed namespace collisions with other KOReader plugins (such as obsidian-sync) by namespacing internal helper modules. Bumps version to 1.0.1."

# v1.0 · 2026-05-17


- **Feature:** Added `Search files/folder` and `Search code` inside repositories!
- **Performance:** Capped search results to prevent UI lag on massive repositories.
- **Fix:** Resolved a major layout crash (`makeline`) on e-ink devices when displaying long code search snippets.
- **UI:** Replaced raw text snippets with sanitized text to ensure clean rendering on all devices.
**Full Changelog**: https://github.com/right9code/githubbrowser.koplugin/compare/v0.2...v1.0

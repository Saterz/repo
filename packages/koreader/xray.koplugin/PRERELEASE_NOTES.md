# 26.10.15-beta · 2026-10-16

## New Features: Prefetch Horizon & Entity Evolution

- **Offline Prefetch Horizon**: You can now set X-Ray to quietly pre-generate *1, 2, 3, or 5 chapters ahead* in the background while on Wi-Fi. Future characters, locations, terms, and events stay hidden until you actually reach those pages, so your data is ready when reading offline.
- **Full Book Pre-generation**: Added a **Pre-generate Entire Book** option to the main menu to scan a book chapter-by-chapter in the background while keeping full spoiler protection as you read.
- **Character & Entity Evolution**: Descriptions, roles, and statuses now update chapter-by-chapter as the story unfolds. Detail cards include a new *Past Evolution* view showing how an entry has changed up to your current page, and flipping back to earlier chapters automatically shows descriptions as they were at that point in the book.
- **Stricter Spoiler Protection**: Tightened text boundaries so multi-chapter files, highlights, mention scans, and single-word lookups never pull context from past your current page.

## Bug Fixes & Improvements
* Fix: enable Cyrillic units scan by @Gargoyle-Gecko in https://github.com/ultimatejimmy/xray.koplugin/pull/148
- **Wider Device Support for Images**: Reworked EPUB and CBZ image scanning to use KOReader's built-in archive reader rather than relying only on system `unzip` commands. The Images gallery now works much more reliably across Android, Kindle, and Linux setups.
- **Image Gallery Fixes**: Improved how maps, full-page illustrations, and small decorative graphics are sorted out, and fixed an issue where revealing a spoiler-protected image wouldn't stick while browsing the gallery.
- **Fractional Series Numbering**: Fixed series handling for novellas and split volumes numbered like *1.5* or *2.5*. Decimal book numbers are now preserved in **Manage Series**, confirmation prompts, and timeline labels, and custom series rosters properly sync and fetch prior-book context without skipping fractional entries or wiping cached data.

**Full Changelog**: https://github.com/ultimatejimmy/xray.koplugin/compare/26.10.12-beta...26.10.15-beta

# 26.10.12-beta · 2026-10-12

## What's Changed
* Fix series context for fractional series indices (1.5, 2.5, …) by @tristinbaker in https://github.com/ultimatejimmy/xray.koplugin/pull/151
* Update gemini, claude, and deepseek model lists

## New Contributors
* @tristinbaker made their first contribution in https://github.com/ultimatejimmy/xray.koplugin/pull/151

**Full Changelog**: https://github.com/ultimatejimmy/xray.koplugin/compare/26.10.10-beta...26.10.12-beta

# 26.10.10-beta · 2026-10-10

- Update gemini models

**Full Changelog**: https://github.com/ultimatejimmy/xray.koplugin/compare/26.10.8...26.10.10-beta

# 26.10.6-beta · 2026-10-06

## What's Changed
* Fix Ukrainian unit conversion by @Gargoyle-Gecko in https://github.com/ultimatejimmy/xray.koplugin/pull/146
* Fix: restore unit underlines from cache on book reopen by @Gargoyle-Gecko in https://github.com/ultimatejimmy/xray.koplugin/pull/147

## New Contributors
* @Gargoyle-Gecko made their first contribution in https://github.com/ultimatejimmy/xray.koplugin/pull/146

**Full Changelog**: https://github.com/ultimatejimmy/xray.koplugin/compare/26.10.2-beta3...26.10.6-beta

# 26.10.2-beta3 · 2026-10-02

## What's Changed

This release focuses on memory optimizations and stability improvements to keep X-Ray running smoothly, especially on older or low-memory e-ink devices like earlier Kindles and Kobos.

* **Low-memory protection**: X-Ray now dynamically monitors available device RAM. If system memory is running critically low, silent background tasks (like automatic chapter fetches and weekly update checks) will quietly step aside to prevent crashes or freezes. Manual requests from the menu still work as usual.
* **Smoother book opening**: Background tasks and automatic unit scans are now deferred for a few moments after opening a book. This gives KOReader the breathing room it needs to render pages and load fonts without competing for CPU and RAM.
* **Unit scanner memory cleanup**: Searching an entire book for units now cleans up temporary search tables in stages rather than holding them in memory, noticeably lowering peak memory usage during book scans.
* **Leaner AI data handling**: Background network requests now clean up raw downloaded buffers and temporary structures immediately after parsing book details.

**Full Changelog**: https://github.com/ultimatejimmy/xray.koplugin/compare/26.10.2-beta...26.10.2-beta3

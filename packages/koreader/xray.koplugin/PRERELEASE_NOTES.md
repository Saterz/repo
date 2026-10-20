# 26.10.19-beta · 2026-10-20

- Fix bug with highlighted text.

**Full Changelog**: https://github.com/ultimatejimmy/xray.koplugin/compare/26.10.18-beta...26.10.19-beta

# 26.10.18-beta · 2026-10-19

Gesture now opens normal x-ray menu

**Full Changelog**: https://github.com/ultimatejimmy/xray.koplugin/compare/26.10.16-beta...26.10.18-beta

# 26.10.16-beta · 2026-10-16

## What's Changed

### Story Arc Fixes & Consistency
* **Updated Settings Naming**: Renamed all remaining menu items and descriptions to **Story Arc Settings** across all languages for consistency.
* **Support for Part-Only Books**: Fixed an issue where books divided into large "Parts" rather than regular numbered chapters (such as Stephen King's *Carrie*) resulted in missing character arcs. The plugin now automatically breaks oversized sections into smaller segments during prefetch so characters evolve naturally across the entire story.
* **Prefetch Truncation Fix**: Fixed a bug where starting full-book pre-generation or horizon prefetch from early pages could prematurely truncate the first chapter.

### Stability & Performance on E-Readers
* **Reduced Memory Footprint**: Fixed an issue where extracted chapter text was kept in memory during background pre-generation. Text buffers are now freed immediately once sent.
* **Low Memory Guards**: Added checks that monitor free memory between prefetch batches and pause background scanning if system RAM runs low, preventing crashes on memory-constrained devices like Kindles.
* **Fetch Collision Prevention**: Page turns and chapter transitions while reading will no longer trigger conflicting background fetches while pre-generation is actively running.

### Unit Converter
* **Language-Aware Cache Versioning**: The unit converter now tracks rule changes per language and category rather than using a single global version bump. Updates to vocabulary or aliases in other languages will no longer invalidate your existing scanned books, eliminating unnecessary re-scans.
* **Legacy Cache Migration**: Existing unit caches are now automatically recognized and preserved across updates.

**Full Changelog**: https://github.com/ultimatejimmy/xray.koplugin/compare/26.10.15-beta...26.10.16-beta

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

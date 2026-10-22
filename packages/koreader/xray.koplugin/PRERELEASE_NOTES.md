# 26.10.23-beta · 2026-10-22

## What's New

### Instant X-Ray Popups on Highlight

You can now jump straight into X-Ray details when selecting a character, location, or term on the page, skipping the intermediate dictionary popup or highlight menu.

* **Direct Lookups on Text Selection:** When enabled, long-pressing or highlighting a word or phrase that matches an X-Ray entry immediately opens its profile or footnote popup.
* **Smart Fallback:** If you highlight an entire sentence, a phrase without X-Ray data, or an ordinary word, KOReader's standard dictionary or highlight menu opens just like before.
* **One-Tap Access to the Highlight Menu:** Whenever an X-Ray popup opens from a highlight, a new **Highlight Menu** button appears in the action bar. Tapping it restores your text selection and opens the native KOReader highlight menu so you can still create notes, highlight passages, translate, or check external dictionaries without losing your place.
* **New X-Ray Mode Setting:** Choose how X-Ray integrates with reading under **Settings → X-Ray Mode Settings**:
  * **Button in Menu (Default):** Keeps the classic behavior, adding an *X-Ray* button inside KOReader's dictionary and highlight menus.
  * **Auto-Popup on Highlight:** Skips the menu and displays X-Ray data instantly when a match is found.
  * **Disabled:** Hides in-text X-Ray buttons completely.

**Full Changelog**: https://github.com/ultimatejimmy/xray.koplugin/compare/26.10.22...26.10.23-beta

# 26.10.21-beta2 · 2026-10-21

- Change notification logic on full-book fetch
- update logging


**Full Changelog**: https://github.com/ultimatejimmy/xray.koplugin/compare/26.10.19-beta...26.10.21-beta2

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

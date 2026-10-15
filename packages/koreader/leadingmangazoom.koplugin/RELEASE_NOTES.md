# v1.3.0 · 2026-10-15

Free zoom for newspapers, magazines and textbooks, plus quadrant navigation for manga. This release also includes v1.2.0, which never got its own release.

### ✨ New: Free zoom (v1.3.0)
- **Spread** zooms in on the spot between your fingers, by how far you spread. Spread again to go further (up to 8× the fitted page).
- **Drag** to move around the page in any direction. It doesn't snap back to a page corner when you change direction, and the screen redraws once when you lift your finger, so e-ink doesn't flash.
- **Swipe**, diagonals included, to jump straight to the next article.
- **Pinch** zooms out step by step; pinch back to full-page size (or tap) to return.
- Your Gesture manager actions keep working. The plugin only takes spread, pinch, drags and swipes while it's using them, so there's no need to set them to *Pass through*.

### 🔧 Fixes (v1.3.0)
- Fixed a crash when opening the zoom tab of the bottom menu while zoomed (`koptoptions.lua:172: attempt to compare nil with number`). Picking a zoom mode there while zoomed now switches to it.
- Free zoom is capped so huge broadsheet pages don't ask the renderer for oversized images.

### 📚 Quadrant navigation (v1.2.0)
- While a quadrant is zoomed, swipe, tap the screen sides or press the page buttons to move to the next quadrant in reading order (RTL aware), continuing onto the next page.
- Page changes made while zoomed (go to page, TOC, links) release the zoom cleanly.
- Zoom levels account for a visible status bar, so quadrants aren't cropped at the bottom.

### 📥 Installation
Download **leadingmangazoom.koplugin.zip** below and extract it into KOReader's `plugins/` folder, replacing the old `leadingmangazoom.koplugin` folder. You should end up with `plugins/leadingmangazoom.koplugin/main.lua`. Restart KOReader, and keep Reflow off for the document.

> Don't use GitHub's "Source code" zip. It has an extra outer folder, and the plugin won't show up.

### 🧪 Testing
Regression tests pass (34), including touch-dispatch checks against KOReader's real gesture code. An earlier build of free zoom was tried by @shuvashish76 on Android and a Kobo Clara BW (thanks!); the fixes above came from that feedback.

Requested in [Euphoriyy/KOReader.patches#26](https://github.com/Euphoriyy/KOReader.patches/issues/26) · Changes: #8, #9, #10

# v1.1.2 · 2026-09-06

Fixes for module loading, gestures, and split-page navigation on KOReader.

- Fix settings crashes and duplicate menus caused by module-name collisions with Maximum or other plugins.
- Make two-finger tap, spread, pinch, and tap-to-collapse take priority while enabled, with normal gesture fallback when disabled.
- Fix split-page navigation using taps, swipes, and physical buttons, including RTL and backward navigation between spreads.
- Apply landscape modes immediately and on the opening page; keep auto-rotate and split defaults mutually exclusive.
- Cancel stale pan callbacks and restore previous zoom, pan, reading direction, and continuous-view settings after temporary zooming.
- Retain the v1.1.1 physical-button fix and correct layout updates when restoring portrait orientation.

Installation: download **leadingmangazoom.koplugin.zip**, extract it into KOReader's **plugins/** directory, replace the existing **leadingmangazoom.koplugin** folder, and restart KOReader. Disable Reflow for the document.

Validation: regression tests pass on Lua 5.1 and LuaJIT, with touch-dispatch integration checks against KOReader 2026.03 and 2026.07. Physical-device testing was not available.

Changes: https://github.com/Auri3l/leadingmangazoom.koplugin/pull/6

# v1.1.1 · 2026-07-24

v1.1.1 Release: Fix physical page-turn button remapping bug on Kobo Sage, Kobo Libra 2, Kobo Forma, PocketBook, and Kindle Oasis devices when auto-rotating landscape pages.

# v1.1.0 · 2026-07-16

v1.1.0 release: Add CZB support, fix zoom coordinates, pinch gesture, and RTL split-page navigation

# v1.0.0 · 2026-04-11

Initial release of LeadingMangaZoom for KOReader.

Two-finger tap to zoom into any quadrant. Tap to zoom back out. Spread/pinch for page zoom. Auto-rotate and page split for landscape pages.

**Installation:** Extract the zip and copy the `leadingmangazoom.koplugin` folder into KOReader's `plugins/` directory. Restart KOReader.

Supports CBZ, CBR, and PDF files. Requires touch-enabled device.

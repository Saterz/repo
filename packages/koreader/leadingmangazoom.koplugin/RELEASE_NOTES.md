# v1.5.1 · 2026-10-18

Double tap to zoom, with a zoom level you choose.

### 👆 Double-tap to zoom
- **Double tap** anywhere on the page to zoom in on that spot; double tap again to go back to the page. Drag, swipe and pinch work as usual while zoomed.
- Turn it on in **Leading Manga Zoom › Double-tap to zoom** and pick a **Zoom level**: 1.5×, 2×, 2.5×, 3× or 4×. Off by default.
- KOReader normally ignores double taps. While this option is on, the plugin turns them on for supported books only, so single taps (like page turns) wait a moment to check for a second tap.

### 🔄 Updating
On v1.5.0, use **Leading Manga Zoom › Updates › Check for updates**. On older versions, download **leadingmangazoom.koplugin.zip** below and replace the `leadingmangazoom.koplugin` folder in KOReader's `plugins/` folder.

Closes #12 · Changes: #17

# v1.5.0 · 2026-10-18

Update the plugin from inside KOReader, no computer needed.

### 🔄 Updates from inside KOReader
- **Leading Manga Zoom › Updates › Check for updates** checks GitHub, shows what's new in the latest release and installs it with one tap, then offers to restart KOReader. Wi-Fi is turned on if needed.
- **Check automatically once a day** (off by default) looks for a new version only when Wi-Fi is already on, and never turns Wi-Fi on by itself.
- Before anything is replaced, the download is checked: it must be this plugin's release zip, contain its main files and carry the expected version. It's unpacked into a temporary folder first, so a broken download leaves your installed version untouched, and the message says why.

### Other changes
- The plugin menu now opens for any book, so **About** and **Updates** are always reachable. Reading options still need a supported file.

### 📥 Installation
**Install this version by hand once**; from here on, the plugin can update itself.

Download **leadingmangazoom.koplugin.zip** below and extract it into KOReader's `plugins/` folder, replacing the old `leadingmangazoom.koplugin` folder. You should end up with `plugins/leadingmangazoom.koplugin/main.lua`. Restart KOReader, and keep Reflow off for the document.

> Don't use GitHub's "Source code" zip. It has an extra outer folder, and the plugin won't show up.

Changes: #16

# v1.4.1 · 2026-10-18

Desktop controls for KOReader on Linux, macOS and Windows. This release includes v1.4.0, which didn't get its own release.

### 🖱️ Desktop controls
- **Ctrl + mouse wheel** zooms in and out, keeping the spot under the mouse pointer in place, like Okular.
- **Ctrl + / Ctrl −** zoom from the keyboard, main keys or keypad. **Ctrl 0** returns to the full page.
- **Mouse wheel** scrolls while zoomed in. **Shift + wheel** (or a sideways wheel/trackpad) scrolls left and right. On the full page the wheel turns pages as before.
- **Click and drag** moves the page around.

### 🔧 Fixes
- The mouse wheel no longer turns the page while you're zoomed in.
- Keypad +, − and 0 now work. KOReader's desktop builds didn't recognise them.

### 📥 Installation
Download **leadingmangazoom.koplugin.zip** below and extract it into KOReader's `plugins/` folder, replacing the old `leadingmangazoom.koplugin` folder. You should end up with `plugins/leadingmangazoom.koplugin/main.lua`. Restart KOReader, and keep Reflow off for the document.

> Don't use GitHub's "Source code" zip. It has an extra outer folder, and the plugin won't show up.

Requested in [Euphoriyy/KOReader.patches#26](https://github.com/Euphoriyy/KOReader.patches/issues/26) · Changes: #13, #15

# v1.3.1 · 2026-10-15

Fixes from Kindle Colorsoft feedback. This is the first release with the free zoom zip attached (v1.3.0 went out without it), so if you downloaded "latest" in the last few hours, please grab this one.

### 🔧 Fixes
- **Moving between quadrants with swipes:** if *swipe to go back* or *swipe to follow nearest link* is turned on in KOReader, those swipes used to take priority while a quadrant was zoomed. Quadrant swipes now win while zoomed, and link swipes work as before otherwise.
- **Zoom mode kept when closing mid-zoom:** closing a book (or an autosave) while zoomed in no longer replaces the book's zoom mode with the temporary free zoom.

### Included from v1.3.0
- **Free zoom** for newspapers, magazines and textbooks: spread to zoom by how far you spread, drag or swipe (diagonals too) to move anywhere, pinch to zoom out.
- Fixed the crash when opening the zoom tab of the bottom menu while zoomed.
- Quadrant navigation from v1.2.0 (swipe, side taps or page buttons to move between quadrants).

### 📥 Installation
Download **leadingmangazoom.koplugin.zip** below and extract it into KOReader's `plugins/` folder, replacing the old `leadingmangazoom.koplugin` folder. You should end up with `plugins/leadingmangazoom.koplugin/main.lua`. Restart KOReader, and keep Reflow off for the document.

> Don't use GitHub's "Source code" zip. It has an extra outer folder, and the plugin won't show up.

Changes: #11

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

# v1.5.3 · 2026-10-29

Continuous view now zooms what you actually see on screen.

### 🔧 Fixes
- **Quadrant zoom in continuous view** (#20): when the screen showed the end of one page and the start of the next, quadrant zoom divided only the top page into quarters, so tapping the bottom of the screen could zoom into the wrong page. Quadrants are now quarters of the screen as you see it, each zooming into whichever page it shows. Moving between quadrants follows the screen across pages, and after the last one it scrolls to the next screen.
- **Spread, double tap and Ctrl + wheel** in continuous view now zoom into the page under your fingers or mouse pointer, not the top page.
- **Back where you were:** returning from any zoom in continuous view puts the view back exactly where it was scrolled, instead of at the top of a page.

Single-page view works as before.

### 🔄 Updating
On v1.5.0 or newer, use **Leading Manga Zoom › Updates › Check for updates**. On older versions, download **leadingmangazoom.koplugin.zip** below and replace the `leadingmangazoom.koplugin` folder in KOReader's `plugins/` folder.

Fixes #20 · Changes: #21

# v1.5.2 · 2026-10-18

Fix: double-tap zoom now stays on.

### 🔧 Fixes
- **Double-tap zoom stays on after closing a book.** Turning it on is now remembered for all books, like its zoom level. Before, tapping the option only turned it on for the open book, so it seemed to switch itself off (#18, reported on a Kindle Paperwhite SE 2024). The other options work as before: tap for this book, hold to set the default.

### 🔄 Updating
On v1.5.0 or newer, use **Leading Manga Zoom › Updates › Check for updates**. On older versions, download **leadingmangazoom.koplugin.zip** below and replace the `leadingmangazoom.koplugin` folder in KOReader's `plugins/` folder.

Fixes #18 · Changes: #19

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

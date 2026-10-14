# v8.0.0 · 2026-10-14

## Panel View Update

- **Detail panel in split view:** Tap an annotation or bookmark row in the split menu to preview its page. Tap the same page again to open the detail panel, which shows the full content of that item (the quote, note, chapter, and page) instead of only the page preview. You can now swipe through annotations inside the detail panel. A "Show in book" link jumps to that page in the book. You can expand the panel to use more of the screen.

- **New Images tab in the split menu:** It works like the annotation tabs. The right menu lists the pages that contain images. Tap a row to preview that page, and tap it again to open the detail panel, where you can pinch-zoom the image or expand the panel for a bigger view and more room to zoom.
  - Can be turned off in Settings > Layout > Disable Image Tab.
  - Only scans images up to the point you've read, which avoids spoilers and keeps it from loading every image at once.
  - Creates two files in the conf folder to store the image data.

- **Selection menu:** Text selection, Dictionary, Wikipedia, and Translate can now be added to the main selection menu from Settings > Buttons in selection menu. Buttons left off stay in the More row.

## Fixes

- Minor visual improvements to the quick menu and settings (gray divider lines).
- Long-pressing a highlight and choosing a color now paints it with that color. Previously it sometimes showed as the default yellow.
- Toggles that are off by default were shown as enabled in the selection menu settings.
- If the pinned page has a bookmark, it now also shows up in the bookmarks list.

## Installation
1. Download the zip named `page_scrubber.koplugin-<version>.zip` from the **Assets** section below (not "Source code").
2. Unzip it and copy the `page_scrubber.koplugin` folder into `koreader/plugins/`.
3. Restart KOReader.

To update, replace the folder. To uninstall, delete it (and `koreader/patches/2--page-scrubber-font.lua` if you used the system font).

# v7.7.7 · 2026-10-09

## New Features

### Split Menu
* **Color filter:** Now, in the Highlights and Notes tab, if there are annotations with more than one color, a new triangle icon will appear allowing you to filter entries by color.
* **Individual color selector:** A new circular button was added to the highlight type editing row. This button allows you to directly change the color of a specific annotation (works for all styles except invert).

### Selection Menu
* **Quick color menu:** By long-pressing any highlight style (Highlight, Underline, or Strikethrough), the new color menu will now unfold to let you choose which color to paint the annotation with.

---

## Fixes & Improvements

### Interface & Behavior
* **DPI pagination fix:** Fixed a critical bug where changing the screen DPI caused selecting an annotation in the Split Menu to take you to the wrong page.
* **Optimized Split Menu loading:** The plugin now uses the same logic as KOReader's native listing. This fixes the excessive loading times when opening the menu after rotating the screen between portrait and landscape.
* **Native notes integration:** Tapping the button to add text notes will now directly invoke KOReader's native menu.
* **Visual refinement:** Slightly reduced the thickness of the buttons within the Split Menu and refined the SVG icons overall for a more polished look.

### Performance
* **Reduced lag when turning pages:** Rewrote the pagination logic to prevent bottlenecks and extreme slowdowns.
  * **Preload queue optimization:** Each new tap now cancels older preload tasks that were still in the queue. Additionally, the engine now prioritizes loading pages in the direction you are navigating.
  * **Concurrency control (Semaphore):** Implemented a semaphore system. If the current page hasn't finished rendering, page turns are blocked, preventing background processes from piling up and freezing the device.


## Installation
1. Download the zip named `page_scrubber.koplugin-<version>.zip` from the **Assets** section below (not "Source code").
2. Unzip it and copy the `page_scrubber.koplugin` folder into `koreader/plugins/`.
3. Restart KOReader.

To update, replace the folder. To uninstall, delete it (and `koreader/patches/2--page-scrubber-font.lua` if you used the system font).

# v7.7.3 · 2026-10-06

# What's new!

##  Multi Grid: Now you can select 9 pages!
- New option under **Layout → Multi Grid: Show 9 pages**. Shows 9 pages (3x3) instead of 6, with the current page in the center. Works in both portrait and landscape.
- Small visual tweak to the index: added a dithering effect for a nicer look (based on `hatching.lua` from ZenOS).
- Added visual feedback when pressing the `<`, `>` and `X` buttons in Simple UI mode.

##  <-- Library button
The Library button now it redirects you to the path you have asigned as 'Start With' instead of simply going to the file browser. That means: Simple UI Homescreen, Bookshelf, or history... 

## Fixes:

- **Multi Grid and Simple Grid:** CBZ and PDF pages now respect their true size more accurately and no longer shrink or stretch awkwardly to fit the grid.
- The same fix was applied to the 3-page Grid in **Landscape** mode.

## Installation
1. Download the zip named `page_scrubber.koplugin-<version>.zip` from the **Assets** section below (not "Source code").
2. Unzip it and copy the `page_scrubber.koplugin` folder into `koreader/plugins/`.
3. Restart KOReader.

To update, replace the folder. To uninstall, delete it (and `koreader/patches/2--page-scrubber-font.lua` if you used the system font).

# v7.7.2 · 2026-10-04

## Bug Fixes in dictionary 
- Fixed the Highlight button doing nothing in the dictionary pop-up.
- Fixed plugin buttons in the dictionary pop-up (text mode) not receiving the selected text.

## Installation
1. Download the zip named `page_scrubber.koplugin-<version>.zip` from the **Assets** section below (not "Source code").
2. Unzip it and copy the `page_scrubber.koplugin` folder into `koreader/plugins/`.
3. Restart KOReader.

To update, replace the folder. To uninstall, delete it (and `koreader/patches/2--page-scrubber-font.lua` if you used the system font).

# v7.7.1 · 2026-10-03

### Bug Fix
- Fixed a crash when tapping the AI button with AI Assistant v1.18 (thanks @DerailleurAgile, #7).

## Installation
1. Download `page_scrubber.koplugin-vX.Y.Z.zip` from the [latest release](../../releases/latest) (under Assets, not "Source code").
2. Unzip it and copy the `page_scrubber.koplugin` folder into `koreader/plugins/`.
3. Restart KOReader.

To update, replace the folder. To uninstall, delete it (and `koreader/patches/2--page-scrubber-font.lua` if you used the system font).

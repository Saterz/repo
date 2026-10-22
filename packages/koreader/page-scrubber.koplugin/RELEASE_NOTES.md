# v8.2.0 · 2026-10-21

## What's new

### New: Study Mode
- When enabled, a **Study** button appears in the split menu (it can also be opened with a gesture). It lets you study your annotations with the same spaced-repetition method used by apps like Anki: every annotation is a card, and you rate it **Again**, **Good** or **Easy** depending on how hard it was. The easier a card is, the longer it takes to come back in your next session.
- When you finish a session, **Review mode** unlocks: you can browse all your annotations, but without the rating buttons, so your progress is never modified.
- On every card you can **tap the page** to jump straight to that page in the book and read the context. You can also **undo** a card if you rated it wrong.
- **How it works:** it's off by default. You can enable it for all books or only for a specific folder, like School, University or Work.
- The study data of each book lives inside that book's `.sdr` folder.
- You can delete the Study progress of each book from **Settings > Study Mode > Reset Study Progress**.
- All the text in the Study / Review card follows **Settings > Appearance > Text size**.

### New: Custom icons
- Now in **Settings > Appearance > Custom icons**: add your own icons!
- Tap **+** on any SVG, browse your KOReader files to the folder where your icon is, and **long-press** the SVG you want to use.
- You can go back to the original SVG individually, or reset all of them at once.
- Prefer to do it manually? Drop your SVGs in `koreader/settings/page_scrubber/icons/` using exactly the same file names as the plugin's icons (they are case-sensitive), then reopen the scrubber. Your icons are kept when the plugin is updated.

### Settings improvements
- The **Favorite fonts**, **System font** and **Add scrubber action** menus were updated to match the new settings design.
- Settings (and Study mode) can now be used with physical buttons on **non-touch devices**. *Feedback is welcome to check it works as intended.*

### Quick Menu
- Small redesign so everything looks bigger and fits better.
- **New Status Row:** time, Wi-Fi and battery (and a Study mode notification if Study mode is enabled). Enable it in Settings > Quick Menu > Status Row 
- Fixed the frontlight toggle.

### Updated the page scrubber Updater: 
-Now it displays a nice window showing the full patch notes and other changes.

- Updated spanish and Portuguese. 
- **Help translate:** If you'd like to help update the translation into your language, contributions are welcome!

## Installation
1. Download the zip named `page_scrubber.koplugin-<version>.zip` from the **Assets** section below (not "Source code").
2. Unzip it and copy the `page_scrubber.koplugin` folder into `koreader/plugins/`.
3. Restart KOReader.

To update, replace the folder. To uninstall, delete it (and `koreader/patches/2--page-scrubber-font.lua` if you used the system font).

# v8.1.0 · 2026-10-18

## Settings & Split Menu Redesign

### Visual updates
- **Settings menu redesign:** new header with back and close buttons, options grouped into sections, the current value shown on the right of each row, and a cleaner, lighter look.
- **Split menu refresh:** the selected row is now a rounded pill, the pinned row has a softer selected state, the color filter arrows are chevron icons, and page numbers are centered. Landscape got the same changes.
- The book title and chapter name now match the size of the "Library" label, and the selection menu has a thicker outline.

### New book title style: Bar
- Under **Settings > Appearance > Top bar > Book title style** there is a new **Bar** style. It draws the book title on a full-width white bar, vertically centered.
- Turn on **Top bar separator line** together with the **Bar** style and the result looks very similar to the Kindle's own top bar.

### Selection menu
- **New option: Size of selection menu** (Small / Medium / Large) under Settings > Reading Pop-Ups. It scales the icons, the buttons and the outline. Medium is the previous size.

### New: Advanced settings
A new **Advanced** submenu (Settings > Other > Advanced):
- **Settings**
  - **Back up settings:** saves all your PageScrubber options and your favorite images to `page_scrubber_backup.lua` in KOReader's `settings` folder.
  - **Restore settings from backup:** brings back the options and favorite images saved in that file. To restore on another device, copy the file to the same folder first.
  - **Reset all settings:** back to defaults. Asks for confirmation, and also clears your favorite fonts, quick actions and favorite images. Back up first if you want to keep them.
- **Cache**
  - **Clear image cache:** deletes the scan cache of the Images tab (the current size is shown next to it). Your favorite images are kept.
- **Updates**
  - **Check for updates:** looks for a newer release on GitHub, shows its notes and installs it from the reader. It keeps a backup and restores the previous version if the install fails. Restart KOReader when it finishes.

## Installation
1. Download the zip named `page_scrubber.koplugin-<version>.zip` from the **Assets** section below (not "Source code").
2. Unzip it and copy the `page_scrubber.koplugin` folder into `koreader/plugins/`.
3. Restart KOReader.

To update, replace the folder. To uninstall, delete it (and `koreader/patches/2--page-scrubber-font.lua` if you used the system font).

# v8.0.0 · 2026-10-14

## New: Panel View Update

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

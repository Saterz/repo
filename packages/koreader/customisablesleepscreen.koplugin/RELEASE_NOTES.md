# v2.5.0 · 2026-10-11

## New Features

* **Lock screen:** An optional PIN lock that appears after the sleep screen. Tap or swipe to clear the sleep screen after waking, then enter your 4-digit PIN to gain access. It needs Customisable Sleep Screen to be your chosen sleep screen.
   * **Retry limit:** five wrong PINs in a row lock the keypad for 30 seconds, doubling with each further lock-out up to 10 minutes. The count and lock-out are saved, so restarting KOReader doesn't reset them.
   * **Lock when KOReader starts:** also ask for the PIN at launch, so restarting the app or rebooting can't be used to skip the lock.
   * **Deferred locking:** skip the lock when the device has only been asleep for a short time (30 seconds up to 1 hour).
   * **Owner message:** add up to three lines of text under the keypad, such as "If found, call...".
   * **Customisable look:** Ruled, Plain, Filled or Outlined (Filled and Outlined can be a circle or a rounded square). The background can be your sleep screen background, plain white, plain black, or follow automatic preset switching (white for the day preset, black for the night one). Text colour and a backing panel keep it readable over pictures. Night mode is switched off while the lock screen is up, as it is for the sleep screen.
   * **Back to sleep:** the key at the bottom left of the unlock pad puts the device back to sleep.
   * **Delete:** tap the key at the bottom right to delete a digit, or hold it to clear them all. An open padlock shows after a correct PIN.
   * **Forgotten PIN:** create an empty file named `reset-lock` in the plugin folder and restart KOReader to clear it.
   * **Security:** the PIN is stored as a salted hash. The lock screen deters casual access but it isn’t strong security: the files on your device aren’t encrypted or protected. Lock settings aren’t part of presets.
* **Flash screen to reduce ghosting:** now a submenu in Global settings with separate switches for the sleep screen and the PIN pad, and a choice of a black flash or a white flash.
* **Export triggers:** choose when the sleep screen image is exported - on book close, book open, suspend, or periodically. Close and suspend are on by default.
* **Highlights:** choose between highlights from the current book only or from all of your books, and optionally show the highlight's book title and author.
* **Cover drop shadow:** gives the cover image rounded corners and a drop shadow, like a card.
* **White icon outline in dark mode:** adds a thin white outline around each icon, like a sticker, so they stay visible against dark backgrounds. Works with every icon set.
* **Weekly streak:** a new option in the daily goal section that counts consecutive weeks with any reading.
* **Hide every section:** "Section order & visibility" no longer insists that one section stays visible, so you can show only your background.
* **Previews:** a new "Preview file manager sleep screen" at the top of "Sleep screen in file manager", and "Preview sleep screen" now sits below the active preset in the Presets menu (it's no longer in the main menu, and is still at the top of each section).

For installation instructions, see the [README](https://github.com/pxlflux/customisablesleepscreen.koplugin/blob/main/README.md).

# v2.4.0 · 2026-09-22

## New Features
- **Automatic preset switching**: Switch between two presets (e.g. light by day, dark at night) on a fixed schedule or by KOReader's night mode. Includes a "Sync now" button and separate day/night pickers, in the Presets menu. Prevents sleep screen colours from being inverted if KOReader's night mode is enabled.
- **Preview sleep screen**: See what your current settings or any preset will look like from the main menu, without suspending the device. Pinned at the top of each core menu section, or hold-to-preview on any preset.
- **Alternative sleep screen for the file manager**: The file manager can now optionally show a simpler background-only sleep screen (transparent, solid colour, custom image, or random folder image) instead of the regular one, with its own settings that stay fixed regardless of your active preset.
- **Stable page number support**: Sleep screen now also supports stable page numbers when the user has them enabled.
- **Check for updates**: Checks GitHub, downloads and installs new release if available, and runs clean up. Any custom added icons/wallpapers survive updates.
- **Export format improvements**: Sleep screen export now defaults to JPG for faster saves, and a new "Export in greyscale" toggle has been added to reduce file size in case colour isn't needed.
- **Menu rework**: Icons on each headline and reset item; presets now live in their own submenus with individual management instead of bulk hide/delete; some settings moved out of 'Advanced' menu into more logical menus; nested menus added for more items (export, cover exclusion, icons, bars, border, etc.); section visibility and reordering combined into one screen; 'Advanced' renamed to 'Global settings' (since this menu now only covers global parameters), and 'Layout & Spacing' renamed to 'Layout, Spacing & Frame'; Fonts & Text now shows current values inline; several settings (cover alignment, icons, bars, inline bars, auto-switch options) now grey out properly when their parent selection is off.
- **Reworked built-in presets**: 'Default' is now 'Default Day', and 'Night' is now 'Default Night' - with a matching design, and are now the default presets for Automatic preset switching. Additional minor tuning to the other presets.
## Fixes
- Fixed a rare crash on export/power-off from shared buffer tracking.
- Fixed 'Clean chapter titles' missing roman-numeral markers, all-caps titles, and non-breaking spaces.
- Fixed battery time remaining showing manual estimate for non-manual setting, instead of "Data unavailable" when real data isn't available.
- Fixed the colour picker defaulting to 0% brightness on first use, and its +/- buttons getting stuck at the boundaries
- Fixed content parameters not refreshing in menu after reset is performed. Previously needed to exit menu and return.
- Fixed some Global settings items which were silently varying by preset, when they shouldn't have.

For installation instructions, see the [README](https://github.com/pxlflux/customisablesleepscreen.koplugin/blob/main/README.md).

# v2.3.0 · 2026-09-11

## New Features
- **Custom image background** - Added “Custom image” as a background type, letting you use a single image as your sleep screen background (instead of the single image in folder workaround that many users were using).
- **Export image on suspend** - If the export sleep screen to file option is in use, then the sleep screen now additionally exports on device suspend in addition to on book close.
- **Configurable export filename and format** - Choose the filename and file format (PNG, JPG, BMP) used when exporting the sleep screen image. Useful for devices where a specific file name and type is needed e.g. Tolino, Pocketbook etc. Note/ Pocketbook caches images, so even though the file is changed, a reboot may be needed to see the new image.
- **Anti-ghosting flash** - Optionally flashes the screen to black just before showing the sleep screen, clearing faint ghosting some e-ink devices show from text/images. Off by default since not every device is affected.
- **Exclude a book’s cover from the sleep screen** - Per book option to hide a specific book’s cover (similar to the coverimage plugin option). Handy if you read multiple books simultaneously but don’t want to change or forget to change the sleep screen preset, and you’d rather have certain covers hidden.
- **Independent clock and date on battery section** - ‘Show clock’ and ‘Show date’ are now separate toggles, and no longer on the title line. You can now show either, both or hide the clock and date if you’d rather not see them (since it’s static data at the time of sleep screen generation).
- **Show/hide percentages on book, chapter and goal sections** - Hide the percentage labels if you’d rather they not be visible.
- **WebP support** - Background images now support WebP in addition to PNG and JPG.
- **Additional language support** - language support added for Hungarian, European Portuguese (pt_PT) and Ukrainian.

## Fixes
- Fixed chapter section data (title, chapter number, chapter page count) being incorrect when Hidden flows feature was in use.
- Fixed incorrect “Minimal” and “Night” preset layout positioning.
- Removed the “Show titles”, “Show subtitles” options - deemed unnecessary since subtitles items can be toggled in their content menus, and title line information should always remain.
- Fixed broken .pot and .po strings for hr/hrs, min/mins and page/pages.

Thanks to the community for your contributions.

For installation instructions, see the [README](https://github.com/pxlflux/customisablesleepscreen.koplugin/blob/main/README.md).

# v2.2.0 · 2026-05-09

## New Features

* **Sleep screen image export** - Saves the generated sleep screen as an image when closing a book. Android users can then use the image with their device's screensaver feature. Also useful for sharing setups.
* **Rounded corners** - Configurable corner radius on the infobox, from small rounding to full pill shape.
* **Inline progress bars** - Progress bars can now sit within the text column rather than spanning the full section width.
* **Cover image in book section** - Add your book cover inline with reading stats as an alternative to the full background option.
* **Infobox layout tweaks** - Added an offset option to move the infobox slightly off-screen (useful for rounded corners), and per-side padding control.
* **Spin widgets** - All numeric settings now use spin widgets for precise control over values.
* **Hide message section header** - The message section title can now be hidden.

## Fixes

* Bold titles now apply to all section titles, not just the book title.
* Daily goal reset time and week start now follow KOReader's own reading statistics settings.
* Background folder picker defaults to classic file view and allows full directory navigation.
* Removed compiled language files, only `.po` source files are now used. Turkish po added.
* Plugin settings now moved out from `settings.reader.lua` and stored in two files within `koreader/settings`.
* Updated to support settings removal with KOReader’s new feature for on-device plugin removal (currently in the nightly builds).
* Replaced `Terminal` preset option with `Capsule` preset as shown in the screenshot.
* Renamed several Lua files to avoid potential filename conflicts.

For installation instructions, see the [README](https://github.com/pxlflux/customisablesleepscreen.koplugin/blob/main/README.md).

# v2.1.0 · 2026-04-08

This release fixes reported issues from v2 and adds user suggested features. 
## New Features
- **Time-based goal type.** Users can now choose between page/time goal. Pages read today has been moved to the section title line, which can be set to display pages read, time read, or both.
- **Orientation lock.** Force the sleep screen into portrait/landscape independent of the book’s orientation. Option added to advanced menu.
- **Cover image alignment.** If stretch to fill is disabled, the book cover can now be aligned left, centre or right. Also, the letterbox fill can now be any user-chosen colour.
- **Custom quote option** added to the message section. Quotes are saved in `custom_quotes.lua` for easy editing.
- **Series display option.** Enable series name (and series # if available) in the book section.
- **Hidden flow support.** Book time remaining, page numbers and percentage read now work with hidden flow (if activated).
## Fixes
- **Expanded document format support.** Fixed a crash when using plugin with `cbz` or `pdf` files. These often lack chapter metadata, so it’s recommended to disable the chapter section when reading these formats (chose not to program this to be disabled outright on the off-chance that they contain chapter information).
- **Power off stability.** Fixed a crash when powering down from within KOReader. Sleep screen will now also correctly remain as the last image on display when powered off.
- **Silent failure fix.**  If the plugin is opened from the file manager before being run in a book, it will now show a notification explaining why nothing is displayed, rather than silently not loading.
- **Plugin version metadata fix.** Fixed a crash where plugins version metadata was being read incorrectly by other plugins.
- **File manager sleep screen update.** Sleep screen contents are now updated on book closure, so the file manager sleep screen always shows the most up-to-date information.
- **Comic icons updated.** Jpeg icons changed to svgs so they can be recoloured with progress bar colours. The comic preset has been updated to use new features and is now suited for reading comics in landscape.
- **Menu and display adjustments.** Section gap options moved into a submenu, standardised section names and slightly modified goal section strings.

For installation instructions, see the [README](https://github.com/pxlflux/customisablesleepscreen.koplugin/blob/main/README.md).

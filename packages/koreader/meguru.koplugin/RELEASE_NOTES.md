# v1.6.0 · 2026-10-16

## New features

- **Settings are shared across a series** — a menu row you change applies to every book in it. Turn off *Remember settings for this series* to stop the sharing.
- **Panel rotation has three states**: No rotate / Rotate / Autorotate, remembered across books.
- **Hardware Dithering row** on devices whose screen controller can dither. It replaces the software row there, and starts from the device's own setting.
- **Full refresh on every page turn**, for Meguru only.
- **Crop recognises more margins**: paper, drawn frames, and bars down a side.
- **The letterbox is painted in the margin that was trimmed**.
- **Book info names the OPDS catalog** when it differs from the server.

## Improvements

- **Decode budget raised to 10 Mpx.**
- **Resuming a book no longer decodes page 1.**
- **The panel view warms the next page's crop, panels and first tile.**
- **Panel detection no longer copies the page.**
- **The pair offset gesture action is named *Meguru: …* and is offered only while a Meguru book is open.**
- **Menu regrouped**: server rows are now under **OPDS**.

## Bug fixes

- Fixed the margin colour around the first page of a book.
- Fixed a catalog that changed server being remembered as the old one.
- Fixed an error when a local `.cbz` is opened for the first time.

**Full Changelog**: https://github.com/Craftwork2720/meguru/compare/v1.5.4...v1.6.0

# v1.5.4 · 2026-10-11

## Bug fixes

- **Kavita: chapters are no longer skipped.** ([#5](https://github.com/Craftwork2720/meguru/issues/5)).
- **Komga: series covers now use the full-size image**.

**Full Changelog**: https://github.com/Craftwork2720/meguru/compare/v1.5.3...v1.5.4

# v1.5.3 · 2026-10-10

## Bug fixes

- **No more crash on Android while the file browser builds covers.** Opening a folder of local `.cbz` files or `.meguru` streams could close the app: KOReader builds covers in a background process, and that process was asking Android two questions only the main one may ask — the answer it got was an abort. Both are gone; those answers are now taken in the main process ([#4](https://github.com/Craftwork2720/meguru/issues/4))
- Everything else is untouched: reading, panel view, two-page view and streaming are unchanged, and covers outside Android are fetched exactly as before

**Full Changelog**: https://github.com/Craftwork2720/meguru/compare/v1.5.2...v1.5.3

# v1.5.2 · 2026-10-10

# New features

- **Derainbow** — removes the rainbow shimmer on colour e-ink screens. All credit goes to [Euphoriyy](https://github.com/Euphoriyy) and his [derainbowify.koplugin](https://github.com/Euphoriyy/derainbowify.koplugin). Off by default, shown only on colour screens
- **Show in OPDS** — opens the OPDS browser on the book's series, from its Info popup or the on hold **file** menu (.meguru)
- **ComicInfo.xml switch** — Settings → *Read metadata from ComicInfo.xml*. On by default; off = local `.cbz` titled by file name

**Full Changelog**: https://github.com/Craftwork2720/meguru/compare/v1.4.0...v1.5.2

# v1.4.0 · 2026-10-03

## New features

- **Two-page view**: shows two pages at once as a spread (off / landscape only / always, set per book). Wide pages are shown alone and the pairing restarts after them, so spreads never get cut in half
- **Pair offset**: lets you shift which pages get paired, for books where the pairing is off by one page. Can also be bound to a gesture
- **Flexible gutter**: brings back as much of the trimmed inner margin as fits between the two pages, without exceeding what the original page had
- **Bottom menu reorganized** into 4 tabs: Reading, Page, Rotation, Tone — plus an Info button showing current page, progress, and book metadata (with full description in its own popup)

## Improvements

- Shorter pages in a pair are now scaled up to fill the space, so mismatched page heights no longer leave blank space
- Panel cropping is now flush on all sides, and keeps a background frame on dark pages
- Slanted-border panels are now cropped along their actual border instead of the first detected line
- Menu rows renamed to match what they do: *Crop*, *Reading direction*, *Pair offset*, *Panel view*, *View mode* (now under *Fit*), and *Tone* has its own tab again
- Left/right arrows now navigate panel views in the book's own reading direction

## Bug fixes

- Fixed an issue where opening a book would request a page before the first one, causing a failed fetch (HTTP 400)
- Page numbers touching the edge of the artwork are now cropped correctly again
- Fixed a visual glitch where switching crop from off to auto briefly showed the old margin color

**Full Changelog**: https://github.com/Craftwork2720/meguru/compare/v1.3.0...v1.4.0

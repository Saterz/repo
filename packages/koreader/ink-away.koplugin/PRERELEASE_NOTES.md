# v4.1.0 · 2026-10-11

**This is a prerelease.** To get it from inside Ink Away, turn on Settings, Updates, "Tell me about prereleases", then install it from there. Or download `ink-away.koplugin-v4.1.0.zip` below and put the `ink-away.koplugin` folder in KOReader's plugins folder. You can go back to the latest release from Settings, Updates at any time.

A text tool update, with fixes for colour readers and the Kindle Scribe. A
prerelease, as most of it could only be tested in the emulator: reports from
colour and pen readers are very welcome.

## Added
- Text boxes turn to any angle. While a box is open, drag the ring on the stem
  above it round its middle; it snaps to quarter turns. A box picked out with
  a hold or the lasso turns with the selection's handle and its quarter turn
  button too. A turned box is edited turned, with the caret, selection and
  grips following its lines, and pages, thumbnails and exports show it the
  same. The eraser and taps find it where it is drawn.
- Text colours. On a colour screen a word or a selection can be coloured
  (black, two greys, red, orange, green, blue, purple and up to three colours
  of your own from the colour wheel); a grey screen offers the greys.
- Highlight colours. Text highlights come in yellow (the default, which
  highlights made before take too), orange, blue, green and pink, plus up to
  three of your own; hold one you added to remove it. A grey screen keeps
  its grey, and on a dark paper a highlight is toned down so white letters
  read on it. Exports show the colours as the screen does.
- The Format sheet has tabs: Text (styles, size, colour, highlight and Plain
  to clear them), Paragraph (alignment, lists, line spacing, direction and the
  font) and Edit (copy, cut, paste, select all and today's date).
- Alignment: left, centre or right, for each box.
- Line spacing: tight, normal or loose, for each box.
- Reads down and Reads up turn a box on end, for a book's margins: a new box
  stands where it was tapped, an older one where it shows, and a line too
  long for the page there is shortened.
- The book annotation toolbar can fit in the book's margin: "Fit the toolbar
  in the margin" in Book ink settings (off by default) makes it as wide as
  the margin on its side, with its icons sized to it, so it stays clear of the
  text. It stays thick enough to tap, so a narrow margin needs widening in the
  reader's settings; PDFs and comics keep the usual toolbar.
- Checklists: a list with a box before each line. Tap a box to tick it, with
  the text open or closed (one undo step); a ticked item greys out.
- A second tap on a word in the text being written selects it, and the
  keyboard stays to type over it.

## Changed
- The Format sheet stays open while you pick options, so several can follow
  one another; Done, Format or a tap outside brings the keyboard back. The
  font can be changed there too, so it is at hand over a book while writing.
- A text box's grips are sized for a finger: about 9 mm to hit on any reader,
  just outside its corners so a tap near a letter still places the caret, and
  always whole on the screen. Dragging the band around the frame moves the box
  too.
- A tap away from a text box only closes it. It used to start a new box where
  you tapped and bring the keyboard straight back; a tap on another box still
  opens that one.

## Fixed
- On colour e-ink (Kobo Libra Colour and others) a shape being dragged out no
  longer falls behind the pen. Each move asked the screen to redraw the whole
  shape's box, and the screen queued every one of them; now each new outline
  waits for the last to show, so it stays with the pen at any size.
- On a Kindle Scribe a hand resting on the screen could draw lines, or keep the
  pen from drawing, until a stroke or two were written with the hand lifted.
  When the touch screen took the edge of the hand for a pen, Ink Away took it
  for the real pen. Only the pen's own digitizer is the pen now, and a hand on
  the screen while the side button is held is never taken for it either.
- A pen stroke that starts on a floating button (zoom, Pan, the toolbar's
  chevron, the pen or layer strip) is drawn instead of lost. A pen that lifts
  within about 1.3 mm of where it landed, and within KOReader's hold time,
  still presses the button.
- On colour e-ink, moving, resizing or turning a text box and dragging out the
  export area keep up with the finger, as shapes now do: each refresh waits
  for the panel to show the last.
- With "Erase whole strokes" on, the eraser takes a text box it touches unless
  text is protected, and a picture when "Erase pictures" is on. It used to
  leave both alone whatever the settings said. As with a filled shape, rubbing
  out writing on top of one keeps it. "Protect text from eraser" is in the
  Eraser's sheet now as well as the Text sheet.

# v3.1.3 · 2026-09-27

Prerelease rolling up **everything since 3.1.0** (3.1.1 and 3.1.2 were prereleases), with a major focus on making landscape fast and correct.

## New
- **Landscape orientation.** Draw with the device held sideways; Ink Away remembers the choice and reopens the same way. A landscape session gets a wide canvas, and its PNG / JPEG / PDF export comes out landscape automatically.
- **Background remover for images.** First-pass remover that flood-fills from the edges, so a photo's subject stays solid while the surrounding background drops out.

## Landscape performance (the big rework)
On e-ink readers that render landscape by rotating the framebuffer in software, drawing and menus used to lag. Landscape is now rebuilt to be as responsive as portrait:
- Panel-order rendering — the canvas is scaled and copied through the screen's native pixel order (a memcpy) instead of a per-pixel rotated copy on every frame.
- The master bitmap is mirrored in panel order, so pan / zoom / redraw never re-rotate the whole screen.
- Shape commits re-render only the shape's rectangle, not the whole drawing area.
- The floating zoom control is cached as a sprite instead of being redrawn every frame; toolbar chrome isn't repainted mid-stroke or mid-drag.

## Settings & grid
- Grid type, size and opacity moved into their own grid sub-sheet, so the settings sheet fits with no scrolling (no more nudging a slider by accident).
- Fixed grid-on drawing slowness (the grid is clipped to the changed region while you draw).

## Reliability
- Reopening Ink Away can no longer stack a second canvas over an old one (which had made the app get slower until a restart); reopening recovers cleanly.
- Notebook shape clipping on rotation fixed; text stays put across rotation.
- Online image browser: fixed a tap-to-add crash and re-searching without the keyboard getting trapped.
- Memory backstops so long sessions don't degrade.

## Known issue
- Very heavy, prolonged switching between portrait and landscape *while drawing* can gradually reduce responsiveness until KOReader is restarted. Normal use is unaffected; a fix is still being investigated.

# v3.1.2 · 2026-09-26

Faster landscape, a tidier settings menu, and a pen-input test to help track down stylus problems.

* Landscape drawing and repaints are noticeably faster.
* The settings menu is tidied up so it fits without scrolling — all the grid options (type, size, opacity) now live together in one Grid panel.
* The grid no longer slows drawing: turning it on, even at a small size, keeps drawing as smooth as with it off.
* New pen-input test in the gear menu, for stylus users: it shows exactly what your pen and palm report to the device. If you're on a stylus device and seeing stray dots or lines under your palm, please run it and send me what it shows — it lets me look into palm rejection on devices I can't test myself.

Prerelease — please try it on your device and let me know how it holds up, especially the pen-input test on stylus devices.

# v3.1.1 · 2026-09-26

Landscape mode, plus a few fixes.

- Portrait or landscape — set it in the gear menu, or just open Ink Away with your device turned. It remembers which way you left it, and the page (and your PNG/JPEG/PDF exports) come out in that orientation.
- Background remover for added images (early version): pick an image in Pan mode and tap Remove background to cut a plain/solid background out to transparent.
- Fixed a crash when tapping (instead of long-pressing) an image in the online image browser.
- Fixed editing your search term in the online image browser — it now keeps what you typed so you can change it.

Prerelease — please try landscape and the background remover on your device and let me know how they hold up.

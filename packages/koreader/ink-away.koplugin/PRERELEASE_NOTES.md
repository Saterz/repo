# v4.1.1 · 2026-10-16

**This is a prerelease.** To get it from inside Ink Away, turn on Settings, Updates, "Tell me about prereleases", then install it from there. Or download `ink-away.koplugin-v4.1.1.zip` below and put the `ink-away.koplugin` folder in KOReader's plugins folder. You can go back to the latest release from Settings, Updates at any time.

Notebooks and drawings on Bookshelf shelves with drawings in twelve frames,
pen pressure as a setting that starts off and a round of pen and page fixes.
A prerelease, as the pen and colour fixes could only be tested in the
emulator: reports from pen and colour readers are very welcome.

## Added
- Go to the contents page: in the page menu of a notebook that has one, and
  as an action for any gesture or page turn button, with Back to return.
  The guide now says how links are followed: a tap with Pan, or with a
  finger while palm rejection is on, on ink, shapes and pictures alike.
- On colour screens ink keeps its colour in KOReader's night mode: blue
  stays blue instead of turning yellow, and dark ink turns light so it reads
  on the dark page. Keep colours in night mode in Settings turns it off.
- In annotation mode the eraser takes away the highlights it crosses, as it
  does ink, in one undo step with whatever ink it cut. A long press on a
  highlight (with a finger while palm rejection is on, or with the lasso)
  offers to remove it. Until now a highlight could only go from KOReader's
  own menu once Ink Away was closed.
- The reader's page turn buttons work in Ink Away: they turn a notebook's
  pages, and the book's in annotation mode, where they did nothing before.
  Gestures and pen buttons can give them another action.
- Refresh the screen by hand: a long two-finger swipe down redraws the whole
  screen with a full refresh, so anything a quick refresh missed shows and
  the faint marks of fast drawing go. Any gesture can be set to it in
  Gestures and pen buttons, and Settings has a Refresh the screen button,
  in annotation mode too.
- The first time a finger drags on the page with palm rejection on, a note
  says why it doesn't draw: the pen draws and a finger moves the page, and
  palm rejection is in the pen menu, Pen and input. It shows once.
- Notebooks on a Bookshelf shelf. With the Bookshelf plugin installed, a
  shelf can show "Ink Away notebooks": a new shelf shows every notebook's
  cover front facing, and a tap opens it in Ink Away. Without Bookshelf
  nothing changes.
- Six cover styles for the shelf: Front page (the notebook's first page, with
  a spiral and its name on a coloured band), Hardcover, Composition book,
  Reporter pad, Kraft with window and Legal pad. The first time, your
  notebooks get a mix of all six, so you see what there is. A long press on a
  notebook on the shelf picks its style and colour, which follows its tab
  colour until you pick another; "Cover on the shelf" in a notebook's menu in
  the library does the same, and "Covers on Bookshelf" in Ink Away's settings
  sets the style new notebooks start with. A notebook keeps its cover through
  renames, moves and the trash.
- Covers are quick and never draw your strokes again. The first page on a
  cover is a picture Ink Away keeps of it as you close the notebook or turn
  from that page, only when it changed; writing on any other page leaves the
  cover alone. A notebook not opened since has its first page drawn once in
  the background, small and only while no notebook or book is open. The long
  press sheet opens at once, also for a notebook with smudges.
- Drawings on a Bookshelf shelf. A shelf can show "Ink Away drawings": each
  drawing hangs face out in a frame, and a tap opens it in Ink Away. There
  are twelve frames, from old to modern: Gilded Baroque, Louis XVI, Dutch
  Ripple, Carved Victorian, Arts and Crafts, Art Deco, Museum Mat, Floating
  Frame, Minimal Metal, Painted Box, Canvas Wrap and Instant Photo, each in a
  few finishes (gold, antique gold or silver gilt, oak or walnut, and so on).
  A new drawing gets a frame and finish at random, all twelve before any
  comes again. A long press on a drawing on the shelf picks its frame and
  finish, as does "Frame on the shelf" in a drawing's menu in the library.
  A drawing keeps its frame through renames and moves.
- The frames are as quick as the notebooks' covers: each was carved and lit
  once ahead of time and comes as small pieces that are fitted round the
  drawing, so a cover takes moments and the frame fits any drawing's shape.
  The drawing on a cover is a picture Ink Away keeps as you close it, only
  when it changed. With Bookshelf's "True cover aspect" on, the frame hugs
  the drawing in its own shape; with it off (Bookshelf's default, which shows
  every cover 2:3) the drawing fills a 2:3 frame, trimmed a little at its
  sides, so it is never stretched.

## Changed
- Pen pressure is now "Pen pressure (Beta)" in Pen and input, and starts off,
  also on readers that had it on. It shows on readers with a pen: the Kindle
  Scribe and the Kobo Elipsa, Sage, Elipsa 2E and Libra Colour. Another reader
  shows it once Ink Away has seen a pen on it. It works with Palm rejection
  on. While it is off the pen's pressure is not read at all: Pencil and
  Calligraphy keep an even width, and Ballpoint and Fountain follow your
  writing speed, as they do with a finger.

## Fixed
- A page with smudges could take ten times longer to open after an export or
  after Bookshelf covers were drawn: the smudge's drawing was left running
  slowly. It now runs at full speed whatever was drawn before.
- With "Fit the toolbar in the margin" on, the book's toolbar ended right
  where the text began. It now leaves a little space before the text.
- With the screen turned upside down (a Kobo Libra Colour held with its
  buttons on the left, for one) the page under Ink Away was dark: strokes
  showed as white boxes and the eraser drew white, over a book and in
  drawings alike. The page shows as it does the right way up.
- A page added to a book's notes named the notebook in the strip above it
  instead of its chapter, so it looked like another notebook had opened. It
  names the chapter it belongs to now.
- Opening a book's notes in a new chapter, adding a page and writing only on
  that one moved the notes to the chapter before when the notes closed, and
  the chapter opened on an empty page the next time. The chapter's page now
  stays when a page after it has notes, and goes with the empty pages after
  it when they are all left empty.
- On a pen reader a tap with the lasso did nothing (or said "Nothing inside
  the loop"), so what was cut or copied could not be pasted and a picture,
  shape or text box could not be picked out with a tap. A tap with the pen
  now does what a finger's tap does.
- A tool menu dragged out of the way went back to where it opens as soon as
  an option was picked in it, and a menu opened from it (Pen type, the colour
  wheel, a font) opened in the usual place too. Both now stay where the menu
  was dragged, kept whole on the screen; a menu opened later starts in its
  usual place.
- Over a book, Pen after the highlighter and another tool (the eraser, say)
  gave the highlighter back. It gives back the pen you had before the
  highlighter.
- On Android readers (a Boox, for one) "Nothing to undo" could start showing
  on every tap, with a finger or the pen, until Ink Away was closed. When the
  system took a touch away in the middle of a stroke, Ink Away later handed
  KOReader a finger that was no longer there, so every tap after it read as a
  two finger tap, which is Undo. A touch the system takes away now goes for
  Ink Away too.
- A shape being dragged out with a lowered opacity, or in a pale colour,
  showed a broken outline or none at all until a menu opened: the quick
  refresh that keeps the outline up with the pen shows only black and white.
  The outline is now drawn in the page's ink while it is dragged, and the
  shape takes its colour and opacity when it is placed.
- On colour e-ink a grey pen did not show while writing: the quick refresh
  used for live ink shows only black and white, and a grey has no colour to
  show. It now writes in the page's ink and turns grey when the pen lifts, as
  every pen does with "Colour while drawing" off, which on a dark paper now
  writes in white instead of black.
- Ballpoint and Fountain lines no longer turn thin when the pen lifts. A
  straight stroke is kept as its two ends, and its tapered ends' thinness was
  drawn all along it on the page, in thumbnails and in exports, so the width
  you pressed disappeared. Notes written before show at their proper width.
- Each lift of the pen drew the whole stroke again from its saved copy with
  the Ballpoint, Fountain and Calligraphy, and with the Pencil when pressure
  was on, which could make writing lag on a Kindle Scribe (with the Pencil it
  took about twenty times the rest of the lift). A lift now draws only what it
  changes: the thinning end of a Ballpoint or Fountain stroke, and nothing for
  the others. That end now shows on the screen at once; it often waited for
  the page's next full redraw before. A page full of Ballpoint or Fountain
  writing draws faster too.
- On a Kindle Scribe the ink could fall seconds behind the pen, and letters
  written quickly came out straightened. Ink Away asked the screen for a
  refresh at every point the pen reported, more than the Scribe's display can
  show, so the requests queued up. The live ink is now shown at a steady pace
  of up to fifty refreshes a second, as on colour readers.
- On a Kobo Sage or Elipsa the ink showed as scattered dots and dashes while
  writing, and the whole strokes only appeared when the screen was redrawn
  (closing the toolbar, say). Their display drops many of the tiny updates
  sent at every point of the pen. The live ink is now shown at a steady pace
  there too, and each stroke is shown whole once more as the pen lifts. Black
  ink is shown then in the same quick mode it was drawn with, so the screen is
  free sooner for the next letter.
- Closing Ink Away took the pen away from whatever had it before: another
  plugin that draws with the pen lost it until it was opened again, and with
  two Ink Away windows open (a book's notes and its annotation), closing one
  left the other without palm rejection, so the hand drew lines. Closing a
  window now gives the pen back to the one under it, or to the plugin that
  had it.
- On a Kobo the pen's eraser end highlighted and its side button did nothing,
  whatever Gestures and pen buttons said: Ink Away read a Kobo pen's buttons
  as a Kindle Scribe's. The eraser end now erases and the side button
  highlights, each as set in Gestures and pen buttons, also with
  pencil.koplugin's input.lua installed. The setting for a second side
  button is gone, as no Kobo or Kindle pen has one.
- On a Kindle Scribe with pencil.koplugin's input.lua installed, the pen's
  side button did nothing. It does what Gestures and pen buttons says again.
- On Android readers (a Boox, for one) the pen's eraser end was ignored until
  the pen had drawn once, taken for a resting hand. It erases from the first
  touch now, with KOReader 2026.08 or later. The pen's side button still
  can't work there: KOReader doesn't pass it on to plugins on Android.

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

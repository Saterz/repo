# v4.2.0 · 2026-10-16

Ink Away 4.2.0 is the stable release of everything since 4.0.1: the 4.1.0 and 4.1.1 prereleases, now tested on a Kobo Libra Colour and a Kindle Scribe, plus coloured library folders, typing on a physical keyboard and fixes for the book toolbar and the Scribe's pen.

Highlights:
- Notebooks and drawings on [Bookshelf](https://github.com/AndyHazz/bookshelf.koplugin) shelves, with six notebook covers and twelve picture frames.
- Library folders in twelve colours, with an icon from your KOReader.
- Type into text boxes on a Bluetooth or USB keyboard.
- Text boxes at any angle, text and highlight colours, checklists, alignment and line spacing.
- The book toolbar can fit in the margin, the reader's page turn buttons work, and the eraser takes away highlights.
- Pen pressure as a Beta setting, and a long list of pen fixes for the Kindle Scribe, Kobo Libra Colour, Sage and Elipsa, and Android readers.

To update from inside Ink Away: Settings, Updates, Install. Or download `ink-away.koplugin-v4.2.0.zip` below and put the `ink-away.koplugin` folder in KOReader's plugins folder.

## Added
- Library folders in colour: hold a folder for Colour and icon, then pick one
  of twelve colours and, if you like, an icon for its front. The icons are
  the ones in your KOReader: its own, Ink Away's, and any SVG or PNG you put
  in the koreader/icons folder. The look is kept in the library, so updates
  leave it alone, and each folder is drawn once, so the library opens as fast
  as before. Renamed and moved folders keep their look.
- Typing on a physical keyboard: a Bluetooth or USB keyboard that KOReader has
  set up types into text boxes, with Shift, Caps Lock, Backspace, Delete, the
  arrows, Home and End, Enter for a new line and Esc to finish the box. Ctrl+Z
  and Ctrl+Y undo and redo, Ctrl+A selects all and Ctrl+C, Ctrl+X and Ctrl+V
  copy, cut and paste. When KOReader counts the keyboard, the on-screen one
  stays away, as in KOReader's own text fields.
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
- Pen pressure is now "Pen pressure (Beta)" in Pen and input, and starts off,
  also on readers that had it on. It shows on readers with a pen: the Kindle
  Scribe and the Kobo Elipsa, Sage, Elipsa 2E and Libra Colour. Another reader
  shows it once Ink Away has seen a pen on it. It works with Palm rejection
  on. While it is off the pen's pressure is not read at all: Pencil and
  Calligraphy keep an even width, and Ballpoint and Fountain follow your
  writing speed, as they do with a finger.
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
- Over a book, the tab that hides the toolbar covered the start of the text
  beside it. It now sits in its own space at the end of the toolbar.
- Over a book with the toolbar along the bottom, a tool's settings opened at
  the top of the screen. They now open just above the toolbar, as they open
  beside it on the other sides.
- On the Kindle Scribe a resting palm took the pen again once a book had been
  opened, until KOReader was restarted: the pen stopped being recognised near
  the hand and drew stray lines. Opening a book, the reader sleeping or some
  popups pause KOReader's input, and after that Ink Away no longer kept the pen
  and the palm apart. It now does, whatever came before.
- On KOReader 2026.07.1 and later, a touch panel that also reports a resting
  hand as a single point can no longer move or lift the pen.
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

Full changelog: https://github.com/EmirErtorer/ink-away.koplugin/blob/main/CHANGELOG.md

# v4.0.1 · 2026-10-10

**Updating:** on 4.0.0, open Settings, Updates in Ink Away and install it from there. On 3.3.0 or older, download `ink-away.koplugin-v4.0.1.zip` below and put the `ink-away.koplugin` folder in KOReader's plugins folder, as before.

Two fixes for pen and colour readers.

## Fixed
- With palm rejection on (the default on pen readers), a text box's Done and
  Format buttons answered neither the pen nor a finger, so the keyboard could
  not be closed. Both work now, and a finger tapping away closes the box.
- Colour ink on colour e-ink settles to its true colour once the pen rests.
  Pale colours such as pink could stay invisible, and blue could stay cyan,
  until something else redrew the page.

# v4.0.0 · 2026-10-10

**Updating from 3.3.0 or older:** download `ink-away.koplugin-v4.0.0.zip` below and put the `ink-away.koplugin` folder in KOReader's plugins folder, as before. From 4.0.0 on, Ink Away can update itself: Settings, Updates.

The biggest update yet: write on your books, a whole new set of pens, layers,
dark mode, paper colours, a guide and updates from inside Ink Away.

## Added

#### Write on your books
- Annotate any book KOReader opens (EPUB, MOBI, FB2, PDF, DjVu, CBZ and more):
  pen, eraser, shapes, text and pictures right on the page.
- Ink follows the text: on a reflowing book each stroke is anchored to the words
  it was written beside, so it stays with them when you change the font size,
  margins or orientation. On PDFs and comics it keeps its place on the page.
- Smart highlighter: a highlighter stroke over text becomes KOReader's own
  highlight, in the pen's colour, and shows in your highlights list. Strokes that
  run into the margin, wobble or cross lines still snap; over empty space it
  stays ink.
- Book notes: a notebook for each book, with a page per chapter, in a window
  over the page that expands to full screen.
- The annotation toolbar can sit on any side of the screen and folds away.
- Erasing over a book cuts strokes where you rub; "Erase whole strokes" brings
  the old eraser back.
- Annotations live beside the book's own KOReader data and follow the book when
  it is moved or renamed. KOReader's Reset keeps them; deleting a book, or
  "Delete all annotations on this book", puts them in the trash for 30 days.
- The book gestures are set up for you (swipe up or down the right edge, or
  two-finger swipes when those are taken), with a notice saying which you got.

#### Pens
- Pen pressure on pen readers (Kindle Scribe, Kobo stylus): the line follows
  how hard you press. Switch it in Pen and input.
- New pens: Ballpoint, Fountain and Calligraphy (with its own nib angle).
- See-through pens that blend with the page: Highlighter (text stays black on
  top), Marker and Watercolor.
- Smudge, which moves ink (and only ink) and mixes colours the way paint does.
- A compact pen case: up to 20 saved pens, each shown at its real size, "+" for
  a new pen of any kind, and hold to move, copy or remove one. New readers start
  with Fineliner, Ballpoint, Pencil, Calligraphy, Highlighter, Watercolor and
  Smudge.
- A floating pen strip with your first saved pens, and the pen's colour under
  the Pen button.

#### Layers
- Drawings can be drawn in layers, up to five. File, Layers turns them on, and
  what is drawn so far becomes the first layer.
- A small strip at the right, shown only while layers are on, adds a layer and
  picks the one to draw on; tap that one to show or hide it, rename, move,
  merge down or delete it. Turning layers off merges them into one drawing.
- Only the layer you draw on is touched: the lasso, both erasers and the paint
  bucket leave the others alone, and the eraser shows the layers under it as
  it goes. A stroke under other layers stays under them while it is drawn.
- Hidden layers are left out of exports and thumbnails.
- No layer is kept as a picture of its own, so drawing stays as fast as on a
  plain page.

#### Gestures and pen buttons
- Choose what each gesture and pen button does, from one list of actions, with
  a warning when two would clash.
- By default, holding the pen's side button turns it into a highlighter.

#### Look
- Dark mode for Ink Away's toolbars, menus and library: Light, Dark or
  following KOReader's night mode. Your page and colours are never changed.
- Paper colours: twelve papers on colour screens (cream, sandpaper, legal pad,
  kraft, blueprint, chalkboard and more) and white or black on grey ones. The
  ruling and grid take the paper's shade so they always show, black ink and text
  turn white on a dark paper, and exports come out on the same paper.

#### Help
- A guide: short cards on what a glance doesn't show, by topic, each with
  "Show me".
- A notice the first time Ink Away opens, with the book gestures you got.
- Test pen and touch, in Settings: shows how your pen, its buttons and your hand
  arrive, handy for bug reports.
- Check for updates: Settings, Updates shows the latest release and, apart from
  it, any newer prerelease, with their notes, and installs them after checking
  the download. Once a day, only on Wi-Fi that is already on, Ink Away looks by
  itself and puts a dot on the Settings button when there is something new. You
  can always go from a prerelease back to the latest release, never to an older
  one.

#### Android and Boox
- On a Boox, Ink Away asks the screen for its fast refresh while you draw.
- On Android readers whose pen KOReader still reports as a finger (before
  KOReader 2026.08), the pen draws again instead of scrolling the page, and a
  tip explains slow drawing on readers that need a setting changed.

## Changed
- Settings are tidier: pen settings live in Pen and input, every setting is in
  one place, and Settings fits a Paperwhite without scrolling.
- Watercolor is smoother and three times faster.
- See-through pens on grey e-ink refresh only what changed as you draw.

## Removed
- Acrylic and Stipple are no longer in the pen picker (drawings that use them
  still show them).

## Fixed
- A stroke ends exactly where the pen lifted (it could stop short).
- A quick drag on a slider no longer moves the whole menu.

## For developers
- The code passes luacheck, and the tests (about 3,800 checks, many on
  KOReader's real drawing, zip and network code) run on every push.

# v3.3.0 · 2026-10-05

The biggest update so far: Ink Away is now a proper notebook app, with a library, a binder-style browser, search, a trash, links and a contents page, and handwriting you can turn into text on the device.

## Your notes, organized
- No more Save button: every drawing and notebook is its own file and saves itself as you go. The File menu has rename, duplicate, export and new.
- A library with folders (and folders inside folders), thumbnails and + Drawing / + Notebook / + Folder buttons. Rename, move, duplicate or delete without a computer.
- Browse: a folder's notebooks as colored tabs beside their pages, like a binder. Star pages, filter by stars, move or copy pages between notebooks.
- Search by name, or inside pages for typed text, converted handwriting included. Results are remembered, so the next search is instant.
- A trash: deleted notebooks, drawings, folders and pages wait 30 days and come back exactly where they were.
- Choose what Ink Away opens on: the last document, the library or your notebooks.
- Old drawing and notebook project folders move into the library on their own.

## Notebooks
- Pages can have titles, stars and their own paper.
- New papers with previews: blank, lined, grid, dotted, isometric, margin ruled and Cornell, plus planners (handwriting practice, checklist, two columns, storyboard, music, daily, weekly, week columns, monthly, meeting notes, habit tracker).
- Save a page as a template and start new pages from it.
- Links: link anything to a page in this or another notebook; tap to jump, Back to return.
- Contents page: built from your titled pages in one tap, every line a link, updated whenever you like.
- PDF export: titled pages become bookmarks, links keep working, and a whole folder can be exported as one PDF.
- Drawings can include their grid when exported.

## Writing and editing
- Convert to text: lasso printed handwriting and it becomes a text box, read by a small model on the device. Nothing is sent anywhere. English letters and digits for now.
- One selection for everything: lasso strokes, shapes, pictures and text, then move, resize, rotate, flip, duplicate, recolor or change opacity and thickness from one small menu. Cut, copy and paste across pages and notebooks.
- Hold to straighten: hold the pen still at the end of a stroke and a rough line, box, ellipse or triangle snaps clean. Writing is left alone. Replaces Shape assist.
- Eraser mode that removes whole strokes.
- A more forgiving lasso: overlapping ends, grazed writing, text and pictures are picked up.
- Lasso has its own toolbar button with a new icon; Pan is a round button above the zoom control (tap again to return to your tool).
- The pen can tap the toolbar and menus.

## Gestures
- Two-finger tap: undo. Two-finger double tap: redo.
- Two-finger swipe: turn pages. Long two-finger swipe up: open your notebooks (or the library from a drawing).
- Hold Prev or Next: jump to the first or last page.
- With palm rejection on, "Finger on the page" makes a finger navigate or do nothing while the pen writes.
- Zooming out stops at the page width.

## Color screens
- A theme color, Ink Away green by default, or black, a preset or any color.
- Color ink shows in color while you draw; a toggle brings back the black preview.
- Colored binder tabs.

## Faster, with fewer flashes
- Saving big notebooks about 90% faster (only changed pages are written).
- Closing a 120-page notebook practically instant; the page overview opens about a third faster.
- Drawing 12-28% faster per point.
- Page turns refresh only the page and the bar; a stroke is no longer refreshed again on lift.
- Fewer flashes in the library and browser, none on color screens.
- Dragging a selection follows the finger smoothly.
- Android (Boox and others): drawing, erasing, shapes, the lasso and panning no longer refresh the screen for every pen sample, which made writing slow there. Not yet tried on a real Boox, so feedback is welcome. Kindle and Kobo work as before.

## Fixes
- Undo puts a moved lasso selection back.
- Moving no longer picks up shapes you had erased.
- Long menus on small or landscape screens slide over the toolbar instead of scrolling.

## For developers
- The canvas, once one 11,500-line file, is now 27 feature files with shared helpers, so a feature can be changed or added in one small file. A good time to fork it.
- A test suite of around 2,300 automated checks (including pixel-exact tests on KOReader's real drawing code), performance benchmarks and an e-ink refresh audit. Tests are not part of the download.

# v3.2.0 · 2026-10-02

Everything since 3.1.0 in one stable release.

## New
- **Landscape mode.** Remembered between sessions, and exports come out landscape.
- **Paste and copy in text boxes.** Long-press for a Paste bubble; Copy / Cut / Paste in the format menu. Uses KOReader's clipboard.
- **Background remover** for images, plus refreshed text controls.

## Pen
- Small handwriting no longer turns into straight lines.
- Kindle Scribe: strokes no longer join up when your hand rests on the screen.
- Quick writing no longer connects neighbouring letters.

## PDF
- Exporting long PDFs no longer crashes. Pages are saved one at a time, with a progress bar you can stop.
- Faster page turns, with fewer flashes.

## Colour screens
- Much faster drawing: ink shows instantly in black and settles to colour when you pause. Coloured pens no longer slow down at larger sizes.

## Fixes and speed
- The eraser no longer removes notebook lines.
- Menus open around 40% faster, strokes draw with far less work, and landscape is as fast as portrait.
- Typing no longer zooms the page when you tap away, and a new text box no longer starts with a stray letter.
- Toolbar taps no longer lag after closing a menu.

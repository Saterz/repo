# v6.0.4 · 2026-10-27

- Fix: Module card colours on PocketBook colour screens (#565)
- Fix: Border colours stay in colour on colour Kobo and Kindle screens
- Fix: Black screen after waking with Sleep screen anti-ghosting on
- Fix: Fewer full-screen flashes closing Shelf style and Filters
- New: Search in the collection editor (#488)

# v6.0.3 · 2026-10-26

- Fix: Paint shelf after sleep resume on some devices (#551)
- Fix: Status line tap keeps full screen when swipe back is off (#554)
- New: Micro modules > On the shelf switch

# v6.0.2 · 2026-10-25

- Fix: Refresh metadata (#552)
- New functions for module authors

# v6.0.1 · 2026-10-25

- Fix: cover shadows on colour screens (#550).
- Fix: top panel flicker under other plugins' windows (#549).
- Smaller status line refresh.
- Fix: keyboard access to the module editor.

# v6.0.0 · 2026-10-25

- Micro-modules have a layout editor: long-press a module, or the space between modules, to move it, resize it, send it to another page or add more. Swipe a module to move it, pinch or spread to resize it. Full screen is a 6-column grid with up to four pages (swipe or tap the dots); the top panel is two rows. Portrait and landscape keep their own layouts.
- Modules fit the space you give them: a wide clock puts its date beside it, and reading goals sit side by side.
- Each module can have its own card colors: tap the palette icon in the layout editor.
- New Shelf module: one of your shelves inside a module, as covers or spines on a plank. Point it at an existing shelf or give it a shelf of its own. Tapping a book shows it in the top panel, as on a shelf.
- New Ornament module: any piece from your ornament packs, with its own tap action.
- Modules among your books: Shelf editor > Add a module to this shelf… stands any module between the books on a covers or spines shelf.
- The module picker is sorted into chips: Shelf & books, Reading, Time & device, Fun & info, Actions, one per module pack, and My modules. Module packs can be published as small KOReader plugins, so they install and update from the device.
- The micro-modules view opened from inside a book shows the status line, and its clocks keep time.
- Module cards are warm paper by default on colour screens (the same grey as before on black-and-white screens).
- Colors > Panel color and Panel text: the top panel and footer can have a colour of their own.
- The book menu has a Highlights tab: a book's highlights, notes and bookmarks without opening it, with View in book to jump to one.
- Pin here on a shelf ornament's long-press menu keeps it where it stands, page after page; the others are still dealt around it.
- Shelf editor: Copy a shelf, and Move to… a shelf of shelves (or back out). A shelf of shelves' + Add shelf tile can Move a shelf here….
- Library & search > Show each book in one group only: on Authors, Genres and Collections shelves, a book in several groups appears in just its first.
- Author photos fill a cover-shaped card; square and wide photos are cropped at the sides.
- Bookshelf has its own icon in KOReader's top menu, as KOReader's new Reader tab uses the open book (#548). To use a different one, copy your own bookshelf.svg (or .png) into koreader/icons.
- Faster on a Kindle Paperwhite 5: the first visit to a shelf after starting is about twice as quick (Home 3.6 s to 1.9 s, Recent 2.1 s to 0.8 s), tapping a book takes about half the time, the book menu opens and closes faster, and closing a menu or waking from sleep no longer redraws the whole shelf. Genres with every book face out turns pages in 0.6 s instead of 1.6 s.
- Fix: inside a book, KOReader's menu and brightness gestures work under the micro-modules view.
- Fix: on low-memory devices without swap, the page-count scan no longer freezes the device on a heavy book; books it skipped before get one more try (#518).
- Fix: the Shelf size module no longer breaks when its numbers need two columns.
- Fix: %datetime day and month names follow KOReader's language (#545).
- Fix: with the Appearance plugin, Bookshelf's own text colours (spine titles, badges) are kept (#543).
- Fix: Kobo store books stay in Recent and the top panel after a restart (#546).
- Fix: a tall ornament standing over the shelf menu no longer stays behind after a page turn or takes the top panel's taps.

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

# v5.5.5 · 2026-10-20

- Covers can show your star rating in the corner: Settings > Cover display > Favorite icon or star rating > Stars (rating). With Hardcover enrichment > Use Hardcover rating if no user rating, books you haven't rated show their Hardcover rating instead, and the Rating sort and Ratings shelf use it too (#538).
- New gesture action: Bookshelf: refresh the library, for picking up new or edited books straight away (#541).
- Fix: page counts follow KOReader's Use stable page numbers when it's turned off (#539).
- Fix: the top panel's cover fills the panel's height again when the panel is tall (one row of covers, or swiped down).
- Fix: Clear cover cache also redoes every spine's colour from its cover (#537).
- Fix: Home (folders) and folder shelves sorted by Added or opened, Last opened, progress, status or rating re-sort straight after you close a book (#519).
- Fix: Back on the base shelf no longer climbs above your library with KOReader's Back in file browser set to parent folder, and neither does the Folder up gesture action (#542).

# v5.5.4 · 2026-10-18

- Spines: an optional Paperback binding, per shelf (long-press the shelf > Shelf style > Book binding) or per series (long-press a series > Book binding). Thanks @komadorirobin (#536).
- New: Advanced > Performance tweaks > Use E-ink refresh rate for shelf pages. Shelf page turns flash clean as often as KOReader's own full refresh rate, to clear ghosting (#529).
- Micro-modules open much faster: the full-screen view's first open after a restart went from about 4 seconds to half a second on a PW5, and Shelf size and Reading goal fill in their numbers in the background.
- About links the new user guide, andyhazz.github.io/bookshelf-docs.
- Fix: on Spines shelves of folders (Home, or a folder shelf), status, Opened, rating and the other progress sorts order the books in each folder (#534).
- Fix: Action cards in the full-screen micro-modules view work straight after closing a book (#533).
- Fix: KOReader gestures (brightness swipes, corner taps) and LiveLight's edge slides work over the shelf, book details and the ornament zoom while a closed book is still finishing.
- Fix: Shelf size in the full-screen view catches up after you finish a book.
- Fix: the About logo shows properly in night mode.

# v5.5.3 · 2026-10-17

- Shelf of shelves: the stack count badge now shows on its shelves' tiles, under Folders only or All stacks (#527), and Random book on "current shelf only" picks from the shelves inside it (#528).
- Spines: face-out covers keep the theme's border, so a custom Border colour no longer outlines them apart from the book.
- Fix: the section labels on Spines shelves show your Folder overlay colour instead of a grey (#525).
- Fix: Calibre metadata is found on a Kobo whose home folder was never set (#517).
- Fix: About now warns about another copy of bookshelf in a custom plugin folder.

# v5.5.2 · 2026-10-16

- Random book can open the book straight away: long-press the module > Module settings… > On tap > Open book directly.
- Fix: on PocketBook colour readers such as the Era Color, panel shading and the plates under cover captions are see-through instead of solid (#520).

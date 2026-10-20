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

# v5.5.1 · 2026-10-16

- Fix: a series' own image, set from its menu or in the image library's series folder, now shows on the front of its box set instead of the first book's cover.

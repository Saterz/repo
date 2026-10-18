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

# v5.5.0 · 2026-10-16

- Series boxes: long-press a shelf > Shelf style > Series boxes. On a Spines shelf each series stands as an open slipcase holding its books, with the first book's cover on the front and how many you've read. Tap it to open the series face-out, in series order (thanks @komadorirobin).
- Find author photos online: Settings > Library & search > Find author images online…, or long-press an author. Looks on Open Library, then Wikipedia, and saves each photo, sized for a tile, in your image library. Progress shows in the status line, with Stop. On an Authors shelf each photo sits in a frame at its own shape.
- Page badge replaces Show page count in Settings > Cover display: show pages, percent read or both, the number without the "p" (#499), and printed page counts first instead of the count at your reading settings.
- New sort keys: Added or opened, where new books and the book you just opened both go to the front, like a Kindle's home (#519); and Favorites first (thanks @dmaglio).
- Recently read module: the covers of the books you last opened (based on @rapinoinfeliz's PR).
- Books in formats that other plugins add, such as Meguru, now show on your shelves (thanks @AcidWeb).
- OPDS books that can be streamed (Komga, Kavita, Suwayomi) get Page stream, Stream from page and Resume buttons.
- For patch and plugin authors: add your own tokens, draw the placeholder for books without a cover, and add buttons to OPDS book details. See README and SOURCE_API.md.
- Moved: Extra wallpaper folder is now in Theme > Wallpaper, so Library & search is back on the first page of Settings.
- Fix: on a shelf inside a Shelf of shelves, turning a page no longer redraws the whole screen, which could show the shelf going white before it painted in.
- Fix: Scan all library metadata no longer stops straight away in French and some other languages (#516).
- Fix: one book that crashes the page count scan no longer takes KOReader down on every scan (#518).
- Fix: a book with progress but no reading status, e.g. from another app, shows its progress bar (#524).
- Fix: in list view a wrapped line keeps the style it started with and no longer covers the divider above (#510).
- Fix: accented letters written as HTML codes in descriptions now show as letters.
- Fix: On This Day, Trivia and Daily Fun no longer ask to turn on Wi-Fi when the home screen is drawn offline; tap them to fetch.
- Fix: shelf and tag button labels sit centred in UI fonts that put them high or low.
- Fix: opening a face-out book you had already selected no longer draws its shadow on the wall.
- Fix: re-linking a book to Hardcover keeps its cover and description choices.
- Fix: OPDS login details are no longer sent when a catalog redirects to another server.
- Fix: a plugin source's new books show straight away on Spines shelves (#511).

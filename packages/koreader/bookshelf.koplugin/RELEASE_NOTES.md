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

# v5.4.4 · 2026-10-12

- When Auto shows a list on both levels, Shelf style has list columns and rows for each, under Level 1 and Level 2.
- Spine shelves can face out Finished and On hold books.
- Fix: on spine shelves, a favourite that faces out shows its heart, and edge-on spines show the favourite icon you chose (heart by default) instead of always a star.

# v5.4.3 · 2026-10-11

- Auto now lets you choose a style for each level of a shelf. In Shelf style, choose Auto and tap Level 1 (the shelf itself) and Level 2 (anything you open from it) to step through Covers, List and Spines. A Genres shelf can list its genres and show each genre's books as covers or on spines, say. Level 1 also applies when the shelf is expanded, so an Auto shelf you haven't changed now shows covers expanded instead of a list. The list and spine settings below follow the styles you pick. A shelf of shelves no longer offers Auto, since each of its shelves has its own style.
- Fix: the top panel no longer changes height between shelves that show captions under their covers and shelves that don't, such as Home holding only folders.
- Fix: on a spine shelf, each folder, author or genre you open gets its own ornaments, instead of the same pieces in the same places every time.
- Fix: opening the book shown in the top panel from the cover grid no longer leaves a white frame around the cover over a wallpaper.

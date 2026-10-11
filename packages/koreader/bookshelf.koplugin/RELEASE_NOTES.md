# v5.4.3 · 2026-10-11

- Auto now lets you choose a style for each level of a shelf. In Shelf style, choose Auto and tap Level 1 (the shelf itself) and Level 2 (anything you open from it) to step through Covers, List and Spines. A Genres shelf can list its genres and show each genre's books as covers or on spines, say. Level 1 also applies when the shelf is expanded, so an Auto shelf you haven't changed now shows covers expanded instead of a list. The list and spine settings below follow the styles you pick. A shelf of shelves no longer offers Auto, since each of its shelves has its own style.
- Fix: the top panel no longer changes height between shelves that show captions under their covers and shelves that don't, such as Home holding only folders.
- Fix: on a spine shelf, each folder, author or genre you open gets its own ornaments, instead of the same pieces in the same places every time.
- Fix: opening the book shown in the top panel from the cover grid no longer leaves a white frame around the cover over a wallpaper.

# v5.4.2 · 2026-10-11

- Spine shelves now show every book. Home, folders and search shown as spines stopped at 5,000 books before.
- A theme of your own can now be just a wallpaper: make a folder in koreader/settings/bookshelf/ornaments, put a folder called theme inside it, and put your wallpaper.png in that. It shows in the Theme library under the folder's name, with no theme.json or ornaments needed. Optional wallpaper.dark.png, wallpaper.full.png and wallpaper.full.dark.png cover dark mode and full screen shelves.

# v5.4.1 · 2026-10-10

- Each shelf can choose its own cover captions: long-press a shelf, then Shelf style > Cover captions. For example, series names on your Series shelf and titles everywhere else. Shelves you leave alone follow Settings > Cover display.
- A shelf inside a shelf of shelves can now have its own theme. Until you choose one it wears its shelf of shelves' theme, shown as "Same as …" in Shelf style and the Theme menu, and the Theme menu's This shelf row now sets the shelf you're on.
- The line under each cover is now called a cover caption: Settings > Cover display > Cover captions, and Settings > Text size > Cover captions.
- Show text below groups is now a single switch, Show author below series. The Custom option for groups is gone: the only thing it could add was a series' author. If you had Author or Custom chosen, the switch is on.

# v5.4.0 · 2026-10-10

- Each shelf can now have its own theme (#495). Choose one in the new Theme library: a card for each theme, and the shelf behind changes as you tap. Shelves you leave alone use your Default theme.
- Any theme can be edited. Change its wallpaper, plank, colours or ornaments and the changes stay with that theme; Reset in the Theme library puts it back.
- Your own wallpaper, plank and colours are now a theme of their own, Custom theme, and choosing a pack no longer overwrites them. There is also a new built-in Plain theme: no wallpaper, Oak plank, default colours.
- Every ornament pack can be chosen as a theme.
- Your shelf looks the same after updating: a pack you were using becomes your Default theme, and your own settings become Custom theme.
- One Theme menu replaces Shelf theme and Wallpaper, ornaments and colours. Shelf style (long-press a shelf) also starts with a Theme row.
- Shelf of shelves: a new shelf source that holds other shelves, as many levels deep as you like, each with all the options of any shelf. On Spines it shows the books from all of them (#489).
- Taking a face-out book off a spine shelf now shows it in 3D, pulled off the shelf and turned so you see its pages and boards.
- Ornaments no longer stand in the same places on every page, and each shelf keeps its own ornaments in its own order. Swap and Shuffle this shelf only change the shelf you're on.
- Custom text below covers: Settings > Cover display > Show text below covers > Custom… builds the line from tokens, e.g. %book_pct · %size for how far you've read and the file size.
- Show text below groups: a separate line under series and other stacks, so you can have titles under books and the author under series (#486). Choose None, Author or Custom… in Settings > Cover display.
- Panel shading is now in Theme > Wallpaper and part of the theme, so a pack can bring its own. Two new options sit with it: Blur wallpaper behind panels, and Panel behind Covers shelves for the same solid panel list view has (#483).
- The shelf editor applies each change as you make it, so Close replaces Cancel and Save.
- The Kobo shelf is now a shelf source: add a shelf and choose Kobo library. The Kobo setting under Advanced is gone.
- Other plugins can now add their own shelf sources (#452). See SOURCE_API.md.
- Moved: Extra wallpaper folder is now under Settings. Colours > Colours for: Light | Dark switches the set you're editing without turning on night mode. Transparent is now a choice in Colours > Shelf menu background.
- For pack makers: plank_solid plank ends; in theme.json a "hero" ornament for the pack's card and panel_shading, panel_blur and covers_panel; a per-piece "trim" in pack.json.
- Fix: on a shelf with a filter, opening a series or other stack shows all its matching books, not only the first (#485).
- Fix: in list view, a book marked finished without being opened shows a full progress bar (#487).
- Fix: books from Calibre-Web no longer start their description with its RATING, TAGS and SERIES lines, books already downloaded included (#490).
- Fix: on a new KOReader install with no home folder set, Home shows the device's books instead of none.
- Fix: closing a picker while its search keyboard was open no longer leaves the keyboard behind with KOReader looking frozen.
- Fix: an ornament in the bottom-left corner no longer takes taps meant for the start menu button.
- Fix: Transparent panel shading no longer makes the shelf menu transparent too. If you had that look, it is kept as Shelf menu background: Transparent.
- Fix: with a plank design, hanging ornaments stay on the wall instead of overlapping a plank, and plank ends are no longer cut short after an animated page turn.
- Fix: switching a shelf to another style and back no longer changes the size of the top panel.
- Fix: covers added by a fallback cover patch no longer disappear after the first draw (#500).
- Fix: under Most recently read on a series shelf, adding a book no longer counts as reading it: unread books, and the series they join, no longer jump to the front.
- Fix: every top panel progress bar style (Rounded, Metro, Wave, Pacman) now draws without Bookends installed; the default Rounded bar was square without it.
- Fix: a UI font with no italic file no longer fills the log with font errors (#501, thanks @Tsukumi233).

# v5.3.1 · 2026-10-03

- Fix: a series, author, genre or collection opened from book details shows all of its books again, instead of only those matching the shelf you opened it from (#480).
- Fix: on a spine shelf, the D-pad reaches every book on the page, and up and down move between shelves. Before, it stopped after the first few books on each shelf.
- Fix: on devices without a touchscreen (#361):
  - the page arrows, page number and start-menu button highlight as you move between them;
  - the book details tabs switch when you press on them;
  - the highlight in the shelf editor follows the D-pad instead of staying on the first button;
  - Back closes Adjust shelf/top panel size, the same as Cancel.

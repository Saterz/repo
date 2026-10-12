# 2.0 · 2026-10-12

Plain UI 2.0 adds a minimal reading interface alongside the library browser.

- Swipe down for typography, recent books, reading stats, and other reading tools.
- Use three typography profiles, with settings remembered for each book.
- Swipe up from the bottom edge to preview pages, browse chapters, and reach bookmarks, the table of contents, and search.
- Retrace navigation jumps with the return footer.
- Browse Books, Series, Authors, and Tags in cover grids or lists, with filters, sorting, and reading-progress badges.
- Use the reader controls with EPUBs and fixed-page documents, including PDFs.

[User guide](https://code.anh.do/plainui.koplugin/) · [Tested compatibility](https://code.anh.do/plainui.koplugin/#compatibility)

Download **plainui.koplugin.zip** and extract its plugin folder into KOReader's `plugins` folder. When upgrading, replace the existing `plainui.koplugin` folder. Enable both **Plain UI** and **Cover browser**, disable conflicting UI replacements, and restart KOReader. Follow any notice about redundant older library patches.

Please report problems through [GitHub Issues](https://github.com/quanganhdo/plainui.koplugin/issues), including your KOReader version, device, and enabled UI or statistics patches/plugins.

**Full changelog:** [1.2 → 2.0](https://github.com/quanganhdo/plainui.koplugin/compare/1.2...2.0)

# 1.2 · 2026-05-06

**Full Changelog**: https://github.com/quanganhdo/plainui.koplugin/compare/1.1...1.2

### Browsing

  - Tap the selected tab to open view options.
  - Books can now be filtered by All, Unread, Reading, or Finished.
  - Books can now be sorted by Last read, Title, or Progress.
  - Authors, Series, and Tags can now be filtered by All, Unread, Reading, or Finished.
  - Authors, Series, and Tags can now be sorted by name/title or by number of books.

### Cover Grid

  - Accessibility: Cover badge font size can now be customized with `plainui_badge_font_size`.

# 1.1 · 2026-05-05

**Full Changelog**: https://github.com/quanganhdo/plainui.koplugin/compare/1.1...1.1

### Browsing

- Added Tags as a first-class tab.
- Added multi-filter browsing via the title dropdown.
- Excludes non-book junk like .log, .sh, .md, etc from virtual folders.

### Cover Grid

- Virtual folders now use randomized representative covers.
- Removed virtual folder stack visualization.
- Series index badges now use #, e.g. #2.
- Badge styling is more consistent and translucent across finished, progress, series index, and count badges.

# 1.0 · 2026-05-03

Hello World!

**Full Changelog**: https://github.com/quanganhdo/plainui.koplugin/commits/1.0

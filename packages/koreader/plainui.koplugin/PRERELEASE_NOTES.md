# 2.0 · 2026-10-12

Plain UI 2.0 adds a minimal reading interface alongside the library browser. This is a prerelease for early testing.

- Swipe down for typography, recent books, reading stats, and other reading tools.
- Use three typography profiles, with settings remembered for each book.
- Swipe up from the bottom edge to preview pages, browse chapters, and reach bookmarks, the table of contents, and search.
- Retrace navigation jumps with the return footer.
- Browse Books, Series, Authors, and Tags in cover grids or lists, with filters, sorting, and reading-progress badges.
- Use the reader controls with EPUBs and fixed-page documents, including PDFs.

[User guide](https://code.anh.do/plainui.koplugin/) · [Tested compatibility](https://code.anh.do/plainui.koplugin/#compatibility)

Download **plainui.koplugin.zip** and extract its plugin folder into KOReader's `plugins` folder. When upgrading, replace the existing `plainui.koplugin` folder. Enable both **Plain UI** and **Cover browser**, disable conflicting UI replacements, and restart KOReader. Follow any notice about redundant older library patches.

Validated with KOReader `v2026.03-81-g41c9e02b5`: all 17 unit suites / 144 checks pass. Native emulator checks cover fresh installation, upgrade from Plain UI 1.2, restart persistence, EPUB/PDF reading, typography, statistics, and navigation. Physical-device behavior and external sync transfers are not covered by those checks.

Please report problems through [GitHub Issues](https://github.com/quanganhdo/plainui.koplugin/issues), including your KOReader version, device, and enabled UI or statistics patches/plugins.

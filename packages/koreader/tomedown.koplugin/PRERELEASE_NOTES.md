# v1.1.0-beta.1 · 2026-10-25

**Tomedown 1.1.0-beta.1, the first beta of the per book edition.**

1.1 is about one question: whose notes are kept. Preservation is now decided per book instead of for the whole library, the index has its own switch instead of following whichever book you exported last, and turning preserve off asks first and puts your notes back when you turn it on again. Block IDs arrived too, so a link to a highlight in Obsidian survives the next export.

A beta, and it behaves like one: it replaces 1.0.0 in the plugin folder (going back means installing the 1.0.0 zip again). What it needs is a week of real reading, and a note from you the moment something feels off.

## Highlights

- **A switch for each book.** *Preserve: this book*, in the book's menu under *Export current book*, decides for that book alone. *Preserve: global* stays the default: on, every file follows it and the per file rows are not even built; off, each book goes back to whatever it stored.
- **A heading for each book.** *Book notes: %1* names that book's zone, and only that book's. Any title you like ("The Witch theory", "Julian Carax Dixit", ...); leave it empty and the zone exports with nothing above it.
- **The index stopped tagging along.** *Preserve: index* and *Index notes: %1* sit in *Settings → Markdown files*, and exporting one book can no longer rewrite your notes in `00 - Index.md`. Off keeps the file as `00 - Index.md.bak`; on brings it back.
- **Turning it off asks first.** A box says what is about to happen, because with preserve off the render overwrites the file (no merge, no copy). Confirm and the file you had is kept as `.bak`, so turning preserve on again puts your notes back into the file, as long as the plain file is the one Tomedown wrote last: something you typed meanwhile is never replaced by an older snapshot.
- **Block IDs on every highlight.** A stable `^hl-…` at the end of each quote, so a link from another note lands on that highlight and survives the next export. Off by default, from *Block IDs for highlights*, with the id taken from the highlight's own creation time.

## Added

- A *Highlights* group in Settings, with its own icon: *All highlights as Special Highlights*, *Special highlight marker: %1* (callout, or bold for a paragraph-wrapped quote) and *Block IDs for highlights*. The three moved out of *Markdown files*, which had grown too crowded.

## Changed

- Three rows finally read what they do: *Preserve: global* for *Preserve manual edits*, *Notes: %1* for *Personal notes: %1*, and *Export every book's highlights* for *Import all books from history*, which exports and never imports. The global one takes that name to sit next to the other two preserve rows.
- The rows that need a book (*Export current book*, *Preserve: this book*, *Book notes: %1*) only exist while a book is open: in the file manager they pointed at whatever had been read last, so that menu now starts at *Export only what changed*.
- New screenshots everywhere, including the menu inside an open book, and the guide sheets follow the new row names.

## Fixed

- **A picked folder no longer gets lost.** It is written to the settings file on the spot; before, it only reached the disk at the next suspend or autosave, so KOReader closing in between sent the next export to the folder you had just left.
- **A backup can no longer be thrown away by one worth less.** All backups went to a single name, so the next one overwrote the last, and the copy destroyed could be the one holding your notes (turning preserve back on found the plain file Tomedown itself had written and flagged it for backup anyway). There are two slots now, `.bak` and `.bak.1`, the older one rotates back, and a file that is exactly what Tomedown wrote last is not copied at all.

## Still open

On the roadmap after this beta. No promises, no dates, nothing decided:

- **Where the copies live, and how many.** Two slots per file is what this beta ships; one slot only, a `highlights_backup/` folder, or the two we have plus rows to clear them by hand is the question for the Discussion.
- **Managing the `.bak` copies.** A row to delete a book's own copy, a row that lists every copy in the folder, never a button that deletes them all at once: they may be the only copy of what you wrote by hand.
- **Spacing that matches the reader**, so the merge respects the blank lines you leave under a heading.
- **Index speed**, only if a large library ever feels slow.

## What to try first

Flip *Preserve: global* on and off with notes sitting in the books and in the index. Turn *Preserve: this book* off for one book and read the box. Export, type a line in the plain file by hand, switch preserve on again and check your line is still there. Rename *Book notes: %1* on two books and make sure each keeps its own.

## Installing

Download `tomedown.koplugin-v1.1.0-beta.1.zip` from the **Assets** section at the bottom of this page (not the *Source code* archive), unzip it into `koreader/plugins/` and restart KOReader.

The beta is also opt-in inside KOReader: *Settings → Updates → Developer*, with *Beta Releases* ticked, will offer it. Without that tick nothing changes, the background check stays on stable releases and nobody gets nudged towards it.

README, full tutorial, quickstart sheets and Obsidian guide sheets: https://github.com/imanubdesigner/tomedown.koplugin

# v0.8.0-beta.6 · 2026-10-03

> **Last beta before the Vault stable: an index grammar fix and a device check for the new menus.**

Sixth beta of the **Vault** release.

## Highlights

- **Stats line grammar**: a vault with a single book (or a single highlight) now reads `*1 book · 1 highlight — click a title to open its note.*` — no more `1 books · 1 highlights`
- Nothing else changed in the export: hashes stay valid, so there is nothing to re-export; the index line corrects itself on the next export that writes files
- README: the index sample shows the rendered status label, and the stale pre-format screenshot is gone

## Beta focus

1. On the Kindle: Settings → **Beta Releases** ON → *Check for updates* → update to beta.6 and restart.
2. On desktop: reinstall the plugin from the asset below, then restart KOReader.
3. **Device check this round**: open a highlight's menu on the Kindle screen — the entry *All highlights as Special Highlights* is longer than the old one. If it gets truncated on the e-ink menu, say so in the discussion.

All 758 test assertions green.

*Remotely Save users: set **Abort Sync If Modification Above Percentage** to **100 (disable the protection)** — Tomedown re-exports notes in bulk, which trips the default 50% guard.*

# v0.8.0-beta.5 · 2026-10-02

> **The Vault release is getting close — this beta locks the new export layout. Update, run one export, and every note is rewritten once.**

Fifth beta of the **Vault** release: a cleaner layout for every exported file.

## Highlights

- **Every exported file opens with a horizontal rule** right after the frontmatter — properties, rule, content (book notes and the index alike)
- **The index shows a stats line above the table** — `*9 books · 53 highlights — click a title to open its note.*`
- **The book cover is centered** and framed by a rule before the `# **HIGHLIGHTS**` heading
- **Menu renames**: *Generate the 00 - Index.md (for Obsidian)* and *All highlights as Special Highlights* — same behavior, clearer names
- **Automatic rewrite**: the render format is part of the stored hash, so the first export after the update rewrites every note — no *Import all books* needed
- Index covers stay at 90×120 (the table caps the size anyway)
- README: refreshed menu and Obsidian screenshots

## 0.8.0 recap (betas 1–5)

- Book covers in the exports (frontmatter + `<img>` + index column), Obsidian 1.8.1+
- Covers upload into their own `covers/` folder, created on the server on the first upload
- Callouts on export, new index (v2)
- Special Highlight: its own menu entry plus a dynamic row in the compact highlight menu
- Status popup: wide (90% of the screen), small font, labels in bold
- Keywords always valid Obsidian tags (whitelist)
- Clean export layout: rules, stats line, centered cover

## Beta focus

1. On the Kindle: Settings → **Beta Releases** ON → *Check for updates* → update to beta.5 and restart.
2. On desktop: reinstall the plugin from the asset below, then restart KOReader.
3. Export once — everything rewrites — and check in Obsidian: the rule after the properties, the stats line above the index table, the centered cover.

All 757 test assertions green.

*Remotely Save users: set **Abort Sync If Modification Above Percentage** to **100 (disable the protection)** — Tomedown re-exports notes in bulk, which trips the default 50% guard.*

# v0.8.0-beta.4 · 2026-10-02

> **This is a more stable beta of the Vault release — if you want to try the book covers, this is a good moment to test them.**

Fourth beta of the **Vault** release: keywords now export as always-valid Obsidian tags.

## Fixes

- **Keywords are sanitized by a whitelist now, not a blacklist** — Obsidian's real tag validator is stricter than its documented forbidden list, so `Horror tales; American` survived the previous fix (`;` is not in the docs' list) and its chip stayed struck through in the properties, as did anything carrying `'`, `=`, `[`, `]` or `#`. `sanitizeTag` keeps only letters, numbers, `-`, `_`, `/` and every non-ASCII character (accents, emoji): whitespace becomes `-`, everything else outside the whitelist is dropped. Books whose keywords change re-export automatically at the next export (hash migration) — nothing to clean up in the vault.

## 0.8.0 recap (betas 1–4)

- Book covers in the exports (frontmatter + `<img>` + index column), Obsidian 1.8.1+
- Covers upload into their own `covers/` folder, created on the server on the first upload
- Callouts on export, new index (v2)
- Special Highlight: its own menu entry plus a dynamic row in the compact highlight menu
- Status popup: wide (90% of the screen), small font, labels in bold
- Keywords always valid Obsidian tags (whitelist)

## Beta focus

1. On the Kindle: Settings → **Beta Releases** ON → *Check for updates* → update to beta.4 and restart.
2. On desktop: reinstall the plugin from the asset below, then restart KOReader.
3. Export, sync, and check in Obsidian that tags like `Horror-tales-American` are no longer struck through (`Horror tales; American` was the trigger).

All 750 test assertions green.

*Remotely Save users: set **Abort Sync If Modification Above Percentage** to **100 (disable the protection)** — Tomedown re-exports notes in bulk, which trips the default 50% guard.*

# v0.8.0-beta.3 · 2026-10-02

Third beta of the **Vault** release: covers export in full colour on any screen.

## Fixes

- **Covers are now always full colour** — on greyscale e-ink screens KOReader decodes covers in greyscale (`Pic.color = Device:hasColorScreen()` for EPUB/CRE JPEGs, `CanvasContext.is_color_rendering_enabled` for PDF/DJVU and custom image covers), so every exported `.jpg` came out black and white even though Obsidian shows it on a colour screen. The extraction now forces colour rendering on for the duration of the call and restores it unconditionally right after.

## 0.8.0 recap (betas 1–3)

- Book covers in the exports (frontmatter + `<img>` + index column), Obsidian 1.8.1+
- Covers upload into their own `covers/` folder, created on the server on the first upload
- Callouts on export, new index (v2)
- Special Highlight: its own menu entry plus a dynamic row in the compact highlight menu
- Status popup: wide (90% of the screen), small font, labels in bold

## Beta focus

1. On the Kindle: Settings → **Beta Releases** ON → *Check for updates* → update to beta.3 and restart.
2. In the vault: delete the stray `.jpg` files sitting in the **root** (leftovers of beta.1) and the grey ones inside `covers/`.
3. In Settings untick and tick **Include book covers** again (this invalidates the stored hashes), then export.
4. Check in Obsidian that the covers come back **in colour** in the book notes and in the index column.

All 725 test assertions green.

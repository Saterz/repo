# v1.0.0 · 2026-10-21

**Tomedown 1.0.0, the first stable release of the two-way edition.**

Two betas are behind this one, both tested end to end, offline included. This is the version that stops throwing away what you write.

## Highlights

- **Your own notes survive the export.** *Preserve manual edits* is new in 1.0.0, off by default: switch it on and the new render folds into the file you already annotated instead of replacing it. Your words stay under their own heading, fenced by the invisible HTML comments the plugin uses as handles. In 0.8.0 there was no such thing: every export won, and anything you typed at your desk was gone on the next run.
- **The merge works both ways now.** Before folding the new highlights in, the export fetches your copy from the cloud and, if it changed since the last upload, uses that as the base instead of the local one. Your notes come along with the fresh highlights. The setting is *Merge edits made in the cloud*, it is on by default, and it lives in Settings → Cloud right under *Upload to cloud*.
- **Offline is a first-class case.** Export with no connection and the file is queued. When you are back online, the plugin fetches the cloud copy, compares it with the one it sent last, folds your notes in, and only then pushes. If the download fails for some transient reason the file is held back and retried at the next chance, so nothing gets lost in either direction.

## Added

- *Preserve manual edits* as a setting, together with *Personal notes*, the heading above your notes block. Rename it per your taste, or leave the field empty to export without a heading. The row only exists while preserve is on.
- The settings menu is flatter, and the rows appear and disappear in place as you flip the toggles. The *Cloud* group shows only when a server is set, upload is on and preserve is on, because that is the only case where it has something to do.
- The About popup shows both repository links.

## Changed

- *Reload everything to the cloud* is now *Upload everything to the cloud*, which is what it actually does. It runs the same reconciliation as the export before pushing, so notes written in Obsidian get folded in there too.
- Reading progress bars are drawn as plain rectangles instead of glyphs, so they render the same on every device font.
- The guide sheets, the quickstart sheets and the menu screenshots were all retouched: portable fonts, the Obsidian palette, the settings paths corrected, the cover captions reworded to match what the plugin really does.
- The release zip now carries only what KOReader loads at runtime: the Lua modules, `languages/` and the logo.

## Fixed

- The flush cannot start twice over the same files. `reconcilePending` costs one network request per queued file and the flag that guards the upload was raised only after it, so a reconnect or a resume landing in the middle of that window could queue a second flush on top of the first one. The flag now stays up for the whole reconciliation, lowered on every exit including the error path, where it is wrapped in `pcall` so a failure inside it cannot leave the flush switched off until restart.
- The open book is read from memory during the export instead of being reopened, which was both slower and able to fail on a book still in use.
- `00 - Index.md` reports a write failure instead of failing quietly.

## Upcoming

Things we would like to try next. No promises, no dates, and nothing here is decided yet:

- **Preserve per book.** Keep the global toggle as the default and let a single book override it, for the series you annotate by hand and the ones you do not.
- **Stable block IDs on the highlights.** Give every exported highlight an Obsidian block ID so you can link straight to it from another note and keep that link alive after the next export. Suggested by [Tewel](https://codeberg.org/Tewel), and the one idea from this round that is not in the release yet.
- **Spacing that matches the reader.** Let the merge respect the blank lines you leave under a heading instead of framing the zone the way the plugin prefers.
- **Index speed**, only if a large library ever feels slow. Nothing to do there today.

## Installing

**If you already use a KOReader plugin store** — [Storefront](https://github.com/ultimatejimmy/storefront.koplugin) or [AppStore](https://github.com/omer-faruq/appstore.koplugin), both under *Tools* search `tomedown` and install it. They are community plugins, not part of KOReader itself; if you have neither, use the zip below.

**Manual**: download `tomedown.koplugin-v1.0.0.zip` from the **Assets** section at the bottom of this page (not the *Source code* archive), unzip it into `koreader/plugins/` and restart KOReader.

**Coming from 0.8.0** > *Check for updates* in the plugin menu now finds this release by itself, no zip needed.

README, full tutorial, quickstart sheets and Obsidian guide sheets:
https://github.com/imanubdesigner/tomedown.koplugin

# v0.8.0 · 2026-10-03

> **The Vault release is here: book covers, callouts, a new index and an export layout that reads like a note vault instead of a dump of quotes.**


https://github.com/user-attachments/assets/d4eb3e01-4b22-4947-ab4f-ed8c080bb7d5



## Highlights

- **Book covers** — *Include book covers* (off by default): every export saves the book's cover as an 800×1200 JPEG in full colour (quality 50) under `covers/`, embeds it in the book note and in the index. The `covers/` folder is created on the server on the first upload (WebDAV, FTP, Dropbox); the file leaves the device once the upload has confirmed it, stays queued while offline and goes away on the next flush. Obsidian 1.8.1+ renders the plain `<img>` tags — no snippet to install.

- **Callouts** — *All highlights as Special Highlights* (off by default): every highlight becomes an `> [!highlight]` callout instead of a plain quote; when the toggle is off, only *Special Highlight* marks turn into callouts.

- **Special Highlight** — one tap on a fresh selection (right under *Highlight*) creates and flags a highlight; the compact edit menu of an existing highlight carries the same dynamic row, *Special Highlight* / *Remove Special Highlight*. The mark lives on the annotation, is part of the book hash, and is always exported as a callout.

- **Index v2** — the book index gains cover, book, author, series, status, highlight count and last export per row, wiki links, and a stats line above the table. Existing vaults are backfilled on the next export.

- **Clean export layout** — every file opens with a rule right after the frontmatter, the book cover is centered and framed by rules before the `# **HIGHLIGHTS**` heading, and the index leads with `*9 books · 53 highlights — click a title to open its note.*` (singular agrees too: `*1 book · 1 highlight …*`).

- **Menu renames** — *Generate the 00 - Index.md (for Obsidian)* and *All highlights as Special Highlights*: same behavior, clearer names.

- **Status popup** — widened to 90% of the screen, smallest font, one line per entry with the labels in bold.

- **Keywords are always valid Obsidian tags** — a whitelist sanitizer keeps only letters, numbers, `-`, `_`, `/` and every non-ASCII character (accents, emoji); whitespace becomes `-`, everything else is dropped (`Horror tales; American` → `Horror-tales-American`). Books whose keywords change re-export automatically.

- **Automatic rewrite** — the render format is part of the stored book hash, so the first export after updating rewrites every note once. No *Import all books from history* needed.

## Updating

Update and run one export: notes, covers and the index regenerate themselves. Running one of the betas? Update as usual and switch **Beta Releases** off again if you don't want prereleases any more.

New to Tomedown: download the zip below and install it as a KOReader plugin.

All 758 test assertions green.

*Remotely Save users: set **Abort Sync If Modification Above Percentage** to **100 (disable the protection)** — Tomedown re-exports notes in bulk, which trips the default 50% guard.*

# v0.7.1 · 2026-10-01

## v0.7.1

### **Fixed**

-	Closing a book no longer runs the export **twice**. The plugin was
  registering itself in KOReader's event chain in addition to KOReader's
  own registration, so `CloseDocument` (and suspend/network events)
  reached it twice: the first run exported and toasted
  `Closing · 1 file exported locally`, the second one — a second later,
  finding nothing changed — stayed silent and overwrote the outcome
  recorded for the Status panel, which then read
  `Last export: … — 0 exported, 1 skipped` right after the toast. The
  same overwrite hid real suspend exports.

-	With this fix the Status panel's *Last export* always matches what
  the last run actually did: the toast and the panel report the same
  numbers.

### **Documentation**

-	Menu screenshots refreshed for 0.7: Tomedown on top of the reader's
  *Navigation* tab and of the file browser's menu, the submenu with the
  new *Status* row; the stale `NEW:` screenshot is gone. *Status* is
  documented in the Usage list.

### **Zip contents**

`main.lua`, `_meta.lua`, `tomedown_i18n.lua`, `tomedown_render.lua`,
`tomedown_update.lua`, `languages/it.po`, `LICENSE`,
`assets/logo.svg` - no tests, no README.

### **Upgrading**

-	Drop-in, no re-export needed. After updating, the next close exports
  once and *Last export* reflects that run.

# v0.7.0 · 2026-10-01

## v0.7.0

### **Menu placement**

-	Tomedown now sits at the top of the reader's *Navigation* tab and the
  file manager's *Settings* tab — the first entry on the first page, the
  way the Bookshelf plugin does it — instead of falling to the bottom of
  the tab with KOReader's automatic `NEW: ` prefix.

-	The entry was already in both menus: it only moved. No extra tab, no
  duplicated row. (A dedicated top-level tab is deliberately deferred to
  a future release.)

### **Status panel**

-	A new *Status* row, right under *Reload everything to the cloud*, opens
  one screen with the state that otherwise only lives in the transient
  toast history: network, server and folder, queued uploads with what
  the next flush is waiting for, and the last export/upload with their
  timestamp and outcome.

-	Export and upload outcomes are recorded for every path, silent
  suspend exports included, so the panel reflects what actually ran.

### **Uploads in crash.log**

-	Each upload now logs its target and file count when it starts and the
  ok/errors tally when it finishes; the pending queue logs how many
  files it flushes. Batch totals were already there — which uploads
  actually ran and how they ended only ever reached the toasts.

### **Notification labels**

-	Automatic exports say where they came from: `Closing · 3 files
  exported locally` (`Chiusura · 3 file esportati localmente` in
  Italian). Manual exports keep the plain toast — you just tapped the
  menu entry.

-	The error window, which stays on screen after a background close,
  always names its trigger (`Closing` or `Manual`).

### **Under the hood**

-	The widget class was renamed `MdBook` → `Tomedown`.

-	625 test assertions (lua5.4 + `luac5.1 -p`); Italian translation
  updated for every new string.

### **Zip contents**

`main.lua`, `_meta.lua`, `tomedown_i18n.lua`, `tomedown_render.lua`,
`tomedown_update.lua`, `languages/it.po`, `LICENSE`,
`assets/logo.svg` - no tests, no README.

### **Upgrading**

-	Drop-in: no format change, no re-export needed. The menu entry moves
  to the top of the tab it was already in; everything else stays where
  it was.

# v0.6.0 · 2026-10-01

## v0.6.0

### **New file format**

-	The framed HIGHLIGHTS heading is now a bold level-one heading:

    ```markdown
    # **HIGHLIGHTS: 150**
    ```

    (`# **EVIDENZIATI: 150**` with an Italian KOReader)

-	Chapters and the `Page bookmarks` section are level-one headings now
  (they were `####`): top-level entries in Obsidian's outline, as
  `# Chapter I` and `# Segnalibri di pagina` in Italian.

-	Sections are separated by horizontal rules before every heading,
  with blank lines around them, and a file never ends with a stray
  rule:

    ```markdown
    ---

    # Chapter I
    ```

### **Tags and index**

-	Books are tagged `ebook` instead of `kindle`, in the books and in
  the index alike.

-	The wiki links in the index escape the pipe
  (`[[Blackwater\|Blackwater]]`), so the table renders the link
  instead of breaking the column.

### **Changelog viewer**

-	Release notes and update notices render in a sans-serif face now,
  instead of the default serif; the *Font size*, *Monospace* and
  *Justify* options in the viewer menu keep working as before.

-	List points open with a plain hyphen instead of a bullet, which
  some device fonts draw like an apostrophe.

### **Documentation**

-	The README walks through every plugin menu with screenshots, shows
  the result in Obsidian and links a short demo video of the index
  in action.

### **Under the hood**

-	591 test assertions (lua5.4 + `luac5.1 -p`); Italian translation
  unchanged.

### **Zip contents**

`main.lua`, `_meta.lua`, `tomedown_i18n.lua`, `tomedown_render.lua`,
`tomedown_update.lua`, `languages/it.po`, `LICENSE`,
`assets/logo.svg` - no tests, no README.

### **Upgrading**

-	Exported files are always rebuilt from scratch by KOReader, so the new
  format needs **one full re-export**: menu > *Import all books from
  history* rewrites every file in the new format and uploads it (or
  queues it offline).

-	*Export only what changed* and auto-export on close skip books whose
  annotations have not changed - they leave older files alone, by
  design: run the full export once after updating.

-	*Reload everything to the cloud* does not reformat anything: it
  uploads local files exactly as they are.

-	Queries filtering on the old tag (`#kindle` in Dataview or similar)
  need to move to `#ebook`.

-	A full export overwrites every file: hand-made edits inside the
  `.md` files are not merged back.

---

*Sorry for the formatting tweaks: I want this changelog to read as cleanly as possible on every screen. Thanks for bearing with me.*

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

# v0.8.0-beta.2 · 2026-10-02

Second beta of the **Vault** release: fixes where the book covers end up on the cloud.

## Fixes

- **Covers now upload into `covers/`** — KOReader's cloud providers build the remote path as `<folder>/<basename>`, dropping the local subfolder, so in beta.1 every cover landed flattened in the vault root and the `covers/` folder never existed on the server (Obsidian's `covers/…` links pointed nowhere). The upload url now carries the subfolder, and the remote folder is created on the first upload (MKCOL once per run; an existing folder — 405/550/409 — or a refused MKCOL never blocks the upload). Same behaviour on WebDAV (Koofr & co.), FTP and Dropbox.
- The Settings screenshot refreshed (it was missing *Include book covers*), the Status popup shown in the README, *Special highlights* linked in the TOC.

## 0.8.0 recap (from beta.1)

- Book covers in the exports (frontmatter + `<img>` + index column), Obsidian 1.8.1+
- Callouts on export, new index (v2)
- Special Highlight: its own menu entry (`03b_special`) plus a dynamic row in the compact highlight menu
- Status popup: wide (90% of the screen), small font, labels in bold

## Beta focus

1. On the Kindle: Settings → **Beta Releases** ON → *Check for updates* → update and restart.
2. Delete the stray `.jpg` files sitting in the **vault root** (leftovers of beta.1) in Koofr and in Obsidian.
3. Run **Import all books from history**: covers are re-extracted and uploaded into `covers/`.
4. Check in Obsidian that the book note image and the index cover column resolve.

All 718 test assertions green.

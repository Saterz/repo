# v0.1.0-beta.14 · 2026-10-27

## Svenska

- Arkivskåpsknappen i läsmenyn använder nu OrbitUI:s snabba återgång till rätt Bookshelf-hylla/profil. Säker vanlig stängning används när en förberedd hylla saknas. Går att stänga av under Navigation och gränssnitt → Öppna böcker och återgå.
- Tydligare profil- och chipinställningar: källa/mapp inne i respektive chip, gemensamma biblioteksmappar under Avancerat och separata numrerade ordningsvyer som uppdateras direkt. Svenska och engelska ingår.
- SimpleUI uppdaterad med bättre Unicode-sökning/sortering, en startguidefix och spanska/kinesiska översättningar. Äldre KOReader-versioner behåller en kompatibel Unicode-reservväg.
- Fel vid läsning av metadatacachen fångas utan upstreams automatiska radering av databasen. Detta är inte automatisk reparation av en korrupt databas.
- Home/Bento, omslagsfixen för Android, bibliotek/profiler, ornament och externa integrationer behålls. Inga böcker flyttas och inga inställningar eller läsdata återställs.

Uppdatera via OrbitUI:s förhandsversionskanal och starta om KOReader. Bootstrap/API 1 är oförändrat och äldre stödda installerare kan uppdatera direkt. Säkerhetskopiera inställningar separat; kodåterställning återställer inte senare inställningsändringar. Detta är en förhandsversion: fysiska Boox/Bigme-tester av de nya funktionerna återstår.

## English

- The reading menu's cabinet/file-browser button now uses OrbitUI's fast return to the original shelf or matching Bookshelf profile, with safe normal-close fallback and a bilingual opt-out.
- Clearer profile/chip settings: source and folder inside each chip, library-wide roots under Advanced, and separate live numbered library/chip ordering screens.
- Reviewed SimpleUI update: Unicode-aware search/sorts, onboarding preset-list fix, Spanish/Chinese translations, and compatibility fallback for older supported KOReader versions. Bookshelf stays at 6.0.3.
- Recognized metadata-cache read faults are contained without automatically deleting the database/WAL or resetting shared connections. This does not automatically repair corrupt databases.
- Existing Home/Bento layouts, Android cover fix, profiles, ornaments, links, reading data and external sync owners are preserved.

Use OrbitUI's preview update channel and restart KOReader. Bootstrap/API 1 and the installed path inventory remain unchanged; no resources or older notes were removed to fit. Previous releases/assets are immutable. Physical device acceptance remains outstanding; automated tests are not device or measured-performance claims.

# v0.1.0-beta.13 · 2026-10-27

# OrbitUI 0.1.0-beta.13

## Svenska

Tydligare OrbitUI-inställningar på svenska och engelska. Experimentell beta,
publicerad på uttrycklig begäran. SimpleUI av doctorhetfield-cmd och Bookshelf
av AndyHazz, med respektive bidragsgivare, ingår i denna fristående kombination;
detta är inte en officiell release från något av originalprojekten.

- Fem tydliga områden: Hem (SimpleUI), Bookshelf, Navigation och gränssnitt,
  Integrationer samt System och underhåll. Avancerade originalinställningar
  finns kvar. Boksökning ligger under Bookshelf, separat från inställningssökning.
- Lokal inställningssökning förstår svenska och engelska oavsett valt menyspråk.
  Den söker i fasta menytexter, inte privata inställningsvärden eller nätkonton.
- Omfattningen visas tydligare: gemensamma Bookshelf-inställningar, ett visst
  bibliotek/en viss hylla, delat tema eller SimpleUI-skärmar.
- Direktreglage för bokpanelens innehåll, bland annat genre och andra etiketter.
  Håll på bokpanelen för att anpassa den; originalets bokåtgärd finns också kvar.
  Hyllans långtrycksmeny har en tydligare genväg till dess anpassning.
- Tillbaka går till föregående inställningsnivå och sökningen minns söktexten.
  Fördröjda inställningssidor får inte täcka en nyare destination.

Starta om KOReader efter uppdateringen. Använd OrbitUI:s gemensamma uppdaterare
med förhandsversioner aktiverade, eller hela **orbitui.koplugin.zip** (inte
källkodsarkivet). Följ verifierings-/omstartsanvisningar vid extern installation.
För att dölja genren: Bookshelf → Bokpanelen överst → stäng av Visa genrer.
Du kan också hålla på bokpanelen och välja Anpassa bokpanelen.

Sparade layouter, profiler/chip, typsnitt, teman, bokdata och länkar behålls;
ingen inställningsåterställning, cachetömning eller ny indexering görs.
Omslagsfixen från Beta 12 och Android safe mode-skydden finns kvar. Ingen ny
upstream-merge. Kodåterställning rullar inte tillbaka läsframsteg eller inställningar.

## English

Clearer OrbitUI settings in Swedish and English. Experimental prerelease,
published on explicit request. Includes and adapts SimpleUI by doctorhetfield-cmd
and Bookshelf by AndyHazz, with their contributors; this independent combined
plugin is not an official release from either upstream project.

- Five areas: Home (SimpleUI), Bookshelf, Navigation & interface, Integrations,
  and System & maintenance. Native advanced controls remain available. Book
  search is under Bookshelf, separate from settings search.
- Local settings search understands Swedish and English independently of the
  UI language. It indexes static labels, not private setting values/accounts.
- Scope headers distinguish shared Bookshelf settings, individual libraries/
  shelves, the shared theme, and SimpleUI screens.
- Direct book-panel visibility controls, including genres and other labels.
  Hold the book panel to customize it or use the original book action. Shelf
  long-press retains its actions with a clearer customization shortcut.
- Back returns to the previous settings level; search retains its query.
  Stale deferred settings pages cannot cover a newer destination.

Restart KOReader after updating. Use the common OrbitUI updater with preview
releases enabled, or the complete **orbitui.koplugin.zip**, not a source archive.
Follow external-install verification/restart prompts. To hide the genre:
Bookshelf → Book panel at the top → turn off Show genres.
Alternatively, hold the book panel and choose Customize book panel.

Existing layouts, profiles/chips, fonts, themes, reading data and links remain
intact. No preference reset, cache wipe or reindexing is performed. Beta 12's
cover fix and Android safe-mode guards remain. No new upstream merge. Code
rollback does not restore older reading progress or settings.

## Verification / verifiering

Release gates cover both complete Lua/LuaJIT suites, translations, sealed bytes,
native older-installer upgrade/rollback, history/artwork/secrets, CI and exact
draft/public asset verification. These are not physical-reader tests. Actual
SV/EN pagination, touch/hold, SimpleUI custom-screen return, shared themes,
reader return, rotation and sleep/wake still need Boox/Bigme acceptance.

Bootstrap/API 1 and older releases stay unchanged. This release uses all 2,000
installed API 1 file slots, including its manifest; future packages require a
reviewed compatibility plan before adding runtime files.

Bookshelf `c37580a1ca5040d2423e45b9bdd429776117f3c1` (6.0.3),
SimpleUI `b1580f90b2e17cf03a66c744c323a1df66d77100` (3.0 follow-ups).

# v0.1.0-beta.12 · 2026-10-26

# OrbitUI 0.1.0-beta.12

Local Bookshelf covers with Android safe mode still enabled. Experimental
prerelease, explicitly requested for the reported Boox cover problem.

OrbitUI includes and adapts **SimpleUI by doctorhetfield-cmd** and **Bookshelf
by AndyHazz**, with their contributors' work. This is an independent combined
plugin, not an official release by either upstream project.

## What changes

- Android safe mode previously blocked Bookshelf's automatic metadata/cover
  extraction altogether. Local covers now load one document at a time between
  UI turns, without forking a background process or using BIM's subprocess-only
  extractor. The Android safety preference is not changed.
- The visible page and large current-book image get appropriately sized source
  images. Small cached thumbnails can be replaced with sharper originals;
  refreshing metadata does not downgrade an already larger cached thumbnail.
  A low-resolution original cannot gain real detail by being enlarged.
- Single-book and selected-book Refresh metadata keep the previous database row
  and scaled cover until a replacement is saved successfully. Failed loading,
  decoding or database writes do not first erase the old cover. Custom covers,
  ignore flags, reading data, links and settings remain intact.
- Queues are capped at 256 local books, cancelled when Bookshelf is covered,
  closed, suspended or a reader is opened, and yield between documents. Keep
  Bookshelf open to finish an explicitly requested refresh. Failures can be
  retried; provider-stream formats are excluded, with no automatic network work.
- Bookshelf's old full-library metadata scanner launches subprocesses even in
  safe mode. It now explains page-by-page loading instead of launching that
  scanner while Android safe mode is enabled. Other KOReader/plugin indexers
  are outside this guard.

## After updating

Restart KOReader and leave **Android safe mode enabled**. Open Bookshelf and
pause on a page to let its local covers load. Browse other pages as needed;
do not clear the cover database or repeat a full-library scan. For a stubborn
book, long-press it and choose **Refresh metadata**. Existing selected-book
refresh uses the same safe queue (maximum 256 books per request).

SimpleUI's separate Android background-extraction block remains in place;
Home can reuse covers saved by Bookshelf, but this is not a new Home indexer.
Non-Android and explicitly disabled-safe-mode paths retain native behavior.

Use OrbitUI's common updater with preview releases enabled, or install the
complete **orbitui.koplugin.zip**, not a source archive. Preserve hidden version
directories and settings; follow external-install verification/restart prompts.
Bootstrap/API 1 and older published releases are unchanged. Code rollback does
not reset reading progress or settings.

## Verification and limits

Regression coverage includes native-sized/coverless images, larger-cache
preservation, custom-cover handling, actual single/bulk refresh callbacks,
SQLite savepoint rollback, resource cleanup, read-only parked-reader access,
bounded/cancellable queues and unchanged native fallback. Release gates also
include complete Lua/LuaJIT suites, translations, sealed-byte checks, older
native installers, exact draft/public assets, history/artwork/secrets and CI.

These are headless/native-service tests, not a physical Boox or Bigme session.
One document load runs synchronously and cannot be interrupted midway; large
or damaged files may still pause the UI or expose native-engine defects.
Actual cover quality, input responsiveness, memory, rotation, sleep/wake and
reader-return acceptance remain to be checked on the affected devices. No
measured speed improvement or complete Android-crash fix is claimed.

No upstream merge: Bookshelf `c37580a1ca5040d2423e45b9bdd429776117f3c1` (6.0.3),
SimpleUI `b1580f90b2e17cf03a66c744c323a1df66d77100`.

# v0.1.0-beta.11 · 2026-10-26

# OrbitUI 0.1.0-beta.11

One accurate OrbitUI updater, clearer GitHub errors, and the reviewed October 26
Bookshelf/SimpleUI updates. This remains an experimental prerelease.

OrbitUI includes and adapts **SimpleUI by doctorhetfield-cmd** and **Bookshelf
by AndyHazz**, with their contributors' work. This is an independent combined
plugin, not an official release by either upstream project.

## Updates and recovery

- Bookshelf's embedded update page now uses OrbitUI's real running version,
  preview-release preference, daily online checks and recovery controls. It no
  longer presents Bookshelf's version as the OrbitUI version or offers obsolete
  standalone branch/channel, wake notification and changelog controls.
- Root and embedded update menus share the same controls. Existing OrbitUI
  preview/daily preferences are retained; unrelated Bookshelf settings are not
  rewritten. Standalone component behavior outside OrbitUI is unchanged.
- GitHub 403/429 rate-limit responses show a readable reason and bounded retry
  wait. Checks in the same running session respect GitHub's retry/reset hints.
  Generic 403s are not incorrectly labelled as confirmed rate limits. No raw
  response body, signed URL or Lua source path is shown for these HTTP failures.
- TLS, host allowlisting, archive/hash/inventory checks, deferred activation and
  rollback remain in force. This cannot guarantee that GitHub or a network will
  accept a request; a blocked device must wait or resolve the network restriction.

## Reviewed upstream changes since Beta 10

- Bookshelf 6.0.3 corrects image-screensaver wake repaint and fullscreen status
  strip taps. Modules among books have an independent, non-destructive switch
  and load even when the other module surfaces are disabled.
- SimpleUI adds a categorized module picker, optional free widths/stacking,
  library wallpaper opacity, later-page statistics refresh and corrected Flow
  night-mode cover colours. OrbitUI's existing layouts and independent margins
  remain unchanged until explicitly edited.
- Fast Book Closing exposes SimpleUI's already-present Home soft-parking as a
  saved option, off by default. It keeps Home in RAM while reading; it does not
  replace Bookshelf's existing fast-return/deferred-close mechanism. Extra RAM
  use and reader/suspend/rotation behavior still need physical-device testing.

Saved profiles/chips/navigation, bindings/series boxes, ornaments/fonts, reading
data and optional BookOrbit/MAL/patch integrations are retained. No automatic
rescan, cache reset, settings migration or bootstrap/API change is included.

## Install

Open **Tools > OrbitUI > Uppdatera OrbitUI**, enable preview releases, check for
updates and restart KOReader. Existing Beta 9/Beta 10 installations need no
bridge. If the old updater is blocked by GitHub, wait before retrying; its old
error dialog cannot be repaired until the new runtime is installed. Manual
installation must use **orbitui.koplugin.zip**, not a source-code archive. Keep
hidden version directories and settings; follow the external-update verification
and additional restart prompt. Never delete the plugin to work around a 403.

## Verification and limits

Release gates cover both complete Lua/LuaJIT suites, translations, sealed-byte
Home/navigation/update regressions, clean source/inventory/history/artwork/secret
audits, exact draft/public assets, main/tag CI and actual older native installers'
upgrade/restart/rollback and external-runtime adoption. These use temporary
installations and native-service fixtures, not physical readers.

The photo alone does not establish why that device received 403. Real Boox/Bigme
update dialogs, network restrictions, reader/suspend/rotation, wallpaper/night,
module switches and optional Fast Book Closing still need device acceptance.
No measured speedup or native Android crash fix is claimed. Older public tags
and assets are immutable; code rollback retains current reading data/settings.

Bookshelf Git: `c37580a1ca5040d2423e45b9bdd429776117f3c1`.
SimpleUI Git: `b1580f90b2e17cf03a66c744c323a1df66d77100`.

# v0.1.0-beta.10 · 2026-10-25

# OrbitUI 0.1.0-beta.10

Reviewed Bookshelf 6.0.2 fixes, with OrbitUI's working Home and navigation retained.

OrbitUI includes and adapts **SimpleUI by doctorhetfield-cmd** and **Bookshelf
by AndyHazz**, with their contributors' work. This is an independent combined
plugin, not an official release by either upstream project.

## Changes since Beta 9

- **Metadata and cover refresh:** Bookshelf 6.0 could delete a metadata row but
  keep answering from an old in-memory batch, preventing re-extraction. Single
  and bulk Refresh metadata, stale-cover cleanup and cover reversion now forget
  that row; the hero discards its old book memo when extraction completes.
  This fixes a specific refresh failure, not every possible missing cover.
- **Colour-cover repaint:** clipped status updates no longer paint cover shadows
  outside their refresh area and over the covers. Unknown drawing methods fall
  back to full painting instead of silently drawing unclipped.
- **E-ink status updates:** measure the status strip even before its new widgets
  have painted; avoid unnecessarily refreshing the whole right column/screen.
  Clock/device-state ticks update the tree without panel refreshes underneath
  another window. Closing it repaints current content; live previews still work.
- **Micro-modules:** public `ctx.open_book` / `ctx.show_book` helpers retain the
  usual shelf/ReaderUI opening path. Fullscreen taps report their actual surface.
  Keyboard/d-pad focus can reach the fullscreen pencil and editor toolbar/footer.
  These are Bookshelf's modules, not changes to Home/Bento's editor.

Bookshelf advances by eight reviewed Git commits to 6.0.2. SimpleUI is already
current and does not change. Existing profile/chip IDs, saved navigation bars,
Home/Bento geometry, bindings, series-box aspect/labels/ratings, ornaments,
fonts, reading data and optional BookOrbit/MAL/Patch Manager integrations remain.
No new runtime module, settings/data migration, automatic scan, cache reset or
bootstrap/API change is included.

## Install or update

Enable preview releases in **Tools > OrbitUI > Uppdatera OrbitUI**, check for
updates and restart KOReader. Beta 9 and Beta 5 can update directly; no bridge
or settings reset is needed. Keep a separate settings backup.

For a first installation, download **orbitui.koplugin.zip**, not a source-code
archive. Disable standalone SimpleUI/Bookshelf, keep KOReader's **Cover browser**
enabled and restart. See the
[installation guide](https://github.com/komadorirobin/orbitui.koplugin/blob/v0.1.0-beta.10/README.md#installation).

For a missing/stale cover, try the book's **Refresh metadata** after updating.
For a full local index, use the library section's **Library & search > Scan all
library metadata** control. The scan uses KOReader's configured home directory,
not only that profile's folders; check that scope first. Choose refresh if
existing rows need updating, avoid pruning unless intended, and let it finish.
This is local metadata work, not Hardcover synchronization or a reading-data reset.

## Verification and limitations

Release gates include both complete Lua/LuaJIT suites, all original component
tests and translations, packaged Home/navigation/module-opening regressions,
clean inventory/source and outgoing history/artwork/secret audits, exact
draft/public downloads, main/tag CI and real public Beta 9/Beta 5 native OTA
upgrade/restart/rollback and external-runtime adoption.

Native services/rendering are stubbed in the four new whole-module integration
cases. Native OTA tests use isolated temporary installations, not a reader.
The user confirms Home and Beta 9 navigation work on Boox; the reported missing
covers still need retesting after this update. Colour repaint, covered clock
ticks, module keys/rotation and broader Bigme/external-plugin acceptance remain
open. No measured speedup or resolution of the earlier native Android mutex
abort is claimed. This remains a prerelease.

Bookshelf Git: `5f726c253c5cb4d5a2a2137af52731562e1cb9b7`.
SimpleUI Git: `40b301f0f5e4466021d00b4e47ac8c09bb65ac8c`.

Code rollback retains reading data and does not undo later settings edits.
Releases older than Beta 9 do not recognize the generic Bookshelf action and
may prune that button; reselect an older saved-profile action if needed.
Existing public tags and assets remain unchanged.

# v0.1.0-beta.16 · 2026-10-28

## Svenska

- Läsöversikt begär nu bara statistik, bokräkning och senaste-böcker-data för kort som behöver dem.
- Nya frivilliga **Adaptiv minneshantering** och **Snabbhetsläge** under **OrbitUI-inställningar → System och underhåll → Snabbhet, minne och diagnostik**. Befintligt beteende är standard. Snabbhetsläget stänger av svepanimationer och spekulativ förladdning; kalla sidladdningar kan därför ta längre tid.
- Lokal prestandamätning och kopierbar rapport utan boknamn, sökvägar, konton eller uppladdning. Mätningarna gäller synkrona anrop, inte skärmens totala svarstid.
- Ny snabbguide för Hem (SimpleUI), Bookshelf-profiler, chip, navigationsknapp och snabb återgång från en bok. Alla nya kontroller och hjälptexter finns på svenska och engelska.
- Mindre releasepaket: bara utvecklarnas fil-/radreferenser utelämnas ur översättningsfilerna. Alla språk, texter, bilder, typsnitt och licensuppgifter behålls.
- Säkrare lagringsstädning: efter verifierad start kan högst en gammal, oanvänd kodkopia tas bort. Fabrikskopia, aktiv version, återställningsversion och okända/ändrade filer behålls. Inställningar, läsdata, omslagscache och tilläggsbilder rörs inte.

Android safe mode, omslagskvalitet och snabb återgång till rätt profil/chip/hyllposition behålls. Inga nya upstream-importer; samma granskade Bookshelf 6.0.4 och SimpleUI 3.0.1-uppföljning som Beta 15 ingår.

**Uppdatera via förhandskanalen och starta om KOReader.** För manuell installation: välj `orbitui.koplugin.zip`, inte GitHubs källkodsarkiv. Ta en separat säkerhetskopia av KOReaders data. Detta är en förhandsversion; fysisk Boox/Bigme-kontroll av snabbhet, minne, skärm och lagringsbeteende återstår. Ingen uppmätt enhetsvinst utlovas.

## English

- Reading dashboard data demands follow visible cards and the selected goal owner; hidden cards no longer request unnecessary statistics, book counts or recent-book candidates.
- Optional **Adaptive memory** and **Responsive** profiles: **OrbitUI settings → System & maintenance → Speed, memory & diagnostics**. Existing behaviour remains the default. Responsive skips Bookshelf wipe animations and speculative next-page/chip preload; cold page loads may take longer.
- Opt-in, bounded local call timings and a viewable/copyable performance report. No book names, paths, accounts, raw errors or upload. Synchronous call timings are not end-to-end display latency; Lua heap is not total RAM.
- Bilingual Home/Bookshelf quick guide for library profiles, chip sources, navigation and reader return.
- Smaller package without removing languages, messages, images, fonts or licenses: only developer source-location comments are omitted from packaged translation catalogs.
- After healthy startup, at most one verified strictly older unused code snapshot can be collected. Factory/current/rollback, pending/newer code and unknown/modified files stay protected. No books, settings, reading data, cover caches or add-on artwork are cleanup targets.

Keeps Android safe mode, cover quality, fast profile/chip/page return and external sync ownership. No new upstream import; retains Bookshelf `d07905ba` (6.0.4) and SimpleUI `22d5a3d2` (3.0.1 follow-up).

**Update on the preview channel and restart KOReader.** Use `orbitui.koplugin.zip` for manual installation, not GitHub's source archive. Bootstrap/API 1 and all 2,000 installed paths are unchanged. Earlier public releases remain immutable. Code rollback retains later settings and reading progress; keep an independent data backup.

Automated Lua/LuaJIT, translation/package/source/history and native older-installer upgrade/rollback checks are separate from physical-reader acceptance. Boox/Bigme performance, native image pressure, UI/display and storage acceptance remain outstanding; no measured device speed/RAM improvement is claimed.

# v0.1.0-beta.15 · 2026-10-28

## Svenska

- **Färg i Läsöversikt:** välj Av, Accenter eller Tonade kort under **OrbitUI-inställningar > Hem (SimpleUI) > Läsöversikt > Kortfärger**, eller i modulens egna inställningar. Tonade kort ger pastellbakgrunder och färgade ramar/indikatorer. Valet gäller den aktuella läsöversikten, inte hela gränssnittet.
- **Omslagsfärgat Fortsätt läsa-kort:** ett färgat omslag kan ge kortet en passande mörk nyans. Mörkt/ljust kort, rubriker, layout, bokkällor, öppna/långtryck och oberoende bläddring behålls. Svartvita skärmar och avstängd färgrendering behåller gråskalan; nattläget får egna nyanser.
- **Senaste granskade upstream:** Bookshelf 6.0.4 med färgfixar, mindre onödiga helskärmsblinkningar och sökbar samlingshantering. SimpleUI får rättningar av minnesläckor/sidpilar, uppskjuten fillistning, färre onödiga omslagsuppdateringar, bakgrundsdithering, valfri sidblinkning och Hazel.
- Våra profil-/snabbstängningsfixar, Android safe mode/omslagsfixen, Home/Bento, serieboxar/ornament och BookOrbit/MAL-kopplingar är kvar.

**Befintliga installationer behåller Av tills du väljer färg.** Uppdatera via OrbitUI med förhandsversioner tillåtna och starta om KOReader. Ingen återställning eller ny indexering krävs för färgerna.

## English

- **Reading dashboard card colours:** Off, Accents or Tinted cards, scoped to each Home/Custom Screen. Existing installations remain Off until explicitly changed. Find it in **OrbitUI settings > Home (SimpleUI) > Reading dashboard > Card colours**, or the module's own settings.
- Optional cover-derived continue-reading colour, native monochrome fallback and day/night palettes. Existing dark/light hero, layout, headings, sources, independent row paging and book actions are retained. This is an independent OrbitUI implementation inspired by BookOrbit's colour-board options; no BookOrbit code, palette or artwork is imported.
- Includes reviewed **Bookshelf 6.0.4** through `d07905ba932e09044827aadf480c188a5d324b96` and **SimpleUI 3.0.1 follow-up** through `22d5a3d2dd7be4651e718eb49027d82f68b3ace7`. Fast profile return, settings improvements, safe Android covers, Home/Bento and external sync owners remain intact.

Install **orbitui.koplugin.zip**, not GitHub's source archive. Existing supported betas can update on the preview channel; restart KOReader. Bootstrap/API 1, installer limits and the complete 2,000-file installed path set are unchanged. No settings, progress, links, caches or artwork are reset. Code rollback preserves later data/settings changes; older builds ignore the new scoped colour choice.

This is a **prerelease**. Automated Lua/LuaJIT, contrast/native-UI-boundary, package and native archive/OTA checks are not physical display acceptance. Actual Boox/Bigme colour strength, night-mode rendering, ghosting, responsiveness and touch/rotation/sleep checks remain outstanding. SVG schematics use synthetic covers and approximate text; they are not device screenshots or performance measurements.

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

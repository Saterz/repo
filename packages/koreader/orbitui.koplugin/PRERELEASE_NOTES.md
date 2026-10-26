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

# v0.1.0-beta.9 · 2026-10-25

# OrbitUI 0.1.0-beta.9

Bookshelf is a direct, configurable navigation destination.

OrbitUI includes and adapts **SimpleUI by doctorhetfield-cmd** and **Bookshelf
by AndyHazz**, with their contributors' work. This is an independent combined
plugin, not an official release by either upstream project.

## Changes since Beta 8

- Adds a first-class **Bookshelf** action that works without a `prose` or
  `comics` profile, even when no library sections have been configured. It opens
  native Bookshelf without forcing a profile or resetting its last view.
- New/default bars and the fresh setup guide include a removable Bookshelf
  button. **Existing saved bars are not rewritten.** Explicit removal persists.
  The separate file browser is labelled **File browser**, retaining custom labels.
- **OrbitUI settings > Bookshelf navigation** toggles the button and chooses its
  destination: native Bookshelf or an enabled, saved profile. Long-press the
  Bookshelf button to reach the same settings.
- Each library section/profile offers **Add to navigation bar** and **Use for
  Bookshelf button**. Create Prose, Manga or any other profiles, each with its
  own folders and chips. Several profiles can have separate buttons; a full bar
  asks which existing button to replace. No raw action IDs or custom QAs needed.
- Missing/disabled legacy targets such as `open_bookshelf_prose` explain the
  problem and offer configuration instead of silently doing nothing. A new
  section named Prose does not magically acquire the legacy internal ID `prose`.
- Existing profile/chip IDs, aliases, labels, icons, navigation choices, reading
  data, links, artwork, fonts and external integrations are retained. Explicit
  profile selection uses the normal reader/parking lifecycle and deferred
  coordinator; specific profile tabs take priority over the generic indicator.

No upstream import, component source/pin change, bootstrap/API change or data reset.

## Install or update

Enable preview releases in **Tools > OrbitUI > Uppdatera OrbitUI**, check for
updates and restart KOReader. Beta 8 and Beta 5 can update directly; no bridge
or settings reset is needed.

**For an existing installation:** open **OrbitUI settings > Bookshelf navigation**
(**Bookshelf i navigationsraden**). Enable **Show Bookshelf in navigation bar**,
then choose **Destination** (**Öppnar**). To configure Prose/Manga etc., open
**Profiles and chips** (**Profiler och chip**), choose folders and add shelves.
Each profile can be added directly as a separate navigation button.

If an old custom button still points to `open_bookshelf_prose`, replace that
slot with **Bookshelf** or the NAME of your saved profile. Existing bars are
preserved deliberately, not automatically repaired or replaced.

For a first installation, download **orbitui.koplugin.zip**, not a source-code
archive. Disable standalone SimpleUI/Bookshelf, keep KOReader's **Cover browser**
enabled and restart. See the
[installation guide](https://github.com/komadorirobin/orbitui.koplugin/blob/v0.1.0-beta.9/README.md#installation).

## Verification and limitations

Twelve focused navigation cases load complete SimpleUI config/QA modules, the
real library model/profiles, bridge and host adapters. They cover empty and
home-based inventories, missing legacy targets, saved-bar/label/icon preservation,
persistent removal, profile chips/targets, explicit full-bar replacement,
disabled profiles, indicators, simulated parked-reader enforcement and stale
selection cancellation. Native delivery/rendering/lifecycle services are stubbed.

Release gates include both complete Lua/LuaJIT suites, translations, packaged-byte
navigation/Home regressions, sealed inventory/source comparison, outgoing
history/artwork/secret audits, exact draft/public assets, main/tag CI and native
OTA upgrade/restart/rollback from public Beta 8 and Beta 5.

The user confirms Beta 8 Home works on the affected Go Color 7. This new
navigation/profile flow still needs physical Boox and Bigme testing, including
reader return, rotation and dock indicators. It does not establish resolution
of the earlier unrelated native Android mutex abort.

Bookshelf Git: `fc1103a3de9fd19eea89a53c5f1f1b0e8175682a`.
SimpleUI Git: `40b301f0f5e4466021d00b4e47ac8c09bb65ac8c`.

This remains a prerelease. Code rollback retains reading data and does not undo
later settings edits; keep a separate backup.
Older releases do not recognize the new generic Bookshelf action ID. After a
code rollback they may prune that button; choose an older saved-profile action
again if needed. Keep a backup of navigation choices before testing rollback.

# v0.1.0-beta.8 · 2026-10-25

# OrbitUI 0.1.0-beta.8

Fixes Home failing to load with a missing `Blitbuffer` error.

OrbitUI includes and adapts **SimpleUI by doctorhetfield-cmd** and **Bookshelf
by AndyHazz**, with their contributors' work. This is an independent combined
plugin, not an official release by either upstream project.

## Changes since Beta 7

- Imports KOReader's `ffi/blitbuffer` explicitly in the shared screen engine.
  Its module-level colour initialization otherwise fails at line 288 with
  `attempt to index global 'Blitbuffer' (a nil value)`, before Home can open.
  This matches the newly supplied device photo; the defect also exists in Beta 5.
- Adds whole-module cold-load regressions without ambient `Blitbuffer` or
  `logger`, followed by actual Home/Custom Screen open paths. The previous
  first-run tests extracted the open factory and missed module initialization;
  they remain alongside this new coverage.
- The runtime change is one import. No changes to layouts, settings, reading
  data, links, artwork, fonts, external integrations, upstream pins or bootstrap
  API 1. Beta 7's first-run logger fix and guarded error reporting are retained.

## Install or update

Enable preview releases in **Tools > OrbitUI > Uppdatera OrbitUI**, check for
updates and restart KOReader. Beta 5 and Beta 7 can update directly; no bridge
or settings reset is needed.

For a first installation, download **orbitui.koplugin.zip**, not a source-code
archive. Disable standalone SimpleUI/Bookshelf, keep KOReader's **Cover browser**
enabled and restart. See the
[installation guide](https://github.com/komadorirobin/orbitui.koplugin/blob/v0.1.0-beta.8/README.md#installation).

## Verification and limitations

The whole-engine cold-load regression reproduces the photographed error before
the import and passes afterward in both Lua and LuaJIT. It loads the complete
engine, Home facade and navigation module; native construction/rendering and
surrounding services are stubbed, not a physical KOReader session. Coverage
includes fresh/existing onboarding states, shared identity, cached state,
callbacks and separate Custom Screen state.

Release gates include both complete suites, translations, sealed inventory,
history/artwork/secret audits, exact draft/public assets, main/tag CI and native
OTA upgrade/restart/rollback from public Beta 5 and Beta 7.

The photographed Lua loading error is reproduced and fixed. The separate native
Android mutex abort in earlier logs is not proven resolved. Retest Home on the
affected Go Color 7; wider Bigme/Android physical acceptance remains open.
If it still fails, capture the detailed error/new log without deleting settings.

Bookshelf Git: `fc1103a3de9fd19eea89a53c5f1f1b0e8175682a`.
SimpleUI Git: `40b301f0f5e4466021d00b4e47ac8c09bb65ac8c`.

This remains a prerelease. Code rollback retains reading data and does not undo
later settings edits; keep a separate backup.

# v0.1.0-beta.7 · 2026-10-25

# OrbitUI 0.1.0-beta.7

First-run Home crash fix and actionable Home error diagnostics.

OrbitUI includes and adapts **SimpleUI by doctorhetfield-cmd** and **Bookshelf
by AndyHazz**, with their contributors' work. This is an independent combined
plugin, not an official release by either upstream project.

## Changes since Beta 6

- Fixes a reproduced first-run crash: Home used `logger` without importing it
  when SimpleUI onboarding was not already marked complete. Existing configured
  installations could bypass that branch. The same defect was present in Beta 5.
- Home load errors now show their actual first error in a persistent message
  and record a traceback, including automatic startup, wake and reader-return
  entry points. The first cause survives LuaJIT's generic previous-load errors.
- Home construction/initial-show/first-run-hook errors are caught. A failed
  partial Home is closed without scheduling another Home or deleting settings.
  Only newly failed values for the owned Home/engine modules are cleared;
  valid tables, pre-existing values and third-party module state are retained.
- Keeps Home's shared engine identity, callbacks, optional cached BookOrbit
  refresh and host-owned setup. Layouts, libraries, links, reading data, artwork,
  fonts, component pins and the separate add-on channel are unchanged.

No new upstream import, native Android library change or bootstrap/API change.

## Install or update

Existing OrbitUI users: use **Tools > OrbitUI > Uppdatera OrbitUI**, enable
preview releases, check for updates and restart KOReader. Beta 5 and Beta 6 can
update directly; no bridge is needed. Do not reset settings to try this fix.

For a first installation, download **orbitui.koplugin.zip**, not a source-code
archive. Disable standalone SimpleUI/Bookshelf, keep KOReader's **Cover browser**
enabled and restart. See the
[installation guide](https://github.com/komadorirobin/orbitui.koplugin/blob/v0.1.0-beta.7/README.md#installation).

## Verification and limitations

The new first-run regression fails before the fix and passes afterward under
Lua and LuaJIT. It executes the actual Home facade and generic open factory
with native services stubbed, covering nil/false/true onboarding states,
host-owned onboarding, failed construction/show/hooks, cleanup/notification
failures, real require retries and preservation of other plugin state.
Release gates include both complete suites, translations, sealed inventory,
outgoing-history/artwork/secret audits, exact draft/public assets, main/tag CI
and native OTA upgrade/restart/rollback from public Beta 5 and Beta 6.

These are headless checks. The reported Android `pthread_mutex_lock called on
a destroyed mutex` crash lacks a matching Lua traceback in the provided logs;
this release does not claim that native crash is fixed. Please retest Home on
the affected device. If Home still fails, capture the detailed message or new
log rather than deleting settings. Wider Bigme/Android acceptance remains open.

Bookshelf Git: `fc1103a3de9fd19eea89a53c5f1f1b0e8175682a`.
SimpleUI Git: `40b301f0f5e4466021d00b4e47ac8c09bb65ac8c`.

This remains a prerelease. Code rollback retains reading data and does not undo
later settings edits; keep a separate backup.

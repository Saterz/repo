# v0.2.1 · 2026-10-15

## Changes

- Keep KOReader's frontlight on/off queries and toggles synchronized with the Kindle's current hardware state, including changes made by native auto-brightness. Preserve remembered brightness when the light is off. Fixes #6.
- Remove three forced line breaks from the brightness and scheduled-warmth help popups so sentences wrap to the available width. Thanks to @mergen3107 for #5.

## Installation

Extract `kindle-auto-brightness-bridge-v0.2.1.zip` into KOReader's `plugins` directory, replacing the existing `kindleautobrightness.koplugin` files, then restart KOReader. Existing settings are preserved.

## Validation

- All 33 regression tests pass on the merged release source against the local KOReader source snapshot.
- Lua syntax and whitespace checks pass. The ZIP contains exactly the two plugin modules, byte-for-byte identical to the release source.
- The frontlight on/off change was previously verified in the running KOReader session on the target Kindle with 18 device checks.
- This release's plugin files were installed on the Kindle running KOReader v2026.07.2, with native Lua syntax checks and SHA-256 verification. The help-text change was not newly rendered on the device during this release.

# v0.2.0 · 2026-08-27

## What changed

- Added optional warmth synchronization for supported Kindles with warm frontlights.
  - Uses KOReader's public hardware warmth reader and existing conversion.
  - Reads the Kindle's currently applied hardware warmth only when KOReader asks.
  - Runs no background polling and writes no warmth merely to synchronize.
  - Has a separate setting and is disabled by default.
- Added native long-press help to the existing brightness synchronization menu item.
- Documented the interaction with KOReader AutoWarmth: the two schedulers remain independent.

## Validation

- 21 plugin tests pass against KOReader.
- Luacheck reports 0 warnings and 0 errors.
- Live-tested on the target Kindle running KOReader v2026.07.2.

Closes #1.
Closes #2.

# v0.1.0 · 2026-08-25

Initial public release.

## What it does

- Keeps KOReader synchronized with brightness changes made by Amazon powerd.
- Fixes stale-cache jumps for relative brightness gestures.
- Uses zero polling and no custom lux-to-brightness algorithm.
- Preserves frontlight off/on remembered brightness.
- Supports Kindles whose native ALS is available even when KOReader model detection is incomplete.
- Places the opt-in checkbox under Tools → More tools without an orphaned NEW prefix.

## Verification

- 12 focused Busted specs passed against current KOReader DeviceListener code.
- LuaJIT syntax and Luacheck passed with zero warnings/errors.
- Physically verified on KOReader v2026.07.2 / KindlePaperWhite6: startup 11, external Amazon powerd change 20, real KOReader +1 gesture 21, matching notification.

## Install

Extract the archive and copy `kindleautobrightness.koplugin/` into KOReader’s `plugins/` directory, restart KOReader once, then enable **Synchronize with Kindle Auto Brightness** under **Tools → More tools**.

Enable Auto Brightness in the stock Kindle UI before starting KOReader.

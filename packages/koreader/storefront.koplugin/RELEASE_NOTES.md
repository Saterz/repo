# 26.10.20 · 2026-10-20

## What's Changed
* Fix archive root detection for plugins with embedded components by @komadorirobin in https://github.com/ultimatejimmy/storefront.koplugin/pull/5078
* Fix patch update logic https://github.com/ultimatejimmy/storefront.koplugin/issues/5076
* Fix updates with native libraries https://github.com/ultimatejimmy/storefront.koplugin/issues/5077
* Catalog logic tweak
* memory fix

## New Contributors
* @komadorirobin made their first contribution in https://github.com/ultimatejimmy/storefront.koplugin/pull/5078

**Full Changelog**: https://github.com/ultimatejimmy/storefront.koplugin/compare/26.10.16...26.10.20

# 26.10.16 · 2026-10-16

## What's Changed
* Keep bundled-catalog fallback stale in background update by @danihrndzld in https://github.com/ultimatejimmy/storefront.koplugin/pull/5074
* Persist catalog ETags saved in the background subprocess by @danihrndzld in https://github.com/ultimatejimmy/storefront.koplugin/pull/5075

## New Contributors
* @danihrndzld made their first contribution in https://github.com/ultimatejimmy/storefront.koplugin/pull/5074

**Full Changelog**: https://github.com/ultimatejimmy/storefront.koplugin/compare/26.10.13...26.10.16

# 26.10.13 · 2026-10-13

## What's Changed
* sk: translate "plugin" as "doplnok", translate [draft] by @misko903 in https://github.com/ultimatejimmy/storefront.koplugin/pull/5069
* Show download progress while installing plugins by @dmaglio in https://github.com/ultimatejimmy/storefront.koplugin/pull/5070
* Fix font issue when a font is missing #5071 
* Various memory and performance improvements 

## New Contributors
* @misko903 made their first contribution in https://github.com/ultimatejimmy/storefront.koplugin/pull/5069
* @dmaglio made their first contribution in https://github.com/ultimatejimmy/storefront.koplugin/pull/5070

**Full Changelog**: https://github.com/ultimatejimmy/storefront.koplugin/compare/26.10.2...26.10.13

# 26.10.2 · 2026-10-02

- Address memory issues with lower powered devices
- Add check for RB catalog to not download/refresh if there are no changes
- fix bug in rating system

**Full Changelog**: https://github.com/ultimatejimmy/storefront.koplugin/compare/26.10.1...26.10.2

# 26.10.1 · 2026-10-01

## What's new
- Add Readerbackdrop as an additional source for screensavers, open the filter dialog to change the sources
- Move refresh button to the top level of settings

## Bug fixes
- Fix refresh timestamp
- Update some translations #5066 
- Updated catalog refresh logic to be more consistent and follow the notification frequency settings
- Made sure screensaver catalog is updated at the same time
- Minor performance improvement when removing a screensaver from the collection

**Full Changelog**: https://github.com/ultimatejimmy/storefront.koplugin/compare/26.9.25.1...26.10.1

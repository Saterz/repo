# 26.10.17-beta · 2026-10-16

- Catalog logic tweak
- memory fix

**Full Changelog**: https://github.com/ultimatejimmy/storefront.koplugin/compare/26.10.16...26.10.16-beta2

**Full Changelog**: https://github.com/ultimatejimmy/storefront.koplugin/compare/26.10.16...26.10.16.1-beta

**Full Changelog**: https://github.com/ultimatejimmy/storefront.koplugin/compare/26.10.16...26.10.17-beta

# 26.10.15-beta · 2026-10-16

## What's Changed
* Keep bundled-catalog fallback stale in background update by @danihrndzld in https://github.com/ultimatejimmy/storefront.koplugin/pull/5074
* Persist catalog ETags saved in the background subprocess by @danihrndzld in https://github.com/ultimatejimmy/storefront.koplugin/pull/5075

## New Contributors
* @danihrndzld made their first contribution in https://github.com/ultimatejimmy/storefront.koplugin/pull/5074

**Full Changelog**: https://github.com/ultimatejimmy/storefront.koplugin/compare/26.10.13...26.10.15-beta

# 26.10.11-beta2 · 2026-10-11

- add more memory leak guards around sleeping/waking

**Full Changelog**: https://github.com/ultimatejimmy/storefront.koplugin/compare/26.10.10-beta3...26.10.11-beta2

# 26.10.10-beta3 · 2026-10-11

### Improvements and Fixes

- **Fixed Kindle sleep freeze and lockups**: Resolved an issue where putting the device to sleep while Storefront was updating or loading images in the background could cause the device to freeze completely.
- **Fixed dual screensaver collision**: Addressed a memory spike on low-RAM Kindles that caused the Kindle system software to crash in the background and display the stock Amazon screensaver over the KOReader one.
- **Better sleep and suspend handling**: Background tasks (catalog checks, thumbnail downloads, and ratings syncs) now safely pause and shut down the moment your device goes to sleep, freeing up memory automatically.
- **Cleaned up background tasks**: Prevented background processes and lingering network tasks from stacking up behind the scenes when browsing screensavers and catalog items.

**Full Changelog**: https://github.com/ultimatejimmy/storefront.koplugin/compare/26.10.10-beta2...26.10.10-beta3

# 26.10.10-beta2 · 2026-10-10

Fix bug with filter button

**Full Changelog**: https://github.com/ultimatejimmy/storefront.koplugin/compare/26.10.10-beta...26.10.10-beta2

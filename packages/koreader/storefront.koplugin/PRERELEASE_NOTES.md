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

# 26.10.10-beta · 2026-10-10

### Improvements and Fixes

* **Fixed memory leaks on low-RAM devices**: Fixed an issue where background ratings requests could get stuck and leak memory if they timed out, leading to out-of-memory crashes on memory-constrained e-readers (such as the Kindle Paperwhite 2). All background processes now have strict timeouts and are guaranteed to terminate cleanly.
* **Low-memory voting protection**: When available RAM is running low, Storefront avoids spawning heavy background processes altogether when you rate a plugin. It now submits your vote directly with a brief *"Submitting vote..."* status message so your vote goes through reliably without crashing KOReader.
* **Faster store browsing**: Ratings are now baked directly into the catalog. Storefront no longer fires off heavy background requests every time you open the browser dialog, resulting in faster dialog load times and lower overall memory usage.
* **Reduced memory footprint**: The in-memory ratings cache now discards unrated zero-entry items, cutting down memory usage by roughly 90%.

**Full Changelog**: https://github.com/ultimatejimmy/storefront.koplugin/compare/26.10.9-beta...26.10.10-beta

# 26.10.9-beta · 2026-10-09

## What's Changed

This release focuses on making Storefront significantly faster and more responsive, especially on older e-ink devices like Kindle Paperwhites.

* **In-Place Tab Switching**: Switching between tabs (*Plugins*, *Patches*, *Fonts*, *Screensavers*, *Installed*, and *Updates*) no longer closes and reopens the dialog. The interface now updates in-place with partial e-ink screen refreshes for a much smoother experience.
* **Instant Page Turning**: Turning pages across all catalog tabs is now immediate. Navigating forward or backward updates only the visible items on screen instead of reloading the catalog from storage.
* **Faster Screensavers Tab**: Eliminated the long loading delay when opening the Screensavers tab:
  * Uses KOReader's native, high-speed decoder for much faster catalog loading.
  * Image paths and details are now prepared on-demand only for the items currently visible on your page, rather than thousands of entries at once.
  * Catalog order is loaded directly without unnecessary sort passes on default views.
  * Switching between tabs keeps the catalog ready in memory so tapping back into Screensavers is instantaneous.
* **Better Memory Management**: All temporary catalog caches are automatically cleared from RAM the moment you close Storefront, keeping full memory free for reading your books.
* **Cached Tab Icons**: Tab bar icons are cached in memory after the first draw to prevent redraw stutter when tapping tabs.

**Full Changelog**: https://github.com/ultimatejimmy/storefront.koplugin/compare/26.10.7-beta3...26.10.9-beta

# 26.10.7-beta3 · 2026-10-08

- more screensaver efficiency improvements

**Full Changelog**: https://github.com/ultimatejimmy/storefront.koplugin/compare/26.10.7-beta2...26.10.7-beta3

# v1.21 · 2026-10-02

A KOReader plugin that puts the cover of the book you're reading, with a reading-progress bar and an optional message, on your PocketBook's lock screen. It also works on Android e-readers, Kobo and the desktop emulator, where it writes `cover.jpg` for the device's screensaver.

Tested on a PocketBook Era Lite (PB710), firmware 6.11, KOReader v2026.07.

## Install

1. Download `coverprogresspocketbook.koplugin.zip` below and extract it.
2. Copy the `coverprogresspocketbook.koplugin` folder into KOReader's `plugins/` folder. On PocketBook that's `/mnt/ext1/applications/koreader/plugins/`. Delete any older `coverprogress.koplugin` folder first.
3. Turn off KOReader's built-in **Cover image** plugin under **Tools → More tools → Plugin management**. It writes some of the same files.
4. Restart KOReader, open a book, and go to **Menu → Screen → Cover Image PocketBook → Enabled**.

## What it does on PocketBook

- **Sleep screen:** writes the Line theme's lock screen, portrait and landscape, as you read. Closing the sleep cover or double-clicking the menu button shows the current image without a restart: after each update the plugin asks the firmware's `taskmgr.app` to reload it.
- **Layouts:** progress bar in the margin, below the cover, over the cover, or no bar.
- **Sleep screen message:** your own text with KOReader's placeholders (`%T` title, `%p` percent, `%H` time left, `%b` battery, and more), in a box or a banner.
- **Books without a cover** show their title in bold instead.
- **Startup screen** (optional, off by default): the book cover alone, set when you open a different book.
- **Power-off screen** (optional, off by default): the book cover alone, or the same image as the sleep screen. In the PocketBook settings, set the power-off logo to **Custom image** and pick the file the plugin's menu names.

See the [README](https://github.com/apastuszak/coverprogresspocketbook.koplugin#readme) for the menu, settings and troubleshooting.

## Known limitations

- The image is written ahead of time while you read, so time, date and battery placeholders show their value at the last update, not the moment the device sleeps.
- Locking within about a second of a page turn that changes the percentage can show the previous image.
- Other PocketBook models should work the same way (the image size comes from the screen), but only the Era Lite has been tried.

Licensed under AGPL-3.0, like KOReader, from which it is derived.

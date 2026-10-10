# v1.15.0 · 2026-10-10

### What's new

- **Continuing from Seekquel lands in the right place in the chapter.** When you accept "Continue there" for a place you reached in the Seekquel app, KOReader now opens the same point in that chapter instead of a percentage of the whole book. This works when your file lists the same chapters as the one you read in the app; otherwise the percentage is used as before.
- **Seekquel learns how far into the chapter you are.** Each sync now says how far through the current chapter you have read, so the Seekquel app can open the same point in it.
- **Fixed:** the offer to continue from Seekquel showed two percent signs ("60%%"). It now reads "60%".

### Install

Download `seekquel.koplugin-v1.15.0.zip`, unzip it, copy the `seekquel.koplugin` folder into `koreader/plugins` on your reader and restart KOReader. Then open Tools, Seekquel, Connect this device. If the add-on is already installed, it updates itself from the Seekquel menu.

# v1.14.0 · 2026-10-08

### What's new

- **Pair by scanning a QR code.** The pairing screen now shows a QR code above the code. Scan it with your phone and Seekquel opens with the code already filled in, so all that is left is to tap Connect. Typing the code still works as before.

### Install

Download `seekquel.koplugin-v1.14.0.zip`, unzip it, and copy the `seekquel.koplugin` folder into KOReader's `plugins` folder on your e-reader. Restart KOReader, then open the Seekquel menu to pair. If the add-on is already installed and paired, it updates itself and you do not need to do anything.

# v1.13.0 · 2026-09-27

### What's new

- **A new version is offered once.** When a newer add-on is ready and you are in the file browser with Wi-Fi on, KOReader asks whether to update now. Tap Later and it stays quiet until the next version; the Seekquel menu still offers the update whenever you want it. It never asks while a book is open.
- **An update that does not install tells Seekquel why.** The e-reader sends what went wrong as soon as it happens, so a device left without a working add-on can be spotted and helped.

### Install

Download `seekquel.koplugin-v1.13.0.zip`, unzip it, and copy the `seekquel.koplugin` folder into KOReader's `plugins` folder on your e-reader. Restart KOReader, then open the Seekquel menu to pair. If the add-on is already installed and paired, it updates itself and you do not need to do anything.

# v1.12.1 · 2026-09-25

### What's new

- When the add-on cannot update itself, it now says what went wrong: the download stopped partway, arrived damaged, or could not be installed on this device, and what to try next. Before, every failure read "Could not reach Seekquel".

### Install

Download `seekquel.koplugin-v1.12.1.zip`, unzip it, and copy the `seekquel.koplugin` folder into KOReader's `plugins` folder. Restart KOReader. If the add-on is already installed and paired, it updates itself from Seekquel.

# v1.12.0 · 2026-09-23

### What's new

- A book you finish in Seekquel is now marked finished in KOReader too. The next time you open it on your e-reader, KOReader's own status changes to finished. A status you set on the e-reader since always stands, and a book you are reading again is left alone.
- Sync now sends today's reading up to the page you are on. KOReader only saves its reading statistics every fifty page turns, so a sync mid-sitting could leave out the last few dozen pages. The add-on now asks KOReader to save them first.

### Install

Already using the add-on? It updates itself, so there is nothing to do.

New install: download `seekquel.koplugin-v1.12.0.zip`, unzip it into KOReader's `plugins` folder so you have a `seekquel.koplugin` folder there, restart KOReader, then pair it from the Seekquel menu with the code shown in the app.

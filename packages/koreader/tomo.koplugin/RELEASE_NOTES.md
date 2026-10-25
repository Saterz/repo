# v2.7.4 · 2026-10-25

<!-- © 2026 James Edward Honiball. All Rights Reserved. -->
<!-- Tomo™ (友) — Social Reading Companion for Kobo -->

Tomo v2.7.4

A quieter release. There is nothing new to learn; Tomo simply stays steadier.

**Steadier after sleep.** When your reader wakes, Tomo renews its session on its own before it talks to the server, so your rooms and profile load the first time instead of waiting for a relaunch. If Wi-Fi is slow to come back, Tomo tries again a little later by itself.

**A full storage no longer interrupts a sync.** When the device runs out of space, Tomo notes it quietly and carries on. Nothing is interrupted mid-sync.

**Letters are checked before they are sealed.** If a letter could not be saved, for example when storage is full, Tomo tells you and keeps your drawing on the page.

**Fewer surprises.** Many small fixes so that an unexpected reply from the server, a missing detail in a message, or a damaged cache file can no longer close a screen. A damaged cache rebuilds itself on the next launch.

**Updates install more carefully.** Every file in an update is checked before it replaces the old version, and if anything goes wrong the previous version is put back.

Also in this release: Tomo is tested against KOReader 2026.07, and crash reports now contain only Tomo's own error, never lines from other plugins.

---

**To install for the first time:** download `tomo.koplugin-v2.7.4.zip` below, unzip it, and copy the `tomo.koplugin` folder into KOReader's `plugins` folder. Full step-by-step instructions are in the README.

**Already have Tomo?** It updates itself over Wi-Fi the next time you open it.

Requires KOReader 2024.07 or later.

---

Tomo is free and made by one person. If it has given you something, you can buy me a coffee at https://buymeacoffee.com/Tokeloshe

# v2.7.3 · 2026-07-03

<!-- © 2026 James Edward Honiball. All Rights Reserved. -->
<!-- Tomo™ (友) — Social Reading Companion for Kobo -->
<!-- Paste the text below (from "Tomo v2.7.3" down) as the GitHub Release body. -->

Tomo v2.7.3

Writing letters works the way it should now, and the app fits your screen — whatever screen that is.

**Letter writing fixed.** The Seal and close buttons now respond reliably to finger taps on every device. Slow, deliberate presses work too. If your pen drifts while tapping, Tomo still understands. And sealing an empty page now tells you the page is empty instead of doing nothing.

**The home page always fits on one screen.** No scrolling, no cut-off corners — on any Kobo or Kindle, portrait or landscape. When book rooms bloom, the ones that fit appear on home and the Conservatory holds them all.

**True colours while you draw.** On colour devices, ink now appears in its real colour as you draw — blue is blue, not orange — including the fine pens and the colour swatch.

**Better on Kindle.** Your current book is recognised the moment you open it, book rooms can now bloom from Kindle readers, and updates install reliably on more firmware versions.

**Comfortable to touch everywhere.** Buttons, toggles, room rows, and links across the app are properly sized for fingers on every screen, from the smallest Kobo to the Kindle Scribe.

Also in this release: messages no longer duplicate in rooms, pen pal letters keep their delivery time, long reading sessions stay signed in, and the settings screen no longer clips its controls on large devices.

---

**To install for the first time:** download `tomo.koplugin-v2.7.3.zip` below, unzip it, and copy the `tomo.koplugin` folder into KOReader's `plugins` folder. Full step-by-step instructions are in the README.

**Already have Tomo?** It updates itself over Wi-Fi the next time you open it.

Requires KOReader 2024.07 or later.

# v2.7.0 · 2026-04-16

# v2.6.6 · 2026-04-06

Crash report dedup and upload fix, Kindle device ID fallback, crash log parser, crash-loop detection, full crash field population, atomic OTA with rollback, last_seen tracking, postcrossing debounce, penpal matching fix, reading presence reporting.

# v2.6.5 · 2026-03-31

Fixed OTA updater failing silently. Update now retries on failure and always re-prompts until successful. OTA failures now report to crash telemetry.

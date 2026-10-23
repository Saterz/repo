# v8.3.1 · 2026-10-23

# Part of story 7: "The GOOGLE age"
In this new release, the AppDock keyboard was updated.
- Faster
- More ergonomic keys
- Emojis
- Cleaner look
## And some logos were changed...

# v8.3.0 · 2026-10-23

# Updated the file manager.

# v8.2.28 · 2026-10-23

# v8.7.27 · 2026-10-23

# v8.2.26 · 2026-10-23

# AppDock 8.2.26 — Shorts Playback und Ladefortschritt

## Behoben

- Shorts-Playback aktualisiert jetzt den tatsächlich gerenderten Canvas als Dirty-Widget. Dadurch werden neue BWR-Frames auf KOReader-Geräten zuverlässig sichtbar, statt auf dem ersten Bild stehenzubleiben.
- Playback-Fehler und fehlende, noch nicht fertige BWR-Dateien werden direkt im Shorts-Pane erklärt.
- Der Ladefortschritt ist jetzt als verständlicher Ablauf sichtbar: Suche, Download/Konvertierung und Audio-Extraktion werden mit Status und Prozentwert angezeigt.
- Schnelle Shorts-/Player-Refreshes erzwingen keinen globalen Voll-Repaint mehr. Das reduziert Flackern, vermeidet Refresh-Konflikte und verbessert E-Ink-Animationen.

## Prüfung

Die vollständige UI-Regression mit `bash scripts/test_appdock_ui.sh` ist erfolgreich durchgelaufen. Zusätzlich wurden alle installierbaren Lua-Dateien auf Syntaxfehler geprüft.

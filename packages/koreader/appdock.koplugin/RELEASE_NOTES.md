# v8.5.3 · 2026-10-25

# AppDock 8.5.3

AppDock enthält jetzt eine optionale Doom-DApp für Kobo. Die DApp nutzt den vorhandenen doomgeneric-VNC-Port und stellt Touch-Steuerung, Seitentasten, Waffenwahl, Karte sowie Quicksave und Quickload direkt in AppDock bereit.

Die nativen Doom-Binaries und Freedoom-WADs werden nicht Bestandteil des AppDock-Kernupdates. Sie können separat über DockUpdate 1.4.11 nach `.adds/doom` installiert werden. Bestehende Installationen werden dabei nicht überschrieben.

# v8.5.2 · 2026-10-25

# AppDock 8.5.2 — NetSurf-Browser

AppDocks Browser startet jetzt standardmäßig NetSurf anstelle der integrierten Browser-Startseite. Der bisherige AppDock-Browser bleibt als Fallback verfügbar, falls NetSurf nicht installiert ist.

DockUpdate bezieht das neue Browser-Modul `appdock_netsurf.lua` ab Version 8.5.2. Bei einem bestätigten AppDock-Update wird das NetSurf-Paket nach `/mnt/onboard/.adds/netsurf` entpackt; vorhandene Installationen werden nicht überschrieben.

Nach der Aktualisierung AppDock bzw. KOReader neu starten. NetSurf benötigt das mitgelieferte Reader-Binary und ausreichend freien Speicher im `.adds`-Verzeichnis.

# v8.5.1 · 2026-10-25

# v8.5.0 · 2026-10-25

 jetzt anders aussieht:
Statusleiste: Die Uhr ist fett und die Batterie hat ein gezeichnetes Symbol mit Füllstand plus Prozent, wie in der Android-Statusleiste.
"At a glance": Auf Seite 1 steht oben ein großes Datum (z. B. "Sun, Oct 25"), wie beim Pixel. Es erscheint nur, wenn die Uhr in den Widget-Einstellungen aktiv ist.
Suchleisten: Die DuckDuckGo-Pille hat keine doppelte Lupe mehr. Die App-Suche ist jetzt ebenfalls eine runde Pille mit gezeichneter Lupe statt des Zeichens "⌕", das in manchen Fonts als Kästchen erscheint.
Karten und Dock: Auf Farb-Displays gibt es keine harten Umrandungen mehr, nur eine fast unsichtbare Tonkante. Auf Schwarz-Weiß-Displays bleibt die dünne Umrandung. Das Dock ist ein abgerundetes Fach ohne Trennstrich.
App-Drawer-Symbol: Es ist jetzt das 3×3-Punktraster statt des 2×2-Gitters mit Lupe.
Seitenanzeige: Statt "‹ 1 / 2 ›" gibt es Punkte, die aktive Seite als Kapsel. Ein Tipp auf die Reihe springt zur nächsten Seite, ein Wisch geht weiterhin.
Raster ohne Überschrift: "Apps · 9" und der Edit-Button sind im Normalbetrieb weg. Der Bearbeitungsmodus startet wie bei Android per langem Druck auf eine freie Stelle oder auf eine App. Hinweis und "Done" erscheinen nur beim Bearbeiten.
Außerdem: Der Rand der ausgewählten Kachel im Bearbeitungsmodus nutzte eine Farbe, die es gar nicht gab. Das habe ich behoben.

# v8.4.6 · 2026-10-24

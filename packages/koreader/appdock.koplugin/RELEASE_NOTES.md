# v8.5.6 · 2026-10-26

# AppDock 8.5.6 — Games im AppStore

Der AppStore besitzt jetzt eine eigene **Games**-Sektion. Spiele werden aus dem separaten `games.txt`-Katalog geladen und zeigen neben ihrer Lua-DApp auch das zugehörige ZIP-Paket.

Nach sichtbarer Installationsbestätigung prüft AppDock das ZIP-Archiv, weist absolute und unsichere Pfade zurück und entpackt den Paketinhalt in das KOReader-Geräteverzeichnis `.adds`. Damit können Spiele wie Midless ihre nativen Dateien und Assets gemeinsam mit der Lua-Oberfläche installieren.

Der DApps-Katalog enthält dafür `midless.lua`, `games.txt` und `midless.zip`. Die bestehenden App-, Widget-, Design- und Sleepscreen-Kategorien bleiben erhalten.

# v8.5.5 · 2026-10-25

# v8.5.4 · 2026-10-25

Play DOOM on your eReader

# v8.5.3 · 2026-10-25

# AppDock 8.5.3

AppDock enthält jetzt eine optionale Doom-DApp für Kobo. Die DApp nutzt den vorhandenen doomgeneric-VNC-Port und stellt Touch-Steuerung, Seitentasten, Waffenwahl, Karte sowie Quicksave und Quickload direkt in AppDock bereit.

Die nativen Doom-Binaries und Freedoom-WADs werden nicht Bestandteil des AppDock-Kernupdates. Sie können separat über DockUpdate 1.4.11 nach `.adds/doom` installiert werden. Bestehende Installationen werden dabei nicht überschrieben.

# v8.5.2 · 2026-10-25

# AppDock 8.5.2 — NetSurf-Browser

AppDocks Browser startet jetzt standardmäßig NetSurf anstelle der integrierten Browser-Startseite. Der bisherige AppDock-Browser bleibt als Fallback verfügbar, falls NetSurf nicht installiert ist.

DockUpdate bezieht das neue Browser-Modul `appdock_netsurf.lua` ab Version 8.5.2. Bei einem bestätigten AppDock-Update wird das NetSurf-Paket nach `/mnt/onboard/.adds/netsurf` entpackt; vorhandene Installationen werden nicht überschrieben.

Nach der Aktualisierung AppDock bzw. KOReader neu starten. NetSurf benötigt das mitgelieferte Reader-Binary und ausreichend freien Speicher im `.adds`-Verzeichnis.

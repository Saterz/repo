# v8.2.21 · 2026-10-23

# AppDock 8.2.21 — Stabiler Recovery-Release

## Behoben

Die fehlerhafte Shorts-/Live-Status-Startup-Integration aus 8.2.19 und 8.2.20 wurde vollständig aus dem installierbaren Plugin entfernt. `main.lua` und `appdock_dapps.lua` entsprechen wieder dem letzten nachweislich funktionierenden Plugin-Kern aus 8.2.18.

Damit werden die experimentellen Module nicht mehr beim AppDock-Start geladen und können weder die KOReader-Plugin-Erkennung noch den Recovery-Startpfad unterbrechen.

## Wichtig

Diese Version ist bewusst ein stabiler Recovery-Release. YouTube Shorts und der Remote-Statuskanal sind nicht Bestandteil von 8.2.21. Sie werden erst nach separater KOReader-Laufzeittestung erneut integriert.

## Prüfung

Die Versionsstellen in `_meta.lua` und `main.lua` sind konsistent auf `8.2.21` gesetzt. Die installierbaren Kern-Dateien wurden auf den Stand von `v8.2.18` zurückgesetzt; die neuen Shorts-/Statusmodule sind nicht mehr im Plugin enthalten.

# v8.2.20 · 2026-10-23

# AppDock 8.2.20 — Hotfix für den Plugin-Start

## Behoben

Die neuen YouTube-Shorts- und Live-Statusmodule werden jetzt optional und fehlertolerant geladen. Falls eine optionale Komponente auf einem bestimmten KOReader-/Lua-Build nicht geladen werden kann, bleibt der AppDock-Kern trotzdem als Plugin verfügbar und kann normal gestartet werden.

Fehler beim Abruf einer Live-Statusmeldung werden zusätzlich abgefangen und können den Plugin-Start nicht mehr unterbrechen.

## Prüfung

Alle geänderten Lua-Dateien wurden mit einem Lua-5.1-kompatiblen Parser geprüft. Die Plugin-Metadaten enthalten Version `8.2.20`.

# v8.2.19 · 2026-10-23

# AppDock 8.2.19 — YouTube Shorts und Live-Statusmeldungen

## YouTube Shorts

AppDock enthält jetzt eine eigene **YouTube Shorts**-DApp mit vertikalem E-Ink-freundlichem Feed, großem Player, Creator-/Hashtag-Metadaten sowie Previous-/Next-Navigation.

Der Feed verwendet die bestehende yt-dlp-/ffmpeg-Pipeline, sucht über `#shorts` und begrenzt die Treffer auf maximal 180 Sekunden. Der aktuelle Clip und der nächste Feed-Eintrag werden über die lokale Videobibliothek verwaltet; der nächste Clip kann bereits während der Wiedergabe des aktuellen Clips vorgeladen werden.

Likes werden lokal auf dem Reader gespeichert. Hashtags gelikter Clips und Like-Häufigkeiten beeinflussen die lokale Empfehlungsreihenfolge. Es gibt keinen YouTube-OAuth-Schreibzugriff und keine Übertragung der Like-Daten.

## Live-Mitteilungen

Betreiber können technische Störungen und wichtige Hinweise jetzt ohne neues Plugin-Release veröffentlichen. AppDock ruft beim Start und anschließend alle drei Minuten die Datei `appdock_notice.json` aus dem `main`-Branch über HTTPS ab.

Eine neue, aktivierte Notice-ID erscheint als Update-ähnliches Popup und zusätzlich in der AppDock-Benachrichtigungs-Inbox. Meldungen werden lokal als gesehen gespeichert; `expires_at` und `enabled` erlauben zeitlich begrenzte oder deaktivierte Hinweise.

Die Bedienungsanleitung steht in [`APPDOCK_NOTICES.md`](APPDOCK_NOTICES.md).

## Prüfung

Die Notice-Datei wurde als gültiges JSON validiert und `git diff --check` läuft ohne Befund. Eine Lua-Syntax-/Regressionstest-Ausführung war in der Sandbox nicht möglich, da dort keine Lua-/LuaJIT-Laufzeit installiert ist.

# v8.2.18 · 2026-10-21

# AppDock 8.2.18 — Crash beim Scrollen öffentlicher Sleepscreens behoben

## Änderung

Der öffentliche Sleepscreen-Katalog registriert seinen `ScrollableContainer` jetzt korrekt als `cropping_widget` am aktiven KOReader-DApp-Host. Dadurch werden Repaints von Preview-, Renderer- und Bild-Widgets während des Scrollens auf den sichtbaren Katalogbereich begrenzt, statt an den gesamten Host weitergeleitet zu werden.

Beim Verlassen der Sleepscreen-Kategorie wird der veraltete Crop-Marker entfernt. Ein UI-Regressionstest prüft sowohl die Katalog- als auch die Host-Verknüpfung.

## Prüfung

Die Lua-Syntaxprüfung sowie die Sleepscreen-/AppStore-Regressionstests laufen erfolgreich. Serverseitige Deno-Tests wurden in der Sandbox nicht ausgeführt, da Deno dort nicht installiert ist.

# v8.2.17 · 2026-10-19

# AppDock 8.2.17 — App-Gruppen

Behebt einen Absturz beim Erstellen einer App-Gruppe über **Add another App → Create App Group**. Die Übersetzung `_()` wurde in den Gruppenmenüs durch die erste Rückgabevariable von Lua-`ipairs`/`pairs` überschattet; damit wurde beim Öffnen der Auswahl ein Zahlenwert als Funktion aufgerufen.

Zusätzlich wird beim Wechseln der ausgewählten Apps jetzt nur das gerade offene Dialogfenster geschlossen. Ein neuer Regressionstest durchläuft das Erstellen einer Gruppe, den Mitgliedereditor und die Manageransicht mit vorhandener Gruppe.

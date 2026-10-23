# v8.2.24 · 2026-10-23

# AppDock 8.2.24 — Shorts Feed UX

Die Shorts-DApp startet für neue Nutzer automatisch mit einem ersten YouTube Short aus einem sicheren Shorts-Tab. Danach werden lokale Interaktionen berücksichtigt: abgespielte Shorts, übersprungene Einträge und Likes beeinflussen die spätere Reihenfolge und die nächsten Themen-/Creator-Quellen.

Die Oberfläche bleibt während Suche und Konvertierung im Vollbild-Shorts-Layout. Ein roter Ladebalken erscheint zentriert in der Bildschirmmitte; bei der Feed-Suche läuft er indeterminiert, bei der Videokonvertierung zeigt er den tatsächlichen Fortschritt.

Vertikales Wischen bleibt die primäre Navigation: nach oben zum nächsten Short, nach unten zum vorherigen. Tippen pausiert oder startet den aktuellen Short. Die Interaktionsdaten bleiben begrenzt und lokal in den AppDock-Einstellungen.

# v8.2.23 · 2026-10-23

# AppDock 8.2.23 — YouTube Shorts Feed

Die YouTube-Shorts-DApp nutzt jetzt ausschließlich Einträge aus echten YouTube-Shorts-Tabs. Sie akzeptiert nur kanonische URLs im Format `/shorts/<Video-ID>`; eine Suchanfrage nach `#shorts` oder eine bloße Laufzeitgrenze reicht nicht mehr aus.

Die Oberfläche ist als vertikaler Feed ausgelegt. Tippen startet oder pausiert den aktuellen Short. Ein Swipe nach oben öffnet den nächsten Eintrag, ein Swipe nach unten den vorherigen. Die Aktionen für Like, Next und Themen bleiben direkt im Feed sichtbar.

Likes bleiben lokal auf dem Gerät gespeichert. Sie erfassen die Creator-ID und Hashtags des Shorts und ergänzen dadurch spätere Feed-Quellen. Eigene Hashtags werden als eigene Shorts-Tabs abgefragt. Während ein Short läuft, wird der nächste Eintrag als expliziter Hintergrundjob geladen; er ersetzt weder die sichtbare Wiedergabe noch startet er eine zweite Konvertierung.

Beim Schließen der DApp werden Suche, Vorabruf und Player sauber beendet. Neu- und Bestandsinstallationen erhalten die Shorts-Kachel einmalig neben YouTube. Die YouTube- und Shorts-Regressionstests laufen nun auch in GitHub Actions.

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

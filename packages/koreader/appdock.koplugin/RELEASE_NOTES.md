# v8.2.26 · 2026-10-23

# AppDock 8.2.26 — Shorts Playback und Ladefortschritt

## Behoben

- Shorts-Playback aktualisiert jetzt den tatsächlich gerenderten Canvas als Dirty-Widget. Dadurch werden neue BWR-Frames auf KOReader-Geräten zuverlässig sichtbar, statt auf dem ersten Bild stehenzubleiben.
- Playback-Fehler und fehlende, noch nicht fertige BWR-Dateien werden direkt im Shorts-Pane erklärt.
- Der Ladefortschritt ist jetzt als verständlicher Ablauf sichtbar: Suche, Download/Konvertierung und Audio-Extraktion werden mit Status und Prozentwert angezeigt.
- Schnelle Shorts-/Player-Refreshes erzwingen keinen globalen Voll-Repaint mehr. Das reduziert Flackern, vermeidet Refresh-Konflikte und verbessert E-Ink-Animationen.

## Prüfung

Die vollständige UI-Regression mit `bash scripts/test_appdock_ui.sh` ist erfolgreich durchgelaufen. Zusätzlich wurden alle installierbaren Lua-Dateien auf Syntaxfehler geprüft.

# v8.2.25 · 2026-10-23

# AppDock 8.2.25 — Einheitlicher Plugin-Host und Shorts UX

## YouTube Shorts

Die Shorts-DApp erhält eine klarere, intuitivere Feed-Oberfläche mit direkten Aktionen für **Previous**, **Play/Pause**, **Next**, **Topics**, **Reload** und **Tools**. Video-, Metadaten- und Transportbereiche bleiben auch in schmalen AppDock-Panes innerhalb ihrer lokalen Grenzen.

Swipe-Navigation, Canvas-Offsets, Ladezustände und der Inline-Player wurden stabilisiert. Ein verspäteter Such- oder Prefetch-Abschluss kann keinen neuen Feed überschreiben und startet keine Wiedergabe in einer geschlossenen oder unsichtbaren Oberfläche. Fortschritts-Neuaufbauten behalten den laufenden Short; tatsächliches Verlassen beendet Suche und Player sauber.

## Einheitlicher Plugin-Host

Nicht-DApps werden jetzt immer in AppDock gehostet. Sie dürfen keine eigene native Oberfläche mehr neben AppDock öffnen. Plugin-Panes, Events, Dialoge, ConfirmBoxen, Eingaben, Menüs und Cleanup laufen über eine begrenzte AppDock-Bridge.

Kooperierende Plugins erhalten AppDocks Palette, Kontrastrollen, Metriken und lokale Layout-Geometrie. Lange Aktionslisten, dynamische Untermenüs sowie verzögerte Plugin-Callbacks bleiben innerhalb des aktiven AppDock-Hosts. Nicht sicher adaptierbare Spezialansichten werden nicht als eigenständige Oberfläche geöffnet, sondern als AppDock-Kompatibilitätshinweis dargestellt.

Plugin-Hosts bleiben vom Split-Screen und von Floating Windows ausgeschlossen.

## Prüfung

Die vollständige native UI-Regression wird mit `bash scripts/test_appdock_ui.sh` ausgeführt. Die Suite umfasst DApp-Host, Shorts/YouTube, YouTube Music, Dialoge, Setup, Theme-Kontrast, Gruppen, Manager, Tastatur und Textkompatibilität. Zusätzlich werden alle installierbaren Lua-Dateien auf Syntaxfehler geprüft.

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

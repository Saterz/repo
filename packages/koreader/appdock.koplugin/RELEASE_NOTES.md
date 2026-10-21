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

# v8.2.16 · 2026-10-18

# AppDock 8.2.16 — Stabilitäts-Hotfix für Store-DApps

- Deaktiviert vorübergehend den benutzerdefinierten Transparent-TextBox-Renderer für Store-DApps. `appdock_text` stellt KOReaders natives `TextBoxWidget` bereit; bestehende DApps bleiben API-kompatibel.
- Stellt die Fehler-/Schema-Prüfung beim Wiederherstellen installierter Store-DApps und Store-Widgets wieder her. Damit wird das riskante Verhalten aus 8.2.15 zurückgenommen.
- Der Import von `appdock_text` ist optional; ein fehlendes Modul blockiert nicht mehr die Initialisierung des DApp-Managers.
- Das isolierte DApp-Fehlerfenster zeigt zusätzlich die gekürzte konkrete Fehlermeldung an, falls eine App weiterhin scheitert.

Die DApps behalten ihre expliziten `bgcolor`-Oberflächenwerte. Der Alpha-Masken-Renderer wird erst wieder aktiviert, nachdem er auf echten KOReader-Geräten validiert wurde.

# v8.2.15 · 2026-10-18

# AppDock 8.2.15 — Store-App-Restore ohne Fehlerprüfung

## Änderung

Beim Wiederherstellen installierter Store-DApps und Store-Widgets wird `inspectStoreDApp` beziehungsweise `inspectStoreWidget` nicht mehr aufgerufen. Die Datei wird direkt mit `dofile` ausgeführt. Es gibt dort weder Schema-Prüfung noch `pcall`-Fehlerabfang. Entsprechend der Anforderung eines Anwenders wird ein Syntax-/Laufzeitfehler, eine falsche Definition oder ein fehlender Rückgabewert **nicht mehr einzeln abgefangen** und kann den ganzen AppDock-DApp-Manager beim Start abbrechen. Die Prüfung bleibt nur für neu installierte/aktualisierte Store-Einträge bestehen.

Diese Änderung löscht keine AppDock-Einstellungen oder App-Registrierungen. Sie kann jedoch fehlerhafte Store-Dateien nun ungefiltert ausführen. Nur mit den bekannten Store-Dateien und Testfixtures verifizieren; nicht empfohlen für Installationen mit unbekannten/geänderten Store-Apps.

## Prüfung

Neue Regressionen beweisen, dass die Restore-Pfade die DApp- und Widget-Inspektoren umgehen. Weitere Regressionen verifizieren die normale Prüfung beim erstmaligen Installieren/Updaten.

# v8.2.14 · 2026-10-18

# AppDock 8.2.14

## Vollständige, transparente TextBoxen

Nicht editierbare mehrzeilige Texte aus TextBoxWidget werden jetzt ohne deckende weiße Rechtecke auf die bereits gezeichnete Fläche komponiert. Die Glyphenmaske erhält KOReaders Schriftglättung und funktioniert auch mit weißer Schrift, RGB-Themes und Inversions-/Nachtmodus. Native Layout- und Ressourcenverwaltung bleiben erhalten; globale KOReader-Widgetklassen werden nicht verändert. Für interaktive Sonderfälle und ältere Blitbuffer-Builds bleibt ein sicherer nativer Pfad mit passender Hintergrundfarbe erhalten. Einzeilige TextWidget-Beschriftungen bleiben unverändert.

Der AppDock-DApp-Manager stellt die lokale Komponente Store-DApps optional bereit. Das zugehörige DApps-Update nutzt sie in DChat, AI Chat, DReader, RSS Reader, Dex Document und DockUpdate; ältere AppDock-Hosts bleiben durch explizite Flächenfarben kompatibel.

## Prüfung

Pixel-Regressionen decken weiße und farbige Glyphen, Antialiasing, Leerraum, fehlende Kompositoren, Ressourcenzustände und globale Klassen-Unverändertheit ab. KOReaders echte Mono-/RGB-Blitbuffer sowie Inversion wurden zusätzlich geprüft. Der generische Gesamtlauf enthält weiterhin bereits zuvor bestehende Testprobleme in einem Store-Hook, YouTube/YouTube Music und Gmail. Physische E-Ink-Hardware wurde nicht getestet.

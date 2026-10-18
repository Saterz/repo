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

# v8.2.12 · 2026-10-18

# AppDock 8.2.12

## Stabilität und Crash-Schutz

Gespeicherte Einstellungsgruppen werden beim Laden typgeprüft und fehlende Standardwerte ergänzt. Fehlerhafte Homescreen-, DApp- oder Fremdplugin-Aufrufe werden an zentralen Grenzen abgefangen, sodass ein einzelnes fehlerhaftes Modul nicht den KOReader-Eventloop beendet. DApp-Panes erhalten bei Fehlern eine wiederherstellbare Fehleransicht; verspätete Lifecycle-Aufrufe werden abgefangen.

Der periodische DApp-Hintergrundlauf wird gegen Runtime-Ausnahmen geschützt und bleibt danach aktiv. Einzelne unvollständige Fremdplugin-Module werden übersprungen.

## TBS-Konto verständlicher erklärt

Der TBS-Kontoeintrag zeigt klarer, wofür das Konto verwendet wird. Die Offline-Hilfe erläutert in Deutsch und Englisch Kontozweck, synchronisierte bzw. lokale Daten, Datenschutz, Wiederherstellungscode und Gerätewechsel.

## WLAN-Migration robuster

Die WLAN-Migration validiert und begrenzt empfangene Daten und importierte Assets. Überdimensionierte Nachrichten und ungültige Zustände werden kontrolliert abgewiesen, statt den Importpfad zu destabilisieren.

## Weitere UI-Korrekturen

Der About-Bereich verwendet die zentrale aktuelle Version statt einer alten fest codierten Nummer. Die Hilfekapitel wurden nach dem neuen TBS-Abschnitt neu nummeriert.

## Prüfung

Alle Plugin-Lua-Dateien bestehen die Lua-Syntaxprüfung. 15 ausführbare Regressionstests für TBS, Dialoge, Recovery, Dateiverwaltung, E-Ink-UI, Themes und weitere Komponenten laufen erfolgreich. Einzelne DApp-Tests benötigen KOReader-Subprozess- bzw. Bluetooth-Hardwarefunktionen und sind in einer generischen Sandbox nur eingeschränkt ausführbar.

# v8.2.11 · 2026-10-18

# AppDock 8.2.11

## Dialog-Akzentfarbe auf RGB-Geräten

Primäre Aktionen werden wieder sichtbar in Olivgrün hervorgehoben und erhalten kontrastreiche weiße Beschriftung. Der Dialogrenderer verwendet KOReaders `paintRectRGB32` für RGB-Füllungen; deaktivierte und sekundäre Aktionen bleiben klar unterscheidbar.

## Absturz beim Aktivieren von Wetter behoben

Der Sleepscreen-Widget-Editor überschattete beim Neuaufbau nach dem Einschalten von Open-Meteo eine Übersetzungsfunktion mit einer Schleifenvariable. Die Variable ist umbenannt; ein UI-Regressionstest aktiviert den Wetter-Schalter und prüft, dass die Wetterfelder ohne Absturz erscheinen.

## Prüfung

Dialog- und Wetter-UI-Regressionstests sowie die vollständige Sleepscreen-Testreihe laufen erfolgreich. Die optionalen serverseitigen Deno-Tests sind nur verfügbar, wenn Deno installiert ist.

# v8.2.11 · 2026-10-18

# AppDock 8.2.11

## Dialog-Akzentfarbe auf RGB-Geräten

Primäre Aktionen werden wieder sichtbar in Olivgrün hervorgehoben und erhalten kontrastreiche weiße Beschriftung. Der Dialogrenderer verwendet KOReaders `paintRectRGB32` für RGB-Füllungen; deaktivierte und sekundäre Aktionen bleiben klar unterscheidbar.

## Absturz beim Aktivieren von Wetter behoben

Der Sleepscreen-Widget-Editor überschattete beim Neuaufbau nach dem Einschalten von Open-Meteo eine Übersetzungsfunktion mit einer Schleifenvariable. Die Variable ist umbenannt; ein UI-Regressionstest aktiviert den Wetter-Schalter und prüft, dass die Wetterfelder ohne Absturz erscheinen.

## Prüfung

Dialog- und Wetter-UI-Regressionstests sowie die vollständige Sleepscreen-Testreihe laufen erfolgreich. Die optionalen serverseitigen Deno-Tests sind nur verfügbar, wenn Deno installiert ist.

# v8.2.10 · 2026-10-18

# AppDock 8.2.10

## AppDock-Dialoge im modernen Frostglas-Stil

Alle AppDock-eigenen Auswahl-, Bestätigungs-, Eingabe- und Infodialoge erhalten zentral abgerundete Flächen und Schaltflächen, Olivgrün als Akzent sowie eine leicht durchscheinende Frostglas-Überlagerung. Beschriftungen werden automatisch umbrochen; Buttons wachsen mit mehrzeiligen Texten. Wo KOReaders Renderer keine Alpha-Komposition unterstützt, bleibt ein kontrastreicher E‑Ink-Fallback aktiv. Eine echte Hintergrundunschärfe ist geräteabhängig und wird nicht von allen KOReader-Blitbuffern angeboten.

## Custom Widgets im Sleepscreen-Editor

Custom Widgets lassen sich im Editor auswählen, bearbeiten und direkt mit einer Sleepscreen-Ebene verbinden. Vorlagen unterstützen Uhrzeit, Datum, Akkustand, Gerät, Animationen, Zeitregeln und Wetter-Platzhalter. Open-Meteo kann ohne API-Schlüssel manuell für konfigurierbare Koordinaten abgefragt werden. Der Wetter-Cache wird lokal im Preset gespeichert; Renderer und Suspend-Pfad führen keine Netzwerkanfrage aus. Vor dem öffentlichen Teilen werden Wetterkoordinaten und Cachewerte in der Veröffentlichungsbestätigung offengelegt.

## Prüfung

Dialog-Regressionstests sowie die vollständige Sleepscreen-/AppStore-Testreihe laufen erfolgreich. Serverseitige Deno-Tests wurden mangels Deno-Laufzeit nicht ausgeführt.

# v8.2.9 · 2026-10-18

# AppDock 8.2.9

## Transparenz auf Kobo Libra Colour korrigiert

Element-Hintergründe werden nicht mehr über einen Alpha-Kanal in `ColorRGB32` gezeichnet. Stattdessen erstellt der Renderer einen opaken temporären Hintergrundpuffer und mischt ihn mit KOReaders `addblitFrom(..., opacity)` in den bereits gerenderten Sleepscreen-Puffer. Dadurch funktioniert `background_alpha` auch auf dem Kobo Libra Colour zuverlässig.

Der Fix betrifft sowohl die Live-Vorschau im Editor als auch den aktiven Sleepscreen. Ein Regressionstest prüft den tatsächlichen `addblitFrom`-Pfad.

# v8.2.8 · 2026-10-18

# AppDock 8.2.8

## Codefreie Custom-Widgets

Der Sleepscreen-Editor enthält eine neue Sektion **Custom widgets**. Benutzer können ohne Lua- oder sonstigen Code eigene wiederverwendbare Text-Widgets erstellen:

- Basistexte mit `{time}`, `{date}`, `{battery}`, `{device}` und `{sleeping}`
- zeitabhängige Texte über einfache Zeitbereiche wie `06:00-12:00=Guten Morgen`
- zyklische Animationen über mehrere Textframes, die pro Sleep-Zyklus wechseln
- Einfügen eigener Widgets als Layer im Sleepscreen

Die Definitionen bleiben deklarativ, werden lokal und serverseitig validiert und akzeptieren keine ausführbaren Inhalte.

## Transparenz

Der Element-Hintergrund verwendet nun den zuverlässigen RGB-Blending-Pfad auch dann, wenn die Farbdisplay-Erkennung im Sleep-/Suspend-Pfad unvollständig ist. Bestehende Presets bleiben kompatibel.

# v8.2.7 · 2026-10-17

# AppDock 8.2.7

Element-Hintergründe in Sleepscreens unterstützen jetzt Transparenz.

Im Editor kann die Deckkraft eines Element-Hintergrunds zwischen 0 % und 100 % eingestellt werden. Das deklarative Format verwendet dafür `background_alpha` zwischen `0` und `1`; bestehende Presets ohne dieses Feld bleiben vollständig opak. Auf farbfähigen Geräten wird die Deckkraft über den RGB-Blending-Pfad gerendert, während monochrome Geräte den kompatiblen Graustufen-Fallback behalten.

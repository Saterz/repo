# v7.9.21 · 2026-10-11

# AppDock 7.9.21

## Draw: Kobo-Stiftdruck, Radierer und Marker

Draw nutzt nun den Kobo-Rohereignispfad für Stylus-Eingaben. Stiftdruck wird aus dem Sensorwert normalisiert und auf die ausgewählte Pinselgröße angewendet. Die physische Radiererspitze löscht mit der weißen Zeichenfarbe; der Marker aktiviert die breitere Marker-Spitze.

Die Bildschirmrotation wird bei den Rohkoordinaten berücksichtigt. Der Stylus-Listener ist nur während einer aktiven Draw-Pane registriert und stellt beim Verlassen den ursprünglichen KOReader-Gesture-Handler wieder her. Normale Touch-Eingaben und KOReader-Gesten bleiben unverändert.

## Tests

Alle 14 AppDock-LuaJIT-Regressionstests laufen durch, einschließlich der neuen Draw-Stylus-Tests für Druck, Radierer, Marker, Rotation, Tracking-IDs und Listener-Lifecycle. LuaJIT-Syntaxprüfung aller Plugin-Dateien und `git diff --check` sind sauber.

# v7.9.20 · 2026-10-11

# AppDock 7.9.20

## Window Mode (Beta): Taskbar und mehrere Fenster

Der Beta-Fenstermodus erhält eine Taskleiste mit Startmenü. Darüber lassen sich weitere DApps starten, während bereits geöffnete Apps im Desktop-Fenstermodus geöffnet bleiben. Neue Fenster werden leicht versetzt angeordnet; pro App bleiben Position und Größe erhalten.

Taskbar-Einträge bringen ein Fenster in den Vordergrund und stellen minimierte Fenster wieder her. Fenster können einzeln minimiert oder geschlossen werden, ohne die übrigen Fenster zu beenden. Der Beta-Modus unterstützt bis zu acht gleichzeitig geöffnete Fenster. Vollbild bleibt pro Fenster möglich und blendet die Taskleiste vorübergehend aus.

## Tests

Alle 13 AppDock-LuaJIT-Regressionstests laufen durch. Die Tests decken Startmenü-Launch, mehrere offene Fenster, Taskbar-Fokus, Minimieren/Wiederherstellen, Einzel-Schließen und Vollbildwechsel ab. LuaJIT-Bytecodeprüfung und `git diff --check` sind sauber.

# v7.9.19 · 2026-10-11

# AppDock 7.9.19

## Draw: RGB-Anzeige und Pinselstärke

Draw sendet Farbpixel nun über KOReaders `paintRectRGB32`-Framebufferpfad – wie die funktionierende Minecraft-DApp. Die Farberkennung berücksichtigt sowohl die Farbfähigkeit des Displays als auch KOReaders aktivierte Farbwiedergabe.

Die ausgewählte Pinselgröße wird nicht mehr durch die Canvas-Skalierung auf einen Pixel reduziert. Instabile Druckwerte von Fingereingaben verändern die Strichdicke nicht; explizite Drucksensitivität bleibt für Stylus-Eingaben verfügbar. Pinselstempel verwenden nun die gewählte Durchmessergröße.

## Tests

Alle 13 AppDock-LuaJIT-Regressionstests laufen durch. LuaJIT-Bytecodeprüfung und `git diff --check` sind sauber.

# v7.9.18 · 2026-10-11

# AppDock 7.9.18

## Draw: Farbe auf Farbdisplays und RGB-Farbwahl

Draw erkennt nun die tatsächliche Hardware-Farbdisplay-Fähigkeit statt KOReaders globaler Einstellung „Color rendering“. Dadurch werden RGB-Farben auch dann an Draw übergeben, wenn die Dokument-Farbdarstellung global ausgeschaltet ist.

Die Werkzeugleiste enthält einen RGB-Farbwähler mit Vorschau. Farben können als `#RRGGBB` oder `R,G,B` eingegeben werden. Benutzerdefinierte Farben und die aktuelle Farbauswahl werden in Zeichnungsprojekten gespeichert. Bestehende `ADRAW1`-Projekte bleiben weiterhin ladbar.

## Tests

Alle 13 AppDock-LuaJIT-Testskripte laufen durch. LuaJIT-Bytecodeprüfung und `git diff --check` sind sauber.

# v7.9.17 · 2026-10-11

# AppDock 7.9.17

## YouTube Music: Suche per Enter und überarbeitete Startansicht

Die AppDock-Tastatur löst beim Absenden jetzt den YouTube-Music-Suchbutton aus. Beliebige Texteingaben werden als Suchanfrage behandelt; direkte Downloads bleiben für eingefügte YouTube-Links verfügbar. Fehlende Suchwerkzeuge und Fehler beim Starten einer Suche erscheinen in einer sichtbaren Diagnoseansicht.

Der leere Music-Startbildschirm wiederholt nicht mehr den Fenstertitel, zeigt keinen funktionslosen Play-Button und bietet stattdessen eine gestaltete Leerkartenansicht mit direktem Einstieg in die Suche.

## Tests

Alle 13 AppDock-LuaJIT-Testskripte laufen durch. `git diff --check` und die LuaJIT-Syntaxprüfung sind sauber.

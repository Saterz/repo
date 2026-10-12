# v8.0.0 · 2026-10-12

# Thanks to Quin Easwar
(Biggest release ever)

# v7.9.48 · 2026-10-11

# AppDock 7.9.48

- Die Tastatur lädt die vollständige deutsche und englische Datenbank über mehrere sichere Plugin-Pfade.
- Die Datenbank wird nicht mehr durch den aktuellen Arbeitsordner von KOReader verfehlt.
- Das Release enthält ein vollständiges Installationsarchiv mit `appdock_suggestions.lua` **und** `appdock_suggestions.db`.
- Die kleine Fallback-Liste bleibt nur als Notfall bei einer wirklich fehlenden oder unlesbaren Datenbank.

# v7.9.47 · 2026-10-11

# AppDock 7.9.47

- **Datenbank wieder aktiv:** Die deutsche und englische Vorschlagsdatenbank wird jetzt sicher direkt aus dem AppDock-Plugin-Ordner geladen.
- Funktioniert auch dann, wenn KOReader den Plugin-Ordner nicht in `package.path` einträgt.
- Der Boot-Schutz bleibt erhalten: Nur wenn die Datei wirklich fehlt oder unlesbar ist, wird die kleine Fallback-Liste verwendet.
- Die mitgelieferte `appdock_suggestions.db` bleibt vollständig Bestandteil des Releases.

# v7.9.46 · 2026-10-11

# AppDock 7.9.46

- **Boot-Crash behoben:** Die Vorschlagsdatenbank wird nicht mehr beim Laden des Keyboard-Moduls importiert.
- Die Datenbank wird erst beim tatsächlichen Erzeugen einer Tastatur lazy geladen.
- Falls die Datenbank oder ihr Modul fehlt bzw. fehlerhaft ist, startet die Tastatur mit einer kleinen eingebetteten Fallback-Liste.
- Caps Lock und die größeren Tasten aus 7.9.45 bleiben erhalten.

# v7.9.45 · 2026-10-11

# AppDock 7.9.45

- Die Tastatur hat jetzt eine sichtbare **CAPS**-Taste für dauerhafte Großschreibung.
- Die vorhandene **Shift**-Taste bleibt als einmalige Großschreibung erhalten.
- Normale Buchstaben-, Zahlen-, Symbol- und Steuerungstasten sind größer geworden.
- Caps Lock funktioniert auch mit deutschen Sonderzeichen wie `ä`, `ö`, `ü` und `ß`.
- Optional kann ein Dialog `caps_lock = true` beim Öffnen voraktivieren.

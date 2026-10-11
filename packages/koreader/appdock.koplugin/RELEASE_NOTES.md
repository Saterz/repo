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

# v7.9.44 · 2026-10-11

# AppDock 7.9.44

- Die Tastatur verwendet jetzt eine echte editierbare Offline-Datenbank: `appdock_suggestions.db`.
- Enthalten sind **3.000 deutsche und 3.000 englische Wörter** mit Häufigkeitswerten.
- Vorschläge werden nach Wortfrequenz priorisiert und weiterhin sofort lokal gefiltert.
- Die Datenbank ist bewusst TSV statt SQLite, damit sie auf Kobo ohne native Datenbank-Erweiterung funktioniert und direkt bearbeitet werden kann.
- Eigene Wörter können als weitere Zeilen mit `de` oder `en`, Häufigkeit und Wort ergänzt werden.
- Optional können Dialoge eine Sprache oder eine eigene `suggestions`-Liste übergeben.

# v7.9.43 · 2026-10-11

# AppDock 7.9.43

- **Tastatur-Cancel repariert:** Bereits geschlossene Eingabedialoge werden nicht mehr ein zweites Mal geschlossen.
- Der Update-Hinweis verwendet jetzt eine AppDock-eigene helle Modal-Karte statt den gesamten Inhalt in den ButtonDialog-Titel zu packen.
- Der Feature-Dialog besitzt keinen Timeout und bleibt bei periodischen E-Ink-Vollrefreshes sichtbar.
- Seitenwechsel, `Weiter`, `Später` und `Fertig` bleiben erhalten.

Hinweis: Die allgemeine Testsuite konnte bis zur Dialogprüfung ausgeführt werden; `test_dapps.lua` benötigt außerhalb einer KOReader-Umgebung das KOReader-Modul `json`.

# v7.9.42 · 2026-10-11

# AppDock 7.9.42

- Größere Tasten für schnellere und sicherere E-Ink-Eingabe.
- Drei lokale Vervollständigungsvorschläge werden direkt über der Tastatur angezeigt.
- Ein Vorschlag ersetzt das aktuelle Wort und fügt automatisch ein Leerzeichen ein.
- Vorschläge funktionieren offline; Dialoge können eigene Vorschlagslisten über `suggestions` übergeben.
- Tastatur bleibt mit numerischer Eingabe, Secure-Input, Shift, Symbolen und Cancel kompatibel.

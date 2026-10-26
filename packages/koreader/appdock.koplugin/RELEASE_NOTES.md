# v8.5.10 · 2026-10-26

# AppDock 8.5.10 — Game-Installer-ZIP-Prüfung

Der separate `unzip -tq`-Vorabtest wurde entfernt. Auf dem Kobo schlug genau dieser Test fehl, obwohl der Installer anschließend die normale Extraktion hätte ausführen können. Der Game-Installer prüft das ZIP weiterhin vor dem Entpacken auf unsichere Pfade; maßgeblich für die Integrität ist jetzt der Exit-Status der tatsächlichen Extraktion, die ZIP-Daten und CRCs dabei ebenfalls überprüft.

Die kurze, stufenspezifische Fehlermeldung aus 8.5.9 bleibt erhalten, falls die eigentliche Extraktion nach diesem Fix weiterhin fehlschlägt.

# v8.5.9 · 2026-10-26

# AppDock 8.5.9 — Lesbare Game-Installationsfehler

Fehler beim Installieren eines Games erscheinen jetzt mit kurzer Überschrift und einem kompakten, stufenspezifischen Grund auf einer eigenen Zeile. Das verhindert, dass der lange, doppelte Dialogtext den entscheidenden Teil der Meldung abschneidet.

Die neue Meldung unterscheidet unter anderem ZIP-Auflistung, Integritätsprüfung, Entpacken nach `.adds`, fehlenden Launcher und fehlende Ausführungsrechte. Damit lässt sich der konkrete Gerätefehler beim nächsten Installationsversuch gezielt beheben.

# v8.5.8 · 2026-10-26

# AppDock 8.5.8 — Game-Paketinstallation auf KOReader-Geräten

Der Game-Installer unterstützt jetzt sowohl Info-ZIP als auch BusyBox `unzip`. Für die sichere Archivprüfung wird die portable Listenoption `-lq` statt der Info-ZIP-spezifischen Option `-Z1` verwendet; der Installer prüft außerdem, dass tatsächlich ZIP-Einträge gelesen wurden.

Nach dem Entpacken setzt AppDock den erwarteten Launcher unter `<game>/bin/<game>` auf ausführbar (`0755`). Damit werden beide Hürden abgedeckt: Archive ohne Unix-Ausführungsbits und Geräte, die nur BusyBox statt eines separaten `unzip` bereitstellen.

# v8.5.7 · 2026-10-26

# AppDock 8.5.7 — Game-Installer-Fix

Der Game-Installer setzt nach dem Entpacken das erwartete Programm unter `<game>/bin/<game>` explizit auf ausführbar (`0755`). Damit starten Spiele auch dann, wenn das ZIP-Archiv – etwa durch Erstellung auf einem FAT-/Windows-Dateisystem – keine Unix-Ausführungsrechte enthält.

Der Installer prüft außerdem, ob die erwartete Binärdatei im Archiv vorhanden ist, und meldet einen verständlichen Fehler, wenn sie fehlt oder nicht ausführbar gemacht werden kann. Die ZIP-Dateien von Midless und Geometry Rush sind intakt; ihr bisher fehlendes Ausführungsbit war die Ursache dafür, dass die Spiele nach dem Installieren nicht starteten.

# v8.5.6 · 2026-10-26

# AppDock 8.5.6 — Games im AppStore

Der AppStore besitzt jetzt eine eigene **Games**-Sektion. Spiele werden aus dem separaten `games.txt`-Katalog geladen und zeigen neben ihrer Lua-DApp auch das zugehörige ZIP-Paket.

Nach sichtbarer Installationsbestätigung prüft AppDock das ZIP-Archiv, weist absolute und unsichere Pfade zurück und entpackt den Paketinhalt in das KOReader-Geräteverzeichnis `.adds`. Damit können Spiele wie Midless ihre nativen Dateien und Assets gemeinsam mit der Lua-Oberfläche installieren.

Der DApps-Katalog enthält dafür `midless.lua`, `games.txt` und `midless.zip`. Die bestehenden App-, Widget-, Design- und Sleepscreen-Kategorien bleiben erhalten.

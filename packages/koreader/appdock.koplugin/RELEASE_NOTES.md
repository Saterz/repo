# v8.2.7 · 2026-10-17

# AppDock 8.2.7

Element-Hintergründe in Sleepscreens unterstützen jetzt Transparenz.

Im Editor kann die Deckkraft eines Element-Hintergrunds zwischen 0 % und 100 % eingestellt werden. Das deklarative Format verwendet dafür `background_alpha` zwischen `0` und `1`; bestehende Presets ohne dieses Feld bleiben vollständig opak. Auf farbfähigen Geräten wird die Deckkraft über den RGB-Blending-Pfad gerendert, während monochrome Geräte den kompatiblen Graustufen-Fallback behalten.

# v8.2.6 · 2026-10-17

# AppDock 8.2.6

Ein Farbfix für Sleepscreens auf farbfähigen E-Ink-Geräten.

Der Sleepscreen-Renderer verwendet definierte `#RRGGBB`-Farben nun als echte RGB-Farben und zeichnet farbige Hintergründe über den RGB-Blitbuffer-Pfad. Auf monochromen Geräten bleibt die luminanzbasierte Graustufen-Darstellung als kompatibler Fallback erhalten. Ein Regressionstest deckt beide Farbpfade ab.

# v8.2.5 · 2026-10-17

# AppDock 8.2.5

Ein Touch-Fix für den Sleepscreen-Editor.

- Behebt die fehlende Touch-Reaktion auf Editor-Buttons.
- `Layout.FixedStack` leitet Eingabeereignisse jetzt an interaktive untergeordnete Widgets weiter.
- Ergänzt die Release- und Versionsangaben für den neuen Patch-Release.

# v8.2.4 · 2026-10-17

# AppDock 8.2.4

A usability update for the Sleep-Screen editor.

- Reorganizes editing into clear Screen, Elements, Edit, and Save areas instead of one long stack of controls.
- Groups related settings into compact cards with two-column fields, clearer layer selection, and direct element creation.
- Keeps the live preview visible and shows whether the draft has unsaved changes.
- Refreshes the saved-state UI even when saving succeeds but activation fails, with regression coverage for that case.
- Adds UI regression coverage for section navigation and portrait layout.

# v8.2.3 · 2026-10-17

# AppDock 8.2.3

A bug-fix release for the public Sleep-Screen catalog.

- Fixes a crash when rendering public catalog results by avoiding a loop variable that shadowed the gettext translation function.
- Adds regression coverage for loading and rendering a non-empty public preset list in the AppStore.

# v8.2.3 · 2026-10-17

# AppDock 8.2.3

A bug-fix release for the public Sleep-Screen catalog.

- Fixes a crash when rendering public catalog results by avoiding a loop variable that shadowed the gettext translation function.
- Adds regression coverage for loading and rendering a non-empty public preset list in the AppStore.

# v8.2.2 · 2026-10-17

# AppDock 8.2.2

A bug-fix release for publishing Sleep-Screen presets.

- Fixes publication failures caused by ambiguous PostgreSQL column references in the `tbs_publish_sleepscreen` RPC.
- Adds an additive Supabase migration to repair databases where the original Sleep-Screen migration was already applied.
- Updates the deployment guide with the migration order and clarifies that public catalog availability does not confirm that private publishing is configured correctly.

# v8.2.1 · 2026-10-17

Fixes AppStore Sleepscreens tab and Settings → Other → Sleepscreen editor module loading when KOReader uses another plugin’s Lua search paths.

# v8.2.0 · 2026-10-17

# AppDock 8.2.0

A feature release introducing shareable Sleep-Screens.

- Adds a **Sleepscreens** area to the AppStore with searchable public presets, creator attribution, previews, and offline downloads.
- Adds a native Sleep-Screen editor with instant preview and support for images, custom fonts, text, colors, widgets, and information cards such as battery status.
- Saves presets locally for offline use and supports publishing and updating presets through a TBS account.
- Adds a shared catalog backend with validated declarative layouts, private asset storage, immutable revisions, and protected publishing.

Global publishing requires the TBS account and the deployed Supabase backend. Local editing, activation, and installed presets work offline.

# v8.1.1 · 2026-10-17

# AppDock 8.1.1

A small stability release for TBS account setup and manual installation.

- Refreshes the active AppDock screen after the one-time TBS recovery-code dialog closes, so the new signed-in state is shown reliably.
- Clarifies that GitHub's automatically generated source ZIP contains an outer project folder; install only the inner `appdock.koplugin` directory.

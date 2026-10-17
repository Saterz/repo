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

# v8.1.0 · 2026-10-17

# AppDock 8.1.0

A homescreen and account update focused on the Android-inspired setup flow, app organization, and device migration.

- Repairs the new setup wizard entry in Settings and makes its multi-step dialog flow resilient to E-Ink redraws and modal transitions.
- Adds a bundled default homescreen wallpaper for first-time setup.
- Adds Android-style app groups: one homescreen-sized tile can contain multiple apps.
- Adds TBS account registration and recovery-code migration between readers, with compact settings sync and an installed-app manifest.
- Requires a TBS account to open AppStore, YouTube, YouTube Music, and DockUpdate.
- Keeps reader-specific files and paths, books, DChat messages, lockscreen secrets, and server keys out of TBS cloud snapshots. App installs on a new reader remain individually confirmed.
- Adds the TBS Supabase migration and Edge Function. TBS cloud features require the operator to apply the SQL migration and deploy the `tbs-account` Edge Function to the existing DChat Supabase project first. See [`TBS_SUPABASE_EINFACH.md`](TBS_SUPABASE_EINFACH.md).
- Updates DockUpdate's allowlist so it can install the new AppDock modules and the static default wallpaper.

# v8.0.2 · 2026-10-17

Hotfix for startup stability after the new setup wizard.\n\n- Loads the optional Wi-Fi migration module only when migration is opened.\n- Removes the obsolete DockUpdate password confirmation; installation still requires the normal visible confirmation.

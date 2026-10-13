# v0.2 · 2026-05-14

- Added Dispatcher integration for Gesture shortcut support.
- Fixed FileChooser crash on certain device firmwares when importing tokens.
- Added manual text input fallback for token import.
- Removed `curl` dependency; plugin is now 100% pure Lua using native `socket.http`.
- Polished README and UI formatting.

**Full Changelog**: https://github.com/right9code/githubbrowser.koplugin/compare/v0.1...v0.2

# v0.1 · 2026-05-14

Initial release of the GitHub Browser plugin for KOReader!

**Features:**
- Browse public and private repositories
- View and download files
- Multi-token management
- Pin and bookmark repositories

**Installation:** Download the source code zip below, extract it, and place the `githubbrowser.koplugin` folder inside your KOReader `plugins/` directory.

- Fixed a crash on Kobo devices when importing tokens, added a manual path fallback option, and improved README formatting.

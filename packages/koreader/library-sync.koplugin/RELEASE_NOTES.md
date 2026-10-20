# v0.7.4 · 2026-10-20

# Library Sync 0.7.4

Clearer installation and discovery for ordinary KOReader users.

Library Sync downloads missing EPUB books and CBZ comics from Grimmory or
BookOrbit, organizes local files and refreshes server metadata. It does not
require Bookshelf, OrbitUI or SimpleUI.

## What's new

- Updated English introduction, feature overview and requirements.
- Separate Storefront/AppStore and manual installation instructions, with a clear
  distinction between new installations and the legacy Grimmory directory.
- Explicit explanation of optional UI integrations, opt-in Mirror/automatic
  refresh, and what belongs to BookOrbit's separate progress-sync plugin.
- Reproducible runtime packages, SHA-256 sidecars and automated packaging checks.

This is a documentation and packaging release. Server providers, sync behavior,
saved credentials, local paths, routing profiles and manifests are unchanged from
0.7.3. That version's Grimmory library-source support remains included.

## Install or update

New installation: choose **library-sync.koplugin.zip**, extract it into
`koreader/plugins/`, and restart. Storefront/AppStore users should choose the
**komadorirobin/library-sync.koplugin** entry and this stable release.

Existing installations can use **Library Sync > Check for updates**.
If your installation still uses `grimmory-sync.koplugin`, the built-in updater
selects **grimmory-sync.koplugin.zip**. Do not install both directories.
All settings and reading data are retained.

## Verification

Provider contract tests pass under Lua 5.1 and LuaJIT. Runtime ZIP contents,
canonical/legacy equivalence and checksums are validated. No physical e-reader
installation or live server sync was performed for this documentation release.

# v0.7.3 · 2026-10-19

## What's new

- Add complete Grimmory libraries as selectable sync sources alongside shelves and Magic Shelves.
- Library sources apply consistently to missing-book sync, metadata refresh, and Mirror selected sync source.
- Keep compatibility with older Grimmory versions that do not expose the libraries endpoint.
- Document library selection and add provider contract coverage for both new and legacy Grimmory servers.

Grimmory library selection requires a server version that exposes `/api/v1/opds/libraries`, available in Grimmory 3.5.0.

Both ZIP assets are included for new and legacy OTA installations.

# v0.7.2 · 2026-10-13

## What's new

- Add compatibility with BookOrbit 3.4.0's plain-text OPDS descriptions.
- Compare description content semantically, treating equivalent HTML and plain text as unchanged.
- Migrate existing HTML-based manifest signatures locally instead of downloading and replacing unchanged EPUB/CBZ files.
- Continue detecting genuine description text changes.
- Add regression coverage for HTML-to-text migration and real description changes.

After updating, cancel any previously prepared mass refresh and run **Refresh existing metadata** again. The first scan may take its usual time while old signatures are migrated, but equivalent descriptions should be skipped rather than downloaded.

Both ZIP assets are included for new and legacy OTA installations.

# v0.7.1 · 2026-10-13

## What's new

- Use BookOrbit's download response filename when **Server file name** is selected, avoiding unnecessary `Title - Author` fallback names.
- Preserve existing local paths during metadata refresh so manifest tracking remains stable.
- Validate response filenames against the expected EPUB or CBZ format before using them.
- Keep an existing server-named destination untouched instead of overwriting it.
- Improve `Content-Disposition` parsing and add regression coverage for EPUB, CBZ, refresh paths, and invalid extensions.

Thanks to @kai-arsenault for the original fix in #8.

Both ZIP assets are included for new and legacy OTA installations.

# v0.7.0 · 2026-08-30

## What's new

- Add first-class CBZ manga/comic support for Grimmory and BookOrbit OPDS libraries.
- Preserve CBZ extensions across folder routing and every file-naming profile.
- Support CBZ files in missing-book sync, metadata refresh, Mirror cleanup and restore, and BookOrbit local registration.
- Prevent EPUB and CBZ files from being mistaken for one another during matching or replacement.
- Update the README and installation guide for EPUB/CBZ libraries.

Both ZIP assets are included for new and legacy OTA installations.

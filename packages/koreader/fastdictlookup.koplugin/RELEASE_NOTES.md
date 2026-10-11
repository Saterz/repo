# v1.6.0 · 2026-10-11

## What's Changed
* Use correct stardict_strcmp for index lookups by @fnimick in https://github.com/Sirozha1337/fastdictlookup.koplugin/pull/2

## New Contributors
* @fnimick made their first contribution in https://github.com/Sirozha1337/fastdictlookup.koplugin/pull/2

**Full Changelog**: https://github.com/Sirozha1337/fastdictlookup.koplugin/compare/v1.5.0...v1.6.0

# v1.5.0 · 2026-07-27

Fix compatibility issues with new KOReader version 2026.07.

**Full Changelog**: https://github.com/Sirozha1337/fastdictlookup.koplugin/compare/v1.4.0...v1.5.0

# v1.4.0 · 2026-07-24

* New Full Definition Lookup menu
* Put all settings in sub menu
* Add new settings
    * **Enable Highlighting** - if enabled, first tap on "ok" button will go into highlighting mode
    * **Override Default Lookup Menu** - if enabled, tapping the word will open full definition instead of opening the default KOReader's context menu

**Full Changelog**: https://github.com/Sirozha1337/fastdictlookup.koplugin/compare/v1.3.1...v1.4.0

# v1.3.1 · 2026-05-28

Fix Footnote Lookup issues:
* Footnotes with h1..h6 headers were ignored due to excessive flag
* Plugin crashes on looking up HTTP/HTTPs links (now they are ignored)

**Full Changelog**: https://github.com/Sirozha1337/fastdictlookup.koplugin/compare/v1.3.0...v1.3.1

# v1.3.0 · 2026-05-08

Features:
* Text Highlighting Mode: pressing the button now enables highliting mode, pressing it again opens context menu for the selected text

Fixes:
* Optimize page redraws by only repainting parts of the screen where the cursor is
* Avoid reading dictionary file twice when it has required metadata

**Full Changelog**: https://github.com/Sirozha1337/fastdictlookup.koplugin/compare/v1.2.0...v1.3.0

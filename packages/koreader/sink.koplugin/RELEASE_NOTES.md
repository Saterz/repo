# 26.10.23 · 2026-10-23

### What's Changed

- **Fixed localization across all languages**: Sink was previously staying in English regardless of your KOReader language setting. Menus, pairing screens, and status notifications now properly display in your active language (French, German, Spanish, Portuguese, Russian, Chinese, Japanese, and more).
- **Multi-line translation support**: Fixed an issue in the translation parser where multi-line error alerts and pairing instructions weren't matching up and fell back to English.
- **Regional dialect matching**: Added smoother handling for regional language settings like Brazilian Portuguese.

Special thanks to **@jpiebrig** on GitHub for reporting the issue, digging into why translations weren't loading, and sharing the fix!

**Full Changelog**: https://github.com/ultimatejimmy/sink/compare/26.10.2...26.10.23

# 26.10.2 · 2026-10-02

## What's Changed
* fix(suspend): support silent sleep sync on Kobo devices by @bennybrainless in https://github.com/ultimatejimmy/sink/pull/3
* Updated translations, thanks to @jpiebrig for helping with the French

## New Contributors
* @bennybrainless made their first contribution in https://github.com/ultimatejimmy/sink/pull/3

**Full Changelog**: https://github.com/ultimatejimmy/sink/compare/26.9.10...26.10.2

# 26.9.10 · 2026-09-10

- Add pin for security

**Full Changelog**: https://github.com/ultimatejimmy/sink/compare/26.9.4...26.9.10

# 26.9.4 · 2026-09-04

- Remove x-ray sync
- make normal sync delayed to prevent memory issues

**Full Changelog**: https://github.com/ultimatejimmy/sink/compare/26.9.2...26.9.4

# 26.9.2 · 2026-09-02

Add updater, better UI, list of book, list of devices, welcome screen.

**Full Changelog**: https://github.com/ultimatejimmy/sink/compare/26.8.31.10...26.9.2

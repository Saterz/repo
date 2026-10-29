# 0.6.0 · 2026-10-29

## Requires KOReader 2026.07 or newer

KOReader 2026.07 includes the stylus input support this plugin needs. You no longer need to replace KOReader's `input.lua`. Just copy the `pencil.koplugin` folder into KOReader's `plugins` folder.

Upgrading from an earlier release? Update KOReader to 2026.07 or newer. That installs a fresh `input.lua` over the modified one.

On an older KOReader? Use [0.5.0](https://github.com/mysticknits/pencil.koplugin/releases/tag/0.5.0), which still includes `input.lua`.
## What's Changed
* Drop bundled input.lua; require KOReader 2026.07+ by @mysticknits in https://github.com/mysticknits/pencil.koplugin/pull/91


**Full Changelog**: https://github.com/mysticknits/pencil.koplugin/compare/0.5.0...0.6.0

# 0.5.0 · 2026-05-18

## What's Changed
* Debounce saves, defer bookmark sync, page-index eraser to cut lag for by @mysticknits in https://github.com/mysticknits/pencil.koplugin/pull/68
* add annotation preview and orientation change support by @mysticknits in https://github.com/mysticknits/pencil.koplugin/pull/70


**Full Changelog**: https://github.com/mysticknits/pencil.koplugin/compare/0.4.1...0.5.0

# 0.4.1 · 2026-05-12

## What's Changed
* Side button highlight by @mysticknits in https://github.com/mysticknits/pencil.koplugin/pull/65


**Full Changelog**: https://github.com/mysticknits/pencil.koplugin/compare/0.4.0...0.4.1

# 0.4.0 · 2026-05-11

## What's Changed
* Update compatibility name from Ghost to Snowflake by @mysticknits in https://github.com/mysticknits/pencil.koplugin/pull/46
* Feature/pen width experimental by @mysticknits in https://github.com/mysticknits/pencil.koplugin/pull/53
* Detect side button by @CharlieQLe in https://github.com/mysticknits/pencil.koplugin/pull/49
* fix: use getTopmostVisibleWidget so invisible decorations don't gate stylus input by @AndyHazz in https://github.com/mysticknits/pencil.koplugin/pull/58
* docs: README updates for next release by @mysticknits in https://github.com/mysticknits/pencil.koplugin/pull/62

## New Contributors
* @CharlieQLe made their first contribution in https://github.com/mysticknits/pencil.koplugin/pull/49
* @AndyHazz made their first contribution in https://github.com/mysticknits/pencil.koplugin/pull/58

**Full Changelog**: https://github.com/mysticknits/pencil.koplugin/compare/0.3.1...0.4.0

# 0.3.1 · 2026-03-26

For this release, you will need to swap the input.lua as well as the plugin itself! Please check the README for specific info on how to do that.

xoxo

## What's Changed
* Add compatibility note for Koreader - Ghost by @mysticknits in https://github.com/mysticknits/pencil.koplugin/pull/42
* Koreader version support 03.2026 by @mysticknits in https://github.com/mysticknits/pencil.koplugin/pull/45


**Full Changelog**: https://github.com/mysticknits/pencil.koplugin/compare/0.3.0...0.3.1

# v1.10.0 · 2026-10-23

## [1.10.0](https://github.com/pierspad/notebook.koplugin/compare/v1.9.1...v1.10.0) (2026-10-23)

### ✨ New Features

* add gallery grid density toggle (3x2 vs 4x3) and center cards vertically ([e59ef95](https://github.com/pierspad/notebook.koplugin/commit/e59ef959c0d07685302581139b7e541b1e7ac803))

# v1.9.1 · 2026-10-23

## [1.9.1](https://github.com/pierspad/notebook.koplugin/compare/v1.9.0...v1.9.1) (2026-10-23)

### 🐛 Bug Fixes

* keep KOReader input chain safe after closing a notebook ([856f2ec](https://github.com/pierspad/notebook.koplugin/commit/856f2ec243f13dd923a09caa04e3ca7f60114cfa))

# v1.9.0 · 2026-10-10

## [1.9.0](https://github.com/pierspad/notebook.koplugin/compare/v1.8.0...v1.9.0) (2026-10-10)

### ✨ New Features

* improve gallery navigation and folder naming ([ad3c5d5](https://github.com/pierspad/notebook.koplugin/commit/ad3c5d5a2f7f6249e761994bf4e1c5aa04681b2e))

# v1.8.0 · 2026-10-09

## [1.8.0](https://github.com/pierspad/notebook.koplugin/compare/v1.7.2...v1.8.0) (2026-10-09)

### Features

* allow explicit opt-in to prerelease plugin updates ([47757a3](https://github.com/pierspad/notebook.koplugin/commit/47757a396283963562af134899af7dd3c732d0ab))

### Bug Fixes

* reject mislabeled Scribe 2 palm slots without losing stylus fallback ([fdbad4f](https://github.com/pierspad/notebook.koplugin/commit/fdbad4f5397715ea13065f5b47ee1048d50d56c6)), closes [#4](https://github.com/pierspad/notebook.koplugin/issues/4)

# v1.7.2 · 2026-10-07

## [1.7.2](https://github.com/pierspad/notebook.koplugin/compare/v1.7.1...v1.7.2) (2026-10-07)

### Bug Fixes

* reject persistent palm contacts and erase arrows without object menus ([43b58e7](https://github.com/pierspad/notebook.koplugin/commit/43b58e70ed6fa887aecbe071417977eebbff99f0))

- Palm contacts remain blocked during pen proximity and until finger release; pen takeover clears stale zoom-pan origins.
- Lines and arrows now erase in whole-stroke or area mode without opening object menus. Undo restores the original shape.
- Text stacking controls are omitted for selected lines and arrows.

Validated with the full test bench, package checks and native rendering checks in all shipped languages.

The intermittent Scribe issue where library titles reappear around handwriting has not been reproduced and is not claimed as fixed in this release.

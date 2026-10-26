# v1.11.1-dev.2 · 2026-10-26

## [1.11.1-dev.2](https://github.com/pierspad/notebook.koplugin/compare/v1.11.1-dev.1...v1.11.1-dev.2) (2026-10-26)

### 🐛 Bug Fixes

* clean up failed PDF buffer allocations ([d76aa78](https://github.com/pierspad/notebook.koplugin/commit/d76aa78ed47857b46315c5ea4f59cea5d37ccad3))
* default missing text sizes on load ([953d370](https://github.com/pierspad/notebook.koplugin/commit/953d370631381179c03db5ec1b619703befdd0ec))

### 🔧 Improvements

* avoid sorting simple shape scanlines ([b98ca49](https://github.com/pierspad/notebook.koplugin/commit/b98ca49f2538a893df746795c5baec4096030a3b))
* prune whole-stroke eraser queries ([bfd6ada](https://github.com/pierspad/notebook.koplugin/commit/bfd6ada18110afeea863f37a19b632a2a1b83b63))
* stream Xournal++ marker contours ([ec7d58b](https://github.com/pierspad/notebook.koplugin/commit/ec7d58bb4c63c58c370351dc751014fd2751fc70))
* use native CRC for Xournal++ exports ([1a34768](https://github.com/pierspad/notebook.koplugin/commit/1a347688d61efccd89683c9bcd7b2affb0727f77))

# v1.11.1-dev.1 · 2026-10-24

## [1.11.1-dev.1](https://github.com/pierspad/notebook.koplugin/compare/v1.11.0...v1.11.1-dev.1) (2026-10-24)

### 🐛 Bug Fixes

* use sans-serif release notes ([7910f13](https://github.com/pierspad/notebook.koplugin/commit/7910f133424060edc026843710c883d8f620de72))

# v1.11.0-dev.3 · 2026-10-24

## [1.11.0-dev.3](https://github.com/pierspad/notebook.koplugin/compare/v1.11.0-dev.2...v1.11.0-dev.3) (2026-10-24)

### 🐛 Bug Fixes

* reconcile gray ink with regional REAGL ([8574f9e](https://github.com/pierspad/notebook.koplugin/commit/8574f9e8f5480aeadf1d138abef25821b36bb406))

# v1.11.0-dev.2 · 2026-10-24

## [1.11.0-dev.2](https://github.com/pierspad/notebook.koplugin/compare/v1.11.0-dev.1...v1.11.0-dev.2) (2026-10-24)

### 🐛 Bug Fixes

* recover from PDF preview failures ([d3d824f](https://github.com/pierspad/notebook.koplugin/commit/d3d824f163985173189d95fef0ff403acd7ff83b))

### 🔧 Improvements

* cache brush modules in input loops ([7b8dabd](https://github.com/pierspad/notebook.koplugin/commit/7b8dabd422e9fdf11a89c296995c2ec134f7a70b))
* crop page snapshots to drawable content ([32048e6](https://github.com/pierspad/notebook.koplugin/commit/32048e692146409b60d5b92f99e5df1211a43a6f))
* keep ink tile copies tightly packed ([0b4d3a6](https://github.com/pierspad/notebook.koplugin/commit/0b4d3a6a48ff20658e99e05dd1cb738e59e34b26))
* load only the thumbnail page strokes ([5ae99d2](https://github.com/pierspad/notebook.koplugin/commit/5ae99d2b149d5f83a2becf7b356783857eee2df6))
* snapshot only active ink tiles ([1e67165](https://github.com/pierspad/notebook.koplugin/commit/1e671651f4e362de0595dc416abc821735cddd56))

# v1.11.0-dev.1 · 2026-10-23

## [1.11.0-dev.1](https://github.com/pierspad/notebook.koplugin/compare/v1.10.0...v1.11.0-dev.1) (2026-10-23)

### ✨ New Features

* add clickable gallery folder breadcrumbs and direct home navigation ([97c0507](https://github.com/pierspad/notebook.koplugin/commit/97c05075596ad6740d186ced55b38af293787b25))

### 🐛 Bug Fixes

* autosave committed eraser and lasso edits ([930def9](https://github.com/pierspad/notebook.koplugin/commit/930def91261d2b23117175513973f1adea9a3567))
* contain updater and text dialog callback failures ([5c745e6](https://github.com/pierspad/notebook.koplugin/commit/5c745e6319b0f5ccee78b648a1d287ab14057e33))
* show gallery grid layouts and progressive thumbnails ([9cfb032](https://github.com/pierspad/notebook.koplugin/commit/9cfb032ca1b955c9ee0a2371a799fc5f2a97346a))

### 🔧 Improvements

* cache empty notebook thumbnail results ([1ed6827](https://github.com/pierspad/notebook.koplugin/commit/1ed6827eea7f6445f4847813cee28fab46d0009b))
* prepare shared PDFs with incremental export jobs ([619b4b7](https://github.com/pierspad/notebook.koplugin/commit/619b4b70a46d48ae65397eed2f56f61b73105dc3))

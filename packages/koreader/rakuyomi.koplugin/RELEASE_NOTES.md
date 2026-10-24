# v1.44.3 · 2026-10-24

## [1.44.3](https://github.com/tachibana-shin/rakuyomi/compare/v1.44.2...v1.44.3) (2026-10-24)


### Bug Fixes

* mprove UnixServer:stop() with exit wait logic ([d539181](https://github.com/tachibana-shin/rakuyomi/commit/d53918143f9fd3139d98fb14ee034c38f8ebf817)), closes [#394](https://github.com/tachibana-shin/rakuyomi/issues/394)

# v1.44.2 · 2026-10-23

## [1.44.2](https://github.com/tachibana-shin/rakuyomi/compare/v1.44.1...v1.44.2) (2026-10-23)


### Bug Fixes

* **epub:** generate valid XHTML chapter content ([#393](https://github.com/tachibana-shin/rakuyomi/issues/393)) ([a214f47](https://github.com/tachibana-shin/rakuyomi/commit/a214f47c24e7a696caef082d1d57120cc3157814))

# v1.44.1 · 2026-10-19

## [1.44.1](https://github.com/tachibana-shin/rakuyomi/compare/v1.44.0...v1.44.1) (2026-10-19)


### Bug Fixes

* **tracking:** push local progress on link when ahead of tracker ([#381](https://github.com/tachibana-shin/rakuyomi/issues/381)) ([99d501d](https://github.com/tachibana-shin/rakuyomi/commit/99d501db7d164bdb9094dd01a6e44bb3246cc0ad))

# v1.44.0 · 2026-10-19

# [1.44.0](https://github.com/tachibana-shin/rakuyomi/compare/v1.43.4...v1.44.0) (2026-10-19)


### Bug Fixes

* **build:** pin rquickjs to 0.12.2 so bindgen is enabled ([#386](https://github.com/tachibana-shin/rakuyomi/issues/386)) ([942c4ec](https://github.com/tachibana-shin/rakuyomi/commit/942c4ecc2eb53e2d6661b24fa83d381c967cb532))
* **reader:** only enforce recommended reader settings when opted in ([#388](https://github.com/tachibana-shin/rakuyomi/issues/388)) ([63c3dd9](https://github.com/tachibana-shin/rakuyomi/commit/63c3dd93e2c386f5ed71dd699f0f5b7fe26a3787)), closes [#378](https://github.com/tachibana-shin/rakuyomi/issues/378) [#379](https://github.com/tachibana-shin/rakuyomi/issues/379)
* **ui:** cap source language lists to keep menu post_text short ([#387](https://github.com/tachibana-shin/rakuyomi/issues/387)) ([0a90969](https://github.com/tachibana-shin/rakuyomi/commit/0a90969c44531dd82e79c77b2f2dccbf5905093e)), closes [#374](https://github.com/tachibana-shin/rakuyomi/issues/374)
* **update:** create update download temp file next to the plugin directory ([#390](https://github.com/tachibana-shin/rakuyomi/issues/390)) ([4ca2937](https://github.com/tachibana-shin/rakuyomi/commit/4ca29379dfb0eb44b7dab1cfcd24a0d675dae205)), closes [#362](https://github.com/tachibana-shin/rakuyomi/issues/362)


### Features

* **reader:** add configurable page overlap in continuous mode ([#389](https://github.com/tachibana-shin/rakuyomi/issues/389)) ([9f30a45](https://github.com/tachibana-shin/rakuyomi/commit/9f30a452d83de5a192b2e4f41d4d10d98bd01854)), closes [#376](https://github.com/tachibana-shin/rakuyomi/issues/376)

# v1.43.4 · 2026-10-11

## [1.43.4](https://github.com/tachibana-shin/rakuyomi/compare/v1.43.3...v1.43.4) (2026-10-11)


### Performance Improvements

* **cookie-bot:** stop registering bot commands on every cold isolate ([30d8002](https://github.com/tachibana-shin/rakuyomi/commit/30d80029c0566587edc415dd23a57561d948a720))

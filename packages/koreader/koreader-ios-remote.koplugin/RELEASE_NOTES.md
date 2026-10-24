# v0.6.1 · 2026-10-24

## What's new

### Added

- Page-turn statistics in Settings, showing confirmed Next Page commands for this month and all time. Tracking starts with this version; earlier page turns are not included.
- A layered app icon for iPhone and Apple Watch, with Default, Dark, Clear, and Tinted appearances on iPhone.

### Changed

- Simplified Settings, with volume and media controls directly on the main settings screen and setup/troubleshooting links under Help.
- Connection tests now show a dedicated testing state and a clear connection result.

### Fixed

- Prevented an outdated Apple Watch pairing from relaying actions to a newly paired reader.
- Prevented results from an earlier Watch pairing from overwriting the current connection state.
- Made volume and media control errors visible in Settings, improved recovery when the audio engine stops, and ignored queued control events after capture is disabled.
- Manual pairing now ignores surrounding whitespace in the port and pairing secret.

### Updating

- Update the iPhone and Apple Watch apps together. Older Watch apps cannot relay page actions through the updated iPhone app.


## Downloads

- **iOS IPA — AltStore Classic**: iPhone/iPad app. Import the unsigned IPA through AltStore Classic; opening it directly does not install it.
- **KOReader Plugin**: extract the ZIP, copy `remote_turner.koplugin` into KOReader's `plugins` folder, then restart KOReader.
- **SHA-256 Checksums**: verify your downloads against `SHA256SUMS`.

## Apple Watch

Install from source using Xcode and the **KORemoteFull** scheme, or try **KORemoteFreeWatch** with a Personal Team. Pair KOReader on the iPhone first. Watch provisioning with a free account remains experimental. The AltStore IPA does not include the Watch app; there is no separate Watch IPA to install.

## Setup

See the [installation guide](https://github.com/maxoliinyk/koreader-ios-remote/blob/v0.6.1/README.md) and [distribution details](https://github.com/maxoliinyk/koreader-ios-remote/blob/v0.6.1/DISTRIBUTION.md) for requirements, signing, pairing, updates, and troubleshooting.

GitHub's **Source code** downloads are for building the project yourself, not installing the iPhone app. The app and plugin use your local Wi-Fi network; keep KOReader awake while turning pages.

# v0.5 · 2026-10-23

## Downloads

- **iOS IPA — AltStore Classic**: iPhone/iPad app. Import the unsigned IPA through AltStore Classic; opening it directly does not install it.
- **KOReader Plugin**: extract the ZIP, copy `remote_turner.koplugin` into KOReader's `plugins` folder, then restart KOReader.
- **SHA-256 Checksums**: verify your downloads against `SHA256SUMS`.

## Apple Watch

Install from source using Xcode and the **KORemoteFull** scheme, or try **KORemoteFreeWatch** with a Personal Team. Pair KOReader on the iPhone first. Watch provisioning with a free account remains experimental. The AltStore IPA does not include the Watch app; there is no separate Watch IPA to install.

## Setup

See the [installation guide](https://github.com/maxoliinyk/koreader-ios-remote/blob/v0.5/README.md) and [distribution details](https://github.com/maxoliinyk/koreader-ios-remote/blob/v0.5/DISTRIBUTION.md) for requirements, signing, pairing, updates, and troubleshooting.

GitHub's **Source code** downloads are for building the project yourself, not installing the iPhone app. The app and plugin use your local Wi-Fi network; keep KOReader awake while turning pages.


**Full Changelog**: https://github.com/maxoliinyk/koreader-ios-remote/commits/v0.5

# v0.5.2 · 2026-10-27

Fixes "account history", "account marked for later" and "view your AO3 profile" when logged in
Apologies for not noticing these issues in the last release

## What's Changed
* Fix username parse by @IntrovertedMage in https://github.com/IntrovertedMage/AO3Downloader.koplugin/pull/57


**Full Changelog**: https://github.com/IntrovertedMage/AO3Downloader.koplugin/compare/v0.5.1...v0.5.2

# v0.5.1 · 2026-10-16

Just a quick fix for a login issue

## What's Changed
* Login fix by @IntrovertedMage in https://github.com/IntrovertedMage/AO3Downloader.koplugin/pull/55


**Full Changelog**: https://github.com/IntrovertedMage/AO3Downloader.koplugin/compare/v0.5.0...v0.5.1

# v0.5.0 · 2026-09-04

This update mainly is made up of features and bug fixes made by @JayBigGuy10 on their fork. I'd like to thank them so much for submitting all these code requests to this version of the plugin.

## What's Changed
* Fix tag parsing to handle full stops in searchByTag function by @IntrovertedMage in https://github.com/IntrovertedMage/AO3Downloader.koplugin/pull/22
* Add browsing of the current logged in account history and marked for later to the search menu by @JayBigGuy10 in https://github.com/IntrovertedMage/AO3Downloader.koplugin/pull/31
* rearrange the downloaded fanfics menu so there are less button presses by @JayBigGuy10 in https://github.com/IntrovertedMage/AO3Downloader.koplugin/pull/33
* Fun change to make it more AO3'y by @JayBigGuy10 in https://github.com/IntrovertedMage/AO3Downloader.koplugin/pull/32
* show what chapter has been read up to in a downloaded work, also show author names by @JayBigGuy10 in https://github.com/IntrovertedMage/AO3Downloader.koplugin/pull/37
* Fix the bookmarked works count being 0 when the logged in user views their own profile by @JayBigGuy10 in https://github.com/IntrovertedMage/AO3Downloader.koplugin/pull/38
* fix crash that happens if works is nil because of work fetch failure by @JayBigGuy10 in https://github.com/IntrovertedMage/AO3Downloader.koplugin/pull/36
* fix issue with chapter parsing when in full work mode by @JayBigGuy10 in https://github.com/IntrovertedMage/AO3Downloader.koplugin/pull/35
* Add bookmark, mark for later and subscription support in fanfic_reader by @JayBigGuy10 in https://github.com/IntrovertedMage/AO3Downloader.koplugin/pull/34
* Fix filter search crash on additional tag exclusion by @JayBigGuy10 in https://github.com/IntrovertedMage/AO3Downloader.koplugin/pull/42
* fix crash when a users pseud only has exactly one work by @JayBigGuy10 in https://github.com/IntrovertedMage/AO3Downloader.koplugin/pull/43
* Add support for browsing a users collections by @JayBigGuy10 in https://github.com/IntrovertedMage/AO3Downloader.koplugin/pull/40
* Improve UI for bookmark creation/updates, add collections search feature and auto fetch most recent bookmark details before opening editing widget by @IntrovertedMage in https://github.com/IntrovertedMage/AO3Downloader.koplugin/pull/44
* Update user collections and series page to allow for fetching beyond first page by @IntrovertedMage in https://github.com/IntrovertedMage/AO3Downloader.koplugin/pull/47
* Enhance filename template sanitization to prevent invalid characters and trailing spaces by @IntrovertedMage in https://github.com/IntrovertedMage/AO3Downloader.koplugin/pull/48
* Fix download dialog and downloaded works menu anonymous author issue by @IntrovertedMage in https://github.com/IntrovertedMage/AO3Downloader.koplugin/pull/49
* Actually fix download menu anonymous author issue by @IntrovertedMage in https://github.com/IntrovertedMage/AO3Downloader.koplugin/pull/50

## New Contributors
* @JayBigGuy10 made their first contribution in https://github.com/IntrovertedMage/AO3Downloader.koplugin/pull/31

**Full Changelog**: https://github.com/IntrovertedMage/AO3Downloader.koplugin/compare/v0.4.0...v0.5.0

# v0.4.0 · 2025-12-28

## What's Changed
* Fix cookie parsing by @IntrovertedMage in https://github.com/IntrovertedMage/AO3Downloader.koplugin/pull/15
* Ao3 downloader code refactor by @IntrovertedMage in https://github.com/IntrovertedMage/AO3Downloader.koplugin/pull/16
* Add user search and profile view feature by @IntrovertedMage in https://github.com/IntrovertedMage/AO3Downloader.koplugin/pull/17
* Add confirmation button dialog before running operation settings  by @IntrovertedMage in https://github.com/IntrovertedMage/AO3Downloader.koplugin/pull/18


**Full Changelog**: https://github.com/IntrovertedMage/AO3Downloader.koplugin/compare/v0.3.2...v0.4.0

## To Download:
Download and extract the zip file `AO3Downloader-v0.4.0.zip`.
Move the folder `AO3Downloader.koplugin` inside the extracted folder to your devices `koreader/plugins` folder.

The menu option to open the plugins menu should then be found under the search tab while the filemanger is open.

# v0.3.2 · 2025-11-23

## What's Changed
* Fix searching works by & relationship tag by @IntrovertedMage in https://github.com/IntrovertedMage/AO3Downloader.koplugin/pull/13


**Full Changelog**: https://github.com/IntrovertedMage/AO3Downloader.koplugin/compare/v0.3.1...v0.3.2

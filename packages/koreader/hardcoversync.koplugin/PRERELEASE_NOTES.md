# v2.4.0-beta.1 · 2026-10-25

Browse community reviews even when you are offline. Pages you have opened, including their full text and your place in the list, stay on this device; spoiler protection stays in place, and a later refresh replaces the saved copy only when it succeeds.

## ✨ New

- **Reviews you have opened work offline.** Your saved pages keep their text, spoilers and place in the list. A partial saved list says so clearly, and a failed refresh never removes what you can already read. (#208)
- **Add to a book’s journal from the reader.** The Journal screen now has a plus button for a note, quote or review. It works offline, appears in the list immediately and reuses the existing forms. (#201)
- **Journal replaces Activity in Library.** It brings together progress, reading status, notes, quotes and reviews, with your pending offline entries first. (#199)
- **Jump to Hardcover’s newer page.** When Hardcover is at least five pages ahead, you can jump there instead of working out the page yourself. (#204)

## 🎨 Improved

- **Book details fit comfortably again.** The round actions and their labels are smaller, and Open / Find on device has its normal height. (#200)

## 🐛 Fixes

- **Starting a book is prompted reliably.** “Start reading this book?” now appears even while automatic progress tracking is off. (#205)
- **Offline Home stays accurate.** Currently Reading no longer disappears from Home when you are offline. (#203)
- **Paused books stay paused.** Reading while offline no longer leaves a book stuck in the wrong status after it is synced. (#206)
- **Offline reading keeps its real dates.** Pages read across several days are sent as dated daily progress entries, rather than all appearing on the reconnect day. (#207)

**Full changelog**: https://github.com/CaptainCamin/HardcoverSync.koplugin/compare/v2.3.1...v2.4.0-beta.1

# v2.3.1-beta.2 · 2026-10-22

## 🎨 Improved
- Show release notes in a fixed scrollable Markdown dialog (#198)

**Full changelog**: https://github.com/CaptainCamin/HardcoverSync.koplugin/compare/v2.3.0-beta.1...v2.3.1-beta.2

# v2.3.1-beta.1 · 2026-10-22

No pull requests were merged since the last release.

**Full changelog**: https://github.com/CaptainCamin/HardcoverSync.koplugin/compare/v2.3.0-beta.1...v2.3.1-beta.1

# v2.3.0-beta.1 · 2026-10-22

## ✨ New
- Add one-step stable releases with vX.Y.Z-stable (#185)
- Add the activity feed's data layer: status changes, notes, quotes and reviews (#186)
- Add an Activity tab to the Library (#188)
- Add a Journal button to the reader panel (#192)

## 🎨 Improved
- Book details: every action is a button (#194)
- Rework the reader panel with fixed actions and top controls (#196)

## Other
- Design docs for the e-reader target; dialogs 80% wide with side-by-side buttons (#182)
- Dialogs about 80% wide with side-by-side buttons (#187)
- Update the design docs to leave sheets as they are (#189)
- Keep Activity on the device and show what is waiting to send (#190)
- Let you edit and delete your notes, quotes and reviews from Activity (#193)
- Download new covers three at a time (#184)
- Balance the reader panel and restore readable book actions (#197)

**Full changelog**: https://github.com/CaptainCamin/HardcoverSync.koplugin/compare/v2.2.1-beta.1...v2.3.0-beta.1

# v2.2.1-beta.1 · 2026-10-22

## ✨ New
- Add the Paused reading status (#169)
- Correction dialog when a book is auto-linked (#175)
- Make the journal entry a themed form (#172)
- Settings gear in the reader panel (#168)
- Book search opens as a search bar in the top bar (#176)

## 🎨 Improved
- Show the books behind a book-count goal (#166)
- Move automatic tracking into the set-page dialog (#171)

## 🐛 Fixes
- Fix scrolling stalling mid-page (#177)

## 🛠 For developers
- Run the emulator at three screen sizes with layout checks (#178)
- Hold emulator fixtures to the shape of the real API (#173)
- Add Theme.* ratchet harness (#174)
- Verify journal, review and activity API against Hardcover (#170)

## Other
- Number picker: type the value, dotted buttons at the ends, hold to repeat (#179)
- Notes and quotes save offline and send later (#180)
- Group release notes by category automatically (#181)
- Write your review from the book details, offline too (#183)

**Full changelog**: https://github.com/CaptainCamin/HardcoverSync.koplugin/compare/v2.2.0...v2.2.1-beta.1

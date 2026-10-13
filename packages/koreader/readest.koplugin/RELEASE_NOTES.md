# v0.12.16 · 2026-10-13

## Release Highlights
* Text-to-Speech: Added Readest Voice premium read-aloud voices for Plus and Pro, you can now connect your own OpenAI-compatible voice service, and Edge voices work again
* Annotations: You can now handwrite and draw on your pages, and share passages as quote card images
* Library: Books now show their page count with a new Pages sort and filter that syncs across devices, and numbered titles sort in natural order
* Sync: Custom fonts download when you need them and can be removed from the cloud, custom theme edits now sync, and deleted books no longer come back
* Sync: KOReader progress sync and WebDAV sync are more reliable, and signing out only logs out the current device
* Reading: Very large or link-heavy chapters no longer freeze the reader, and fixed layout issues with headings, blockquotes, footnotes, and background textures
* Audiobooks: Audiobookshelf playback now works in the web app, chapters are detected more reliably, and you can pair audiobooks with books streamed from Audiobookshelf
* Linux: Fixed a freeze with two open windows, the main window reopens maximized, and Reveal in Folder works again
* PDF: You can hide page thumbnails in the PDF table of contents
* More: The share sheet opens again on iOS 16, with polish for the drawing tools, bottom sheets, and bookshelf header

## What's Changed
* chore(android): link WebView APK downloads in the outdated-WebView dialog by @chrox in https://github.com/readest/readest/pull/6649
* chore(deps): bump DeterminateSystems/determinate-nix-action from 3.22.5 to 3.23.0 in the github-actions group by @dependabot[bot] in https://github.com/readest/readest/pull/6679
* ui: place the "Log out" item in the second sub menu by @5w5 in https://github.com/readest/readest/pull/6645
* fix(reader): stop link-heavy single-file sections from hanging by @chrox in https://github.com/readest/readest/pull/6678
* refactor(ai): drop write-only indexingStates map in ragService by @irontaek in https://github.com/readest/readest/pull/6687
* Use music-metadata for audiobook chapters by @Borewit in https://github.com/readest/readest/pull/6686
* feat(reader): render huge sections in chunks by @chrox in https://github.com/readest/readest/pull/6680
* fix(koreader): reliable progress sync with hardened auth and error handling by @ivanovsergey93 in https://github.com/readest/readest/pull/6684
* fix(linux): stop the CEF focus loop that froze two-window sessions by @chrox in https://github.com/readest/readest/pull/6691
* fix(bookorbit): stamp the chapter on synced notes and bookmarks (#6655) by @bianyukun1213 in https://github.com/readest/readest/pull/6658
* fix(reader): read section text when a non-CJK lang hides CJK content by @k6G52m4Dz75W in https://github.com/readest/readest/pull/6672
* fix(library): stamp deletes so the sync merge cannot undelete the book, closes #6663 by @itsmunzir in https://github.com/readest/readest/pull/6682
* fix(opds): keep the feed scroll position after opening a book by @jadhavgaurav in https://github.com/readest/readest/pull/6683
* fix(library): use natural sorting for numbered titles by @kelvinalfaro in https://github.com/readest/readest/pull/6693
* fix(nix): refresh pnpmDeps hash for music-metadata by @chrox in https://github.com/readest/readest/pull/6688
* fix(kosync): keep the server path when proxying KOSync requests by @chrox in https://github.com/readest/readest/pull/6698
* fix(build): keep music-metadata out of the web server bundle by @chrox in https://github.com/readest/readest/pull/6699
* fix(reader): offer Pair Audiobook for EPUBs streamed from Audiobookshelf (#6695) by @ts-eva in https://github.com/readest/readest/pull/6697
* feat(reader): share passages as quote card images by @chrox in https://github.com/readest/readest/pull/6701
* fix(send): poll the inbox every 5 minutes instead of every minute by @chrox in https://github.com/readest/readest/pull/6706
* feat(tts): Readest Voice, premium read-aloud voices for Plus and Pro by @chrox in https://github.com/readest/readest/pull/6720
* fix(tts): connect Edge TTS to the new api.msedgeservices.com endpoint by @chrox in https://github.com/readest/readest/pull/6722
* fix(tts): count queued Readest Voice downloads against the listening quota by @chrox in https://github.com/readest/readest/pull/6721
* Support handwriting annotation by @esmaeelE in https://github.com/readest/readest/pull/6674
* perf(api): verify access tokens locally with getClaims by @chrox in https://github.com/readest/readest/pull/6724
* chore(agent): update agent memories by @chrox in https://github.com/readest/readest/pull/6725
* fix(auth): limit explicit logout to the current session by @hulkbig in https://github.com/readest/readest/pull/6709
* chore(auth): point clients at the Supabase project URL by @chrox in https://github.com/readest/readest/pull/6729
* feat(tts): move Readest Voice into its own service by @chrox in https://github.com/readest/readest/pull/6732
* fix(tts): make Readest Voice downloads responsive and tell users about quota by @chrox in https://github.com/readest/readest/pull/6736
* fix(tts): Readest Voice downloads that resume and follow the voice, and read aloud that survives a slow engine by @chrox in https://github.com/readest/readest/pull/6738
* fix(tts): resume queued downloads with the session's voice by @chrox in https://github.com/readest/readest/pull/6739
* fix(sync): decode XML entities in WebDAV PROPFIND hrefs by @smist37 in https://github.com/readest/readest/pull/6741
* fix(reader): keep the CJK widow/orphan lift alive under Use Book Layout by @k6G52m4Dz75W in https://github.com/readest/readest/pull/6711
* fix(rss): rebuild feed book TOC on every open instead of using the nav cache by @christi4nity in https://github.com/readest/readest/pull/6718
* fix(android): resolve Temp to the app cache so narration and file staging work on older Android by @ChristophWally in https://github.com/readest/readest/pull/6714
* fix(reader): honor justification overrides in footnote popups by @kelvinalfaro in https://github.com/readest/readest/pull/6708
* fix(audiobook): request Audiobookshelf audio with CORS on the web app (#6696) by @ts-eva in https://github.com/readest/readest/pull/6707
* docs(tts): drop the RunPod settings from the web env example by @chrox in https://github.com/readest/readest/pull/6744
* fix(library): retire re-keyed book hashes with a tombstone row (last import wins) by @k6G52m4Dz75W in https://github.com/readest/readest/pull/6703
* fix(tts): send Sec-MS-GEC v2 tokens to Edge TTS by @chrox in https://github.com/readest/readest/pull/6751
* feat(tts): custom OpenAI-compatible TTS services by @chrox in https://github.com/readest/readest/pull/6746
* fix(reader): suppress the webview context menu in the desktop app by @chrox in https://github.com/readest/readest/pull/6752
* fix(linux): make Reveal in Folder work again, closes #6660 by @chrox in https://github.com/readest/readest/pull/6754
* feat(reader): add a toggle to hide PDF page thumbnails in the TOC, closes #6650 by @chrox in https://github.com/readest/readest/pull/6756
* fix(linux): restore the maximized main window on launch, closes #6657 by @chrox in https://github.com/readest/readest/pull/6757
* fix(layout): give inline-only blockquotes the paragraph margin under Override Book Layout by @chrox in https://github.com/readest/readest/pull/6759
* fix(settings): reset the animation style to Push with Reset Behavior, closes #6753 by @chrox in https://github.com/readest/readest/pull/6760
* fix(tts): keep Read Aloud and its highlights intact after the sign-in detour by @chrox in https://github.com/readest/readest/pull/6758
* feat(sync): download synced custom fonts on demand, delete them from the cloud by @chrox in https://github.com/readest/readest/pull/6761
* fix(layout): let a more specific left-align beat a centered heading rule, closes #6723 by @chrox in https://github.com/readest/readest/pull/6763
* fix(metadata): allow 0 as a series index by @chrox in https://github.com/readest/readest/pull/6764
* fix(reader): keep the progress label in place while dragging the slider, closes #6646 by @chrox in https://github.com/readest/readest/pull/6766
* fix(style): keep Override Book Color working over a background texture, closes #6712 by @chrox in https://github.com/readest/readest/pull/6765
* fix(reader): measure image tap zones on its column in a two-page spread, closes #6745 by @chrox in https://github.com/readest/readest/pull/6769
* feat(calibre): add multi-language support by @GOSENGWONG in https://github.com/readest/readest/pull/6768
* fix(reader): keep the image long-press menu working on Android PDF pages by @chrox in https://github.com/readest/readest/pull/6771
* fix(ios): open the share sheet on iOS 16 for files with spaces or non-ASCII names, closes #6719 by @chrox in https://github.com/readest/readest/pull/6770
* build(android): ship per-ABI APKs (arm64, armv7, legacy) instead of universal by @chrox in https://github.com/readest/readest/pull/6772
* feat(library): count pages at import, add Pages sort and filter, closes #6662 by @chrox in https://github.com/readest/readest/pull/6774
* feat(sync): sync the import-time page count across devices by @chrox in https://github.com/readest/readest/pull/6775
* chore(agent): update agent memories by @chrox in https://github.com/readest/readest/pull/6776
* fix(sync): detect in-place custom theme changes by @anirudhqwerty in https://github.com/readest/readest/pull/6777
* fix: iOS reader polish for drawing dock, short sheets, bookshelf header and read aloud by @chrox in https://github.com/readest/readest/pull/6778
* release: version 0.12.16 by @chrox in https://github.com/readest/readest/pull/6779

## New Contributors
* @5w5 made their first contribution in https://github.com/readest/readest/pull/6645
* @irontaek made their first contribution in https://github.com/readest/readest/pull/6687
* @Borewit made their first contribution in https://github.com/readest/readest/pull/6686
* @ivanovsergey93 made their first contribution in https://github.com/readest/readest/pull/6684
* @bianyukun1213 made their first contribution in https://github.com/readest/readest/pull/6658
* @ts-eva made their first contribution in https://github.com/readest/readest/pull/6697
* @esmaeelE made their first contribution in https://github.com/readest/readest/pull/6674
* @smist37 made their first contribution in https://github.com/readest/readest/pull/6741
* @christi4nity made their first contribution in https://github.com/readest/readest/pull/6718
* @ChristophWally made their first contribution in https://github.com/readest/readest/pull/6714
* @GOSENGWONG made their first contribution in https://github.com/readest/readest/pull/6768
* @anirudhqwerty made their first contribution in https://github.com/readest/readest/pull/6777

**Full Changelog**: https://github.com/readest/readest/compare/v0.12.12...v0.12.16

# v0.12.12 · 2026-10-04

## Release Highlights
* Text-to-Speech: You can now listen sentence by sentence and loop a passage with A-B repeat, control playback from your desktop's Now Playing controls
* Reading: Added dialogue highlighting for quoted speech, a Column Gap setting for two-page spreads
* Sync: Added a Readest plugin for CrossPoint e-readers for reading progress sync
* Sync: You can now sync reading progress to Pagebound, sign in to Hardcover more easily, and note edits are no longer overwritten by older synced copies
* PDF: PDFs now blend smoothly with your reading theme with smart image inversion, show page thumbnails in the table of contents
* PDF: Highlighting and text selection on scanned PDFs is smoother and more accurate, and very large scanned pages no longer crash the reader on iOS
* Translation: You can now add your own translation providers with a reusable prompt library, look up words with an AI context dictionary
* Annotations: A global note now appears on every occurrence of its text, exports can include the sentence around each highlight
* Android: Added home screen widgets for your current book and bookshelf, automatic e-ink full refresh every few page turns
* More: Images now have a long-press and right-click menu to copy or save them, Windows shows PDF thumbnails in Explorer

## What's Changed
* fix(koplugin): fix sync on Android, library pull ANR, and Rescan library by @chrox in https://github.com/readest/readest/pull/6364
* chore(agent): add koreader-e2e skill for on-device plugin testing by @chrox in https://github.com/readest/readest/pull/6366
* fix(reader): fall back to saving a file when the gallery save fails by @chrox in https://github.com/readest/readest/pull/6367
* fix(windows): drop the broken native shadow on Windows 10 by @k6G52m4Dz75W in https://github.com/readest/readest/pull/6362
* perf(android): cut the arm64 apk from 90MB to 57MB by @chrox in https://github.com/readest/readest/pull/6368
* fix(build): repair the Docker and Nix builds after #6368 by @chrox in https://github.com/readest/readest/pull/6379
* fix(settings): reset update preferences with behavior settings by @hulkbig in https://github.com/readest/readest/pull/6369
* fix(android): open Readest from TTS media controls by @kelvinalfaro in https://github.com/readest/readest/pull/6370
* fix(reader): handle footnote links in paragraph mode by @hulkbig in https://github.com/readest/readest/pull/6365
* feat(reader): add dialogue highlighting for quoted speech by @WantenMN in https://github.com/readest/readest/pull/6376
* chore(deps): bump the github-actions group with 7 updates by @dependabot[bot] in https://github.com/readest/readest/pull/6387
* fix(annotator): clear the pre-drag range when a highlight is resized by @hulkbig in https://github.com/readest/readest/pull/6357
* fix(reader): keep the sidebar toggler in place when the sidebar opens by @chrox in https://github.com/readest/readest/pull/6435
* fix(payment): revoke one-time Stripe purchases on refund by @chrox in https://github.com/readest/readest/pull/6436
* fix(android): detect e-ink readers whose manufacturer prop reports the SoC vendor by @k6G52m4Dz75W in https://github.com/readest/readest/pull/6392
* refactor(settings): organize the font panel around the role each font plays by @k6G52m4Dz75W in https://github.com/readest/readest/pull/6325
* fix(settings): restore scroll position on reopen by @WantenMN in https://github.com/readest/readest/pull/6389
* fix(web): decode binary files read as text by @WestXu in https://github.com/readest/readest/pull/6402
* fix(library): skip copying a book file onto itself on import by @WestXu in https://github.com/readest/readest/pull/6403
* fix(backup): restore orphan books whose library row was deleted by @WestXu in https://github.com/readest/readest/pull/6405
* fix(sync): push existing notes on the first open of a book by @WestXu in https://github.com/readest/readest/pull/6404
* fix(reader): keep the footer clear of rounded screen corners on Android by @davidfvaquero in https://github.com/readest/readest/pull/6429
* perf(reader): parallelize the EPUB open path by @shiningsprk-arch in https://github.com/readest/readest/pull/6406
* fix(telemetry): stop PostHog traffic when the setting is off by @itsmunzir in https://github.com/readest/readest/pull/6434
* feat(widget): configurable Android bookshelf widget by @RedHatter in https://github.com/readest/readest/pull/6430
* fix(windows): draw the missing window frame on Windows 10 by @k6G52m4Dz75W in https://github.com/readest/readest/pull/6399
* fix(koplugin): prompt to log in again when the session has expired by @chrox in https://github.com/readest/readest/pull/6445
* fix(koplugin): avoid crash when synced position can't be resolved by @stantonb in https://github.com/readest/readest/pull/6441
* fix(sync): refuse Readest Cloud book uploads while Books sync is off by @chrox in https://github.com/readest/readest/pull/6446
* feat(widget): improve bookshelf widget configuration by @RedHatter in https://github.com/readest/readest/pull/6440
* feat(settings): reverse mouse wheel paging and hide e-ink bookshelf buttons by @chrox in https://github.com/readest/readest/pull/6448
* fix(reader): update chapter pages left on every page turn by @chrox in https://github.com/readest/readest/pull/6447
* fix(tts): let the play/pause media key resume TTS on desktop by @chrox in https://github.com/readest/readest/pull/6452
* fix(sync): stop creating OneDrive folders that Graph now rejects by @chrox in https://github.com/readest/readest/pull/6451
* fix(library): skip hidden subdirectories when scanning folders to import by @chrox in https://github.com/readest/readest/pull/6453
* docs(sync): make the write-parent precondition provider-neutral by @chrox in https://github.com/readest/readest/pull/6455
* fix(library): page the e-ink library with volume keys by @chrox in https://github.com/readest/readest/pull/6456
* feat(tts): native desktop Now Playing for macOS, Windows and Linux by @chrox in https://github.com/readest/readest/pull/6457
* fix(nix): add the desktop Now Playing crates to Cargo.cef.lock by @chrox in https://github.com/readest/readest/pull/6459
* fix(reader): turn the page when tapping a page-filling image by @chrox in https://github.com/readest/readest/pull/6458
* fix(library): skip per-book toasts for bulk downloads by @chrox in https://github.com/readest/readest/pull/6463
* feat(annotator): make keeping the selection after an instant lookup optional by @chrox in https://github.com/readest/readest/pull/6460
* fix(koplugin): remove sync response files left behind by exit-time syncs by @chrox in https://github.com/readest/readest/pull/6461
* fix(ios): resume audiobook natively after a CarPlay interruption ends by @chrox in https://github.com/readest/readest/pull/6462
* feat(reader): import MHTML web archives, closes #6413 by @chrox in https://github.com/readest/readest/pull/6464
* fix(annotator): close selection popup after choosing a highlight color by @kelvinalfaro in https://github.com/readest/readest/pull/6465
* fix(reader): close lookup popups when their selection is cleared by @chrox in https://github.com/readest/readest/pull/6467
* fix(sidebar): keep the annotations list still when the clicked note is visible by @chrox in https://github.com/readest/readest/pull/6468
* feat(tts): pause longer after questions, exclamations and ellipses, closes #6412 by @chrox in https://github.com/readest/readest/pull/6469
* fix(library): keep Date Read order when grouping, tagging or editing metadata by @chrox in https://github.com/readest/readest/pull/6470
* test(player): fix flaky podcast session-end tests by @chrox in https://github.com/readest/readest/pull/6472
* fix(reader): keep the footer clear of rounded screen corners on iPhone by @chrox in https://github.com/readest/readest/pull/6474
* fix(reader): hold the horizontal pan lock through momentum swipes on iOS by @chrox in https://github.com/readest/readest/pull/6475
* fix(reader): keep note editor and highlight toolbar open in footnote popups, closes #6395 by @chrox in https://github.com/readest/readest/pull/6477
* fix(transfer): allow uploads and downloads under a custom data location, closes #6383 by @chrox in https://github.com/readest/readest/pull/6478
* chore(agent): update agent memories by @chrox in https://github.com/readest/readest/pull/6479
* fix(library): center the empty library state again by @chrox in https://github.com/readest/readest/pull/6482
* ci(android): give the Android build step 90 minutes by @chrox in https://github.com/readest/readest/pull/6483
* fix: empty library state over a lingering search, and a dropped dictionary card tap by @chrox in https://github.com/readest/readest/pull/6485
* fix(backup): save iOS backups through the share sheet instead of hanging at 0%, closes #6375 by @chrox in https://github.com/readest/readest/pull/6486
* chore(linux): catch up the CEF runtime with upstream feat/cef, closes #6397 by @chrox in https://github.com/readest/readest/pull/6487
* fix(library): download selected Audiobookshelf items for offline from select mode by @chrox in https://github.com/readest/readest/pull/6489
* feat(backup): include reading statistics in library backups, closes #6488 by @chrox in https://github.com/readest/readest/pull/6490
* fix(reader): remove the line between zoomed images in Webtoon Mode, closes #6484 by @chrox in https://github.com/readest/readest/pull/6491
* test(paginator): rest before release so the drag test commits on distance alone by @chrox in https://github.com/readest/readest/pull/6493
* fix(desktop): open books in a new window after closing another reader, closes #6363 by @chrox in https://github.com/readest/readest/pull/6496
* fix(desktop): reopen the library when Readest is relaunched with only reader windows open, closes #6394 by @chrox in https://github.com/readest/readest/pull/6495
* fix(search): ignore soft hyphens when searching book text, closes #6384 by @chrox in https://github.com/readest/readest/pull/6494
* fix(ui): stop iOS 16 reloading to the library when a toggle or slider renders, closes #6355 by @chrox in https://github.com/readest/readest/pull/6497
* feat(annotations): optionally export the sentence around each highlight, closes #6352 by @chrox in https://github.com/readest/readest/pull/6498
* feat(tts): skip Hanja glosses after Hangul in Korean text by @chrox in https://github.com/readest/readest/pull/6500
* feat(annotator): show a global note on every occurrence of its text, closes #6186 by @chrox in https://github.com/readest/readest/pull/6501
* feat(settings): give Nearby BookDrop its own section in Integrations, closes #6360 by @chrox in https://github.com/readest/readest/pull/6499
* fix(ios): keep swipe brightness in sync with the system brightness, closes #6374 by @chrox in https://github.com/readest/readest/pull/6502
* feat(android): probe Hanvon eink service for full refresh by @k6G52m4Dz75W in https://github.com/readest/readest/pull/6505
* fix(reader): animate page turns for PDF and comics on Windows and Linux, closes #6380 by @chrox in https://github.com/readest/readest/pull/6506
* fix(reader): stop the sidebar-width flash on Windows and Linux page turns by @chrox in https://github.com/readest/readest/pull/6509
* feat(annotator): edit highlight ranges and notes inside footnote popups, closes #6504 by @chrox in https://github.com/readest/readest/pull/6510
* fix(reader): keep the selected word readable in dark mode, closes #6503 by @chrox in https://github.com/readest/readest/pull/6512
* fix(annotator): open imported highlights on tap, closes #6160 by @chrox in https://github.com/readest/readest/pull/6515
* fix(annotator): keep the highlight toolbar off the footnote popup, closes #6390 by @chrox in https://github.com/readest/readest/pull/6514
* feat(reader): show Duokan slim covers on tall mobile screens, closes #6513 by @chrox in https://github.com/readest/readest/pull/6516
* feat(reader): optionally mark italic text in dialogue highlighting, closes #6517 by @chrox in https://github.com/readest/readest/pull/6522
* fix(ios): keep chrome and page content clear of iPhone Duo's side status strip by @kad-air in https://github.com/readest/readest/pull/6312
* chore(deps): bump the github-actions group with 3 updates by @dependabot[bot] in https://github.com/readest/readest/pull/6523
* feat(layout): Column Gap setting for two-column spreads by @kad-air in https://github.com/readest/readest/pull/6507
* fix(ios): hide the status bar through the view controller for Xcode 27 builds by @kad-air in https://github.com/readest/readest/pull/6508
* fix(android): focus the WebView on cold start so the first page-turn key isn't lost by @RedHatter in https://github.com/readest/readest/pull/6519
* feat(widget): currently reading Android widget and widget options by @RedHatter in https://github.com/readest/readest/pull/6518
* fix(pdf): stop huge scanned pages crashing or blanking the reader on iOS, closes #6521 by @chrox in https://github.com/readest/readest/pull/6526
* feat(android): automatic e-ink full refresh every N page turns by @k6G52m4Dz75W in https://github.com/readest/readest/pull/6525
* feat(sync): sync reading progress to Pagebound, closes #6511 by @chrox in https://github.com/readest/readest/pull/6528
* fix(reader): show Hardcover status on the sync row and push on tap by @RedHatter in https://github.com/readest/readest/pull/6527
* feat(windows): PDF thumbnails and Explorer preview pane, closes #6524 by @chrox in https://github.com/readest/readest/pull/6533
* feat(dictionary): look up Wiktionary in the book language's own edition, closes #6529 by @chrox in https://github.com/readest/readest/pull/6534
* fix(settings): align the BookOrbit sync rows with the rest of the card by @chrox in https://github.com/readest/readest/pull/6535
* fix(library): erase cloud progress and notes when purging reading data, closes #6532 by @chrox in https://github.com/readest/readest/pull/6536
* fix(epub): show whole pages of comics with unsized SVG page images by @chrox in https://github.com/readest/readest/pull/6537
* fix(bookorbit): list unmatched books for linking when only progress or stats sync is on by @chrox in https://github.com/readest/readest/pull/6539
* fix(calibre): push custom columns in the shape bookshelf filters read by @chrox in https://github.com/readest/readest/pull/6538
* fix(reader): remove note bubbles when deleting highlights by @kelvinalfaro in https://github.com/readest/readest/pull/6545
* fix(windows): stop the main window from growing on every launch by @k6G52m4Dz75W in https://github.com/readest/readest/pull/6546
* feat(pdf): smooth theme colors and smart invert for PDFs by @chrox in https://github.com/readest/readest/pull/6550
* fix(notes): keep note edits from losing to the synced copy they change, closes #6544 by @chrox in https://github.com/readest/readest/pull/6551
* feat(crosspoint): Readest plugin for CrossPoint e-readers by @chrox in https://github.com/readest/readest/pull/6547
* chore(agent): update agent memories by @chrox in https://github.com/readest/readest/pull/6554
* feat(reader): turn PDF pages with the mouse wheel in Fit Width mode by @chrox in https://github.com/readest/readest/pull/6555
* feat(reader): show PDF page thumbnails in the TOC, closes #6177 by @chrox in https://github.com/readest/readest/pull/6553
* fix(reader): keep PDF selections from jumping across text gaps, closes #5599, closes #4945 by @chrox in https://github.com/readest/readest/pull/6559
* feat(crosspoint): web-only sign-in, in-app linking, and recently read books first by @chrox in https://github.com/readest/readest/pull/6561
* fix(reader): drop the horizontal scrollbar from fit-width PDFs by @chrox in https://github.com/readest/readest/pull/6560
* fix(reader): stop the page container's fade on e-ink panels by @k6G52m4Dz75W in https://github.com/readest/readest/pull/6565
* fix(audiobookshelf): fetch a synced audiobook's cover before shelving it by @chrox in https://github.com/readest/readest/pull/6564
* feat(reader): copy and save book images from one right-click menu by @chrox in https://github.com/readest/readest/pull/6567
* fix(reader): keep a selection from jumping next to a footnote marker, closes #6566 by @chrox in https://github.com/readest/readest/pull/6569
* fix(crosspoint): paint /link in the user's theme by @chrox in https://github.com/readest/readest/pull/6570
* fix(reader): stop annotation cards expanding while scrolling on iOS, closes #6568 by @chrox in https://github.com/readest/readest/pull/6571
* fix(utils): treat Korean as CJK in getLanguageInfo by @sx4im in https://github.com/readest/readest/pull/6572
* fix(deps): resolve open Dependabot alerts by @chrox in https://github.com/readest/readest/pull/6573
* fix(reader): set plain-text footnotes in the reader font by @kelvinalfaro in https://github.com/readest/readest/pull/6575
* fix(reader): keep a linked footnote's font in its popup, closes #3602 by @chrox in https://github.com/readest/readest/pull/6580
* docs(readme): serve the Ask DeepWiki badge from shields.io by @chrox in https://github.com/readest/readest/pull/6585
* fix(reader): smooth highlights on scanned PDFs and keep ones dragged past a page's end, closes #6578 by @chrox in https://github.com/readest/readest/pull/6581
* fix(reader): keep the e-ink battery percentage readable at any charge by @chrox in https://github.com/readest/readest/pull/6588
* feat(reader): edit a book's metadata from Book Details in the reader, closes #6584 by @chrox in https://github.com/readest/readest/pull/6587
* fix(reader): select and deselect in the clicked chapter at scroll-mode boundaries, closes #6583 by @chrox in https://github.com/readest/readest/pull/6591
* fix(reader): keep the dragged range when a PDF instant highlight runs past the page by @chrox in https://github.com/readest/readest/pull/6597
* fix(windows): stop the PDF preview pane from freezing Explorer, closes #6590 by @chrox in https://github.com/readest/readest/pull/6594
* feat(crosspoint): plugin updates, version display, and sync for optimized EPUBs by @chrox in https://github.com/readest/readest/pull/6592
* feat(translation): custom translation providers with a prompt library by @chrox in https://github.com/readest/readest/pull/6582
* fix(reader): remember where a locked, zoomed PDF page is panned across reopening by @chrox in https://github.com/readest/readest/pull/6595
* feat(shortcuts): bind several keys to one action, closes #6600 by @chrox in https://github.com/readest/readest/pull/6603
* feat(reader): open the image menu with a long press on iOS and Android, closes #6574 by @chrox in https://github.com/readest/readest/pull/6601
* fix(koplugin): stop BookDrop start errors popping up on every launch by @chrox in https://github.com/readest/readest/pull/6604
* feat(reader): show a PDF's header and footer only at the page's own edges, closes #6596 by @chrox in https://github.com/readest/readest/pull/6605
* fix(reader): keep pull-to-bookmark off the top screen edge, enable it on e-ink, and size the ribbon consistently, closes #6599 by @chrox in https://github.com/readest/readest/pull/6606
* fix(reader): return to the open book when leaving the account page, closes #6607 by @chrox in https://github.com/readest/readest/pull/6609
* fix(reader): reject backslash redirects and retry failed books on return by @chrox in https://github.com/readest/readest/pull/6610
* feat(dictionary): context dictionary, closes #5544 by @nphng15 in https://github.com/readest/readest/pull/5881
* fix(crosspoint): link an optimized copy to the book being read when duplicates tie by @chrox in https://github.com/readest/readest/pull/6614
* fix(sync): don't let a deleted copy's position pull a new copy forward by @chrox in https://github.com/readest/readest/pull/6615
* fix(reader): apply scroll overlap to fixed-layout books only; tidy the fixed-layout view menu by @chrox in https://github.com/readest/readest/pull/6621
* fix(windows): show the main window only after the themed page is painted by @k6G52m4Dz75W in https://github.com/readest/readest/pull/6611
* fix(library): carousel cover spine, Rename Group, Import Books placement, reader return transition by @chrox in https://github.com/readest/readest/pull/6624
* fix(library): keep nested groups when renaming a group by @chrox in https://github.com/readest/readest/pull/6625
* feat(library): badge the series index on covers inside a series group by @kelvinalfaro in https://github.com/readest/readest/pull/6579
* fix(reader): keep scrolled PDFs smooth on iOS: virtualize the strip, hide PDF chrome by layout by @chrox in https://github.com/readest/readest/pull/6626
* feat(tts): sentence-by-sentence mode and A-B repeat by @chrox in https://github.com/readest/readest/pull/6627
* feat(hardcover): sign in with OAuth using the device authorization flow by @RedHatter in https://github.com/readest/readest/pull/6612
* fix(hardcover): follow API rate limits and batch journal writes by @RedHatter in https://github.com/readest/readest/pull/6617
* fix(dictionary): lift dark text colors in dark mode by @itsmunzir in https://github.com/readest/readest/pull/6622
* fix(widget): keep E-ink reading widget text legible in dark mode by @chrox in https://github.com/readest/readest/pull/6628
* feat(library): hide the bookshelf page buttons by default on e-ink by @chrox in https://github.com/readest/readest/pull/6631
* fix(reader): save library progress before the app quits (#6623) by @chrox in https://github.com/readest/readest/pull/6633
* chore(agent): update agent memories by @chrox in https://github.com/readest/readest/pull/6634
* fix(import): pick the declared cover when <meta name="cover"> holds an href by @chrox in https://github.com/readest/readest/pull/6635
* feat(hardcover): use the account's default visibility for new journal entries by @RedHatter in https://github.com/readest/readest/pull/6638
* fix(opds): load plain-http covers natively on iOS/macOS (#6637) by @chrox in https://github.com/readest/readest/pull/6639
* fix(library): keep the bookshelf column count while dragging a file in by @chrox in https://github.com/readest/readest/pull/6640
* fix(library): search book contents only within the opened group by @chrox in https://github.com/readest/readest/pull/6641
* fix(library): keep the shelf scroll position after opening a book by @chrox in https://github.com/readest/readest/pull/6642
* release: version 0.12.12 by @chrox in https://github.com/readest/readest/pull/6644

## New Contributors
* @hulkbig made their first contribution in https://github.com/readest/readest/pull/6369
* @WestXu made their first contribution in https://github.com/readest/readest/pull/6402
* @davidfvaquero made their first contribution in https://github.com/readest/readest/pull/6429
* @shiningsprk-arch made their first contribution in https://github.com/readest/readest/pull/6406
* @itsmunzir made their first contribution in https://github.com/readest/readest/pull/6434
* @RedHatter made their first contribution in https://github.com/readest/readest/pull/6430
* @stantonb made their first contribution in https://github.com/readest/readest/pull/6441
* @sx4im made their first contribution in https://github.com/readest/readest/pull/6572
* @nphng15 made their first contribution in https://github.com/readest/readest/pull/5881

**Full Changelog**: https://github.com/readest/readest/compare/v0.12.10...v0.12.12

# v0.12.10 · 2026-09-21

## Release Highlights
* Library: You can now organize books into configurable bookshelves, tag books in bulk
* Audiobooks: You can download Audiobookshelf books for offline listening, stream audiobooks from OPDS catalogs and BookOrbit
* Reading: You can now open HTML files as books, and select, highlight, and look up text in Paragraph Mode
* Sync: Reading progress refreshes when you return to the app, WebDAV sync is more reliable, and Readwise exports now include bookmarks
* TTS: You can now browse and resume your books from Android Auto and pick up recent books from CarPlay
* PDF: Page-turn animations now work on PDFs, comics, and fixed-layout books, and wide comic pages get a spread of their own
* KOReader: Added background sync, group downloads, and more library controls, and highlights you delete stay deleted
* Dictionary: Pronunciations can play automatically on lookup, accented words are easier to find
* More: Backups are much faster and keep the screen awake, and fixed freezes on App launch and in image-heavy chapters

## What's Changed
* release: version 0.12.8 by @chrox in https://github.com/readest/readest/pull/6135
* fix(library): keep the context menu actions wired to their items by @chrox in https://github.com/readest/readest/pull/6143
* fix(reader): draw the selection toolbar above the footnote popup by @chrox in https://github.com/readest/readest/pull/6146
* fix(ci): bundle libxkbcommon-x11 in the CEF AppImage by @chrox in https://github.com/readest/readest/pull/6151
* fix(proofread): keep selection rules applied after a toggle, edit or reopen (#6148) by @chrox in https://github.com/readest/readest/pull/6152
* chore(deps): bump the github-actions group with 3 updates by @dependabot[bot] in https://github.com/readest/readest/pull/6166
* fix(txt): detect Chinese chapters numbered with 两 or uppercase numerals (#6172) by @chrox in https://github.com/readest/readest/pull/6181
* fix(annotator): keep a highlight's rounded caps on its own page, closes #6128 by @chrox in https://github.com/readest/readest/pull/6182
* feat(reader): hide the image viewer controls on tap by @chrox in https://github.com/readest/readest/pull/6183
* Fixed translation error by @tygoee in https://github.com/readest/readest/pull/6215
* fix(reader): keep sliders mirrored when a book turns the layout RTL by @jadhavgaurav in https://github.com/readest/readest/pull/6168
* docker: pull minio images from quay.io, Docker Hub removed them by @thietala in https://github.com/readest/readest/pull/6196
* fix(payment): resolve the user's plan across every billing provider by @chrox in https://github.com/readest/readest/pull/6228
* fix(reader): open image-heavy sections in paged mode without freezing by @chrox in https://github.com/readest/readest/pull/6229
* fix(linux): drop the WebKitGTK assumptions now that Linux is CEF only by @Berserker-GM in https://github.com/readest/readest/pull/6218
* chore(deps): bump the github-actions group with 5 updates by @dependabot[bot] in https://github.com/readest/readest/pull/6236
* ci(android): stop asking sdkmanager for the removed `tools` package by @chrox in https://github.com/readest/readest/pull/6238
* Fix page-turn direction fallback and add missing applyMarginAndGap for vertical layout by @JackyHe398 in https://github.com/readest/readest/pull/6197
* fix(opds): persist sync progress incrementally so a large first sync can converge by @raman325 in https://github.com/readest/readest/pull/6237
* fix(android): stop the app freezing at launch on a page load deadlock by @chrox in https://github.com/readest/readest/pull/6240
* test(paginator): wait for the scroll relocate in the scrolled cover test by @chrox in https://github.com/readest/readest/pull/6243
* chore(agent): update agent memories by @chrox in https://github.com/readest/readest/pull/6244
* fix(epub): play embedded media the OPF manifest never declares by @chrox in https://github.com/readest/readest/pull/6245
* feat(reader): animate page turns on PDF, CBZ and fixed-layout books by @chrox in https://github.com/readest/readest/pull/6246
* fix(tts): keep a non-English book on its own voice when the doc says en-US by @chrox in https://github.com/readest/readest/pull/6247
* fix(reader): select text on a long press near a link on Android (#6242) by @chrox in https://github.com/readest/readest/pull/6248
* fix(paginator): keep an RTL book's progression when a re-render lands mid-load by @chrox in https://github.com/readest/readest/pull/6249
* fix(reader): backward page curl on PDF/CBZ froze a few pixels in by @chrox in https://github.com/readest/readest/pull/6250
* feat(reader): animate Push on PDF, CBZ and fixed-layout books by @chrox in https://github.com/readest/readest/pull/6251
* fix(reader): keep a page-wide image inside its column in paginated mode by @chrox in https://github.com/readest/readest/pull/6252
* fix(macos): keep the traffic lights on the library page and stop them jumping on navigation by @chrox in https://github.com/readest/readest/pull/6253
* feat(reader): confirm before following external links by @chrox in https://github.com/readest/readest/pull/6254
* fix(ios): restore cross-page selection on iPadOS 27 by @chrox in https://github.com/readest/readest/pull/6255
* fix(reader): let the macOS annotation export save to disk (#6201) by @chrox in https://github.com/readest/readest/pull/6260
* feat(reader): select, highlight and look up text in Paragraph Mode by @chrox in https://github.com/readest/readest/pull/6258
* fix(ios): keep reader screen awake with native idle timer by @chrox in https://github.com/readest/readest/pull/6261
* fix(reader): restore tablet toolbar taps at fractional display density by @chrox in https://github.com/readest/readest/pull/6263
* feat(audiobookshelf): sync reading progress for ebook-only books (#6257) by @chrox in https://github.com/readest/readest/pull/6264
* feat(audiobookshelf): download books for offline use and import ABS zips from the web browser by @chrox in https://github.com/readest/readest/pull/6267
* fix(abs): stream audiobook tracks through a loopback media proxy so self-signed servers play (#6216) by @chrox in https://github.com/readest/readest/pull/6268
* fix(annotator): hand the selection back when the instant dictionary closes by @chrox in https://github.com/readest/readest/pull/6272
* perf(reader): split chapter loading to reduce swipe stalls by @chrox in https://github.com/readest/readest/pull/6266
* feat(reader): give each wide comic page a spread of its own (#6210) by @chrox in https://github.com/readest/readest/pull/6273
* fix(reader): preserve style tag attributes in the style transformer by @jadhavgaurav in https://github.com/readest/readest/pull/6270
* fix(nix): add imagesize to the CEF lockfile by @chrox in https://github.com/readest/readest/pull/6274
* feat(reader): cache wide comic pages and find them in streamed comics (#6210) by @chrox in https://github.com/readest/readest/pull/6276
* fix(bookdrop): only sound on a completed transfer, enable Nearby BookDrop by default by @chrox in https://github.com/readest/readest/pull/6277
* feat(reader): add pull-down bookmark gesture setting by @chrox in https://github.com/readest/readest/pull/6278
* fix(sentry,about): report the real WebView build via webview_version() by @k6G52m4Dz75W in https://github.com/readest/readest/pull/6275
* test(bookdrop): make the cue test independent of test order by @chrox in https://github.com/readest/readest/pull/6279
* feat(reader): import and render HTML files, closes #6198 by @chrox in https://github.com/readest/readest/pull/6281
* feat(dictionary): auto-play pronunciation on lookup by @chrox in https://github.com/readest/readest/pull/6280
* fix(nix): don't query wry's webview_version on Linux by @chrox in https://github.com/readest/readest/pull/6282
* feat(readwise): export bookmarks and their notes by @chrox in https://github.com/readest/readest/pull/6294
* fix(android): recognize iReader devices in e-ink detection by @k6G52m4Dz75W in https://github.com/readest/readest/pull/6293
* fix(backup): keep the screen awake and move bulk zip work to Rust, closes #6291 by @chrox in https://github.com/readest/readest/pull/6299
* fix(translate): remember source language per book by @chrox in https://github.com/readest/readest/pull/6300
* feat(wordlens): Traditional Chinese hints and an English→Arabic pack by @chrox in https://github.com/readest/readest/pull/6303
* fix(test): stop ResizeObserver notices flooding the browser-test log by @chrox in https://github.com/readest/readest/pull/6305
* fix(linux): explain missing X11 display on startup by @chrox in https://github.com/readest/readest/pull/6302
* feat(android): browse and resume books in Android Auto by @kelvinalfaro in https://github.com/readest/readest/pull/6285
* feat(opds): stream audiobooks from OPDS catalogs, with a BookOrbit connector (#6224) by @chrox in https://github.com/readest/readest/pull/6301
* fix(reader): keep highlight options inside the reading area by @chrox in https://github.com/readest/readest/pull/6306
* chore(agent): update agent memories by @chrox in https://github.com/readest/readest/pull/6309
* feat(audiobook): stream BookOrbit audio through the loopback media proxy (#6224) by @chrox in https://github.com/readest/readest/pull/6308
* fix(sync): retry failed WebDAV writes without advancing config state by @chrox in https://github.com/readest/readest/pull/6310
* fix(sync): preserve WebDAV errors and report incomplete syncs by @chrox in https://github.com/readest/readest/pull/6311
* fix(reader): prevent vertical toolbar swipes from paging Push books by @chrox in https://github.com/readest/readest/pull/6313
* fix(mobile): align reader menus and improve dialog dismissal by @chrox in https://github.com/readest/readest/pull/6314
* fix(translate): decode HTML entities in popup text by @chrox in https://github.com/readest/readest/pull/6317
* fix: correct remaining-time sorting and chapter estimates by @chrox in https://github.com/readest/readest/pull/6319
* fix(dictionary): normalize Unicode and fold Latin diacritics by @chrox in https://github.com/readest/readest/pull/6320
* feat(koreader): background sync, group downloads, and library controls by @chrox in https://github.com/readest/readest/pull/6321
* fix(koreader): keep synced highlight deletions from reappearing by @chrox in https://github.com/readest/readest/pull/6322
* fix: refresh sidebar note timestamps every minute by @kv-chiu in https://github.com/readest/readest/pull/6324
* feat(library): add configurable bookshelves by @chrox in https://github.com/readest/readest/pull/6329
* fix(library): improve e-ink pagination and bookshelf sync by @chrox in https://github.com/readest/readest/pull/6330
* fix(reader): keep note editors open until saving succeeds by @chrox in https://github.com/readest/readest/pull/6331
* fix(sync): refresh reading progress when the app resumes by @chrox in https://github.com/readest/readest/pull/6332
* fix(reader): read M4B chapters when moov comes after the audio (#6262) by @knigam in https://github.com/readest/readest/pull/6327
* feat(library): book tags in the list view and a Tag Books action by @chrox in https://github.com/readest/readest/pull/6334
* fix(ui): smooth bottom-sheet gestures and Settings scrolling by @chrox in https://github.com/readest/readest/pull/6335
* fix(library): prevent scrollbar initialization layout shift by @chrox in https://github.com/readest/readest/pull/6336
* chore(payments): end the Full Customization grace period for storage add-ons by @chrox in https://github.com/readest/readest/pull/6337
* fix(reader): size annotation toolbar to enabled actions by @chrox in https://github.com/readest/readest/pull/6338
* fix(payments): store Play cancellation time as a timestamp by @chrox in https://github.com/readest/readest/pull/6342
* feat(ios): add CarPlay recent books and fix scene handoff by @chrox in https://github.com/readest/readest/pull/6339
* fix: harden ebook content and proxy trust boundaries by @chrox in https://github.com/readest/readest/pull/6343
* fix(tts): bound startup probes and filter Apple system voices by @chrox in https://github.com/readest/readest/pull/6345
* fix(android-auto): play cold EPUBs in media service by @kelvinalfaro in https://github.com/readest/readest/pull/6341
* fix: align player headers and restore mobile view menu dismissal by @chrox in https://github.com/readest/readest/pull/6346
* chore(agent): update agent memories by @chrox in https://github.com/readest/readest/pull/6348
* release: version 0.12.10 by @chrox in https://github.com/readest/readest/pull/6349

## New Contributors
* @tygoee made their first contribution in https://github.com/readest/readest/pull/6215
* @thietala made their first contribution in https://github.com/readest/readest/pull/6196
* @Berserker-GM made their first contribution in https://github.com/readest/readest/pull/6218
* @JackyHe398 made their first contribution in https://github.com/readest/readest/pull/6197
* @raman325 made their first contribution in https://github.com/readest/readest/pull/6237
* @kelvinalfaro made their first contribution in https://github.com/readest/readest/pull/6285
* @kv-chiu made their first contribution in https://github.com/readest/readest/pull/6324
* @knigam made their first contribution in https://github.com/readest/readest/pull/6327

**Full Changelog**: https://github.com/readest/readest/compare/v0.12.8...v0.12.10

# v0.12.8 · 2026-09-07

## Release Highlights
* Reading: Customize the information shown in headers and footers, resize text with zoom shortcuts
* Sync: You can choose whether to use Readest Cloud before signing in, and recover missing covers during sync
* Annotations: You can now import highlights, bookmarks, and reading progress from ReadEra, and sync your notes and highlights to Notion
* Audiobooks: You can now stream ebook-only titles from Audiobookshelf
* Text-to-Speech: use Apple Enhanced and Premium voices on the web, and optionally skip parenthetical readings in Japanese books
* Web Imports: You can now clip signed-in pages and import web novels that require an account, with more reliable text decoding
* Styling: Your library and reader can now use separate theme modes and colors, and e-ink mode is available on every platform
* PDF: You can lock horizontal panning while zoomed, highlights stay visible in dark mode, and PDFs work on older devices
* Dictionary: Dictionary entries can now play embedded audio, jump to parts of speech, and enlarge images
* Sharing: Nearby BookDrop now offers easier pairing, transfer sounds, and more reliable device discovery and reconnection

## What's Changed
* fix(ios): stop web-browser downloads from deadlocking the main thread by @chrox in https://github.com/readest/readest/pull/5947
* feat(settings): show which scope the Settings dialog writes by @bmfrosty in https://github.com/readest/readest/pull/5933
* feat(ui): separate theme mode and color for the library and the reader by @chrox in https://github.com/readest/readest/pull/5948
* fix(reader): stop a mid-touch text selection from hijacking the brightness swipe (#5939) by @chrox in https://github.com/readest/readest/pull/5958
* feat(reader): customizable header and footer style (#5938) by @chrox in https://github.com/readest/readest/pull/5960
* fix(reader): contain Notebook text while typing (#5956) by @chrox in https://github.com/readest/readest/pull/5962
* fix(library): update the existing book when an updated EPUB is re-imported (#5959) by @chrox in https://github.com/readest/readest/pull/5961
* feat(grouping): Adding existing status as Grouping by @rigen1048 in https://github.com/readest/readest/pull/5935
* fix(reader): keep TTS chapter indicators synced (#5953) by @chrox in https://github.com/readest/readest/pull/5968
* fix(reader): correct PDF reference totals and slider endpoint (#5951) by @chrox in https://github.com/readest/readest/pull/5969
* feat(notion): sync notes and highlights to Notion by @PaleVerge in https://github.com/readest/readest/pull/5949
* fix(reader): stabilize Hardcover Sync submenu sizing by @chrox in https://github.com/readest/readest/pull/5978
* fix(reader): shrink hidden Android navigation controls (#5966) by @chrox in https://github.com/readest/readest/pull/5974
* fix(markdown): support tab-indented footnotes by @chrox in https://github.com/readest/readest/pull/5975
* chore: update agent memories and tidy library styles by @chrox in https://github.com/readest/readest/pull/5985
* feat(payments): yearly subscription plans and a modernized store front by @chrox in https://github.com/readest/readest/pull/5989
* feat(payments): record Apple one-time purchases from ONE_TIME_CHARGE by @chrox in https://github.com/readest/readest/pull/5993
* fix(payments): acknowledge Apple notifications that carry no transaction by @chrox in https://github.com/readest/readest/pull/5994
* feat(payments): separate storage and customization entitlements, unlock all when self-hosted by @chrox in https://github.com/readest/readest/pull/5996
* fix(payments): align the plan panels and stop the header eating clicks by @chrox in https://github.com/readest/readest/pull/6000
* READ-9: shrink hidden Android navigation buttons to 8px by @chrox in https://github.com/readest/readest/pull/6001
* fix(bookorbit): cap page-stat uploads at server limits by @chrox in https://github.com/readest/readest/pull/6002
* fix(reader): stop the note popup growing scrollbars of its own by @chrox in https://github.com/readest/readest/pull/6006
* fix(opds): import the publication date, not the calibre added-date by @chrox in https://github.com/readest/readest/pull/6008
* fix(kosync): resolve KOReader XPointers in their own DocFragment by @chrox in https://github.com/readest/readest/pull/6014
* fix(reader): write a new note on the selection, not in the sidebar by @chrox in https://github.com/readest/readest/pull/6013
* fix(pdf): render documents on older WebKit by @chrox in https://github.com/readest/readest/pull/6019
* fix(dict): play MDD audio, jump to POS sections, zoom entry images by @chrox in https://github.com/readest/readest/pull/6021
* fix(reader): keep lookup surfaces open when native handles are suppressed by @chrox in https://github.com/readest/readest/pull/6022
* feat(bookdrop): AirDrop-style Nearby BookDrop with pairing, sounds, and resilient discovery by @chrox in https://github.com/readest/readest/pull/6023
* feat(settings): add a Gamepad Support toggle by @chrox in https://github.com/readest/readest/pull/6027
* feat(pdf): add a Lock Horizontal Panning toggle for zoomed pages by @chrox in https://github.com/readest/readest/pull/6030
* feat(annotator): show highlight options immediately when highlight tool is present by @chrox in https://github.com/readest/readest/pull/6031
* fix(sync): fit OAuth tokens in Windows keychain by @chrox in https://github.com/readest/readest/pull/6033
* feat(annotator): import highlights, bookmarks and progress from ReadEra by @chrox in https://github.com/readest/readest/pull/6032
* feat(sync): add a manual sync option for BookOrbit (#6029) by @chrox in https://github.com/readest/readest/pull/6034
* fix(reader): keep mobile header tools stationary by @chrox in https://github.com/readest/readest/pull/6035
* fix(annotator): keep the annotation toolbar below the range handles by @chrox in https://github.com/readest/readest/pull/6036
* chore: update agent memories by @chrox in https://github.com/readest/readest/pull/6037
* fix(reader): restore XHTML namespaces so book CSS selectors match by @chrox in https://github.com/readest/readest/pull/6040
* fix(reader): draw scripted canvases and keep them inside their column by @chrox in https://github.com/readest/readest/pull/6042
* feat(sync): choose Readest Cloud before sign-in starts syncing by @chrox in https://github.com/readest/readest/pull/6045
* chore(deps): bump the github-actions group with 5 updates by @dependabot[bot] in https://github.com/readest/readest/pull/6039
* fix(ui): preserve mobile toast gutters by @chrox in https://github.com/readest/readest/pull/6046
* fix(bookdrop): recover the iOS service after suspension and keep peer presence honest by @chrox in https://github.com/readest/readest/pull/6049
* fix(koplugin): honour BookDrop goodbyes and un-dangle the localsend pin by @chrox in https://github.com/readest/readest/pull/6050
* fix(novel): decode imported pages with the charset they declare by @chrox in https://github.com/readest/readest/pull/6052
* fix(audiobookshelf): add web CORS setup hint by @chrox in https://github.com/readest/readest/pull/6053
* fix(reader): restore EPUB namespace in section fragments by @chrox in https://github.com/readest/readest/pull/6054
* fix(reader): stop the default font from overriding a book's embedded fonts by @k6G52m4Dz75W in https://github.com/readest/readest/pull/6047
* fix(reader): make the reading ruler legible on e-ink by @chrox in https://github.com/readest/readest/pull/6055
* feat(tts): skip inline parenthetical readings by @chrox in https://github.com/readest/readest/pull/6057
* fix(tts): stop Android narration rewinding when the block cursor stalls by @chrox in https://github.com/readest/readest/pull/6058
* feat(audiobookshelf): stream ebook-only books by @chrox in https://github.com/readest/readest/pull/6056
* fix(annotator): stop PDF selections opening the translator popup by @chrox in https://github.com/readest/readest/pull/6063
* chore(agent): update agent memories by @chrox in https://github.com/readest/readest/pull/6064
* fix: resolve dependency and code-scanning alerts by @chrox in https://github.com/readest/readest/pull/6065
* fix(annotator): keep PDF highlights visible in dark mode by @chrox in https://github.com/readest/readest/pull/6066
* feat(reader): zoom shortcuts adjust font size in reflowable books, closes #5694 by @chrox in https://github.com/readest/readest/pull/6067
* fix(annotator): anchor the selection toolbar to the book cell by @chrox in https://github.com/readest/readest/pull/6068
* fix: own route transitions and scope Yandex cancellation by @chrox in https://github.com/readest/readest/pull/6069
* fix: guard reader reloads, search views, and sentence navigation by @chrox in https://github.com/readest/readest/pull/6070
* fix: await PDF destinations for TTS download chapters by @chrox in https://github.com/readest/readest/pull/6072
* fix: skip desktop fullscreen commands on mobile by @chrox in https://github.com/readest/readest/pull/6073
* fix(tts): read aloud only the selection on Ctrl/Cmd+R by @chrox in https://github.com/readest/readest/pull/6076
* fix(tts): stop a redundant PDF render detaching the ranges TTS reads by @chrox in https://github.com/readest/readest/pull/6075
* fix: ignore incomplete reader relocation events after close by @chrox in https://github.com/readest/readest/pull/6077
* feat(linux): ship Readest on the tauri CEF runtime by @chrox in https://github.com/readest/readest/pull/6074
* fix(linux): catch the CEF stack up with upstream feat/cef by @chrox in https://github.com/readest/readest/pull/6080
* fix: serialize TTS cache compaction before shutdown by @chrox in https://github.com/readest/readest/pull/6078
* chore: bump tauri to version 2.11.5 by @chrox in https://github.com/readest/readest/pull/6081
* feat(nix): build the Linux package on the CEF runtime by @chrox in https://github.com/readest/readest/pull/6083
* fix(nix): let the linker resolve libcef.so's own dependencies by @chrox in https://github.com/readest/readest/pull/6084
* chore: remove the packages/tao submodule by @chrox in https://github.com/readest/readest/pull/6085
* feat(linux): debug the CEF build over CDP, and three fixes it found by @chrox in https://github.com/readest/readest/pull/6087
* fix: continue library sync after cover download failures by @chrox in https://github.com/readest/readest/pull/6086
* fix(epub): match `[xml|lang]` and `:lang()` on `xml:lang` attributes by @chrox in https://github.com/readest/readest/pull/6090
* feat(ui): dismiss bottom sheets by swiping down from anywhere by @chrox in https://github.com/readest/readest/pull/6097
* fix(tts): allow Apple Enhanced and Premium Web TTS voices by @chrox in https://github.com/readest/readest/pull/6099
* fix(docker): unbreak large uploads and self-hosted cloud sync by @chrox in https://github.com/readest/readest/pull/6100
* fix(ci): bundle the NSS modules the CEF AppImage dlopens by @chrox in https://github.com/readest/readest/pull/6101
* Fix Wayland WebKitGTK window sizing bug on non-CEF Linux builds by @Frebbers in https://github.com/readest/readest/pull/6098
* fix(reader): never let the hidden nav buttons take taps by @chrox in https://github.com/readest/readest/pull/6102
* fix(ui): pad the plans section so its buttons align on mobile by @chrox in https://github.com/readest/readest/pull/6103
* feat(reader): hinge the two-column Page Curl at the spine by @kad-air in https://github.com/readest/readest/pull/6107
* fix(ci): bundle the audio libraries the CEF AppImage dlopens by @chrox in https://github.com/readest/readest/pull/6108
* fix(test): keep the curl leaf in flight until the incoming bitmap lands by @chrox in https://github.com/readest/readest/pull/6114
* feat(ui): remove e-ink mode checks for all devices and platforms by @54wedge in https://github.com/readest/readest/pull/6113
* ci: manual Linux AppImage build for validating bundler changes by @chrox in https://github.com/readest/readest/pull/6115
* feat: unify web imports with signed-in page clipping by @chrox in https://github.com/readest/readest/pull/6117
* feat(proofread): allow tts rules to be created in proofread management panel by @54wedge in https://github.com/readest/readest/pull/6109
* fix(deeplink): consume the launch URL once per app run by @chrox in https://github.com/readest/readest/pull/6111
* fix(tts): keep mini player above navigation panels by @chrox in https://github.com/readest/readest/pull/6118
* fix(sync): repair missing local covers from the file-sync remote by @jadhavgaurav in https://github.com/readest/readest/pull/6116
* compat(image): exclude some images in gallery view by @54wedge in https://github.com/readest/readest/pull/6120
* chore(scripts): account inspector and merge scripts for support tickets by @chrox in https://github.com/readest/readest/pull/6121
* feat: support authenticated web novel imports by @chrox in https://github.com/readest/readest/pull/6119
* fix(sync): closing unclosed void tags before XML re-parsing, closes #5271 by @chrox in https://github.com/readest/readest/pull/6122
* fix(ci): use CEF bundler with deployment array quoting fix by @chrox in https://github.com/readest/readest/pull/6125
* fix(nix): sync CEF dependencies for offline builds by @chrox in https://github.com/readest/readest/pull/6126
* release: version 0.12.8 by @chrox in https://github.com/readest/readest/pull/6127
* fix(reader): sync reading progress on a first open in scrolled mode by @chrox in https://github.com/readest/readest/pull/6130
* fix(android): follow system theme in reading widget by @chrox in https://github.com/readest/readest/pull/6131
* fix(abs): refresh cached token for streaming file access by @chrox in https://github.com/readest/readest/pull/6132
* i18n: update translations by @chrox in https://github.com/readest/readest/pull/6134

## New Contributors
* @bmfrosty made their first contribution in https://github.com/readest/readest/pull/5933
* @rigen1048 made their first contribution in https://github.com/readest/readest/pull/5935
* @PaleVerge made their first contribution in https://github.com/readest/readest/pull/5949
* @k6G52m4Dz75W made their first contribution in https://github.com/readest/readest/pull/6047
* @Frebbers made their first contribution in https://github.com/readest/readest/pull/6098
* @kad-air made their first contribution in https://github.com/readest/readest/pull/6107

**Full Changelog**: https://github.com/readest/readest/compare/v0.12.6...v0.12.8

# v0.12.6 · 2026-08-28

## Release Highlights
* Audiobooks: Added Audiobookshelf support for streaming audiobooks and podcasts, and you can now pair an audiobook with its ebook to read along as it plays
* Text-to-Speech: Added a lyric-style view that shows the sentences around the one being read, plus per-book offline voice downloads and steadier pauses between sentences
* Library: You can now browse the web inside Readest to add books, choose which chapters to import from a web novel, hide covers for privacy, and watch download progress right on the shelf
* Sharing: Added Nearby BookDrop to send and receive books between nearby devices over your local network, including KOReader devices
* Reading: Added customizable keyboard and mouse shortcuts, Yomitan dictionary support, a full-screen book cover view, and right-to-left page order for comics and fixed-layout books
* Reading: The Notebook is now a full writing workspace, where your notes save as you type, sync across devices, and link back to the passage they came from
* Footnotes: Footnote popups no longer get cut off, let you select and look up text, and can jump straight to the note's place in the book
* PDF: You can now select text across page boundaries, copy paragraphs without broken line breaks, and see the printed page numbers as reference pages
* Sync: Your book groups and shelves now sync, file sync between devices settles reliably, highlights you delete in KOReader come across, and your progress survives an OPDS re-download
* More: Fixed crashes on launch, garbled AZW3 books, the reading position drifting after rotating the screen, and unreadable highlights on e-ink screens

## What's Changed
* fix(ios): App Review launch crash, CarPlay crash on connect, and main thread hangs by @chrox in https://github.com/readest/readest/pull/5590
* fix(opds): make the title bar draggable in the online library view by @chrox in https://github.com/readest/readest/pull/5592
* fix(opds): filter incompatible download formats and offer one-click EPUB by @chrox in https://github.com/readest/readest/pull/5593
* fix(sync): drop the Origin header from OAuth token requests by @chrox in https://github.com/readest/readest/pull/5604
* fix(android): stop claiming APKs and other downloads as openable books by @chrox in https://github.com/readest/readest/pull/5610
* feat(localsend): send and receive books over the local network by @chrox in https://github.com/readest/readest/pull/5611
* fix(library): release TXT sources and chapter HTML during import by @ChuwuYo in https://github.com/readest/readest/pull/5607
* fix(library): checkpoint, serialize, and pool folder imports by @chrox in https://github.com/readest/readest/pull/5615
* fix(translation): gate Enable Translation on book availability by @chrox in https://github.com/readest/readest/pull/5617
* docs(readme): restore the Sponsors / TestMu AI section by @chrox in https://github.com/readest/readest/pull/5619
* fix(translate): send Bing language codes in the Azure provider by @chrox in https://github.com/readest/readest/pull/5620
* fix(library): stop a long press from selecting and then deselecting a book by @chrox in https://github.com/readest/readest/pull/5621
* fix(ci): stop cargo pulling the flutter SDK for the localsend dep by @chrox in https://github.com/readest/readest/pull/5622
* fix(reader): isolate the book cell to drop the Linux black corner by @PolybiusPro in https://github.com/readest/readest/pull/5618
* fix(popup): stop mounting the filtered pointer triangle at rest by @chrox in https://github.com/readest/readest/pull/5628
* fix(localsend): let Readest devices discover each other by @chrox in https://github.com/readest/readest/pull/5626
* fix(sync): recover KOReader progress when a chapter is not well-formed XML by @chrox in https://github.com/readest/readest/pull/5630
* fix(ci): gate build_tauri_app on tauri paths and give webdriver its own timeout by @chrox in https://github.com/readest/readest/pull/5644
* feat(ci): Added new step to release workflow to send release notes to a Discord channel by @sloaner in https://github.com/readest/readest/pull/5637
* fix(reader): commit settled image zoom into the layout size, closes #5633 by @chrox in https://github.com/readest/readest/pull/5639
* fix(novel): retry transient fetch failures and backfill work metadata by @chrox in https://github.com/readest/readest/pull/5650
* fix(markdown): title imported books after the file, not the first heading by @chrox in https://github.com/readest/readest/pull/5653
* fix(sanitizer): render Persian/Arabic half-space by converting misused RLM to ZWNJ by @shahram7 in https://github.com/readest/readest/pull/5651
* fix(reader): stop iOS 16 WebContent crash when opening a book by @chrox in https://github.com/readest/readest/pull/5654
* feat(reader): flash the target of in-page footnote jumps, closes #5647 by @chrox in https://github.com/readest/readest/pull/5655
* fix(koplugin): extract self-update with ffi/archiver on KOReader 2026.07+ by @chrox in https://github.com/readest/readest/pull/5656
* fix(reader): render fixed-layout pages as authored in dark mode, closes #5649 by @chrox in https://github.com/readest/readest/pull/5657
* fix(reader): disable text autosizing in fixed-layout books, closes #5641 by @chrox in https://github.com/readest/readest/pull/5659
* ci: raise nightly and release build timeouts to 90 minutes by @chrox in https://github.com/readest/readest/pull/5664
* fix(opds): stop auto-downloaded books from vanishing on restart by @chrox in https://github.com/readest/readest/pull/5665
* fix(iap): re-verify restored iOS one-time purchases with the server by @chrox in https://github.com/readest/readest/pull/5669
* chore(deps): bump the github-actions group with 6 updates by @dependabot[bot] in https://github.com/readest/readest/pull/5668
* fix(ui): size the alert surface off its container, not its content by @WantenMN in https://github.com/readest/readest/pull/5662
* fix(koplugin): push reading stats in bounded chunks, closes #5666 by @chrox in https://github.com/readest/readest/pull/5670
* feat(reader): jump to the start or end of the book with Home/End by @chrox in https://github.com/readest/readest/pull/5673
* fix(sync): never show a future Last Synced time from a clock-skewed peer by @chrox in https://github.com/readest/readest/pull/5674
* fix(reader): update progress during Auto Scroll and put slider overlay values on top by @chrox in https://github.com/readest/readest/pull/5676
* fix(reader): reach the last page of the book on iOS by @chrox in https://github.com/readest/readest/pull/5678
* feat(reader): scroll Auto Scroll smoothly at low speeds by @chrox in https://github.com/readest/readest/pull/5679
* chore: update agent memories by @chrox in https://github.com/readest/readest/pull/5682
* fix(library): allow unchecking Read books in place for registered folders, closes #5680 by @chrox in https://github.com/readest/readest/pull/5685
* fix(reader): keep table label columns from collapsing by @chrox in https://github.com/readest/readest/pull/5686
* feat(tts): scroll to the current chapter when opening Offline Audio by @gfreitash in https://github.com/readest/readest/pull/5684
* feat(koplugin): LocalSend receive and send for KOReader devices by @chrox in https://github.com/readest/readest/pull/5687
* fix(sync): create the replica bundle dir before downloading, closes #5675 by @chrox in https://github.com/readest/readest/pull/5700
* chore(koplugin): build nightly plugin zip and default to device targets by @chrox in https://github.com/readest/readest/pull/5699
* feat(sync): add cloud shelves and safe provider deletion by @chrox in https://github.com/readest/readest/pull/5701
* fix(android): gate gamepad polling on controller connection by @chrox in https://github.com/readest/readest/pull/5702
* fix(dictionary): recover StarDict searches after an empty result by @chrox in https://github.com/readest/readest/pull/5705
* feat(tts): symmetric minimal mini-player with centered play button by @chrox in https://github.com/readest/readest/pull/5707
* fix(reader): remove header controls duplicated by the mobile footer bar by @chrox in https://github.com/readest/readest/pull/5708
* feat(sync): optional document metadata on KOSync progress uploads by @chrisbutler in https://github.com/readest/readest/pull/5704
* feat(reader): resume Auto Scroll when reopening a book by @chrox in https://github.com/readest/readest/pull/5710
* fix(reader): support page turner key combinations by @chrox in https://github.com/readest/readest/pull/5709
* feat(reader): right-to-left page order for fixed-layout books by @chrox in https://github.com/readest/readest/pull/5712
* fix(reader): avoid wide word gaps from authored text-wrap pretty, closes #5582 by @chrox in https://github.com/readest/readest/pull/5718
* fix(reader): restore scrolled PDF highlights by @chrox in https://github.com/readest/readest/pull/5719
* fix(sync): remove the mixed-fleet info toast, closes #5720 by @chrox in https://github.com/readest/readest/pull/5726
* fix(sync): sync the reference page count and stop import wiping configs, closes #5716 by @chrox in https://github.com/readest/readest/pull/5727
* fix(reader): highlight search results visible across chapter boundary by @WantenMN in https://github.com/readest/readest/pull/5725
* fix(reader): drop the 500-result cap from in-book search by @chrox in https://github.com/readest/readest/pull/5728
* fix(annotator): drop the selection when the instant dictionary opens, closes #5585 by @chrox in https://github.com/readest/readest/pull/5730
* fix(reader): neutralize fixed backgrounds and drop negative margins by @chrox in https://github.com/readest/readest/pull/5729
* fix(library): optimize bookshelf covers in background, closes #5632 by @chrox in https://github.com/readest/readest/pull/5731
* fix(eink): make e-ink highlights and chips visible, closes #5667 by @chrox in https://github.com/readest/readest/pull/5735
* feat(wordlens): add the en-vi gloss pack, sync incrementally by @chrox in https://github.com/readest/readest/pull/5737
* feat(wordlens): add the en-hu gloss pack by @chrox in https://github.com/readest/readest/pull/5738
* fix(wordlens): key the manifest diff on pack routing fields too by @chrox in https://github.com/readest/readest/pull/5739
* chore: update agent memories by @chrox in https://github.com/readest/readest/pull/5740
* feat(library): add hide-covers privacy option for the bookshelf by @WantenMN in https://github.com/readest/readest/pull/5733
* feat(tts): queue chapter downloads with per-book persistence by @gfreitash in https://github.com/readest/readest/pull/5690
* feat(library): show download progress overlay on book covers by @WantenMN in https://github.com/readest/readest/pull/5736
* feat(annotator): support text selection tools in footnote popups by @chrox in https://github.com/readest/readest/pull/5744
* feat(reader): pair local audiobooks with ebooks by @chrox in https://github.com/readest/readest/pull/5754
* fix(tts): make sentence and paragraph pauses consistent by @chrox in https://github.com/readest/readest/pull/5753
* fix(reader): keep chapter images openable after repeated footnote popups by @chrox in https://github.com/readest/readest/pull/5756
* docs: add contributor code of conduct by @chrox in https://github.com/readest/readest/pull/5758
* fix(opds): honor the Manage Sync Books toggle for automatic cloud uploads by @chrox in https://github.com/readest/readest/pull/5759
* feat(opds): confirm auto-download toggles and allow catalog reordering by @chrox in https://github.com/readest/readest/pull/5760
* feat(i18n): add Georgian translations by @chrox in https://github.com/readest/readest/pull/5763
* fix(cbz): order split chapter folders base-first by @chrox in https://github.com/readest/readest/pull/5762
* fix(opds): drop the webview Origin header on native requests by @NoaHimesaka1873 in https://github.com/readest/readest/pull/5765
* feat(dictionaries): add bundled plugin and Yomitan support by @chrox in https://github.com/readest/readest/pull/5764
* feat: package for nix by @dastarruer in https://github.com/readest/readest/pull/5605
* fix(reader): translate iframe text without duplicating TTS by @Columpio in https://github.com/readest/readest/pull/5772
* fix(tts): allow chapters sharing sentences with earlier packs to download by @gfreitash in https://github.com/readest/readest/pull/5768
* fix(deps): resolve open Dependabot alerts by @chrox in https://github.com/readest/readest/pull/5778
* fix(nix): update pnpmDeps hash and verify dep hashes on PRs by @chrox in https://github.com/readest/readest/pull/5779
* fix(library): recover from a failed startup instead of rendering a blank window by @chrox in https://github.com/readest/readest/pull/5789
* chore(deps): bump the github-actions group with 7 updates by @dependabot[bot] in https://github.com/readest/readest/pull/5796
* docs: use git input instead of github input by @dastarruer in https://github.com/readest/readest/pull/5791
* feat: Audiobookshelf integration with audiobook streaming and podcasts by @chrox in https://github.com/readest/readest/pull/5801
* fix(reader): extend pull-to-bookmark to fixed layout and yield to late selection by @chrox in https://github.com/readest/readest/pull/5802
* feat(reader): expose data-eink on the book document for per-device custom CSS by @chrox in https://github.com/readest/readest/pull/5803
* fix(android): keep the reader alive when a Bluetooth controller connects (#5799) by @chrox in https://github.com/readest/readest/pull/5804
* fix(reader): render markdown in the note bubble popup, closes #5785 by @chrox in https://github.com/readest/readest/pull/5805
* feat(reader): add inline note editing by @libbybar in https://github.com/readest/readest/pull/5780
* feat(reader): expose book title and series as data attributes for custom UI CSS, closes #5776 by @chrox in https://github.com/readest/readest/pull/5806
* feat(reader): show PDF page labels as reference pages, closes #5822 by @chrox in https://github.com/readest/readest/pull/5824
* feat(rsvp): add exact WPM entry and 10 WPM nudge to the speed dropdown, closes #5820 by @chrox in https://github.com/readest/readest/pull/5825
* fix(translate): follow Bing regional host and show why a translation failed by @chrox in https://github.com/readest/readest/pull/5826
* feat(reader): join PDF line wraps into paragraphs when copying, closes #5814 by @chrox in https://github.com/readest/readest/pull/5828
* fix(annotator): hide the range editor handles while a lookup popup is open, closes #5815 by @chrox in https://github.com/readest/readest/pull/5829
* feat(reader): show the book cover full screen from the sidebar and book details, closes #5813 by @chrox in https://github.com/readest/readest/pull/5827
* perf(sync): merge stat_pages pushes in one upsert_stat_pages RPC by @chrox in https://github.com/readest/readest/pull/5832
* feat(reader): select text across PDF pages as one selection, closes #5809 by @chrox in https://github.com/readest/readest/pull/5831
* fix(koplugin): pull reading stats in bounded pages by @chrox in https://github.com/readest/readest/pull/5833
* feat(stats): tier stat_pages history into R2 segments behind a 7-day hot window by @chrox in https://github.com/readest/readest/pull/5835
* chore: update agent memories by @chrox in https://github.com/readest/readest/pull/5840
* fix(audiobookshelf): hide ABS books without a server row and backfill covers unauthenticated by @chrox in https://github.com/readest/readest/pull/5841
* fix(stats): survive PostgREST's row cap when building archive segments by @chrox in https://github.com/readest/readest/pull/5844
* chore(stats): enable the archive compaction cron by @chrox in https://github.com/readest/readest/pull/5845
* fix(sync): send S3 object keys in SigV4 canonical form by @chrox in https://github.com/readest/readest/pull/5849
* fix(nix): match the Android AVD ABI to the host architecture (#5732) by @chrox in https://github.com/readest/readest/pull/5850
* fix(koplugin): stop auto sync from prompting for Wi-Fi on book open and wake by @chrox in https://github.com/readest/readest/pull/5848
* fix(backup): export only live library books and reclaim orphaned book files by @chrox in https://github.com/readest/readest/pull/5851
* fix(reader): keep the reading position across screen rotations by @chrox in https://github.com/readest/readest/pull/5855
* fix(sync): sync highlight deletions from KOReader to Readest by @chrox in https://github.com/readest/readest/pull/5853
* feat(reader): pair an Audiobookshelf audiobook and read along (#5807) by @chrox in https://github.com/readest/readest/pull/5856
* feat(reader): let users pick the Hardcover book a file syncs to, closes #5846 by @chrox in https://github.com/readest/readest/pull/5857
* feat(toc): wrap long headings onto multiple lines instead of truncating by @chrox in https://github.com/readest/readest/pull/5858
* fix(bookorbit): list the open book under Unmatched KOReader Books for manual linking by @chrox in https://github.com/readest/readest/pull/5860
* fix(wordlens): build kaikki packs from the raw wiktextract dump by @chrox in https://github.com/readest/readest/pull/5861
* fix(reader): move a paired audiobook by audio and decode WebP covers (#5863) by @chrox in https://github.com/readest/readest/pull/5865
* fix(sync): stop OPDS re-downloads from losing reading progress (#5859) by @chrox in https://github.com/readest/readest/pull/5866
* fix(reader): resolve media that book scripts add after the section loads, closes #1812 by @chrox in https://github.com/readest/readest/pull/5868
* fix(sync): shelve an imported book on other devices without opening it first by @chrox in https://github.com/readest/readest/pull/5869
* feat(library): add From Web Browser import with an in-app browser (#5775) by @chrox in https://github.com/readest/readest/pull/5870
* fix(reader): render the IDPF EPUB 3 samples correctly (#480) by @chrox in https://github.com/readest/readest/pull/5872
* fix(windows): match the main window's scroll bar style in clip and browser windows by @chrox in https://github.com/readest/readest/pull/5873
* fix(library): rubber-band the bookshelf at both edges and keep the reader from overscrolling by @jadhavgaurav in https://github.com/readest/readest/pull/5867
* fix(android): stop the launch crash on covers that decode 1px tall by @chrox in https://github.com/readest/readest/pull/5874
* chore: update agent memories by @chrox in https://github.com/readest/readest/pull/5875
* feat(ui): migrate to daisyUI 5 and Tailwind CSS 4 by @chrox in https://github.com/readest/readest/pull/5884
* fix(library): save the new data location when migrating an empty library by @jadhavgaurav in https://github.com/readest/readest/pull/5878
* fix(sync): apply pulled file-sync progress to the live reader by @chrox in https://github.com/readest/readest/pull/5886
* feat(reader): jump from a footnote popup to the location in the book by @chrox in https://github.com/readest/readest/pull/5889
* feat(library): select chapters when importing web novels by @chrox in https://github.com/readest/readest/pull/5892
* chore(deps): upgrade to TypeScript 7 by @chrox in https://github.com/readest/readest/pull/5893
* fix(ui): size toasts to their message and fade dialogs out whole by @chrox in https://github.com/readest/readest/pull/5894
* fix(library): refresh PDF metadata on re-import by @chrox in https://github.com/readest/readest/pull/5895
* fix(reader): do not truncate footnote popups by @alexander-pecheny in https://github.com/readest/readest/pull/5887
* fix(reader): make cross-page selection actually work by @alexander-pecheny in https://github.com/readest/readest/pull/5888
* chore(deps): bump the github-actions group with 6 updates by @dependabot[bot] in https://github.com/readest/readest/pull/5902
* fix(android): migrate Google Play Billing to v9 by @chrox in https://github.com/readest/readest/pull/5896
* fix: folder import of Markdown, widget opens, comic zoom, selection handle and TTS word highlight by @chrox in https://github.com/readest/readest/pull/5903
* fix(ui): restore the daisyUI 4 loading dots animation by @chrox in https://github.com/readest/readest/pull/5906
* fix(sync): converge multi-device file sync (#5900) by @jadhavgaurav in https://github.com/readest/readest/pull/5905
* feat(tts): lyric-style sentence view in the Read Aloud player (#5755) by @chrox in https://github.com/readest/readest/pull/5908
* fix(tts): queue a lyric reload requested during an in-flight fetch by @chrox in https://github.com/readest/readest/pull/5909
* feat(shortcuts): add customizable keyboard and mouse bindings by @WhiteHades in https://github.com/readest/readest/pull/5907
* fix(translate): Chinese targets, provider rate limits, and translator popup layout by @chrox in https://github.com/readest/readest/pull/5913
* fix(android): avoid full PDF parsing during import by @chrox in https://github.com/readest/readest/pull/5914
* feat(localsend): brand the LAN transfer feature as Nearby BookDrop by @chrox in https://github.com/readest/readest/pull/5915
* fix(ui): paint modal boxes that sit outside an open daisyUI modal by @chrox in https://github.com/readest/readest/pull/5916
* fix(mobi): keep AZW3 text and TOC intact when section loads overlap by @chrox in https://github.com/readest/readest/pull/5920
* fix(sync): report third-party sync status in the reader menu (#5910) by @chrox in https://github.com/readest/readest/pull/5922
* fix(sync): resolve book groups and metadata on their own clock (#5911, #5912) by @chrox in https://github.com/readest/readest/pull/5921
* fix(ui): search cloud storage files on demand instead of while typing (#5923) by @chrox in https://github.com/readest/readest/pull/5925
* fix(reader): stop the a11y skip link from padding RTL sections with blank pages (#5924) by @chrox in https://github.com/readest/readest/pull/5926
* fix(ui): align the keyboard shortcuts header with its group titles by @chrox in https://github.com/readest/readest/pull/5927
* feat(reader): Notebook as a linked writing workspace by @chrox in https://github.com/readest/readest/pull/5928
* release: version 0.12.6 by @chrox in https://github.com/readest/readest/pull/5929

## New Contributors
* @sloaner made their first contribution in https://github.com/readest/readest/pull/5637
* @gfreitash made their first contribution in https://github.com/readest/readest/pull/5684
* @chrisbutler made their first contribution in https://github.com/readest/readest/pull/5704
* @NoaHimesaka1873 made their first contribution in https://github.com/readest/readest/pull/5765
* @libbybar made their first contribution in https://github.com/readest/readest/pull/5780
* @jadhavgaurav made their first contribution in https://github.com/readest/readest/pull/5867

**Full Changelog**: https://github.com/readest/readest/compare/v0.12.1...v0.12.6

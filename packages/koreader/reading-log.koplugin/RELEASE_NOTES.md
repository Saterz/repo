# v1.4.0 · 2026-10-30

Reading Log is now one KOReader plugin that works with Simple UI and with Bookshelf. New in this version: Cyber and Dark Academia styles, five ornaments, a Device card, a Lifetime pages card, and a small panel under the reader's menu.

**To install:** download `readinglog-1.4.0.zip` below, unzip it, copy the `readinglog.koplugin` folder into KOReader's `plugins` folder and restart KOReader. You can also install it from the App Store plugin. On the Simple UI version already? Use Tools > Reading Log > Check for updates.

## Coming from 1.3

- **Bookshelf micro-modules version:** install the plugin as above. On the next start, Reading Log copies your settings across and offers to remove the old copy in `settings/bookshelf/micromodules`, then asks you to restart. Your Bookshelf layouts keep their cards.
- **Simple UI version: replace the `readinglog.koplugin` folder. 

Your settings live in `koreader/settings/readinglog.lua`, so updates keep them.

## New

- **One plugin for Simple UI and Bookshelf.** It installs and updates like any other KOReader plugin, with no files to copy into Bookshelf's settings. Bookshelf 6 loads the cards straight from the plugin. Both home screens share one settings file.
- **Check for updates** in Tools > Reading Log, now for Bookshelf too. It shows what's new and installs only when you say so. It can also check once a day on its own.
- **Style: Cyber.** A black page in neon yellow and cyan, cards with two corners cut off, and every card's cyber look at once. Rings become segments that light up, Continue reading becomes a HUD, the Year goal a terminal, the Monthly challenge a neural network, the quote cards a terminal window, Reading trends a diagnostics readout and the Finish forecast a countdown. The clock and page titles glitch.
- **Style: Dark Academia.** Parchment cards on a dark study's page, set in a serif with a brass rule inside each frame. Rings become pocket watches, Continue reading hangs your cover in a gilt frame, the Year goal is a globe you shade in as you read, and the Monthly challenge is a chess board that plays the Immortal Game move by move. Bar charts are rows of candles, the quote cards manuscript pages with a wax seal, and the Finish forecast an almanac entry.
- **Modules as ornaments:** five new modules with no card. They hang on the wallpaper or stand on Bookshelf's shelf among your books:
  - **Books this year:** how many books you've finished this year.
  - **Streak flame:** your reading streak, as a flame that grows the longer it runs.
  - **Letter board:** a few words of your own.
  - **Today's pages:** the pages you've read today.
  - **Pages turned:** every page you've turned, or just this year's.
- **Device card:** battery, storage, memory, Wi-Fi and front light, each with a level bar. Tap it for KOReader's battery statistics.
- **Lifetime pages card:** every page you've ever turned in KOReader, your daily average, a bar to the next round number, and this year's, this month's and this week's pages.
- **Reader panel:** off until you switch it on in Tools > Reading Log. The reader's top menu opens on a small panel with the cover, two lines of figures, a progress bar (or this week's rings) and up to eight buttons. Each button can run any action from KOReader's gesture list, with a glyph, one of KOReader's icons or a picture of your own. Every part can be switched off.

## Changes and fixes

- **Library stats match Bookshelf's count.** With Bookshelf, each book counts under the status Bookshelf gives it, like its own Shelf size card. A book marked New no longer counts as Reading because of a percentage left in it.
- **Simple UI: no white box around framed cards.** Cyber and Dark Academia cards and the ornaments now sit straight on the wallpaper.
- **Quote of the day:** Another picks a random highlight now instead of the next one in the same book.
- **Bookshelf:** cards show the colours you give them with the palette icon (#4). Opening a book and its book menu use Bookshelf's own calls (#5). Times follow KOReader's 12- or 24-hour clock.


## What you need

KOReader with Simple UI 2.7.5 or newer, or Bookshelf 6.0 or newer

# v1.3.0 · 2026-10-24

## Reading Log 1.3.0

A Cute style, a cover calendar, more quote cards, and a faster Dashboard.

### New cards
- **Cover calendar**: every day of the month with the cover of the book you read most that day, the time read under it, and the month's pages, books and time along the top. Tap a day for its books; **Today** jumps back to this month. It has its own Dashboard tab, **Calendar**.
- **Week in covers**: this week's covers in one row, as a card or a small card in the Mini dashboard.
- **Quote of the day 2, 3 and 4**: each shows a random highlight of its own, never the same one as your other quote cards.

### Style: Default or Cute
Dashboard settings (or Look and colours on any card) > **Style** > **Cute** turns on every cute look at once:
- **Hearts instead of rings**: the outer heart fills with pages, the inner one with time, and a missed day gets a broken heart.
- **Monthly challenge**: a peony that colours in as you near your goal.
- **Book club**: a garden, with vine progress bars and a dragonfly on finished covers.
- **Year goal**: a jar of hearts that spills over once you pass your goal.
- **Quote cards**: on notebook paper.
- **Cover calendars**: as tilted polaroids.
- **Continue reading**: a scrapbook.
- **Reading trends**: on sticky notes.
- **Charts**: book spines and hearts.
- **Today's timeline**: a sky from sunrise to night.
- **Finish forecast**: a desk calendar.

### Also
- Control centre buttons can show a PNG or JPEG of your own
- **Faster**: cards that haven't changed are copied instead of redrawn
- Room for 8 Dashboard tabs.

**Install:** unzip, then copy everything inside `micromodules` into `.adds/koreader/settings/bookshelf/micromodules/` and restart KOReader. Your settings are kept.

# v1.2.0 · 2026-10-22

Reading Log 1.2.0: now in four languages

Reading Log now shows in the same language as KOReader: English, Italian, Spanish or Brazilian Portuguese. 

Thanks to [@DevGizmo86](https://github.com/DevGizmo86), who built the translation system and the Italian translation. 

Also in this release

Tab names and the Random pick heading shrink a little instead of being cut off when a translation is longer.
KOReader’s log notes which language Reading Log loaded, which helps if it ever stays in English.

To update, download reading-log-1.2.0.zip and copy everything inside its micromodules folder into koreader/settings/bookshelf/micromodules/, replacing the old files.

# v1.1.0 · 2026-10-20

### New in 1.1

- **Dashboard**: Trends and Library pages, up to 7 tabs, move tabs, remove pages you added, reset the whole Dashboard.
- **Mini dashboard**: one row of up to three small modules for the top of the home screen.
- **Reading trends**: your last 90 days against your year (time, pages, reading days, session length, speed, books finished).
- **Monthly challenge**: one goal for the month, picked from your last three months or set by you.
- **Finish forecast**: when you'll finish the books you're reading at your recent pace, and where your year is heading.
- **This week vs last**: your average a day this week against last week (or month, or year).
- **Today's timeline**: each sitting today on a line through the day.
- **Control centre**: up to 8 buttons for any action, with brightness and warmth.
- **Library stats**, **Most-read authors**, **Random pick** (only the next book of a series) and **Quote of the day** (from your own highlights).

# v1.0.0 · 2026-10-19

- 21 cards for Bookshelf's home screen and full-screen view: Banner,
  Continue reading, Activity rings, Week rings, Month rings, Month totals,
  Pages per day, When you read, Longest reads (month), Longest reads (year),
  Time read by month, Books and pages, Year in covers, Year goal, Top genres,
  Book club, TBR shelf, Finish by, This week, Reading heatmap and Recently
  finished.
- A Dashboard that puts them together as three tabbed pages, Today, Yearly
  and Monthly, with every page editable on the device. The Monthly page steps
  back through the last twelve months.
- Cards on their own match Bookshelf's look, including its dark theme.
- Three themes (White, Dark, Paper) and twelve accent colours chosen for
  colour e-ink, with screen updates that clear ghosting.
- Any card can run a plugin, a KOReader action or a menu entry when tapped.

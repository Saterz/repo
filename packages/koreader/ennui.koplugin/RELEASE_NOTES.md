# v1.7 · 2026-10-28

## What's new in 1.7
- **Module Rack changes.** (The rack first appeared in 1.6: a panel that appears over the
  home screen from the left or right edge, full height and about half the screen wide,
  with the edge against the screen edge flush and the inside edge rounded.)
  - **System:** Battery and Storage are now one card. In its options, Battery,
    Frontlight, Storage and Used and total space can each be switched on or off. Racks
    set up in 1.6 carry over: a rack that had only one of the two keeps only that one.
  - **Highlights** now come from every highlight in every book you've opened, not just
    recent ones (the "Books to draw from" setting is gone). They're kept in a small index
    file (`cache/ennui_highlights.lua`) that is brought up to date in the background, a
    few books at a time, and only for books whose data changed, so the first run on a big
    library can take a little while and later runs are quick. One highlight is picked when
    you open the rack and nothing else changes it. **Tap** it to see the whole highlight
    (with your note and the book) in a pop-up. **Long-press** it to load a different one.
    This fixes taps on the card doing nothing in 1.6.
  - **Reading stats** are worked out at most once every 24 hours and kept; **long-press**
    the card to refresh them now. The card says when it was last updated, so the Today
    row can be out of date until then. The current book's progress is always read fresh.
  - **Font settings** (Module Rack > Font settings): a typeface and size for card titles,
    and a typeface and size for everything else, applying to every module. The big
    numbers are 1.9 times the body size and the small captions 0.85 times.
- **Smaller tap areas.** Plugin entries, the weather line, the page indicator and each
  cover now respond to taps only on the item itself plus about 8 pixels of invisible
  margin (covers: at most half the gap between them), not across the whole width of the
  screen. The alignment setting still decides where they sit.
- **Build Mode long press** now uses where each item really is on screen: long-pressing
  on the date, clock, weather, a plugin entry or a cover (or just beside it) opens that
  section's settings, and long-pressing empty space beside it does nothing. This should
  also fix long-pressing Recent books. If it still doesn't work, the log line "long press
  at ... isn't on any section" shows where the press landed.
- Everything else from 1.6 works as before: Refresh cover cache under Extras, Recent
  books wrapping like text, Hide lower sections in folders, padding from -1000 to +1000,
  and the color screen with its - and + buttons, Copy color and Paste color. Opacity is
  still gone.
- Version numbers use two digits (1.7).

# ennUI · 2026-10-04

**What's new in 1.0**
- Renamed throughout to **ennUI** (the capitalization you'll see everywhere
  it's displayed — toasts, menu titles, the plugin listing).
- The Plugin entries "Max entries per page" setting now reads
  **"Auto-fit to page"** instead of "No limit" when no cap is set.
- KOReader's top menu (Tools) now has a single **"ennUI"** entry, which takes
  you to the home screen. The separate "ennUI settings" entry is gone — swipe
  up from the bottom of the home screen for Settings, as in the last version.

# v5.31.0 · 2026-10-18

**New**

- Conditionals can now check what another plugin is showing in the status bar. `[if:plugin_content{readtimer}]` is true while Read Timer has a countdown running, so a line like `[if:plugin_content{readtimer}]%plugin_content{readtimer}[else]%time[/if]` shows the timer while it runs and the clock the rest of the time. `[if:plugin_content]` on its own checks any plugin.
- Traditional Chinese translation, and corrections to Simplified Chinese, thanks to @GOSENGWONG.

**Fixed**

- `%calibre{}` found nothing when no home folder had been set, on devices where Calibre puts `metadata.calibre` in KOReader's default home (e.g. Kobo).
- Book descriptions that write accented letters as HTML codes (`P&aacute;nfilo`) now show the letters.

# v5.30.0 · 2026-10-06

**Fixed**

- With Bookshelf 5.3 or later, Bookends leaves room for Bookshelf's status line again. Bookshelf 5.3 moved the status line's settings, so Bookends stopped finding them.
- Typing in the token library's search box and then picking a token, or tapping Close, while the keyboard was still open left the keyboard behind. KOReader then stopped responding to taps until it was restarted.

**New**

- Calibre metadata is now also looked for in the folder above your home folder. Calibre puts `metadata.calibre` in the root of the device, so it's now found when home is a Books folder inside that root.

# v5.29.1 · 2026-09-29

Submitting a preset to the gallery now always asks who to credit and for its description, pre-filled so you can check them. Before, a preset installed from the gallery and then changed could go out under the original author's name without asking.

# v5.29.0 · 2026-09-28

**New**

- The preset gallery has two new sorts, *This week* and *This month*, showing which presets people have been installing lately. *Popular* still ranks by installs of all time.

# v5.28.0 · 2026-09-27

**New**

- Full-width progress bars can now be placed relative to the lines of text at the top or bottom, instead of at a fixed distance from the edge of the screen. Turn on *Position relative to line text* in a bar's settings and it keeps its place beside the text, even on a screen where the text comes out bigger or smaller. The new *Inverted header* preset in the gallery uses it to look the same on any device.

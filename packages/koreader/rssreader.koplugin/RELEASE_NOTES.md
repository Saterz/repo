# v1.21.0 · 2026-10-18

# RSS Reader v1.21.0

## New: Instapaper sanitizer

You can now use Instapaper's own article parser, through its API v2, to fetch full articles (`type = "instapaper"`).

- **Setup:** create an application and a personal access token at [instapaper.com/developers/applications](https://www.instapaper.com/developers/applications). Put the token in the `token` field of the new sanitizer entry and set `active = true`. No other plugin is needed.
- **How it works:** Instapaper only parses articles that are saved in your account. Each story is therefore saved as a bookmark, its parsed text is read back, and the bookmark is deleted again.
- **Cost:** parsing is free for personal use up to Instaparser's free credit. Once that runs out, Instapaper answers `402` and the next sanitizer in your chain is tried.
- **Your existing bookmarks are safe:** if a link is already saved in your account, the plugin keeps that bookmark and never deletes it. This covers bookmarks that are archived, liked, in a folder, tagged, partly read, or saved more than two minutes earlier.
  > ⚠️ A link you saved moments ago and never touched looks the same as the plugin's temporary copy. If you also read with Instapaper, **use a separate Instapaper account for this sanitizer**.
- **Rate limiting:** parse calls are spaced like Instaparser's (`seconds_between_calls`, default **2 s**), and the spacing also applies across Offline Mode's parallel workers. If a save or parse is rate-limited (`429`), it is retried once.
- **Fails fast:** a `401` (token refused), `402` (credit used up) or `403` (application suspended) pauses the sanitizer for an hour. The stories after it skip it instead of each spending a save and a delete to find out. Restarting KOReader clears the pause.

### Configuration

Copy the new entry from `rssreader_configuration.sample.lua`:

```lua
{
    order = 5,
    type = "instapaper",
    active = false,
    token = "your_instapaper_access_token",
    seconds_between_calls = 2, -- 0 = no limit
},

# v1.20.1 · 2026-10-10

# RSS Reader v1.20.1

## 🐛 Fix: Instaparser rate limiting in Offline Mode

Offline Mode's parallel downloads could go over Instaparser's Trial limit of 1 call per second, so Instaparser rejected calls and sent a warning e-mail.

- Instaparser calls now go out at least **2 s apart**, including across Offline Mode's parallel downloads.
- A call that is rate-limited anyway is retried once.
- New option `seconds_between_calls` in the Instaparser sanitizer entry (default `2`, `0` turns the limit off). Existing configurations work without changes.


# RSS Reader v1.20.0

## ✨ New: Offline Mode

Download the stories of the feeds you choose in one go, then read them with Wi-Fi off. Built for devices that are slow to get online. Open it from the new **Offline** row in the account list. The number next to it is how many downloaded stories are still unread.

### Choosing feeds
- Pick feeds from any account, local ones included. You can also pick virtual feeds such as **★ All Unread**, FreshRSS special feeds and CommaFeed tags.
- Long-press a folder to **Tick all** or **Untick all** feeds in it, subfolders included. Tick all skips virtual feeds, so no story is downloaded twice.
- Your selection is saved on every tap and stays ticked for next time.

### Downloading
- Options: stories per feed (5/10/20/50), only unread, full article or feed text only, images on or off, what to do with previous downloads, and turn Wi-Fi off when done.
- Every option opens with the value you used last time.
- Full articles are fetched three at a time in the background. Diffbot and FiveFilters (RapidAPI) never run in parallel, so their rate limits and quotas are respected.
- Tap the progress message to cancel. Stories already downloaded are kept.

### Reading offline
- Downloaded stories open without any connection. **Next** at the end of an article opens the next downloaded story.
- Long-press a story to mark it read or unread, or to delete it. Long-press a feed to mark all its stories read, delete its downloads, or remove it from the selection.

### Syncing read states
- Read states from offline reading are sent to the server automatically: when the device comes online, before a download, and before you open the account. A manual mode is also available.
- Changes that could not be sent stay pending and are retried next time.
- CommaFeed, FreshRSS, Miniflux, NewsBlur and Feedbin send up to 100 stories per request.

### Gestures and Profiles
Three new actions:
- **RSS Reader: offline list**
- **RSS Reader: download selected feeds**: starts a download with your last options and no dialog
- **RSS Reader: sync offline read states**

Combined with *Turn Wi-Fi off when done*, a single gesture connects, downloads and disconnects.

## 🐛 Fixes
- A restored feed that comes back empty (for example **All Unread** after you read its last story) no longer leaves only "No stories available." on screen. The plugin now forgets that feed and returns to where you opened it from.

# v1.19.0 · 2026-10-09

## v1.19.0

### New: Feedbin accounts
- Add a `feedbin` account. It signs in with your Feedbin email and password.
- Feedbin tags show as folders. A feed with several tags appears in each of them.
- The account's top level has **★ All Feeds**, **★ All Unread** and **★ Starred**.
- You can mark stories read or unread and starred or unstarred.
- *Mark all as read* works on feeds, folders, the whole account and the ★ feeds.
- Unread counts fill in over a few refreshes and show as e.g. `(12+)` until they are complete.

### New: Feedbin article extraction
- A new sanitizer type, `feedbin`, fetches the full article for Feedbin stories. It needs no token and has no quota.
- Stories from other accounts skip it and go to the next sanitizer.
- It is off by default. To turn it on, set `active = true` for it in your configuration.

### Fixes
- Titles with an apostrophe or `&` no longer show `&#39;` or `&amp;` in the title or the saved file's name.
- A title made only of punctuation no longer becomes a hidden `.html` file.
- A very long title no longer makes opening the article fail. Filenames are now capped at 64 bytes.
- After the RSS button in an article, Back now goes up through the feed's folder instead of straight to the account list.
- Tapping an account on that list no longer closes the article underneath.

Thanks to @anthonyfelts for this release (#18).

# v1.18.0 · 2026-09-27

### New

- A refresh icon in the top-left corner of feed and article lists (or the Menu key on devices without a touchscreen) reloads the list without leaving the plugin.
- On lists that support it, that same icon opens a small menu with "Refresh" and "Mark all as read".
- You can long-press any feed or folder and pick "Open on startup" so the plugin opens straight to it.
- In the article preview, turning the page past the last page opens the next article, and turning back from the first page opens the previous one. You can change this under Settings > Page keys at article edges.
- The article preview has a new "Previous" button for devices that only have a touchscreen.
- The dialog at the end of an article now has "Next" and "Next unread" buttons, so you can go on to the following article without going back to the list.

### Fixed

- "Mark all as read" now works for FreshRSS feeds, folders and whole accounts. Before, they stayed unread.
- If your login is rejected, the plugin now stops instead of retrying forever.
- Leaving the RSS list now closes the article that was open under it, so you're no longer stuck going back and forth between the two.
- Two articles opened quickly one after another no longer break each other's images.

# v1.17.2 · 2026-09-22

## v1.17.2 — Designed EPUB covers

Saved articles now get a cover of their own instead of a bare lead image.

- **Painted cover** — the article title on top, the lead image cropped into a
  landscape band in the middle, and the byline plus feed name at the bottom.
- **No image, still a cover** — articles without a usable picture get a
  text-only cover with larger type, so nothing lands in the library as a blank
  tile.
- **No extra downloads** — the cover reuses the image already picked for the
  article; it is fetched once and packed into the EPUB as before.

On by default. Turn it off under **Settings → Designed EPUB cover** to keep the
previous plain lead-image cover; if a cover cannot be painted for any reason,
the plugin falls back to that automatically.

## v1.17.1 — Sanitizer fixes

- **Diffbot is usable again** — its wait was cut short by the wrong timeout, so
  most successful extractions never arrived; the timeout now follows Diffbot's
  own page-fetch budget.
- **Diffbot rate limit handled** — a 429 from the free plan is retried once
  after the wait the server asks for, instead of silently falling through to
  the next sanitizer.
- **Plain-text and list pages** — Diffbot responses that carry only a `content`
  field were read as empty; they now come through.
- **RSS links with entities** — `&amp;` and `&#038;` inside `<link>` are decoded
  like every other field, fixing the ~4% of feed links that opened broken.

## v1.17.0 — Metadata, speed and FreshRSS favourites

- **Richer saved EPUBs** — author, description, cover image and a real chapter
  list are filled in from data already downloaded, at no extra request.
- **Parallel image downloads** — an article's images are fetched by several
  worker processes at once instead of one after another.
- **FiveFilters via RapidAPI** — replaces the discontinued free service, with a
  monthly request cap so the plan is not overrun.
- **FreshRSS favourites** — star and unstar articles, browse them in a Starred
  feed, and see the star in the list.
- **FreshRSS 404 fix** — the error that hid every feed on some servers is gone.

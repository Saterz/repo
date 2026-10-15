# v2.0.3 · 2026-10-15


- **Connection doctor.** "Menu > Diagnostics > Connection doctor" checks the network, the Goodreads backend, your sign-in and saved session, pending syncs, the device clock and diagnostic logging, then tells you what to do about anything it flags.
- **Export diagnostic log.** One tap writes a single report file into the plugin's settings folder - the checks, your settings, recent activity and the latest KOReader crash log - so it can be copied off over USB and attached to a bug report. Passwords, cookies and session tokens are never included; the summary can also be copied to the clipboard.

# v2.0.2 · 2026-10-15

Minor bug fixes.

- **Author search works again.** Goodreads replaced the author search page with a client-side (React) app that returns no author data to a scraper, so it always reported "No matches". Author candidates are now derived from the autocomplete payload, which carries each book's author id and name.
- **"Find on Goodreads" is more reliable by id or link.** A book link (or `goodreads id N`) is now resolved directly — autocomplete never resolves those forms — and a bare numeric id still falls back to a direct lookup even when the autocomplete request fails or is challenged, instead of reporting an error.

# v2.0.1 · 2026-10-15

- **Find on Goodreads now accepts a Goodreads link or numeric ID.** Pasting a book's Goodreads link (for example `https://www.goodreads.com/book/show/17306293-shift`) or typing its numeric ID in "Find manually" now finds the book. Until now those searches reported "No matches found"; searching by title, author or ISBN was unaffected. An all-digit title (like 1984) still searches by title.

# v2.0.0 · 2026-09-30

Release v2.0.0

# v1.26.1 · 2026-09-30

- **Browse Goodreads — crash fix.** If the image cache directory was missing, pruning threw and the whole page failed ("Couldn't load the page"). Pruning is now a safe no-op and image/CSS enrichment can never fail a page. Added a regression test.
- **Browse Goodreads — better home + messages.** It opens **My Books** (`/review/list`) instead of the anti-bot-challenged root `/`, and shows clearer "sign-in required" / "blocked" messages.
- **Browse Goodreads is now experimental and dev-channel only** (hidden on stable), labelled "Browse Goodreads (experimental)…".
- **Reader-style rendering by default** (skips the site's modern CSS, which CRE can't lay out); dev toggle for Site vs Reader style.

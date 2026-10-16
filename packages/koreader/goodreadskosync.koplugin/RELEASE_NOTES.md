# v2.0.5 · 2026-10-16


- **The right edition, not just the first hit.** When a search returns several editions of one book, the plugin now shows them to pick from instead of silently linking the first result. The list shows what tells editions apart - page count, and the ISBN/ASIN when the search carried one - and marks the one that matched your file's identifier. A file's ISBN or ASIN is preferred when matching; if it finds nothing on Goodreads, the plugin falls back to a title/author search so there is still a list to choose from, and a weak match is never linked on its own.

# v2.0.4 · 2026-10-16


Android sign-in works now, and the diagnostic report explains itself.

- **Sign-in on Android completes.** The plugin saves your session the moment Goodreads accepts it, and on Android the crypto library it used raised instead of falling back, so a successful sign-in was reported as a failure - Goodreads would email "a new device logged in" while the plugin said the login failed. Crypto failures now fall back to plaintext (Android has no OS keystore) instead of breaking the login. Kindle behaviour is unchanged.
- **Connection doctor: new "Secure connection" check**, and the exported report gained a **"platform" section** (where the plugin keeps its files, whether a KOReader crash log exists). Handy when a report comes from a phone.
- **Saving plugin state no longer depends on a shell.** The settings folder, the diagnostic log and the cover cache are created with KOReader's own `util.makePath` instead of `mkdir`.

# v2.0.3 · 2026-10-15


- **Connection doctor.** "Menu > Diagnostics > Connection doctor" checks the network, the Goodreads backend, your sign-in and saved session, pending syncs, the device clock and diagnostic logging, then tells you what to do about anything it flags.
- **Export diagnostic log.** One tap writes a single report file into the plugin's settings folder - the checks, your settings, recent activity and the latest KOReader crash log - so it can be copied off over USB and attached to a bug report. Passwords, cookies and session tokens are never included; the summary can also be copied to the clipboard.

# v2.0.2 · 2026-10-15

Minor bug fixes.

- **Author search works again.** Goodreads replaced the author search page with a client-side (React) app that returns no author data to a scraper, so it always reported "No matches". Author candidates are now derived from the autocomplete payload, which carries each book's author id and name.
- **"Find on Goodreads" is more reliable by id or link.** A book link (or `goodreads id N`) is now resolved directly — autocomplete never resolves those forms — and a bare numeric id still falls back to a direct lookup even when the autocomplete request fails or is challenged, instead of reporting an error.

# v2.0.1 · 2026-10-15

- **Find on Goodreads now accepts a Goodreads link or numeric ID.** Pasting a book's Goodreads link (for example `https://www.goodreads.com/book/show/17306293-shift`) or typing its numeric ID in "Find manually" now finds the book. Until now those searches reported "No matches found"; searching by title, author or ISBN was unaffected. An all-digit title (like 1984) still searches by title.

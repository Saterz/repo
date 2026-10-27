# v1.1.0 · 2026-10-26

## v1.1.0
- Color rendering on color Kindle panels (Colorsoft).
- Page navigation: ▲/▼ buttons on the right edge (zoom-aware, one screen per tap, with overlap).
- Selectable browser User-Agent (Firefox/Chrome/NetSurf) in Settings.
- Torrent-downloaded azw3/mobi now offers EPUB conversion.
- Fix crash/busy-loop on older devices (BusyBox sleep without fractional seconds).

# 1.0.2 · 2026-10-25

   ## v1.0.2
   - Fix crash/busy-loop on devices whose BusyBox `sleep` rejects fractional
     seconds (older Kindles): the supervisor now falls back to `sleep 1`.

# v1.0.1 · 2026-10-25

Just pushed v1.0.1 which makes the framebuffer writer bit-depth-aware (8/16/32 bpp), so it should now fill the whole screen on color Kindles (grayscale for now).

# v1.0.0 · 2026-10-24

InkSurf v1.0.0 — a real web browser for jailbroken Kindle, as a KOReader plugin.

Embeds the NetSurf engine (limited JavaScript) so logins, forms, images and most
file types work — things the stock Kindle browser can't do.

Highlights:
- Custom e-ink touch toolbar; type into the URL bar and in-page fields with
  KOReader's own keyboard (existing field text is loaded and replaced).
- Minimize/resume, pinch-zoom, drag-to-pan, reader mode (local, private).
- Downloads to koreader/documents; .torrent via a built-in aria2 manager.
- azw3 → EPUB conversion; OpenVPN (any provider) with kill-switch; ad/tracker
  blocking; UI in English / Hungarian / German.

Requirements: a jailbroken Kindle (MTK / hwtcon_v2, e.g. PW5/PW6) with KOReader.

Install:
1. Download `inksurf.koplugin.zip` below.
2. Extract so that `inksurf.koplugin` lands in `koreader/plugins/`.
3. Restart KOReader. Open it from the main menu.
4. (Optional) VPN: drop your own `.ovpn` + `.auth` into `inksurf.koplugin/vpn/`
   (see `vpn/README.txt`). No VPN credentials are shipped.

Built from source via GitHub Actions (`build.sh`). GPL-2.0-or-later; see
THIRD_PARTY_NOTICES.md for bundled components (NetSurf, aria2, OpenVPN, FBInk,
libmobi) and their licenses.

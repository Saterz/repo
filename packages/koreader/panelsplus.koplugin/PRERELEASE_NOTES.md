# v1.5.0-nightly · 2026-09-21

# The `Texty Texty` Update

This is a `Release Candidate` which means it basically is 90% done. Just I need to test it with more edge-cases and polish some features here and there, you can already test it if you want it. I doubt it could have any bugs there, its stable, so it's more about improving the new "Smart" algorithm (you'll see it in the next # Features section).

---

# Features and changes
<div align="center">

<h2>1. OCR strongly improved</h2>
<p><em>No PDF text-layer needed—just images and it works!</em></p>
<table>
  <thead>
    <tr>
      <th width="50%" align="center">Native OCR Improvements</th>
      <th width="50%" align="center">Text-Layer Force Option</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center" valign="top">
        <video src="https://github.com/user-attachments/assets/f9c2908d-21ad-4fbd-a528-8db51af4ddc6" controls width="100%"></video>
      </td>
      <td align="center" valign="top">
        <video src="https://github.com/user-attachments/assets/7742d6a0-c2dd-4f9f-822c-c9b81871cf2c" controls width="100%"></video>
      </td>
    </tr>
    <tr>
      <td align="left" valign="top">
        This is the <strong>main focus</strong> of this update. You don't need to scan previously your mangas for OCR support, Panels+ natively finds the word in your image and send it to your dictionary lookup. OCR has been strongly improved for <strong>any language</strong> as long as you the correct Tesseract language model (spanish, for spanish mangas; english for english mangas, etc...) and install it in your KOReader. 

This video was made in a .CBZ manga, only images there!.
      </td>
      <td align="left" valign="top">
        <strong>For PDFs with a text-layer:</strong> You can force Panels+ to use your existing text-layer instead of Panels+ native OCR recognition (opt-in feature).
      </td>
    </tr>
  </tbody>
</table>
</div>

But this time I wanted to go even *further*. Panels+ from now on will have 2 builds! for you to download:
1. `Vanilla/normal`: The normal Panels+ experience, and very lightweight in MB size, the zip file is: `panelsplus-1-5-0-RC1.koplugin.zip` below in downloads version.
2. `OCR-Embbeded` (Exclusive for English and Spanish recognition text): This build includes ***2 OCR Panels+ Fine-tuned*** models for manga lettering style, which works 10-15% better than any other generic OCR teserract build for english and spanish, by default english enabled, but as you saw in the demo before, you can change easily of OCR teserract, including your own-installed teserract installed ones!.
Zip file is: `panelsplus-1-5-0-RC1-OCR-EmbbededVersion.koplugin.zip` below in downloads section.

---

<div align="center">
<h2>2. Panels+ config menu `redesigned`</h2>
<img width="40%" height="auto" alt="image" src="https://github.com/user-attachments/assets/717bf138-e21d-46a5-8f63-04bcb76f0379" /><img width="60%" height="auto" alt="image" src="https://github.com/user-attachments/assets/36aec568-6a5f-435f-adb3-9a8763f13c9a" />
</div>
<em>This new update brings many new options, that the classic menu would not be enough space for all of them, so I redesigned the menu to improve user experience and, avoid many clunky buttons in the interface. Buttons accomodate themselves depending if landscape or portrait mode</em>
<em>Probably I'll add a toggle option to revert back the old look and original button disposition for the final v1.5.0 version</em>

---

<div align="center">
<h2>Panels Finding Algorithms Improved. New algorithm: Smart(er)</h2>
<video src="https://github.com/user-attachments/assets/f3e96cc3-a1d3-40e7-b4e5-33c704b26783"></video>
</div>
<em>Classic panels finding algorithm from previous version (since first commit in this repo up to v1.4.0 previous) is still available for you in "Safe" mode, which is safe to find panels by grouping them when possible to avoid breaking some styles in panels. But if you want to get EVERY panel, even if sometime there's a character or a weird dialog text only intersecting by one pixel between 2 panels, smart algorithm is for you!. You can choose either of them, opt-in. By default Panels+ uses "Safe" algorithm.</em>

---

<h3>There are many other features there. But I'm too lazy to make a showcase of them all only for a Release Candidate, over time, ill be adding them here, or you can discover them by yourself \<3</h3>

<em>From here: I need to improve the redaction of this section. It'll be cleaned over time.</em>

<div align="center">
<h2>Quality of Life and miscellanea features<h2>
<h3>New trigger with double finger tab instead of always long press</h3>
In case you have other plugins that uses the Long-press gestures in your panels, (opt-in option).  

https://github.com/user-attachments/assets/46cfb6a1-3f66-48fc-a8eb-0ecc5a7a6921
</div>



---

## D2 @MartinoAichner [\[Pull Request\]](https://github.com/KristanLaimon/PanelsPlus/pull/9): Improved OCR recognition for PDF files that include a text-layer embbeded.

<img width="800" height="450" alt="text_layer_before_ocr" src="https://github.com/user-attachments/assets/2a72596c-efb5-48bc-9d1c-caa8eb33b2d4" />
<em>Showcase made by @MartinoAichner</em>

--- 

## D3 @KristanLaimon [Generic Feature]: Increased panel recognition patterns by adding more common mangas to internal Panels+ dataset like:
- [Nagatoro (Vol. 1)](https://es.wikipedia.org/wiki/Ijiranaide,_Nagatoro-san)
- [Horimiya (Vol 1.)](https://es.wikipedia.org/wiki/Hori-san_to_Miyamura-kun)
Which means, this plugin will have at least 95% precision on those mangas natively and will improve panels finding in other mangas as collateral effect (the purpose for this).

---

## D4 @KristanLaimon [(1/2 Bug-fix, reported by @Keithcat25)](https://github.com/KristanLaimon/PanelsPlus/issues/6): Fixed bad rotation bug in android devices
Before:
<table>
  <tr>
    <td width="33%">
      <img alt="Image" src="https://github.com/user-attachments/assets/abe26e27-ef2f-402c-a867-d13e369a1b5d" />
    </td>
    <td width="33%">
      <img alt="Image" src="https://github.com/user-attachments/assets/13b4662d-414d-4d56-92cf-b42439289e02" />
    </td>
    <td width="33%">
      <img alt="Image" src="https://github.com/user-attachments/assets/f02e3046-8470-4a0b-9aa2-1405f4217eee" />
    </td>
  </tr>
</table>
<em>Images/Feedback provided thanks to @Keithcat25</em>

After:
<video alt="Image" src="https://github.com/user-attachments/assets/86a7a166-557d-4354-9754-2f90e7339e66" />

<em>Showcase made by <strong>me</strong></em>

### NOTE: this works for android phones with RGB screens, currently not working in android ink-based screens, still working on it.

---
## D5 @Pixxel123  [\[Pull Request\]](https://github.com/KristanLaimon/PanelsPlus/pull/10): Improved OCR recognition for PDF files that include a text-layer embbeded.

<img align="center" alt="img" height="auto" width="480"  src="https://private-user-images.githubusercontent.com/36304206/655848880-61ef544c-b595-4b5d-9d4b-7415bf739563.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3OTA0MTUyNzcsIm5iZiI6MTc5MDQxNDk3NywicGF0aCI6Ii8zNjMwNDIwNi82NTU4NDg4ODAtNjFlZjU0NGMtYjU5NS00YjVkLTlkNGItNzQxNWJmNzM5NTYzLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjA5MjYlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYwOTI2VDA5MjkzN1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWRhZjQzMWRiYmFjNTc5NGViZDY5NjY5OWJiYzQ0OWVlMjBiZDUxYjI2YTFlNDdmMTZlMmUyMGY2ZmViNWE4NzcmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JnJlc3BvbnNlLWNvbnRlbnQtdHlwZT1pbWFnZSUyRnBuZyJ9.JFnCFeoQhOcFJYPWJgfdBaYK8kXPJPQ8Y8mJ2rPhbBg" />

--- 

## New Contributors
* @Pixxel123 made their first contribution in https://github.com/KristanLaimon/PanelsPlus/pull/7
* @MartinoAichner made their first contribution in https://github.com/KristanLaimon/PanelsPlus/pull/9
*  @IMJXXL made Chinese Simplified translation.

---

Zips:

1. `panelsplus_1_5_0_nightly_android_fix.koplugin.zip`  (Pre v1.5.0-RC1, really old)
This is a build including *D1*, *D2* and *D4* (read previous section), featuring android fix. Made to test fix for [this PR](#6) along other android bugs I found. This is an old build. Just keep for legacy concerns.

2. `panelsplus-1-5-0-RC1-OCR-EmbbededVersion.koplugin.zip`  (v1.5.0-RC1 OCR Embbeded version)
It includes all the features previously mentioned + 2 fine-tuned OCR models for spanish and english (but still compatible with your hand-installed OCR models like teserract). `4.08 MB Size`

3. `panelsplus-1-5-0-RC1.koplugin.zip` (v1.5.0-RC1)
It includes all the features previously mentioned only without embbeded fine-tuned models (but still compatible with your hand-installed OCR models like teserract). `183 KB`

# v1.4.0-nightly · 2026-09-06

Hello fellas, this time, it's a nightly build release. Including some fixes for bugs found thanks to @sukhmeetsingh170200 and other ones I found myself and translations!. Why not a full release? well, normally I test the plugin many days myself until I found it stable and pleasant to use but wanted to release these meanwhile I'm battle-testing this 1.4.0 version. 

## Features
- Added native spanish translations for my spanish users.

## Enhancements 
- Improved flow layout order when reading in comic and manga mode, should follow panels from top to bottom and (left to right | comicmode) and (right to left | mangamode) going from upper panel to upwards direction instead of upwards.

## Fixes
- Fixed [strange device orientation behaviour](#1) when using Panels+ orientation then for some reason going back to original Koreader orientation.
- Many other fixes that are too technical and I'm lazy to document.I'll document them properly in the future 1.4.0 stable release.


# Notes:
This version is not battle-tested as normal stable-versions, use this nightly build if you want to test-out the latest features without having to wait for the next stable release.

If you're openning an issue make sure you're using the [latest stable version instead](https://github.com/KristanLaimon/PanelsPlus/releases/latest)

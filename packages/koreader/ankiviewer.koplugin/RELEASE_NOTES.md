# v1.4.0 · 2026-10-23

## v1.4.0

### Update decks without losing your progress

You can now add cards to a deck you're already studying, for example during a semester, without resetting your reviews.

Export the deck from Anki again with the **same file name** and import it. If a deck with that name already exists, you can choose:

- **Merge (keep progress):** new cards are added, edited cards get their new text, and all review progress is kept.
- **Merge and remove cards not in file:** same as above, but cards you deleted in Anki are removed too.
- **Replace (reset progress):** the previous behavior; the deck is rebuilt from scratch.

Cards are matched by their Anki note ID, so fixing a typo or rewording a card in Anki keeps its review history.

### Other changes

- Changing a deck's **field mapping** no longer resets review progress.
- Existing databases are upgraded automatically; no data is lost when updating the plugin.

### Notes

- Decks imported with an earlier version are matched by their front text the first time you merge. After one **Merge** import, matching uses the Anki note ID.
- The deck name comes from the `.apkg` file name. A file renamed to something like `Biology (1).apkg` is imported as a separate deck.

# v1.3.0 · 2026-04-05

- **Delete Button**: Added delete button to study screen rating row (rightmost position) with confirmation dialog
- **Fullscreen Study Mode**: Toggle fullscreen mode in settings to maximize card display area with optimized dimensions
- **Tap to View Full Text**: Tap on card content to view complete text in a scrollable popup viewer
- **Minimum Interval Setting**: Configure minimum review interval (1d, 3d, 7d, 14d) with proportional scaling across all ratings (Again: 1x, Hard: 1.5x, Good: 2x, Easy: 4x)
- **Enhanced Touch Areas**: Expanded rating button tap areas to include interval labels above buttons for easier interaction

# v1.2.0 · 2026-02-05

- New Settings: max number of daily new cards

# v1.1.0 · 2025-12-26

- new option: randomize cards

# v1.0.1 · 2025-12-13

- fix: crash on vertical small

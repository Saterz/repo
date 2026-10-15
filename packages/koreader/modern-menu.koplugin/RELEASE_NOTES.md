# v1.7.0 · 2026-10-14

## modern_menu 1.7.0

Shortcuts Toolbar custom actions run from this menu, and the file-browser status bar is optional.

### Changes
- Custom Shortcuts Toolbar buttons run from the reader row: system actions, menu-path actions, and a shortcut that opens a submenu
- Choosing **Menu action** records a tap in this menu, including items inside a submenu
- The file-browser shortcut row is present when KOReader starts in the file browser
- **Status bar in file browser** is in **Modern Menu** settings and is off until you turn it on. The switch is no longer in the menu header

### Install
1. Download **modern_menu.koplugin-v1.7.0.zip**
2. Extract into your KOReader `plugins/` directory
3. Restart KOReader and enable **Modern Menu**
4. Install Simple UI, Quick Menu, Neo Quick Settings, or Shortcuts Toolbar as well if you use those

# v1.6.0 · 2026-10-14

## modern_menu 1.6.0

Shortcuts Toolbar in the reader menu, and a tap outside a short menu closes it.

### Changes
- Shortcuts Toolbar’s reader row (back button and shortcut icons) sits at the bottom of the menu when that plugin is enabled
- A tap on the page below the menu closes it when height is fit to content or a percentage. Full-screen height stays open until you close it
- Works with Simple UI, Quick Menu, Neo Quick Settings, and Shortcuts Toolbar. Does not work with Zen OS

### Install
1. Download **modern_menu.koplugin-v1.6.0.zip**
2. Extract into your KOReader `plugins/` directory
3. Restart KOReader and enable **Modern Menu**
4. Install Simple UI, Quick Menu, Neo Quick Settings, or Shortcuts Toolbar as well if you use those

# v1.5.0 · 2026-10-14

## modern_menu 1.5.0

Custom Neo actions, a Simple UI tab, and a menu that can be shorter than the screen.

### Changes
- Custom Neo Quick Settings buttons run their real action. Exit, restart, dispatcher, and menu-path buttons no longer stop at closing the tab
- Simple UI’s quick-settings tab shows its action buttons, and taps, swipes, and holds on that panel do what Simple UI expects
- **Default tab** picks which tab opens first. Automatic keeps the Quick Menu or Neo default
- **Menu height** can be full screen, fit to content, or a fixed percentage of the screen (40–100). The sheet stays at the top; a tap below it closes the menu
- Fit-content and percentage sheets end on a rule, so the bottom of the menu is visible
- The percentage picker can confirm 70%, the default, without the Set button staying disabled

### Install
1. Download **modern_menu.koplugin-v1.5.0.zip**
2. Extract into your KOReader `plugins/` directory
3. Restart KOReader and enable **Modern Menu**
4. Install [quickmenu.koplugin](https://github.com/jbreizh/quickmenu.koplugin), Neo Quick Settings, or Simple UI as well if you want that tab

# v1.4.0 · 2026-10-13

## modern_menu 1.4.0

Hosts Neo Quick Settings the same way as Quick Menu, and adds a menu font picker.

### Changes
- Neo Quick Settings is hosted as a tab when that plugin is installed, including its buttons, settings, and brightness and warmth sliders
- Slider drags repaint through the menu, so swiping a slider no longer crashes on Android
- Swipe-to-exit and swipe-to-restart confirmations work from the hosted panel
- Quick Menu’s exit tab leaves the book for the file browser; in the file browser a tap closes the menu and a hold asks before quitting KOReader
- **Menu font** setting lists the same faces KOReader uses for its menus
- Neo Quick Settings grid lines up with the menu’s side inset

### Install
1. Download **modern_menu.koplugin-v1.4.0.zip**
2. Extract into your KOReader `plugins/` directory
3. Restart KOReader and enable **Modern Menu**
4. Install [quickmenu.koplugin](https://github.com/jbreizh/quickmenu.koplugin) or Neo Quick Settings as well if you want that tab

# v1.3.0 · 2026-10-12

## modern_menu 1.3.0

Hosts Quick Menu as the first tab when that plugin is installed, and refreshes button state as soon as a toggle runs.

### Changes
- Quick Menu panel and footer render inside Modern Menu
- Opens on the Quick Menu tab when “Always start on quick menu tab” is on
- Hold the Quick Menu tab to open its settings
- Button active state, icons, and labels update on toggle

### Install
1. Download **modern_menu.koplugin-v1.3.0.zip**
2. Extract into your KOReader `plugins/` directory
3. Restart KOReader and enable **Modern Menu**
4. Install [quickmenu.koplugin](https://github.com/jbreizh/quickmenu.koplugin) as well if you want the Quick Menu tab

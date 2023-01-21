<!--
# _______  _______  ______  _______  __      
#|       ||   _   ||   __ \|     __||  |.-----.
#|   -  _||       ||      <|__     ||  ||  _  |
#|_______||___|___||___|__||_______||__||   __|
#                                       |__|   
# QARSlp Qtile + Arch Ricing Script
# By: gibranlp <thisdoesnotwork@gibranlp.dev>
# MIT licence
-->
# QARSlp V2.1.7 Beta

This is a autoricing theme for Qtile, it takes a random wallpaper located at ~/Pictures/Wallpapers and will change the entire system colors to the wallpaper ones.


There are a few functions built  in the  Theme, such as:

- Randomize Wallpaper
  - Alt + r = Set Random wallpaper from (~/Pictures/wallPapers)
  ***
- Change Backend of Pywal (Differente Colors, same Wallpaper)
  - Alt + Shift + r = Change backend Rofi widget.
  - Using thecurrent wallpaper change between the 4 different pywal backends
    - Wal
    - Colorz
    - ColorThief
    - Haishoku
*** 
- Change Theme (Default, Colorful, Topbar, More to Come...)
  - Alt + w = Chnge the theme Rofi widget.
  - Default
    - Top & Bottom semi-transparent bars, 
    - Rofi widgets dark-semi-transparent
  - Colorful
    - Left & Top rounded bars
  - Top Bar
    - Top transparent bar
*All Shortcuts remain the same for all themes.
***

- Rofi Launcher
  - mod + Shift + Return
***
- Rofi Session Menu
  - mod + x
***
- Rofi File / Folders search
  mod + Shift + F
***
- Rofi Web Search based on Surfraw
  - mod + f
***
- Rofi Shortcut viewer
  - mod + h
  - Show Basic Shortcuts for all the system
***
- Rofi Color Picker with Dunst
  - mod + p (Pick a color and get it as a notification HEX & RGB)
***
- Rofi Network menu
  - mod + n
  - Modify the wifi and ethernet connections
***
- Rofi Monitor Modes (Set your resolution and multimonitor setup with ease)
  - mod + Shift + x
  - Set your multimonitor build, fast and easy
***
### Installer
```bash
git clone git@github.com:gibranlp/QARSlp.git
cd QARSlp
chmod +x install.sh
./install.sh
```
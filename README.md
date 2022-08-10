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

This is a autoricing theme for Qtile, it takes a random wallpaper located at ~/Pictures/wallPapers and will change the entire system colors to the wallpaper ones.

There are a few functions built  in the  Theme, such as:

- Randomize Wallpaper
  - Alt + r = Set Random wallpaper from (~/Pictures/wallPapers)
  - ![Rofi Launcher](/gifs/random_wallpaper.gif)
  ***

- Change Backend of Pywal (Differente Colors, same Wallpaper)
  - Alt + Shift + r = Change backend Rofi widget.
  - Using thecurrent wallpaper change between the 4 different pywal backends
    - Wal
    - Colorz
    - ColorThief
    - Haishoku
  ![Rofi Launcher](/gifs/backend.gif)
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
- ![Rofi Launcher](/gifs/theme.gif)
*All Shortcuts remain the same for all themes.
***

- Rofi Launcher
  - mod + Shift + Return
![Rofi Launcher](/gifs/Launcher.gif)
***
- Rofi Session Menu
  - mod + x
![Rofi Launcher](/gifs/session.gif)
***
- Rofi File / Folders search
  mod + Shift + F
  ![Rofi Launcher](/gifs/search.gif)
***
- Rofi Web Search based on Surfraw
  - mod + f
  - ![Rofi Launcher](/gifs/surfraw.gif)
***
- Rofi Shortcut viewer
  - mod + h
  - Show Basic Shortcuts for all the system
![Rofi Launcher](/gifs/shortcuts.gif)
***
- Rofi Color Picker with Dunst
  - mod + p (Pick a color and get it as a notification HEX & RGB)
![Rofi Launcher](/gifs/colors1.gif)
![Rofi Launcher](/gifs/colors2.gif)
***
- Rofi Network menu
  - mod + n
  - Modify the wifi and ethernet connections
![Rofi Launcher](/gifs/network.gif)
***
- Rofi Monitor Modes (Set your resolution and multimonitor setup with ease)
  - mod + Shift + x
  - Set your multimonitor build, fast and easy
![Rofi Launcher](/gifs/monitor_modes.gif)
***
### Installer
[https://github.com/gibranlp/QARSlp](https://github.com/gibranlp/QARSlp)
```bash
git clone git@github.com:gibranlp/QARSlp.git
cd QARSlp/installer
chmod +x installer.sh updater.sh
./installer.sh
# Then Just run updater.sh to make sure  you have the latest version
updater.sh
```
- If you run the QARSlp/installer/installer.sh command, this will install several packages needed for QARSlp to run properly, here is the list of that programs:
  - **Pacman**: 'base-devel' 'alacritty' 'xorg-xkill' 'xcolor' 'xdg-user-dirs' 'bluez' 'bluez-tools' 'blueman' 'htop' 'alsa-utils' 'alsa-lib' 'bc' 'ntfs-3g' 'alsa-firmware' 'playerctl' 'kdeconnect' 'firefox' 'pulseaudio' 'pulseaudio-alsa' 'pavucontrol' 'volumeicon' 'scrot' 'rofi' 'surfraw' 'python-pip' 'pkgfile' 'ranger' 'tumbler' 'feh' 'neofetch' 'lxappearance' 'lxsession' 'numlockx' 'unzip' 'bmon' 'lightdm' 'lm_sensors' 'obconf' 'viewnior' 'ntp' 'nm-connection-editor' 'network-manager-applet' 'arandr' 'cmatrix' 'xarchiver' 'python-pywal' 'python-psutil' 'python-xdg' 'python-iwlib' 'python-dateutil' 'ueberzug' 'xsettingsd' 'otf-ipafont' 'acpi' 'qtile' 'wget' 'cmake' 'tlp' 'zsh' 'texlive-full' 'gvfs' 'dunst'
  - **Pip Packages**: 'fontawesome' 'ipc' 'pywalfox' 'colorz' 'colorthief' 'haishoku' 'dbus-next' 'git+http://github.com/bcbnz/python-rofi.git'
  - **AUR Packages**: 'p7zip' 'unrar' 'openssh' 'farge' 'wpgtk-git' 'nbfc' 'qtile-extras-git' 'thunar-custom-actions' 'thunar-volman' 'thunar-archive-plugin-git' 'thunar-shares-plugin-git' 'picom-ibhagwan-git' 'deepin-screenshot' 'font-manager' 'jmtpfs' 'lightdm-webkit-theme-aether' 'themix-gui-git'


### Know Issues
-  GTK still not working fine
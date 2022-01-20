# QARSlp Qtile Auto Ricing Script v1.1
by: gibranlp [thisdoesnotwork@gibranlp.dev](mailto:thisdoesnotwork@gibranlp.dev)
MIT licence

QARSlp is an integration of tools to create an autoricingand functional desktop based on the Wallpaper. It is made with Qtile, Rofi, Pywal, ZSH based on Arch and lots and lots of love.

To start just ```bash mod + h ``` to view all the things you can do.

Fork / upgrade from [QAAS](https://github.com/gibranlp/QAAS), the  Autoricing feature depends entirely on the Wallpaper, it generates several palettes using pywal and wpgtk to adapt the colors of the entire system to the wallpaper

## Installation

This is based on ![Arch](https://archlinux.org/) so any Arch based distro should work.

In order for QARSlp to run properly needs a lot of sudo permissions, so its a lot better if you add your user to /etc/sudoers

```bash
sudo vim /etc/sudoers
#add at the end of the file
$USER ALL=(ALL) NOPASSWD:All
#where $user = your username
```
### First you need Git & Base-devel

```bash
sudo pacman -S git base-devel
```
### Then clone this repository  & run install.sh

```bash
git clone https://github.com/gibranlp/QARSlp.git
cd QARSlp/installer 
chmod +x install.sh 
```
## This will install:
### Base Packages:
```bash
'htop' 'alsa-utils' 'alsa-lib' 'bc''ntfs-3g' 'alsa-firmware' 'ttf-fira-code' 'ttf-font-awesome' 'playerctl' 'kdeconnect' 'firefox' 'pulseaudio' 'pulseaudio-alsa' 'pavucontrol' 'volumeicon' 'picom' 'scrot' 'rofi' 'surfraw' 'python-pip' 'pkgfile' 'ranger' 'tumbler' 'feh' 'neofetch' 'lxappearance' 'lxsession' 'numlockx' 'unzip' 'bmon' 'dunst' 'lightdm' 'lm_sensors' 'obconf' 'viewnior' 'ntp' 'nm-connection-editor' 'network-manager-applet' 'arandr' 'cmatrix' 'xarchiver' 'python-pywal' 'python-psutil' 'python-xdg' 'python-iwlib' 'python-dateutil' 'ueberzug' 'xsettingsd' 'otf-ipafont' 'acpi' 'qtile' 'wget' 'cmake' 'lightdm-webkit2-greeter' 'tlp'
```
### Pip Packages
```bash
'fontawesome' 'ipc' 'pywalfox' 'colorz' 'colorthief' 'haishoku' 'dbus-next' 'git+http://github.com/bcbnz/python-rofi.git'
```
### AUR Packages

QARSlp will install the AUR Helper [paru](https://github.com/Morganamilo/paru) and this packages
```bash
'p7zip' 'unrar' 'rxvt-unicode' 'wpgtk-git' 'nbfc' 'ncspot' 'qtile-extras-git' 'visual-studio-code-bin' 'thunar-custom-actions' 'thunar-volman' 'thunar-archive-plugin-git' 'thunar-extended' 'thunar-shares-plugin-git'
```
- [x] Packs of wallpapers
  - [x] [Pack 1](https://gibranlp.dev/wallpacks/pack1.tar.gz)
  - [x] [Pack 2](https://gibranlp.dev/wallpacks/pack2.tar.gz)
  - [x] [Pack 3](https://gibranlp.dev/wallpacks/pack3.tar.gz)
  - [x] All the wallpapers should be put on **~/Pictures/wallPapers** This folder is created with the installation.


Once the installer finishes just reboot and you should boot to lightdm QARSlp.

If any error please report it here, i'm creating a better documentation on the develop branch, but that will take some time.



<a href="https://www.buymeacoffee.com/gibranlp"><img src="https://img.buymeacoffee.com/button-api/?text=Buy me a Coffee&emoji=&slug=gibranlp&button_colour=FFDD00&font_colour=000000&font_family=Bree&outline_colour=000000&coffee_colour=ffffff"></a>
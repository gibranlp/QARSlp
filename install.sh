#!/usr/bin/env bash
# _______  _______  ______  _______  __        
#|       ||   _   ||   __ \|     __||  |.-----.
#|   -  _||       ||      <|__     ||  ||  _  |
#|_______||___|___||___|__||_______||__||   __|
#                                       |__|   
# QARSlp Qtile + Arch Ricing System
# By: gibranlp <thisdoesnotwork@gibranlp.dev>
# MIT licence 
#
function base() {
  packets=(
    'base-devel'
    'alsa-utils'
    'pulseaudio-alsa'
    'pavucontrol'
    'openssh'
    'alacritty'
    'xcolor'
    'playerctl'
    'scrot'
    'rofi'
    'surfraw'
    'python-pip'
    'ranger'
    'lxappearance'
    'bmon'
    'lm_sensors'
    'nm-connection-editor'
    'arandr'
    'python-psutil'
    'python-xdg'
    'python-iwlib'
    'python-dateutil'
    'ueberzug'
    'xsettingsd'
    'zsh'
    'dunst'
    'tk'
    'transmission-cli'
    'vlc'
    'kdeconnect'
    'lightdm-gtk-greeter-settings'
    'reflector'
    'rsync'
    'curl'
    'cmus'
    'bc'
    'picom'
    'neofetch'
    'firefox'
    'cmus'
    'xorg-xkill'
    'xdg-user-dirs'
    'bluez'
    'bluez-tools'
    'blueman'
    'htop'
    'os-prober'
    'gnome-disk-utility'
    'networkmanager'
    'unzip'
    'xarchiver'
    'tlp'
    'gvfs'
    'barrier'
    'noto-fonts'
    'noto-fonts-cjk'
    'ttf-dejavu'
    'ttf-liberation'
    'ttf-opensans'
    'libayatana-appindicator'
    'tlp'
    'powertop'
    'tumbler'
    'redshift'
    'libmicrodns' # Libraries for vlc and Chromecast
    'protobuf' # Libraries for vlc and Chromecast
    'linux-headers'
    'linux-docs'
    'linux-lts'
    'linux-lts-headers'
    #'nvidia-dkms'
    

)

for packet in "${packets[@]}"; do
    echo "Instalando --> ${packet}"
    sudo pacman -S "${packet}" --noconfirm --needed
done
}

function paru_install(){
  git clone https://aur.archlinux.org/paru.git 
  cd paru 
  makepkg -si --noconfirm
  cd ..
  rm -rf paru
} 

function aur_packages() {
  packets=(
    'farge'
    'python-pywalfox'
    'qtile-extras-git'
    'caffeine-ng'
    'qtile-git'
    'visual-studio-code-bin'
    'slack-desktop'
    'teams-for-linux'
    'telegram-desktop'
    'google-chrome'
    'wpgtk-git'
    'cava'
    'thunar-extended'
    'thunar-volman'
    'hugo'
    'nbfc'
    'ntfs-3g'
    'cava'
    'nativefier-freedesktop-git'

)
for packet in "${packets[@]}"; do
    echo "Instalando --> ${packet}"
    paru -S "${packet}" --noconfirm
done
}

function zsh(){
    sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended
    git clone https://github.com/zsh-users/zsh-autosuggestions.git ~/.oh-my-zsh/plugins/zsh-autosuggestions
    git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ~/.oh-my-zsh/plugins/zsh-syntax-highlighting
}

function copy_dotfiles(){
  mkdir -p ~/.config/alacritty
  cp ~/QARSlp/dotfiles/.config/alacritty/alacritty.yml ~/.config/alacritty/alacritty.yml
  cp ~/QARSlp/dotfiles/.shortcuts ~/
  mkdir -p ~/.config/wal/templates
  mkdir -p ~/.config/dunst
  cp ~/QARSlp/dotfiles/.config/dunst/dunstrc ~/.config/wal/templates
  mkdir -p ~/.config/cava
  cp ~/QARSlp/dotfiles/.config/cava/config ~/.config/wal/templates
  mkdir -p  ~/.fonts
  cp ~/QARSlp/dotfiles/fonts/otf/* ~/.fonts
  cp ~/QARSlp/dotfiles/fonts/ttf/* ~/.fonts
  fc-cache -f -v
  mkdir -p ~/.config/picom
  cp ~/QARSlp/dotfiles/.config/picom/picom.conf ~/.config/picom/picom.conf
  mkdir -p ~/.config/qtile
  cp ~/QARSlp/dotfiles/.config/qtile/themes/default.py ~/.config/qtile/theme.py
  cp -r ~/QARSlp/dotfiles/.config/qtile/* ~/.config/qtile/
  mkdir -p ~/.config/ranger
  cp ~/QARSlp/dotfiles/.config/ranger/rc.conf ~/.config/ranger/rc.conf
  mkdir -p ~/.config/rofi
  cp -r ~/QARSlp/dotfiles/.config/rofi/* ~/.config/rofi/
  sudo mkdir -p /root/.config/rofi
  sudo cp -r ~/QARSlp/dotfiles/.config/rofi/* /root/.config/rofi/
  sudo mkdir -p /root/.cache/wal
  sudo cp -r ~/.cache/wal/colors-rofi-dark.rasi /root/.cache/wal/
  sudo timedatectl set-ntp true
  xdg-settings set default-web-browser firefox.desktop 
  mkdir -p ~/.local/bin
  cp -r ~/QARSlp/dotfiles/.local/bin/* ~/.local/bin
  chmod +x ~/.local/bin/*
  cp ~/QARSlp/dotfiles/.zshrc ~/
  mkdir -p ~/.oh-my-zsh
  cp ~/QARSlp/dotfiles/.oh-my-zsh/themes/* ~/.oh-my-zsh/themes/
  mkdir ~/Pictures
  sudo mkdir -p /usr/share/backgrounds
  mkdir -p ~/Pictures/Wallpapers
  cp -r ~/QARSlp/Wallpapers/* ~/Pictures/Wallpapers
  sudo mkdir -p /usr/share/FlatColor 
}

function web_apps(){
  mkdir -p ~/WebApps
  cd ~/WebApps
  nativefier https://github.com/ --name github --single-instance --tray
  nativefier https://www.primevideo.com/ --name prime --single-instance --windevine --tray
  nativefier https://drive.google.com/drive/shared-drives --name drive --single-instance --tray
  nativefier https://www.figma.com/files/recent?fuid=1177005402390460721 --name figma --single-instance --tray
  nativefier https://admin.google.com/?rapt=AEjHL4N0yGwzCoucouWtW0MKQj6kYhIIfkadjCaxgZTjhnUCSuKHDVoVPYARCWt1YOfZ542j11diwR4Td8HEVfzHv_vT509KMg --name admin --single-instance --tray
  nativefier https://calendar.google.com/calendar/u/0/r?pli=1 --name calendar --single-instance --tray
  nativefier https://www.notion.so/helgen/ --name notion --single-instance --tray
  nativefier https://www.overleaf.com/project --name overleaf --single-instance --tray
  nativefier https://meet.google.com/ --name meet --single-instance --tray

  sudo ln -s ~/WebApps/PrimeVideo/WelcometoPrimeVideo /usr/bin/prime
  sudo ln -s ~/WebApps/Drive/Drive /usr/bin/drive
  sudo ln -s ~/WebApps/GoogleAdmin/GoogleAdmin /usr/bin/admin
  sudo ln -s ~/WebApps/GoogleCalendar/GoogleCalendar /usr/bin/Calendar
  sudo ln -s ~/WebApps/Notion/Notion /usr/bin/Notion
  sudo ln -s ~/WebApps/Overleaf/Overleaf /usr/bin/overleaf
  sudo ln -s ~/WebApps/Figma/Figma /usr/bin/Figma
  sudo ln -s ~/WebApps/meet/meet /usr/bin/meet
  sudo ln -s ~/WebApps/github/github /usr/bin/github
}

function post(){
  timedatectl set-local-rtc 1
  timedatectl set-timezone America/Mexico_City
  sudo systemctl enable bluetooth.service
  sudo systemctl start bluetooth.service
  sudo systemctl enable sshd.service
  sudo systemctl start sshd.service
  sudo systemctl enable tlp.service
  journalctl --vacuum-size=100M
  journalctl --vacuum-time=2weeks
  wpg-install.sh -gio
  ~/.local/bin/genwal
  pywalfox install
  pywalfox start
}
sudo pacman -Syyu --noconfirm
base
paru_install
#sudo pacman -Rcns qtile thunar --noconfirm
#aur_packages
pip install -r pip.txt
zsh
copy_dotfiles
#web_apps
#post
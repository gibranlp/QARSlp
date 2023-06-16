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
    'feh'
    'unclutter'
    'fuse-exfat'
    'base-devel'
    'alsa-utils'
    'pulseaudio-alsa'
    'pulseaudio-bluethooth'
    'pavucontrol'
    'openssh'
    'alacritty'
    'xcolor'
    'playerctl'
    'scrot'
    'flameshot'
    'rofi'
    'surfraw'
    'python-pip'
    'ranger'
    'lxappearance'
    'bmon'
    'acpilight'
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
    'neofetch'
    #'firefox'
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
    'linux'
    'linux-headers'
    'linux-docs'
    'linux-lts'
    'linux-lts-headers'
    'xorg-xdpyinfo'
    'taskwarrior-tui'
    'fzf'
    'thefuck'
    'pamixer'
    'gvfs-mtp' 
    'gvfs-nfs'
    'gvfs-smb'
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
    'qtile-git'
    'farge'
    #'python-pywalfox' # If you install firefox you will need  this
    'qtile-extras-git'
    'caffeine-ng-git'
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
    'i3lock-fancy'
    'wal-telegram-git'
    'picom-pijulius-git'
    'lazy-docker'
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
  cp ~/QARSlp/dotfiles/.config/rofi/QARSlp.rasi ~/.config/wal/templates
  mkdir -p ~/.config/cava
  cp ~/QARSlp/dotfiles/.config/cava/config ~/.config/wal/templates
  mkdir -p ~/.config/ncspot
  cp ~/QARSlp/dotfiles/.config/ncspot/config.toml ~/.config/ncspot/config.toml
  mkdir -p  ~/.fonts
  cp ~/QARSlp/dotfiles/.fonts/* ~/.fonts
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
  sudo cp ~/QARSlp/Wallpapers/wall.jpg /usr/local/backgrounds/background.png
  sudo mkdir -p /usr/local/themes
  sudo cp -r ~/.local/share/themes/FlatColor /usr/local/themes
  sudo chown $USER:$USER /usr/local/themes/FlatColor
  sudo ln -s /usr/local/themes/FlatColor /usr/share/themes/FlatColor
  sudo mkdir /usr/local/backgrounds
  sudo chown $USER:$USER /usr/local/backgrounds
  sudo cp ~/QARSlp/dotfiles/lightdm-gtk-greeter.conf /etc/lightdm/lightdm-gtk-greeter.conf
  sudo cp ~QARSlp/pulse/system.pa /etc/pulse/system.pa
}

function web_apps(){

  mkdir -p ~/Apps
  cd ~/Apps
  nativefier https://github.com/ --name github --single-instance 
  nativefier https://www.primevideo.com/ --name prime --single-instance --windevine 
  nativefier https://drive.google.com/drive/shared-drives --name drive --single-instance 
  nativefier https://www.figma.com/files/recent?fuid=1177005402390460721 --name figma --single-instance 
  nativefier https://admin.google.com/?rapt=AEjHL4N0yGwzCoucouWtW0MKQj6kYhIIfkadjCaxgZTjhnUCSuKHDVoVPYARCWt1YOfZ542j11diwR4Td8HEVfzHv_vT509KMg --name admin --single-instance 
  nativefier https://calendar.google.com/calendar/u/0/r?pli=1 --name calendar --single-instance 
  nativefier https://www.notion.so/helgen/00-Helgen-Ltd-42570ee0ace34d19b7d0a91955b7d976--name notion --single-instance 
  nativefier https://www.overleaf.com/project --name overleaf --single-instance 
  nativefier https://meet.google.com/ --name meet --single-instance 
  nativefier https://app.clockify.me/tracker# --name clockify --single-instance 
  nativefier https://admin.microsoft.com/Adminportal/Home#/homepage --name madmin --single-instance 

  sudo ln -s ~/Apps/PrimeVideo/WelcometoPrimeVideo /usr/bin/prime
  sudo ln -s ~/Apps/drive/drive /usr/bin/drive
  sudo ln -s ~/Apps/admin/admin /usr/bin/admin
  sudo ln -s ~/Apps/calendar/calendar /usr/bin/calendar
  sudo ln -s ~/Apps/notion/notion /usr/bin/notion
  sudo ln -s ~/Apps/overleaf/overleaf /usr/bin/overleaf
  sudo ln -s ~/Apps/figma/figma /usr/bin/figma
  sudo ln -s ~/Apps/meet/meet /usr/bin/meet
  sudo ln -s ~/Apps/github/github /usr/bin/github
  sudo ln -s ~/Apps/clockify/clockify /usr/bin/clockify
  wpg-install.sh -gio
  ~/.local/bin/genwal
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
  
}
#sudo pacman -Syyu --noconfirm
#base
#paru_install
#sudo pacman -Rcns qtile thunar --noconfirm
#aur_packages
#pip install -r pip.txt
#zsh
#copy_dotfiles
#web_apps
#post
update

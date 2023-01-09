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

function paru(){
  git clone https://aur.archlinux.org/paru.git 
  cd paru 
  makepkg -si --noconfirm
  cd ..
  rm -rf paru
} 

function pip3(){
  pip_packets=(
    'requests'
    'fontawesome'
    'ipc'
    'colorz'
    'colorthief'
    'haishoku'
    'dbus-next'
    'git+http://github.com/bcbnz/python-rofi.git'
  )

for pip_packet in "${pip_packets[@]}"; do
  echo "Instalando --> ${pip_packet}"
  pip install "${pip_packet}"
done
}


function aur () {
  packets=(
    'qtile-git'
    'farge'
    'python-pywalfox'
    'qtile-extras-git'
    'caffeine-ng'
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
  \cp -r ~/QARSlp/dotfiles/.[^.]* ~/
  sudo \cp -r ~/QARSlp/dotfiles/.[^.]* /root
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
#sudo pacman -Syyu
#base
#paru
#aur
pip install -r pip.txt
zsh
copy_dotfiles
web_apps
post
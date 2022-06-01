#!/usr/bin/env bash
# _______  _______  ______  _______  __        
#|       ||   _   ||   __ \|     __||  |.-----.
#|   -  _||       ||      <|__     ||  ||  _  |
#|_______||___|___||___|__||_______||__||   __|
#                                       |__|   
# QARSlp Qtile + Arch Ricing Script
# by: gibranlp <thisdoesnotwork@gibranlp.dev>
# MIT licence 
# 
## Apps
function i_zsh(){
    sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended
    git clone https://github.com/zsh-users/zsh-autosuggestions.git ~/.oh-my-zsh/plugins/zsh-autosuggestions
    git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ~/.oh-my-zsh/plugins/zsh-syntax-highlighting
}

function i_paru(){
  git clone https://aur.archlinux.org/paru.git
  cd paru
  makepkg -sri --noconfirm
  cd ..
  rm -rf paru
}

function i_base () {
  packets=('base-devel' 'htop' 'alsa-utils' 'alsa-lib' 'bc' 'ntfs-3g' 'alsa-firmware' 'playerctl' 'kdeconnect' 'firefox' 'pulseaudio' 'pulseaudio-alsa' 'pavucontrol' 'volumeicon' 'scrot' 'rofi' 'surfraw' 'python-pip' 'pkgfile' 'ranger' 'tumbler' 'feh' 'neofetch' 'lxappearance' 'lxsession' 'numlockx' 'unzip' 'bmon' 'dunst' 'lightdm' 'lm_sensors' 'obconf' 'viewnior' 'ntp' 'nm-connection-editor' 'network-manager-applet' 'arandr' 'cmatrix' 'xarchiver' 'python-pywal' 'python-psutil' 'python-xdg' 'python-iwlib' 'python-dateutil' 'ueberzug' 'xsettingsd' 'otf-ipafont' 'acpi' 'qtile' 'wget' 'cmake' 'lightdm-webkit2-greeter' 'tlp' 'zsh' 'texlive-full' 'nvidia-dkms'
)

for packet in "${packets[@]}"; do
    echo "Instalando --> ${packet}"
    sudo pacman -S "${packet}" --noconfirm --needed
done
}

function i_pip(){
  pip_packets=(
    'fontawesome'
    'ipc'
    'pywalfox'
    'colorz'
    'colorthief'
    'haishoku'
    'dbus-next'
    'git+http://github.com/bcbnz/python-rofi.git'
   
  )

  for pip_packet in "${pip_packets[@]}"; do
    echo "Instalando --> ${pip_packet}"
    sudo pip install "${pip_packet}"
  done
}

function i_aur () {
  packets=(
    'p7zip' 'unrar' 'rxvt-unicode' 'wpgtk-git' 'nbfc' 'ncspot' 'qtile-extras-git' 'visual-studio-code-bin' 'thunar-custom-actions' 'thunar-volman' 'thunar-archive-plugin-git' 'thunar-extended' 'thunar-shares-plugin-git' 'picom-ibhagwan-git' 'deepin-screenshot' 'google-chrome' 'slack-desktop' 'hugo' 'whatsdesk-bin' 'telegram-desktop' 'owncloud-client' 'font-manager'

)


for packet in "${packets[@]}"; do
    echo "Instalando --> ${packet}"
    paru -S "${packet}" --noconfirm
done
}

function i_settings(){
  sudo timedatectl set-timezone America/Mexico_City &
  sudo timedatectl set-ntp true &
  pywalfox install &
  git clone https://github.com/zsh-users/zsh-autosuggestions.git ~/.oh-my-zsh/plugins/zsh-autosuggestions &
  git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ~/.oh-my-zsh/plugins/zsh-syntax-highlighting &
  wpg-install.sh -g -d -i &
  ~/.local/bin/autostart &
  ~/.local/bin/alwaystart &
  
}

function i_files(){
\cp -r ~/QARSlp/dotfiles/.[^.]* ~/ 
sudo \cp -r ~/QARSlp/dotfiles/.[^.]* /root 
\cp -r ~/QARSlp/dotfiles/.config/qtile/themes/default/wallPapers ~/Pictures 
sudo \cp -r  ~/QARSlp/scripts/* /usr/local/bin 
sudo chmod +x ~/.local/bin/*
sudo \cp -r ~/QARSlp/lightdm/* /etc/lightdm
sudo \cp -r ~/QARSlp/lightdm-webkit /usr/share
mkdir ~/.local/bin
}

i_base
i_paru
i_aur
i_zsh
i_pip
i_settings
i_files



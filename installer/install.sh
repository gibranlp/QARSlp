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
  packets=('base-devel' 'alacritty' 'xorg-xkill' 'vlc' 'xcolor' 'xdg-user-dirs' 'bluez' 'bluez-tools' 'blueman' 'gnome-disk-utility' 'htop' 'alsa-utils' 'alsa-lib' 'bc' 'ntfs-3g' 'alsa-firmware' 'playerctl' 'kdeconnect' 'firefox' 'pulseaudio' 'pulseaudio-alsa' 'pavucontrol' 'volumeicon' 'scrot' 'rofi' 'surfraw' 'python-pip' 'pkgfile' 'ranger' 'tumbler' 'feh' 'neofetch' 'lxappearance' 'lxsession' 'numlockx' 'unzip' 'bmon' 'lightdm' 'lm_sensors' 'obconf' 'viewnior' 'ntp' 'nm-connection-editor' 'network-manager-applet' 'arandr' 'cmatrix' 'xarchiver' 'python-pywal' 'python-psutil' 'python-xdg' 'python-iwlib' 'python-dateutil' 'ueberzug' 'xsettingsd' 'otf-ipafont' 'acpi' 'qtile' 'wget' 'cmake' 'tlp' 'zsh' 'texlive-full' 'nvidia-dkms' 'gvfs' 'dunst'
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
    pip install "${pip_packet}"
  done
}

function i_aur () {
  packets=(
    'p7zip' 'unrar' 'thunderbird-bin' 'openssh' 'farge' 'wpgtk-git' 'nbfc' 'qtile-extras-git' 'visual-studio-code-bin' 'thunar-custom-actions' 'thunar-volman' 'thunar-archive-plugin-git' 'thunar-extended' 'thunar-shares-plugin-git' 'picom-ibhagwan-git' 'deepin-screenshot' 'google-chrome' 'slack-desktop' 'hugo' 'whatsdesk-bin' 'telegram-desktop' 'owncloud-client' 'font-manager' 'thunar-extended' 'jmtpfs' 'lightdm-webkit-theme-aether' 'themix-gui-git'

)

for packet in "${packets[@]}"; do
    echo "Instalando --> ${packet}"
    paru -S "${packet}" --noconfirm
done
}

function i_settings(){
  sudo timedatectl set-ntp true &
  pywalfox install &
  git clone https://github.com/zsh-users/zsh-autosuggestions.git ~/.oh-my-zsh/plugins/zsh-autosuggestions &
  git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ~/.oh-my-zsh/plugins/zsh-syntax-highlighting &
  wpg-install.sh -g -d -i &
  mkdr ~/.config/dunst &
  xdg-settings set default-web-browser librewolf.desktop &
  mkdir ~/.config/dunst &
  mkdir ~/.config/rofi &
  mkdir ~/Pictures/wallPapers &
  mkdir ~/.local/bin &
  cp ~/QARSlp/walls/wal.png ~/Pictures/wallPapers
  
}

function i_files(){
\cp -r ~/QARSlp/dotfiles/.[^.]* ~/ 
#sudo \cp -r ~/QARSlp/dotfiles/.[^.]* /root 
sudo \cp -r  ~/QARSlp/scripts/* ~/.local/bin/
sudo chmod +x ~/.local/bin/*
#sudo \cp ~/QARSlp/installer/etc/X11/xorg.conf.d/30-touchpad.conf /etc/X11/xorg.conf.d/30-touchpad.conf
sudo cp ~/QARSlp/fonts/otf/* /usr/share/fonts/OTF/
sudo cp ~/QARSlp/fonts/ttf/* /usr/share/fonts/TTF/
sudo \cp -r ~/QARSlp/lightdm/* /etc/lightdm
sudo \cp -r ~/QARSlp/lightdm-webkit /usr/share
cp ~/QARSlp/dotfiles/.config/wal/* ~/.config/wal/templates/
}

i_base
i_paru
i_pip
i_zsh
i_aur
i_settings
i_files



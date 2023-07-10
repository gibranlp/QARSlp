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
function install_new_packages() {
  packets=(
   'xclip'
   'xdotool'
   'noto-fonts-emoji'
   'unclutter'
   'flameshot'
   'bluez-utils'
   'ripgrep'
   'noto-fonts-emoji'
   'fzf'
  'cups'
  'thefuck'
  'pamixer'
  'exa'
  'xclip'
  'xdotool'
  'man'
)

for packet in "${packets[@]}"; do
    echo "Instalando --> ${packet}"
    sudo pacman -S "${packet}" --noconfirm --needed
done
}

function aur_packages() {
  packets=(
    'rofi-emoji'
    'insect'
    'gromit-mpx-git'
    'i3lock-fancy'
    'zathura-pdf-mupdf' 
    'zathura-pywal-git'
    'zathura-ps'
    'libby-git'
    'python-rofi-git'
)
for packet in "${packets[@]}"; do
    echo "Instalando --> ${packet}"
    paru -S "${packet}" --noconfirm
done
}

function update(){
  cp -r ~/QARSlp/dotfiles/.config/rofi/* ~/.config/rofi/
  cp -r ~/QARSlp/dotfiles/.config/qtile/* ~/.config/qtile/
  cp ~/QARSlp/dotfiles/.shortcuts ~/
  cp -r ~/QARSlp/dotfiles/.local/bin/recorder ~/.local/bin/
  cp -r ~/QARSlp/dotfiles/.local/bin/notesfi ~/.local/bin/
  chmod +x ~/.local/bin/*
  cp ~/QARSlp/dotfiles/.shortcuts ~/
  
  cp ~/QARSlp/dotfiles/.config/picom/picom.conf ~/.config/picom/picom.conf
  cp ~/QARSlp/dotfiles/.zshrc ~/
  cp ~/QARSlp/dotfiles/.config/dunst/dunstrc ~/.config/wal/templates
  cp ~/QARSlp/dotfiles/.config/cava/config ~/.config/wal/templates
  cp ~/QARSlp/dotfiles/.config/ranger/rc.conf ~/.config/ranger/rc.conf
  cp ~/QARSlp/dotfiles/.config/alacritty/alacritty.yml ~/.config/alacritty/alacritty.yml
  cp ~/QARSlp/dotfiles/.config/gromit-mpx.ini ~/.config
  cp ~/QARSlp/dotfiles/.oh-my-zsh/themes/avit.zsh-theme ~/.oh-my-zsh/themes
}

#install_new_packages
#aur_packages
update
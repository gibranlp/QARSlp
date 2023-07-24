#!/usr/bin/env bash
# _______  _______  ______  _______  __        
#|       ||   _   ||   __ \|     __||  |.-----.
#|   -  _||       ||      <|__     ||  ||  _  |
#|_______||___|___||___|__||_______||__||   __|
#                                       |__|   
# SpectrumOS - Embrace the Chromatic Symphony!
# By: gibranlp <thisdoesnotwork@gibranlp.dev>
# MIT licence 
#

function install_new_packages() {
  packets=(
)

for packet in "${packets[@]}"; do
    echo "Instalando --> ${packet}"
    sudo pacman -S "${packet}" --noconfirm --needed
done
}

function aur_packages() {
  packets=(
    'rofi-file-browser-extended-git'
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
  # cp -r ~/QARSlp/dotfiles/.local/bin/recorder ~/.local/bin/
  cp -r ~/QARSlp/dotfiles/.local/bin/notesfi ~/.local/bin/
  cp -r ~/QARSlp/dotfiles/.local/bin/wifi2 ~/.local/bin/
  cp -r ~/QARSlp/dotfiles/.local/bin/recorder ~/.local/bin/
  cp -r ~/QARSlp/dotfiles/.local/bin/selectwal ~/.local/bin/
  cp -r ~/QARSlp/dotfiles/.local/bin/calculator ~/.local/bin/
  cp -r ~/QARSlp/dotfiles/.local/bin/calendar ~/.local/bin/
  cp -r ~/QARSlp/dotfiles/.local/bin/change_display ~/.local/bin/
  cp -r ~/QARSlp/dotfiles/.local/bin/autostart ~/.local/bin/
  cp -r ~/QARSlp/dotfiles/.local/bin/alwaystart ~/.local/bin/
  cp -r ~/QARSlp/dotfiles/.local/bin/bluet ~/.local/bin/
  cp -r ~/QARSlp/dotfiles/.local/bin/genwal ~/.local/bin/
  cp -r ~/QARSlp/dotfiles/.local/bin/cleansys ~/.local/bin/
  chmod +x ~/.local/bin/*
  # cp ~/QARSlp/dotfiles/.shortcuts ~/
  
  cp ~/QARSlp/dotfiles/.config/picom/picom.conf ~/.config/picom/picom.conf
  cp ~/QARSlp/dotfiles/.zshrc ~/
  cp ~/QARSlp/dotfiles/.config/dunst/dunstrc ~/.config/wal/templates
  cp ~/QARSlp/dotfiles/.config/flameshot/flameshot.ini ~/.config/wal/templates
  # cp ~/QARSlp/dotfiles/.config/cava/config ~/.config/wal/templates
  # cp ~/QARSlp/dotfiles/.config/ranger/rc.conf ~/.config/ranger/rc.conf
  # cp ~/QARSlp/dotfiles/.config/alacritty/alacritty.yml ~/.config/alacritty/alacritty.yml
  # cp ~/QARSlp/dotfiles/.config/gromit-mpx.ini ~/.config
  cp ~/QARSlp/dotfiles/.oh-my-zsh/themes/avit.zsh-theme ~/.oh-my-zsh/themes
}

#install_new_packages
#aur_packages
update
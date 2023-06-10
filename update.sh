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

function update(){
  cp -r ~/QARSlp/dotfiles/.config/qtile/* ~/.config/qtile/
  cp ~/QARSlp/dotfiles/.shortcuts ~/
  cp ~/QARSlp/dotfiles/.config/picom/picom.conf ~/.config/picom/picom.conf
  cp ~/QARSlp/dotfiles/.zshrc ~/
  mkdir -p ~/.config/ncspot
  cp ~/QARSlp/dotfiles/.config/ncspot/config.toml ~/.config/ncspot/config.toml
}

update
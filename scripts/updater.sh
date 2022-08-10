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


function i_gen_update(){
  cd ~/QARSlp &&
  git pull &&
~/QARSlp/installer/./cp_files &&
~/.local/bin/genwal
}

i_gen_update &&
dunstify "You have been updated to version 2.1.7 Beta"

# _______  _______  ______  _______  __        
#|       ||   _   ||   __ \|     __||  |.-----.
#|   -  _||       ||      <|__     ||  ||  _  |
#|_______||___|___||___|__||_______||__||   __|
#                                       |__|   
# QARSlp Qtile + Arch Ricing Script
# By: gibranlp <thisdoesnotwork@gibranlp.dev>
# MIT licence 

import os, re
import socket, random, requests
import subprocess, json
from os.path import expanduser
from subprocess import run
from libqtile import qtile, hook, layout, bar, widget
from libqtile.config import Screen, Key, Drag, Click, Group, Match
from libqtile.command import lazy
from rofi import Rofi
from qtile_extras import widget

### Variables ####
ver = ' QARSlp v2.0.1' # Current version
mod = "mod4" # Command / Windows key
alt = "mod1" # Alt key                  
term = "urxvt" # Terminal in use
home = os.path.expanduser('~')
prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

#### Resolution ####
main_font = "Fira Code Medium" # Font in use for the entire system
fontsz = 20
iconsz = 19

#### Music / Media ####
scrollchar = 50
scrollint = 0.1
scrollwint = 4000


#### Internet Chekup ####
internet = ' Internet is working'

#### Themes ####
theme=['default', 'top_bar', 'bottom_bar', 'minimal', 'alpha', 'simple']
backend = ["Wal", "Colorz", "Colorthief","Haishoku"]
rofi_l = Rofi(rofi_args=['-theme', '~/.config/rofi/left_toolbar.rasi'])
rofi_r = Rofi(rofi_args=['-theme', '~/.config/rofi/right_toolbar.rasi'])

#### Resolution ####



#### Weather ####
w_appkey = "e45a0f07f0c675b273ef8636663941db" # 
w_cityid = "3995402" #City id find it here


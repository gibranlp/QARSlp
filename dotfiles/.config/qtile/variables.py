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
ver = ' QARSlp v2.1.34Beta' # Current version
mod = "mod4" # Command / Windows key
alt = "mod1" # Alt key                  
term = "urxvt" # Terminal in use
home = os.path.expanduser('~')
prompt = ":".format(os.environ["USER"], socket.gethostname())

#### Resolution fix ####
main_font = "Fira Code Medium" # Font in use for the entire system
awesome_font = "Font Awesome 6 Pro Solid"
fontsz = 22
 #Font size for bars
iconsz = 20 #Icon size for bars
lfontsz = 17 # Layout font size
lmargin = 7 # Layout margins
lborderwd = 3 # Layout border width

#### Bars ####
barsz = 32 # bar size
bar_top_width = [0,0,0,0] # bar borders top
bar_bot_width = [0,0,0,0] # bar borders top
bar_opa = 0.99

transparency = "95" #Overall Transparency

#### Music / Media ####
scrollchar = 50
scrollint = 1
scrollwint = 500
### Gaps
#### Internet Chekup ####
internet = ' Internet is working'
#### Themes ####
theme=['default', 'top_bar', 'bottom_bar', 'minimal', 'alpha', 'simple']
backend = ["Wal", "Colorz", "Colorthief","Haishoku"]
rofi_l = Rofi(rofi_args=['-theme', '~/.config/rofi/left_toolbar.rasi'])
rofi_r = Rofi(rofi_args=['-theme', '~/.config/rofi/right_toolbar.rasi'])
rofi_session = Rofi(rofi_args=['-theme', '~/.config/rofi/logout.rasi'])
rofi_display = Rofi(rofi_args=['-theme', '~/.config/rofi/display.rasi'])
rofi_network= Rofi(rofi_args=['-theme', '~/.config/rofi/network.rasi'])
rofi_backend= Rofi(rofi_args=['-theme', '~/.config/rofi/backend.rasi'])
rofi_websearch= Rofi(rofi_args=['-theme', '~/.config/rofi/websearch.rasi'])
rofi_screenshot= Rofi(rofi_args=['-theme', '~/.config/rofi/screenshot.rasi'])
#### Resolution ####

#### Weather ####
w_appkey = "e45a0f07f0c675b273ef8636663941db" # 
w_cityid = "3995402" #City id find it here


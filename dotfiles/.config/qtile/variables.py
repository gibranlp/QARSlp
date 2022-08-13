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
from libqtile import qtile, hook, layout, bar
from libqtile.config import Screen, Key, Drag, Click, Group, Match, ScratchPad, DropDown
from qtile_extras.widget.decorations import RectDecoration
from qtile_extras import widget
from libqtile.widget import TextBox
from qtile_extras.widget.mixins import TooltipMixin

from libqtile.command import lazy
from rofi import Rofi
from qtile_extras import widget

### Variables ####
main_font = "Fira Code Medium" # Font in use for the entire system
awesome_font = "Font Awesome 6 Pro Solid"
#### Resolution ####
resolution = "4k" # 4k 3460 x 2560 or Fullhd 1920 x 1080
ver = 'QARSlp  v2.1.7' # Current version
#### Keys ####
mod = "mod4" # Command / Windows key
alt = "mod1" # Alt key                  

term = "alacritty" # Terminal in use
home = os.path.expanduser('~') # Path for use in folders
prompt = ":".format(os.environ["USER"], socket.gethostname()) # Format of the prompt

#### Groups ####
group_names = ["1","2","3","4","5","6","7","8","9"]
group_labels=["","","","","","","","",""]
group_layouts=["monadtall", "monadthreecol", "matrix","monadtall", "monadtall", "monadthreecol","monadthreecol", "monadtall", "monadtall"]
group_matches=[
  [Match(wm_class=[])],
  [Match(wm_class=[])],
  [Match(wm_class=[])],
  [Match(wm_class=[])],
  [Match(wm_class=[])],
  [Match(wm_class=[])],
  [Match(wm_class=[])],
  [Match(wm_class=[])],
  [Match(wm_class=[])],]

#### Music / Media ####
scrollchar = 50
scrollint = 1
scrollwint = 200

### Gaps
#### Internet Chekup ####
internet = ' Internet is working'
#### Themes ####
theme=['colorful','blur', 'minimal_top_bar_D','color1']
backend = ['Wal', 'Colorz', 'Colorthief','Haishoku']
defaultBackend= "Wal"
rofi_session = Rofi(rofi_args=['-theme', '~/.config/rofi/logout.rasi'])
rofi_display = Rofi(rofi_args=['-theme', '~/.config/rofi/display.rasi'])
rofi_network= Rofi(rofi_args=['-theme', '~/.config/rofi/network.rasi'])
rofi_backend= Rofi(rofi_args=['-theme', '~/.config/rofi/backend.rasi'])
rofi_websearch= Rofi(rofi_args=['-theme', '~/.config/rofi/websearch.rasi'])
rofi_screenshot= Rofi(rofi_args=['-theme', '~/.config/rofi/screenshot.rasi'])
rofi_fargewidget= Rofi(rofi_args=['-theme', '~/.config/rofi/fargewidget.rasi'])
#### Resolution ####

#### Weather ####
w_appkey = "e45a0f07f0c675b273ef8636663941db" # 
w_cityid ="3995402" # "3995402" Morelia, "3521342" Playa del Carmen, "3520914" Querétaro, "3514783" Veracruz
# https://openweathermap.org/city/
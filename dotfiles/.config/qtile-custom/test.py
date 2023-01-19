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
from libqtile.command import lazy
from rofi import Rofi
from qtile_extras import widget

subprocess.run(["cp", "%s" % rand_wallpaper, hom + "/Pictures/Wallpapers/current.png" ])
# By: gibranlp <thisdoesnotwork@gibranlp.dev>
# MIT licence
# Qtile Config

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

# Variables

## Version
ver = 'v2.0' # Current dotfiles version

## Fonts
m_font = "Fira Code Medium" # Font in use for the entire system
a_font = "Font Awesome 6 Pro Solid" # Font for all the Special Characters

## Keys ####
mod = "mod4" # Super / Command / Windows key
alt = "mod1" # Alt key

## Software
term = "alacritty" # Terminal in use

## System
home = os.path.expanduser('~') # Path for use in folders
prompt = ":".format(os.environ["USER"], socket.gethostname()) # Format of the prompt

## Theming
def_Backend= "wal"
theme=['default.py', 'colors.py'] # Themes available
backend=['Wal', 'Colorz', 'Colorthief','Haishoku'] #Backends available


## Margins and Borders
l_margin = 5 # Layout margins
sl_margin = 5 # Single window margin 
l_border_w = 3 # Layout border width
s_border_w = 3 # Single border width

## Theming

rofi_session = Rofi(rofi_args=['-theme', '~/.config/rofi/logout.rasi'])
rofi_display = Rofi(rofi_args=['-theme', '~/.config/rofi/display.rasi'])
rofi_network= Rofi(rofi_args=['-theme', '~/.config/rofi/network.rasi'])
rofi_backend= Rofi(rofi_args=['-theme', '~/.config/rofi/backend.rasi'])
rofi_websearch= Rofi(rofi_args=['-theme', '~/.config/rofi/websearch.rasi'])
rofi_screenshot= Rofi(rofi_args=['-theme', '~/.config/rofi/screenshot.rasi'])
rofi_fargewidget= Rofi(rofi_args=['-theme', '~/.config/rofi/fargewidget.rasi'])


## Widgets
### Weather
w_appkey = "e45a0f07f0c675b273ef8636663941db" # Get a key here https://home.openweathermap.org/users/sign_up 
w_cityid ="3995402" # "3995402" Morelia, "3521342" Playa del Carmen https://openweathermap.org/city/

########################################################################################

# Functions
groups = []
## Hooks
@hook.subscribe.startup # This file gets executed everytime qtile restarts
def start():
  subprocess.call(home + '/.local/bin/alwaystart')
      
@hook.subscribe.startup_once # Ths fle gets executed at first start only
def start_once():
  subprocess.call(home + '/.local/bin/autostart')

@hook.subscribe.client_new
def follow_window(client):
  for group in groups:
    match = next((m for m in group.matches if m.compare(client)), None)
    if match:
      targetgroup = qtile.groups_map[group.name]
      targetgroup.cmd_toscreen(toggle=False)
      break

@hook.subscribe.client_name_updated
def follow_window_name(client):
  for group in groups:
    match = next((m for m in group.matches if m.compare(client)), None)
    if match:
      targetgroup = qtile.groups_map[group.name]
      targetgroup.cmd_toscreen(toggle=False)
      break

##Specific Apps/Groups
def app_or_group(group, app):
  def f(qtile):
    if qtile.groups_map[group].windows:
       qtile.groups_map[group].cmd_toscreen(toggle=False)
       qtile.cmd_spawn(app)
    else:
      qtile.groups_map[group].cmd_toscreen(toggle=False)
      qtile.cmd_spawn(app)
    return f
  
## Get network device in use
def get_net_dev():
  get_dev = "ip addr show | awk '/inet.*brd/{print $NF; exit}'"
  ps = subprocess.Popen(get_dev,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
  output = ps.communicate()[0].decode('ascii').strip()
  return(output)

wifi = get_net_dev()

pc_name = os.popen('uname -n').read()

# Set the the right icon for network device
if pc_name.startswith('h'):
  wifi_icon=''
  res="FullHD"
  wall_dir = home + '/Pictures/Wallpapers/'
  sensor='Core 0' 
else:
  wifi_icon=''
  res="4k"
  wall_dir = home + '/Pictures/Wallpapers/'
  sensor='Tctl'

## Resolution change
f_size = 20 # Bars Font size
i_size = 18 # Tray Icon size
b_size = 30 # Bar size
if res == "4k":
  f_size = 20 # Bars Font size
  i_size = 18 # Tray Icon size
  b_size = 30 # Bar size
else:
  f_size = 14 # Bars Font size
  i_size = 16 # Tray Icon size
  b_size = 23 # Bar size  

## Get local IP Address
def get_private_ip():
  ip = socket.gethostbyname(socket.gethostname())
  return ip

private_ip = get_private_ip()

## Get Public IP Address
def get_public_ip():
  try:
    raw = requests.get('https://api.duckduckgo.com/?q=ip&format=json')
    answer = raw.json()["Answer"].split()[4]
  except Exception as e:
    return "0.0.0.0"
  else:
    return answer
        
public_ip = get_public_ip()

## Check Internet Connection
internet = ' Internet is Working!!! '
if public_ip.startswith('0'):
  internet = "∅ No internet connection "
  
## Import Colors from Pywal
with open(home + '/.cache/wal/colors.json') as wal_import:
  data = json.load(wal_import)
  wallpaper = data['wallpaper']
  colors = data['colors']
  val_colors = list(colors.values())
  def getList(val_colors):
    return [*val_colors]
    
  def init_colors():
    return [*val_colors]

color = init_colors()

dir = wall_dir
selection = random.choice(os.listdir(dir))
rand_wallpaper = os.path.join(dir, selection)
## Set Random Wallpaper
def set_rand_wallpaper(qtile):
  while(True):
    if rand_wallpaper != wallpaper:
      subprocess.run(["wpg", "-s", "%s" % rand_wallpaper, "--backend", "%s" %def_Backend.lower()])
      subprocess.run(["sudo", "cp", "%s" % rand_wallpaper,  "/usr/share/backgrounds/background.png"])
      subprocess.run(["sudo", "cp", "-r", home + "/.local/share/themes/FlatColor",  "/usr/share/themes/"])
      qtile.reload_config()
      break
    else:
      subprocess.run(["wpg", "-s", "%s" % rand_wallpaper, "--backend", "%s" %def_Backend.lower()])
      subprocess.run(["sudo", "cp", "%s" % rand_wallpaper,  "/usr/share/backgrounds/background.png"])
      subprocess.run(["sudo", "cp", "-r", home + "/.local/share/themes/FlatColor", "/usr/share/themes/"])
      qtile.reload_config()
      break
## Rofi Menus

## Change Color Backend
def change_color_scheme(qtile):
  options = backend
  index, key = rofi_backend.select('  Color Scheme', options)
  if key == -1 or index == 4:
    rofi_backend.close()
  else:
    subprocess.run(["wal", "-i", "/usr/share/backgrounds/background.png", "--backend", "%s" %backend[index].lower()])
    subprocess.run(["wpg", "-s", "/usr/share/backgrounds/background.png", "--backend", "%s" %backend[index].lower()])
    subprocess.run(["sudo", "cp", "-r", home + "/.local/share/themes/FlatColor",  "/usr/share/themes/"])
    qtile.reload_config()

## Set random colorts to theme
def random_colors(qtile):

  subprocess.run(["wpg", "-z", "%s" % wallpaper])
  subprocess.run(["wpg", "-s", "%s" % wallpaper])
  subprocess.run(["rm", "-rf", "%s" %wallpaper + "_wal_sample.png"])
  qtile.reload_config()

## Display Shortcuts widget
def shortcuts(qtile):
  subprocess.run("cat ~/.shortcuts | rofi -theme '~/.config/rofi/left_bar.rasi' -i -dmenu -p ' Shortcuts:'",shell=True)

#### NightLight widget
def nightLight_widget(qtile):
  options = [' Night Time(3500k)', ' Neutral (6500k)', ' Cool (7500k)']
  index, key = rofi_session.select('  Night Light', options)
  if key == -1:
    rofi_session.close()
  else:
    if index == 0:
      os.system('redshift -O 3500k -r -P')
    elif index == 1:
      os.system('redshift -x')
    else:
      os.system('redshift -O 7500k -r -P')

## Logout widget
def session_widget(qtile):
  options = [' Log Out', ' Reboot',' Poweroff',' Lock']
  index, key = rofi_session.select('  Session', options)
  if key == -1:
    rofi_session.close()
  else:
    if index == 0:
      qtile.cmd_shutdown()
    elif index == 1:
      os.system('systemctl reboot')
    elif index == 2:
      os.system('systemctl poweroff')    
    else:
      os.system('dm-tool switch-to-greeter')

## Screenshot widget
def screenshot(qtile):
  options = [' Screen', ' Window', ' Area', ' 5s Screen']
  index, key = rofi_screenshot.select('  Screenshot', options)
  if key == -1:
    rofi_screenshot.close()
  else:
    if index ==0:
      subprocess.run("scrot -d 1 'Screenshot_%S-%m-%y.png' -e 'mv $f ~/Pictures/ #; feh -F ~/Pictures/$f' && dunstify ' Screenshot Taken!'",shell=True)
    elif index==1:
      subprocess.run("scrot -u 'Screenshot_%S-%m-%y.png' -e 'mv $f ~/Pictures/ #; feh -F ~/Pictures/$f' && dunstify ' Screenshot Taken!'",shell=True)
    elif index==2:
      subprocess.run("scrot -s 'Screenshot_%S-%m-%y.png' -e 'mv $f ~/Pictures/ #; feh -F ~/Pictures/$f' && dunstify ' Screenshot Taken!'",shell=True)
    else:
      subprocess.run("scrot -d 5 -c 'Screenshot_%S-%m-%y.png' -e 'mv $f ~/Pictures/ #; feh -F ~/Pictures/$f' && dunstify ' Screenshot Taken!'",shell=True)

## Farge Widget
def fargewidget(qtile):
  options = [' Hex',' RGB']
  index, key = rofi_fargewidget.select('  Color Picker', options)
  if key == -1:
    rofi_fargewidget.close()
  else:
    if index ==0:
      subprocess.run("farge --notify --expire-time 10000",shell=True)
    else:
      subprocess.run("farge --notify --rgb --expire-time 10000",shell=True)

## Network Widget
def network_widget(qtile):
  get_ssid = "iwgetid -r"
  pos = subprocess.Popen(get_ssid,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
  ssid = pos.communicate()[0].decode('ascii').strip()
  get_status = "nmcli radio wifi"
  ps = subprocess.Popen(get_status,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
  status = ps.communicate()[0].decode('ascii').strip()
  if status == 'enabled':
    connected = ' Turn Wifi Off'
    active = "off"
  else:
    connected = ' Turn Wifi On'
    active="on"
  options = [connected,' Bandwith Monitor (CLI)', ' Network Manager (CLI)']
  index, key = rofi_network.select(wifi_icon + internet, options)
  if key == -1:
    rofi_network.close()
  else:
    if index ==0:
      subprocess.run("nmcli radio wifi " + active, shell=True)
    elif index==1:
      qtile.cmd_spawn(term + ' -e bmon')
    else:
      qtile.cmd_spawn(term + ' -e nmtui')

## Change Theme widget
def change_theme(qtile):
  options = theme
  index, key = rofi_backend.select('  Select Theme', options)
  if key == -1:
    rofi_backend.close()
  else:
    subprocess.run('rm -rf ~/.config/qtile/theme.py', shell=True)
    subprocess.run('\cp ~/.config/qtile/themes/%s ~/.config/qtile/theme.py'% theme[index], shell=True)
    qtile.reload_config()

## Multimedia
def play_pause(qtile):
  qtile.cmd_spawn("playerctl -p spotify play-pause")
  qtile.cmd_spawn("playerctl -p ncspot play-pause")
  qtile.cmd_spawn("playerctl -p vlc play-pause")
  qtile.cmd_spawn("playerctl -p cmus play-pause")

def nexts(qtile):
  qtile.cmd_spawn("playerctl -p spotify next")
  qtile.cmd_spawn("playerctl -p ncspot next")
  qtile.cmd_spawn("playerctl -p vlc next")
  qtile.cmd_spawn("playerctl -p cmus next")

def prev(qtile):
  qtile.cmd_spawn("playerctl -p spotify previous")
  qtile.cmd_spawn("playerctl -p ncspot previous")
  qtile.cmd_spawn("playerctl -p vlc previous")
  qtile.cmd_spawn("playerctl -p cmus previous")

## Internet Search
def wsearx():
  run(home + '/.local/bin/wsearch')

##########################################################################
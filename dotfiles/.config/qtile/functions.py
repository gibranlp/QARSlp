#
# _______  _______  ______  _______  __        
#|       ||   _   ||   __ \|     __||  |.-----.
#|   -  _||       ||      <|__     ||  ||  _  |
#|_______||___|___||___|__||_______||__||   __|
#                                       |__|   
# QARSlp Qtile + Arch Ricing System
# By: gibranlp <thisdoesnotwork@gibranlp.dev>
# MIT licence 
#
import json
import os
import random
import socket
import subprocess
from os.path import expanduser
from pathlib import Path
import requests
from libqtile import bar, hook, layout, qtile, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from qtile_extras import widget
from qtile_extras.popup.toolkit import (PopupImage, PopupRelativeLayout,PopupText, PopupWidget)
from qtile_extras.widget.decorations import (BorderDecoration,PowerLineDecoration,RectDecoration)
from rofi import Rofi

#### Variables ####

version='v2.0.2'

# Modifiers
mod = "mod4"
alt = "mod1"

## Fonts
main_font = "Fira Code Medium" # Font in use for the entire system
awesome_font = "Font Awesome 6 Pro" # Font for the icons
font_size=17 # This value will be overwritten by the size of the display
bar_size=30 # This value will be overwritten by the size of the display

# Terminal 
terminal = "alacritty" # Terminal in use

#Home Path
home = os.path.expanduser('~') # Path for use in folders
prompt = "".format(os.environ["USER"], socket.gethostname()) # Format of the prompt

## Import Persistent Variables
file = open(home + '/.config/qtile/variables', 'r')
variables=file.readlines()

# Wallpapers / Theming
wallpaper_dir= home + '/Pictures/Wallpapers/' # Wallpapers folders
light=str(variables[3].strip()) # Option for light themes

# Diferenciator, this will get added to generate a slightly different pallete
differentiator = '191919'

#Show all groups
hide_unused_groups=True

# Theme
current_theme=str(variables[0].strip())
themes_dir = home + str(variables[4].strip())
theme_dest = (home + "/.config/qtile/theme.py")
theme_file = themes_dir + "/" + current_theme
theme=['QARSlp', 'nice', 'slash', 'minimal', 'Monochrome', 'no_bar']

# Pywal backends Options: Wal, Colorz, Colorthief, Haishoku
def_backend=str(variables[1].strip()) # Default Color Scheme for random wallpaper
backend=['wal', 'colorz', 'colorthief','haishoku']

## Margins
layout_margin=10 # Layout margins
single_layout_margin=10 # Single window margin 
## Borders
layout_border_width=5 # Layout border width
single_border_width=5 # Single border width

# Bar Position
bar_position=str(variables[5].strip())

#Widgets
widget_width=200 #Width of widgets varies depending the resolution

# Get current screen resolution
resolution = os.popen('xdpyinfo | awk "/dimensions/{print $2}"').read()
xres = resolution[17:21]
yres = resolution[22:26]

# Set Bar and font sizes for different resolutions
if xres >= "3840" and yres >= "2160": #4k
  layout_margin=15
  single_layout_margin=10  
  layout_border_width=5
  single_border_width=5
  font_size=20
  bar_size=30
  widget_width=400
  max_ratio=0.85
  ratio=0.70
  if bar_position == "bottom":
    bar_margin=[0,15,10,15]
  else:
    bar_margin=[10,15,0,15]
elif xres == "1920" and yres == "1080": #FullHD
  layout_margin=10
  single_layout_margin=5  
  layout_border_width=4 
  single_border_width=4
  font_size=16
  bar_size=25
  widget_width=220
  max_ratio=0.85
  ratio=0.70
  if bar_position == "bottom":
    bar_margin=[0,10,5,10]
  else:
    bar_margin=[5,10,0,10]
else: # 1366 x 768 Macbook air 11"
  layout_margin=2
  single_layout_margin=2  
  layout_border_width=2
  single_border_width=2
  font_size=13
  bar_size=20
  widget_width=100
  max_ratio=0.60
  ratio=0.50
  bar_margin=[0,0,0,0]

# Rofi Configuration files
rofi_right = Rofi(rofi_args=['-theme', '~/.config/rofi/right.rasi'])
rofi_network= Rofi(rofi_args=['-theme', '~/.config/rofi/network.rasi'])
rofi_left= Rofi(rofi_args=['-theme', '~/.config/rofi/left.rasi'])
rofi_wallpaper=Rofi(rofi_args=(['rofi', '-show file-browser-extended', '-theme', '~/.config/rofi/sel_wal.rasi', '-file-browser-dir', '~/Pictures/Wallpapers', '-file-browser-stdout']))

### Weather
w_appkey = str(variables[2].strip()) # Get a key here https://home.openweathermap.org/users/sign_up 
w_cityid ="3995402" # "3995402" Morelia, "3521342" Playa del Carmen https://openweathermap.org/city/

## Hooks
@hook.subscribe.startup # This file gets executed everytime qtile restarts
def start():
  subprocess.call(home + '/.local/bin/alwaystart')
      
@hook.subscribe.startup_once # Ths file gets executed at first start only
def start_once():
  subprocess.call(home + '/.local/bin/autostart')

@hook.subscribe.client_new
def follow_window(client):
  for group in groups:
    match = next((m for m in group.matches if m.compare(client)), None)
    if match:
      targetgroup = qtile.groups_map[group.name]
      targetgroup.toscreen(toggle=False)
      break

@hook.subscribe.client_name_updated
def follow_window_name(client):
  for group in groups:
    match = next((m for m in group.matches if m.compare(client)), None)
    if match:
      targetgroup = qtile.groups_map[group.name]
      targetgroup.toscreen(toggle=False)
      break

##Specific Apps/Groups
def app_or_group(group, app):
  def f(qtile):
    if qtile.groups_map[group].windows:
       qtile.groups_map[group].toscreen(toggle=False)
       qtile.spawn(app)
    else:
      qtile.groups_map[group].cdtoscreen(toggle=False)
      qtile.spawn(app)
    return f

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

## Generate Secondary Palette
def secondary_pallete(colors, differentiator):
    updated_colors = []
    for color in colors:
        # Remove the '#' symbol
        color = color.lstrip('#')

        # Convert hexadecimal colors to integers
        color_int = int(color, 16)
        differentiator_int = int(differentiator, 16)

        # Perform addition
        result_int = color_int + differentiator_int

        # Ensure the result is within the valid range of 0-FFFFFF
        result_int = min(result_int, 0xFFFFFF)
        result_int = max(result_int, 0)

        # Convert the result back to hexadecimal
        result_hex = '#' + hex(result_int)[2:].zfill(6).upper()

        updated_colors.append(result_hex)

    return updated_colors

secondary_color = secondary_pallete(color, differentiator)

# Run i3-lock with Colors

def i3lock_colors(qtile):
  subprocess.run(['i3lock', 
    '--ring-color={}'.format(secondary_color[0])+"DD",
    '--inside-color={}'.format(secondary_color[0])+"DD",
    '--line-color={}'.format(color[2]),
    '--separator-color={}'.format(color[4]),
    '--time-color={}'.format(color[2]),           
    '--date-color={}'.format(color[4]),
    '--insidever-color={}'.format(secondary_color[0])+"DD",
    '--ringver-color={}'.format(secondary_color[0])+"DD",
    '--verif-color={}'.format(color[5]),          
    '--verif-text=Checking',
    '--insidewrong-color={}'.format(secondary_color[0])+"DD",
    '--ringwrong-color={}'.format(secondary_color[0])+"DD",
    '--wrong-color={}'.format(color[1]),
    '--wrong-text=Wrong!',
    '--keyhl-color={}'.format(color[1]),         
    '--bshl-color={}'.format(color[6]),            
    '--clock',
    '--blur', '10',                 
    '--indicator',       
    '--time-str="%H:%M:%S"',   
    '--date-str="%A, %Y-%m-%d"',
    ])

# Transparent for bars and widgets
transparent=color[0] + "00"

# Set Random Wallpaper
def change_wallpaper(qtile):
  selection = random.choice(os.listdir(wallpaper_dir))
  selected_wallpaper = os.path.join(wallpaper_dir, selection)
  i=0
  while selected_wallpaper != wallpaper and i<2:
    subprocess.run(["wpg", light, "-s", str(selected_wallpaper), "--backend", def_backend.lower()])
    subprocess.run(["cp", str(selected_wallpaper), "/usr/local/backgrounds/background.png"])
    subprocess.run(["cp", "-r", str(Path.home() / ".local/share/themes/FlatColor"), "/usr/local/themes/"])
    break
  else:
    selection = random.choice(os.listdir(wallpaper_dir))
    selected_wallpaper = os.path.join(wallpaper_dir, selection)
  
  qtile.reload_config()
  #subprocess.run(["notify-send","-a", " QARSlp", "Random Wallpaper Set to: ", "%s" %selection])

## Get network device in use
def get_net_dev():
  get_dev = "echo $(ip route get 8.8.8.8 | awk -- '{printf $5}')"
  ps = subprocess.Popen(get_dev,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
  output = ps.communicate()[0].decode('ascii').strip()
  return(output)

wifi = get_net_dev()

# Set Ethernet or Wifi icon according
if wifi.startswith('e'):
  wifi_icon=''
else:
  wifi_icon=''

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

# Call Calendar Notification

def calendar_notification(qtile):{
    subprocess.call(home + '/.local/bin/calendar')
}

def calendar_notification_prev(qtile):{
    subprocess.call([home + '/.local/bin/calendar', 'prev'])
}

def calendar_notification_next(qtile):{
    subprocess.call([home + '/.local/bin/calendar', 'next'])
}

## Rofi Widgets

## Set default backend
def set_default_backend(qtile):
  options = backend
  index, key = rofi_left.select('  Backend -  ' + def_backend , options)
  if key == -1 or index == 4:
    rofi_left.close()
  else:
    subprocess.run(["wal", light.lower(), "-i", "/usr/local/backgrounds/background.png", "--backend", "%s" %backend[index].lower()])
    subprocess.run(["wpg", light, "-s", "/usr/local/backgrounds/background.png", "--backend", "%s" %backend[index].lower()])
    subprocess.run(["cp", "-r", home + "/.local/share/themes/FlatColor",  "/usr/local/themes/"])
    variables[1]=backend[index] + "\n"
    with open(home + '/.config/qtile/variables', 'w') as file:
      file.writelines(variables)
    qtile.reload_config()
    subprocess.run(["notify-send","-a", " QARSlp", "Color Theme: ", " %s" %backend[index]])

# Display Shortcuts widget
def shortcuts(qtile):
  subprocess.run("cat ~/.shortcuts | rofi -theme '~/.config/rofi/shortcuts.rasi' -i -dmenu -p ' Shortcuts:'",shell=True)

# Display Emojis
def emojis(qtile):
  subprocess.run("rofi -modi emoji -show emoji -theme '~/.config/rofi/emojis.rasi' -emoji-format {emoji}",shell=True)

# NightLight widget
def nightLight_widget(qtile):
  options = [' Night Time(3500k)', ' Neutral (6500k)', ' Cool (7500k)']
  index, key = rofi_left.select('  Night Light', options)
  if key == -1:
    rofi_left.close()
  else:
    if index == 0:
      os.system('redshift -O 3500k -r -P')
      subprocess.run(["notify-send","-a", " QARSlp", "Temperature Set to Night Time"])
    elif index == 1:
      os.system('redshift -x')
      subprocess.run(["notify-send","-a", " QARSlp", "Temperature Set to Neutral"])
    else:
      os.system('redshift -O 7500k -r -P')
      subprocess.run(["notify-send","-a", " QARSlp", "Temperature Set to Cool"])

# Farge Widget
def fargewidget(qtile):
  options = [' Hex',' RGB']
  index, key = rofi_left.select('  Color Picker', options)
  if key == -1:
    rofi_left.close()
  else:
    if index ==0:
      subprocess.run("farge --notify --expire-time 20000",shell=True)
    else:
      subprocess.run("farge --notify --rgb --expire-time 20000",shell=True)

# Draw Widget
def draw_widget(qtile):
  options = [' Draw', ' Exit']
  index, key = rofi_left.select('  Screen Draw', options)
  if key == -1:
    rofi_left.close()
  else:
    if index ==0:
      subprocess.run("gromit-mpx -a &",shell=True)
      subprocess.run(["notify-send", "-a", " QARSlp", "You can Draw Now"])
    else:
      subprocess.run("gromit-mpx -q",shell=True)

# Logout widget
def session_widget(qtile):
  options = [' Log Out', ' Reboot',' Poweroff',' Lock']
  index, key = rofi_left.select('  Session', options)
  if key == -1:
    rofi_left.close()
  else:
    if index == 0:
      qtile.shutdown()
    elif index == 1:
      os.system('systemctl reboot')
    elif index == 2:
      os.system('systemctl poweroff')    
    else:
      qtile.function(i3lock_colors)

# Network Widget
def network_widget(qtile):
  options = [' Wlan Manager','  Bandwith Monitor (CLI)', ' Network Manager (CLI)']
  index, key = rofi_network.select(" " + private_ip + " -" + "  " + public_ip, options)
  if key == -1:
    rofi_network.close()
  else:
    if index == 0:
      qtile.spawn(home + '/.local/bin/wifi2')
    elif index==1:
      qtile.spawn(terminal + ' -e bmon')
    else:
      qtile.spawn(terminal + ' -e nmtui')


## Select Dark or Light Theming
def dark_white(qtile):
  options = [' Dark', ' Light']
  index, key = rofi_left.select(' Select Theme', options)
  if key == -1 or index == 2:
    rofi_left.close()
  else:
    if index == 0:
      variables[3]="-c" + "\n"
      variables[4]="/.config/qtile/themes/dark" + "\n"
      subprocess.run(['cp', home + '/.config/qtile/themes/dark/' + current_theme + ".py", home + '/.config/qtile/theme.py'])
      subprocess.run(["wal", "-i", "/usr/local/backgrounds/background.png", "--backend", "%s" %def_backend])
      subprocess.run(["wpg", "-s", "/usr/local/backgrounds/background.png", "--backend", "%s" %def_backend])
    else:
      variables[3]="-L" + "\n"
      variables[4]="/.config/qtile/themes/light" + "\n"
      subprocess.run(['cp', home + '/.config/qtile/themes/light/' + current_theme + ".py", home + '/.config/qtile/theme.py'])
      subprocess.run(["wal", "-l", "-i", "/usr/local/backgrounds/background.png", "--backend", "%s" %def_backend])
      subprocess.run(["wpg", "-L", "-s", "/usr/local/backgrounds/background.png", "--backend", "%s" %def_backend])

    subprocess.run(["cp", "-r", home + "/.local/share/themes/FlatColor",  "/usr/local/themes/"])
    with open(home + '/.config/qtile/variables', 'w') as file:
      file.writelines(variables)
    qtile.reload_config()
    subprocess.run(["notify-send","-a", " QARSlp", "Theme changed to: ", "%s" %options[index]])


## Select Bar Position Top or Bottom
def bar_pos(qtile):
  options = ['Top', 'Bottom', 'Toggle Bar']
  index, key = rofi_left.select(' Bar -> ' + bar_position , options)
  if key == -1:
    rofi_left.close()
  else:
    if index == 0:
      variables[5]="top"
      subprocess.run(["cp", "-r", home + "/.local/share/themes/FlatColor",  "/usr/local/themes/"])
      with open(home + '/.config/qtile/variables', 'w') as file:
        file.writelines(variables)
      qtile.reload_config()
    elif index == 1:
      variables[5]="bottom"
      subprocess.run(["cp", "-r", home + "/.local/share/themes/FlatColor",  "/usr/local/themes/"])
      with open(home + '/.config/qtile/variables', 'w') as file:
        file.writelines(variables)
      qtile.reload_config()
    else:
      qtile.hide_show_bar()

    

# Change Theme widget
def change_theme(qtile):
  options = theme
  index, key = rofi_left.select('  Theme -  ' + current_theme , options)
  if key == -1:
    rofi_left.close()
  else:
    subprocess.run('rm -rf ~/.config/qtile/theme.py', shell=True)
    variables[0]=theme[index] + "\n"
    new_theme=theme[index] + ".py"
    subprocess.run(['cp', themes_dir + "/" + new_theme, home + '/.config/qtile/theme.py'])
    with open(home + '/.config/qtile/variables', 'w') as file:
      file.writelines(variables)
    qtile.reload_config()
    subprocess.run(["notify-send","-a", " QARSlp", " Theme: ", "%s" %theme[index]])
    
# Set random colors to theme
def random_colors(qtile):
  subprocess.run(["wpg", "-z", "%s" % wallpaper])
  subprocess.run(["wpg", "-s", "%s" % wallpaper])
  subprocess.run(["rm", "-rf", "%s" %wallpaper + "_wal_sample.png"])
  qtile.reload_config()

# Screenshot widget
def screenshot(qtile):
  options = [' Area', ' Screen', ' Window',  ' 5s Screen']
  index, key = rofi_left.select('  Screenshot', options)
  if key == -1:
    rofi_left.close()
  else:
    if index ==0:
      subprocess.run("flameshot gui --path ~/Pictures/area_screenshot.png --delay 400",shell=True)
    elif index==1:
      subprocess.run("flameshot full --path ~/Pictures/Screenshot.png --delay 500",shell=True)
    elif index==2:
      subprocess.run("scrot -u 'window_screenshot.png' -e 'mv $f ~/Pictures/ #; feh -F ~/Pictures/$f' && notify-send -a 'flameshot' 'Window Picture Taken!'",shell=True)
    else:
      subprocess.run("flameshot full --path ~/Pictures/Screenshot.png --delay 5000",shell=True)

# Control Panel Widget
def control_panel(qtile):
  options = [
    ' Wallpaper Options',#0
    '     Set Random Wallpaper (⎇ + R)',
    '     Select Wallpaper (❖ +  + E)',
    ' Theme Options',#3
    '     Set Color Scheme (⎇ +  + W)',
    '     Dark/Light Theme (❖ + D)',
    '     Bar Position (❖ +  + W)',
    '     Change Bar Theme (⎇ + W)',
    ' Tools',#8
    '     Notes (❖ + N)',
    '     Apps as Sudo (⎇ + )',
    '     Calculator (❖ + C)',
    '     Network Manager (❖ + B)',
    '     Screenshot (prtnsc)',
    '     Monitor Temperature (❖ +  + O)',
    '     Monitor Layout (❖ +  + X)',
    '     Bluetooth (❖ + T)',
    '     Screen Recorder ( +  + R)',
    ' Miscelaneous',#17
    '     Screen Draw (❖ +  + P)',
    '     Pick Color (❖ + P)',
    '     View Shortcuts (❖ + S)',
    '     Emojis ( +  + )',
    ' Session Menu (❖ + X)',
    ' Update QARSlp %s' %version,
    '<<<< Nomenclature >>>>' 
    ' :: Control Key' 
    '❖ :: Super / Windows Key' 
    '⎇ :: Alt Key'
    ' :: Enter Key'
    ' :: Shift Key'
    ]
  index, key = rofi_left.select('  Control Panel', options)
  if key == -1:
    rofi_left.close()
  else:
    if index == 1:
      qtile.function(change_wallpaper)
    elif index == 2:
      qtile.spawn(home + '/.local/bin/selectwal')
    elif index == 4:
      qtile.function(set_default_backend)
    elif index == 5:
      qtile.function(dark_white)
    elif index == 6:
      qtile.function(bar_pos)
    elif index == 7:
      qtile.function(change_theme)
    elif index == 9:
      subprocess.Popen(home + '/.local/bin/notesfi', shell=True)
    elif index == 10:
      qtile.spawn('sudo rofi -show drun -show-icons -theme "~/.config/rofi/launcher.rasi"')
    elif index == 11:
      subprocess.run(home + '/.local/bin/calculator')
    elif index == 12:
      qtile.function(network_widget)
    elif index == 13:
      qtile.function(screenshot)
    elif index == 14:
      qtile.function(nightLight_widget)
    elif index == 15:
      subprocess.run(home + '/.local/bin/change_display')
    elif index == 16:
      subprocess.run(home + '/.local/bin/bluet')
    elif index == 17:
      subprocess.run(home + '/.local/bin/recorder')
    elif index == 19:
      qtile.function(draw_widget)
    elif index == 20:
      qtile.function(fargewidget)
    elif index == 21:
      qtile.function(shortcuts)
    elif index == 22:
      qtile.function(emojis)
    elif index == 23:
      qtile.function(session_widget)
    elif index == 23:
      subprocess.run(home + '/.local/bin/updater')
    
## 
keys = [
    #Basics
    Key([alt], "r",lazy.function(change_wallpaper)), # Set random wallpaper / colors to entire system
    Key([mod, "shift"], "e",lazy.spawn(home + '/.local/bin/selectwal')), # Set random wallpaper / colors to entire system
    Key([mod], "Return", lazy.spawn(terminal)), # Open Terminal
    Key([mod, "shift"], "Return", lazy.spawn('rofi -show drun -show-icons -theme "~/.config/rofi/launcher.rasi"')), # Open Rofi launcher
    Key([alt, "shift"], "Return", lazy.spawn('sudo rofi -show drun -show-icons -theme "~/.config/rofi/launcher.rasi"')), # Open Rofi launcher as Sudo
    Key(["control", "shift"], "Return", lazy.function(emojis)), # Open Rofi Emojis
    Key([mod], "r", lazy.spawncmd()), # Launch Prompt
    Key([mod], "q",lazy.window.kill()), # Close Window 
    Key([mod, "shift"], "r",lazy.reload_config()), # Restart Qtile
    Key([mod, "shift"], "q",lazy.shutdown()), # Logout         
    Key([alt], "Escape", lazy.spawn('xkill')), # Click window to close

    # Widgets
    Key([mod],"s",lazy.function(shortcuts)), # Shortcuts widget
    Key([mod],"c",lazy.spawn(home + '/.local/bin/calculator')), # Calculator Widget
    Key([mod], "n", lazy.spawn(home + '/.local/bin/notesfi')), # Notes Widget
    Key([mod],"d",lazy.function(dark_white)), # Select Dark or Light Theme
    Key([mod, "shift"],"w",lazy.function(bar_pos)), # Set bar position
    Key([mod, "shift"],"o",lazy.function(nightLight_widget)), # Set night light
    Key([mod],"p",lazy.function(fargewidget)), # Color Picker Widget
    Key(["control", "shift"], "r", lazy.spawn(home + '/.local/bin/recorder')), # Recorder Widget
    Key([mod, "shift"],"p",lazy.function(draw_widget)), # Desktop draw widget
    Key([alt], "Return", lazy.function(control_panel)), # Search for files and folders
    Key([mod], "t", lazy.spawn(home + '/.local/bin/bluet')), # Bluetooth widget
    Key([mod],"x",lazy.function(session_widget)), # Log out
    Key([mod],"b",lazy.function(network_widget)), # Network Settings
    Key([alt, "shift"],"w",lazy.function(set_default_backend)), # Set Default Color Scheme
    Key([alt],"w",lazy.function(change_theme)), # Change Theme
    Key([mod, "shift"],"x",lazy.spawn(home + '/.local/bin/change_display')),# Monitor modes Widget
    Key([alt, "shift"], "r",lazy.function(random_colors)), # Set randwom wallpaper / colors to entire system

    # Layouts
    Key([mod], "Tab",lazy.layout.down()), # Change focus of windows down
    Key([mod, "shift"], "Tab",lazy.layout.up()), # Change focus of windows up
    Key([alt], "Tab", lazy.layout.swap_left()), # Swap Left Down
    Key([alt, "shift"], "Tab", lazy.layout.swap_right()), # Swap Right Up
    Key([mod], 'period', lazy.next_screen()), # Send Cursor to next screen

    # Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("sudo xbacklight -inc 5")), # Aument Brightness
    Key(["control", alt], "p", lazy.spawn("sudo xbacklight -inc 5")), # Aument Brightness
    Key([], "XF86MonBrightnessDown", lazy.spawn("sudo xbacklight -dec 5")), # Lower Brightness
    Key(["control", alt], "o", lazy.spawn("sudo xbacklight -dec 5")),

    # Volume
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")), # Mute
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -q set Master 1%- && dunstify -a Volume ' '$(pamixer --get-volume-human) -h int:value:$(pamixer --get-volume)", shell=True)),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -q set Master 1%+ && dunstify -a Volume ' '$(pamixer --get-volume-human) -h int:value:$(pamixer --get-volume)", shell=True)), # Raise Volume

    # Media Control
    Key([], "XF86AudioPlay", lazy.spawn("playerctl --player=%any play-pause")), # Play Pause
    Key([], "XF86AudioNext", lazy.spawn("playerctl --player=%any next")), # Next song
    Key([], "XF86AudioPrev", lazy.spawn("playerctl --player=%any previous")), # Previous Song

    # Window hotkeys
    Key([alt], "g", lazy.window.toggle_fullscreen()), # Toggle Current window ;n
    Key([alt, "shift"], "f", lazy.window.toggle_floating()), # Toggle current window floating
    Key([mod], "space", lazy.next_layout()), # Cycle layouts

    # Resize windows
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod, "shift"], "h", lazy.layout.swap_left()),
    Key([mod, "shift"], "l", lazy.layout.swap_right()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod], "i", lazy.layout.grow()),
    Key([mod, "shift"], "i", lazy.layout.grow_main()),
    Key([mod], "m", lazy.layout.shrink()),
    Key([mod, "shift"], "m", lazy.layout.shrink_main()),
    Key([mod], "o", lazy.layout.maximize()),
    Key([mod, "shift"], "space", lazy.layout.flip()),

    # Keyboard
    Key([alt], "space", lazy.widget["keyboardlayout"].next_keyboard()), # Change Keyboard Layout

    # Screenshots
    Key([], "Print", lazy.function(screenshot)),

    # Lock Screen
    Key(["control", alt],"l",lazy.function(i3lock_colors)), # Run i3lock 

    # Dunst Shortuts
    Key(["control"], "space",  lazy.spawn("dunstctl close")), # Clear Last Notification
    Key(["control", "shift"], "space",  lazy.spawn("dunstctl close-all")), # Clear All Notifications
    Key(["control", "shift"], "n",  lazy.spawn("dunstctl  history-pop")), # Show Notificaction history
]

## Groups
groups = []
group_names = ["Escape","1","2","3","4","5","6","7","8","9"]

#### Groups Labels
#group_labels=["零","一","二","三","四","五","六","七","八","九"] # Kanji Numbers
#group_labels=["0","1","2","3","4","5","6","7","8","9"] # Numbers
#group_labels=["","","","","","","","","",""] # Circles
#group_labels=["","","","","","","","","",""] # Dot Circles
group_labels=["","","","","","","","","",""] # Custom
#group_labels=["","","","","","","","","",""] # Star Wars


####

group_layouts=["monadtall", "monadtall", "monadtall", "monadtall","monadtall", "monadtall", "monadtall","monadwide", "monadtall", "monadtall"]
for i in range(len(group_names)):
  groups.append(
    Group(
      name=group_names[i],
      layout=group_layouts[i].lower(),
      label=group_labels[i],
  ))
for i in groups:
    keys.append(Key([mod], i.name, lazy.group[i.name].toscreen()))
    keys.append(Key([mod, 'shift'], i.name, lazy.window.togroup(i.name)))

## Layouts
def init_layout_theme():
  return {"font":main_font,
    "fontsize":font_size,
    "margin":layout_margin,
    "border_on_single":False,
    "border_width":layout_border_width,
    "border_normal":color[0],
    "border_focus":color[2],
    "single_margin":single_layout_margin,
    "single_border_width":single_border_width,
    "change_ratio":0.01,
    "new_client_position":'bottom',
    }

layout_theme = init_layout_theme()

def init_layouts():
  return [
    layout.Spiral(main_pane="left",ratio_increment=0.01,**layout_theme),
    layout.MonadTall(max_ratio=max_ratio,ratio=ratio,**layout_theme),
    layout.MonadWide(max_ratio=0.85,ratio=0.85,**layout_theme),
    layout.Floating(**layout_theme),
    ]
layouts = init_layouts()

widget_defaults = dict(
    font=main_font,
    fontsize=font_size,
    padding=3,
)



# _______  _______  ______  _______  __        
#|       ||   _   ||   __ \|     __||  |.-----.
#|   -  _||       ||      <|__     ||  ||  _  |
#|_______||___|___||___|__||_______||__||   __|
#                                       |__|   
# SpectrumOS - Embrace the Chromatic Symphony!
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



# Modifiers
mod = "mod4"
alt = "mod1"

#Home Path
home = os.path.expanduser('~') # Path for use in folders

## Import config
file = open(home + '/.config/qtile/variables', 'r')
variables=file.readlines()

## Get update if available
file = open(home + '/QARSlp/dotfiles/.config/qtile/update', 'r')
update_available=file.readlines()

# SpectrumOS version
remote_version=float(update_available[0].strip())
version=float(variables[0].strip())

if version == remote_version:
  update_spectrumos= ' SpectrumOS is up to date!'
else:
  update_spectrumos= f' Update Available {version} -> {remote_version}',


## Fonts
main_font = "Fira Code Medium" # Font in use for the entire system
awesome_font = "Font Awesome 6 Pro" # Font for the icons
font_size=17 
bar_size=30

# Terminal 
terminal = "alacritty" # Terminal in use


# Format of the prompt
prompt = " ".format(os.environ["USER"], socket.gethostname()) 

# Wallpapers / Theming
wallpaper_dir= home + '/Pictures/Wallpapers/' # Wallpapers folders
light=str(variables[4].strip()) # Option for light themes

# Diferenciator, this will get added to generate a slightly different pallete
differentiator = '222222'

#Initialize Groups
groups = []
group_names = ["Escape","1","2","3","4","5","6","7","8","9"]
hide_unused_groups=bool(str(variables[8].strip()))

# Theme
current_theme=str(variables[1].strip())
themes_dir = home + str(variables[5].strip())
theme_dest = (home + "/.config/qtile/theme.py")
theme_file = themes_dir + "/" + current_theme
theme=['Spectrum', 'Slash', 'Miasma', 'Nice',  'Minimal', 'Monochrome', 'no_bar']

# Pywal backends Options: Wal, Colorz, Colorthief, Haishoku
def_backend=str(variables[2].strip()) # Default Color Scheme for random wallpaper
backend=['wal', 'colorz', 'colorthief','haishoku']

## Margins
layout_margin=10 # Layout margins
single_layout_margin=10 # Single window margin 
## Borders
layout_border_width=5 # Layout border width
single_border_width=5 # Single border width

# Bar Position
bar_position=str(variables[6].strip())

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
  font_size=15
  bar_size=25
  widget_width=150
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

# Make font smaller for cetain groups icons
if int(variables[10]) in [7, 8, 9,10,11,12]:
   groups_font = font_size - 6
else:
   groups_font = font_size 

# Rofi Configuration files
rofi_right = Rofi(rofi_args=['-theme', '~/.config/rofi/right.rasi'])
rofi_network= Rofi(rofi_args=['-theme', '~/.config/rofi/network.rasi'])
rofi_left= Rofi(rofi_args=['-theme', '~/.config/rofi/left.rasi'])
rofi_wallpaper=Rofi(rofi_args=(['rofi', '-show file-browser-extended', '-theme', '~/.config/rofi/sel_wal.rasi', '-file-browser-dir', '~/Pictures/Wallpapers', '-file-browser-stdout']))

### Weather
w_appkey = str(variables[3].strip()) # Get a key here https://home.openweathermap.org/users/sign_up 
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
    '--blur', '20',                 
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
  while i<5:
    if selected_wallpaper != wallpaper:
      subprocess.run(["wpg", light, "-s", str(selected_wallpaper), "--backend", def_backend.lower()])
      subprocess.run(["cp", str(selected_wallpaper), "/usr/local/backgrounds/background.png"])
      subprocess.run(["cp", "-r", str(Path.home() / ".local/share/themes/FlatColor"), "/usr/local/themes/"])
      break
    else:
      selection = random.choice(os.listdir(wallpaper_dir))
      selected_wallpaper = os.path.join(wallpaper_dir, selection)
  
  qtile.reload_config()
  #subprocess.run(["notify-send","-a", " SpectrumOS", "Wallpaper Set to: ", "%s" %selection])

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
  index, key = rofi_left.select(' Backend -> ' + def_backend.capitalize() , options)
  if key == -1 or index == 4:
    rofi_left.close()
  else:
    subprocess.run(["wal", light.lower(), "-i", "/usr/local/backgrounds/background.png", "--backend", "%s" %backend[index].lower()])
    subprocess.run(["wpg", light, "-s", "/usr/local/backgrounds/background.png", "--backend", "%s" %backend[index].lower()])
    subprocess.run(["cp", "-r", home + "/.local/share/themes/FlatColor",  "/usr/local/themes/"])
    variables[2]=backend[index] + "\n"
    with open(home + '/.config/qtile/variables', 'w') as file:
      file.writelines(variables)
    qtile.reload_config()
    subprocess.run(["notify-send","-a", " SpectrumOS", "Color Theme: ", " %s" %backend[index]])

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
      subprocess.run(["notify-send","-a", " SpectrumOS", "Temperature Set to Night Time"])
    elif index == 1:
      os.system('redshift -x')
      subprocess.run(["notify-send","-a", " SpectrumOS", "Temperature Set to Neutral"])
    else:
      os.system('redshift -O 7500k -r -P')
      subprocess.run(["notify-send","-a", " SpectrumOS", "Temperature Set to Cool"])

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
      subprocess.run(["notify-send", "-a", " SpectrumOS", "You can Draw Now"])
    else:
      subprocess.run("gromit-mpx -q",shell=True)

# Logout widget
def session_widget(qtile):
  options = [' Lock',' Log Out', ' Reboot',' Poweroff']
  index, key = rofi_left.select('  Session', options)
  if key == -1:
    rofi_left.close()
  else:
    if index == 0:
      qtile.function(i3lock_colors)
    elif index == 1:
      qtile.shutdown()
    elif index == 2:
      os.system('systemctl reboot')
    else:
      os.system('systemctl poweroff')

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

## Show / Hide all Groups
def show_groups(qtile):
  if hide_unused_groups == True:
    variables[8]=" " + "\n"
    variables[9]="" + "\n"
  else:
    variables[8]="True" + "\n"
    variables[9]="" + "\n"
      
  with open(home + '/.config/qtile/variables', 'w') as file:
    file.writelines(variables)
  qtile.reload_config()
   
## groups_icon_select
def group_icon(qtile):
  options = [
    '->          ', 
    '-> 零 一 二 三 四 五 六 七 八 九', 
    '->          ',
    '->          ',
    '->          ',
    '-> 0 1 2 3 4 5 6 7 8 9',
    '-> : ( ) { : | : & } ;',
    '->          ',
    '->          ',
    '->          ',
    '->          ',
    '->          ',
    '->          ',
    ]
  index, key = rofi_left.select(' Group Icons ', options)
  if key == -1:
    rofi_left.close()
  else:
    variables[10]=str(index) + "\n"
    with open(home + '/.config/qtile/variables', 'w') as file:
      file.writelines(variables)
    qtile.reload_config()
    subprocess.run(["notify-send","-a", " SpectrumOS", "Color Theme: ", " %s" %backend[index]])

## Select Dark or Light Theming
def dark_white(qtile):
  options = [' Dark', ' Light']
  index, key = rofi_left.select(' Theme -> ' + str(variables[7].strip()), options)
  if key == -1 or index == 2:
    rofi_left.close()
  else:
    if index == 0:
      variables[4]="-c" + "\n"
      variables[7]="Dark" + "\n"
      variables[5]="/.config/qtile/themes/dark" + "\n"
      subprocess.run(['cp', home + '/.config/qtile/themes/dark/' + current_theme + ".py", home + '/.config/qtile/theme.py'])
      subprocess.run(["wal", "-i", "/usr/local/backgrounds/background.png", "--backend", "%s" %def_backend])
      subprocess.run(["wpg", "-s", "/usr/local/backgrounds/background.png", "--backend", "%s" %def_backend])
    else:
      variables[4]="-L" + "\n"
      variables[7]="Light" + "\n"
      variables[5]="/.config/qtile/themes/light" + "\n"
      subprocess.run(['cp', home + '/.config/qtile/themes/light/' + current_theme + ".py", home + '/.config/qtile/theme.py'])
      subprocess.run(["wal", "-l", "-i", "/usr/local/backgrounds/background.png", "--backend", "%s" %def_backend])
      subprocess.run(["wpg", "-L", "-A", "-s", "/usr/local/backgrounds/background.png", "--backend", "%s" %def_backend])

    subprocess.run(["cp", "-r", home + "/.local/share/themes/FlatColor",  "/usr/local/themes/"])
    with open(home + '/.config/qtile/variables', 'w') as file:
      file.writelines(variables)
    qtile.reload_config()
    subprocess.run(["notify-send","-a", " SpectrumOS", "Theme changed to: ", "%s" %options[index]])


## Select Bar Position Top or Bottom
def bar_pos(qtile):
  options = ['Top', 'Bottom', 'Toggle Bar']
  index, key = rofi_left.select(' Bar -> ' + bar_position , options)
  if key == -1:
    rofi_left.close()
  else:
    if index == 0:
      variables[6]="top" + "\n"
      subprocess.run(["cp", "-r", home + "/.local/share/themes/FlatColor",  "/usr/local/themes/"])
      with open(home + '/.config/qtile/variables', 'w') as file:
        file.writelines(variables)
      qtile.reload_config()
    elif index == 1:
      variables[6]="bottom" + "\n"
      subprocess.run(["cp", "-r", home + "/.local/share/themes/FlatColor",  "/usr/local/themes/"])
      with open(home + '/.config/qtile/variables', 'w') as file:
        file.writelines(variables)
      qtile.reload_config()
    else:
      qtile.hide_show_bar()

# Change Theme widget
def change_theme(qtile):
  options = theme
  index, key = rofi_left.select('  Theme -> ' + current_theme , options)
  if key == -1:
    rofi_left.close()
  else:
    subprocess.run('rm -rf ~/.config/qtile/theme.py', shell=True)
    variables[1]=theme[index] + "\n"
    new_theme=theme[index] + ".py"
    subprocess.run(['cp', themes_dir + "/" + new_theme, home + '/.config/qtile/theme.py'])
    with open(home + '/.config/qtile/variables', 'w') as file:
      file.writelines(variables)
    qtile.reload_config()
    subprocess.run(["notify-send","-a", " SpectrumOS", " Theme: ", "%s" %theme[index]])
    
# Set random colors to theme
def random_colors(qtile):
  subprocess.run(["wpg", light, "-z", "%s" % wallpaper])
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
    '     Dark/Light Theme (❖ + D)',
    '     Bar Position (❖ +  + W)',
    '     Change Bar Theme (⎇ + W)',
    '    %s Toggle Groups' %str(variables[9].strip()),
    '     Change Groups Icons',
    ' Tools',#10
    '     Notes (❖ + N)',
    '     Apps as Sudo (⎇ + )',
    '     Calculator (❖ + C)',
    '     Network Manager (❖ + B)',
    '     Screenshot (prtnsc)',
    '     Monitor Temperature (❖ +  + O)',
    '     Monitor Layout (❖ +  + X)',
    '     Bluetooth Manager (❖ + T)',
    '     Screen Recorder ( +  + R)',
    ' Miscelaneous',#19
    '     Screen Draw (❖ +  + P)',
    '     Pick Color (❖ + P)',
    '     View Shortcuts (❖ + S)',
    '     Emojis ( +  + )',
    ' Session Menu (❖ + X)',
    '%s' %update_spectrumos,
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
    elif index == 8:
      qtile.function(show_groups)
    elif index == 9:
      qtile.function(group_icon)
    elif index == 11:
      subprocess.Popen(home + '/.local/bin/notesfi', shell=True)
    elif index == 12:
      qtile.spawn('sudo rofi -show drun -show-icons -theme "~/.config/rofi/launcher.rasi"')
    elif index == 13:
      subprocess.run(home + '/.local/bin/calculator')
    elif index == 14:
      qtile.function(network_widget)
    elif index == 15:
      qtile.function(screenshot)
    elif index == 16:
      qtile.function(nightLight_widget)
    elif index == 17:
      subprocess.run(home + '/.local/bin/change_display')
    elif index == 18:
      subprocess.run(home + '/.local/bin/bluet')
    elif index == 19:
      subprocess.run(home + '/.local/bin/recorder')
    elif index == 21:
      qtile.function(draw_widget)
    elif index == 22:
      qtile.function(fargewidget)
    elif index == 23:
      qtile.function(shortcuts)
    elif index == 24:
      qtile.function(emojis)
    elif index == 25:
      qtile.function(session_widget)
    elif index == 26:
      subprocess.run(home + '/.local/bin/updater')
    

widget_defaults = dict(
    font=main_font,
    fontsize=font_size,
    padding=3,
)



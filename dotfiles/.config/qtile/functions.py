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
import os, socket, json, subprocess, random, requests
from os.path import expanduser
from libqtile import qtile, bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from qtile_extras import widget
from qtile_extras.widget.decorations import (RectDecoration, PowerLineDecoration, BorderDecoration)
from rofi import Rofi
from pathlib import Path
from qtile_extras.popup.toolkit import (PopupImage, PopupText, PopupRelativeLayout, PopupWidget)

#### Variables ####

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
prompt = ":".format(os.environ["USER"], socket.gethostname()) # Format of the prompt

## Import Persistent Variables
file = open(home + '/.config/qtile/variables', 'r')
variables=file.readlines()

# Wallpapers / Theming
wallpaper_dir= home + '/Pictures/Wallpapers/' # Wallpapers folders
light=str(variables[3].strip()) # Optin for light themes

# Diferenciator, this will get added to generate a slightly different pallete
differentiator = '090909' 

# Theme
current_theme=str(variables[0].strip())
themes_dir = home + str(variables[4].strip())
theme_dest = (home + "/.config/qtile/theme.py")
theme_file = themes_dir + "/" + current_theme
theme=['QARSlp', 'nice', 'slash', 'minimal', 'Monochrome', 'no_bar']

# Pywal backends Options: Wal, Colorz, Colorthief, Haishoku
def_backend=str(variables[1].strip()) # Default Color Scheme for random wallpaper
backend=['Wal', 'Colorz', 'Colorthief','Haishoku']

## Margins
layout_margin=10 # Layout margins
single_layout_margin=10 # Single window margin 
## Borders
layout_border_width=4 # Layout border width
single_border_width=4 # Single border width

# Bar Position
bar_position=str(variables[5].strip())

#Widgets
widget_width=200 #Width of widgets varies depending the resolution

# Get current screen resolution
resolution = os.popen('xdpyinfo | awk "/dimensions/{print $2}"').read()
xres = resolution[17:21]
yres = resolution[22:26]

# Set Bar and font sizes for different resolutions
if xres == "3840" and yres == "2160": #4k
  layout_margin=10
  single_layout_margin=10  
  layout_border_width=5
  single_border_width=5
  font_size=20
  bar_size=30
  widget_width=400
  if bar_position == "bottom":
    bar_margin=[0,10,5,10]
  else:
    bar_margin=[5,10,0,10]
elif xres == "1920" and yres == "1080": #FullHD
  layout_margin=5
  single_layout_margin=5  
  layout_border_width=3 
  single_border_width=3
  font_size=16
  bar_size=25
  widget_width=220
  if bar_position == "bottom":
    bar_margin=[0,5,5,5]
  else:
    bar_margin=[5,5,0,5]
else: # 1366 x 768 Macbook air 11"
  layout_margin=2
  single_layout_margin=2  
  layout_border_width=2
  single_border_width=2
  font_size=13
  bar_size=20
  widget_width=100
  bar_margin=[0,0,0,0]

# Rofi Configuration files
rofi_session = Rofi(rofi_args=['-theme', '~/.config/rofi/logout.rasi'])
rofi_display = Rofi(rofi_args=['-theme', '~/.config/rofi/display.rasi'])
rofi_network= Rofi(rofi_args=['-theme', '~/.config/rofi/network.rasi'])
rofi_backend= Rofi(rofi_args=['-theme', '~/.config/rofi/backend.rasi'])
rofi_websearch= Rofi(rofi_args=['-theme', '~/.config/rofi/websearch.rasi'])
rofi_screenshot= Rofi(rofi_args=['-theme', '~/.config/rofi/screenshot.rasi'])
rofi_fargewidget= Rofi(rofi_args=['-theme', '~/.config/rofi/fargewidget.rasi'])

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
       qtile.spawn(app)
    else:
      qtile.groups_map[group].cmd_toscreen(toggle=False)
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

# Transparent for bars and widgets
transparent=color[0] + "00"

# Set Random Wallpaper
def change_wallpaper(qtile):
  selection = random.choice(os.listdir(wallpaper_dir))
  selected_wallpaper = os.path.join(wallpaper_dir, selection)
  wallpaper_file = selected_wallpaper
  subprocess.run(["wpg", light, "-s", str(wallpaper_file), "--backend", def_backend.lower()])
  subprocess.run(["cp", str(wallpaper_file), "/usr/local/backgrounds/background.png"])
  subprocess.run(["cp", "-r", str(Path.home() / ".local/share/themes/FlatColor"), "/usr/local/themes/"])
  qtile.reload_config()

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

## Select Dark or Light Theming
def dark_white(qtile):
  options = ['Dark', 'Light']
  index, key = rofi_backend.select('  Dark or  Light Theme', options)
  if key == -1 or index == 2:
    rofi_backend.close()
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


## Select Bar Position Top or Bottom
def bar_pos(qtile):
  options = ['Top', 'Bottom']
  index, key = rofi_backend.select('  Top Bar or  Bottom Bar -> ' + bar_position , options)
  if key == -1 or index == 2:
    rofi_backend.close()
  else:
    if index == 0:
      variables[5]="top"
    else:
      variables[5]="bottom"

    subprocess.run(["cp", "-r", home + "/.local/share/themes/FlatColor",  "/usr/local/themes/"])
    with open(home + '/.config/qtile/variables', 'w') as file:
      file.writelines(variables)
    qtile.reload_config()
      
## Set default backend
def set_default_backend(qtile):
  options = backend
  index, key = rofi_backend.select('  Backend -  ' + def_backend , options)
  if key == -1 or index == 4:
    rofi_backend.close()
  else:
    subprocess.run(["wal", light.lower(), "-i", "/usr/local/backgrounds/background.png", "--backend", "%s" %backend[index].lower()])
    subprocess.run(["wpg", light, "-s", "/usr/local/backgrounds/background.png", "--backend", "%s" %backend[index].lower()])
    subprocess.run(["cp", "-r", home + "/.local/share/themes/FlatColor",  "/usr/local/themes/"])
    variables[1]=backend[index] + "\n"
    with open(home + '/.config/qtile/variables', 'w') as file:
      file.writelines(variables)
    qtile.reload_config()

# Display Shortcuts widget
def shortcuts(qtile):
  subprocess.run("cat ~/.shortcuts | rofi -theme '~/.config/rofi/left_bar.rasi' -i -dmenu -p ' Shortcuts:'",shell=True)

# NightLight widget
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

# Farge Widget
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

# Logout widget
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
      os.system('i3lock-fancy -p -f Fira-Code-Medium -t "Password?"')

# Network Widget
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
  options = [connected,'  Bandwith Monitor (CLI)', ' Network Manager (CLI)']
  index, key = rofi_network.select(wifi_icon + "  IP " + private_ip + " ->" + "  IP" + public_ip, options)
  if key == -1:
    rofi_network.close()
  else:
    if index ==0:
      subprocess.run("nmcli radio wifi " + active, shell=True)
    elif index==1:
      qtile.cmd_spawn(terminal + ' -e bmon')
    else:
      qtile.cmd_spawn(terminal + ' -e nmtui')

# Change Theme widget
def change_theme(qtile):
  options = theme
  index, key = rofi_backend.select('  Theme -  ' + current_theme , options)
  if key == -1:
    rofi_backend.close()
  else:
    subprocess.run('rm -rf ~/.config/qtile/theme.py', shell=True)
    variables[0]=theme[index] + "\n"
    new_theme=theme[index] + ".py"
    subprocess.run(['cp', themes_dir + "/" + new_theme, home + '/.config/qtile/theme.py'])
    with open(home + '/.config/qtile/variables', 'w') as file:
      file.writelines(variables)
    qtile.reload_config()
    
# Set random colors to theme
def random_colors(qtile):
  subprocess.run(["wpg", "-z", "%s" % wallpaper])
  subprocess.run(["wpg", "-s", "%s" % wallpaper])
  subprocess.run(["rm", "-rf", "%s" %wallpaper + "_wal_sample.png"])
  qtile.reload_config()

# Screenshot widget
def screenshot(qtile):
  options = [' Screen', ' Window', ' Area', ' 5s Screen']
  index, key = rofi_screenshot.select('  Screenshot', options)
  if key == -1:
    rofi_screenshot.close()
  else:
    if index ==0:
      subprocess.run("flameshot full --path ~/Pictures/Screenshot.png --delay 500",shell=True)
    elif index==1:
      subprocess.run("scrot -u 'Screenshot_%S-%m-%y.png' -e 'mv $f ~/Pictures/ #; feh -F ~/Pictures/$f' && dunstify ' Window Picture Taken!'",shell=True)
    elif index==2:
      subprocess.run("flameshot gui --path ~/Pictures/Screenshot.png --delay 400",shell=True)
    else:
      subprocess.run("flameshot full --path ~/Pictures/Screenshot.png --delay 5000",shell=True)

## Keys
keys = [
    #Basics
    Key([alt], "r",lazy.function(change_wallpaper)), # Set random wallpaper / colors to entire system
    Key([mod], "Return", lazy.spawn(terminal)), # Open Terminal
    Key([mod, "shift"], "Return", lazy.spawn('rofi -theme "~/.config/rofi/launcher.rasi" -show run')), # Open Rofi launcher
    Key([mod], "r", lazy.spawncmd()), # Launch Prompt
    Key([mod], "q",lazy.window.kill()), # Close Window 
    Key([mod, "shift"], "r",lazy.reload_config()), # Restart Qtile
    Key([mod, "shift"], "q",lazy.shutdown()), # Logout         
    Key([alt], "Escape", lazy.spawn('xkill')), # Click window to close

    # Widgets
    Key([mod],"c",lazy.function(shortcuts)), # Shortcuts widget
    Key([mod],"d",lazy.function(dark_white)), # Select Dark or Light Theme
    Key([mod, "shift"],"w",lazy.function(bar_pos)), # Set bar position
    Key([mod, "shift"],"o",lazy.function(nightLight_widget)), # Set night light
    Key([mod],"p",lazy.function(fargewidget)), # Color Picker Widget
    Key([alt], "Return", lazy.spawn('rofi  -theme "~/.config/rofi/left_bar.rasi" -show find -modi find:~/.local/bin/finder')), # Search for files and folders
    Key([mod],"f",lazy.spawn(home + '/.local/bin/wsearch')), # WEB Search widget
    Key([mod, "shift"],"f",lazy.spawn('rofi  -theme "~/.config/rofi/filesfolders.rasi" -show find -modi find:~/.local/bin/finder')), # Search files and folders
    Key([mod],"t",lazy.spawn('rofi  -theme "~/.config/rofi/tasks.rasi" -show tasks:task')), # Task list
    Key([mod],"x",lazy.function(session_widget)), # Log out
    Key([mod],"b",lazy.function(network_widget)), # Network Settings
    Key([alt, "shift"],"w",lazy.function(set_default_backend)), # Set Default Color Scheme
    Key([alt],"w",lazy.function(change_theme)), # Change Theme
    Key([mod, "shift"],"x",lazy.spawn(home + '/.local/bin/change_display')),# Monitor modes Widget
    Key([alt, "shift"], "r",lazy.function(random_colors)), # Set randwom wallpaper / colors to entire system

    # Layouts
    Key([mod], "Tab",lazy.layout.down()), # Change focus of windows down
    Key([mod, "shift"], "Tab",lazy.layout.up()), # Change focus of windows up
    Key([alt], "Tab", lazy.layout.shuffle_down()), # Swap Left Down
    Key([alt, "shift"], "Tab", lazy.layout.shuffle_up()), # Swap Right Up
    Key([mod], 'period', lazy.next_screen()), # Send Cursor to next screen

    # Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("sudo xbacklight -inc 5")), # Aument Brightness
    Key(["control", alt], "p", lazy.spawn("sudo xbacklight -inc 5")), # Aument Brightness
    Key([], "XF86MonBrightnessDown", lazy.spawn("sudo xbacklight -dec 5")), # Lower Brightness
    Key(["control", alt], "o", lazy.spawn("sudo xbacklight -dec 5")),

    # Volume
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")), # Mute
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -q set Master 5%-")), # Lower Volume
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -q set Master 5%+")), # Raise Volume

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
    Key([mod], "n", lazy.layout.normalize()),
    Key([mod], "o", lazy.layout.maximize()),
    Key([mod, "shift"], "space", lazy.layout.flip()),

    # Keyboard
    Key([alt], "space", lazy.widget["keyboardlayout"].next_keyboard()), # Change Keyboard Layout

    # Screenshots
    Key([], "Print", lazy.function(screenshot)),

    # Lock Screen
    Key(["control", alt],"l",lazy.spawn('i3lock-fancy -p -f Fira-Code-Medium -t "Password?"')), # Run i3lock 

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
group_labels=["","","","","","","","","",""] # Custom
####

group_layouts=["spiral", "spiral", "spiral", "spiral","spiral", "spiral", "spiral","spiral", "spiral", "floating"]
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
    layout.MonadTall(max_ratio=0.90,ratio=0.75,**layout_theme),
    layout.Floating(**layout_theme),
    ]
layouts = init_layouts()

widget_defaults = dict(
    font=main_font,
    fontsize=font_size,
    padding=3,
)

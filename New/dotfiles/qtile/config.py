# _______  _______  ______  _______  __        
#|       ||   _   ||   __ \|     __||  |.-----.
#|   -  _||       ||      <|__     ||  ||  _  |
#|_______||___|___||___|__||_______||__||   __|
#                                       |__|   
# QARSlp Qtile + Arch Ricing Script
# By: gibranlp <thisdoesnotwork@gibranlp.dev>
# MIT licence

# Qtile Config Gibranlp

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
from numpy import size
from pyparsing import cpp_style_comment

# Variables

## Version
ver = 'v0.0.1' # Current dotfiles version

## Fonts
m_font = "Fira Code Medium" # Font in use for the entire system
a_font = "Font Awesome 6 Pro Solid" # Font for all the Special Characters

## Monitor Resolution
res = "4k" # 4k or FullHD this will change font size and bar size and other things

## Keys ####
mod = "mod4" # Super / Command / Windows key
alt = "mod1" # Alt key

## Software
term = "alacritty" # Terminal in use

## System
home = os.path.expanduser('~') # Path for use in folders
prompt = ":".format(os.environ["USER"], socket.gethostname()) # Format of the prompt

## Theming
theme=['Default'] # Themes available
backend=['Wal', 'Colorz', 'Colorthief','Haishoku', 'Schemer2'] #Backends available
wall_dir = home + '/Cloud/Wallpapers/4K'

## Custom Bar / Font Size
f_size = 20 # Bars Font size
i_size = 18 # Tray Icon size
b_size = 30 # Bar size

## Margins and Borders
l_margin = 10 # Layout margins
sl_margin = 10 # Single window margin 
l_border_w = 4 # Layout border width
s_border_w = 4 # Single border width

## Theming
def_Backend= "Wal"
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

## Resolution change
if res == "4k":
  f_size = 20 # Bars Font size
  i_size = 18 # Tray Icon size
  b_size = 30 # Bar size
else:
  f_size = 16 # Bars Font size
  i_size = 18 # Tray Icon size
  b_size = 25 # Bar size  
## Get network device in use
def get_net_dev():
  get_dev = "ip addr show | awk '/inet.*brd/{print $NF; exit}'"
  ps = subprocess.Popen(get_dev,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
  output = ps.communicate()[0].decode('ascii').strip()
  return(output)

wifi = get_net_dev()

# Set the the right icon for network device
if wifi.startswith('w'):
  wifi_icon=''
else:
  wifi_icon=''

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
internet = 'Yay Internet is Working!!! =D'
if public_ip.startswith('0'):
  internet = "∅ No internet connection =("
  
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

## Set Random Wallpaper
def set_rand_wallpaper(qtile):
  dir = wall_dir
  selection = random.choice(os.listdir(dir))
  rand_wallpaper = os.path.join(dir, selection)
  while(True):
    if rand_wallpaper != wallpaper:
      subprocess.run(["wal", "-i", "%s" % rand_wallpaper, "--backend", "%s" %def_Backend.lower()])
      qtile.cmd_reload_config()
      break
    else:
      subprocess.run(["wal", "-i", "%s" % rand_wallpaper, "--backend", "%s" %def_Backend.lower()])
      qtile.cmd_reload_config()
      break
  
# Rofi Menus

## Change Color Backend
def change_color_scheme(qtile):
  options = backend
  index, key = rofi_backend.select('  Color Scheme', options)
  if key == -1 or index == 4:
    rofi_backend.close()
  else:
    subprocess.run('wal -w' + ' --backend ' + backend[index].lower(), shell=True)
    qtile.cmd_reload_config()

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
    subprocess.run('\cp ~/.config/qtile/themes/%s/theme.py ~/.config/qtile/'% theme[index], shell=True)
    subprocess.run('\cp ~/.config/qtile/themes/%s/rofi/* ~/.config/rofi/'% theme[index], shell=True)
    subprocess.run('\cp ~/.config/qtile/themes/%s/picom/* ~/.config/picom/'% theme[index], shell=True)
    qtile.cmd_reload_config()

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

# Qtile Configuration

## Groups
groups = []
g_names = ["1","2","3","4","5","6","7","8","9"]
g_labels=["","","","","","","","",""]
g_layouts=["monadtall", "monadthreecol", "matrix","monadtall", "monadtall", "monadthreecol","monadthreecol", "monadtall", "monadtall"]
g_matches=[
  [Match(wm_class=[])],
  [Match(wm_class=[])],
  [Match(wm_class=[])],
  [Match(wm_class=[])],
  [Match(wm_class=[])],
  [Match(wm_class=[])],
  [Match(wm_class=[])],
  [Match(wm_class=[])],
  [Match(wm_class=[])],
 ]

for i in range(len(g_names)):
  groups.append(
    Group(
      name=g_names[i],
      matches=g_matches[i],
      layout=g_layouts[i].lower(),
      label=g_labels[i],
  ))

## Layouts
def init_layout_theme():
  return {"font":m_font,
    "fontsize":f_size,
    "margin":l_margin,
    "border_on_single":False,
    "border_width":l_border_w,
    "border_normal":color[0],
    "border_focus":color[2],
    "single_margin":sl_margin,
    "single_border_width":s_border_w,
    "change_ratio":"after_current",
    }

layout_theme = init_layout_theme()

def init_layouts():
  return [
    layout.MonadTall(max_ratio=0.90,ratio=0.80,**layout_theme),
    layout.MonadWide(max_ratio=0.90,ratio=0.80,**layout_theme),
    layout.Matrix(**layout_theme),
    layout.MonadThreeCol(**layout_theme),     
    ]
layouts = init_layouts()

##########################################################################

# Theme

#### Widgets ####
def init_widgets_defaults():
    return dict(font=m_font,fontsize=f_size)

def init_widgets_top():
    widgets_top = [
      ## Groups
      widget.GroupBox(
        background=color[0],
        font=a_font,
        disable_drag=True,
        hide_unused=True,
        padding_x=3,
        borderwidth=0,
        active=color[2], #Program opened in that group
        inactive=color[8], # Empty Group
        rounded=False,
        highlight_method="text",
        this_current_screen_border=color[9],
        center_aligned = True,
        other_current_screen_border=color[9],
        block_highlight_text_color=color[2],    
        urgent_border=color[5],
      ),
      widget.Prompt(
        prompt=prompt,
        foreground=color[14],
        cursor_color=color[14],
        visual_bell_color=[14],
        visual_bell_time=0.2,
        background=color[0],
      ),
      widget.CurrentLayout(
        foreground=color[1],
        background=color[0],
      ),
      widget.TextBox(
        background=color[0],
        foreground=color[3],
        text="",
      ),
      widget.ThermalSensor(
        background=color[0],
        foreground=color[3],
        foreground_alert="ffcccc",
        metric=True,
        update_interval=1,
       tag_sensor='Tctl'
      ),
      widget.TextBox(
        background=color[0],
        foreground=color[10],
        text="",
      ),
      widget.NvidiaSensors(
        decorations=[RectDecoration(colour=color[0], radius=[0,10,10,0], filled=True)],
        foreground=color[10],
      ),
      widget.Spacer(
        length=bar.STRETCH,
        background='ffffff00',
      ),
      widget.Clock(
        foreground=color[4],
        format="%a %d %H:%M",
        mouse_callbacks={'Button1': lazy.group['scratchpad'].dropdown_toggle('khal')},
        update_interval=1,
        decorations=[RectDecoration(colour=color[0], radius=[10,0,0,10], filled=True)],
      ),
      widget.OpenWeather(
        font=a_font,
        background=color[0],
        app_key=w_appkey,
        cityid=w_cityid,
        weather_symbols={
          "Unknown": "",
          "01d": "",
          "01n": "🌕",
          "02d": "",
          "02n": "",
          "03d": "",
          "03n": "",
          "04d": "",
          "04n": "",
          "09d": "⛆",
          "09n": "⛆",
          "10d": "",
          "10n": "",
          "11d": "🌩",
          "11n": "🌩",
          "13d": "❄",
          "13n": "❄",
          "50d": "🌫",
          "50n": "🌫",
          },
          format='{icon}',
          foreground=color[13],
          metric=True,
          update_interval=600,
      ),
      widget.OpenWeather(
        app_key=w_appkey,
        cityid=w_cityid,
        foreground=color[13],
        format='{temp}°{units_temperature}',
        metric=True,
        update_interval=600,
        decorations=[RectDecoration(colour=color[0], radius=[0,10,10,0], filled=True)],
      ),
      widget.Spacer(
        length=bar.STRETCH,
        background='ffffff00',
      ),
      #widget.Systray(
       # background="00000000",
       # icon_size=i_size,
      #),
      widget.TextBox(
        decorations=[RectDecoration(colour=color[0], radius=[10,0,0,10], filled=True)],
        foreground=color[12],
        text="",
        mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(term + " -e cava")},
      ),
      ## Cmus
      widget.Mpris2(
        background=color[0],
        foreground=color[1],
        name='cmus',
        objname='org.mpris.MediaPlayer2.cmus',
        scroll_chars=50,
        stop_pause_text='',
        display_metadata=['xesam:title', 'xesam:artist'],
        scroll_interval=0.5,
        scroll_wait_intervals=2000,    
      ),
      ## Vlc
      widget.Mpris2(
        background=color[0],
        foreground=color[1],
        name='vlc',
        objname='org.mpris.MediaPlayer2.vlc',
        scroll_chars=50,
        stop_pause_text='',
        display_metadata=['xesam:title', 'xesam:artist'],
        scroll_interval=0.5,
        scroll_wait_intervals=2000,
      ),
      widget.TextBox(
        background=color[0],
        foreground=color[4],
        text="",
        mouse_callbacks={'Button1':lambda: qtile.cmd_function(prev)},
      ),
      widget.TextBox(
        background=color[0],
        foreground=color[4],
        text="",
        mouse_callbacks={'Button1':lambda: qtile.cmd_function(nexts)},
      ),
      ## Network
      widget.WidgetBox(
        background=color[0],
        text_closed=" " + wifi_icon,
        text_open='  ',
        foreground=color[7],
        widgets=[widget.TextBox(
          background=color[0],
          text='  '+private_ip,
          foreground=color[7],
          mouse_callbacks={'Button1':lambda: qtile.cmd_function(network_widget)}
        ),
        widget.TextBox(
          background=color[0],
          text='  '+public_ip + " " + wifi_icon,
          foreground=color[7],
          mouse_callbacks={'Button1':lambda: qtile.cmd_function(network_widget)}
        ),]
      ),
      widget.Wlan(
        background=color[0],
        interface=wifi,
        format='{essid} {percent:2.0%}',
        disconnected_message='Unplugged',
        foreground=color[7],
        mouse_callbacks={'Button1':lambda: qtile.cmd_function(network_widget)}
      ),
      widget.Net(
        background=color[0],
        interface=wifi,
        format='{down}',
        foreground=color[7],
        use_bits=True,
        mouse_callbacks={'Button1':lambda: qtile.cmd_function(network_widget)}
      ),
      widget.TextBox(
        background=color[0],
        font=a_font,
        text="",
        foreground=color[12],
      ),
      widget.KeyboardLayout(
        background=color[0],
        configured_keyboards=['us intl', 'latam'],
        foreground=color[12],
      ),
      widget.TextBox(
        background=color[0],
        font=a_font,
        text="  ",
        foreground=color[11],
        padding=0,
        mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('pavucontrol')}
      ),
      widget.ALSAWidget(
        background=color[0],
        device='Master',
        bar_colour_high=color[11],
        bar_colour_loud=color[11],
        bar_colour_normal=color[11],
        bar_colour_mute=color[11],
        hide_interval=3,
        update_interval=0.1,
        bar_width=60,
        mode='bar',
        foreground=color[14],
      ),
      widget.TextBox(
        background=color[0],
        foreground=color[2],
        text="",
      ),
      widget.Bluetooth(
        background=color[0],
        foreground=color[2],
        hci='/dev_28_EC_9A_9B_64_72',
        mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('blueman-manager')}
      ),
      ## Lock, Logout, Poweroff
      widget.UPowerWidget(
        border_charge_colour=color[7],
        border_colour=color[5],
        border_critical_colour='#cc0000',
        fill_critical='#cc0000',
        fill_low='#FF5511',
        fill_normal=color[5],
        foregound=color[5],
        background=color[0],
      ),
      widget.TextBox(
        decorations=[RectDecoration(colour=color[0], radius=[0,10,10,0], filled=True)],
        font=a_font,
        foreground=color[8],
        text="",
        mouse_callbacks={'Button1': lambda: qtile.cmd_function(session_widget)}
      ),
    ]
    return widgets_top

#### End Widgets ####

##### Screens #####

def init_widgets_screen_top():
    widgets_screen_top = init_widgets_top()
    return widgets_screen_top

def init_screens():
    return [
        Screen(
            bottom=bar.Bar(
                background="00000000",
                widgets=widgets_screen_top,  
                size=b_size,
                margin=[0,10,10,10]
                ),
            ),
        Screen(bottom=bar.Bar(
                background="00000000",
                widgets=widgets_screen_top,  
                size=b_size,
                margin=[0,5,5,5]
                ),
        ),
        ]

#### End Screens ####

widget_defaults = init_widgets_defaults()
widgets_top = init_widgets_top()
widgets_screen_top = init_widgets_screen_top()
screens = init_screens()

##########################################################################
# Keys

def init_keys():
  keys = [ 
    ##Basics
    Key([alt], "r",lazy.function(set_rand_wallpaper)), # Set randwom wallpaper / colors to entire system

    Key([mod], "Return", lazy.spawn(term)), # Open Terminal
            
    Key([mod, "shift"], "Return", lazy.spawn('rofi -theme "~/.config/rofi/launcher.rasi" -show drun')), # Open Rofi launcher
            
    Key([mod, "mod1"], "Return", lazy.spawn('sudo rofi -theme "~/.config/rofi/launcher.rasi" -show drun')), # Open Rofi Launcher as Sudo

    Key([mod], "r", lazy.spawncmd()), # Launch Prompt
            
    Key([mod], "q",lazy.window.kill()), # Close Window 
         
    Key([mod, "shift"], "r",lazy.reload_config()), # Restart Qtile
           
    Key([mod, "shift"], "q",lazy.shutdown()), # Logout 
            
    Key([mod], "Escape", lazy.spawn('xkill')), # Click window to close
            
    ## Widgets
    Key([mod],"h",lazy.function(shortcuts)), # Shortcuts widget
    Key([mod],"o",lazy.function(nightLight_widget)),
    Key([mod],"p",lazy.function(fargewidget)), # Color Picker Widget
    Key([alt], "Return", lazy.spawn('rofi  -theme "~/.config/rofi/left_bar.rasi" -show find -modi find:~/.local/bin/finder')), # Search for files and folders
    Key([mod],"f",lazy.spawn(home + '/.local/bin/wsearch')), # WEB Search widget
    Key([mod, "shift"],"f",lazy.spawn('rofi  -theme "~/.config/rofi/filesfolders.rasi" -show find -modi find:~/.local/bin/finder')), # Search files and folders
    Key([mod],"x",lazy.function(session_widget)), # Log out
    Key([mod],"n",lazy.function(network_widget)), # Network Settings
    Key([alt, "shift"],"r",lazy.function(change_color_scheme)), # Change Color Scheme
    Key([alt],"w",lazy.function(change_theme)), # Change Theme
    Key([mod, "shift"],"x",lazy.spawn(home + '/.local/bin/change_display')),# Monitor modes Widget

    ## Theming
    Key([alt], "r",lazy.function(set_rand_wallpaper)), # Set randwom wallpaper / colors to entire system

    ## Apps
    Key([mod, "shift"],"e",lazy.spawn(term + ' -e /usr/bin/zsh -c ranger')), 
    
    #File manager
    Key([mod, "shift"],"s",lazy.function(app_or_group('7', term + ' -e cmus'))), #Open Cmus en the group 7
    Key([mod, "shift"],"m",lazy.spawn('thunderbird')), # Open Thunderbird
    Key([mod],"g",lazy.spawn('firefox')), # Open Firefox   
    Key([mod, "shift"],"f",lazy.spawn('google-chrome-stable')), # Open Google Chrome    
    Key([mod, "shift"],"c",lazy.spawn('code')), # Open Visual Code Studio
          
    ## Layouts
    Key([mod], "Tab",lazy.layout.next()), # Change focus of windows down
    Key([mod, "shift"], "Tab",lazy.layout.up()), # Change focus of windows up
    Key([alt], "Tab", lazy.layout.swap_left()), # Swap Left Down
    Key([alt, "shift"], "Tab", lazy.layout.swap_right()), # Swap Right Up
    Key([alt], "space", lazy.widget["keyboardlayout"].next_keyboard()), # Change Keyboard Layout
    Key([mod], 'period', lazy.next_screen()), # Send Cursor to next screen

    ## Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("xbacklight -inc 5")), # Aument Brightness
    Key([], "XF86MonBrightnessDown", lazy.spawn("xbacklight -dec 5")), # Lower Brightness

    ## Volume
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")), # Mute
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -q set Master 5%-")), # Lower Volume
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -q set Master 5%+")), # Raise Volume

    ## Media Control
    Key([], "XF86AudioPlay", lazy.function(play_pause)), # Play Pause
    Key([], "XF86AudioNext", lazy.function(nexts)), # Next song
    Key([], "XF86AudioPrev", lazy.function(prev)), # Previous Song

    ## Window hotkeys
    Key([alt], "f", lazy.window.toggle_fullscreen()), # Toggle Current window Full screen
    Key([alt, "shift"], "f", lazy.window.toggle_floating()), # Toggle current window floating
    Key([mod], "space", lazy.next_layout()), # Cycle layouts

    ## Resize windows
    Key([mod, alt], "w", lazy.layout.grow()), # Grow window
    Key([mod, alt], "s", lazy.layout.shrink()), # Shrink window
    Key([mod, "shift"], "space", lazy.layout.flip()), # Flip Layout

    ## Change focus
    Key([mod], "Up", lazy.layout.up()), 
    Key([mod], "Down", lazy.layout.down()),
    Key([mod], "Left", lazy.layout.left()),
    Key([mod], "Right", lazy.layout.right()),
           
    ##  Dunst Shortuts
    Key(["control"], "space",  lazy.spawn("dunstctl close")), # Clear Last Notification
    Key(["control", "shift"], "space",  lazy.spawn("dunstctl close-all")), # Clear All Notificatins
    Key(["control", "shift"], "n",  lazy.spawn("dunstctl  history-pop")), # Show Notificaction history

    ## Screenshots
    Key([], "Print", lazy.function(screenshot)),
  ] # Screenshot widget

  for i in groups:
    keys.append(Key([mod], i.name, lazy.group[i.name].toscreen()))
    keys.append(Key([mod, 'shift'], i.name, lazy.window.togroup(i.name)))
  return keys
#### End Keys ####

##### Mouse/Keyboard #####
def init_mouse():
  return [Drag([mod], "Button1", lazy.window.set_position_floating(),      # Move floating windows
  start=lazy.window.get_position()),
  Drag([mod], "Button2", lazy.window.set_size_floating(),          # Resize floating windows
  start=lazy.window.get_size()),
  Click([mod, "shift"], "Button1", lazy.window.bring_to_front())]  # Bring floating window to front

keys = init_keys()
mouse = init_mouse()

wmname = "QARSlp"
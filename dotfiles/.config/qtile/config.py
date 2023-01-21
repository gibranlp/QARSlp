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
from qtile_extras.widget.decorations import RectDecoration
from rofi import Rofi

# Variables
# Modifiers
mod = "mod4"
alt = "mod1"

## Fonts
main_font = "Fira Code Medium" # Font in use for the entire system
awesome_font = "Font Awesome 6 Pro Solid" # Font for all the Special Characters
font_size=17

# Terminal 
terminal = "alacritty"

#Home Path
home = os.path.expanduser('~') # Path for use in folders
prompt = ":".format(os.environ["USER"], socket.gethostname()) # Format of the prompt

# Wallpapers / Theming
wallpaper_dir=home + '/Pictures/Wallpapers/'
# Pywal backends Options: Wal, Colorz, Colorthief, Haishoku
def_Backend="Wal"
backend=['Wal', 'Colorz', 'Colorthief','Haishoku']
transparent="00000000"
rofi_session = Rofi(rofi_args=['-theme', '~/.config/rofi/logout.rasi'])
rofi_display = Rofi(rofi_args=['-theme', '~/.config/rofi/display.rasi'])
rofi_network= Rofi(rofi_args=['-theme', '~/.config/rofi/network.rasi'])
rofi_backend= Rofi(rofi_args=['-theme', '~/.config/rofi/backend.rasi'])
rofi_websearch= Rofi(rofi_args=['-theme', '~/.config/rofi/websearch.rasi'])
rofi_screenshot= Rofi(rofi_args=['-theme', '~/.config/rofi/screenshot.rasi'])
rofi_fargewidget= Rofi(rofi_args=['-theme', '~/.config/rofi/fargewidget.rasi'])

## Margins and Borders
layout_margin=5 # Layout margins
single_layout_margin=5 # Single window margin 
layout_border_width=3 # Layout border width
single_border_width=3 # Single border width

### Weather
w_appkey = "e45a0f07f0c675b273ef8636663941db" # Get a key here https://home.openweathermap.org/users/sign_up 
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

# Set Random Wallpaper
selection = random.choice(os.listdir(wallpaper_dir))
rand_wallpaper = os.path.join(wallpaper_dir, selection)
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

## Get network device in use
def get_net_dev():
  get_dev = "ip addr show | awk '/inet.*brd/{print $NF; exit}'"
  ps = subprocess.Popen(get_dev,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
  output = ps.communicate()[0].decode('ascii').strip()
  return(output)

wifi = get_net_dev()

# Set Ethernet or Wifi Icon according
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

## Check Internet Connection
internet = ' Connected! -> IP: '
if public_ip.startswith('0'):
  internet = "∅ No internet connection "

## Rofi Widgets

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
      os.system('dm-tool switch-to-greeter')

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
  options = [connected,' Bandwith Monitor (CLI)', ' Network Manager (CLI)']
  index, key = rofi_network.select(wifi_icon + internet + public_ip, options)
  if key == -1:
    rofi_network.close()
  else:
    if index ==0:
      subprocess.run("nmcli radio wifi " + active, shell=True)
    elif index==1:
      qtile.cmd_spawn(terminal + ' -e bmon')
    else:
      qtile.cmd_spawn(terminal + ' -e nmtui')

# Change Color Backend
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

# Change Theme widget
def change_theme(qtile):
  options = theme
  index, key = rofi_backend.select('  Select Theme', options)
  if key == -1:
    rofi_backend.close()
  else:
    subprocess.run('rm -rf ~/.config/qtile/theme.py', shell=True)
    subprocess.run('\cp ~/.config/qtile/themes/%s ~/.config/qtile/theme.py'% theme[index], shell=True)
    qtile.reload_config()

# Set random colorts to theme
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
      subprocess.run("scrot -d 1 'Screenshot_%S-%m-%y.png' -e 'mv $f ~/Pictures/ #; feh -F ~/Pictures/$f' && dunstify ' Screen Picture Taken!'",shell=True)
    elif index==1:
      subprocess.run("scrot -u 'Screenshot_%S-%m-%y.png' -e 'mv $f ~/Pictures/ #; feh -F ~/Pictures/$f' && dunstify ' Window Picture Taken!'",shell=True)
    elif index==2:
      subprocess.run("scrot -s 'Screenshot_%S-%m-%y.png' -e 'mv $f ~/Pictures/ #; feh -F ~/Pictures/$f' && dunstify ' Area Picture Taken!'",shell=True)
    else:
      subprocess.run("scrot -d 5 -c 'Screenshot_%S-%m-%y.png' -e 'mv $f ~/Pictures/ #; feh -F ~/Pictures/$f' && dunstify ' Timed Screenshot Taken!'",shell=True)


## Keys
keys = [
    #Basics
    Key([alt], "r",lazy.function(set_rand_wallpaper)), # Set randwom wallpaper / colors to entire system
    Key([mod], "Return", lazy.spawn(terminal)), # Open Terminal
    Key([mod, "shift"], "Return", lazy.spawn('rofi -theme "~/.config/rofi/launcher.rasi" -show drun')), # Open Rofi launcher
    Key([mod], "r", lazy.spawncmd()), # Launch Prompt
    Key([mod], "q",lazy.window.kill()), # Close Window 
    Key([mod, "shift"], "r",lazy.reload_config()), # Restart Qtile
    Key([mod, "shift"], "q",lazy.shutdown()), # Logout         
    Key([alt], "Escape", lazy.spawn('xkill')), # Click window to close

    # Widgets
    Key([mod],"c",lazy.function(shortcuts)), # Shortcuts widget
    Key([mod, "shift"],"o",lazy.function(nightLight_widget)),
    Key([mod],"p",lazy.function(fargewidget)), # Color Picker Widget
    Key([alt], "Return", lazy.spawn('rofi  -theme "~/.config/rofi/left_bar.rasi" -show find -modi find:~/.local/bin/finder')), # Search for files and folders
    Key([mod],"f",lazy.spawn(home + '/.local/bin/wsearch')), # WEB Search widget
    Key([mod, "shift"],"f",lazy.spawn('rofi  -theme "~/.config/rofi/filesfolders.rasi" -show find -modi find:~/.local/bin/finder')), # Search files and folders
    Key([mod],"x",lazy.function(session_widget)), # Log out
    Key([mod],"b",lazy.function(network_widget)), # Network Settings
    Key([alt, "shift"],"w",lazy.function(change_color_scheme)), # Change Color Scheme
    Key([alt],"w",lazy.function(change_theme)), # Change Theme
    Key([mod, "shift"],"x",lazy.spawn(home + '/.local/bin/change_display')),# Monitor modes Widget
    Key([alt, "shift"], "r",lazy.function(random_colors)), # Set randwom wallpaper / colors to entire system

    # Layouts
    Key([mod], "Tab",lazy.layout.next()), # Change focus of windows down
    Key([mod, "shift"], "Tab",lazy.layout.up()), # Change focus of windows up
    Key([alt], "Tab", lazy.layout.swap_left()), # Swap Left Down
    Key([alt, "shift"], "Tab", lazy.layout.swap_right()), # Swap Right Up
    Key([mod], 'period', lazy.next_screen()), # Send Cursor to next screen

    # Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("xbacklight -inc 5")), # Aument Brightness
    Key([], "XF86MonBrightnessDown", lazy.spawn("xbacklight -dec 5")), # Lower Brightness

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
    Key([mod, "shift"], "l", lazy.layout.swap_right()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod], "i", lazy.layout.grow()),
    Key([mod], "m", lazy.layout.shrink()),
    Key([mod], "n", lazy.layout.normalize()),
    Key([mod], "o", lazy.layout.maximize()),
    Key([mod, "shift"], "space", lazy.layout.flip()),

    # Keyboard
    Key([alt], "space", lazy.widget["keyboardlayout"].next_keyboard()), # Change Keyboard Layout

    # Screenshots
    Key([], "Print", lazy.function(screenshot)),

    # Dunst Shortuts
    Key(["control"], "space",  lazy.spawn("dunstctl close")), # Clear Last Notification
    Key(["control", "shift"], "space",  lazy.spawn("dunstctl close-all")), # Clear All Notifications
    Key(["control", "shift"], "n",  lazy.spawn("dunstctl  history-pop")), # Show Notificaction history
]

## Groups

groups = []
group_names = ["Escape","1","2","3","4","5","6","7","8","9"]
group_labels=["零","一","二","三","四","五","六","七","八","九"] # Kanji Numbers
group_layouts=["monadtall", "monadtall", "monadtall", "matrix","monadtall", "monadtall", "monadtall","monadtall", "monadtall", "monadtall"]
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
    "change_ratio":0.05,
    "change_ratio":0.05,
    "new_client_position":'bottom',
    }

layout_theme = init_layout_theme()

def init_layouts():
  return [
    layout.MonadTall(max_ratio=0.90,ratio=0.75,**layout_theme),
    layout.MonadWide(max_ratio=0.90,ratio=0.75,**layout_theme),
    layout.MonadThreeCol(**layout_theme),
    layout.Stack(**layout_theme), 
    layout.Matrix(**layout_theme),
    ]
layouts = init_layouts()

widget_defaults = dict(
    font=main_font,
    fontsize=font_size,
    padding=3,
)
extension_defaults = widget_defaults.copy()

## Screens

screens = [
    Screen(
        bottom=bar.Bar(
            [
            widget.GroupBox(
              decorations=[RectDecoration(colour=color[0], radius=7, filled=True)],
              font=awesome_font,
              disable_drag=True,
              hide_unused=True,
              padding_x=3,
              borderwidth=0,
              active=color[3], #Program opened in that group
              inactive=color[6], # Empty Group
              rounded=False,
              highlight_method="text",
              this_current_screen_border=color[2],
              center_aligned = True,
              other_curren_screen_border=color[2],
              block_highlight_text_color=color[2],    
              urgent_border="fc0000",
            ),
            widget.Spacer(
              length=5,
              background=transparent,
            ),
            widget.CurrentLayout(
              decorations=[RectDecoration(colour=color[3], radius=7, filled=True)],
              foreground=color[0],
            ),
            widget.Spacer(
              length=5,
              background=transparent,
            ),
            widget.TextBox(
              decorations=[RectDecoration(colour=color[0], radius=[7,0,0,7], filled=True)],
              foreground=color[5],
              text="",
            ),
            widget.CPU(
              decorations=[RectDecoration(colour=color[5], radius=[0,7,7,0], filled=True)],
              foreground=color[0],
              format='{load_percent}%'
            ),
            widget.Spacer(
              length=5,
              background=transparent,
            ),
            widget.TextBox(
            decorations=[RectDecoration(colour=color[0], radius=[7,0,0,7], filled=True)],
            foreground=color[1],
            text="",
            ),
            widget.Memory(
              decorations=[RectDecoration(colour=color[1], radius=[0,7,7,0], filled=True)],
              foreground=color[0],
              format='{MemUsed:.0f}{mm}',
              measure_mem='M',
            ),
            widget.Spacer(
                length=5,
                background=transparent,
            ),
            widget.TextBox(
              decorations=[RectDecoration(colour=color[0], radius=[7,0,0,7], filled=True)],
              foreground=color[2],
              text="",
            ),
            widget.WindowName(
              decorations=[RectDecoration(colour=color[2], radius=[0,7,7,0], filled=True)],
              foreground=color[0],
              width=250,
              format='{name}',
              scroll=True,
              scroll_delay=2,
              scroll_repeat=True,
              scroll_step=1,
            ),
            widget.Spacer(
              length=5,
              background=transparent,
            ),
            widget.Prompt(
              decorations=[RectDecoration(colour=color[0], radius=7, filled=True)],
              prompt=prompt,
              foreground=color[4],
              cursor_color=color[4],
              visual_bell_color=[4],
              visual_bell_time=0.2,
            ),
            widget.Spacer(
              length=bar.STRETCH,
              background=transparent,
            ),
            widget.Pomodoro(
              decorations=[RectDecoration(colour=color[2], radius=[7,0,0,7], filled=True)],
              foreground=color[0],
              color_active=color[0],
              color_break='ffff00',
              color_inactive=color[0],
              length_long_break=30,
              length_pomodori=45,
              length_short_break=15,
              notification_on=True,
              num_pomodori=2,
              prefix_active=' ',
              prefix_inactive='',
              prefix_break=' Break!',
              prefix_long_break=' Long Break!',
              prefix_paused=' ',
              scroll=True,
              width=250,
            ),
            widget.TextBox(
              decorations=[RectDecoration(colour=color[0], radius=0, filled=True)],
              text="",
              foreground=color[6],
            ),
            ## Cmus
            widget.Mpris2(
              decorations=[RectDecoration(colour=color[6], radius=[0,7,7,0], filled=True)],
              mouse_callbacks={'Button1': lambda: qtile.spawn(terminal  + " -e cava")},
              objname='org.mpris.MediaPlayer2.cmus',
              foreground=color[0],
              width=250,
              format=['xesam:artist', 'xesam:title'],
              paused_text='Paused',
              stopped_text='',
              name='cmus',
              scroll=True,
              scroll_repeat=True,
            ),
            ## Vlc
            widget.Mpris2(
              decorations=[RectDecoration(colour=color[6], radius=[0,7,7,0], filled=True)],
              mouse_callbacks={'Button1': lambda: qtile.spawn(terminal  + " -e cava")},
              foreground=color[0],
              width=250,
              paused_text='Paused',
              stopped_text='',
              name='vlc',
              objname='org.mpris.MediaPlayer2.vlc',
              format=['xesam:artist', 'xesam:title'],
              scroll=True,
              scroll_repeat=True,
            ),
            ## Spotify
            widget.Mpris2(
              decorations=[RectDecoration(colour=color[6], radius=[0,7,7,0], filled=True)],
              mouse_callbacks={'Button1': lambda: qtile.spawn(terminal  + " -e cava")},
              foreground=color[0],
              width=250,
              paused_text='Paused',
              stopped_text='',
              name='spotify',
              objname='org.mpris.MediaPlayer2.spotify',
              format=['xesam:artist', 'xesam:title'],
              scroll=True,
              scroll_repeat=True,
            ),
            ## Ncspot
            widget.Mpris2(
              decorations=[RectDecoration(colour=color[6], radius=[0,7,7,0], filled=True)],
              mouse_callbacks={'Button1': lambda: qtile.spawn(terminal  + " -e cava")},
              foreground=color[0],
              width=250,
              paused_text='Paused',
              stopped_text='',
              name='ncspot',
              objname='org.mpris.MediaPlayer2.ncspot',
              format=['xesam:artist', 'xesam:title'],
              scroll=True,
              scroll_repeat=True,
            ),
            widget.Spacer(
              length=bar.STRETCH,
              background=transparent,
            ),
            widget.Systray(),
            widget.Spacer(
              length=5,
              background=transparent,
            ),
            widget.OpenWeather(
              decorations=[RectDecoration(colour=color[0], radius=[7,0,0,7], filled=True)],
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
                foreground=color[2],
                metric=True,
                update_interval=600,
                
            ),
            widget.OpenWeather(
              decorations=[RectDecoration(colour=color[2], radius=[0,7,7,0], filled=True)],
              app_key=w_appkey,
              cityid=w_cityid,
              foreground=color[0],
              format='{temp}°{units_temperature}',
              metric=True,
              update_interval=600,
              
            ),
            widget.Spacer(
              length=5,
              background=transparent,
            ),
            ## Network
            widget.WidgetBox(
              decorations=[RectDecoration(colour=color[0], radius=[7,0,0,7], filled=True)],
              text_closed=' ' + wifi_icon + ' ',
              text_open='  ',
              foreground=color[3],
              widgets=[
                  widget.TextBox(
                  decorations=[RectDecoration(colour=color[0], radius=0,filled=True)],
                  text='  ',
                  foreground=color[3],
                  mouse_callbacks={'Button1':lambda: qtile.cmd_function(network_widget)}
                ),
                widget.TextBox(
                  decorations=[RectDecoration(colour=color[3], radius=0, filled=True)],
                  text=private_ip,
                  foreground=color[0],
                  mouse_callbacks={'Button1':lambda: qtile.cmd_function(network_widget)}
                ),
                widget.TextBox(
                  decorations=[RectDecoration(colour=color[0], radius=0, filled=True)],
                  text='  ',
                  foreground=color[3],
                  mouse_callbacks={'Button1':lambda: qtile.cmd_function(network_widget)}
                ),
                widget.TextBox(
                  decorations=[RectDecoration(colour=color[2], radius=0, filled=True)],
                  text=public_ip,
                  foreground=color[0],
                  mouse_callbacks={'Button1':lambda: qtile.cmd_function(network_widget)}
                ),
                widget.TextBox(
                  decorations=[RectDecoration(colour=color[0], radius=0, filled=True)],
                  text=wifi_icon,
                  foreground=color[3],
                  mouse_callbacks={'Button1':lambda: qtile.cmd_function(network_widget)}
                ),
                # widget.Wlan(
                #  decorations=[RectDecoration(colour=color[0], radius=0, filled=True)],
                #  interface=wifi,
                #  format='{essid}',
                #  disconnected_message='',
                #  foreground=color[3],
                #  mouse_callbacks={'Button1':lambda: qtile.cmd_function(network_widget)}
                # ),
              ]
            ),
            # widget.Wlan(
            #       decorations=[RectDecoration(colour=color[0],radius=0, filled=True)],
            #       interface=wifi,
            #       format='{percent:2.0%}',
            #       disconnected_message='',
            #       foreground=color[3],
            #       mouse_callbacks={'Button1':lambda: qtile.cmd_function(network_widget)}
            #     ),
            widget.Net(
              interface=wifi,
              format='{down}',
              foreground=color[0],
              use_bits=True,
              mouse_callbacks={'Button1':lambda: qtile.cmd_function(network_widget)},
              decorations=[RectDecoration(colour=color[3], radius=[0,7,7,0], filled=True)],
            ),
            widget.Spacer(
              length=5,
              background=transparent,
            ),
            widget.TextBox(
              decorations=[RectDecoration(colour=color[0], radius=[7,0,0,7], filled=True)],
              text="",
              foreground=color[4],
            ),
            widget.KeyboardLayout(
              decorations=[RectDecoration(colour=color[4], radius=[0,7,7,0], filled=True)],
              configured_keyboards=['us intl', 'latam'],
              foreground=color[0],
            ),
            widget.Spacer(
              length=5,
              background=transparent,
            ),
            widget.TextBox(
              decorations=[RectDecoration(colour=color[0], radius=[7,0,0,7], filled=True)],
              text="",
              foreground=color[5],
              mouse_callbacks={'Button1': lambda: qtile.spawn('pavucontrol')}
            ),
            widget.ALSAWidget(
              decorations=[RectDecoration(colour=color[5], radius=[0,7,7,0], filled=True)],
              device='Master',
              bar_colour_high=color[0],
              bar_colour_loud=color[0],
              bar_colour_normal=color[0],
              bar_colour_mute=color[5],
              hide_interval=3,
              update_interval=0.1,
              bar_width=60,
              mode='bar',
              foreground=color[0],
              text_format='{volume}%',
            ),
            widget.Spacer(
              length=5,
              background=transparent,
            ),
            widget.Clock(
              foreground=color[0],
              format="%a",
              update_interval=1,
              decorations=[RectDecoration(colour=color[3], radius=[7,0,0,7], filled=True)],
            ),
            widget.Clock(
              foreground=color[3],
              format="%d",
              update_interval=1,
              decorations=[RectDecoration(colour=color[0], radius=0,filled=True)],
            ),
            widget.Clock(
              foreground=color[0],
              format="%H:%M",
              update_interval=1,
              decorations=[RectDecoration(colour=color[3], radius=[0,7,7,0], filled=True)],
            ),
            widget.Spacer(
              length=5,
              background=transparent,
            ),
            widget.UPowerWidget(
               border_charge_colour=color[7],
               border_colour=color[3],
               border_critical_colour='#cc0000',
               fill_critical='#cc0000',
               fill_low='#FF5511',
               fill_normal=color[3],
               foreground=color[3],
               decorations=[RectDecoration(colour=color[0], radius=[0,7,7,0], filled=True)],
               percentage_critical=0.1,
               percentage_low=0.3,
               text_charging=' ({percentage:.0f}%) {ttf} to ',
               text_discharging=' ({percentage:.0f}%) {tte} Left',
            ),
            ## Lock, Logout, Poweroff
            widget.TextBox(
              decorations=[RectDecoration(colour=color[6], radius=[0,7,7,0], filled=True)],
              foreground=color[0],
              text="",
              mouse_callbacks={'Button1': lambda: qtile.cmd_function(session_widget)}
            ),
              ],
              size=30,
              background=transparent,
              margin=[0,5,5,5],
          ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
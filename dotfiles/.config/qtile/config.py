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
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from qtile_extras import widget
from functions import *

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
def_Backend= "Haishoku"
transparent="00000000"

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

keys = [
    ##Basics
    Key([alt], "r",lazy.function(set_rand_wallpaper)), # Set randwom wallpaper / colors to entire system
    Key([mod], "Return", lazy.spawn(terminal)), # Open Terminal
    Key([mod], "r", lazy.spawncmd()), # Launch Prompt
    Key([mod], "q",lazy.window.kill()), # Close Window 
    Key([mod, "shift"], "r",lazy.reload_config()), # Restart Qtile
    Key([mod, "shift"], "q",lazy.shutdown()), # Logout         
    Key([alt], "Escape", lazy.spawn('xkill')), # Click window to close

    ## Layouts
    Key([mod], "Tab",lazy.layout.next()), # Change focus of windows down
    Key([mod, "shift"], "Tab",lazy.layout.up()), # Change focus of windows up
    Key([alt], "Tab", lazy.layout.swap_left()), # Swap Left Down
    Key([alt, "shift"], "Tab", lazy.layout.swap_right()), # Swap Right Up
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
    Key([alt], "g", lazy.window.toggle_fullscreen()), # Toggle Current window Full screen
    Key([alt, "shift"], "f", lazy.window.toggle_floating()), # Toggle current window floating
    Key([mod], "space", lazy.next_layout()), # Cycle layouts

    ## Resize windows
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

    ## Keyboard
    Key([alt], "space", lazy.widget["keyboardlayout"].next_keyboard()), # Change Keyboard Layout
]


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

screens = [
    Screen(
        bottom=bar.Bar(
            [
            widget.GroupBox(
              background=color[0],
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
              background=color[3],
              foreground=color[0],
            ),
            widget.Spacer(
              length=5,
              background=transparent,
            ),
            widget.TextBox(
              background=color[0],
              foreground=color[5],
              text="",
            ),
            widget.CPU(
              background=color[5],
              foreground=color[0],
              format='{load_percent}%'
            ),
            widget.Spacer(
              length=5,
              background=transparent,
            ),
            widget.TextBox(
            background=color[0],
            foreground=color[1],
            text="",
            ),
            widget.Memory(
              background=color[1],
              foreground=color[0],
              format='{MemUsed:.0f}{mm}',
              measure_mem='M',
            ),
            widget.Spacer(
                length=5,
                background=transparent,
            ),
            widget.TextBox(
              background=color[0],
              foreground=color[2],
              text="",
            ),
            widget.WindowName(
              background=color[2],
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
              prompt=prompt,
              foreground=color[9],
              cursor_color=color[9],
              visual_bell_color=[9],
              visual_bell_time=0.2,
              background=color[0],
            ),
            widget.Spacer(
              length=bar.STRETCH,
              background=transparent,
            ),
            widget.Pomodoro(
              background=color[2],
              foreground=color[0],
              color_active=color[7],
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
            widget.Spacer(
              length=5,
              background=transparent,
            ),
            widget.TextBox(
              background=color[0],
              text="",
              foreground=color[6],
            ),
            ## Cmus
            widget.Mpris2(
              background=color[6],
              mouse_callbacks={'Button1': lambda: qtile.spawn(term + " -e cava")},
              foreground=color[0],
              width=250,
              format=['xesam:artist', 'xesam:title'],
              paused_text='',
              stopped_text='',
              name='cmus',
              scroll=True,
              scroll_repeat=True,
            ),
            ## Vlc
            widget.Mpris2(
              background=color[6],
              mouse_callbacks={'Button1': lambda: qtile.spawn(term + " -e cava")},
              foreground=color[0],
              width=250,
              paused_text='',
              stopped_text='',
              name='vlc',
              objname='org.mpris.MediaPlayer2.vlc',
              format=['xesam:artist', 'xesam:title'],
              scroll=True,
              scroll_repeat=True,
            ),
            ## Spotify
            widget.Mpris2(
              background=color[6],
              mouse_callbacks={'Button1': lambda: qtile.spawn(term + " -e cava")},
              foreground=color[0],
              width=250,
              paused_text='',
              stopped_text='',
              name='spotify',
              objname='org.mpris.MediaPlayer2.spotify',
              format=['xesam:artist', 'xesam:title'],
              scroll=True,
              scroll_repeat=True,
            ),
            ## Ncspot
            widget.Mpris2(
              background=color[6],
              mouse_callbacks={'Button1': lambda: qtile.spawn(term + " -e cava")},
              foreground=color[0],
              width=250,
              paused_text='',
              stopped_text='',
              name='ncspot',
              objname='org.mpris.MediaPlayer2.ncspot',
              format=['xesam:artist', 'xesam:title'],
              scroll=True,
              scroll_repeat=True,
            ),
            # widget.Visualizer(
            #   hide=True,
            #   bar_colour=color[1],
            #   background=color[0],
            # ),
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
                foreground=color[2],
                metric=True,
                update_interval=600,
                
            ),
            widget.OpenWeather(
              app_key=w_appkey,
              cityid=w_cityid,
              foreground=color[0],
              format='{temp}°{units_temperature}',
              metric=True,
              update_interval=600,
              background=color[2],
            ),
            widget.Spacer(
              length=5,
              background=transparent,
            ),
            ## Network
            widget.WidgetBox(
              background=color[0],
              text_closed=' ' + wifi_icon + ' ',
              text_open=' ',
              foreground=color[3],
              widgets=[
                  widget.TextBox(
                  background=color[0],
                  text='  ',
                  foreground=color[3],
                  mouse_callbacks={'Button1':lambda: qtile.cmd_function(network_widget)}
                ),
                #widget.Wlan(
                #  background=color[0],
                #  interface=wifi,
                #  format='{essid}',
                #  disconnected_message='',
                #  foreground=color[3],
                #  mouse_callbacks={'Button1':lambda: qtile.cmd_function(network_widget)}
                #),
                widget.TextBox(
                  background=color[3],
                  text=private_ip,
                  foreground=color[0],
                  mouse_callbacks={'Button1':lambda: qtile.cmd_function(network_widget)}
                ),
                widget.TextBox(
                  background=color[0],
                  text='  ',
                  foreground=color[3],
                  mouse_callbacks={'Button1':lambda: qtile.cmd_function(network_widget)}
                ),
                widget.TextBox(
                  background=color[3],
                  text=public_ip,
                  foreground=color[0],
                  mouse_callbacks={'Button1':lambda: qtile.cmd_function(network_widget)}
                ),
                widget.TextBox(
                  background=color[0],
                  text=wifi_icon,
                  foreground=color[3],
                  mouse_callbacks={'Button1':lambda: qtile.cmd_function(network_widget)}
                ),
                #widget.Wlan(
                #  background=color[0],
                #  interface=wifi,
                #  format='{essid}',
                #  disconnected_message='',
                #  foreground=color[3],
                #  mouse_callbacks={'Button1':lambda: qtile.cmd_function(network_widget)}
                #),
              ]
            ),
            # widget.Wlan(
            #       background=color[0],
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
              background=color[3],
            ),
            widget.Spacer(
              length=5,
              background=transparent,
            ),
            widget.TextBox(
              background=color[0],
              
              text="",
              foreground=color[4],
            ),
            widget.KeyboardLayout(
              background=color[4],
              configured_keyboards=['us intl', 'latam'],
              foreground=color[0],
            ),
            widget.Spacer(
              length=5,
              background=transparent,
            ),
            widget.TextBox(
              background=color[0],
              text="",
              foreground=color[5],
              mouse_callbacks={'Button1': lambda: qtile.spawn('pavucontrol')}
            ),
            widget.ALSAWidget(
              background=color[5],
              device='Master',
              bar_colour_high=color[2],
              bar_colour_loud=color[2],
              bar_colour_normal=color[2],
              bar_colour_mute=color[1],
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
              background=color[3],
            ),
            widget.Clock(
              foreground=color[3],
              format="%d",
              update_interval=1,
              background=color[0],
            ),
            widget.Clock(
              foreground=color[0],
              format="%H:%M",
              update_interval=1,
              background=color[3],
            ),
            widget.Spacer(
              length=2,
              background=transparent,
            ),
            # widget.UPowerWidget(
            #   border_charge_colour=color[7],
            #   border_colour=color[3],
            #   border_critical_colour='#cc0000',
            #   fill_critical='#cc0000',
            #   fill_low='#FF5511',
            #   fill_normal=color[3],
            #   foreground=color[3],
            #   background=color[0],
            #   percentage_critical=0.1,
            #   percentage_low=0.3,
            #   text_charging=' ({percentage:.0f}%) {ttf} to ',
            #   text_discharging=' ({percentage:.0f}%) {tte} Left',
            # ),
            widget.Spacer(
              length=2,
              background=transparent,
            ),
            ## Lock, Logout, Poweroff
            widget.TextBox(
              background=color[6],
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
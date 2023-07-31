from keys import *
# _______  _______  ______  _______  __        
#|       ||   _   ||   __ \|     __||  |.-----.
#|   -  _||       ||      <|__     ||  ||  _  |
#|_______||___|___||___|__||_______||__||   __|
#                                       |__|   
# SpectrumOS - Embrace the Chromatic Symphony!
# By: gibranlp <thisdoesnotwork@gibranlp.dev>
# MIT licence
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
    Key([mod], "Tab",lazy.layout.down() ), # Change focus of windows down
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
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -q set Master 2%- && dunstify -a Volume ' '$(pamixer --get-volume-human) -h int:value:$(pamixer --get-volume)", shell=True)),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -q set Master 2%+ && dunstify -a Volume ' '$(pamixer --get-volume-human) -h int:value:$(pamixer --get-volume)", shell=True)), # Raise Volume

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

#group_labels=["","","","","","","","","",""] # SpectrumOS
#### Groups Labels
if int(variables[10]) == 0:
   group_labels=["","","","","","","","","",""] # SpectrumOS
elif int(variables[10]) == 1:
   group_labels=["零","一","二","三","四","五","六","七","八","九"] # Kanji Numbers
elif int(variables[10]) == 2:
   group_labels=["","","","","","","","","",""] # Custom
elif int(variables[10]) == 3:
   group_labels=["","","","","","","","","",""] # Star Wars
elif int(variables[10]) == 4:
   group_labels=["","","","","","","","","",""] # Chess
elif int(variables[10]) == 5:
   group_labels=["0","1","2","3","4","5","6","7","8","9"] # Numbers:
elif int(variables[10]) == 6:
   group_labels=[":","(",")","{",":","|",":","&","}",";"] # Fork Bomb
elif int(variables[10]) == 7:
   group_labels=["","","","","","","","","","",] # Circles
elif int(variables[10]) == 8:
   group_labels=["","","","","","","","","",""] # Squares
elif int(variables[10]) == 9:
   group_labels=["","","","","","","","","",""] # Triangles
elif int(variables[10]) == 10:
   group_labels=["","","","","","","","","",""] # Hexagons
elif int(variables[10]) == 11:
   group_labels=["","","","","","","","","",""] # Rectangles 
elif int(variables[10]) == 12:
   group_labels=["","","","","","","","","","",] # Square Ring 

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
    layout.MonadTall(max_ratio=max_ratio,ratio=ratio,**layout_theme),
    layout.MonadWide(max_ratio=0.85,ratio=0.85,**layout_theme),
    layout.Matrix(**layout_theme),
    ]
layouts = init_layouts()

floating_layout = layout.Floating(
   border_width=layout_border_width,
    border_normal=color[0],
    border_focus=color[2],
)

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = 'floating_only'
cursor_warp = True

auto_fullscreen = True
focus_on_window_activation = 'smart'
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = False

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written inhttps://docs.qtile.org/en/stable/manual/ref/layouts.html#floating
# java that happens to be on java's whitelist.
wmname = "LG3D"
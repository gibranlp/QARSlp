# By: gibranlp <thisdoesnotwork@gibranlp.dev>
# MIT licence
from theme import *
# Keys
def init_keys():
  keys = [ 
    ##Basics
    Key([alt], "r",lazy.function(set_rand_wallpaper)), # Set randwom wallpaper / colors to entire system
    Key([mod], "Return", lazy.spawn(term)), # Open Terminal
    Key([mod, "shift"], "Return", lazy.spawn('rofi -theme "~/.config/rofi/launcher.rasi" -show dmenu')), # Open Rofi launcher
    Key([mod, "mod1"], "Return", lazy.spawn('sudo rofi -theme "~/.config/rofi/launcher.rasi" -show drun')), # Open Rofi Launcher as Sud
    Key([mod], "r", lazy.spawncmd()), # Launch Prompt
    Key([mod], "q",lazy.window.kill()), # Close Window 
    Key([mod, "shift"], "r",lazy.reload_config()), # Restart Qtile
    Key([mod, "shift"], "q",lazy.shutdown()), # Logout         
    Key([alt], "Escape", lazy.spawn('xkill')), # Click window to close
            
    ## Widgets
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

    ## Theming
    Key([alt, "shift"], "r",lazy.function(random_colors)), # Set randwom wallpaper / colors to entire system

    ## Apps
    Key([mod, "shift"],"e",lazy.spawn('thunar')),
    Key(["control", "shift"],"Escape",lazy.spawn(term + ' -e htop')),
    
    #File manager
    Key([mod, "shift"],"s",lazy.function(app_or_group('7', term + ' -e cmus'))), #Open Cmus en the group 7
    Key([mod, "shift"],"m",lazy.spawn('thunderbird')), # Open Thunderbird
    Key([mod],"g",lazy.spawn('firefox')), # Open Firefox   
    Key([mod, "shift"],"g",lazy.spawn('google-chrome-stable')), # Open Google Chrome    
    Key([mod, "shift"],"c",lazy.spawn('code')), # Open Visual Code Studio
          
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
    Key([mod, "shift"], "h", lazy.layout.swap_left()),
    Key([mod, "shift"], "l", lazy.layout.swap_right()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod], "i", lazy.layout.grow()),
    Key([mod], "m", lazy.layout.shrink()),
    Key([mod], "n", lazy.layout.normalize()),
    Key([mod], "o", lazy.layout.maximize()),
    Key([mod, "shift"], "space", lazy.layout.flip()),
           
    ##  Dunst Shortuts
    Key(["control"], "space",  lazy.spawn("dunstctl close")), # Clear Last Notification
    Key(["control", "shift"], "space",  lazy.spawn("dunstctl close-all")), # Clear All Notifications
    Key(["control", "shift"], "n",  lazy.spawn("dunstctl  history-pop")), # Show Notificaction history
    
    ## Keyboard
    Key([alt], "space", lazy.widget["keyboardlayout"].next_keyboard()), # Change Keyboard Layout

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

wmname = "LG3D"


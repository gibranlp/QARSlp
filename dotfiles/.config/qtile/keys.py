from theme import *
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
    Key([mod], "b", lazy.spawn(home + '/.local/bin/bluet')), # Bluetooth widget
    Key([mod],"x",lazy.function(session_widget)), # Log out
    Key([mod],"f",lazy.function(network_widget)), # Network Settings
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

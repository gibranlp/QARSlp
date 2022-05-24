# _______  _______  ______  _______  __        
#|       ||   _   ||   __ \|     __||  |.-----.
#|   -  _||       ||      <|__     ||  ||  _  |
#|_______||___|___||___|__||_______||__||   __|
#                                       |__|   
# QARSlp Qtile + Arch Ricing Script
# By: gibranlp <thisdoesnotwork@gibranlp.dev>
# MIT licence 
#
from theme import *

#### Keys ####
def init_keys():
    keys = [ 
            #### Basics ####          
            Key([mod], "Return", lazy.spawn(term)), # Open Terminal
            Key([mod, "shift"], "Return", lazy.spawn('rofi -theme "~/.config/rofi/launcher.rasi" -show drun')),
            Key([mod, "mod1"], "Return", lazy.spawn('sudo rofi -theme "~/.config/rofi/launcher.rasi" -show drun')),
            Key([alt], "Return", lazy.spawn('rofi  -theme "~/.config/rofi/left_toolbar.rasi" -show find -modi find:~/.local/bin/finder')),
            Key([mod], "r", lazy.spawncmd()),
            Key([mod], "q",lazy.window.kill()), # Close Window 
            Key([mod, "shift"], "r",lazy.reload_config()), # Restart Qtile
            Key([mod, "shift"], "q",lazy.shutdown()), # Logout 
            Key([mod], "Escape", lazy.spawn('xkill')), # Click window to close
            
            #### Widgets ####
            Key([mod],"h",lazy.function(shortcuts)), # Shortcuts widget
            Key([mod],"f",lazy.spawn(home + '/.local/bin/wsearch')), # WEB Search
            Key([mod],"x",lazy.function(session_widget)), # Log out
            Key([mod],"n",lazy.function(network_widget)), # Network Settings
            Key([alt, "shift"],"r",lazy.function(change_color_scheme)), # Change Color Scheme
            Key([alt],"w",lazy.function(change_theme)), # Change Theme
            Key([mod, "shift"],"x",lazy.spawn(home + '/.local/bin/change_display')),

            #### Theming ####
            Key([alt], "r",lazy.function(set_rand_wallpaper)), # Set randwom wallpaper / colors to entire system

            #### Apps ####
            Key([mod, "shift"],"e",lazy.function(app_or_group("1", "thunar"))), #File manager
            Key([alt, "shift"],"e",lazy.function(ranger)), # CLI file manager
            Key([mod, "shift"],"a",lazy.function(app_or_group("1", "anydesk"))),
            Key([mod, "shift"],"s",lazy.function(app_or_group('2', 'simplenote'))),

            ## Group 2 (Organization: Mail)
            Key([mod, "shift"],"m",lazy.function(app_or_group('2', 'thunderbird'))),
            
            ## Group 3 (Social: Whatsapp, Telegram, )
            Key([mod, "shift"],"f",lazy.function(app_or_group('3', 't'))),

            ## Group 4 (WEB: Firefox)(Admin: Mail, notes, social)
            Key([mod, "shift"],"f",lazy.function(app_or_group('4', 'firefox'))),
            Key([mod, "shift"],"g",lazy.function(app_or_group('4', 'google-chrome-stable'))),
            
            ## Group 5 (Code/Write/Office: visual studio, typora, onlyofice)
            Key([mod, "shift"],"h",lazy.function(app_or_group('5', 'typora'))),
            Key([mod, "shift"],"o",lazy.function(app_or_group("6", 'libreoffice'))),
            Key([mod, "shift"],"c",lazy.function(app_or_group('5', 'code'))),

            ## Group 6 (Design: Gimp, Inkscape, feh)
            Key([mod],"g",lazy.function(app_or_group('6', 'gimp'))),

            ## Group 7 (Music: Ncsp, Spotify)
            Key([alt, "shift"],"s",lazy.function(ncsp)),

            ## Group 8 (Virtual Stuff games)
            
            #### Layouts ####
            Key([mod], "Tab",lazy.layout.next()), # Change focus of windows down
            Key([mod, "shift"], "Tab",lazy.layout.up()), # Change focus of windows up
            Key([alt], "Tab", lazy.layout.swap_left()),
            Key([alt, "shift"], "Tab", lazy.layout.swap_right()),
            Key([alt], "space", lazy.widget["keyboardlayout"].next_keyboard()),
            Key([mod], 'period', lazy.next_screen(),),

            #### Brightness ####
            Key([], "XF86MonBrightnessUp", lazy.spawn("xbacklight -inc 5")),
            Key([], "XF86MonBrightnessDown", lazy.spawn("xbacklight -dec 5")),

            #### Volume ####
            Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
            Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -q set Master 5%-")),
            Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -q set Master 5%+")),

            #### Media Control ####
            Key([], "XF86AudioPlay", lazy.function(play_pause)),
            Key([], "XF86AudioNext", lazy.function(nexts)),
            Key([], "XF86AudioPrev", lazy.function(prev)),
            Key([], "XF86AudioStop", lazy.function(stop)),

    
            #### Window hotkeys ####
            Key([alt], "f", lazy.window.toggle_fullscreen()),
            Key([alt, "shift"], "f", lazy.window.toggle_floating()),
            Key([mod], "space", lazy.next_layout()),

            #### Resize windows ####
            Key([mod, alt], "w", lazy.layout.grow()),
            Key([mod, alt], "s", lazy.layout.shrink()),
            Key([mod, "shift"], "space", lazy.layout.flip()),

            ##### Change focus ####
            Key([mod], "Up", lazy.layout.up()),
            Key([mod], "Down", lazy.layout.down()),
            Key([mod], "Left", lazy.layout.left()),
            Key([mod], "Right", lazy.layout.right()),

            ### Screenshots ####
            Key([], "Print", lazy.function(screenshot)),]


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


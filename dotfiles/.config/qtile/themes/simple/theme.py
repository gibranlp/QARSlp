# _______  _______  ______  _______  __        
#|       ||   _   ||   __ \|     __||  |.-----.
#|   -  _||       ||      <|__     ||  ||  _  |
#|_______||___|___||___|__||_______||__||   __|
#                                       |__|   
# QARSlp Qtile + Arch Ricing Script
# By: gibranlp <thisdoesnotwork@gibranlp.dev>
# MIT licence 
from funct import *

#### Widgets ####
def init_widgets_defaults():
    return dict(font="Fira Code Medium",fontsize=16,padding=2,background=color[0],foreground=color[1])

def init_widgets_top():
    widgets_top = [
                widget.TextBox(
                    foreground=color[1],
                    text="◢",
                    fontsize=65,
                    padding=-2
                    ),
                #### Groups ####
                widget.GroupBox(
                    font='Font Awesome 5 Free Solid',
                    fontsize=14,
                    disable_drag=True,
                    hide_unused=False,
                    padding_x=6,
                    padding_y=5,
                    borderwidth=0,
                    active=color[7],
                    inactive=color[0],
                    rounded=False,
                    highlight_color=color[0],
                    highlight_method="block",
                    this_current_screen_border=color[0],
                    this_screen_border=color[0],
                    other_current_screen_border=color[0],
                    other_screen_border=color[0],
                    block_highlight_text_color=color[1],
                    foreground=color[0],
                    background=color[1],
                    urgent_border=color[7]
                    ),
                widget.Prompt(
                       prompt=prompt,
                       padding=10,
                       ),
                widget.TextBox(
                    foreground=color[1],
                    text="◤",
                    fontsize=65,
                    padding=-2
                    ),
                widget.WindowName(
                    foreground=color[1],
                    padding=5,
                    format=' {name}',
                    empty_group_string=ver,
                    ),
                #### Spotify ####
                widget.TextBox(
                    font='Font Awesome 5 Free Solid',
                    fontsize=15,text="",
                    padding=5,
                    foreground=color[1],
                    mouse_callbacks={'Button1':lambda: qtile.cmd_spawn(term + ' -e vis')},
                    ),
                widget.Mpris2(
                    name='ncspot',
                    objname='org.mpris.MediaPlayer2.ncspot',
                    scroll_chars=30,
                    foreground=color[3],
                    stop_pause_text='',
                    display_metadata=['xesam:title', 'xesam:artist', 'xesam:album'],
                    ),
                widget.Mpris2(
                    name='Spotify',
                    objname='org.mpris.MediaPlayer2.spotify',
                    scroll_chars=30,
                    foreground=color[3],
                    stop_pause_text='',
                    display_metadata=['xesam:title', 'xesam:artist', 'xesam:album'],
                    ),
                widget.Mpris2(
                    name='vlc',
                    objname='org.mpris.MediaPlayer2.vlc',
                    scroll_chars=30,
                    foreground=color[3],
                    stop_pause_text='',
                    display_metadata=['xesam:title'],
                    scroll_interval=1,
                    scroll_wait_interval=200
                    ),
                widget.TextBox(
                    foreground=color[1],
                    text="",
                    mouse_callbacks={'Button1':lambda: qtile.cmd_function(prev)},
                    ),
                widget.TextBox(
                    foreground=color[4],
                    text="",
                    mouse_callbacks={'Button1':lambda: qtile.cmd_function(play_pause)},
                    ),
                widget.TextBox(
                    foreground=color[1],
                    text="",
                    mouse_callbacks={'Button1':lambda: qtile.cmd_function(nexts)},
                    ),           
                #### Layouts ####
                widget.TextBox(
                    text="◢",
                    background=color[0],
                    foreground=color[3],
                    padding=-2,
                    fontsize=65
                    ),
                #### Pomodoro ####
                widget.WidgetBox(
                    text_closed='  |',
                    text_open='  |',
                    background=color[3],
                    foreground=color[0],
                    widgets=[widget.Pomodoro(
                        background=color[3],
                        foreground=color[0],
                        color_active=color[0],
                        color_break=color[7],
                        color_inactive=color[0],
                        length_pomodori=50,
                        length_short_break=5,
                        length_long_break=15,
                        num_pomodori=3,
                        prefix_break=' Break |',
                        prefix_inactive=' Pomodoro |',
                        prefix_long_break=' Long Break|',
                        prefix_paused='  |'
                    )],
                ),
                widget.CurrentLayout(
                    background=color[3],
                    foreground=color[0]
                    ),
                widget.TextBox(
                    text="| ",
                    background=color[3],
                    foreground=color[0]
                    ),
                #### Updates ####
                widget.TextBox(
                    font='Font Awesome 5 Free Solid',
                    fontsize=15,
                    background=color[3],
                    foreground=color[0],
                    text="",
                    ),
                widget.CheckUpdates(
                    update_interval=1800,
                    distro='Arch_paru',
                    foreground=color[0],
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(term + ' -e sudo paru -Syu')},
                    display_format="{updates} up",
                    background=color[3],
                    colour_have_updates=color[0],
                    colour_no_updates=color[0],
                    no_update_string=" ",
                    restart_indicator=""
                    ),
                widget.TextBox(
                    text="|",
                    background=color[3],
                    foreground=color[0]
                    ),
                widget.TextBox(
                    font='Font Awesome 5 Free Solid',
                    text=" ",
                    background=color[3],
                    foreground=color[0],
                    padding=0,
                    fontsize=15,
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('pavucontrol')}
                    ),
                widget.ALSAWidget(
                    device='Master',
                    bar_colour_high='#FFA500',
                    bar_colour_loud='#cc0000',
                    bar_colour_normal=color[3],
                    bar_colour_mute=color[0],
                    hide_interval=3,
                    update_interval=0.1,
                    bar_width=75,
                    mode='bar',
                ),
                widget.TextBox(
                    text="| ",
                    background=color[3],
                    foreground=color[0]
                    ),
                widget.UPowerWidget(
                    background=color[3],
                    border_charge_colour=color[7],
                    border_colour=color[0],
                    border_critical_colour='cc0000',
                    fill_critical='cc0000',
                    fill_low='aa00aa',
                    fill_normal=color[0],
                    font_colour=color[0],
                ),
                #### Date Clock Session Control ####
                widget.TextBox(
                    text='◢',
                    background=color[3],
                    foreground=color[0],
                    padding=-2,
                    fontsize=65
                    ),
                widget.Clock(
                    foreground=color[1],
                    format="%b %a %d %H:%M",
                    update_interval=1
                    ),
                #### Lock, Logout, Poweroff ####
                widget.TextBox(
                    font='Font Awesome 5 Free Solid',
                    fontsize=15,
                    foreground=color[3],
                    text="",
                    mouse_callbacks={'Button1': lambda: qtile.cmd_function(session_widget)}
                    ),
                widget.Sep(
                    foreground=color[0],
                ),
    ]
    return widgets_top

def init_widgets_bott():
    
    widgets_bott = [
                #### Shortcuts ####
                widget.TextBox(
                    font='Font Awesome 5 Free Solid',
                    fontsize=16,
                    text="",
                    padding=5,
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('rofi -theme "~/.config/rofi/launcher.rasi" -show drun')},
                    background=color[3],
                    foreground=color[0]
                    ),
                widget.TextBox(
                    font='Font Awesome 5 Free Solid',
                    fontsize=15,
                    foreground=color[1],
                    text="",
                    mouse_callbacks={'Button1':lambda: qtile.cmd_spawn('rofi  -theme "~/.config/rofi/left_toolbar.rasi" -show find -modi find:/usr/local/bin/finder')}
                    ),        
                widget.TextBox(
                    font='Font Awesome 5 Free Solid',
                    fontsize=15,
                    foreground=color[2],
                    text="",
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(term)}
                    ),
                widget.TextBox(
                    font='Font Awesome 5 Free Solid',
                    fontsize=15,
                    foreground=color[3],
                    text="",
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("thunar")}
                    ),
                widget.TextBox(
                    font='Font Awesome 5 Free Solid',
                    fontsize=15,
                    foreground=color[4],
                    text="",
                    mouse_callbacks={'Button1':lambda: qtile.cmd_function(set_rand_wallpaper)},
                ),
                widget.TextBox(
                    font='Font Awesome 5 Free Solid',
                    fontsize=15,
                    foreground=color[5],
                    text="",
                    mouse_callbacks={'Button1':lambda: qtile.cmd_function(change_color_scheme)},
                ),
                widget.TextBox(
                    font='Font Awesome 5 Free Solid',
                    fontsize=15,
                    foreground=color[6],
                    text="",
                    mouse_callbacks={'Button1': lambda: qtile.cmd_function(shortcuts)}
                    ),
                #### Spacer ####
                widget.Spacer(
                    length=bar.STRETCH,
                    ),   
                #### Network ####
                widget.WidgetBox(
                    text_closed=wifi_icon,
                    text_open='',
                    foreground=color[4],
                    widgets=[widget.TextBox(
                        text='  '+private_ip,
                        foreground=color[3],
                        mouse_callbacks={'Button1':lambda: qtile.cmd_function(network_widget)}
                        ),
                        widget.TextBox(
                        text='  '+public_ip,
                         
                        foreground=color[3],
                        mouse_callbacks={'Button1':lambda: qtile.cmd_function(network_widget)}
                        ),]
                ),
                widget.Wlan(
                    interface=wifi,
                    format=' {essid} {percent:2.0%} ',
                    disconnected_message='Unplugged',
                    foreground=color[4],
                     
                    mouse_callbacks={'Button1':lambda: qtile.cmd_function(network_widget)}
                    ),
                widget.Net(
                    interface=wifi,
                    format=' {down}',
                    foreground=color[4],
                     
                    use_bits=True,
                    mouse_callbacks={'Button1':lambda: qtile.cmd_function(network_widget)}
                    ),
                widget.TextBox(
                    text="◢",
                    background=color[0],
                    foreground=color[1],
                    padding=-2,
                    fontsize=65
                    ),
                #### Weather ####
                widget.TextBox(
                    text='  ',
                    background=color[1],
                    foreground=color[0],
                ),
                widget.OpenWeather(
                    app_key=w_appkey,
                    cityid=w_cityid,
                    background=color[1],
                    foreground=color[0],
                    format='{main_temp}°{units_temperature} {humidity}% {weather_details}',
                    metric=True,                        update_interval=600
                    ),
                widget.TextBox(
                    text="| ",
                    background=color[1],
                    foreground=color[0]
                    ),
                #### RAM ####
                widget.TextBox(
                    font='Font Awesome 5 Free Solid',
                    fontsize=15,
                    background=color[1],
                    foreground=color[0],
                    text=""
                    ),
                widget.Memory(
                    format='{MemUsed:.0f}{mm}/{MemTotal:.0f}{mm}',
                    foreground=color[0],
                    background=color[1],
                    padding=5
                    ),
                widget.TextBox(
                    text="| ",
                    background=color[1],
                    foreground=color[0]
                    ),
                #### CPU ####
                widget.TextBox(
                    font='Font Awesome 5 Free Solid',
                    fontsize=15,
                    background=color[1],
                    foreground=color[0],
                    text=""
                    ),
                widget.CPU(
                    format='{load_percent}%',
                    foreground=color[0],
                    background=color[1],
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(term + ' -e htop')},
                    ),
                widget.TextBox(
                    text="| ",
                    background=color[1],
                    foreground=color[0]
                    ),
                #### Disk Space ####
                widget.TextBox(
                    font='Font Awesome 5 Free Solid',
                    fontsize=15,
                    background=color[1],
                    foreground=color[0],
                    text=""
                    ),
                widget.DF(
                    format='{p} ({uf}{m}|{r:.0f}%)',
                    measure='G',
                    Partition='/',
                    update_interval=60,
                    foreground=color[0],
                    background=color[1],
                    padding=5,
                    visible_on_warn=False,
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(term + ' -e ranger')},
                    warn_color="ff0000"
                    ),
                widget.TextBox(
                    text="| ",
                    background=color[1],
                    foreground=color[0]
                    ),
                #### Thermal Sensors ####
                widget.TextBox(
                    font='Font Awesome 5 Free Solid',
                    fontsize=15,
                    text="",
                    background=color[1],
                    foreground=color[0]
                    ),
                widget.ThermalSensor(
                    background = color[1],
                    foreground=color[0],
                    tag_sensor='Core 0',
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('/usr/local/bin/fans')},
                    ),
                widget.TextBox(
                    text="| ",
                    background=color[1],
                    foreground=color[0]
                    ),
                #### Keyboard Layout ####
                widget.TextBox(
                    font='Font Awesome 5 Free Solid',
                    fontsize=17,
                    text="",
                    foreground=color[0],
                    background=color[1],
                    ),
                widget.KeyboardLayout(
                    configured_keyboards=['us intl', 'latam'],
                    foreground=color[0],
                    background=color[1],
                    padding=5
                    ),
                widget.TextBox(
                    text="| ",
                    background=color[1],
                    foreground=color[0]
                    ),
                #### Caps lock Num Lock Indicator ####
                widget.CapsNumLockIndicator(
                    foreground=color[0],
                    background=color[1],
                    padding=5
                    ),
                #### System Tray ####
                widget.TextBox(
                    text="◢",
                    background=color[1],
                    foreground=color[0],
                    padding=-2,
                    fontsize=65
                    ),
                #### Systray ####
                widget.Systray(
                    icon_size=18,
                    ),
                    ]
    return widgets_bott

#### End Widgets ####

##### Screens #####

def init_widgets_screen_top():
    widgets_screen_top = init_widgets_top()
    return widgets_screen_top
def init_widgets_screen_bot():
    widgets_screen_bot = init_widgets_bott()  
    return widgets_screen_bot

def init_screens():
    return [
        Screen(
            top=bar.Bar(
                widgets=init_widgets_screen_top(),  
                size=25,
                ),
            bottom=bar.Bar(
                widgets=init_widgets_screen_bot(),
                size=25,
                )
        ),
        Screen(
            top=bar.Bar(
                widgets=init_widgets_screen_top(),  
                size=25,
                ),
            bottom=bar.Bar(
                widgets=init_widgets_screen_bot(),
                size=25,
                )
        )
        ]

#### End Screens ####

widget_defaults = init_widgets_defaults()
widgets_top = init_widgets_top()
widgets_screen_top = init_widgets_screen_top()
screens = init_screens()
widgets_bott = init_widgets_bott()
widgets_screen_top = init_widgets_screen_top()
init_widgets_screen_bot = init_widgets_screen_bot()

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
    return dict(font="Fira Code Medium",fontsize=15,padding=2,background=color[0])

def init_widgets_top():    
    widgets_top = [
                #### Shortcuts ####
                widget.TextBox(
                    font='Font Awesome 5 Free Solid',
                    fontsize=16,
                    text="",
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('rofi -theme "~/.config/rofi/launcher.rasi" -show drun')},
                    background=color[6],
                    foreground=color[0],
                    padding=5
                    ),
                widget.TextBox(
                    font='Font Awesome 5 Free Solid',
                    fontsize=15,
                    foreground=color[4],
                    text="",
                    mouse_callbacks={'Button1': lambda: qtile.cmd_function(shortcuts)}
                    ),
                widget.Sep(
                    width=10
                ),
                #### Groups ####
                widget.GroupBox(
                    font='Font Awesome 5 Free Solid',
                    fontsize=15,
                    disable_drag=True,
                    center_aligned=True,
                    padding=5,
                    active=color[4],
                    inactive=color[2],
                    rounded=False,
                    this_current_screen_border=color[2],
                    this_screen_border=color[2],
                    other_current_screen_border=color[2],
                    other_screen_border=color[2],
                    block_highlight_text_color= color[0],
                    highlight_method="block",
                    foreground=color[7],
                    background=color[0]
                    ),
                widget.Sep(
                    width=10
                ),
                widget.Prompt(
                       prompt=prompt,
                       padding=10,
                       foreground=color[0],
                       background=color[2]
                       ),
                widget.Sep(
                    width=10
                ),
                widget.WindowName(
                    foreground=color[4],
                    background=color[0],
                    padding=5,
                    format=' {name}',
                    empty_group_string=ver,
                    ),
                widget.Systray(
                    icon_size=18,
                    background=color[0],
                    foreground=color[7]
                    ),
                widget.Sep(
                    width=10
                ),
                widget.Mpris2(
                    name='ncspot',
                    objname='org.mpris.MediaPlayer2.ncspot',
                    scroll_chars=30,
                    background=color[0],
                    foreground=color[6],
                    stop_pause_text='',
                    max_chars=50,
                    display_metadata=['xesam:title', 'xesam:artist', 'xesam:album'],
                    scroll_interval=0.5,
                    scroll_wait_intervals=8
                    ),
                widget.Mpris2(
                    name='Spotify',
                    objname='org.mpris.MediaPlayer2.spotify',
                    scroll_chars=30,
                    background=color[6],
                    foreground=color[0],
                    stop_pause_text='',
                    max_chars=50,
                    display_metadata=['xesam:title', 'xesam:artist', 'xesam:album'],
                    scroll_interval=0.5,
                    scroll_wait_intervals=8,
                    ),
                widget.Sep(
                    width=10
                    ),
                #widget.Wlan(
                #    interface=wifi,
                #    format='{essid} {percent:2.0%} ',
                #    disconnected_message='Unplugged',
                #    foreground=color[6],
                #    background=color[0],
                #    mouse_callbacks={'Button1':lambda: qtile.cmd_function(network_widget)}
                #    ),
                widget.Net(
                    interface=wifi,
                    format='{down}',
                    foreground=color[6],
                    background=color[0],
                    use_bits=True,
                    mouse_callbacks={'Button1':lambda: qtile.cmd_function(network_widget)}
                    ),
                widget.Sep(
                    width=10
                    ),
                widget.WidgetBox(
                    text_closed='',
                    text_open='',
                    background=color[6],
                    foreground=color[0],
                    widgets=[widget.OpenWeather(
                        app_key=w_appkey,
                        cityid=w_cityid,
                        background=color[6],
                        foreground=color[0],
                        format=' {main_temp}°{units_temperature} {weather_details}',
                        metric=True,
                        update_interval=600
                        ),
                    widget.Sep(
                    width=10
                    ),
                ]),
                widget.Sep(
                    width=10
                    ),
                 widget.DF(
                    format='{uf}{m}',
                    measure='G',
                    Partition='/',
                    update_interval=1800,
                    foreground=color[6],
                    background=color[0],
                    padding=5,
                    visible_on_warn=False,
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(term + ' -e ranger')},
                    warn_color="ff0000"
                    ),
                widget.Sep(
                    width=10
                    ),
                widget.CheckUpdates(
                    update_interval=300,
                    distro='Arch_paru',
                    foreground=color[0],
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(term + ' -e paru -Syyu')},
                    display_format="up",
                    background=color[0],
                    colour_have_updates=color[6],
                    colour_no_updates=color[6],
                    no_update_string="",
                    restart_indicator=""
                    ),
                widget.Sep(
                    width=10
                    ),
                widget.ALSAWidget(
                    background=color[0],
                    device='Master',
                    bar_colour_high=color[6],
                    bar_colour_loud=color[6],
                    bar_colour_normal=color[6],
                    bar_colour_mute=color[6],
                    hide_interval=3,
                    update_interval=0.1,
                    text_format=' {volume}%',
                ),
                widget.Sep(
                    width=10
                    ),
                widget.Clock(
                    foreground=color[0],
                    background=color[6],
                    format="%b %a %d %H:%M",
                    update_interval=1,
                    padding=5,
                    padding_y=15
                    ),
                widget.Sep(
                    width=10
                    ),
                #### Lock, Logout, Poweroff ####
                widget.TextBox(
                    font='Font Awesome 5 Free Solid',
                    fontsize=15,
                    foreground=color[6],
                    text="",
                    mouse_callbacks={'Button1': lambda: qtile.cmd_function(session_widget)},
                    fontshadow=color[3]
                    ),
                widget.Sep(
                    foreground=color[0],
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
            top=bar.Bar(
                widgets=init_widgets_screen_top(),  
                size=25,
                margin=10,
                border_color=color[1],
                border_width=[2,2,2,2],
                background=color[0],
                )),
        Screen(
            top=bar.Bar(
                widgets=init_widgets_screen_top(),  
                size=25,
                margin=10,
                border_color=color[1],
                border_width=[2,2,2,2],
                background=color[0],
                ))
        ]

#### End Screens ####

widget_defaults = init_widgets_defaults()
widgets_top = init_widgets_top()
widgets_screen_top = init_widgets_screen_top()
screens = init_screens()

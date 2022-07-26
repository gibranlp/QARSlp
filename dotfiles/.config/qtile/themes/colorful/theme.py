# _______  _______  ______  _______  __        
#|       ||   _   ||   __ \|     __||  |.-----.
#|   -  _||       ||      <|__     ||  ||  _  |
#|_______||___|___||___|__||_______||__||   __|
#                                       |__|   
# QARSlp Qtile + Arch Ricing Script
# By: gibranlp <thisdoesnotwork@gibranlp.dev>
# MIT licence 
from numpy import size
from pyparsing import cpp_style_comment
from funct import *

#### Widgets ####
def init_widgets_defaults():
    return dict(font=main_font,fontsize=fontsz)

def init_widgets_top():
    widgets_top = [
                widget.TextBox(
                    background=color[1],
                    font=awesome_font,
                    text="",
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('rofi -theme "~/.config/rofi/launcher.rasi" -show drun')},
                    foreground=color[0],
                    fontsize=fontsz
                    ),
                widget.TextBox(
                    background=color[0],
                    foreground=color[1],
                    text="",
                    padding=0,
                    fontsize=30,
                ),
                #### Groups ####
                widget.GroupBox(
                    background=color[0],
                    font=awesome_font,
                    disable_drag=True,
                    hide_unused=False,
                    padding_x=3,
                    borderwidth=0,
                    active=color[3], #Program opened in that group
                    inactive=color[8], # Empty Group
                    rounded=False,
                    highlight_method="text",
                    this_current_screen_border=color[5],
                    center_aligned = True,
                    other_current_screen_border=color[1],
                    block_highlight_text_color=color[2],    
                    urgent_border=color[5]
                    ),
                widget.TextBox(
                    background=color[2],
                    foreground=color[0],
                    text="",
                    padding=0,
                    fontsize=30,
                ),
                widget.Prompt(
                    background=color[2],
                       prompt=prompt,
                       foreground=color[0],
                       cursor_color=color[0],
                       visual_bell_color=[0],
                       visual_bell_time=0.2,
                       ),
                widget.TextBox(
                    background=color[5],
                    foreground=color[2],
                    text="",
                    padding=0,
                    fontsize=30,
                ),
                widget.CurrentLayout(
                    background=color[5],
                    foreground=color[0],
                    ),
                widget.TextBox(
                    background=color[3],
                    foreground=color[5],
                    text="",
                    padding=0,
                    fontsize=30,
                ),
                #### Weather ####
                widget.OpenWeather(
                    font=awesome_font,
                    background=color[3],
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
                    foreground=color[0],
                    metric=True,
                    update_interval=600
                    ),
               widget.OpenWeather(
                    background=color[3],
                    app_key=w_appkey,
                    cityid=w_cityid,
                    foreground=color[0],
                    format='{temp}°{units_temperature} {humidity}%',
                    metric=True,
                    update_interval=600
                    ),
                widget.TextBox(
                    background=color[0],
                    foreground=color[3],
                    text="",
                    padding=0,
                    fontsize=30,
                ),
                widget.WindowName(
                    background=color[0],
                    foreground=color[1],
                    empty_group_string=ver,
                    format='  {name}',
                ),
                widget.Spacer(
                    length=bar.STRETCH,
                    background=color[0]
                    ),
                widget.TextBox(
                    background=color[6],
                    foreground=color[0],
                    text="",
                    padding=0,
                    fontsize=30,
                ),
                widget.Clock(
                    background=color[6],
                    foreground=color[0],
                    format="%a %d %H:%M",
                    update_interval=1
                    ),
                widget.TextBox(
                    background=color[6],
                    foreground=color[0],
                    text="",
                    padding=0,
                    fontsize=30,
                ),
                widget.Spacer(
                    length=bar.STRETCH,
                    background=color[0]
                    ),
                widget.Systray(
                    icon_size=iconsz,
                    background=color[0],
                    ),
                #### Spotify ####
                 widget.TextBox(
                    background=color[0],
                    foreground=color[2],
                    text=" ",
                    mouse_callbacks={'Button1':lambda: qtile.cmd_function(prev)},
                    ),
                widget.Mpris2(
                    background=color[0],
                    foreground=color[2],
                    name='cmus',
                    objname='org.mpris.MediaPlayer2.cmus',
                    scroll_chars=scrollchar,
                    stop_pause_text='',
                    display_metadata=['xesam:title', 'xesam:artist'],
                    scroll_interval=scrollint,
                    scroll_wait_intervals=scrollwint,
                    ),
                widget.Mpris2(
                    background=color[0],
                    foreground=color[2],
                    name='ncspot',
                    objname='org.mpris.MediaPlayer2.ncspot',
                    scroll_chars=scrollchar,
                    stop_pause_text='',
                    display_metadata=['xesam:title', 'xesam:artist'],
                    scroll_interval=scrollint,
                    scroll_wait_intervals=scrollwint,
                    ),
                widget.Mpris2(
                    background=color[0],
                    foreground=color[2],
                    name='Spotify',
                    objname='org.mpris.MediaPlayer2.spotify',
                    scroll_chars=scrollchar,
                    stop_pause_text='',
                    display_metadata=['xesam:title', 'xesam:artist'],
                    scroll_interval=scrollint,
                    scroll_wait_intervals=scrollwint,
                    ),
                widget.Mpris2(
                    background=color[0],
                    foreground=color[2],
                    name='vlc',
                    objname='org.mpris.MediaPlayer2.vlc',
                    scroll_chars=scrollchar,
                    stop_pause_text='',
                    display_metadata=['xesam:title', 'xesam:artist'],
                    scroll_interval=scrollint,
                    scroll_wait_intervals=scrollwint,
                    ),
                widget.TextBox(
                    background=color[0],
                    foreground=color[2],
                    text=" ",
                    mouse_callbacks={'Button1':lambda: qtile.cmd_function(nexts)},
                    ),
                widget.TextBox(
                    background=color[0],
                    foreground=color[3],
                    text="",
                    padding=0,
                    fontsize=30,
                ),
                #### Network ####
                widget.WidgetBox(
                    background=color[3],
                    text_closed="" + wifi_icon,
                    text_open=' ',
                    foreground=color[0],
                    widgets=[widget.TextBox(
                        background=color[3],
                        text='  '+private_ip,
                        foreground=color[0],
                        mouse_callbacks={'Button1':lambda: qtile.cmd_function(network_widget)}
                        ),
                        widget.TextBox(
                        background=color[3],
                        text='  '+public_ip + " " + wifi_icon,
                        foreground=color[0],
                        mouse_callbacks={'Button1':lambda: qtile.cmd_function(network_widget)}
                        ),]
                ),
                #widget.Wlan(
                #   background=color[3],
                #    interface=wifi,
                #    format=' {essid} {percent:2.0%} ',
                #    disconnected_message='Unplugged',
                #    foreground=color[0],
                #    mouse_callbacks={'Button1':lambda: qtile.cmd_function(network_widget)}
                #    ),
                widget.Net(
                    background=color[3],
                    interface=wifi,
                    format='{down}',
                    foreground=color[0],
                    use_bits=True,
                    mouse_callbacks={'Button1':lambda: qtile.cmd_function(network_widget)}
                    ),
                widget.TextBox(
                    background=color[3],
                    foreground=color[5],
                    text="",
                    padding=0,
                    fontsize=30,
                ),
                widget.TextBox(
                    background=color[5],
                    font=awesome_font,
                    text="",
                    foreground=color[0],
                    ),
                widget.KeyboardLayout(
                    background=color[5],
                    configured_keyboards=['us intl', 'latam'],
                    foreground=color[0],
                    ),
                widget.TextBox(
                    background=color[5],
                    foreground=color[2],
                    text="",
                    padding=0,
                    fontsize=30,
                ),
                widget.TextBox(
                    background=color[2],
                    font=awesome_font,
                    text=" ",
                    foreground=color[0],
                    padding=0,
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('pavucontrol')}
                    ),
                widget.ALSAWidget(
                    bckground=color[2],
                    device='Master',
                    bar_colour_high=color[2],
                    bar_colour_loud=color[2],
                    bar_colour_normal=color[2],
                    bar_colour_mute=color[2],
                    hide_interval=3,
                    update_interval=0.1,
                    bar_width=20,
                    mode='bar',
                    foreground=color[0],
                ),
                widget.TextBox(
                    background=color[2],
                    foreground=color[0],
                    text="",
                    padding=0,
                    fontsize=30,
                ),
                widget.TextBox(
                    background=color[0],
                    foreground=color[1],
                    text="",
                ),
                widget.Bluetooth(
                    background=color[0],
                    foreground=color[1],
                    hci='/dev_28_EC_9A_9B_64_72',
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('blueman-manager')}
                ),
                widget.TextBox(
                    background=color[0],
                    foreground=color[1],
                    text="",
                    padding=0,
                    fontsize=30,
                ),
                #### Lock, Logout, Poweroff ####
                widget.TextBox(
                    background=color[1],
                    font=awesome_font,
                    foreground=color[0],
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
            top=bar.Bar(
                background=color[7],
                widgets=init_widgets_screen_top(),  
                size=barsz,
                border_width=barBorderWidth,
                margin=[10,10,0,10]
                )),
        Screen(
            top=bar.Bar(
                background=color[7],
                widgets=init_widgets_screen_top(),  
                size=barsz,
                border_width=barBorderWidth,
                margin=[10,10,0,10]
                )
        )
        ]

#### End Screens ####

widget_defaults = init_widgets_defaults()
widgets_top = init_widgets_top()
widgets_screen_top = init_widgets_screen_top()
screens = init_screens()
# _______  _______  ______  _______  __        
#|       ||   _   ||   __ \|     __||  |.-----.
#|   -  _||       ||      <|__     ||  ||  _  |
#|_______||___|___||___|__||_______||__||   __|
#                                       |__|   
# QARSlp Qtile + Arch Ricing Script
# By: gibranlp <thisdoesnotwork@gibranlp.dev>
# MIT licence 
from numpy import size
from funct import *

#### Widgets ####
def init_widgets_defaults():
    return dict(font=main_font,fontsize=fontsz,padding=2)

def init_widgets_top():
    widgets_top = [
                #### Groups ####
                widget.GroupBox(
                    font=awesome_font,
                    disable_drag=True,
                    hide_unused=False,
                    padding_x=6,
                    padding_y=5,
                    borderwidth=0,
                    active=color[3],
                    fontshadow=color[0],
                    inactive=color[0],
                    rounded=False,        
                    highlight_color=color[3],
                    highlight_method="text",
                    this_current_screen_border=color[7],
                    this_screen_border=color[3],
                    other_current_screen_border=color[4],
                    other_screen_border=color[5],
                    block_highlight_text_color=color[2],
                    foreground=color[1],
                    urgent_border=color[4]
                    ),
                widget.Prompt(
                       prompt=prompt,
                       padding=10,
                       foreground=color[3],
                       ),
                 widget.Notify(
                    fmt=' ℹ ',
                    foreground=color[1],
                    fontshadow=color[0],
                    default_timeout=15,
                    max_chars=5,
                    action=False,
                    foreground_low=color[1],
                ),
                widget.Notify(
                    foreground=color[3],
                    fontshadow=color[0],
                    default_timeout=15,
                    max_chars=200,
                    action=False,
                    foreground_low=color[4],
                ),
                widget.Spacer(
                    length=bar.STRETCH,
                    foreground=color[0]
                    ),
                widget.Sep(
                    foreground=color[1],
                    linewidth=5,
                ),
                 widget.Sep(
                    foreground=color[2],
                    linewidth=5,
                ),
                 widget.Sep(
                    foreground=color[3],
                    linewidth=5,
                ),
                widget.Sep(
                    foreground=color[4],
                    linewidth=5,
                ),
                 widget.Sep(
                    foreground=color[5],
                    linewidth=5,
                ),
                 widget.Sep(
                    foreground=color[6],
                    linewidth=5,
                ),
                 widget.Sep(
                    foreground=color[7],
                    linewidth=5,
                ),
                 widget.Sep(
                    foreground=color[8],
                    linewidth=5,
                ),
                #### Spotify ####
                widget.TextBox(
                    font=awesome_font,
                    text="  ",
                    padding=5,
                    foreground=color[4],
                    fontshadow=color[1],
                    mouse_callbacks={'Button1':lambda: qtile.cmd_spawn(term + ' -e vis')},
                    ),
                widget.Mpris2(
                    name='ncspot',
                    objname='org.mpris.MediaPlayer2.ncspot',
                    scroll_chars=scrollchar,
                    foreground=color[3],
                    fontshadow=color[0],
                    stop_pause_text='  ',
                    display_metadata=['xesam:title', 'xesam:artist'],
                    scroll_interval=scrollint,
                    scroll_wait_intervals=scrollwint,
                    ),
                widget.Mpris2(
                    name='Spotify',
                    objname='org.mpris.MediaPlayer2.spotify',
                    scroll_chars=scrollchar,
                    foreground=color[3],
                    fontshadow=color[0],
                    stop_pause_text='  ',
                    display_metadata=['xesam:title', 'xesam:artist'],
                    scroll_interval=scrollint,
                    scroll_wait_intervals=scrollwint,
                    ),
                widget.Mpris2(
                    name='vlc',
                    objname='org.mpris.MediaPlayer2.vlc',
                    scroll_chars=scrollchar,
                    foreground=color[3],
                    fontshadow=color[0],
                    stop_pause_text='  ',
                    display_metadata=['xesam:title', 'xesam:artist'],
                    scroll_interval=scrollint,
                    scroll_wait_intervals=scrollwint,
                    ),
                widget.TextBox(
                    foreground=color[3],
                    fontshadow=color[4],
                    text=" ",
                    mouse_callbacks={'Button1':lambda: qtile.cmd_function(prev)},
                    ),
                widget.TextBox(
                    foreground=color[4],
                    fontshadow=color[1],
                    text="⏸",
                    mouse_callbacks={'Button1':lambda: qtile.cmd_function(play_pause)},
                    ),
                widget.TextBox(
                    foreground=color[3],
                    fontshadow=color[4],
                    text=" ",
                    mouse_callbacks={'Button1':lambda: qtile.cmd_function(nexts)},
                    ),           
                #### Layouts ####
                widget.TextBox(
                    text='  ',
                    foreground=color[5],
                    fontshadow=color[0],
                ),
                widget.CurrentLayout(
                    foreground=color[5],
                    fontshadow=color[0],
                    ),
                #### Pomodoro ####
                widget.WidgetBox(
                    text_closed='  ',
                    text_open='  ',
                    foreground=color[6],
                    fontshadow=color[0],
                    widgets=[widget.Pomodoro(
                        foreground=color[6],
                        fontshadow=color[0],
                        color_active=color[4],
                        color_break=color[3],
                        color_inactive=color[4],
                        length_pomodori=50,
                        length_short_break=5,
                        length_long_break=15,
                        num_pomodori=3,
                        prefix_break=' Break',
                        prefix_inactive=' Pomodoro',
                        prefix_long_break=' Long Break',
                        prefix_paused=' '
                    )],
                ),
                #### Updates ####\
                widget.TextBox(
                    font=awesome_font,
                    foreground=color[3],
                    fontshadow=color[0],
                    text="  ",
                    ),
                widget.CheckUpdates(
                    update_interval=1800,
                    distro='Arch_paru',
                    foreground=color[0],
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(term + ' -e sudo paru -Syu')},
                    display_format="{updates} up",
                    FOREGROUND=color[3],
                    colour_have_updates=color[3],
                    colour_no_updates=color[3],
                    no_update_string=" ",
                    restart_indicator=" ",
                    fontshadow=color[0],
                    ),
                  widget.UPowerWidget(
                    border_charge_colour=color[4],
                    border_colour=color[4],
                    border_critical_colour='cc0000',
                    fill_critical='cc0000',
                    fill_low='aa00aa',
                    fill_normal=color[4],
                    font_colour=color[4],
                    fontshadow=[0]
                ),
                widget.TextBox(
                    font=awesome_font,
                    text="  ",
                    foreground=color[5],
                    fontshadow=color[0],
                    padding=0,
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('pavucontrol')}
                    ),
                widget.ALSAWidget(
                    device='Master',
                    bar_colour_high=color[6],
                    bar_colour_loud="#FF0000",
                    bar_colour_normal=color[4],
                    bar_colour_mute=color[1],
                    hide_interval=3,
                    update_interval=0.1,
                    bar_width=100,
                    mode='bar',
                    fontshadow=color[0],
                ),
                widget.Clock(
                    foreground=color[6],
                    fontshadow=color[0],
                    format="%b %a %d %H:%M",
                    update_interval=1
                    ),
                #### Lock, Logout, Poweroff ####
                widget.TextBox(
                    font=awesome_font,
                    foreground=color[4],
                    fontshadow=color[0],
                    text=" ",
                    mouse_callbacks={'Button1': lambda: qtile.cmd_function(session_widget)}
                    ),
    ]
    return widgets_top

def init_widgets_bott():
    
    widgets_bott = [
                #### Shortcuts ####
                widget.TextBox(
                    font=awesome_font,
                    text="  ",
                    padding=5,
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('rofi -theme "~/.config/rofi/launcher.rasi" -show drun')},
                    foreground=color[7],
                    fontsize=25
                    ),
                widget.TextBox(
                    font=awesome_font,
                    foreground=color[4],
                    text="⚲ ",
                    mouse_callbacks={'Button1':lambda: qtile.cmd_spawn('rofi  -theme "~/.config/rofi/filesfolders.rasi" -show find -modi find:~/.local/bin/finder')}
                    ),        
                widget.TextBox(
                    font=awesome_font,
                    foreground=color[6],
                    text=" ",
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(term)}
                    ),
                widget.TextBox(
                    font=awesome_font,
                    foreground=color[1],
                    text=" ",
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("thunar")}
                    ),
                widget.TextBox(
                    font=awesome_font,
                    foreground=color[3],
                    text=" ",
                    mouse_callbacks={'Button1':lambda: qtile.cmd_function(set_rand_wallpaper)},
                ),
                widget.TextBox(
                    font=awesome_font,
                    foreground=color[8],
                    text=" ",
                    mouse_callbacks={'Button1':lambda: qtile.cmd_function(change_color_scheme)},
                ),
                widget.TextBox(
                    font=awesome_font,
                    foreground=color[1],
                    text="ℹ ",
                    mouse_callbacks={'Button1': lambda: qtile.cmd_function(shortcuts)}
                    ),
                 widget.Sep(
                    foreground=color[4],
                    linewidth=3,
                ),
                widget.WindowName(
                    foreground=color[4],
                    fontshadow=color[0],
                    padding=5,
                    empty_group_string=ver,
                    max_chars=120,
                    format='  {name}',
                    ),
                widget.Sep(
                    foreground=color[1],
                    linewidth=3,
                ),
                #### Network ####
                widget.WidgetBox(
                    text_closed=" " + wifi_icon,
                    text_open='  ',
                    foreground=color[1],
                    fontshadow=color[0],
                    widgets=[widget.TextBox(
                        text='  '+private_ip,
                        foreground=color[8],
                        fontshadow=color[0],
                        mouse_callbacks={'Button1':lambda: qtile.cmd_function(network_widget)}
                        ),
                        widget.TextBox(
                        text='  '+public_ip + wifi_icon,
                        foreground=color[1],
                        fontshadow=color[0],
                        mouse_callbacks={'Button1':lambda: qtile.cmd_function(network_widget)}
                        ),]
                ),
                widget.Wlan(
                    interface=wifi,
                    format=' {essid} {percent:2.0%} ',
                    disconnected_message='Unplugged',
                    foreground=color[1],
                    fontshadow=color[0],
                    mouse_callbacks={'Button1':lambda: qtile.cmd_function(network_widget)}
                    ),
                widget.Net(
                    interface=wifi,
                    format=' {down} ',
                    foreground=color[1],
                    fontshadow=color[0],
                    use_bits=True,
                    mouse_callbacks={'Button1':lambda: qtile.cmd_function(network_widget)}
                    ),
                 widget.Sep(
                    foreground=color[2],
                    linewidth=3,
                ),
                #### Weather ####
                widget.OpenWeather(
                    app_key=w_appkey,
                    cityid=w_cityid,
                    weather_symbols = {
                        "Unknown": "",
                        "01d": "☀",
                        "01n": "🌕",
                        "02d": "",
                        "02n": "",
                        "03d": "",
                        "03n": "",
                        "04d": "",
                        "04n": "",
                        "09d": "⛆",
                        "09n": "⛆",
                        "10d": "⛆",
                        "10n": "⛆",
                        "11d": "🌩",
                        "11n": "🌩",
                        "13d": "❄",
                        "13n": "❄",
                        "50d": "🌫",
                        "50n": "🌫",
                    },
                    foreground=color[2],
                    fontshadow=color[0],
                    format=' {icon} ',
                    metric=True,
                    update_interval=600
                    ),
               widget.OpenWeather(
                    app_key=w_appkey,
                    cityid=w_cityid,
                    foreground=color[2],
                    fontshadow=color[0],
                    format='{main_temp}°{units_temperature}',
                    metric=True,
                    update_interval=600
                    ),
                widget.OpenWeather(
                    app_key=w_appkey,
                    cityid=w_cityid,
                    foreground=color[6],
                    fontshadow=color[0],
                    format='  {location_city}',
                    metric=True,
                    update_interval=600
                    ),
                widget.Sep(
                    foreground=color[3],
                    linewidth=3,
                ),
                #### RAM ####
                widget.TextBox(
                    font=awesome_font,
                    foreground=color[3],
                    fontshadow=color[0],
                    text="  "
                    ),
                widget.Memory(
                    format='{MemUsed:.0f}{mm}/{MemTotal:.0f}{mm} ',
                    foreground=color[3],
                    fontshadow=color[0],
                    padding=5
                    ),
                 widget.Sep(
                    foreground=color[4],
                    linewidth=3,
                ),
                #### CPU ####
                widget.TextBox(
                    font=awesome_font,
                    foreground=color[4],
                    fontshadow=color[0],
                    text="  "
                    ),
                widget.CPU(
                    format='{load_percent}% ',
                    foreground=color[4],
                    fontshadow=color[0],
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(term + ' -e htop')},
                    ),
                 widget.Sep(
                    foreground=color[5],
                    linewidth=3,
                ),
                #### Disk Space ####
                widget.TextBox(
                    font=awesome_font,
                    foreground=color[5],
                    fontshadow=color[0],
                    text="  "
                    ),
                widget.DF(
                    format='{p} ({uf}{m}|{r:.0f}%)',
                    measure='G',
                    Partition='/',
                    update_interval=60,
                    foreground=color[5],
                    fontshadow=color[0],
                    padding=5,
                    visible_on_warn=False,
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(term + ' -e ranger')},
                    warn_color="ff0000"
                    ),
                 widget.Sep(
                    foreground=color[6],
                    linewidth=3,
                ),
                #### Thermal Sensors ####
                widget.TextBox(
                    font=awesome_font,
                    text="  ",
                    foreground=color[6],
                    fontshadow=color[0],
                    ),
                widget.ThermalSensor(
                    tag_sensor="Tctl",
                    fontshadow=color[0],
                    foreground=color[6],
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('~/.local/bin/fans')},
                    ),
                 widget.Sep(
                    foreground=color[7],
                    linewidth=3,
                ),
                #### Keyboard Layout ####
                widget.TextBox(
                    font=awesome_font,
                    text="  ",
                    foreground=color[7],
                    fontshadow=color[0],
                    ),
                widget.KeyboardLayout(
                    configured_keyboards=['us intl', 'latam'],
                    foreground=color[7],
                    fontshadow=color[0],
                    padding=5
                    ),
                 widget.Sep(
                    foreground=color[3],
                    linewidth=3,
                ),
                #### Caps lock Num Lock Indicator ####
                widget.CapsNumLockIndicator(
                    foreground=color[3],
                    fontshadow=color[0],
                    padding=5
                    ),
                #### System Tray ####
                #### Systray ####
                widget.Systray(
                    icon_size=iconsz
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
                background=color[0] + transparency,
                widgets=init_widgets_screen_top(),  
                size=barsz,
                border_color=color[1]+ transparency,
                border_width=bar_top_width,
                opacity=bar_opa,
                ),
            bottom=bar.Bar(
                widgets=init_widgets_screen_bot(),
                size=barsz,
                border_color=color[1]+ transparency,
                border_width=bar_bot_width,
                opacity=bar_opa,
                background=color[0] + transparency,
                )
        ),
        Screen()
        ]

#### End Screens ####

widget_defaults = init_widgets_defaults()
widgets_top = init_widgets_top()
widgets_screen_top = init_widgets_screen_top()
screens = init_screens()
widgets_bott = init_widgets_bott()
widgets_screen_top = init_widgets_screen_top()
init_widgets_screen_bot = init_widgets_screen_bot()
 



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
                widget.Sep(
                    foreground=color[1],
                    linewidth=5,
                ),
                #### Groups ####
                widget.GroupBox(
                    font=awesome_font,
                    disable_drag=True,
                    hide_unused=True,
                    padding_x=6,
                    borderwidth=0,
                    active=color[4],
                    fontshadow=color[0],
                    inactive=color[0],
                    rounded=False,        
                    highlight_color=color[3],
                    highlight_method="text",
                    this_current_screen_border=color[7],
                    this_screen_border=color[3],
                    center_aligned = True,
                    other_current_screen_border=color[3],
                    other_screen_border=color[5],
                    block_highlight_text_color=color[6],
                    foreground=color[2],    
                    urgent_border=color[4]
                    ),
                widget.Sep(
                    foreground=color[2],
                    linewidth=5,
                ),
                widget.Prompt(
                       prompt=prompt,
                       padding=10,
                       foreground=color[2],
                       ),
                widget.Sep(
                    foreground=color[3],
                    linewidth=5,
                ),
                widget.ThermalSensor(
                    background=color[0],
                    foreground=color[3],
                    foreground_alert='ff0000',
                    metric=True,
                    update_interval=1,
                    tag_sensor='Tctl'
                ),
                widget.Sep(
                    foreground=color[5],
                    linewidth=5,
                ),
                widget.NvidiaSensors(
                    background=color[0],
                    foreground=color[5],
                ),
                widget.Sep(
                    foreground=color[6],
                    linewidth=5,
                ),
                widget.WindowName(
                    foreground=color[6],
                    fontshadow=color[0],
                    padding=5,
                    empty_group_string=ver,
                    max_chars=50,
                    format='  {name}',
                    ),
                widget.Spacer(
                    length=bar.STRETCH,
                    foreground=color[0]
                    ),
                widget.Sep(
                    foreground=color[3],
                    linewidth=5,
                ),
                #### Spotify ####
                widget.Mpris2(
                    name='cmus',
                    objname='org.mpris.MediaPlayer2.cmus',
                    scroll_chars=scrollchar,
                    foreground=color[3],
                    fontshadow=color[0],
                    stop_pause_text='  ',
                    display_metadata=['xesam:title', 'xesam:artist'],
                    scroll_interval=scrollint,
                    scroll_wait_intervals=scrollwint,
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
                widget.Sep(
                    foreground=color[4],
                    linewidth=5,
                ),
                widget.WidgetBox(
                    font=awesome_font,
                    text_closed="",
                    text_open='  ',
                    foreground=color[4],
                    fontshadow=color[0],
                    widgets=[widget.TextBox(
                        text=' '+private_ip,
                        foreground=color[4],
                        fontshadow=color[0],
                        mouse_callbacks={'Button1':lambda: qtile.cmd_function(network_widget)}
                        ),
                        widget.TextBox(
                        text=' '+public_ip + " " + wifi_icon,
                        foreground=color[4],
                        fontshadow=color[0],
                        mouse_callbacks={'Button1':lambda: qtile.cmd_function(network_widget)}
                        ),]
                ),
                widget.Wlan(
                    interface=wifi,
                    format='{percent:2.0%}  {essid}',
                    disconnected_message='Unplugged',
                    foreground=color[4],
                    fontshadow=color[0],
                    mouse_callbacks={'Button1':lambda: qtile.cmd_function(network_widget)}
                    ),
                widget.Net(
                    interface=wifi,
                    format='{down}',
                    foreground=color[4],
                    fontshadow=color[0],
                    use_bits=True,
                    mouse_callbacks={'Button1':lambda: qtile.cmd_function(network_widget)}
                    ),
                widget.Sep(
                    foreground=color[5],
                    linewidth=5,
                ),
                widget.WidgetBox(
                    text_closed='',
                    text_open='  ',
                    foreground=color[5],
                    fontshadow=color[0],
                    widgets=[widget.Pomodoro(
                        foreground=color[5],
                        fontshadow=color[0],
                        color_active=color[7],
                        color_break=color[5],
                        color_inactive=color[8],
                        length_pomodori=45,
                        length_short_break=10,
                        length_long_break=25,
                        num_pomodori=3,
                        prefix_break='Break',
                        prefix_inactive='Start',
                        prefix_long_break='Long Break',
                        prefix_paused='Paused'
                    )],
                ),
                widget.Sep(
                    foreground=color[6],
                    linewidth=5,
                ),
                widget.CheckUpdates(
                    update_interval=1800,
                    distro='Arch_paru',
                    foreground=color[6],
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(term + ' -e sudo paru -Syu')},
                    display_format="{updates}",
                    colour_have_updates=color[6],
                    colour_no_updates=color[6],
                    no_update_string="",
                    restart_indicator="",
                    ),
                widget.Sep(
                    foreground=color[4],
                    linewidth=5,
                ),
                widget.ALSAWidget(
                    device='Master',
                    bar_colour_high=color[4],
                    bar_colour_loud="#FF0000",
                    bar_colour_normal=color[4],
                    bar_colour_mute=color[0],
                    hide_interval=3,
                    update_interval=0.1,
                    bar_width=100,
                    mode='bar',
                    fontshadow=color[0],
                    foreground=color[2],
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('pavucontrol')},
                ),
                widget.Sep(
                    foreground=color[2],
                    linewidth=5,
                ),
                widget.Bluetooth(
                    foreground=color[2],
                    fontshadow=color[0],
                    hci='/dev_28_EC_9A_9B_64_72',
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('blueman-manager')}
                ),
                widget.Sep(
                    foreground=color[5],
                    linewidth=5,
                ),
                widget.UPowerWidget(
                    border_charge_colour=color[5],
                    border_colour=color[5],
                    border_critical_colour='#cc0000',
                    fill_critical='#cc0000',
                    fill_low='#FF5511',
                    fill_normal=color[5],
                    foregound=color[5],
                    fontshadow=[0]
                ),
                widget.Sep(
                    foreground=color[3],
                    linewidth=5,
                ),
                widget.Clock(
                    foreground=color[3],
                    fontshadow=color[0],
                    format="%H:%M",
                    update_interval=1
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
                background=color[0],
                widgets=init_widgets_screen_top(),  
                size=barsz,
                )),
        Screen()
        ]

#### End Screens ####

widget_defaults = init_widgets_defaults()
widgets_top = init_widgets_top()
widgets_screen_top = init_widgets_screen_top()
screens = init_screens()
widgets_screen_top = init_widgets_screen_top()

 

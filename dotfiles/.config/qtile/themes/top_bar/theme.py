

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
                    linewidth=lwidth,
                ),
                widget.Sep(
                    foreground=color[2],
                    linewidth=lwidth,
                ),
                widget.Sep(
                    foreground=color[3],
                    linewidth=lwidth,
                ),
                widget.Sep(
                    foreground=color[4],
                    linewidth=lwidth,
                ),
                widget.Sep(
                    foreground=color[5],
                    linewidth=lwidth,
                ),
                 widget.Sep(
                    foreground=color[6],
                    linewidth=lwidth,
                ),
                 widget.Sep(
                    foreground=color[7],
                    linewidth=lwidth,
                ),
                 widget.Sep(
                    foreground=color[8],
                    linewidth=lwidth,
                ),
                #### Groups ####
                widget.GroupBox(
                    font=awesome_font,
                    disable_drag=True,
                    hide_unused=False,
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
                widget.Prompt(
                       prompt=prompt,
                       padding=10,
                       foreground=color[3],
                       ),
                widget.Spacer(
                    length=bar.STRETCH,
                    foreground=color[0]
                    ),
                widget.Clock(
                    foreground=color[2],
                    fontshadow=color[0],
                    format=" %b ",
                    update_interval=1
                    ),
                widget.Clock(
                    foreground=color[4],
                    fontshadow=color[0],
                    format="%a",
                    update_interval=1
                    ),
                widget.Clock(
                    foreground=color[6],
                    fontshadow=color[0],
                    format=" %d ",
                    update_interval=1
                    ),
                widget.Clock(
                    foreground=color[3],
                    fontshadow=color[0],
                    format="%H:%M ",
                    update_interval=1
                    ),
                widget.Spacer(
                    length=bar.STRETCH,
                    foreground=color[0]
                    ),
                #### Spotify ####
                 widget.TextBox(
                    foreground=color[3],
                    fontshadow=color[1],
                    text=" ",
                    mouse_callbacks={'Button1':lambda: qtile.cmd_function(prev)},
                    ),
                widget.TextBox(
                    foreground=color[4],
                    fontshadow=color[1],
                    text="",
                    mouse_callbacks={'Button1':lambda: qtile.cmd_function(play_pause)},
                    ),
                widget.TextBox(
                    foreground=color[3],
                    fontshadow=color[1],
                    text=" ",
                    mouse_callbacks={'Button1':lambda: qtile.cmd_function(nexts)},
                    ),
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
                #### Layouts ####WW
                widget.CurrentLayoutIcon(
                    foreground=color[2],
                    scale=0.8,
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
                    border_critical_colour='#cc0000',
                    fill_critical='#cc0000',
                    fill_low='#FF5511',
                    fill_normal=color[4],
                    foregound=color[4],
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
                    foreground=color[7],
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

#### End Widgets ####

##### Screens #####

def init_widgets_screen_top():
    widgets_screen_top = init_widgets_top()
    return widgets_screen_top

def init_screens():
    return [
        Screen(
            top=bar.Bar(
                margin=[5, 10, 5, 10],
                background=[color[0] + barTransparency],
                widgets=init_widgets_screen_top(),  
                size=barsz,
                border_color=color[1]+ barTransparency,
                border_width=barBorderWidth,
                )),
        Screen()
        ]

#### End Screens ####

widget_defaults = init_widgets_defaults()
widgets_top = init_widgets_top()
widgets_screen_top = init_widgets_screen_top()
screens = init_screens()
widgets_screen_top = init_widgets_screen_top()

 

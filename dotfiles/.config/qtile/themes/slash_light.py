#
# _______  _______  ______  _______  __        
#|       ||   _   ||   __ \|     __||  |.-----.
#|   -  _||       ||      <|__     ||  ||  _  |
#|_______||___|___||___|__||_______||__||   __|
#                                       |__|   
# QARSlp Qtile + Arch Ricing System
# By: gibranlp <thisdoesnotwork@gibranlp.dev>
# MIT licence 
#
from functions import *

# Theme 
## Decorations

powerline = {
    "decorations":[RectDecoration(use_widget_background=True, radius=0, filled=True), PowerLineDecoration(path="forward_slash")],
}

## Screens

screens = [
    Screen(
        bottom=bar.Bar(
            [
            widget.GroupBox(
              background=color[0],
              font=awesome_font,
              disable_drag=True,
              hide_unused=True,
              padding_x=3,
              borderwidth=0,
              active=color[1], #Program opened in that group
              inactive=color[5], # Empty Group
              rounded=False,
              highlight_method="text",
              this_current_screen_border=color[7],
              center_aligned = True,
              other_curren_screen_border=color[7],
              block_highlight_text_color=color[7],    
              urgent_border="fc0000",
              **powerline
            ),
            widget.CurrentLayoutIcon(
              use_mask=True,
              foreground=color[0],
              scale=0.8,
              background=color[3],
              **powerline,
            ),
            widget.TextBox(
              background=color[5],
              foreground=color[0],
              text="",
              **powerline,
            ),
            widget.CPU(
              background=color[5],
              foreground=color[0],
              format='{load_percent}',
              **powerline,
            ),
            widget.TextBox(
            background=color[0],
            foreground=color[2],
            text="",
            **powerline,
            ),
            widget.Memory(
              background=color[0],
              foreground=color[2],
              format='{MemUsed:.0f}{mm}',
              measure_mem='G',
              **powerline,
            ),
            widget.TextBox(
              background=color[4],
              foreground=color[0],
              text="",
              **powerline,
            ),
            widget.WindowName(
              background=color[4],
              foreground=color[0],
              width=widget_width,
              format='{name}',
              scroll=True,
              scroll_delay=2,
              scroll_repeat=True,
              scroll_step=1,  
              **powerline,  
            ),
            widget.Prompt(
              background=color[1],
              prompt=prompt,
              foreground=color[0],
              cursor_color=color[0],
              visual_bell_color=[0],
              visual_bell_time=0.2,
              **powerline,
            ),
            widget.Spacer(
              length=bar.STRETCH,
              background=color[0],
              **powerline,
            ),
            widget.TextBox(
              background=color[3],
              text="",
              foreground=color[0],
              **powerline,
            ),
            # widget.Visualizer(
            #   bar_colour=color[0],
            #   background=color[3],
            #   **powerline,
            # ),
            widget.Mpris2(
              background=color[3],
              mouse_callbacks={'Button1': lambda: qtile.spawn(terminal  + " -e cava")},
              objname=None,
              foreground=color[0],
              width=widget_width,
              format='{xesam:artist} -> {xesam:title}',
              paused_text='Paused',
              scroll=True,
              scroll_repeat=True,
              scroll_delay=0.1,
              **powerline,
            ),
            widget.Spacer(
              length=bar.STRETCH,
              background=color[0],
              **powerline,
            ),
            widget.OpenWeather(
              background=color[1],
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
                update_interval=600,
                **powerline,
            ),
            widget.OpenWeather(
              background=color[1],
              app_key=w_appkey,
              cityid=w_cityid,
              foreground=color[0],
              format='{temp}°{units_temperature}',
              metric=True,
              update_interval=600,
              **powerline,
            ), 
            ## Network
            widget.WidgetBox(
              background=color[0],
              text_closed=wifi_icon,
              text_open='',
              foreground=color[1],
              **powerline,
              widgets=[
                  widget.TextBox(
                  background=color[0],
                  text='',
                  foreground=color[7],
                  mouse_callbacks={'Button1':lambda: qtile.spawn(home + "/.local/bin/wifi2")},
                  **powerline,
                ),
                widget.TextBox(
                  background=color[2],
                  text=private_ip,
                  foreground=color[0],
                  mouse_callbacks={'Button1':lambda: qtile.spawn(home + "/.local/bin/wifi2")},
                  **powerline,
                ),
                widget.TextBox(
                  background=color[0],
                  text='',
                  foreground=color[7],
                  mouse_callbacks={'Button1':lambda: qtile.spawn(home + "/.local/bin/wifi2")},
                  **powerline,
                ),
                widget.TextBox(
                  background=color[4],
                  text=public_ip,
                  foreground=color[0],
                  mouse_callbacks={'Button1':lambda: qtile.spawn(home + "/.local/bin/wifi2")},
                  **powerline,
                ),
                widget.TextBox(
                  background=color[0],
                  text=wifi_icon,
                  foreground=color[1
                                   ],
                  mouse_callbacks={'Button1':lambda: qtile.spawn(home + "/.local/bin/wifi2")},
                  **powerline,
                ),
                # widget.Wlan(
                #  decorations=[RectDecoration(colour=color[0], radius=0, filled=True)],
                #  interface=wifi,
                #  format='{essid}',
                #  disconnected_message='',
                #  foreground=color[3],
                #  mouse_callbacks={'Button1':lambda: qtile.cmd_function(network_widget)}
                # ),
              ]
            ),
            # widget.Wlan(
            #       decorations=[RectDecoration(colour=color[0],radius=0, filled=True)],
            #       interface=wifi,
            #       format='{percent:2.0%}',
            #       disconnected_message='',
            #       foreground=color[3],
            #       mouse_callbacks={'Button1':lambda: qtile.cmd_function(network_widget)}
            #     ),
            widget.Net(
              prefix='M',
              interface=wifi,
              format='{down:4.1f}↓↑{up:3.1f}',
              foreground=color[1],
              use_bits=True,
              mouse_callbacks={'Button1':lambda: qtile.spawn(home + "/.local/bin/wifi2")},
              background=color[0],
              **powerline,
            ),
            widget.TextBox(
              background=color[2],
              text="",
              foreground=color[0],
              **powerline,
            ),
            widget.KeyboardLayout(
              background=color[2],
              configured_keyboards=['us intl', 'latam'],
              foreground=color[0],
              **powerline,
            ),
            widget.TextBox(
              background=color[0],
              text="",
              foreground=color[5],
              mouse_callbacks={'Button1': lambda: qtile.spawn('pavucontrol')},
              **powerline,
            ),
            widget.ALSAWidget(
              background=color[0],
              device='Master',
              bar_colour_high=color[4],
              bar_colour_loud=color[2],
              bar_colour_normal=color[5],
              bar_colour_mute=color[1],
              hide_interval=3,
              update_interval=0.1,
              bar_width=80,
              mode='bar',
              foreground=color[0],
              text_format=' ',
              **powerline,
            ),
            widget.Clock(
              foreground=color[0],
              format="%a %d %H:%M",
              update_interval=1,
              background=color[4],
              mouse_callbacks={'Button1': lambda: qtile.function(calendar_notification),'Button4': lambda: qtile.function(calendar_notification_prev),'Button5': lambda: qtile.function(calendar_notification_next)}, 
              **powerline,
            ),
            widget.UPowerWidget(
               border_charge_colour=color[7],
               border_colour=color[3],
               border_critical_colour='#cc0000',
               fill_critical='#cc0000',
               fill_low='#FF5511',
               fill_normal=color[3],
               foreground=color[3],
               background=color[0],
               percentage_critical=0.2,
               percentage_low=0.4,
               text_charging=' ({percentage:.0f}%) {ttf} to ',
               text_discharging=' ({percentage:.0f}%) {tte} Left',
               **powerline,
            ),
            ## Lock, Logout, Poweroff
            widget.TextBox(
              background=color[0],
              foreground=color[7],
              text="",
              mouse_callbacks={'Button1': lambda: qtile.cmd_function(session_widget)},
            ),
              ],
              size=bar_size,
              background=transparent,
              margin=[0,5,5,5],
          ),
    ),
]

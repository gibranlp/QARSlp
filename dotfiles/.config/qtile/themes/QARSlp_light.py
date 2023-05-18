#
# _______  _______  ______  _______  __        
#|       ||   _   ||   __ \|     __||  |.-----.
#|   -  _||       ||      <|__     ||  ||  _  |
#|_______||___|___||___|__||_______||__||   __|
#                                       |__|   
# QARSlp Qtile + Arch Ricing System
# By: gibranlp <thisdoesnotwork@gibranlp.dev>
# MIT licence 
# QARSlp Light Theme

from functions import *

# Theme
## Screens

screens = [
    Screen(
        bottom=bar.Bar(
            [
            widget.GroupBox(
              decorations=[RectDecoration(colour=color[1], radius=7, filled=True)],
              font=awesome_font,
              disable_drag=True,
              hide_unused=True,
              borderwidth=0,
              active=color[0], #Program opened in that group
              inactive=color[2], # Empty Group
              rounded=False,
              highlight_method="text",
              this_current_screen_border=color[7],
              center_aligned = True,
              other_curren_screen_border=color[7],
              block_highlight_text_color=color[7],    
              urgent_border="fc0000",
            ),
            widget.Spacer(
              length=5,
              background=transparent,
            ),
            widget.CurrentLayoutIcon(
              use_mask=True,
              decorations=[RectDecoration(colour=color[2], radius=7, filled=True)],
              foreground=color[7],
              scale=0.7,
            ),
            widget.Spacer(
              length=5,
              background=transparent,
            ),
            widget.TextBox(
              decorations=[RectDecoration(colour=color[2], radius=[7,0,0,7], filled=True)],
              foreground=color[7],
              text="",
            ),
            widget.CPU(
              decorations=[RectDecoration(colour=color[3], radius=[0,7,7,0], filled=True)],
              foreground=color[0],
              format='{load_percent}'
            ),
            widget.Spacer(
              length=5,
              background=transparent,
            ),
            widget.TextBox(
            decorations=[RectDecoration(colour=color[3], radius=[7,0,0,7], filled=True)],
            foreground=color[7],
            text="",
            ),
            widget.Memory(
              decorations=[RectDecoration(colour=color[4], radius=[0,7,7,0], filled=True)],
              foreground=color[0],
              format='{MemUsed:.0f}{mm}',
              measure_mem='G',
            ),
            widget.Spacer(
                length=5,
                background=transparent,
            ),
            widget.TextBox(
              decorations=[RectDecoration(colour=color[4], radius=[7,0,0,7], filled=True)],
              foreground=color[7],
              text="",
            ),
            widget.WindowName(
              decorations=[RectDecoration(colour=color[5], radius=[0,7,7,0], filled=True)],
              foreground=color[0],
              width=widget_width,
              format='{name}',
              scroll=True,
              scroll_delay=2,
              scroll_repeat=True,
              scroll_step=1,
            ),
            widget.Spacer(
              length=5,
              background=transparent,
            ),
            widget.Prompt(
              decorations=[RectDecoration(colour=color[5], radius=7, filled=True)],
              prompt=prompt,
              foreground=color[7],
              cursor_color=color[7],
              visual_bell_color=[7],
              visual_bell_time=0.2,
            ),
            # widget.Pomodoro(
            #   decorations=[RectDecoration(colour=color[2], radius=[7,0,0,7], filled=True)],
            #   foreground=color[0],
            #   color_active=color[0],
            #   color_break='ffff00',
            #   color_inactive=color[0],
            #   length_long_break=30,
            #   length_pomodori=45,
            #   length_short_break=15,
            #   notification_on=True,
            #   num_pomodori=2,
            #   prefix_active=' ',
            #   prefix_inactive='',
            #   prefix_break=' Break!',
            #   prefix_long_break=' Long Break!',
            #   prefix_paused=' ',
            #   scroll=True,
            #   width=250,
            # ),
            widget.TextBox(
              decorations=[RectDecoration(colour=color[6], radius=[7,0,0,7], filled=True)],
              text="",
              foreground=color[7],
            ),
            widget.Mpris2(
              decorations=[RectDecoration(colour=color[5], radius=[0,7,7,0], filled=True)],
              mouse_callbacks={'Button1': lambda: qtile.spawn(terminal  + " -e cava")},
              objname=None,
              foreground=color[0],
              width=widget_width,
              format=' {xesam:artist} -  {xesam:title}',
              paused_text='Paused',
              scroll=True,
              scroll_repeat=True,
              scroll_delay=0.1,
            ),
            widget.Spacer(
              length=bar.STRETCH,
              background=transparent,
            ),
            widget.Systray(),
            widget.OpenWeather(
              decorations=[RectDecoration(colour=color[5], radius=[7,0,0,7], filled=True)],
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
                
            ),
            widget.OpenWeather(
              decorations=[RectDecoration(colour=color[4], radius=[0,7,7,0], filled=True)],
              app_key=w_appkey,
              cityid=w_cityid,
              foreground=color[7],
              format='{temp}°{units_temperature}',
              metric=True,
              update_interval=600,
            ),
            widget.Spacer(
              length=5,
              background=transparent,
            ), 
            ## Network
            widget.WidgetBox(
              decorations=[RectDecoration(colour=color[0], radius=[7,0,0,7], filled=True)],
              text_closed=' ' + wifi_icon + ' ',
              text_open='  ',
              foreground=color[3],
              widgets=[
                  widget.TextBox(
                  decorations=[RectDecoration(colour=color[0], radius=0,filled=True)],
                  text='  ',
                  foreground=color[3],
                  mouse_callbacks={'Button1':lambda: qtile.spawn(home + "/.local/bin/wifi2")}),
                widget.TextBox(
                  decorations=[RectDecoration(colour=color[3], radius=0, filled=True)],
                  text=private_ip,
                  foreground=color[0],
                  mouse_callbacks={'Button1':lambda: qtile.spawn(home + "/.local/bin/wifi2")}),
                widget.TextBox(
                  decorations=[RectDecoration(colour=color[0], radius=0, filled=True)],
                  text='  ',
                  foreground=color[3],
                  mouse_callbacks={'Button1':lambda: qtile.spawn(home + "/.local/bin/wifi2")}),
                widget.TextBox(
                  decorations=[RectDecoration(colour=color[2], radius=0, filled=True)],
                  text=public_ip,
                  foreground=color[0],
                  mouse_callbacks={'Button1':lambda: qtile.spawn(home + "/.local/bin/wifi2")}),
                widget.TextBox(
                  decorations=[RectDecoration(colour=color[0], radius=0, filled=True)],
                  text=wifi_icon,
                  foreground=color[3],
                  mouse_callbacks={'Button1':lambda: qtile.spawn(home + "/.local/bin/wifi2")}),
                # widget.Wlan(
                #  decorations=[RectDecoration(colour=color[0], radius=0, filled=True)],
                #  interface=wifi,
                #  format='{essid}',
                #  disconnected_message='',
                #  foreground=color[3],
                #  mouse_callbacks={'Button1':lambda: qtile.function(network_widget)}
                # ),
              ]
            ),
            # widget.Wlan(
            #       decorations=[RectDecoration(colour=color[0],radius=0, filled=True)],
            #       interface=wifi,
            #       format='{percent:2.0%}',
            #       disconnected_message='',
            #       foreground=color[3],
            #       mouse_callbacks={'Button1':lambda: qtile.function(network_widget)}
            #     ),
            widget.Net(
              prefix='M',
              interface=wifi,
              format='{down:4.1f}↓↑{up:3.1f}',
              foreground=color[0],
              use_bits=True,
              mouse_callbacks={'Button1':lambda: qtile.function(network_widget)},
              decorations=[RectDecoration(colour=color[3], radius=[0,7,7,0], filled=True)],
            ),
            widget.Spacer(
              length=5,
              background=transparent,
            ),
            widget.TextBox(
              decorations=[RectDecoration(colour=color[3], radius=[7,0,0,7], filled=True)],
              text="",
              foreground=color[0],
            ),
            widget.KeyboardLayout(
              decorations=[RectDecoration(colour=color[2], radius=[0,7,7,0], filled=True)],
              configured_keyboards=['us intl', 'latam'],
              foreground=color[0],
            ),
            widget.Spacer(
              length=5,
              background=transparent,
            ),
            widget.TextBox(
              decorations=[RectDecoration(colour=color[2], radius=[7,0,0,7], filled=True)],
              text="",
              foreground=color[0],
              mouse_callbacks={'Button1': lambda: qtile.spawn('pavucontrol')}
            ),
            widget.ALSAWidget(
              decorations=[RectDecoration(colour=color[5], radius=[0,7,7,0], filled=True)],
              device='Master',
              bar_colour_high=color[0],
              bar_colour_loud=color[0],
              bar_colour_normal=color[0],
              bar_colour_mute=color[5],
              hide_interval=5,
              update_interval=0.1,
              bar_width=80,
              mode='bar',
              foreground=color[1],
              text_format=' ',
            ),
            widget.Spacer(
              length=5,
              background=transparent,
            ),
            widget.Clock(
              foreground=color[0],
              format="%a",
              update_interval=1,
              decorations=[RectDecoration(colour=color[3], radius=[7,0,0,7], filled=True)],
              mouse_callbacks={'Button1': lambda: qtile.function(calendar_notification),'Button4': lambda: qtile.function(calendar_notification_prev),'Button5': lambda: qtile.function(calendar_notification_next)},
            ),
            widget.Clock(
              foreground=color[3],
              format="%d",
              update_interval=1,
              decorations=[RectDecoration(colour=color[0], radius=0,filled=True)],
              mouse_callbacks={'Button1': lambda: qtile.function(calendar_notification),'Button4': lambda: qtile.function(calendar_notification_prev),'Button5': lambda: qtile.function(calendar_notification_next)},
            ),
            widget.Clock(
              foreground=color[0],
              format="%H:%M",
              update_interval=1,
              decorations=[RectDecoration(colour=color[3], radius=[0,7,7,0], filled=True)],
              mouse_callbacks={'Button1': lambda: qtile.function(calendar_notification),'Button4': lambda: qtile.function(calendar_notification_prev),'Button5': lambda: qtile.function(calendar_notification_next)},              
            ),
            widget.Spacer(
              length=5,
              background=transparent,
            ),
            widget.UPowerWidget(
               border_charge_colour=color[7],
               border_colour=color[3],
               border_critical_colour='#cc0000',
               fill_critical='#cc0000',
               fill_low='#FF5511',
               fill_normal=color[3],
               foreground=color[3],
               decorations=[RectDecoration(colour=color[0], radius=[7,0,0,7], filled=True)],
               percentage_critical=0.2,
               percentage_low=0.4,
               text_charging=' ({percentage:.0f}%) {ttf} to ',
               text_discharging=' ({percentage:.0f}%) {tte} Left',
            ),
            ## Lock, Logout, Poweroff
            widget.TextBox(
              decorations=[RectDecoration(colour=color[6], radius=[0,7,7,0], filled=True)],
              foreground=color[0],
              text="",
              mouse_callbacks={'Button1': lambda: qtile.function(session_widget)}
            ),
              ],
              size=bar_size,
              background=transparent,
              margin=bar-margin,
          ),
    ),
]

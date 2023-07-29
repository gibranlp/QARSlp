# _______  _______  ______  _______  __        
#|       ||   _   ||   __ \|     __||  |.-----.
#|   -  _||       ||      <|__     ||  ||  _  |
#|_______||___|___||___|__||_______||__||   __|
#                                       |__|   
# SpectrumOS - Embrace the Chromatic Symphony!
# By: gibranlp <thisdoesnotwork@gibranlp.dev>
# MIT licence
from functions import *

# Theme 
## Screens

def init_widgets_list():
    widgets_list = [
        widget.GroupBox(
          background=color[0],
          fontsize=groups_font,
          font=awesome_font,
          disable_drag=True,
          hide_unused=hide_unused_groups,
          padding_x=3,
          borderwidth=0,
          active=color[3], #Program opened in that group
          inactive=color[6], # Empty Group
          rounded=False,
          highlight_method="text",
          this_current_screen_border=color[2],
          center_aligned = True,
          other_curren_screen_border=color[2],
          block_highlight_text_color=color[2],    
          urgent_border="fc0000",
        ),
        widget.WindowName(
          background=color[0],
          foreground=color[2],
          format='{name}',
          scroll=True,
          scroll_delay=2,
          scroll_repeat=True,
          scroll_step=1,
          width=500,
        ),
        widget.Prompt(
          background=color[0],
          prompt=prompt,
          foreground=color[4],
          cursor_color=color[4],
          visual_bell_color=[4],
        ),
        widget.Spacer(
          length=bar.STRETCH,
          background=color[0],
        ),
        widget.Mpris2(
          background=color[0],
          mouse_callbacks={'Button1': lambda: qtile.spawn(terminal  + " -e cava")},
          objname=None,
          foreground=color[6],
          width=widget_width,
          format=' {xesam:artist} -  {xesam:title}',
          stopped_text="Stop",
          paused_text='  ',
          scroll=True,
          scroll_repeat=True,
          scroll_delay=0.1,
        ),
        widget.OpenWeather(
          background=color[0],
          app_key=w_appkey,
          cityid=w_cityid,
          weather_symbols={
            "Unknown": "",
            "01d": "",
            "01n": "",
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
            foreground=color[5],
            metric=True,
            update_interval=600, 
        ),
        ## Network
        widget.TextBox(
          background=color[0],
          text=wifi_icon,
          foreground=color[3],
          mouse_callbacks={'Button1': lambda: qtile.function(network_widget)},
          ),
        widget.ALSAWidget(
          background=color[0],
          device='Master',
          bar_colour_high=color[5],
          bar_colour_loud=color[5],
          bar_colour_normal=color[5],
          bar_colour_mute=color[5],
          hide_interval=5,
          update_interval=0.1,
          bar_width=80,
          mode='bar',
          foreground=color[0],
          text_format=' ',
        ),
        widget.Clock(
          foreground=color[1],
          format="%a %d %H:%M",
          update_interval=1,
          background=color[0],
          mouse_callbacks={'Button1': lambda: qtile.function(calendar_notification),'Button4': lambda: qtile.function(calendar_notification_prev),'Button5': lambda: qtile.function(calendar_notification_next)}, 
        ),
        widget.UPowerWidget(
            border_charge_colour=color[2],
            border_colour=secondary_color[0],
            border_critical_colour='#cc0000',
            fill_critical='#cc0000',
            fill_low='#FF5511',
            fill_normal=color[2],
            foreground=color[2],
            background=color[0],
            percentage_critical=0.2,
            percentage_low=0.4,
            text_charging=' ({percentage:.0f}%) {ttf} to ',
            text_discharging=' ({percentage:.0f}%) {tte} Left',
        ),
        ## Lock, Logout, Poweroff
        widget.TextBox(
          background=color[0],
          foreground=color[2],
          text="",
          mouse_callbacks={'Button1': lambda: qtile.function(session_widget)},
        )]
    return widgets_list

def screen1_widgets():
    widgets_screen1=init_widgets_list()
    return widgets_screen1


def init_screens_bottom():
    return[Screen(bottom=bar.Bar(widgets=screen1_widgets(),size=bar_size,background=transparent,margin=bar_margin))]

def init_screens_top():
    return[Screen(top=bar.Bar(widgets=screen1_widgets(),size=bar_size,background=transparent,margin=bar_margin))]

if bar_position == "top":
    screens=init_screens_top()
else:
  screens=init_screens_bottom()

widgets_list = init_widgets_list()
widgets_screen1 = screen1_widgets()
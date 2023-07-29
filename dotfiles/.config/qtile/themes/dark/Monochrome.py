# _______  _______  ______  _______  __        
#|       ||   _   ||   __ \|     __||  |.-----.
#|   -  _||       ||      <|__     ||  ||  _  |
#|_______||___|___||___|__||_______||__||   __|
#                                       |__|   
# SpectrumOS - Embrace the Chromatic Symphony!
# By: gibranlp <thisdoesnotwork@gibranlp.dev>
# MIT licence
from functions import *
# Fix for widget Width
widget_width=widget_width+100

# Theme
## Screens

color_in_use=color[1]
secondary_in_use=secondary_color[1]

def init_widgets_list():
    widgets_list = [
      widget.TextBox(
        decorations=[RectDecoration(colour=color[0], radius=7, filled=True)],
        foreground=color_in_use,
        text=" QARSlp",
        padding_x=5,
        mouse_callbacks={'Button1':lambda: qtile.spawn('rofi -show drun -show-icons -theme "~/.config/rofi/launcher.rasi"')},
      ),
      widget.Spacer(
        length=5,
        background=transparent,
      ),
      widget.GroupBox(
        decorations=[RectDecoration(colour=color[0], radius=7, filled=True)],
        font=main_font,
        disable_drag=True,
        hide_unused=hide_unused_groups,
        fontsize=font_size,
        borderwidth=0,
        active=secondary_in_use, #Program opened in that group
        inactive=secondary_color[0], # Empty Group
        rounded=False,
        highlight_method="text",
        this_current_screen_border=color_in_use,
        center_aligned = True,
        other_curren_screen_border=color_in_use,
        block_highlight_text_color=color_in_use,    
        urgent_border="fc0000",
        padding_y=10,
      ),
      widget.Spacer(
        length=5,
        background=transparent,
      ),
      widget.Mpris2(
        decorations=[RectDecoration(colour=color[0], radius=7, filled=True)],
        mouse_callbacks={'Button1': lambda: qtile.spawn(terminal  + " -e cava")},
        objname=None,
        foreground=color_in_use,
        width=widget_width,
        format='{xesam:artist}  {xesam:title}',
        stopped_text="Stop",
        paused_text='  ',
        scroll=True,
        scroll_repeat=True,
        scroll_delay=0.1,
      ),
      widget.Spacer(
        length=5,
        background=transparent,
      ),
      widget.WidgetBox(
        decorations=[RectDecoration(colour=color[0], radius=5, filled=True)],
        text_closed='',
        text_open='',
        foreground=color_in_use,
        widgets=[
            widget.Systray(),]
      ),
      widget.Spacer(
        length=5,
        background=transparent,
      ),
      widget.Prompt(
        decorations=[RectDecoration(colour=color[0], radius=7, filled=True)],
        prompt=prompt,
        foreground=color_in_use,
        cursor_color=color_in_use,
        visual_bell_color=color[1],
        visual_bell_time=0.2,
      ),
      widget.Spacer(
        length=bar.STRETCH,
        background=transparent,
      ),
      widget.WindowName(
        decorations=[RectDecoration(colour=color[0], radius=7, filled=True)],
        foreground=color_in_use,
        width=widget_width,
        format='{name}',
        scroll=True,
        scroll_delay=2,
        scroll_repeat=True,
        scroll_step=1,
        padding=10,
      ),
      widget.Spacer(
        length=bar.STRETCH,
        background=transparent,
      ),
      widget.OpenWeather(
        decorations=[RectDecoration(colour=color[0], radius=7, filled=True)],
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
          format='{icon} {temp}°{units_temperature}',
          foreground=color_in_use,
          metric=True,
          update_interval=600,
          padding=10,  
      ),
      widget.Spacer(
        length=5,
        background=transparent,
      ), 
      ## Network
        widget.TextBox(
          decorations=[RectDecoration(colour=color[0], radius=[7,0,0,7],filled=True)],
          text=' ' + wifi_icon + ' ',
          foreground=color_in_use,
          mouse_callbacks={'Button1':lambda: qtile.function(network_widget)}
        ),
      widget.Wlan(
        decorations=[RectDecoration(colour=color[0],radius=0, filled=True)],
        interface=wifi,
        format='{percent:2.0%} ',
        disconnected_message='',
        foreground=color_in_use,
        mouse_callbacks={'Button1':lambda: qtile.function(network_widget)}
      ),
      widget.KeyboardLayout(
        decorations=[RectDecoration(colour=color[0], radius=[0,7,7,0],filled=True)],
        configured_keyboards=['us intl', 'latam'],
        foreground=color_in_use,
      ),
      widget.Spacer(
        length=5,
        background=transparent,
      ),
      widget.TextBox(
        decorations=[RectDecoration(colour=color[0], radius=[7,0,0,7], filled=True)],
        text="",
        foreground=color_in_use,
        mouse_callbacks={'Button1': lambda: qtile.spawn('pavucontrol'),'Button4': lambda: qtile.spawn("amixer -q set Master 5%+ && dunstify -a Volume ' '$(pamixer --get-volume-human) -h int:value:$(pamixer --get-volume)", shell=True),'Button5': lambda: qtile.spawn("amixer -q set Master 5%- && dunstify -a Volume ' '$(pamixer --get-volume-human) -h int:value:$(pamixer --get-volume)", shell=True)},
      ),
      widget.ALSAWidget(
        decorations=[RectDecoration(colour=color_in_use, radius=0, filled=True)],
        device='Master',
        bar_colour_high=color[0],
        bar_colour_loud=color[0],
        bar_colour_normal=color[0],
        bar_colour_mute=color_in_use,
        hide_interval=5,
        update_interval=0.1,
        bar_width=80,
        mode='bar',
        text_format=' ',
      ),
      widget.TextBox(
        decorations=[RectDecoration(colour=color[0], radius=[0,7,7,0], filled=True)],
        text=" ",
        foreground=color[5],
        mouse_callbacks={'Button1': lambda: qtile.spawn('pavucontrol'),'Button4': lambda: qtile.spawn("amixer -q set Master 5%+ && dunstify -a Volume ' '$(pamixer --get-volume-human) -h int:value:$(pamixer --get-volume)", shell=True),'Button5': lambda: qtile.spawn("amixer -q set Master 5%- && dunstify -a Volume ' '$(pamixer --get-volume-human) -h int:value:$(pamixer --get-volume)", shell=True)},
      ),
      widget.Spacer(
        length=5,
        background=transparent,
      ),
      widget.UPowerWidget(
          border_charge_colour=color_in_use,
          border_colour=secondary_color[0],
          border_critical_colour='#cc0000',
          fill_critical='#cc0000',
          fill_low='#FF5511',
          fill_normal=color_in_use,
          foreground=color_in_use,
          decorations=[RectDecoration(colour=color[0], radius=7, filled=True)],
          percentage_critical=0.2,
          percentage_low=0.4,
          text_charging=' ({percentage:.0f}%) {ttf} to ',
          text_discharging=' ({percentage:.0f}%) {tte} Left',
      ),
      widget.Spacer(
        length=5,
        background=transparent,
      ),
      widget.Clock(
        decorations=[RectDecoration(colour=color[0], radius=7, filled=True)],
        foreground=color_in_use,
        format="%A %H:%M",
        update_interval=1,
        mouse_callbacks={'Button1': lambda: qtile.function(calendar_notification),'Button4': lambda: qtile.function(calendar_notification_prev),'Button5': lambda: qtile.function(calendar_notification_next)},
      ),
      
      ]
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
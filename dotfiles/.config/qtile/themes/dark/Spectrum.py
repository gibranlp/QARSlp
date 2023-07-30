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
            widget.CurrentLayoutIcon(
              use_mask=True,
              decorations=[RectDecoration(colour=color[3], radius=7, filled=True)],
              foreground=color[0],
              scale=0.8,
            ),
            widget.Spacer(
              length=5,
              background=transparent,
            ),
            widget.TextBox(
              decorations=[RectDecoration(colour=color[0], radius=[7,0,0,7], filled=True)],
              foreground=color[5],
              text="",
            ),
            widget.CPU(
              decorations=[RectDecoration(colour=color[5], radius=[0,7,7,0], filled=True)],
              foreground=color[0],
              format='{load_percent}%'
            ),
            widget.Spacer(
              length=5,
              background=transparent,
            ),
            widget.TextBox(
            decorations=[RectDecoration(colour=color[0], radius=[7,0,0,7], filled=True)],
            foreground=color[1],
            text="",
            ),
            widget.Memory(
              decorations=[RectDecoration(colour=color[1], radius=[0,7,7,0], filled=True)],
              foreground=color[0],
              format='{MemUsed:.0f}{mm}',
              measure_mem='M',
            ),
            widget.Spacer(
                length=5,
                background=transparent,
            ),
            widget.TextBox(
              decorations=[RectDecoration(colour=color[0], radius=[7,0,0,7], filled=True)],
              foreground=color[2],
              text="",
            ),
            widget.WindowName(
              decorations=[RectDecoration(colour=color[2], radius=[0,7,7,0], filled=True)],
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
            widget.TextBox(
              decorations=[RectDecoration(colour=color[0], radius=[7,0,0,7], filled=True)],
              text="",
              foreground=color[6],
            ),
            widget.Mpris2(
              decorations=[RectDecoration(colour=color[6], radius=[0,0,0,0], filled=True)],
              mouse_callbacks={'Button1': lambda: qtile.spawn(terminal  + " -e cava")},
              objname=None,
              foreground=color[0],
              width=widget_width,
              format='{xesam:artist}  {xesam:title}',
              stopped_text="Stop",
              paused_text='  ',
              scroll=True,
              scroll_repeat=True,
              scroll_delay=0.1,
            ),
            widget.TextBox(
              decorations=[RectDecoration(colour=color[0], radius=[0,7,7,0], filled=True)],
              text="",
              foreground=color[6],
              mouse_callbacks={'Button1': lambda: qtile.spawn(terminal  + " -e cava")},
            ),
            widget.Spacer(
              length=5,
              background=transparent,
            ),
            widget.Pomodoro(
              decorations=[RectDecoration(colour=color[1], radius=7, filled=True)],
              foreground=color[0],
              color_active=color[0],
              color_break=color[0],
              color_inactive=color[0],
              length_long_break=30,
              length_pomodori=45,
              length_short_break=15,
              notification_on=True,
              num_pomodori=3,
              prefix_active=' ',
              prefix_inactive='',
              prefix_break=' ',
              prefix_long_break=' ',
              prefix_paused=' ',
            ),
            widget.Spacer(
              length=5,
              background=transparent,
            ),
            widget.WidgetBox(
              decorations=[RectDecoration(colour=secondary_color[5], radius=4, filled=True)],
              text_closed='',
              text_open='',
              foreground=color[0],
              widgets=[
                  widget.Spacer(
                  length=5,
                  background=transparent,
            ),
                  widget.Systray(),]
            ),
            widget.Spacer(
              length=5,
              background=transparent,
            ),
            widget.Prompt(
              decorations=[RectDecoration(colour=secondary_color[0], radius=7, filled=True)],
              prompt=prompt,
              foreground=color[4],
              cursor_color=color[4],
              visual_bell_color=[4],
              visual_bell_time=0.2,
              padding=5,
            ),
            widget.Spacer(
              length=5,
              background=transparent,
            ),
            widget.Spacer(
              length=bar.STRETCH,
              background=transparent,
            ),
            widget.GroupBox(
              decorations=[RectDecoration(colour=color[0], radius=7, filled=True)],
              fontsize=groups_font,
              font=awesome_font,
              disable_drag=True,
              hide_unused=hide_unused_groups,
              borderwidth=0,
              active=color[3], #Program opened in that group
              inactive=color[6], # Empty Group
              rounded=False,
              highlight_method="text",
              this_current_screen_border=secondary_color[1],
              center_aligned = True,
              other_curren_screen_border=secondary_color[1],
              block_highlight_text_color=secondary_color[1],    
              urgent_border="fc0000",
              #visible_groups=['Escape','1','2','3','4'],
            ),
            widget.Spacer(
              length=bar.STRETCH,
              background=transparent,
            ),
            widget.OpenWeather(
              decorations=[RectDecoration(colour=color[0], radius=[7,0,0,7], filled=True)],
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
            widget.OpenWeather(
              decorations=[RectDecoration(colour=color[5], radius=[0,7,7,0], filled=True)],
              app_key=w_appkey,
              scroll=True,
              width=widget_width -60,
              cityid=w_cityid,
              foreground=color[0],
              format='{temp}°{units_temperature} {weather_details}',
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
                  mouse_callbacks={'Button1':lambda: qtile.function(network_widget)}),
                widget.TextBox(
                  decorations=[RectDecoration(colour=color[3], radius=0, filled=True)],
                  text=private_ip,
                  foreground=color[0],
                  mouse_callbacks={'Button1':lambda: qtile.function(network_widget)}),
                widget.TextBox(
                  decorations=[RectDecoration(colour=color[0], radius=0, filled=True)],
                  text='  ',
                  foreground=color[3],
                  mouse_callbacks={'Button1':lambda: qtile.function(network_widget)}),
                widget.TextBox(
                  decorations=[RectDecoration(colour=color[2], radius=0, filled=True)],
                  text=public_ip,
                  foreground=color[0],
                  mouse_callbacks={'Button1':lambda: qtile.function(network_widget)}),
                widget.TextBox(
                  decorations=[RectDecoration(colour=color[0], radius=0, filled=True)],
                  text=wifi_icon,
                  foreground=color[3],
                  mouse_callbacks={'Button1':lambda: qtile.function(network_widget)}),
              ]
            ),
            widget.Wlan(
                  decorations=[RectDecoration(colour=color[3], radius=0, filled=True)],
                  interface=wifi,
                  format='{essid} {percent:2.0%}',
                  disconnected_message='',
                  foreground=color[0],
                  width=widget_width -20,
                  scroll=True,
                  scroll_repeat=True,
                  scroll_interval=0.1,
                  scroll_step=1,
                  update_interval=1,
                  mouse_callbacks={'Button1':lambda: qtile.function(network_widget)}),
            widget.Net(
              prefix='M',
              interface=wifi,
              format='{down:1.1f}M',
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
              decorations=[RectDecoration(colour=color[0], radius=[7,0,0,7], filled=True)],
              text="",
              foreground=secondary_color[4],
              mouse_callbacks={'Button1': lambda: qtile.spawn('pavucontrol'),'Button4': lambda: qtile.spawn("amixer -q set Master 5%+ && dunstify -a Volume ' '$(pamixer --get-volume-human) -h int:value:$(pamixer --get-volume)", shell=True),'Button5': lambda: qtile.spawn("amixer -q set Master 5%- && dunstify -a Volume ' '$(pamixer --get-volume-human) -h int:value:$(pamixer --get-volume)", shell=True)},
            ),
            widget.ALSAWidget(
              decorations=[RectDecoration(colour=color[0], radius=0, filled=True)],
              device='Master',
              bar_colour_high=secondary_color[4],
              bar_colour_normal=secondary_color[4],
              bar_colour_mute=secondary_color[1],
              hide_interval=5,
              update_interval=0.1,
              bar_width=50,
              mode='bar',
              text_format=' ',
            ),
            widget.TextBox(
              decorations=[RectDecoration(colour=color[0], radius=[0,7,7,0], filled=True)],
              text=" ",
              foreground=color[2],
              mouse_callbacks={'Button1': lambda: qtile.spawn('pavucontrol'),'Button4': lambda: qtile.spawn("amixer -q set Master 5%+ && dunstify -a Volume ' '$(pamixer --get-volume-human) -h int:value:$(pamixer --get-volume)", shell=True),'Button5': lambda: qtile.spawn("amixer -q set Master 5%- && dunstify -a Volume ' '$(pamixer --get-volume-human) -h int:value:$(pamixer --get-volume)", shell=True)},
            ),
            widget.Spacer(
              length=5,
              background=transparent,
            ),
            widget.Clock(
              foreground=color[0],
              format="%a",
              update_interval=1,
              decorations=[RectDecoration(colour=color[1], radius=[7,0,0,7], filled=True)],
              mouse_callbacks={'Button1': lambda: qtile.function(calendar_notification),'Button4': lambda: qtile.function(calendar_notification_prev),'Button5': lambda: qtile.function(calendar_notification_next)},
            ),
            widget.Clock(
              foreground=color[1],
              format="%d",
              update_interval=1,
              decorations=[RectDecoration(colour=color[0], radius=0,filled=True)],
              mouse_callbacks={'Button1': lambda: qtile.function(calendar_notification),'Button4': lambda: qtile.function(calendar_notification_prev),'Button5': lambda: qtile.function(calendar_notification_next)},
            ),
            widget.Clock(
              foreground=color[0],
              format="%H:%M",
              update_interval=1,
              decorations=[RectDecoration(colour=color[1], radius=[0,7,7,0], filled=True)],
              mouse_callbacks={'Button1': lambda: qtile.function(calendar_notification),'Button4': lambda: qtile.function(calendar_notification_prev),'Button5': lambda: qtile.function(calendar_notification_next)},              
            ),
            widget.Spacer(
              length=5,
              background=transparent,
            ),
            widget.TextBox(
              decorations=[RectDecoration(colour=color[0], radius=[7,0,0,7], filled=True)],
              text="",
              foreground=color[4],
            ),
            widget.KeyboardLayout(
              decorations=[RectDecoration(colour=color[4], radius=[0,7,7,0], filled=True)],
              configured_keyboards=['us intl', 'latam'],
              foreground=color[0],
            ),
            widget.Spacer(
              length=5,
              background=transparent,
            ),
            widget.UPowerWidget(
               border_charge_colour=color[3],
               border_colour=secondary_color[0],
               border_critical_colour='#cc0000',
               fill_critical='#cc0000',
               fill_low='#FF5511',
               fill_normal=color[3],
               foreground=color[3],
               decorations=[RectDecoration(colour=color[0],radius=7,filled=True)],
               percentage_critical=0.2,
               percentage_low=0.4,
               text_charging=' ({percentage:.0f}%) {ttf} to ',
               text_discharging=' ({percentage:.0f}%) {tte} Left',
            ),
            widget.Spacer(
              length=5,
              background=transparent,
            ),
            ## Lock, Logout, Poweroff
            widget.TextBox(
              decorations=[RectDecoration(colour=color[6], radius=7, filled=True)],
              foreground=color[0],
              text="",
              mouse_callbacks={'Button1': lambda: qtile.function(session_widget)},
              padding_x=5,
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
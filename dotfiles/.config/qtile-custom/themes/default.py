# By: gibranlp <thisdoesnotwork@gibranlp.dev>
# MIT licence

from turtle import width
from base import *

# Qtile Configuration

## Groups
g_names = ["Escape","1","2","3","4","5","6","7","8","9"]

#g_labels=["","","","","","","","","",""] ## Icons Original
g_labels=["零","一","二","三","四","五","六","七","八","九"] ## Kanji Numbers

g_layouts=["monadtall", "monadtall", "monadtall", "matrix","monadtall", "monadtall", "monadtall","monadtall", "monadtall", "monadtall"]
g_matches=[
  [Match(wm_class=[])],
  [Match(wm_class=[])],
  [Match(wm_class=[])],
  [Match(wm_class=[])],
  [Match(wm_class=[])],
  [Match(wm_class=[])],
  [Match(wm_class=[])],
  [Match(wm_class=[])],
  [Match(wm_class=[])],
  [Match(wm_class=[])],
 ]

for i in range(len(g_names)):
  groups.append(
    Group(
      name=g_names[i],
      matches=g_matches[i],
      layout=g_layouts[i].lower(),
      label=g_labels[i],
  ))

## Layouts
def init_layout_theme():
  return {"font":m_font,
    "fontsize":f_size,
    "margin":l_margin,
    "border_on_single":False,
    "border_width":l_border_w,
    "border_normal":color[0],
    "border_focus":color[2],
    "single_margin":sl_margin,
    "single_border_width":s_border_w,
    "change_ratio":0.05,
    "change_ratio":0.05,
    "new_client_position":'bottom',
    }

layout_theme = init_layout_theme()

def init_layouts():
  return [
    layout.MonadTall(max_ratio=0.90,ratio=0.75,**layout_theme),
    layout.MonadWide(max_ratio=0.90,ratio=0.75,**layout_theme),
    layout.MonadThreeCol(**layout_theme),
    layout.Stack(**layout_theme), 
    layout.Matrix(**layout_theme),
    ]
layouts = init_layouts()

# Theme

#### Widgets ####
def init_widgets_defaults():
    return dict(font=m_font,fontsize=f_size)

def init_widgets_top():
    widgets_top = [
      ## Groups
      widget.GroupBox(
        decorations=[RectDecoration(colour=color[0], radius=5, filled=True)],
        font=a_font,
        disable_drag=True,
        hide_unused=True,
        padding_x=3,
        borderwidth=0,
        active=color[1], #Program opened in that group
        inactive=color[8], # Empty Group
        rounded=False,
        highlight_method="text",
        this_current_screen_border=color[6],
        center_aligned = True,
        other_curren_screen_border=color[6],
        block_highlight_text_color=color[6],    
        urgent_border="ffcccc",
      ),
      widget.CurrentLayout(
        decorations=[RectDecoration(colour=color[3], radius=5, filled=True)],
        foreground=color[0],
      ),
      widget.Spacer(
        length=5,
        background='ffffff00',
      ),
      widget.TextBox(
        decorations=[RectDecoration(colour=color[0], radius=5, filled=True)],
        foreground=color[5],
        text="",
      ),
      widget.CPU(
        decorations=[RectDecoration(colour=color[5], radius=5, filled=True)],
        foreground=color[0],
        format='{load_percent}%'
      ),
      widget.Spacer(
        length=5,
        background='ffffff00',
      ),
      widget.TextBox(
        decorations=[RectDecoration(colour=color[0], radius=5, filled=True)],
        foreground=color[3],
        text="",
      ),
      widget.Memory(
        decorations=[RectDecoration(colour=color[3], radius=5, filled=True)],
        foreground=color[0],
        format='{MemUsed:.0f}{mm}',
        measure_mem='M',
      ),
      widget.Spacer(
        length=5,
        background='ffffff00',
      ),
      widget.TextBox(
        decorations=[RectDecoration(colour=color[0], radius=5, filled=True)],
        foreground=color[2],
        text="",
      ),
      widget.WindowName(
        decorations=[RectDecoration(colour=color[2], radius=5, filled=True)],
        foreground=color[0],
        width=250,
        format='{name}',
        scroll=True,
        scroll_delay=2,
        scroll_repeat=True,
        scroll_step=1,
      ),
      widget.Spacer(
        length=5,
        background='ffffff00',
      ),
      widget.Prompt(
        prompt=prompt,
        foreground=color[9],
        cursor_color=color[9],
        visual_bell_color=[9],
        visual_bell_time=0.2,
        decorations=[RectDecoration(colour=color[0], radius=5, filled=True)],
      ),
      widget.Spacer(
        length=bar.STRETCH,
        background='ffffff00',
      ),
      widget.Pomodoro(
        decorations=[RectDecoration(colour=color[2], radius=5, filled=True)],
        foreground=color[0],
        color_active=color[7],
        color_break='ffff00',
        color_inactive=color[0],
        length_long_break=30,
        length_pomodori=45,
        length_short_break=15,
        notification_on=True,
        num_pomodori=2,
        prefix_active=' ',
        prefix_inactive='',
        prefix_break=' Break!',
        prefix_long_break=' Long Break!',
        prefix_paused=' ',
        scroll=True,
        width=250,

      ),
      widget.Spacer(
        length=5,
        background='ffffff00',
      ),
      widget.TextBox(
        decorations=[RectDecoration(colour=color[0], radius=5, filled=True)],
        font=a_font,
        text="",
        foreground=color[6],
      ),
      ## Cmus
      widget.Mpris2(
        decorations=[RectDecoration(colour=color[6],radius=5, filled=True)],
        mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(term + " -e cava")},
        foreground=color[0],
        width=250,
        display_metadata=['xesam:artist', 'xesam:title'],
        paused_text='',
        stopped_text='',
        name='cmus',
        scroll=True,
        scroll_repeat=True,
      ),
      ## Vlc
      widget.Mpris2(
        decorations=[RectDecoration(colour=color[6],radius=5, filled=True)],
        mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(term + " -e cava")},
        foreground=color[0],
        width=250,
        paused_text='',
        stopped_text='',
        name='vlc',
        objname='org.mpris.MediaPlayer2.vlc',
        display_metadata=['xesam:artist', 'xesam:title'],
        scroll=True,
        scroll_repeat=True,
      ),
      ## Spotify
      widget.Mpris2(
        decorations=[RectDecoration(colour=color[6],radius=5, filled=True)],
        mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(term + " -e cava")},
        foreground=color[0],
        width=250,
        paused_text='',
        stopped_text='',
        name='spotify',
        objname='org.mpris.MediaPlayer2.spotify',
        display_metadata=['xesam:artist', 'xesam:title'],
        scroll=True,
        scroll_repeat=True,
      ),
      widget.Visualizer(
        hide=True,
        bar_colour=color[1],
        decorations=[RectDecoration(colour=color[0], radius=5, filled=True)],
      ),
      widget.Spacer(
        length=bar.STRETCH,
        background='ffffff00',
      ),
      widget.Systray(),
      widget.Spacer(
        length=5,
        background='ffffff00',
      ),
      widget.OpenWeather(
        font=a_font,
        decorations=[RectDecoration(colour=color[0], radius=5, filled=True)],
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
          foreground=color[2],
          metric=True,
          update_interval=600,
          
      ),
      widget.OpenWeather(
        app_key=w_appkey,
        cityid=w_cityid,
        foreground=color[0],
        format='{temp}°{units_temperature}',
        metric=True,
        update_interval=600,
        decorations=[RectDecoration(colour=color[2], radius=5, filled=True)],
      ),
      widget.Spacer(
        length=5,
        background='ffffff00',
      ),
      ## Network
      widget.WidgetBox(
        decorations=[RectDecoration(colour=color[0], radius=[5,0,0,5], filled=True)],
        text_closed=' ' + wifi_icon + ' ',
        text_open=' ',
        foreground=color[3],
        widgets=[
            widget.TextBox(
            background=color[0],
            text='  ',
            foreground=color[3],
            mouse_callbacks={'Button1':lambda: qtile.cmd_function(network_widget)}
          ),
          widget.Wlan(
            background=color[0],
            interface=wifi,
            format='{essid}',
            disconnected_message='',
            foreground=color[3],
            mouse_callbacks={'Button1':lambda: qtile.cmd_function(network_widget)}
          ),
          widget.TextBox(
            background=color[3],
            text=private_ip,
            foreground=color[0],
            mouse_callbacks={'Button1':lambda: qtile.cmd_function(network_widget)}
          ),
          widget.TextBox(
            background=color[0],
            text='  ',
            foreground=color[3],
            mouse_callbacks={'Button1':lambda: qtile.cmd_function(network_widget)}
          ),
          widget.TextBox(
            background=color[3],
            text=public_ip,
            foreground=color[0],
            mouse_callbacks={'Button1':lambda: qtile.cmd_function(network_widget)}
          ),
          widget.TextBox(
            background=color[0],
            text=wifi_icon,
            foreground=color[3],
            mouse_callbacks={'Button1':lambda: qtile.cmd_function(network_widget)}
          ),
          widget.Wlan(
            background=color[0],
            interface=wifi,
            format='{essid}',
            disconnected_message='',
            foreground=color[3],
            mouse_callbacks={'Button1':lambda: qtile.cmd_function(network_widget)}
          ),]
      ),
      widget.Wlan(
            background=color[0],
            interface=wifi,
            format='{percent:2.0%}',
            disconnected_message='',
            foreground=color[3],
            mouse_callbacks={'Button1':lambda: qtile.cmd_function(network_widget)}
          ),
      widget.Net(
        interface=wifi,
        format='{down}',
        foreground=color[0],
        use_bits=True,
        mouse_callbacks={'Button1':lambda: qtile.cmd_function(network_widget)},
        decorations=[RectDecoration(colour=color[3], radius=5, filled=True)],
      ),
      widget.Spacer(
        length=5,
        background='ffffff00',
      ),
      widget.TextBox(
        decorations=[RectDecoration(colour=color[0], radius=5, filled=True)],
        font=a_font,
        text="",
        foreground=color[4],
      ),
      widget.KeyboardLayout(
        decorations=[RectDecoration(colour=color[4], radius=5, filled=True)],
        configured_keyboards=['us intl', 'latam'],
        foreground=color[0],
      ),
      widget.Spacer(
        length=5,
        background='ffffff00',
      ),
      widget.TextBox(
        decorations=[RectDecoration(colour=color[0], radius=5, filled=True)],
        font=a_font,
        text="",
        foreground=color[5],
        mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('pavucontrol')}
      ),
      widget.ALSAWidget(
        decorations=[RectDecoration(colour=color[5], radius=5, filled=True)],
        device='Master',
        bar_colour_high=color[2],
        bar_colour_loud=color[2],
        bar_colour_normal=color[2],
        bar_colour_mute=color[1],
        hide_interval=3,
        update_interval=0.1,
        bar_width=60,
        mode='bar',
        foreground=color[0],
        text_format='{volume}%',
      ),
      widget.Spacer(
        length=5,
        background='ffffff00',
      ),
      widget.Clock(
        foreground=color[0],
        format="%a",
        update_interval=1,
        decorations=[RectDecoration(colour=color[3], radius=5, filled=True)],
      ),
      widget.Clock(
        foreground=color[3],
        format="%d",
        update_interval=1,
        decorations=[RectDecoration(colour=color[0], filled=True)],
      ),
      widget.Clock(
        foreground=color[0],
        format="%H:%M",
        update_interval=1,
        decorations=[RectDecoration(colour=color[3], radius=5, filled=True)],
      ),
      widget.Spacer(
        length=2,
        background='ffffff00',
      ),
      widget.UPowerWidget(
        border_charge_colour=color[7],
        border_colour=color[3],
        border_critical_colour='#cc0000',
        fill_critical='#cc0000',
        fill_low='#FF5511',
        fill_normal=color[3],
        foreground=color[3],
        decorations=[RectDecoration(colour=color[0], radius=5, filled=True)],
        percentage_critical=0.1,
        percentage_low=0.3,
        text_charging=' ({percentage:.0f}%) {ttf} to ',
        text_discharging=' ({percentage:.0f}%) {tte} Left',
      ),
      widget.Spacer(
        length=2,
        background='ffffff00',
      ),
      ## Lock, Logout, Poweroff
      widget.TextBox(
        decorations=[RectDecoration(colour=color[6], radius=5, filled=True)],
        font=a_font,
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
            bottom=bar.Bar(
                background="00000000",
                widgets=widgets_screen_top,  
                size=b_size,
                margin=[0,10,10,10]
                ),
            ),
        Screen(bottom=bar.Bar(
                background="00000000",
                widgets=widgets_screen_top,  
                size=b_size,
                margin=[0,5,5,5]
                ),
        ),
        ]

#### End Screens ####

widget_defaults = init_widgets_defaults()
widgets_top = init_widgets_top()
widgets_screen_top = init_widgets_screen_top()
screens = init_screens()

##########################################################################

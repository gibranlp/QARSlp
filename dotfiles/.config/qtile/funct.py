# _______  _______  ______  _______  __        
#|       ||   _   ||   __ \|     __||  |.-----.
#|   -  _||       ||      <|__     ||  ||  _  |
#|_______||___|___||___|__||_______||__||   __|
#                                       |__|   
# QARSlp Qtile + Arch Ricing Script
# By: gibranlp <thisdoesnotwork@gibranlp.dev>
# MIT licence
from variables import *

#### Hooks ####
@hook.subscribe.startup
def start():
    subprocess.call(home + '/.local/bin/alwaystart')
    
@hook.subscribe.startup_once
def start_once():
    subprocess.call(home + '/.local/bin/autostart')

@hook.subscribe.client_new
def floating(window):
    floating_types = ['notification', 'toolbar', 'splash', 'dialog','Nextcloud','Gcr-prompter','lxappearance','_NET_WM_WINDOW_TYPE_NORMAL']
    transient = window.window.get_wm_transient_for()
    if window.window.get_wm_type() in floating_types or transient:
        window.floating = True

#### Import Used Network Interface ####
def get_net_dev():
    get_dev = "ip addr show | awk '/inet.*brd/{print $NF; exit}'"
    ps = subprocess.Popen(get_dev,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    output = ps.communicate()[0].decode('ascii').strip()
    return(output)

wifi = get_net_dev()

if wifi.startswith('w'):
    wifi_icon='  '
else:
    wifi_icon='  '

#### Gety IP addreses Private / Public
def get_private_ip():
    ip = socket.gethostbyname(socket.gethostname())
    return ip

private_ip = get_private_ip()

def get_public_ip():
    try:
        raw = requests.get('https://api.duckduckgo.com/?q=ip&format=json')
        answer = raw.json()["Answer"].split()[4]
    except Exception as e:
        return "0.0.0.0"
    else:
        return answer
       
public_ip = get_public_ip()

if public_ip.startswith('0'):
    internet = "∅ No internet connection"

###### Import Battery for Laptops
def get_bat():
    get_bat = "ls /sys/class/power_supply | grep BAT"
    ps = subprocess.Popen(get_bat,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    output = ps.communicate()[0].decode('ascii').strip()
    return(output)

batt = get_bat()


##### Import Pywal Palette #####
with open(home + '/.cache/wal/colors.json') as wal_import:
    data = json.load(wal_import)
    wallpaper = data['wallpaper']
    alpha = data['alpha']
    colors = data['colors']
    val_colors = list(colors.values())
    def getList(val_colors):
        return [*val_colors]
    
def init_colors():
    return [*val_colors]

color = init_colors()

#### Send app to group ####
@lazy.function
def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)

@lazy.function
def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)

##### Specific Apps/Groups #####
def app_or_group(group, app):
    def f(qtile):
        if qtile.groups_map[group].windows:
            qtile.groups_map[group].cmd_toscreen(toggle=False)
            qtile.cmd_spawn(app)
        else:
            qtile.groups_map[group].cmd_toscreen(toggle=False)
            qtile.cmd_spawn(app)
    return f

#### Set Random Wallpaper ####
def set_rand_wallpaper(qtile):
    dir = home + '/Pictures/wallPapers'
    selection = random.choice(os.listdir(dir))
    rand_wallpaper = os.path.join(dir, selection)
    subprocess.run(["wpg", "-s" + rand_wallpaper])
    subprocess.run(["sudo", "cp", "%s" % rand_wallpaper,  "/usr/share/backgrounds/background.png"])
    subprocess.run(["wal", "-R"])
    qtile.cmd_reload_config()

#### Functions for Widgets ####
#### Display Shortcuts widget
def shortcuts(qtile):
    subprocess.run("cat ~/.shortcuts | rofi -theme '~/.config/rofi/shortcuts.rasi' -i -dmenu -p ' Shortcuts:'",shell=True)

#### Logout widget
def session_widget(qtile):
    options = [' Poweroff',' Log Out', ' Reboot',' Lock']
    index, key = rofi_session.select('  Session', options)
    if key == -1:
        rofi_session.close()
    else:
        if index == 0:
            os.system('systemctl poweroff')
        elif index == 1:
            qtile.cmd_shutdown()
        elif index == 2:
            os.system('systemctl reboot') 
        else:
            os.system('dm-tool switch-to-greeter')

#### Screenshot widget
def screenshot(qtile):
    options = [' Advanced',' Screen', ' Window', ' Area', ' 5s Screen']
    index, key = rofi_screenshot.select('  Screenshot', options)
    if key == -1:
        rofi.close()
    else:
        if index ==0:
            subprocess.run("deepin-screenshot -s" + home + "/Pictures",shell=True)
        if index ==1:
            subprocess.run("scrot -d 1 'Screenshot_%S-%m-%y.png' -e 'mv $f $$(xdg-user-dir PICTURES) #; viewnior $$(xdg-user-dir PICTURES)/$f' && dunstify ' Taken!'",shell=True)
        elif index==2:
            subprocess.run("scrot -u 'Screenshot_%S-%m-%y.png' -e 'mv $f $$(xdg-user-dir PICTURES) #; viewnior $$(xdg-user-dir PICTURES)/$f' && dunstify ' Taken!'",shell=True)
        elif index==3:
            subprocess.run("scrot -s 'Screenshot_%S-%m-%y.png' -e 'mv $f $$(xdg-user-dir PICTURES)  #; viewnior $$(xdg-user-dir PICTURES)/$f'&& dunstify ' Taken!'",shell=True)
        else:
            subprocess.run("scrot -d 5 -c 'Screenshot_%S-%m-%y.png' -e 'mv $f C #; viewnior $$(xdg-user-dir PICTURES)/$f' && dunstify ' Taken!'",shell=True)

#### Network Widget
def network_widget(qtile):
    get_ssid = "iwgetid -r"
    pos = subprocess.Popen(get_ssid,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    ssid = pos.communicate()[0].decode('ascii').strip()
    get_status = "nmcli radio wifi"
    ps = subprocess.Popen(get_status,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    status = ps.communicate()[0].decode('ascii').strip()
    if status == 'enabled':
        connected = ' Turn Wifi Off'
        active = "off"
    else:
        connected = ' Turn Wifi On'
        active= "on"
    options = [connected,' Bandwith Monitor (CLI)', ' Network Manager (CLI)']
    index, key = rofi_network.select(wifi_icon + internet, options)
    if key == -1:
        rofi_network.close()
    else:
        if index ==0:
            subprocess.run("nmcli radio wifi " + active, shell=True)
        elif index==1:
            qtile.cmd_spawn(term + ' -e bmon')
        else:
            qtile.cmd_spawn(term + ' -e nmtui')

                 

#### Change Theme widget ####
def change_theme(qtile):
    options = [theme[0],theme[1],theme[2],theme[3],theme[4],theme[5]]
    index, key = rofi_backend.select('  Color Scheme', options)
    if key == -1 or index >= 6:
        rofi_backend.close()
    elif key == 0 and index < 6:
        subprocess.run('\cp ~/.config/qtile/themes/%s/theme.py ~/.config/qtile/'% theme[index], shell=True)
        subprocess.run('\cp ~/.config/qtile/themes/%s/rofi/* ~/.config/rofi/' % theme[index],shell=True)
        qtile.cmd_reload_config()

#### Change Color scheme widget ####
def change_color_scheme(qtile):
    options = [backend[0],backend[1],backend[2],backend[3], '<<-<< Light Themes >>-->>', backend[0],backend[1],backend[2],backend[3]]
    index, key = rofi_backend.select('  Color Scheme', options)
    if key == -1 or index == 4:
        rofi_backend.close()
    elif key == 0 and index < 4:
        subprocess.run('wpg -s ' + wallpaper + ' --backend ' + backend[index].lower(), shell=True)
        qtile.cmd_reload_config()
    elif key == 0 and index > 4:
        subprocess.run('wpg -s ' + wallpaper + ' -L --backend ' + backend[index-5].lower(), shell=True)
        qtile.cmd_reload_config()

#### Multimedia #### 
def play_pause(qtile):
    qtile.cmd_spawn("playerctl -p spotify play-pause")
    qtile.cmd_spawn("playerctl -p ncspot play-pause")
    qtile.cmd_spawn("playerctl -p vlc play-pause")

def nexts(qtile):
    qtile.cmd_spawn("playerctl -p spotify next")
    qtile.cmd_spawn("playerctl -p ncspot next")
    qtile.cmd_spawn("playerctl -p vlc next")

def prev(qtile):
    qtile.cmd_spawn("playerctl -p spotify previous")
    qtile.cmd_spawn("playerctl -p ncspot previous")
    qtile.cmd_spawn("playerctl -p vlc previous")

def stop(qtile):
    qtile.cmd_spawn("playerctl -p spotify stop")
    qtile.cmd_spawn("playerctl -p ncspot stop")
    qtile.cmd_spawn("playerctl -p vlc stop")

def ncsp(qtile):
    qtile.groups_map["7"].cmd_toscreen(toggle=False)
    qtile.cmd_spawn(term + ' -e ncspot')

def ranger(qtile):
    qtile.groups_map["1"].cmd_toscreen(toggle=False)
    qtile.cmd_spawn(term + ' -e ranger')

#### Internet Search ####
def wsearx():
    run(home + '/.local/bin/wsearch')

#### Files/Folders Search ####
def cfilex():
    qtile.groups_map["1"].cmd_toscreen(toggle=False)
    qtile.cmd_spawn('thunar')

#### End Functions ####


##### Groups #####
group_names = ["1","2","3","4","5","6","7","8","9"]
group_labels=["","✉","","","","","","",""]
group_layouts=["monadtall", "monadtall", "matrix","monadtall", "monadtall", "monadtall","monadtall", "monadtall", "monadtall"]
group_matches=[[Match(wm_class=[''])],[Match(wm_class=[])],[Match(wm_class=[])],[Match(wm_class=[])],[Match(wm_class=[])],[Match(wm_class=[])],[Match(wm_class=[])],[Match(wm_class=['Steam', 'steam'])],[Match(wm_class=[])],]
groups = []

@hook.subscribe.client_new
def follow_window(client):
    for group in groups:
        match = next((m for m in group.matches if m.compare(client)), None)
        if match:
            targetgroup = qtile.groups_map[group.name]
            targetgroup.cmd_toscreen(toggle=False)
            break

@hook.subscribe.client_name_updated
def follow_window_name(client):
    for group in groups:
        match = next((m for m in group.matches if m.compare(client)), None)
        if match:
            targetgroup = qtile.groups_map[group.name]
            targetgroup.cmd_toscreen(toggle=False)
            break

for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            matches=group_matches[i],
            layout=group_layouts[i].lower(),
            label=group_labels[i],
        ))

#### End Groups ####


#### Layouts ####
def init_layout_theme():
    return {"font":main_font,
            "fontsize":lfontsz,
            "margin": lmargin,
            "border_width":lborderwd ,
            "border_normal":color[0],
            "border_focus":color[2],
            "single_margin":10,
            "single_border_width":3,
           }

layout_theme = init_layout_theme()

def init_layouts():
    return [
        layout.MonadTall(max_ratio=0.90,ratio=0.70,**layout_theme),
        layout.Matrix(**layout_theme),
        #layout.Bsp(**layout_theme),
        #layout.Columns(**layout_theme),
        layout.MonadThreeCol(**layout_theme),
        layout.Spiral(**layout_theme),
        #layout.RatioTile(**layout_theme),
        #layout.Slice(**layout_theme),
        #layout.Stack(**layout_theme),
        #layout.Tile(**layout_theme),
        #layout.VerticalTile(**layout_theme),
        #layout.Zoomy(**layout_theme),
        #layout.TreeTab(sections = ["Tabs"],section_fontsize=lfontsz,bg_color=color[0] + transparency,active_bg=color[8],active_fg=color[0],inactive_bg=color[0],inactive_fg=color[7],padding_left=0,padding_x=0,padding_y=5,section_top=10,section_bottom=20,level_shift=8,vspace=3,panel_width=250,**layout_theme),
        #layout.Floating(**layout_theme)            
        ]

floating_layout = layout.Floating(auto_float_rules=[
    Match(title='Confirmation'),  # tastyworks exit box
    Match(title='Qalculate!'),  # qalculate-gtk
    Match(wm_class='pinentry-gtk-2'),  # GPG key password entry
    Match(wm_class='confirmreset'),
    Match(wm_class='makebranch'),
    Match(wm_class='maketag'),
    Match(wm_class='branchdialog'),
    Match(wm_class='pinentry'),
    Match(wm_class='ssh-askpass'),
    Match(wm_class='Obconf')])
layouts = init_layouts()
#### End layouts ####

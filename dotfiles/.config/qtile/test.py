from functions import *

def select_wallpaper(qtile):
  index = rofi_wallpaper.select(' Select Wallpaper: ')
  if index == -1:
    rofi_left.close()
  else:
    subprocess.run(["wpg", light, "-s", wallpaper_dir + str(options[index]), "--backend", def_backend.lower()])
    subprocess.run(["cp", wallpaper_dir + str(options[index]), "/usr/local/backgrounds/background.png"])
    subprocess.run(["cp", "-r", str(Path.home() / ".local/share/themes/FlatColor"), "/usr/local/themes/"])
    qtile.reload_config()



 
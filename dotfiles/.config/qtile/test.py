from functions import *
## Select Wallpaper
def select_wallpaper(qtile):
  options = subprocess.check_output(["exa", wallpaper_dir]).decode("utf-8").splitlines()
  index, key = rofi_shortcuts.select(' Select Wallpaper: ', options)
  if key == -1 or index == 2:
    rofi_left.close()
  else:
    subprocess.run(["wpg", light, "-s", wallpaper_dir + str(options[index]), "--backend", def_backend.lower()])
    subprocess.run(["cp", wallpaper_dir + str(options[index]), "/usr/local/backgrounds/background.png"])
    subprocess.run(["cp", "-r", str(Path.home() / ".local/share/themes/FlatColor"), "/usr/local/themes/"])
    qtile.reload_config()


select_wallpaper(qtile)
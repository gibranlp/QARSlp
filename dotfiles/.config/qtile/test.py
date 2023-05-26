from theme import *

def dark_white(qtile):
  options = ['Dark', 'Light']
  index, key = rofi_backend.select('  Random Wallpaper & Theme', options)
  if key == -1 or index == 2:
    rofi_backend.close()
  else:
    if index == 0:
      variables[3]="-c" "\n"
    else:
      variables[3]="-L" "\n"

    with open(home + '/.config/qtile/variables', 'w') as file:
      file.writelines(variables)
    qtile.reload_config()
    
dark_white(qtile)
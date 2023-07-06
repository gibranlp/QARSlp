from functions import *
# Draw Widget
def draw_widget(qtile):
  options = [' Draw',' Clean', ' Exit']
  index, key = rofi_right.select('  Desktop Draw', options)
  if key == -1:
    rofi_right.close()
  else:
    if index ==0:
      subprocess.run("gromit-mpx -a",shell=True)
    elif index == 1:
      subprocess.run("gromit-mpx -a",shell=True)
    else:
      subprocess.run("gromit-mpx -q",shell=True)

draw_widget(qtile)
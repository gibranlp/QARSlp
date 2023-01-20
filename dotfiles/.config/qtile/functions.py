
# _______  _______  ______  _______  __        
#|       ||   _   ||   __ \|     __||  |.-----.
#|   -  _||       ||      <|__     ||  ||  _  |
#|_______||___|___||___|__||_______||__||   __|
#                                       |__|   
# QARSlp Qtile + Arch Ricing System
# By: gibranlp <thisdoesnotwork@gibranlp.dev>
# MIT licence 
#

## Multimedia
def play_pause(qtile):
  qtile.spawn("playerctl -p spotify play-pause")
  qtile.spawn("playerctl -p ncspot play-pause")
  qtile.spawn("playerctl -p vlc play-pause")
  qtile.spawn("playerctl -p cmus play-pause")

def nexts(qtile):
  qtile.spawn("playerctl -p spotify next")
  qtile.spawn("playerctl -p ncspot next")
  qtile.spawn("playerctl -p vlc next")
  qtile.spawn("playerctl -p cmus next")

def prev(qtile):
  qtile.spawn("playerctl -p spotify previous")
  qtile.spawn("playerctl -p ncspot previous")
  qtile.spawn("playerctl -p vlc previous")
  qtile.spawn("playerctl -p cmus previous")
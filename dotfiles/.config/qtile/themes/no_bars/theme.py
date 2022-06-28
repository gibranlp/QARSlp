

# _______  _______  ______  _______  __        
#|       ||   _   ||   __ \|     __||  |.-----.
#|   -  _||       ||      <|__     ||  ||  _  |
#|_______||___|___||___|__||_______||__||   __|
#                                       |__|   
# QARSlp Qtile + Arch Ricing Script
# By: gibranlp <thisdoesnotwork@gibranlp.dev>
# MIT licence 
from numpy import size
from funct import *

##### Screens #####

def init_screens():
    return [
        Screen(
            top=bar.Bar(
                background=[color[0] + transparency],  
                size=1,
                border_color=color[1]+ transparency,
                border_width=bar_top_width,
                opacity=bar_opa,
                ),
            bottom=bar.Bar(
                size=1,
                border_color=color[1]+ transparency,
                border_width=bar_bot_width,
                opacity=bar_opa,
                background=[color[0] + transparency]
                )
        ),
        Screen()
        ]

#### End Screens ####

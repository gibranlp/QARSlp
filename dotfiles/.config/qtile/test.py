from functions import *

def i3lock_colors(qtile):
  subprocess.run(['i3lock', 
    '--insidever-color={}'.format(secondary_color[5])+"22",
    '--ringver-color={}'.format(color[2]),
    '--insidewrong-color={}'.format(color[6]),
    '--ringwrong-color={}'.format(color[3]),
    '--inside-color={}'.format(secondary_color[5])+"22",
    '--ring-color={}'.format(secondary_color[5])+"22",        
    '--line-color={}'.format(color[2]),          
    '--separator-color={}'.format(color[4]),   
    '--verif-color={}'.format(color[7]),          
    '--wrong-color=#880000bb',          
    '--time-color={}'.format(color[2]),           
    '--date-color={}'.format(color[3]),           
    '--layout-color={}'.format(color[0]),         
    '--keyhl-color={}'.format(color[1]),         
    '--bshl-color={}'.format(color[3]),               
    '--clock',
    '--blur', '10',                 
    '--indicator',       
    '--time-str="%H:%M:%S"',   
    '--date-str="%A, %Y-%m-%d"',
    ])
i3lock_colors(qtile)
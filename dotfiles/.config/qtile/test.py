from functions import *
def i3lock_colors(qtile):
  subprocess.run(['i3lock', 
    '--ring-color={}'.format(secondary_color[0])+"DD",
    '--inside-color={}'.format(secondary_color[0])+"DD",
    '--line-color={}'.format(color[2]),
    '--separator-color={}'.format(color[4]),
    '--time-color={}'.format(color[2]),           
    '--date-color={}'.format(color[4]),
    '--insidever-color={}'.format(secondary_color[0])+"DD",
    '--ringver-color={}'.format(secondary_color[0])+"DD",
    '--verif-color={}'.format(color[5]),          
    '--verif-text=Checking',
    '--insidewrong-color={}'.format(secondary_color[0])+"DD",
    '--ringwrong-color={}'.format(secondary_color[0])+"DD",
    '--wrong-color={}'.format(color[1]),
    '--wrong-text=Wrong!',
    '--keyhl-color={}'.format(color[1]),         
    '--bshl-color={}'.format(color[6]),            
    '--clock',
    '--blur',    
    '--indicator',       
    '--time-str="%H:%M:%S"',   
    '--date-str="%A, %Y-%m-%d"',
    ])
  
i3lock_colors(qtile)

 
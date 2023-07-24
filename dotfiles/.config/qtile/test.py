from functions import *

## Show / Hide all Groups
def show_groups2(qtile):
   if hide_unused_groups == True:
      variables[7]=" " + "\n"
   else:
      variables[7]="True" + "\n"
      
   with open(home + '/.config/qtile/variables', 'w') as file:
      file.writelines(variables)
   
   

show_groups2(qtile)
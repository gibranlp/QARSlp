
from functions import *
 

#change_themes(qtile)
new_theme="slash" + ".py"
#subprocess.run(['cp', themes_dir, "/", new_theme, " ", theme_dest ])
print(['cp', themes_dir, "/", new_theme, " ", theme_dest ])

subprocess.run(['cp', themes_dir + "/" + new_theme, home + '/.config/qtile/theme.py'])
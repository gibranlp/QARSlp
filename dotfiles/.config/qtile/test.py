from theme import *
from pathlib import Path
#!/usr/bin/env python3

# selectfile
# Use rofi to select file or folder until file is selected, then print it.

# Arguments
#   $1=directory to start, defaults to "." (specified in variable default_dir)

# Source directory with systems folders.
default_dir = "."
# Filter modes: normal, regex, glob, fuzzy, prefix
rofi_filter_mode = "regex"
# Prompt in rofi, defaults to scriptname.
prompt = os.path.basename(__file__)

# rofi command to run for each selection.
rofi = ["rofi", "-dmenu", "-p", prompt, "-lines", "15", "-matching", rofi_filter_mode, "-i"]

if len(os.sys.argv) > 1:
    dir_path = os.path.abspath(os.sys.argv[1])
else:
    dir_path = os.path.abspath(default_dir)

# selected will be set to empty string, if user cancels in rofi. This should
# start out with any value, as the until loop stops if its empty.
# ! Attention: Be careful with modifying these things, otherwise you could end
# up in an infinite loop.
selected = "x"
file_path = ""
while not os.path.isfile(file_path) and selected != "":
    # List all folders in the directory and add ".." as top entry.
    file_list = sorted(os.listdir(dir_path))
    file_list.insert(0, "..")
    file_list_str = "\n".join(file_list)
    process = subprocess.run(rofi, input=file_list_str.encode(), stdout=subprocess.PIPE, text=True)
    selected = process.stdout.decode().strip()

    if selected == "":
        file_path = ""
    elif selected == "..":
        # ".." will be translated to go up one folder level and run rofi again.
        dir_path = os.path.dirname(dir_path)
    else:
        file_path = os.path.join(dir_path, selected)
        dir_path = file_path

# Extract folder portion, if its a file. This is needed, because the dir
# variable is overwritten previously.
# if os.path.isfile(file_path):
#     dir_path = os.path.dirname(file_path)
# print(dir_path)

# Finally print the fullpath of selected file.
if file_path != "":
    print(file_path)

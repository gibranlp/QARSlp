from functions import *

subprocess.run(["notify-send", "$(", "pamixer", "--get-volume-human",")"])

function i_rofi(){
  mkdir -p ~/.config/rofi
  cp ~/dotfiles/rofi/* ~/.config/rofi/
  sudo mkdir -p /root/.config/rofi
  sudo cp ~/dotfiles/rofi/* /root/.config/rofi/
  sudo mkdir -p /root/.cache/wal
  sudo cp ~/.cache/wal/colors-rofi-dark.rasi /root/.cache/wal
}

i_rofi
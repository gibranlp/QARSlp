function i_scripts(){
  mkdir -p ~/.local/bin
  cp -r ~/dotfiles/scripts/* ~/.local/bin
  chmod +x ~/.local/bin/*
}

i_scripts
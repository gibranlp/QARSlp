function i_fonts(){
  mkdir -p  ~/.fonts
  cp ~/dotfiles/fonts/otf/* ~/.fonts
  cp ~/dotfiles/fonts/ttf/* ~/.fonts
  fc-cache -f -v
}

i_fonts
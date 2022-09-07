function i_zsh(){
    sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended
    git clone https://github.com/zsh-users/zsh-autosuggestions.git ~/.oh-my-zsh/plugins/zsh-autosuggestions
    git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ~/.oh-my-zsh/plugins/zsh-syntax-highlighting
}

function cp_files(){
  mkdir -p ~/.oh-my-zsh/themes
  cp ~/dotfiles/.oh-my-zsh/themes/passion.zsh-theme ~/.oh-my-zsh/themes/passion.zsh-theme
  cp ~/dotfiles/.zshrc ~/
  echo "Enter your password and change the shell to /bin/zsh"
  chsh
}

i_zsh
cp_files
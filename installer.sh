# _______  _______  ______  _______  __        
#|       ||   _   ||   __ \|     __||  |.-----.
#|   -  _||       ||      <|__     ||  ||  _  |
#|_______||___|___||___|__||_______||__||   __|
#                                       |__|   
# SpectrumOS - Embrace the Chromatic Symphony!
# By: gibranlp <thisdoesnotwork@gibranlp.dev>
# MIT licence

# Variables

VER="v1.0.1"
BASE_PACKAGE_FILE="base_packages.txt"
PIP_PACKAGES="pip.txt"
AUR_PACKAGE_FILE="aur_packages.txt"

# Check screen size
screen_size=$(stty size 2>/dev/null || echo 24 80)
rows=$(echo $screen_size | awk '{print $1}')
columns=$(echo $screen_size | awk '{print $2}')

# Dialog Screen
r=$(( rows / 2 ))
c=$(( columns / 2 ))

# Check root
echo "::: Checking for sudo ..."
if [[ $EUID -eq 0 ]];then
    echo "::: Passed, Continuing..."
else
    if [[ $(pacman -Qi sudo) ]];then
        echo ":::sudo is installed, please run this script as root."
    else
        echo "::: sudo package was not fund, please install Sudo"
        exit 1
    fi
fi

# Check for AUR helper installed
AUR_MANAGERS=("yay" "aurman" "pikaur" "paru")
AUR_MANAGER=""
echo "::: Cheking for AUR manger"
for MANAGER in "${AUR_MANAGERS[@]}"; do
    if command -v "$MANAGER" >/dev/null 2>&1; then
        AUR_MANAGER="$MANAGER"
        break
    fi
done

# Print the detected AUR package manager
if [[ -n "$AUR_MANAGER" ]]; then
    echo "::: AUR Manager Found!: $AUR_MANAGER Continuing..."
else
    echo "::: No AUR Manager found, please install one (yay, aurman, pikaur, paru)"
    exit 1
fi

installMenu(){
  CHOICE=$(whiptail --menu "QARSlp Installation" ${r} ${c} 5 \
  "Install Base Packages" " " \
  "Install Pip Packages" " " \
  "Install AUR Packages" " " \
  "Copy all Dotfiles" " " \
  "Post Installation" " " 3>&1 1>&2 2>&3)

  for CHOICE in $CHOICES; do
    case "$CHOICE" in
    "1")
      baseInstall >&2
      ;;
    "2")
      echo "Option 2 was selected"
      ;;
    "3")
      echo "Option 3 was selected"
      ;;
    "4")
      echo "Option 4 was selected"
      ;;
    *)
      echo "Unsupported item $CHOICE!" >&2
      exit 1
      ;;
    esac
  done

}


welcomeDialogs() {
    # Welcome message
    whiptail --msgbox --backtitle "QARSlp Installer $VER" --title "Installing QARSlp" "This script will install QARSlp into your PC. \n \n 
    This script will work only on Arch Linux or Arch Linux based distributions. \n \n

    If you are running something else,you can try finding the packages in your distro to make it work.\n \n

    If you need help you can contact me through an issue in Github or at thisdoesnotwork@gibranlp.dev
    \n \n
    Please click OK to continue." ${r} ${c}
}

# Install Packages
## Base Packages
installBasePackages() {
  while read -r package; do
    sudo pacman -S --noconfirm "$package"

    echo "::: "
    echo "Installing $package..."
    sleep 1
  done < "$BASE_PACKAGE_FILE"

  echo "::: "
  echo "Installation complete!"
  sleep 1
}

baseInstall() {
    whiptail --msgbox --backtitle "QARSlp Installer $VER" --title "Base Packages Install" "The base packages needed for QARSlp to work will be installed now \n \n Click OK to Continue" ${r} ${c}
    
    whiptail --title "Package Installation" --gauge "Installing ..." 6 50 0 < <(installBasePackages) 2>&1
}

## Pip Packages
installPipPackages() {
  TOTAL_PACKAGES=$(wc -l < "$PIP_PACKAGES")
  count=0
  
  while read -r PACKAGE; do
    ((count++))

    pip install -r pip.txt --break-system-packages

    PERCENTAGE=$((count * 100 / TOTAL_PACKAGE))

    echo "::: "
    echo "Installing $PACKAGE..."
    echo "$PERCENTAGE"
    sleep 1
  done < "$PIP_PACKAGES"

  echo "::: "
  echo "Installation complete!"
  sleep 1
}

pipInstall() {
    whiptail --msgbox --backtitle "QARSlp Installer $VER" --title "Pip Packages Install" "The pip packages needed for QARSlp to work will be installed now \n \n Click OK to Continue" ${r} ${c}
    
    whiptail --title "Pip Packages Installation" --gauge "Installing ..." 6 50 0 < <(installPipPackages) 2>&1
}

## AUR Packages
installAURPackages() {
  while read -r package; do
    $AUR_MANAGER -S --noconfirm "$package"

    echo "::: "
    echo "Installing $package..."
    sleep 1
  done < "$AUR_PACKAGE_FILE"

  echo "::: "
  echo "Installation complete!"
  sleep 1
}

AURInstall() {
    whiptail --msgbox --backtitle "QARSlp Installer $VER" --title "AUR Packages Install" "The AUR packages needed for QARSlp to work will be installed now \n \n Click OK to Continue" ${r} ${c}
    
    whiptail --title "Package Installation" --gauge "Installing ..." 6 50 0 < <(installAURPackages) 2>&1
}

## Post Install
postInstall(){
  whiptail --title "File Selection" --checklist "Select files to copy:" 15 60 5 "${file_list[@]}" 3>&1 1>&2 2>&3
}

installMenu
#welcomeDialogs
#pipInstall
#baseInstall
#AURInstall
#postInstall

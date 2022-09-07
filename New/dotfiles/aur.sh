function i_aur () {
  packets=(
    'p7zip'
    'unrar'
    'thunderbird-bin'
    'openssh'
    'farge'
    'nbfc'
    #'visual-studio-code-bin'
    'picom-ibhagwan-git'
    'google-chrome'
    #'slack-desktop'
    'hugo'
    #'whatsdesk-bin'
    'telegram-desktop'
    'python-pywalfox'

)
for packet in "${packets[@]}"; do
    echo "Instalando --> ${packet}"
    paru -S "${packet}" --noconfirm
done
}
i_aur
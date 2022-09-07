function i_pip(){
  pip_packets=(
    'fontawesome'
    'ipc'
    'colorz'
    'colorthief'
    'haishoku'
    'dbus-next'
    'git+http://github.com/bcbnz/python-rofi.git'
   
  )

  for pip_packet in "${pip_packets[@]}"; do
    echo "Instalando --> ${pip_packet}"
    pip install "${pip_packet}"
  done
}

i_pip
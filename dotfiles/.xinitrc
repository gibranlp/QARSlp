exec qtile-session
default_user        gibranlp

case "$1" in
     qtile) exec qtile-session ;;
     
     *) exec $DEFAULTSESSION ;;
esac
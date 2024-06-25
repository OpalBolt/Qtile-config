dbus-update-activation-environment --systemd WAYLAND_DISPLAY XDG_CURRENT_DESKTOP=wlroots &
systemctl --user import-environment DISPLAY &
systemctl --user restart pipewire wireplumber.service xdg-desktop-portal xdg-desktop-portal-wlr &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
swayidle -w timeout 600 'swaylock' &
dunst --conf "~/.config/dunst/dunstrc"

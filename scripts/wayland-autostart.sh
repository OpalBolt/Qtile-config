#!/bin/bash

dbus-update-activation-environment --systemd \
	WAYLAND_DISPLAY XDG_CURRENT_DESKTOP="$XDG_CURRENT_DESKTOP"

# Authentication dialog

pkill -f /usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &

pkill -u "${USER}" -x pipewire\|wireplumber 1>/dev/null 2>&1 &
dbus-run-session pipewire &>/dev/null &

# Start xdg-desktop-portal-wlr

pkill -f /usr/libexec/xdg-desktop-portal-wlr &
systemctl --user start xdg-desktop-portal-wlr &

pkill -f dunst &
dunst &

# swayidle \
# 	timeout 5 'qtile cmd-obj -o core -f hide_cursor' resume 'qtile cmd-obj -o core -f unhide_cursor' \
# 	timeout 300 'swaylock'
#	timeout 600 'wlopm --off \*' resume 'wlopm --on \*' &

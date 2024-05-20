#                       ,,    ,,                                                 ,...,,
#   .g8""8q.     mm     db  `7MM                .g8"""bgd                      .d' ""db
# .dP'    `YM.   MM           MM              .dP'     `M                      dM`
# dM'      `MM mmMMmm `7MM    MM  .gP"Ya      dM'       ` ,pW"Wq.`7MMpMMMb.   mMMmm`7MM  .P"Ybmmm
# MM        MM   MM     MM    MM ,M'   Yb     MM         6W'   `Wb MM    MM    MM    MM :MI  I8
# MM.      ,MP   MM     MM    MM 8M""""""     MM.        8M     M8 MM    MM    MM    MM  WmmmP"
# `Mb.    ,dP'   MM     MM    MM YM.    ,     `Mb.     ,'YA.   ,A9 MM    MM    MM    MM 8M
#   `"bmmd"'     `Mbmo.JMML..JMML.`Mbmmd'       `"bmmmd'  `Ybmd9'.JMML  JMML..JMML..JMML.YMMMMMb
#       MMb                                                                             6'     dP
#        `bood'                                                                         Ybmmmd'

# --------------------
# Imports
# --------------------

import os
from vars import *
from modules.initkeys import keys, wl_input_rules
from modules.initscreens import screens
from modules.initlayout import layouts, floating_layout
from libqtile import bar, widget
from libqtile.config import Click, Drag, Screen
from libqtile.lazy import lazy
from pathlib import Path

# from libqtile.backend.wayland import InputConfig

# --------------------
# Auto fetching variables
# --------------------
home = str(Path.home())  # Fetches the home location
platform = int(
    os.popen("cat /sys/class/dmi/id/chassis_type").read()
)  # Finds the type of system that is running

# Load colors from initcolors.py
# Currently only the following colors schemes has been created
# for this configuration
# kanagawa


# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

#                       ,,    ,,                                    ,,        ,,
#   .g8""8q.     mm     db  `7MM              `7MMF'     A     `7MF'db      `7MM                    mm
# .dP'    `YM.   MM           MM                `MA     ,MA     ,V            MM                    MM
# dM'      `MM mmMMmm `7MM    MM  .gP"Ya         VM:   ,VVM:   ,V `7MM   ,M""bMM  .P"Ybmmm .gP"Ya mmMMmm
# MM        MM   MM     MM    MM ,M'   Yb         MM.  M' MM.  M'   MM ,AP    MM :MI  I8  ,M'   Yb  MM
# MM.      ,MP   MM     MM    MM 8M""""""         `MM A'  `MM A'    MM 8MI    MM  WmmmP"  8M""""""  MM
# `Mb.    ,dP'   MM     MM    MM YM.    ,          :MM;    :MM;     MM `Mb    MM 8M       YM.    ,  MM
#   `"bmmd"'     `Mbmo.JMML..JMML.`Mbmmd'           VF      VF    .JMML.`Wbmd"MML.YMMMMMb  `Mbmmd'  `Mbmo
#       MMb                                                                      6'     dP
#        `bood'                                                                  Ybmmmd'

from sys import path
from qtile_extras.widget.decorations import RectDecoration
from libqtile.lazy import lazy
from libqtile.widget import TextBox
from qtile_extras import widget

path.append("..")
from vars import font
from modules.initcolors import colors


widget_defaults = dict(
    font=font,
    fontsize=15,
    foreground=colors["highlight"],
    # padding=3,
)

dark_widgets = {
    "decorations": [
        RectDecoration(
            colour=colors["darkBackground"],
            filled=True,
            radius=10,
            padding_y=4,
            group=True,
        )
    ]
}

light_widgets = {
    "decorations": [
        RectDecoration(
            colour=colors["widgetLight"],
            filled=True,
            radius=10,
            padding_y=4,
            group=True,
        )
    ]
}

mid_widgets = {
    "decorations": [
        RectDecoration(
            foreground=colors["highlight"],
            # colour=colors["lighterBackground"],
            colour=colors["darkBackground"],
            filled=True,
            radius=10,
            padding_y=4,
            group=True,
        )
    ]
}


def w_update_box():
    return


def load_widgets():
    widgets_list = [
        widget.Sep(linewidth=0, padding=10, **mid_widgets),
        widget.CurrentLayoutIcon(scale=0.50, **widget_defaults, **mid_widgets),
        widget.CurrentLayout(**widget_defaults, **mid_widgets),
        widget.Sep(linewidth=0, padding=10, **mid_widgets),
        widget.Sep(linewidth=0, padding=10),
        widget.Sep(linewidth=0, padding=10, **mid_widgets),
        widget.TextBox(
            text="󱑤",
            **mid_widgets,
            **widget_defaults,
        ),
        widget.CheckUpdates(
            distro="Arch_checkupdates",
            display_format="{updates}",
            initial_text="0",
            no_update_string="0",
            **widget_defaults,
            **mid_widgets,
        ),
        widget.Sep(linewidth=0, padding=10, **mid_widgets),
        widget.Sep(linewidth=0, padding=10),
        widget.Sep(linewidth=0, padding=10, **mid_widgets),
        widget.TextBox(
            text="",
            **mid_widgets,
            **widget_defaults,
        ),
        widget.Volume(
            get_volume_command="/home/wingej0/dotfiles/qtile/scripts/volume.sh",
            **mid_widgets,
            **widget_defaults,
        ),
        widget.Sep(
            foreground=colors["highlight"], padding=10, size_percent=60, **mid_widgets
        ),
        widget.TextBox(text="", **mid_widgets, **widget_defaults),
        widget.Battery(
            format="{percent:2.0%}",
            **widget_defaults,
            **mid_widgets,
        ),
        widget.Sep(linewidth=0, padding=10, **mid_widgets),
        widget.Spacer(),
        widget.Sep(linewidth=0, padding=10, **dark_widgets),
        widget.GroupBox(
            active=colors["highlight"],
            borderwidth=2,
            disable_drag=True,
            hide_unused=False,
            highlight_color=["#00000000", "#00000000"],
            highlight_method="line",
            inactive=colors["inactive"],
            this_current_screen_border=colors["active"],
            this_screen_border=colors["highlight"],
            other_current_screen_border=colors["screencontrast"],
            other_screen_border=colors["screencontrast"],
            urgent_method="line",
            use_mouse_wheel=False,
            **dark_widgets,
            **widget_defaults,
        ),
        widget.Sep(linewidth=0, padding=10, **dark_widgets),
        widget.Spacer(),
        widget.Sep(linewidth=0, padding=10, **mid_widgets),
        widget.TextBox(
            text="",
            mouse_callbacks={
                "Button1": lazy.spawn("blueman-manager"),
            },
            **mid_widgets,
            **widget_defaults,
        ),
        widget.TextBox(
            text="",
            mouse_callbacks={
                "Button1": lazy.spawn("chromium --app=https://chatgpt.com/"),
            },
            **mid_widgets,
            **widget_defaults,
        ),
        widget.WiFiIcon(
            active_colour=colors["highlight"],
            interface="wlan0",
            padding_y=9,
            mouse_callbacks={
                "Button3": lazy.spawn("kitty -e nmtui"),
            },
            **widget_defaults,
            **mid_widgets,
        ),
        widget.TextBox(
            text="",
            mouse_callbacks={
                "Button1": lazy.spawn("nautilus"),
            },
            **widget_defaults,
            **mid_widgets,
        ),
        widget.Sep(linewidth=0, padding=10, **mid_widgets),
        widget.Sep(
            linewidth=0,
            padding=10,
        ),
        widget.Sep(linewidth=0, padding=10, **mid_widgets),
        widget.Clock(
            format=" %b %d | %H:%M ",
            mouse_callbacks={
                "Button1": lazy.spawn("wlogout"),
            },
            **widget_defaults,
            **mid_widgets,
        ),
        widget.Sep(linewidth=0, padding=10, **mid_widgets),
    ]
    return widgets_list

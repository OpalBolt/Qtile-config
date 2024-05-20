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
from libqtile import widget

path.append("..")
from vars import font
from modules.initcolors import colors


widget_defaults = dict(
    font=font,
    fontsize=12,
    padding=3,
)

dark_widgets = {
    "decorations": [
        RectDecoration(
            colour=colors["highlight"],
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
            colour=colors["highlight"], filled=True, radius=10, padding_y=4, group=True
        )
    ]
}


def load_widgets():
    widgets_list = [
        widget.CurrentLayout(**widget_defaults),
        widget.GroupBox(),
        widget.WindowName(),
        widget.KeyboardLayout(
            fmt="⌨  Kbd: {}",
        ),
        widget.Chord(
            chords_colors={
                "launch": ("#ff0000", "#ffffff"),
            },
            name_transform=lambda name: name.upper(),
        ),
        widget.TextBox("default config", name="default"),
        widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
        # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
        # widget.StatusNotifier(),
        widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
        widget.QuickExit(),
    ]

    return widgets_list

#                       ,,    ,,
#   .g8""8q.     mm     db  `7MM              `7MMF' `YMM'
# .dP'    `YM.   MM           MM                MM   .M'
# dM'      `MM mmMMmm `7MM    MM  .gP"Ya        MM .d"     .gP"Ya `7M'   `MF',pP"Ybd
# MM        MM   MM     MM    MM ,M'   Yb       MMMMM.    ,M'   Yb  VA   ,V  8I   `"
# MM.      ,MP   MM     MM    MM 8M""""""       MM  VMA   8M""""""   VA ,V   `YMMMa.
# `Mb.    ,dP'   MM     MM    MM YM.    ,       MM   `MM. YM.    ,    VVV    L.   I8
#   `"bmmd"'     `Mbmo.JMML..JMML.`Mbmmd'     .JMML.   MMb.`Mbmmd'    ,V     M9mmmP'
#       MMb                                                          ,V
#        `bood'                                                   OOb"

from sys import path
from libqtile.lazy import lazy
from libqtile.config import Key
from libqtile import qtile
from libqtile.backend.wayland.inputs import InputConfig

path.append("..")
from vars import mod, mod1, terminal, keyboard_Lang

from modules.initgroups import groups


keys = [
    # ------
    # Focus
    # ------
    # Keys used to switch focus between windows
    Key([mod], "Up", lazy.layout.up(), desc="Change focus to window above."),
    Key([mod], "Down", lazy.layout.down(), desc="Change focus to window below."),
    Key([mod], "Left", lazy.layout.left(), desc="Change focus to window on the left."),
    Key([mod], "Right", lazy.layout.right(), desc="Change focus to window the right."),
    Key([mod], "k", lazy.layout.up(), desc="Change focus to window above."),
    Key([mod], "j", lazy.layout.down(), desc="Change focus to window below."),
    Key([mod], "h", lazy.layout.left(), desc="Change focus to window on the left."),
    Key([mod], "l", lazy.layout.right(), desc="Change focus to window on the right."),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # ------
    # Move
    # ------
    # Key(
    #     [mod, "shift"],
    #     "h",
    #     lazy.layout.shuffle_left(),
    #     desc="Move window to the left",
    # ),
    # Key(
    #     [mod, "shift"],
    #     "l",
    #     lazy.layout.shuffle_right(),
    #     desc="Move window to the right",
    # ),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Shuffle window up."),
    Key(
        [mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Shuffle window down."
    ),
    Key([mod, "shift"], "Left", lazy.layout.swap_left(), desc="Shuffle window left."),
    Key(
        [mod, "shift"], "Right", lazy.layout.swap_right(), desc="Shuffle window right."
    ),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Shuffle window up."),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Shuffle window down."),
    Key([mod, "shift"], "h", lazy.layout.swap_left(), desc="Shuffle window left."),
    Key([mod, "shift"], "l", lazy.layout.swap_right(), desc="Shuffle window right."),
    #
    # ------
    # Size
    # ------
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key(
        [mod, "control"],
        "l",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        desc="Increase active window size.",
    ),
    Key(
        [mod, "control"],
        "Right",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        desc="Increase active window size.",
    ),
    Key(
        [mod, "control"],
        "h",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        desc="Decrease active window size.",
    ),
    Key(
        [mod, "control"],
        "Left",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        desc="Decrease active window size.",
    ),
    Key(
        [mod, "control"],
        "k",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        desc="Increase active window size.",
    ),
    Key(
        [mod, "control"],
        "Up",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        desc="Increase active window size.",
    ),
    Key(
        [mod, "control"],
        "j",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        desc="Decrease active window size.",
    ),
    Key(
        [mod, "control"],
        "Down",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        desc="Decrease active window size.",
    ),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key(
        [mod], "r", lazy.layout.reset(), desc="Reset the sizes of all window in group."
    ),
    # ------
    # Monitor change
    # ------
    Key([mod], "i", lazy.to_screen(0), desc="Keyboard focus to monitor 1"),
    Key([mod], "o", lazy.to_screen(1), desc="Keyboard focus to monitor 2"),
    Key([mod], "p", lazy.to_screen(2), desc="Keyboard focus to monitor 3"),
    Key([mod], "period", lazy.next_screen(), desc="Move focus to next monitor"),
    Key([mod], "comma", lazy.prev_screen(), desc="Move focus to prev monitor"),
    Key([mod1], "Tab", lazy.screen.next_group(), desc="Move to next group."),
    Key(
        [mod1, "shift"],
        "Tab",
        lazy.screen.prev_group(),
        desc="Move to previous group.",
    ),
    # ------
    # Layout mgmt
    # ------
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "q", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key(
        [mod, "shift"],
        "f",
        lazy.window.toggle_floating(),
        desc="Toggle floating on the focused window",
    ),
    # ------
    # Qtile management
    # ------
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    # ------
    # Launch apps
    # ------
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
]

# Add key bindings to switch VTs in Wayland.
# We can't check qtile.core.name in default config as it is loaded before qtile is started
# We therefore defer the check until the key binding is run by using .when(func=...)
for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )

for i in groups:
    keys.extend(
        [
            # mod1 + group number = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + group number = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                # lazy.window.togroup(i.name, switch_group=True),
                lazy.window.togroup(i.name),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + group number = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

keys.extend(
    [
        Key([mod, "mod1"], "Return", lazy.group["scratchpad"].dropdown_toggle("term")),
        Key(["mod1"], "v", lazy.group["scratchpad"].dropdown_toggle("volume")),
        Key(["mod1"], "b", lazy.group["scratchpad"].dropdown_toggle("bitwarden")),
    ]
)

keys.extend(
    [
        Key([mod], "d", lazy.spawn("rofi -show drun"), desc="Application launcher"),
        Key([mod], "b", lazy.spawn("firefox"), desc="Launch web browser"),
        Key([mod], "Escape", lazy.spawn("swaylock"), desc="Lock Screen"),
        Key(
            ["mod1"],
            "f",
            lazy.spawn("bash /home/mads/.config/qtile/scripts/screenshot.sh"),
            desc="Capture region",
        ),
        Key(
            [mod],
            "u",
            lazy.spawn("bash /home/mads/scripts/rofi-power-command.sh"),
            desc="Power menu",
        ),
        Key(
            [],
            "XF86AudioRaiseVolume",
            lazy.spawn("pactl -- set-sink-volume 0 +5%"),
            desc="Volume Up",
        ),
        Key(
            [],
            "XF86AudioLowerVolume",
            lazy.spawn("pactl -- set-sink-volume 0 -5%"),
            desc="Volume Down",
        ),
        Key(
            [],
            "XF86AudioMute",
            lazy.spawn("pactl set-sink-mute 0 toggle"),
            desc="Toggle Mute",
        ),
        Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause"), desc="Play/Pause"),
        Key([], "XF86AudioNext", lazy.spawn("playerctl next"), desc="Next Song"),
        Key(
            [], "XF86AudioPrev", lazy.spawn("playerctl previous"), desc="Previous Song"
        ),
        Key([], "XF86AudioStop", lazy.spawn("playerctl stop"), desc="Stop music"),
        Key(
            [],
            "XF86MonBrightnessUp",
            lazy.spawn("brightnessctl set 5%+"),
            desc="Increase brightness",
        ),
        Key(
            [],
            "XF86MonBrightnessDown",
            lazy.spawn("brightnessctl set 5%-"),
            desc="Decrease brightness",
        ),
    ]
)

wl_input_rules = {
    "type:keyboard": InputConfig(
        # kb_options="caps:swapescape,altwin:swap_alt_win",
        kb_layout=keyboard_Lang,
        # kb_repeat_rate=25,
        # kb_repeat_delay=600,
    ),
}

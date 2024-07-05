from libqtile.config import Group, ScratchPad, DropDown

# Create labels for groups and assign them a default layout.
groups = []

# group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "minus", "equal"]
group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

# group_labels = ["", "", "", "", "", "", "", "", "", "", "", ""]

group_layouts = [
    "monadtall",
    "monadtall",
    "monadtall",
    "monadtall",
    "monadtall",
    "monadtall",
    "monadtall",
    "monadtall",
    "monadtall",
    "monadtall",
    "monadtall",
    "monadtall",
    "monadtall",
    "monadtall",
]

# Add group names, labels, and default layouts to the groups object.
for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            layout=group_layouts[i].lower(),
            #            label=group_labels[i],
        )
    )


groups.append(
    ScratchPad(
        "scratchpad",
        [
            DropDown(
                "term",
                "kitty -e zellij",
                width=0.997,
                height=0.6,
                x=0,
                y=-0.03,
                opacity=1,
            ),
            DropDown(
                "volume",
                "pavucontrol",
                width=0.8,
                height=0.8,
                x=0.1,
                y=0.1,
                opacity=1,
            ),
            DropDown(
                "bitwarden", "bitwarden-desktop", width=0.4, height=0.6, x=0.3, y=0.1
            ),
        ],
    )
)

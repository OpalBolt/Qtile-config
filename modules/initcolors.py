#                       ,,    ,,                                   ,,
#   .g8""8q.     mm     db  `7MM                .g8"""bgd        `7MM
# .dP'    `YM.   MM           MM              .dP'     `M          MM
# dM'      `MM mmMMmm `7MM    MM  .gP"Ya      dM'       ` ,pW"Wq.  MM  ,pW"Wq.`7Mb,od8 ,pP"Ybd
# MM        MM   MM     MM    MM ,M'   Yb     MM         6W'   `Wb MM 6W'   `Wb MM' "' 8I   `"
# MM.      ,MP   MM     MM    MM 8M""""""     MM.        8M     M8 MM 8M     M8 MM     `YMMMa.
# `Mb.    ,dP'   MM     MM    MM YM.    ,     `Mb.     ,'YA.   ,A9 MM YA.   ,A9 MM     L.   I8
#   `"bmmd"'     `Mbmo.JMML..JMML.`Mbmmd'       `"bmmmd'  `Ybmd9'.JMML.`Ybmd9'.JMML.   M9mmmP'
#       MMb
#        `bood'

from sys import path
import tomllib
import os

path.append("..")
from vars import theme


# Ensure that all color schemes are loaded from file
def load_file():
    home = os.path.expanduser("~")
    with open(home + "/.config/qtile/colors.toml", mode="rb") as file:
        colorconfig = tomllib.load(file)
    file.close()
    return colorconfig


# Returns relevant colors based on the
inputcolors = load_file()
colors = {}
match theme:
    case "kanagawa":
        colors["highlight"] = inputcolors["kanagawa"]["carpYellow"]
        colors["darkerForground"] = inputcolors["kanagawa"]["sumiInk4"]
        colors["darkBackground"] = inputcolors["kanagawa"]["sumiInk0"]
        colors["widgetDefault"] = inputcolors["kanagawa"]["waveBlue1"]
        colors["widgetLight"] = inputcolors["kanagawa"]["waveBlue2"]

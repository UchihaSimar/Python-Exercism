COLOR_CODES = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9,
}

def value(colors):
    first_color, second_color, *rest = colors

    return 10*COLOR_CODES[first_color] + COLOR_CODES[second_color]

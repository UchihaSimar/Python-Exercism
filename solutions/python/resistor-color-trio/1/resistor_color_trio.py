# Color encoding lookup
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


def label(colors):
    """Translates 3 color bands into a formatted resistance label.

    :param colors: list[str] - three color names
    :return: str - formatted string representation with metric prefix (e.g., '33 kiloohms')
    """
    # 1. Decode main two-digit value
    main_value = COLOR_CODES[colors[0]] * 10 + COLOR_CODES[colors[1]]

    # 2. Add trailing zeros specified by the 3rd color band
    exponent = COLOR_CODES[colors[2]]
    total_ohms = main_value * (10**exponent)

    # 3. Scale with appropriate metric prefix
    if total_ohms >= 1_000_000_000:
        value = total_ohms // 1_000_000_000
        prefix = "giga"
    elif total_ohms >= 1_000_000:
        value = total_ohms // 1_000_000
        prefix = "mega"
    elif total_ohms >= 1_000:
        value = total_ohms // 1_000
        prefix = "kilo"
    else:
        value = total_ohms
        prefix = ""

    return f"{value} {prefix}ohms"
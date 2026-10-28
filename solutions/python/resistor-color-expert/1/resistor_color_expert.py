# Digit encoding lookup
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

# Tolerance lookup table
TOLERANCE_CODES = {
    "grey": "0.05%",
    "violet": "0.1%",
    "blue": "0.25%",
    "green": "0.5%",
    "brown": "1%",
    "red": "2%",
    "gold": "5%",
    "silver": "10%",
}


def resistor_label(colors):
    """Translates 1, 4, or 5 resistor color bands into a formatted resistance label.

    :param colors: list[str] - list of color names
    :return: str - formatted string representation with unit and tolerance (e.g., '33 kiloohms ±0.05%')
    """
    # 1. Handle 1-band resistor edge case
    if len(colors) == 1:
        return "0 ohms"

    # 2. Separate tolerance band (last color) from value bands
    tolerance = TOLERANCE_CODES[colors[-1]]
    value_bands = colors[:-1]

    # 3. Extract multiplier (the band immediately preceding tolerance)
    multiplier_exponent = COLOR_CODES[value_bands[-1]]
    digit_bands = value_bands[:-1]

    # 4. Construct the base numeric value from digit bands
    base_value = 0
    for color in digit_bands:
        base_value = base_value * 10 + COLOR_CODES[color]

    # 5. Calculate total resistance in ohms
    total_ohms = base_value * (10**multiplier_exponent)

    # 6. Apply metric prefix scaling
    if total_ohms >= 1_000_000_000:
        val = total_ohms / 1_000_000_000
        prefix = "giga"
    elif total_ohms >= 1_000_000:
        val = total_ohms / 1_000_000
        prefix = "mega"
    elif total_ohms >= 1_000:
        val = total_ohms / 1_000
        prefix = "kilo"
    else:
        val = total_ohms
        prefix = ""

    # Format float values cleanly (e.g., convert 33.0 -> 33, but 3.3 -> 3.3)
    val_str = f"{val:g}"

    return f"{val_str} {prefix}ohms ±{tolerance}"
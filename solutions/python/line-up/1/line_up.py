def line_up(name: str, number: int) -> str:
    # Check the last two digits for the 11, 12, 13 exceptions
    if 11 <= number % 100 <= 13:
        suffix = "th"
    else:
        # Check the last digit for 1, 2, or 3
        suffix = {1: "st", 2: "nd", 3: "rd"}.get(number % 10, "th")
        
    return f"{name}, you are the {number}{suffix} customer we serve today. Thank you!"

# --- Examples ---
print(line_up("Mary", 1))    # Mary, you are the 1st customer we serve today. Thank you!
print(line_up("John", 12))   # John, you are the 12th customer we serve today. Thank you!
print(line_up("Dahir", 162)) # Dahir, you are the 162nd customer we serve today. Thank you!

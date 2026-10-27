def is_valid(isbn):
    """Verify if a given string is a valid ISBN-10 number.

    :param isbn: str - candidate ISBN-10 string
    :return: bool - True if valid, False otherwise
    """
    # Remove hyphens
    clean_isbn = isbn.replace("-", "")

    # ISBN-10 must be exactly 10 characters long after removing hyphens
    if len(clean_isbn) != 10:
        return False

    total_sum = 0

    for i, char in enumerate(clean_isbn):
        # The check digit ('X' or a number) is only allowed at the final position (index 9)
        if char == "X" and i == 9:
            digit_val = 10
        elif char.isdigit():
            digit_val = int(char)
        else:
            # Contains invalid character or 'X' in non-final position
            return False

        # Weight decreases from 10 down to 1
        weight = 10 - i
        total_sum += digit_val * weight

    return total_sum % 11 == 0
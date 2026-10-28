def square_root(number):
    """Find square root of a number"""
    root_number = 0
    while (root_number+1)*(root_number+1) <= number:
        root_number += 1

    return root_number

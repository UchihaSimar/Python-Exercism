def is_valid_triangle(sides):
    """Helper function to validate triangle constraints."""
    a, b, c = sides
    # All sides must be greater than 0
    if a <= 0 or b <= 0 or c <= 0:
        return False
    # Triangle inequality: sum of any two sides must be >= the third side
    return (a + b >= c) and (b + c >= a) and (a + c >= b)

def equilateral(sides):
    if not is_valid_triangle(sides):
        return False
    a, b, c = sides
    return a == b == c

def isosceles(sides):
    if not is_valid_triangle(sides):
        return False
    a, b, c = sides
    return a == b or b == c or a == c

def scalene(sides):
    if not is_valid_triangle(sides):
        return False
    a, b, c = sides
    return a != b and b != c and a != c

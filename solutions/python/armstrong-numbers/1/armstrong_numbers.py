def is_armstrong_number(number):
    digits = []
    current_number = number
    while number >= 10:
        digit = number % 10
        number = number // 10
        digits.append(digit)
    digits.append(number)

    sum = 0
    for digit in digits:
        sum = sum + digit ** len(digits)

    return sum == current_number
def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")

    # 1 is a special case (has no proper divisors other than none < 1)
    if number == 1:
        return "deficient"

    # 1 is always a proper divisor for numbers > 1
    aliquot_sum = 1

    # Check potential divisors up to the square root of number
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            aliquot_sum += i
            # Add the paired divisor if it's distinct (e.g., for 12: 2 and 6)
            if i != number // i:
                aliquot_sum += number // i

    # Classify based on the aliquot sum comparison
    if aliquot_sum == number:
        return "perfect"
    elif aliquot_sum > number:
        return "abundant"
    else:
        return "deficient"
"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    Parameters:
        number (int): Total number of seat letters to be generated.

    Returns:
        generator: A generator that yields seat letters.

    Note:
        Seat letters are generated from A to D.
        After D the sequence starts again with A.
        For example: A, B, C, D, A, B

    """

    letters = ['A','B','C','D']
    for i in range(number):
        yield letters[i%4]


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    Parameters:
        number (int): The total number of seats to be generated.

    Returns:
        generator: A generator that yields seat numbers.

    Note:
        A seat number consists of the row number and the seat letter.
        There is no row 13, and each row has 4 seats.

        Seats should be sorted from low to high.
        For example: 3C, 3D, 4A, 4B

    """

    letters = ["A", "B", "C", "D"]
    count = 0
    row = 1
    
    while count < number:
        # Skip row 13 entirely
        if row == 13:
          row += 1
          continue
    
        for letter in letters:
          if count >= number:
            break
          yield f"{row}{letter}"
          count += 1
    
        row += 1


def assign_seats(passengers):
    """Assign seats to passengers.

    Parameters:
        passengers (list[str]): A list of strings containing names of passengers.

    Returns:
        dict: With passenger names as keys and seat numbers as values.
        Example output: {"Adele": "1A", "Björk": "1B"}

    """

    letters = ["A", "B", "C", "D"]
    count = 0
    row = 1
    assignment = {}
    while count < len(passengers):
        # Skip row 13 entirely
        if row == 13:
          row += 1
          continue
    
        for letter in letters:
          if count >= len(passengers):
            break
          assignment[passengers[count]] = f"{row}{letter}"
          count += 1
    
        row += 1

    return assignment


def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    Parameters:
        seat_numbers (list[str]): A list of seat numbers.
        flight_id (str): A string containing the flight identifier.

    Returns:
        generator: A generator that yields 12 character long ticket codes.

    """

    for seat_numbers_item in seat_numbers:
        ticket_id = seat_numbers_item+flight_id
        remaining_length = 12 - len(ticket_id)
        yield (ticket_id + '0'*remaining_length)

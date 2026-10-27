def is_isogram(string):
    """Determine if a word or phrase is an isogram.

    :param string: str - the word or phrase to evaluate.
    :return: bool - True if the string is an isogram, False otherwise.
    """
    seen_letters = set()
    
    for char in string.lower():
        if char.isalpha():
            if char in seen_letters:
                return False
            seen_letters.add(char)
            
    return True
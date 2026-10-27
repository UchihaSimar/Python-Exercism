def rotate(text, key):
    effective_key = key % 26
    result = []

    for character in text:
        if character.isalpha():
            # Determine base ASCII value ('A' = 65, 'a' = 97)
            start = ord('A') if character.isupper() else ord('a')
            # Shift character with wrap-around using modulo 26
            shifted = chr(start + (ord(character) - start + effective_key) % 26)
            result.append(shifted)
        else:
            result.append(character)

    return "".join(result)
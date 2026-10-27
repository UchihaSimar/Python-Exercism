import string 
def is_pangram(sentence):
    character_list = list(sentence.lower())
    alphabet_dict = dict.fromkeys(string.ascii_lowercase, 0)
    for character in character_list:
        if character in alphabet_dict:
            alphabet_dict[character] = alphabet_dict[character] + 1

    if any(value == 0 for value in alphabet_dict.values()):
        return False

    return True

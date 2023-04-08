# SUBFONCTIONS
import string


def polybe_encode(text):
    """Takes in argument a text (string)
    Returns the text encoded with Polybius square"""
    # TODO Polybe encode


def polybe_decode(text):
    """Takes in argument a text (string)
    Returns the text decoded by Polybius square"""
    # TODO Polybe decode


# FINAL FUNCTIONS
def rot13(text):
    """Takes in argument a text (string)
    Returns the text after applying the ROT13 encoding"""
    return cesar(text, 13)


def polybe(text, encrypt_mode):
    """Takes in argument a text (string) and an Encrypt Mode (1-2)
    Returns the encoded/decoded text"""
    # TODO Polybe


def cesar(text, key):
    """Takes in argument a text (string) a key (int)
    Returns the encoded/decoded text"""
    # LISTS
    uppercase = list(string.ascii_uppercase)
    lowercase = list(string.ascii_lowercase)
    numbers = list(string.digits)

    for i in range(len(text)):  # Parse all the characters
        char = text[i]
        if char in uppercase:
            new_index = uppercase.index(char) + key  # Get the index of the new letter (old one + key)
            while new_index > 25:  # Convert the number if it is out of bounds
                new_index -= 26
            text = text[:i] + uppercase[new_index] + text[i+1:]  # Replace the character of index i by a new one
        elif char in lowercase:
            new_index = lowercase.index(char) + key
            while new_index > 25:
                new_index -= 26
            text = text[:i] + lowercase[new_index] + text[i+1:]
        elif char in numbers:
            new_index = numbers.index(char) + key
            while new_index > 9:
                new_index -= 10
            text = text[:i] + numbers[new_index] + text[i+1:]
        # If the char isn't in a list (space, special caracter) it doesn't get replaced
    return text


def vigenere(encrypt_mode, text, key):
    """Takes in argument an encrypt mode (1-2), a text (string) and a key (string)
    Returns the encoded/decoded text"""
    # TODO Vigenere code


def encode(encrypt_mode, text, algorithm, key):
    """Takes in argument en Encrypt Mode (1-2), a text (string), an algorithm (1-4) and a key
    Returns True if the user want to continue using the programe, else False"""
    if algorithm == 1:  # If loop to check all the algorithms
        if encrypt_mode == 1:
            print(cesar(text, key))
        else:
            print(cesar(text, 26 - key))  # I do this cause decoding with a x key equals to encoding with a 26-x key
    elif algorithm == 2:
        print(vigenere(encrypt_mode, text, key))
    elif algorithm == 3:
        print(rot13(text))
    elif algorithm == 4:
        print(polybe(text, encrypt_mode))

    # TODO ask for user if he want to encode another file or if he want to end the program

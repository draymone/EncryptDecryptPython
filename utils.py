import string
import numpy


def convert_for_polybe_encode(text):
    """Takes in argument a text (string)
    Returns the text converted for being used in the polybe encoding"""
    text = text.upper()  # Make the text uppercase

    i = 0
    while i < len(text):  # Replace W by VV
        if text[i] == "W":
            text = text[:i] + "VV" + text[i + 1:len(text)]
        i += 1

    i = 0
    uppercases = list(string.ascii_uppercase)
    while i < len(text):  # Remove non numeric characters
        if not text[i] in uppercases:
            text = text[:i] + text[i + 1:len(text)]
            i -= 1
        i += 1

    return text


def convert_for_polybe_decode(text):
    """Takes in argument a text (string)
    Returns the text converted for being used in the polybe encoding"""

    i = 0
    digits = list(string.digits)
    while i < len(text):  # Remove non numeric characters
        if not text[i] in digits:
            text = text[:i] + text[i + 1:len(text)]
            i -= 1
        i += 1

    return text


def get_polybius_square():
    """Takes no argument
    Returns a 5x5 array containing the letters of the alphabet"""
    letters = list(string.ascii_uppercase)
    letters.remove("W")
    polybius_square = numpy.empty((5, 5), dtype=str).tolist()

    for i in range(5):
        sublist = []
        for j in range(5):
            sublist += letters[5 * i + j]
        polybius_square[i] = sublist

    return polybius_square


def get_polybe_encoded_char(char):
    """Takes an uppercase letter
    Returns this encoded letter with polybius' square"""
    if not (char in string.ascii_uppercase) or (char == "W"):  # Check if the character is acceptable
        return

    polybius_square = get_polybius_square()
    for i in range(5):
        if char in polybius_square[i]:
            return str(i + 1) + str(polybius_square[i].index(char) + 1)


def get_polybe_decoded_char(x, y):
    """Takes in argument the character coordinates (1-5)
    Returns the associated letter with polybius' square"""
    polybius_square = get_polybius_square()
    return polybius_square[x-1][y-1]


def polybe_encode(text):
    """Takes in argument a text (string)
    Returns the text encoded with Polybius square"""
    text = convert_for_polybe_encode(text)
    converted = ""
    for letter in text:
        converted += str(get_polybe_encoded_char(letter))
    return converted


def polybe_decode(text):
    """Takes in argument a text (string)
    Returns the text decoded by Polybius square"""
    text = convert_for_polybe_decode(text)
    if (len(text) % 2) == 1:
        return
    coordinates = []
    decoded_text = ""
    for i in range(int(len(text)/2)):
        temporary_coordinates = (int(text[2*i]), int(text[2*i+1]))
        coordinates += temporary_coordinates

    for j in range(int(len(coordinates)/2)):
        decoded_text += get_polybe_decoded_char(coordinates[2 * j], coordinates[2 * j + 1])

    return decoded_text


def vigenere_table():
    """Takes no argument
    Returns the Vigenere's table"""
    table = numpy.empty((26, 26), dtype=str).tolist()

    uppercase = list(string.ascii_uppercase)
    for i in range(len(table)):
        table[i] = uppercase[:]
        uppercase.append(uppercase[0])
        uppercase.pop(0)
    return table


def convert_key_for_vigenere(key, text):
    """Takes in argument a key and a text (ONLY CAPS)
    Returns the key repeated time enough to have the same lenght as the text and have letters where there are letters in
    the text
    TLDR: make the key compatible for use in vigenere code"""
    new_key = ""
    letters = list(string.ascii_uppercase)

    j = 0
    for i in range(len(text)):
        if text[i] in letters:
            new_key += key[j % len(key)]
            j += 1
        else:
            new_key += " "

    return new_key


def vigenere_encode(text, key):
    text = text.upper()
    key = convert_key_for_vigenere(key.upper(), text)
    letters = list(string.ascii_uppercase)
    table = vigenere_table()
    encoded_text = ""

    for i in range(len(text)):
        if text[i] in letters:
            txt_index = letters.index(text[i])
            key_index = letters.index(key[i])
            new_letter = table[key_index][txt_index]
            text = text[:i] + new_letter + text[i+1:]

    return text


def vigenere_decode(text, key):
    text = text.upper()
    key = convert_key_for_vigenere(key.upper(), text)
    letters = list(string.ascii_uppercase)
    table = vigenere_table()
    encoded_text = ""

    for i in range(len(text)):
        if text[i] in letters:
            key_index = letters.index(key[i])
            table_line = table[key_index]
            new_letter_index = table_line.index(text[i])
            new_letter = letters[new_letter_index]
            text = text[:i] + new_letter + text[i + 1:]

    return text

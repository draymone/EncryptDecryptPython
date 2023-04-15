import string


def polybe_encode(text):
    """Takes in argument a text (string)
    Returns the text encoded with Polybius square"""
    # TODO Polybe encode


def polybe_decode(text):
    """Takes in argument a text (string)
    Returns the text decoded by Polybius square"""
    # TODO Polybe decode


def get_polybius_square():
    """Takes no argument
    Returns a 5x5 array containing the letters of the alphabet"""
    letters = list(string.ascii_uppercase)
    letters.remove("W")
    polybius_square = [[], [], [], [], []]

    for i in range(5):
        sublist = []
        for j in range(5):
            sublist += letters[5*i + j]
        polybius_square[i] = sublist

    return polybius_square

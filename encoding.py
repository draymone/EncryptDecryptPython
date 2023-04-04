# SUBFONCTIONS
def polybe_encode(text):
    """Takes in argument a text (string)
    Returns the text encoded with Polybius square"""


def polybe_decode(text):
    """Takes in argument a text (string)
    Returns the text decoded by Polybius square"""


# FINAL FUNCTIONS
def rot13(text):
    """Takes in argument a text (string)
    Returns the text after applying the ROT13 encoding"""
    # TODO effectuer la conversion
    return text


def polybe(text, encrypt_mode):
    """Takes in argument a text (string) and an Encrypt Mode (1-2)
    Returns the encoded/decoded text"""


def cesar(text, key):
    """Takes in argument a text (string) a key (int)
    Returns the encoded/decoded text"""


def vigenere(encrypt_mode, text, key):
    """Takes in argument an encrypt mode (1-2), a text (string) and a key (string)
    Returns the encoded/decoded text"""


def encode(encrypt_mode, text, algorithm, key):
    """Takes in argument en Encrypt Mode (1-2), a text (string), an algorithm (1-4) and a key
    Returns True if the user want to continue using the programe, else False"""
    if algorithm == 1:  # If loop to check all the algorithms
        if encrypt_mode == 1:
            print(cesar(text, key))
        else:
            print(cesar(text, 26-key))  # I do this cause decoding with a x key equals to encoding with a 26-x key
    elif algorithm == 2:
        print(vigenere(encrypt_mode, text, key))
    elif algorithm == 3:
        print(rot13(text))
    elif algorithm == 4:
        print(polybe(text, encrypt_mode))

import encoding
import utils # TODO remove this line


def getCryptMode():
    """Will get the information about the encoding, this means the algorithm and if the user want to encrypt or
    decrypt"""
    # Declare the values that are correct
    mode_correct_values = ["1", "2"]
    algorithm_correct_values = ["1", "2", "3", "4"]

    # Get if the user wants to encode / decode
    mode = input("Souhaitez vous encoder (1) un message ou en déchiffer (2) un ?\nTapez 1 ou 2: ")
    while mode not in mode_correct_values:
        mode = input("Veuillez entrer 1 ou 2: ")
    mode = int(mode)

    # Get the asked crypt algorithm
    print("Quel cryptage souhaitez vous utiliser ?\n1) Code César\n2) Code de Vigenère\n3) ROT13\n4) Carré de Polybe")
    crypt_algorithm = input("Entrez un nombre entre 1 et 4: ")
    while crypt_algorithm not in algorithm_correct_values:
        crypt_algorithm = input("Entrez un nombre entre 1 et 4: ")
    crypt_algorithm = int(crypt_algorithm)

    # Return the values
    return crypt_algorithm, mode


def getTextToCrypt(crypt_mode):
    """Will get the information about the text, this means the text and the encoding key associated"""

    key = "a1"  # Initialize the key as a1 so the loops underneath will run at least once

    """ALTERNATIVE CODE
    I could make a while true, make a if condition that check if the text is numeric/alpha and break if the condition
    is valid"""
    if crypt_mode[0] == 1:  # César Code (only number)
        while not key.isnumeric():
            key = input("Veuillez entrer la clé de chiffrement (nombre): ")
        key = int(key)

    if crypt_mode[0] == 2:  # Vigenère Code (only letters)
        while not key.isalpha():
            key = input("Veuillez entrer la clé de chiffrement (lettres seulement): ")

    text = input("Veuillez entrer le texte à crypter/décrypter: ")

    return text, key


print(utils.get_polybe_encoded_char("A"))
running = True  # Initialize this value as True so the loop run at least one
print("Bienvenue sur Encrypt&Decrypt")

while running:
    cryptMode = getCryptMode()  # (Algorithme, Encrypt/Decrypt)
    textToCrypt = getTextToCrypt(cryptMode)  # (Texte, <Clé>)

    # Create a new tupple to respect the rule: Encrypt Mode, Text, Algorithm, Key
    running = encoding.encode(cryptMode[1], textToCrypt[0], cryptMode[0], textToCrypt[1])

def getCryptMode():
    mode_correct_values = ["1", "2"]
    algorithm_correct_values = ["1", "2", "3", "4"]

    print("Bienvenue sur Encrypt&Decrypt")
    mode = input("Souhaitez vous encoder (1) un message ou en déchiffer (2) un ?\nTapez 1 ou 2: ")
    while mode not in mode_correct_values:
        mode = input("Veuillez entrer 1 ou 2: ")
    mode = int(mode)

    print("Quel cryptage souhaitez vous utiliser ?\n1) Code César\n2) Code de Vigenère\n3) ROT13\n4) Carré de Polybe")
    crypt_algorithm = input("Entrez un nombre entre 1 et 4: ")
    while crypt_algorithm not in algorithm_correct_values:
        crypt_algorithm = input("Entrez un nombre entre 1 et 4: ")
    crypt_algorithm = int(crypt_algorithm)

    return crypt_algorithm, mode


def getTextToCrypt(crypt_mode):

    key = "a1"
    if crypt_mode[0] == 1:  # Code de césar (numérique)
        while not key.isnumeric():
            key = input("Veuillez entrer la clé de chiffrement (nombre): ")
        key = int(key)

    if crypt_mode[0] == 2:  # Code de vigenère (lettres)
        while not key.isalpha():
            key = input("Veuillez entrer la clé de chiffrement (lettres seulement): ")

    text = input("Veuillez entrer le texte à crypter/décrypter: ")

    return text, key


cryptMode = getCryptMode()  # (Algorithme, Encrypt/Decrypt)

textToCrypt = getTextToCrypt(cryptMode)  # (Texte, <Clé>)

# TODO call a function that will encrypt/decrypt the text

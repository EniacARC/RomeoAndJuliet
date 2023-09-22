"""
Author: Yonathan Chapal
Program name: RomeoAndJuliet
Description:
Date: 22/9/2023
"""

# Define Constants
ENCRYPTION_TABLE = {
    'A': 56, 'B': 57, 'C': 58, 'D': 59, 'E': 40, 'F': 41,
    'G': 42, 'H': 43, 'I': 44, 'J': 45, 'K': 46, 'L': 47,
    'M': 48, 'N': 49, 'O': 60, 'P': 61, 'Q': 62, 'R': 63,
    'S': 64, 'T': 65, 'U': 66, 'V': 67, 'W': 68, 'X': 69,
    'Y': 10, 'Z': 11, 'a': 12, 'b': 13, 'c': 14, 'd': 15,
    'e': 16, 'f': 17, 'g': 18, 'h': 19, 'i': 30, 'j': 31,
    'k': 32, 'l': 33, 'm': 34, 'n': 35, 'o': 36, 'p': 37,
    'q': 38, 'r': 39, 's': 90, 't': 91, 'u': 92, 'v': 93,
    'w': 94, 'x': 95, 'y': 96, 'z': 97, ' ': 98, ',': 99,
    '.': 100, ';': 101, '\'': 102, '?': 103, '!': 104,
    ':': 105
}


def encrypt_message(message):
    """encrypts a message according to the ENCRYPTION_TABLE constant

    :param message: the message the function encrypts
    :type message: str
    :return: a list containing the encrypted message
    :rtype: list of int
    """

    # create a list that substitutes each char to it's corresponding according to the ENCRYPTION_TABLE constant
    return list(map(lambda char_to_encrypt: ENCRYPTION_TABLE[char_to_encrypt], message))


def decrypt_message(message):
    """decrypts a message according to the ENCRYPTION_TABLE constant

    :param message: the message the function decrypts
    :type message: list of int
    :return: the decrypted message
    :rtype: str
    """
    # create separate lists for the keys and values of the encryption table
    key_list = list(ENCRYPTION_TABLE.keys())
    val_list = list(ENCRYPTION_TABLE.values())

    # the key location of each number according to the ENCRYPTION_TABLE constant and join it into a string
    return ''.join(map(lambda int_to_decrypt: key_list[val_list.index(int_to_decrypt)], message))


def main():
    print(decrypt_message(
        [59, 36, 35, 102, 91, 98, 94, 12, 90, 91, 16, 98, 96, 36, 92, 39, 98, 33, 36, 93, 16, 98, 36, 35, 98, 90, 36,
         34, 16, 13, 36, 15, 96, 99, 98, 94, 19, 36, 98, 15, 36, 16, 90, 35, 102, 91, 98, 93, 12, 33, 92, 16, 98, 30,
         91, 100]))


if __name__ == '__main__':
    main()

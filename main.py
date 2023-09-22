"""
Author: Yonathan Chapal
Program name: RomeoAndJuliet
Description:
Date: 22/9/2023
"""

import os
import logging

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

LOG_FORMAT = '%(levelname)s | %(asctime)s | %(processName)s | %(message)s'
LOG_LEVEL = logging.DEBUG
LOG_DIR = 'log'
LOG_FILE = LOG_DIR + '/logger.log'


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


def write_to_file(text, path):
    """writes a message to a txt file at the given path

    :param text: the message to write in the txt file
    :type text: str
    :param path: the path to the txt file
    :type path: str
    :return: None
    """
    try:
        # open file if exists, create file if not
        file = open(path, "w")

        # override the file contents with the text and close the file
        file.write(text)
        file.close()
    except OSError:
        print("An error has occurred while trying to write to file")


def read_from_file(path):
    """reads the txt file and returns its contents

    :param path: the path to the txt file
    "type path: str
    :return: the contents of the txt file
    :rtype: str
    """
    try:
        # opens and read the txt file contents
        file = open(path, "r")
        return file.read()
    except OSError:
        print("An error has occurred while trying to read file")


def main():
    print(read_from_file("demo-file.txt"))


if __name__ == '__main__':
    # make sure we have a logging directory and configure the logging
    if not os.path.isdir(LOG_DIR):
        os.makedirs(LOG_DIR)
    logging.basicConfig(format=LOG_FORMAT, filename=LOG_FILE, level=LOG_LEVEL)
    main()

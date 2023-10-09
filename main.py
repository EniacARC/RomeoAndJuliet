"""
Author: Yonathan Chapal
Program name: RomeoAndJuliet
Description: a program to encrypt and decrypt messages using an encryption table
Date: 22/9/2023
"""

import os
import sys
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
    :return: a string containing the encrypted message separated by commas
    :rtype: str
    """

    # create a list that substitutes each char to it's corresponding according to the ENCRYPTION_TABLE constant
    return ','.join((map(lambda char_to_encrypt: str(ENCRYPTION_TABLE[char_to_encrypt]), message)))


def decrypt_message(message):
    """decrypts a message according to the ENCRYPTION_TABLE constant

    :param message: the message the function decrypts
    :type message: string
    :return: the decrypted message
    :rtype: str
    """
    # create separate lists for the keys and values of the encryption table
    key_list = list(ENCRYPTION_TABLE.keys())
    val_list = list(ENCRYPTION_TABLE.values())

    # the key location of each number according to the ENCRYPTION_TABLE constant and join it into a string
    return ''.join(map(lambda int_to_decrypt: key_list[val_list.index(int(int_to_decrypt))], message.split(',')))


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
        logging.debug(f"program wrote to file at: {path}")
        file.close()
    except OSError:
        logging.error("An error has occurred while trying to read file")


def read_from_file(path):
    """reads the txt file and returns its contents

    :param path: the path to the txt file
    ":type path: str
    :return: the contents of the txt file
    :rtype: str
    """
    try:
        # opens and read the txt file contents
        file = open(path, "r")
        text = file.read()
        logging.debug(f"file at: {path} was read successfully")
        return text
    except OSError:
        print("An error has occurred while trying to read file")
        logging.error(f"An error has occurred while trying to read file at {path}")
        return -1


def validate_input(user_input):
    """validate that all the chars in the input are in the ENCRYPTION_TABLE.

    :param user_input: the user input string
    :return: if the user input is valid
    :rtype: bool
    """
    for c in user_input:
        if ENCRYPTION_TABLE.get(c) is None:
            return False
    return True


def main():
    if sys.argv[1] != "encrypt" and sys.argv[1] != "decrypt":
        logging.error(f"command line argument: '{sys.argv[1]}' isn't a valid argument")

    elif sys.argv[1] == "encrypt":
        valid = False
        message = ""

        # wait until user enters a valid input
        while not valid:
            message = input("Please enter message to encrypt: ")
            logging.debug(f"user entered: '{message}'")
            valid = validate_input(message)
            if not valid:
                print("error! please enter a valid message!")
                logging.warning("user input was invalid")

        write_to_file(encrypt_message(message), "encrypted_msg.txt")

    else:
        message = read_from_file("encrypted_msg.txt")
        if message != -1:
            if validate_input(message):
                message = decrypt_message(message)
                logging.info(f"message in file is: {message}")
                logging.info(f"decrypted successfully: {message}")
                print(f"the message is: {message}")
            else:
                print(f"input message was invalid!")
                logging.error(f"input message: '{message}' was invalid!")


if __name__ == '__main__':
    # make sure we have a logging directory and configure the logging
    if not os.path.isdir(LOG_DIR):
        os.makedirs(LOG_DIR)
    logging.basicConfig(format=LOG_FORMAT, filename=LOG_FILE, level=LOG_LEVEL)

    assert validate_input("fdyDRTtfudf")
    assert not validate_input("hello wor~ld")
    main()
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
KEY_LIST = list(ENCRYPTION_TABLE.keys())
VAL_LIST = list(ENCRYPTION_TABLE.values())

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
    if message == '':
        return ''
    # get the key location of each number according to the ENCRYPTION_TABLE constant and join it into a string
    return ''.join(map(lambda int_to_decrypt: KEY_LIST[VAL_LIST.index(int(int_to_decrypt))], message.split(',')))


def write_to_file(text, path):
    """writes a message to a txt file at the given path

    :param text: the message to write in the txt file
    :type text: str
    :param path: the path to the txt file
    :type path: str
    :return: None
    """
    # open file if exists, create file if not
    try:
        with open(path, "w") as file:
            # override the file contents with the text and close the file
            file.write(text)
            logging.debug(f"program wrote to file at: {path}")
    except OSError:
        logging.error(f"An error has occurred while trying to write to file at {path}")
        print("an error has occurred while trying to write to file")


def read_from_file(path):
    """reads the txt file and returns its contents

    :param path: the path to the txt file
    :type path: str
    :return: the contents of the txt file
    :rtype: str
    """

    try:
        with open(path, "r") as file:
            # opens and read the txt file contents
            text = file.read()
            logging.debug(f"file at: {path} was read successfully")
            return text
    except OSError:
        print("an error has occurred while trying to read file")
        logging.error(f"An error has occurred while trying to read file at {path}")
    return None


def validate(mode, program_input, expected_output):
    """make sure that the program decrypts and encrypts as expected

    :param mode: what mode of the program to check, encrypt or decrypt
    :type mode: str
    :param program_input: the input given to the program
    :type program_input: str
    :param expected_output: the expected output of the program given the input
    :type expected_output: str
    :return: if the program works as expected
    :rtype: bool
    """
    # checks all chars are in the table
    if mode == "encrypt":
        return expected_output == encrypt_message(program_input)
    elif mode == "decrypt":
        return expected_output == decrypt_message(program_input)
    return False


def main():
    if len(sys.argv) < 2:
        logging.error("No command line argument was provided!")
        print("Please provide a command line argument (encrypt, decrypt)")

    elif sys.argv[1].lower() != "encrypt" and sys.argv[1].lower() != "decrypt":
        logging.error(f"command line argument: '{sys.argv[1]}' isn't a valid argument")
        print("please provide a valid command line argument (encrypt, decrypt)")

    elif sys.argv[1] == "encrypt":
        # assume all characters entered are valid
        message = input("Please enter message to encrypt: ")
        write_to_file(encrypt_message(message), "encrypted_msg.txt")

    else:
        message = read_from_file("encrypted_msg.txt")
        if message is not None:
            logging.info(f"message in file is: {message}")
            message = decrypt_message(message)
            logging.info(f"decrypted successfully: {message}")
            print(f"the message is: {message}")


if __name__ == '__main__':
    # make sure we have a logging directory and configure the logging
    if not os.path.isdir(LOG_DIR):
        os.makedirs(LOG_DIR)
    logging.basicConfig(format=LOG_FORMAT, filename=LOG_FILE, level=LOG_LEVEL)

    program_in = ("My bounty is as boundless as the sea, My love as deep; "
                  "the more I give to thee, The more I have, for both are infinite.")
    expected_out = ("48,96,98,13,36,92,35,91,96,98,30,90,98,12,90,98,13,36,92,35,15,33,16,90,90,98,12,"
                    "90,98,91,19,16,98,90,16,12,99,98,48,96,98,33,36,93,16,98,12,90,98,15,16,16,37,101,"
                    "98,91,19,16,98,34,36,39,16,98,44,98,18,30,93,16,98,91,36,98,91,19,16,16,99,98,65,19,"
                    "16,98,34,36,39,16,98,44,98,19,12,93,16,99,98,17,36,39,98,13,36,91,19,98,12,39,16,98,30,"
                    "35,17,30,35,30,91,16,100")
    assert validate("encrypt", program_in, expected_out)
    assert validate("decrypt", expected_out, program_in)

    program_in = "Don't waste your love on somebody, who doesn't value it."
    assert not validate("encrypt", program_in, expected_out)
    assert not validate("decrypt", expected_out, program_in)
    main()

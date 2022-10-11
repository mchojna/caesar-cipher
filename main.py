"""
Title: Caesar Cipher
Author: Michał Chojna
Date: 08.06.2022
Description: Encode word given by user using Caesar Cipher or decode word given by user using Caesar Cipher
"""

# Imports modules
import art
import os
import math

# Creates a list of letters from alphabet
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


# Defines function
def caesar(plain_text, shift_amount, operation):
    """
    Function takes the word given by a user, takes the number by which each letter in the word is to be moved forward or backward, takes the type of operation to be applied on the word (decrypt or encrypt).
    Function returns encrypted or decrypted word
    """

    # Transforms given word to a list
    word = list(plain_text)

    # For loop iterates through each letter in the word given by user
    for word_num in range(len(word)):

        # For loop iterates through each letter of the alphabet
        for alphabet_num in range(len(alphabet)):

            # Checks if the letter of the given by user word is the same as letter of the alphabet
            if word[word_num] == alphabet[alphabet_num]:

                # If the letter of the given by user word is the same as letter of the alphabet
                # Checks if the operation given by user is to encode
                if operation == "encode":

                    # If the operation given by user is to encode
                    # Checks if the number by which world is to be moved is more than 25
                    if alphabet_num + shift_amount > 25:

                        # If the number by which world is to be moved is more than 25
                        # Creates the new letter by subtracting from the index of the same letter of the alphabet the multiplication of the 26 by the ceiling of the division of the number of the shift by 26
                        word[word_num] = alphabet[alphabet_num + shift_amount - 26 * (math.ceil(shift_amount / 26))]

                    else:

                        # If the number by which world is to be moved is not more than 25
                        # Creates new letter by adding to the index of the same letter of the alphabet the according number of the shift
                        word[word_num] = alphabet[alphabet_num + shift_amount]

                    # Breaks the loop
                    break

                # If the letter of the given by user word is the same as letter of the alphabet
                # Checks if the operation given by user is to decode
                elif operation == "decode":

                    # If the operation given by user is to decode
                    # Checks if the number by which world is to be moved is less than 0
                    if alphabet_num - shift_amount < 0:

                        # If the number by which world is to be moved is  less than 0
                        # Creates the new letter by adding to the index of the same letter of the alphabet the multiplication of the 26 by the floor of the division of the number of the shift by 26
                        word[word_num] = alphabet[alphabet_num - shift_amount + 26 * (math.floor(shift_amount / 26))]

                    else:

                        # If the number by which world is to be moved is not less than 0
                        # Creates new letter by subtracting from the index of the same letter of the alphabet the according number of the shift
                        word[word_num] = alphabet[alphabet_num - shift_amount]

                    # Breaks the loop
                    break

    # Transforms list of letter to encrypted or decrypted word
    word = "".join(word)

    # Prints encrypted or decrypted word
    print(word)


# Boolean initializes Caesar Cipher
caesar_cipher = True

# While loop initializes Caesar Cipher
while caesar_cipher:

    # Cleans the windows
    os.system("clear")

    # Prints welcome logo imported from art.py
    print(art.logo)

    # While loop to check if the operation which user wants to apply is correct
    while True:

        # Takes the operation given by user
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")

        # Checks if the operation given by user is correct
        if direction.lower() == "encode" or direction.lower() == "decode":

            # If operation given by user is correct
            # Breaks the loop
            break

    # Takes the word given by user
    text = input("Type your message: ")

    # Takes the number of shifts given by user
    shift = int(input("Type the shift number: "))

    # Initializes "caesar" function with arguments given by user
    caesar(text, shift, direction)

    # While loop to check if the user wants to one more time use program
    while True:

        # Takes the user's decision to run the program again is correct
        again = input("Type 'yes' if you want to go again. Otherwise type 'no'. ")

        # Check if the user's decision to run the program again is correct
        if again.lower() == "yes" or again.lower() == "no":

            # If user's decision to run the program again is correct
            # Breaks the loop
            break

    # Checks if  user's decision to run again the program is no
    if again == "no":

        # If user's decision to run again the program is no
        # Breaks the loop
        break

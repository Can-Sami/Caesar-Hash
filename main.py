
from operator import indexOf
from colorama import *

# TODO: Add  decryption function.

# HOW DOES IT WORK: For each character in the given input: take the index of the char in that string = "i"
# and index in the custom alphabet, add i to the place of that character in alphabet and return "key" replace the
# character with "custom_alphabet[key]" value in alphabet.

# Custom alphabet.
chars = "WYMZapyPoxBlUEDdHJTwzAVOFbrCtmeIkNKSLRhgcfqnuXjvsQiG1234567890 .,;!-_"

# Fixes if the index is out of range.
def fix_value(i):
    if i > 52:
        return i % 52
    else:
        return i

def alph_index(char):
    if char in chars:
        return int(chars.index(char))
    else:
        print("Character is not in the list???")
        return -1

def encrypt_string(input):
    enc_message = ""
    for letter in input:
        i = alph_index(letter) + indexOf(chars, letter)
        enc_message += chars[fix_value(i)]
    return enc_message

while True:
    try:
        print(Fore.CYAN + encrypt_string(input("Please enter the String you want to encrypt: ")))
    except ValueError:
        print(Fore.RED + "The string you entered contains illegal characters in it.")

def decrypt_string(input):
    pass
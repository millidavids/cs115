# Prolog
# Authors: David Yurek, Evan Whitmer, Stanley McClister
# Team 3
# Section: 012
# November 13, 2013
# Lab 13 Team

from string import ascii_uppercase, ascii_letters


def caesarencrypt(string, shift):
    newstring = ''
    for iterate in string:
        character_code = ord(iterate)
        if iterate not in ascii_letters:
            newstring += iterate
        elif iterate in ascii_uppercase:
            newstring += chr((character_code - ord('A') + shift) % 26 + ord('A'))
        else:
            newstring += chr((character_code - ord('a') + shift) % 26 + ord('a'))
    return newstring


def caesardecrypt(string, shift):
    return caesarencrypt(string, - shift)


def main():

    string = input('Enter clear text: ')
    shift = int(input('Enter shift value: '))
    encrypted_string = caesarencrypt(string, shift)
    decrypted_string = caesardecrypt(encrypted_string, shift)

    print(encrypted_string)
    print(decrypted_string)

main()
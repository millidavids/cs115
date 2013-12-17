# Prolog
# Author: David Yurek
# Email: dayure2@g.uky.edu
# Section: 012
# November 6, 2013
# Lab 12 Individual


# ______________________________________________________________________________
#
# Purpose: The purpose of this program is to take a concatenated string of strings to make a sentence.
#          The program only concatenates the word to the sentence if it is longer than 3 characters.
#          Using sentinel logic, the program will quit if the word stop is input.
#
# Preconditions: The program accepts strings from the user.
#
# Post-conditions: The program will output a concatenated string of the words input of words longer than
#                  three characters.
#_______________________________________________________________________________
def main():

    #Initialize a word variable and set equal to the input of the user.
    word = input('Enter a word: ')

    #Initialize a sentence variable and set equal to an empty string.
    sentence = ''

    #While loop using sentinel logic to check the word variable to see if 'stop' was input.
    while word != 'stop':

        #If selection to concatenate the word to the sentence variable if the word is longer than 3 characters.
        if len(word) > 3:
            sentence += word + ' '

        #Reassign the word variable to a new input from the user.
        word = input('Enter a word: ')

    #Print the final sentence.
    print('The sentence is:', sentence)


#Call main().
main()
# Prolog
# Author: David Yurek
# Email: dayure2@g.uky.edu
# Section: 012
# November 12, 2013
# Lab 13 Individual

#Import from the string library to be able to use ascii_letters
from string import ascii_letters


# ______________________________________________________________________________
#
# Purpose: This is the function that uses the count() and isalpha() modules to count the number
#as        'e's and alphabetical characters in the string fed to it.
#
# Preconditions: The function accepts a string as a single argument.
#
# Post-conditions: The function returns 2 numbers. First the number of alphabetical characters
#                  in the string. Second the number of 'e's in the string.
#_______________________________________________________________________________
def stringnumbers(string):

    #Iniitiates an alpha variable with a zero value.
    alpha = 0

    #For loop to iterate over all of the letters in the string.
    for check in string:

        #If statement to test whether or not the letter is an alphabetical character. If so, accumulates a +1 to alpha.
        if check.isalpha():
            alpha += 1

    #Counts the number of 'e's in the string and initiates a e_s variable with that value.
    e_s = string.count('e')

    #Returns the two numbers, alpha first, e_s second.
    return alpha, e_s


# ______________________________________________________________________________
#
# Purpose: This is the function that does not use the count() or isalpha() modules to count
#          the number of 'e's and alphabetical characters in the string fed to it.
#
# Preconditions: The function accepts a string as a single argument.
#
# Post-conditions: The function returns 2 numbers. First the number of alphabetical characters
#                  in the string. Second the number of 'e's in the string.
#_______________________________________________________________________________
def stringchecker(string):

    #Initialize an alpha variable with a value of zero.
    alpha = 0

    #Initialize an e_s variable with a value of zero.
    e_s = 0

    #For loop to iterate through every character in the string.
    for check in string:

        #If statement to check whether the letter is either a upper or lower case 'e'. If so, accumulates a +1 to e_s.
        if check == 'e' or check == 'E':
            e_s += 1

        #If statement to check whether the letter is actually an alphabetical letter. If so, accumulates a +1 to alpha.
        if check in ascii_letters:
            alpha += 1

    #Returns two values, the numbers of alpha and e_s in that order.
    return alpha, e_s


# ______________________________________________________________________________
#
# Purpose: This program asks the user for a string and counts the number of alphabetical characters
#          and the number of 'e's in the string and reports those numbers as well as the percentage of
#          'e's to total alphabetical letters.
#
# Preconditions: The program asks the user for a string.
#
# Post-conditions: The program prints out a statement that reports the number of alphabetical characters
#                  as well as the number of 'e's and the percentage of 'e's to total letters.
#_______________________________________________________________________________
def main():

    #initiates a sentence variable and sets it equal to the input string of the user.
    sentence = input('Enter a sentence: ')

    #Initiates 2 variables and sets them equal to the two returns of the stringchecker() function.
    alpha, e_s = stringchecker(sentence)

    #Calculate percentage of 'e's to letters.
    percent = round(e_s/alpha*100, 1)

    #Prints the final message with the results of the program.
    print('Your text contains ', alpha, ' alphabetic characters of which ', e_s, ' (', percent, "%) are 'e'.", sep='')


#Call main().
main()


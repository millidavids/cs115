# Prolog
# Author: David Yurek, Stanley McClister, Evan Whitmer
# Section: 012
# Team 3
# November 8, 2013
# Lab 11 Team


# ______________________________________________________________________________
#
# Purpose: This function accepts a string and checks whether or not the string is palindrome.
#
# Preconditions: The function accepts one argument, a string.
#
# Post-conditions: The program will check whether or not the string is a palindrome, if so,
#                  it will return a True bool.
#_______________________________________________________________________________
def palindrome(string):

    #Initialize a result bool variable and set to False
    result = False

    #Initialize a backwards string variable and set to empty string.
    backwards_string = ''

    #Set the string to all lower case characters.
    string = string.lower()

    #Strip the spaces out of the string.
    string = string.replace(' ', '')

    #For loop in the range of the length of the string, to zero, decremented by one per iteration.
    for reverse in range(len(string), 0, -1):

        #Concatenates the backwards string with the index of the original string with index # of the for loop iteration.
        backwards_string += string[reverse - 1]

    #If the original string is the same as the backwards sting, set result to True.
    if string == backwards_string:
        result = True

    #Return result
    return result


# ______________________________________________________________________________
#
# Purpose: This program will get input form the user, call the palindrome function, and
#          output whether or not the string is a palindrome or not.
#
# Preconditions: The program accepts a string from the user.
#
# Post-conditions: Outputs whether or not the string was a palindrome or not.
#_______________________________________________________________________________
def main():

    #Get input form the user in string form.
    string = input('Enter you string to check for palindrome: ')

    #If the return of palindrome() is True, print a confirmation, else, print negation.
    if palindrome(string):
        print('Yes, your string is a palindrome.')
    else:
        print('No, your string is not a palindrome.')


#Call main()
main()
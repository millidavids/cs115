# Prolog
# Authors: David Yurek, Evan Whitmer, Stanley McClister
# Team 3
# Section: 012
# November 15, 2013
# Lab 14 Team


# ______________________________________________________________________________
#
# Purpose: This function accepts a list and prints out which substring of the two numbers in
#          the list is larger.
#
# Preconditions: The function accepts one argument, a list.
#
# Post-conditions: The program has no return values, but does, itself, print a string of which
#                  substring is larger based on the list it is fed.
#_______________________________________________________________________________
def comparetwostring(numberslist):

    if numberslist[0] > numberslist[1]:
        print(numberslist[0], 'is larger.')
    elif numberslist[0] < numberslist[1]:
        print(numberslist[1], 'is larger.')
    else:
        print('The numbers are equal.')


# ______________________________________________________________________________
#
# Purpose: This function accepts a list and prints out which number of the two numbers in
#          the list is larger.
#
# Preconditions: The function accepts one argument, a list.
#
# Post-conditions: The program has no return values, but does, itself, print a string of which
#                  number is larger based on the list it is fed.
#_______________________________________________________________________________
def comparetwo(numberslist):

    if float(numberslist[0]) > float(numberslist[1]):
        print(numberslist[0], 'is larger.')
    elif float(numberslist[0]) < float(numberslist[1]):
        print(numberslist[1], 'is larger.')
    else:
        print('The numbers are equal.')


# ______________________________________________________________________________
#
# Purpose: This program loops continually until two zeros are input and asks the user for a string of
#          two numbers. The program then calls the comparetwo() function to print out which number in
#          the string of two numbers is larger.
#
# Preconditions: The program continually asks the user for string inputs until '0 0' is given.
#
# Post-conditions: The program calls the comparetwo() function which prints out which number is larger.
#_______________________________________________________________________________
def main():

    numbers = input('Enter two numbers separated by a space: ')
    numberslist = numbers.split()
    while int(numberslist[0]) != 0 and int(numberslist[1]) != 0:
        comparetwo(numberslist)
        numbers = input('Enter two numbers separated by a space: ')
    print('Goodbye')


main()

# Question 1: The digit version is running. If the string version was running it would have said
#             that 153 is less than 23 because 1 < 2.
# Question 2: The digit version compares the numbers as a whole. The string version compares the indices
#             of each string starting at [0]. That is why the string version would evaluate 153 as less
#             than 23.
# Question 3: If the user puts three numbers, it only compares the first two items. If the users puts in
#             one number, you get an error since the function tries to call the [1] index of the list. If
#             the user tries to input something other than a number, the digit version will cause an error
#             when trying to convert the list index to a float. The string version will work, but will have
#             strange outputs based on ascii characters.
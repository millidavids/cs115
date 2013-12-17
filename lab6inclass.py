# Prolog
# Authors: David Yurek, Stanley McClister, Evan Whitmer
# Section 012 :: Team 3
# September 27, 2013

# ______________________________________________________________________________
#
# Purpose: The purpose of this program is to make a multiplication iteration program
#          based on two integer inputs from the user.
#
# Preconditions: There are two inputs from the user; 2 integers.
#
# Post-conditions: The output of the program are the multiplication iterations of the for loop
#                  based on the 2 integer inputs from the user.
#_______________________________________________________________________________

# Call main.
def main():

    # Defines the variables based on user input.
    firstNum = int(input("Enter the first number: "))       # First integer used in iteration.
    secondNum = int(input("Enter the second number: "))     # Second integer used in iteration.
    iterationNum = int(input("How many iterations "
                             "of multiplication? "))        # Iteration number integer.
    dynamicVar = 0                                          # Dynamic variable used in loop.

    # Prints a line break and the first 2 numbers.
    print()
    print(firstNum, secondNum, end=" ")

    for mult in range(iterationNum):
        dynamicVar = secondNum
        secondNum *= firstNum
        firstNum = dynamicVar
        print(secondNum, end= " ")

main()
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

# Defines main
def main():

    # Defines the variables based on user input.
    firstNum = eval(input("Enter the first number: "))       # First integer used in iteration.
    secondNum = eval(input("Enter the second number: "))     # Second integer used in iteration.
    iterationNum = int(input("How many iterations "
                             "of multiplication? "))        # Iteration number integer.
    dynamicVar = 0                                          # Dynamic variable used in loop.

    # Prints a line break and the first 2 numbers.
    print()
    print(firstNum, secondNum, end=" ")

    # For loop for multiplication iteration based on the 3 integer user inputs.
    for mult in range(iterationNum):
        dynamicVar = secondNum                              # Reassigns dynamicVar as secondNum.
        secondNum *= firstNum                               # Reassigns secondNum as the product of itself and firstNum.
        firstNum = dynamicVar                               # Reassigns firstNum as dynamicVar.
        print(mult, "  ", secondNum)                        # Prints secondNum, which is the product of this iteration.

# Calls main.
main()

# 1. If the first two numbers are both one, all iterations of the loop product an output of 1.
# 2. If one of the first two numbers is zero, then the loop multiplies by zero and all subsequent products are zero.
# 3. If the first number is larger than the second number, the program runs as expected.
# 4. I get an error: ValueError: invalid literal for int() with base 10: '2.1'. It seems that I cannot change
#    a float into an integer. This is because I used the int() typecast instead of eval(). When I changed to
#    eval(), the program runs normally, multiplying floats. The range() for the for loop has to be an integer.
# 5. With any negative numbers in the loop, every third number ends up as a positive.
# 6. If we do not ask for the iteration number, the for loop fails to run because there is no range for it
#    the for loop to iterate over.
# 7. If we only ask for one number there is no second number to multiply with and there is no iteration number
#    for us to use as the iteration number in the for loop.
# 8. My program stopped after the 30th iteration with inputs of 2 and 3.
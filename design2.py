# Prolog
# Author: David Yurek
# Email: dayure2@g.uky.edu
# Section: 012
# Oct. 8, 2013
# Programming Assignment 2 Design
#
# ______________________________________________________________________________
#
# Purpose: The purpose of this assignment is to take an integer input from the user
#          and convert that number into the base of the user's choosing. The program
#          will launch a separate window with a simple user interface with 2 fields
#          for integer inputs and an are for the outputs.
#
# Preconditions: There are two different inputs. The first input is the integer to be
#                converted and the second is the base of conversion, as an integer.
#                The program also accepts mouse clicks from the user to forward the
#                progress of the program.
#
# Post-conditions: The program outputs the base conversion of the integer input as text
#                  in the graphics window, below the entry field. The program then
#                  prompts the user to click to exit the program
#_______________________________________________________________________________

# Step 1: Import math library.
# Step 2: Import graphics library.
#
# Step 3: Define main().
#     Step 4: Define the conversion number as the input from the user: 'convertible'.
#     Step 5: Define the base number as the input from the user: 'conversionBase'.
#     Step 6: Define the conversion range: int(log(convertible)/log(conversionBase)): 'conversionRange'.
#     Step 7: Define the result text calling from the conversion function,
#              with (convertible, conversionBase, conversionRange) as arguments, in the window.
# Step 8: Call main().
#
# Step 9: Define conversion(convInt, convBase, convRange) function with these 3 parameters.
#     Step 10: Define a remainder variable and set equal to zero: 'remainder'.
#     Step 11: Define a range counter and set it equal to convRange: 'convRange_counter.
#     Step 12: Define a result string variable and assign it as an empty string: 'resultStr'
#     Step 13: Call a for loop: for conv in range(convRange):.
#         Step 13.1: Reassign remainder variable as: convInt % convBase ** convRange_counter.
#         Step 13.2: Reassign convInt variable as: convInt // convBase ** convRange_counter.
#         Step 13.3: Add str(convInt) to resultStr. resultStr += str(convInt).
#         Step 13.4: Reassign convInt variable as the remainder variable.
#         Step 13.5: convRange_counter is a decumulator, iterate here: convRange_counter -= 1.
#     Step 14: Add the final convInt to resultStr: resultStr += str(convInt).
#     Step 15: Return resultStr
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
#     Step 4: Draw the window and set the background as gray.
#     Step 5: Define and draw the text for the conversion number entry field in the window.
#     Step 6: Define and draw the entry field for the conversion number in the window.
#     Step 7: Define and draw the text for the base entry field in the window.
#     Step 8: Define and draw the entry field for the base in the window.
#     Step 9: Use window.getMouse() to pause the program at this point so the user can input data.
#     Step 10: Define the conversion number as the input of the first entry field as an integer: 'convertible'.
#     Step 11: Define the base number as the input from the second entry field as an integer: 'conversionBase'.
#     Step 12: Define the conversion range: int(log(convertible)/log(conversionBase)): 'conversionRange'.
#     Step 13: Define and draw the result text calling from the conversion function,
#              with (convertible, conversionBase, conversionRange) as arguments, in the window.
#     Step 14: Define and draw the 'Click to exit.' text in the window.
#     Step 15: Use window.getMouse() to pause the program at this point so the user can see the results.
#     Step 16: Close the window after the mouse click.
# Step 17: Call main().
#
# Step 18: Define conversion(convInt, convBase, convRange) function with these 3 parameters.
#     Step 19: Define a remainder variable and set equal to zero: 'remainder'.
#     Step 20: Define a range counter and set it equal to convRange: 'convRange_counter.
#     Step 21: Define a result string variable and assign it as an empty string: 'resultStr'
#     Step 22: Call a for loop: for conv in range(convRange):.
#         Step 23: Reassign remainder variable as: convInt % convBase ** convRange_counter.
#         Step 24: Reassign convInt variable as: convInt // convBase ** convRange_counter.
#         Step 25: Add str(convInt) to resultStr. resultStr += str(convInt).
#         Step 26: Reassign convInt variable as the remainder variable.
#         Step 27: convRange_counter is a decumulator, iterate here: convRange_counter -= 1.
#     Step 23: Add the final convInt to resultStr: resultStr += str(convInt).
#     Step 24: Return resultStr
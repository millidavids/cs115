# Prolog
# Author: David Yurek, Evan Whitmer, Stanley McClister
# Email: dayure2@g.uky.edu
# Section: 012
# Oct. 9, 2013
# Programming Assignment 2
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

# Step 3: Define main().
#     Step 4: Call and define a window and set the background as gray.
#     Step 5: Set coordinates of the window with setCoords().
#     Step 6: Define and draw the text for the conversion number entry field in the window.
#     Step 7: Define and draw the entry field for the conversion number in the window.
#     Step 8: Define and draw the text for the base entry field in the window.
#     Step 9: Define and draw the entry field for the base in the window.
#     Step 10: Use window.getMouse() to pause the program at this point so the user can input data.
#     Step 11: Define the conversion number as the input of the first entry field as an integer: called convertible.
#     Step 12: Define the base number as the input from the second entry field as an integer: called conversionBase.
#     Step 13: Define the conversion range: int(log(convertible)/log(conversionBase)): called conversionRange.
#     Step 14: Define a remainder variable and set equal to zero: called remainder.
#     Step 15: Define a range counter and set it equal to conversionRange: called convRange_counter.
#     Step 16: Define a result string variable and assign it as an empty string: called resultStr
#     Step 17: Call a for loop: for conv in range(conversionRange):.
#         Step 17.1: Reassign remainder variable as: convertible % conversionBase ** convRange_counter.
#         Step 17.2: Reassign convertible variable as: convertible // conversionBase ** convRange_counter.
#         Step 17.3: Add str(convertible) to resultStr. resultStr += str(convertible).
#         Step 17.4: Reassign convertible variable as the remainder variable.
#         Step 17.5: convRange_counter is a decumulator, iterate here: convRange_counter -= 1.
#     Step 18: Add the final convertible to resultStr: resultStr += str(convertible).
#     Step 19: Define and draw the result text calling from resultStr.
#     Step 20: Define and draw the 'Click to exit.' text in the window.
#     Step 21: Use window.getMouse() to pause the program at this point so the user can see the results.
#     Step 22: Close the window after the mouse click.
# Step 23: Call main().

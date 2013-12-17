# Prolog
# Author: David Yurek
# Email: dayure2@g.uky.edu
# Section: 012
# Oct. 11, 2013
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

#Import math and graphics libraries. From math the log function is used. From the graphics library the GraphWin,
#    setCoords, setBackground, setSize, setStyle, setFill, Text, Entry, Point, and getText functions are used.
from math import log
from graphics import *

#Define main().
def main():

    #Call and define a window, modify the coordinates and set the background as gray.
    window = GraphWin('Big Blue Base Converter', 500, 500)
    window.setCoords(0, 0, 499, 499)
    window.setBackground('gray')

    #Define the text variable for the conversion number entry field in the window.
    convertible_field_text = Text(Point(250, 430), 'Enter a decimal number.')

    #Modify and draw the text variable for the conversion number in the text field.
    convertible_field_text.setSize(15)
    convertible_field_text.setStyle('bold')
    convertible_field_text.draw(window)

    #Define the entry field variable for the conversion number in the window.
    convertible_entry_field = Entry(Point(250, 400), 50)

    #Modify and draw the entry field for the conversion number in the window.
    convertible_entry_field.setFill('white')
    convertible_entry_field.draw(window)

    #Define the text variable for the base entry field in the window.
    conversion_base_field_text = Text(Point(250 ,330), 'Convert to what base?')

    #Modify and draw the text variable for the base entry field.
    conversion_base_field_text.setSize(15)
    conversion_base_field_text.setStyle('bold')
    conversion_base_field_text.draw(window)

    #Define the entry field variable for the base in the window.
    conversion_base_entry_field = Entry(Point(250, 300), 50)

    #Modify and draw the entry field variable for the base in the window.
    conversion_base_entry_field.setFill('white')
    conversion_base_entry_field.draw(window)

    #Use window.getMouse() to pause the program at this point so the user can input data.
    window.getMouse()

    #Define the conversion number as the input of the first entry field as an integer: 'convertible'.
    convertible = int(convertible_entry_field.getText())

    #Define the base number as the input from the second entry field as an integer: 'conversion_base'.
    conversion_base = int(conversion_base_entry_field.getText())

    #Define the conversion range: int(log(convertible)/log(conversionBase)): 'conversion_range'.
    conversion_range = int(log(convertible)/log(conversion_base))

    #Define a remainder variable for use in the for loop with value of zero.
    remainder = 0

    #Define a string variable to concatenate the iterations of the for loop.
    converter_string = ''

    #Define the result string calling from convertible and conversion_base.
    result_string = str(convertible) + ' converted to base ' + str(conversion_base) + ' is '

    #Using a for loop, we will convert the convertible into the appropriate base. This for loop uses reassignment,
    #    modulus, integer division, and concatenation to build the conversion.
    for converter in range(conversion_range, -1, -1):
        remainder = convertible % conversion_base ** (converter)
        convertible = convertible // conversion_base ** (converter)
        converter_string += str(convertible)
        convertible = remainder

    #Concatenate the converter string onto the end of the result string.
    result_string += converter_string + '.'

    #Define a result text variable and set as the result string.
    result_text = Text(Point(250, 230), result_string)

    #Modify and draw the result text into the window.
    result_text.setSize(15)
    result_text.setStyle('bold')
    result_text.draw(window)

    #Define and draw the 'Click to exit.' text in the window.
    exit_text = Text(Point(250, 200), 'Click to exit.')
    exit_text.setSize(15)
    exit_text.setStyle('bold italic')
    exit_text.draw(window)

    #Use window.getMouse() to pause the program at this point so the user can see the results.
    window.getMouse()

    #Close the window after the mouse click.
    window.close()

#Call main().
main()
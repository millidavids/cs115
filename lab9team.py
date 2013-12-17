# Prolog
# Authors: David Yurek, Evan Whitmer, Stanley McClister
# Section: 012
# Oct. 24, 2013
# Lab 9 Team

#Define the leap year calculator.
def leapcalc (year):

    #Define a return variable so we do not have more than one return statement.
    ret = True

    #Use an if/elif/else statement to test for a leap year and set the ret variable accordingly.
    if year % 100 == 0 and year % 400 != 0:
        ret = False
    elif year % 4 == 0:
        ret = True
    else:
        ret = False

    #Return the value of the boolean return variable.
    return ret

#Define main.
def main():

    #Prompt the user for a year.
    year = int(input('Enter a year: '))

    #Use an if statement to determine if the leapcalc function verifies that the year is a leap year or not.
    if leapcalc(year):
        print('Yes,', year, 'is a leap year.')
    else:
        print('No,', year, 'is not a leap year.')

#Call main.
main()


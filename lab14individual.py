# Prolog
# Author: David Yurek
# Email: dayure2@g.uky.edu
# Section: 012
# November 14, 2013
# Lab 14 Individual

# ------------NOTE------------
# I changed up the design a bit. I believe my way runs a bit faster and requires less code.
# It also uses a function call instead of one giant main(). I think this makes readability
# a bit better as well.
# ------------NOTE------------


# ______________________________________________________________________________
#
# Purpose: This function accepts a string which is a name and returns the name in a proper
#          "last name first" form as well as the persons initials.
#
# Preconditions: The function accepts one argument, a string.
#
# Post-conditions: The program returns 2 strings, the proper "last name first" string and the initials.
#_______________________________________________________________________________
def propername(name):

    namelist = name.split()
    newname = ''
    initials = ''

    if len(name) == 0:
        newname = 'No name?'
        initials = 'Blank Initials'
    else:
        for i in range(len(namelist)):
            newname += namelist[i-1]
            if i == 0:
                newname += ', '
            else:
                newname += ' '
            initials += namelist[i][0]

    return newname, initials


# ______________________________________________________________________________
#
# Purpose: This program asks the user to input their name and prints their name in the proper
#          "last name first" format, their initials, and the lowercase form of the proper form.
#
# Preconditions: The program asks the user for one string, a name.
#
# Post-conditions: The program calls the propername() function and uses the return to print the
#                  proper name, initials, and the lowercase form of the proper form.
#_______________________________________________________________________________
def main():

    name = input('Enter full name, first name first: ')
    newname, initials = propername(name)

    print(newname)
    print(initials)
    print('As lowercase:', newname.lower())


main()
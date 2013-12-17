# Prolog
# Author: David Yurek
# Email: dayure2@g.uky.edu
# Section: 012
# Oct. 24, 2013
# Lab 9 Individual

# Define main.
def main():

    #Print opening message about choices.
    print('Enter your choices as y or n.')

    #Define a total variable.
    total = 0

    #Define a hamburger variable from user input then use an if statement to determine if the
    #    price is added to the total.
    hamburger = input('Do you want a hamburger? ')
    if hamburger == 'y':
        total += 5

    #Define a pizza variable from user input then use an if statement to determine if the
    #    price is added to the total.
    pizza = input('Do you want a slice of pizza? ')
    if pizza == 'y':
        total += 3.5

    #Define a fries variable from user input then use an if statement to determine if the
    #    price is added to the total.
    fries = input('Do you want fries? ')
    if fries == 'y':
        total += 2

    #Define a chicken variable from user input then use an if statement to determine if the
    #    price is added to the total.
    chicken = input('Do you want some chicken? ')
    if chicken == 'y':
        total += 5

    #Define a milkshake variable from user input then use an if statement to determine if the
    #    price is added to the total.
    milkshake = input('Do you want a milkshake? ')
    if milkshake == 'y':
        total += 1.75

    # Print a linebreak, output hte food total and print the closing message.
    print("")
    print('The total for your food is $', total, '.', sep='')
    print('Thank you for your business.')

#Call main
main()


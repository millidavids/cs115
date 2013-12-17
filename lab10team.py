# Prolog
# Author: David Yurek, Stanley McClister, Evan Whitmer
# Team 3
# Section: 012
# Nov. 1, 2013
# Lab 10 Team

def main():
    too_high = False
    too_low = False    
    for i in range(10):
        number = float(input('Enter number ' + str(i+1) + ' '))
        if number > 30:
            too_high = True
        if number < 15:
            too_low = True
    if too_low:
        print('There was at least one number below the lower bound')
    else:
        print('There were no numbers below the lower bound')
    if too_high:
        print('There was at least one number above the upper bound')
    else:
        print('There were no numbers above the upper bound')
main()

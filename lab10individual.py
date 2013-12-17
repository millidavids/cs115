# Prolog
# Author: David Yurek
# Email: dayure2@g.uky.edu
# Section: 012
# Oct. 20, 2013
# Lab 10 Individual

def main():

    continuation = 'y'

    first = int(input('Enter a number '))
    largest = first
    compare = first
    ascending = True
    total = first

    while continuation.lower() != 'n':
        continuation = input('More? ')
        if continuation != 'n':
            compare = int(input('Enter a number '))
            total += compare
        if compare < first and ascending:
            ascending = False
        if compare < first:
            largest = first
        else:
            largest = compare
        first = compare



    print('The largest number was', largest)
    if ascending:
        print('The numbers were all in ascending order')
    else:
        print('The numbers were not in ascending order')
    print('The total of all of the numbers is', total)


main()
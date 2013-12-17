# Prolog
# Author: David Yurek
# Email: dayure2@g.uky.edu
# Section: 012
# November 4, 2013
# Lab 11 Individual


#David Yurek
def interest(principal, rate, compounded, years):
    return round(principal * (1 + rate / compounded) ** (compounded * years), 2)


#Stanley McClister
def investment(p,r,n,t):
    A = p*((1 + (r/n))**(n*t))
    return A


#Evan Whitmer
def compound_interest(p, r, n, t):
    total = p * (1 + r / n) ** (n * t)
    total = round(total, 2)
    return total


def main():

    principal = float(input('Enter principal or zero to stop: '))

    if principal == 0:
        print('Goodbye!')
    else:
        rate = float(input('Enter annual interest rate as a decimal: '))
        compounded = int(input('Enter the number of times the interest is compounded: '))
        years = int(input('Enter the number of years: '))
        print('That pays off $', interest(principal, rate, compounded, years), sep='')

main()
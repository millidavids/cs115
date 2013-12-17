# Prolog
# Author: David Yurek
# Email: dayure2@g.uky.edu
# Section: 012
# November 4, 2013
# Lab 11 Individual


#David Yurek - Most descriptive parameters, most compact design. Rounds to cents.
def interest(principal, rate, compounded, years):
    return round(principal * (1 + rate / compounded) ** (compounded * years), 2)


#Stanley McClister
#def investment(p,r,n,t):
#    A = p*((1 + (r/n))**(n*t))
#    return A


#Evan Whitmer
#def compound_interest(p, r, n, t):
#    total = p * (1 + r / n) ** (n * t)
#    total = round(total, 2)
#    return total


def main():
    principal = float(input('Enter principal or zero to stop: '))
    while principal != 0:

            rate = float(input('Enter annual interest rate as a decimal: '))
            compounded = int(input('Enter the number of times the interest is compounded: '))
            years = int(input('Enter the number of years: '))
            final = interest(principal, rate, compounded, years)
            print('That pays off $', final, '\n', sep='')
            principal = float(input('Enter principal or zero to stop: '))

    print('Goodbye!')

main()
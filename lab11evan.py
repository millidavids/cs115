# Evan Whitmer
# 11/3/13
# lab11.py
# Purpose: Calculate the results of compound interest
# Pre-conditions: Input 4 floats
# Post-conditions: 1 integer displaying total money

def main():
    principal = float(input('Enter principal: '))
    interest = float(input('Enter annual interest rate (as a  decimal): '))
    compound = float(input('Enter the number of compounds per year: '))
    year = float(input('Enter the number of years: '))
    total = compound_interest(principal, interest, compound, year)
    print('That pays off $', total, sep='')

# Purpose: Calculate the total amount of money after compound interest
# Pre-conditions: 4 parameters, all float. Principal (initial investment), Annual interest rate in a decimal
#   Times interest is compounded each year, Number of years the investment is compounded
# Post-conditions: returns single float number, total money
def compound_interest(p, r, n, t):
    total = p * (1 + r / n) ** (n * t)
    round(total, 2)
    return total

main()
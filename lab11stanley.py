# Stanley McClister
# Section: 12
# Date: 11/5/13
#-------------------------------------------------------------------
# Purpose is to calculate the interest from user input.
# Pre-conditions: We are given the formula for interest, we need the 
#     principal(p), interest rate(r), compound per year(n), and the 
#     number of years(t) 
# Postconditions: We output the payoff(total) 
#-------------------------------------------------------------------


def investment(p,r,n,t): 
    A = p*((1 + (r/n))**(n*t))
    return A
def main():
    p = int(input("Enter principal "))
    r = float(input("Enter annual interest rate as a decimal "))
    n = int(input("Enter number of compounds per year "))
    t = int(input("Enter number of years "))
    total = investment(p, r, n, t)
    print("That pays off $",total)
    
    
main()
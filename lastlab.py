# Prolog
# Authors: David Yurek, Stanley McClister, Evan Whitmer
# Section: 012 :: Team: 3
# December 11, 2013
# Last Lab


# Recursive functions
def main():
    n = 10
    looper1(n)
    print()
    n = 2
    looper2(n)
    print()
    for n in range(10):
        print(looper3(n), end=" ")
    print()


# The base case is: if n > 1.
# The functions continually stacks with a decremented argument 'n' until n is 1 or lower.
def looper1(n):
    if n > 1:
        print(n)
        looper1(n-1)


# The base case is: if n < 11.
# The functions continually stacks with an incremented argument 'n' until n is 11 or greater.
def looper2(n):
    if n < 11:
        print(n)
        looper2(n+1)


# There are 2 base cases. If n is less than 0 and if n is 0 or 1.
# The function continually stacks until n is 1 or lower.
def looper3(n):
    if n < 0:
        result = -1
    elif n == 1 or n == 0:
        result = 2
    else:
        result = looper3(n-1) * looper3(n-2)
    return result

main()


#a. If looper1 is called with a 0 as an argument, it does nothing.
#b. If looper2 is called with a 100 as an argument, it does nothing.
#c. Looper3 prints out a sequence of numbers whose pattern is determined by multiplying the previous 2 numbers
#   to get the next number.
#
# My python interpreter exceeded the maximum recursion stack with a value of 998. 997 was the highest number.
# error: RuntimeError: maximum recursion depth exceeded in comparison
# pycharm ide
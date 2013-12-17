# Prolog
# Author: David Yurek
# email: dayure2@g.uky.edu
# October 17, 2013
# Lab 8 Individual Problem

x = 5   # line A
y = 7

def funA(x, y):
   print(x+y)  # line B
   return x*y  # line C

def main():
   x = 9
   y = 15
   print(x, y) # line D
   a = funA(x, y)
   print(a) # line E

main()

# 1. The x variable is a global variable so it is available to all functions in this program file.
# 2. The x and y variables in line B are pointing to the global variables. The x and y variables in line D
#    are pointing to the local variables defined within main(). They are not the same.
# 3. The scope of the y variable used in line D is only available to main(). It is a local variable defined
#    only in main().
# 4. The scope of the a variable in line E is only available to main(). It is a local variable defined only
#    in main().
# 5. funA has no parameters in the original program given to us.

# By changing the function to receive 2 arguments (x and y from main()), subsequently changing the function
# to have 2 parameters (x and y), the functions is now being passed the values of x and y from main() and
# assigning them to its own local variables, x and y, rendering the global variables unused.
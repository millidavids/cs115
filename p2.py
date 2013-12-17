# Prolog
# Authors: David Yurek, Stanley McClister, Evan Whitmer
# Section: 012
# Team 3
# Sept. 13, 2013


def main ():

	num = int(input("Enter a number "))
	print("Your number is", num)
	d1 = num//100
	num = num%100
	d2 = num//10
	d3 = num%10

	print("The number reversed is ", d3, d2, d1, sep='')

main()

# When entering more than 3 digits the program reverses the last 2 digits, 
# but none of the others. For instance, if I put in 1234, it would output
# 4312. This program is only able to handle 3 digits.
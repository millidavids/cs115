# Prolog
# Author: David Yurek, Evan Whitmer, Stanley McClister
# October 18, 2013
# Lab 8 Team Problem

from math import e

def pop1(t):
    print(1 / (1 + e ** -t))


def pop2(t):
    return 1 / (1 + e ** -t)


def main():

    for t in range(-6, 7):
        print(t, " ", end="")
        pop1(t)

    total = 0
    for t in range(-6, 7):
        result = pop2(t)
        total += result
    print("Total is", total)

main()
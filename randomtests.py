# Prolog
# Author: David Yurek
# Email: dayure2@g.uky.edu
# Section: 012
# Sept. 26, 2012
# Random Testing

from random import *

def main():
    t = 0
    for i in range(1000):  # thousand
        t += random()
    print(t/1000)

    t = 0
    for i in range(100000): # hundred thousand
        t += random()
    print(t/100000)

    t = 0
    for i in range(1000000):  #million
        t += random()
    print(t / 1000000)
    t = 0
    for i in range(100000000): # hundred million
        t += random()
    print(t / 1e8)

main()

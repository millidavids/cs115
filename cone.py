# Prolog
# Author:  David Yurek
# Section: 012
# Date:   9/1/13
# Purpose:
#  Program to find the volume and surface area of a cone given the length
#       of the side, the radius and the height 
# Preconditions: (input)
#       User supplies radius, side and height of the cone (as numbers, no error checking done)
# Postconditions:  (output)
#       User greeted with a message
#       User prompted for input of radius, side, height
#       cone volume and surface area displayed
#### Design
#   1. greet the user
#   2. ask the user for the radius and read it in
#   3. ask the user for the length of the side of the cone and read it in
#   4. ask the user for the height of the cone and read it in
#   5. calculate the volume using the formula (one third pi radius squared height)
#   6. calculate the surface area using the formula (pi radius side + pi radius squared)
#   7. output the results with appropriate labels

from math import pi  # need value of pi for surface area and volume calculations

def main():
    print ("Hello Human!")  # this is a greeting
    radius = float(input("Enter the radius of the cone "))    # user prompt and input
    side = float(input("Enter the side of the cone "))        # user prompt and input
    height = float(input("Enter the height of the cone "))    # user prompt and input
    volume = pi / 3 * radius **2 * height                    # volume of a cone
    print ("The volume of the cone is", volume)              # output volume
    surface_area = pi * radius * side + pi * radius **2      # surface area of a cone
    print ("The surface area of the cone is", surface_area)  # output surface area

main ()
#  Program ends here
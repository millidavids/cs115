# Prolog
# Author: David Yurek
# Email: dayure2@g.uky.edu
# Section: 012
# Oct. 29, 2013
# Programming Assignment 3 Design

#Import randrange from the random library.
#Define a get_a_roll function that returns a random number randrange(1, 7). Precursor it with a function header comment.
#Define main(). Precursor it with a function header comment.
    #Print the welcome message with game title.
    #Define a first roll variable and call the get_a_roll() function as its value: first_roll
    #Define a current roll variable and set ot zero: current_roll
    #Define a continuation variable and sent to "y": continuation
    #Define an earnings variable and set to first_roll: earnings
    #Print the first roll.
    #Print the game rule that you can continue to play as long as you do not roll the same as the first.
    #Use a while loop to continue play as long as: current_roll != first_roll and continuation != 'n'
        #Add the value of current_roll to the earnings variable.
        #Print the total earnings.
        #Prompt the user for a continuation of play and set to the continua
        #Call the get_a_roll() function and set to current_roll.
        #Use if statement to determine if: current_roll == first_roll and continuation == 'y'
            #If so, print a game over message and that nothing is won.
        #Use elif statement to determine if: continuation == 'y'
            #If so, print how much was won with the roll.
        #Use else statement when the conditions are met to exit the program with earnings.
            #Print how much the use has won before the while loop breaks and the program ends.


#Call main.

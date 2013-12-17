# Prolog
# Author: David Yurek
# Email: dayure2@g.uky.edu
# Section: 012
# Oct. 20, 2013
# Programming Assignment 3 Shell Submission

#Import randrange from the random library.
from random import randrange

# ______________________________________________________________________________
#
# Purpose: The purpose of the get_a_roll function is to return a random number 1 through 6.
#
# Preconditions: The function has no parameters therefore accepts no arguments.
#
# Post-conditions: The function uses the randrange function from the random library to
#                  return a random number 1 through 6.
#_______________________________________________________________________________
def get_a_roll():
    return randrange(1, 7)


# ______________________________________________________________________________
#
# Purpose: The purpose of the prt_roll function is to print the image of the die based on the parameter.
#
# Preconditions: The argument given is the desired roll to print.
#
# Post-conditions: There is no return, instead it prints the die based on the argument fed to it.
#_______________________________________________________________________________
def prt_roll(cur):
    #if/elif statement to draw the correct die.
            if cur == 1:
                print('+---+')
                print('|   |')
                print('| * |')
                print('|   |')
                print('+---+')
            elif cur == 2:
                print('+---+')
                print('|  *|')
                print('|   |')
                print('|*  |')
                print('+---+')
            elif cur == 3:
                print('+---+')
                print('|  *|')
                print('| * |')
                print('|*  |')
                print('+---+')
            elif cur == 4:
                print('+---+')
                print('|* *|')
                print('|   |')
                print('|* *|')
                print('+---+')
            elif cur == 5:
                print('+---+')
                print('|* *|')
                print('| * |')
                print('|* *|')
                print('+---+')
            elif cur == 6:
                print('+---+')
                print('|* *|')
                print('|* *|')
                print('|* *|')
                print('+---+')



# ______________________________________________________________________________
#
# Purpose: This is the shell version of the game 'Don't Match'. The game consists of a dice
#          rolling function and a loop for continuous play. The user will get an initial dice
#          roll. That initial dice roll is added to his/her earnings and subsequent dice rolls
#          will be added as well as long as the dice rolls are not the same as the initial
#          roll. 2 conditions flag the end of the game. Either the user wants to stop playing
#          and leaves with their total earnings, or the player rolls the same as their first
#          roll, in which they win nothing and the program ends.
#
# Preconditions: The player is prompted with only one dialogue that asks for a continuation of
#                play. The user answers either 'y' for yes or 'n' for no. This is repeated
#                until the player loses or enters 'n' in which case the user leaves with their
#                earnings.
#
# Post-conditions: The initial output gives the player their first roll, game rule, and initial
#                  earnings. The outputs within the while loop give the subsequent earnings,
#                  total earnings, and prompts the user for continuation. If the player loses
#                  a separate output is displayed with a losing message, and yet another
#                  different output is displayed when the user stops continuation of play where
#                  the program outputs the total earnings of the player.
#_______________________________________________________________________________
def main():

    #Prints the opening message.
    print("The game of 'Don't Match'\n")

    #Defines the first variable which calls the function get_a_roll() for a value, 1-6.
    first_roll = get_a_roll()

    #Defines the current roll variable and set it equal to zero at the start of the program.
    current_roll = 0

    #Defines the continuation variable which will take on 2 values, either y or n, from the user.
    continuation = 'y'

    #Defines the earnings variable and sets it equal to the first roll for the initial earnings at the start.
    earnings = first_roll

    #Prints the first roll and the rule of the game.
    print('Your first roll is', first_roll)
    prt_roll(first_roll)
    print('You can continue to play as long as you do not roll another', first_roll, '\n')

    #While loop to iterate through the steps of the game dependent on the current roll, first roll, and continuation.
    while current_roll != first_roll and continuation != 'n':

        #Adds the current roll to the earnings, initial value is zero for current roll.
        earnings += current_roll

        #Prints the total earnings based on teh earnings variable.
        print('Your total earnings is $', earnings, sep='')

        #Prompts the user for a continuation of play and assigns the input to the continuation variable.
        continuation = input('Do you want to roll again (y or n)? ')

        #Uses the get_a_roll() function to assign a new random value to the current roll variable.
        current_roll = get_a_roll()

        #If statement to determine if the player wants to continue and has not rolled the initial roll again.
        if current_roll == first_roll and continuation == 'y':

            #Prints the losing message when the above if statement is met.
            print('\nGame over, your roll is the same as the first.')
            print('You win NOTHING!!!')

        #Elif statement to determine when the player wants to continue to play.
        elif continuation == 'y':
            prt_roll(current_roll)
            #Prints the winnings of the current roll.
            print('\nYou won $', current_roll, sep='')

        #Else statement to determine when the player wants to stop playing.
        else:

            #Prints the ending message with the total earnings.
            print('\nYou left with $', earnings, sep='')


#Calls main()
main()
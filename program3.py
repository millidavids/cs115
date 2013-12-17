# Prolog
# Author: David Yurek
# Email: dayure2@g.uky.edu
# Section: 012
# November 4, 2013
# Programming Assignment 3

#Import randrange from the random module to use as a die roller. Import all of the graphics methods from the graphics
# library. We will be using Image, Point, Text, Rectangle, GraphWin, getX, getY, draw, undraw, setSize, and setStyle.
from random import randrange
from graphics import *


# ______________________________________________________________________________
#
# Purpose: The purpose of the get_a_roll function is to return a random number 1 through 6.
#
# Preconditions: The function has no parameters therefore accepts no arguments.
#
# Post-conditions: The function uses the randrange function from the random module to
#                  return a random number 1 through 6.
#_______________________________________________________________________________
def get_a_roll():

    #Returns a number between 1-6 inclusive, which is why the left most number is a 7, using the randrange method.
    return randrange(1, 7)


# ______________________________________________________________________________
#
# Purpose: The purpose of the display_die function is to take a roll and draw the
#          corresponding die face .gif file to the window.
#
# Preconditions: The function accepts three arguments translated to the parameters current,
#                roll, and window. The first parameter is the current parameter, this is used
#                to check to see if the roll is the first roll. In main the current_roll
#                variable is initialized as zero. If this function is passed a zero as the
#                current_roll from main, which can only happen on for the first roll, the
#                image is drawn in a separate position than all other instances of this function.
#                The second parameter is the roll. This is always a number between 1-6 inclusive
#                and uses the if statement ot draw the corresponding image. The last parameter is
#                the window that the function is to draw to.
#
# Post-conditions: The function has no return value, but does draw images to the window initialized in
#                  main() which is passed to it.
#_______________________________________________________________________________
def display_die(current, roll, window):

    #This y position variable is used to determine where on the window the die image will be drawn.
    y_pos = 200

    #This small if statement only follows through on the first roll call, when the current parameter is passed as zero.
    if current == 0:
        y_pos = 400

    #This if/elif/else statement takes the roll parameter and determines which .gif file to draw based on its value.
    # The y-pos variable is used as the y coordinate and is different for the first roll than it is for all other rolls.
    if roll == 1:
        Image(Point(100, y_pos), 'one.gif').draw(window)
    elif roll == 2:
        Image(Point(100, y_pos), 'two.gif').draw(window)
    elif roll == 3:
        Image(Point(100, y_pos), 'three.gif').draw(window)
    elif roll == 4:
        Image(Point(100, y_pos), 'four.gif').draw(window)
    elif roll == 5:
        Image(Point(100, y_pos), 'five.gif').draw(window)
    else:
        Image(Point(100, y_pos), 'six.gif').draw(window)


# ______________________________________________________________________________
#
# Purpose: This program is the game of "Don't Match". This game is a dice rolling game where
#          the user receives a first roll and then continues to roll, accumulating money based on
#          the value of the rolls. There is one rule though. The user cannot roll the same value as
#          their first roll. If they do, then they lose all of their money and the program exits.
#          The use may choose at any time to end the program with their winnings by click on NOT
#          the yes, box. Clicking anywhere other than the yes box will flag the program to stop.
#
# Preconditions: The only input received from the user are mouse clicks. These mouse clicks determine
#                whether or not the program continues to roll for the user or not and if the user wants
#                to leave with their winnings.
#
# Post-conditions: The program outputs information and pictures to a window. This window is labeled
#                  "Don't Match" and has 2 pictures displayed to it, one for the first roll and one
#                  for their current roll. The information displayed is the value of the rolls, the
#                  rules, the yes and no continuation boxes, total earnings, and the winning/losing
#                  messages.
#_______________________________________________________________________________
def main():

    #Initialize the window variable and assign it the GraphWin object, 600x600 pixels, from the graphics module.
    window = GraphWin("Don't Match!", 600, 600)

    #Modify the coordinates of the window to set the origin to the bottom left of the window.
    window.setCoords(0, 0, 599, 599)

    #Initializa a first roll variable and call the get_a_roll function to assign it a random number between 1-6.
    first_roll = get_a_roll()

    #Initialize a current roll variable with a value of zero so the first roll die display draws correct coordinates.
    current_roll = 0

    #Initialize a continuation flag with a True value so the while loop starts and continues without reassignment.
    continuation = True

    #Initialize an earnings variable and set it equal to the first roll. This is how much winnings the user starts with.
    # This will also be the variable that will accumulate the total winnings.
    earnings = first_roll

    #Initialize the Ttxt object variables that will be drawn in th window to display the output.
    roll_text = Text(Point(400, 450), "You're first roll is " + str(first_roll))
    rule_text = Text(Point(400, 400), 'You can roll as long as you do not roll another ' + str(first_roll))
    earnings_text = Text(Point(400, 350), 'You currently have $' + str(earnings))
    question_text = Text(Point(400, 250), 'Would you like to roll again?')
    yes_text = Text(Point(350, 175), 'YES')
    no_text = Text(Point(450, 175), 'NO')

    #Initialize the rectanglular boxes that the user will click into for continuation.
    yes_box = Rectangle(Point(325, 150), Point(375, 200))
    no_box = Rectangle(Point(425, 150), Point(475, 200))

    #Set the size of the text of the text object variables and set the 'Yes' and 'No' as bold type.
    roll_text.setSize(15)
    rule_text.setSize(15)
    earnings_text.setSize(15)
    question_text.setSize(15)
    yes_text.setSize(20)
    yes_text.setStyle('bold')
    no_text.setSize(20)
    no_text.setStyle('bold')

    #Draw the text objects and rectangle objects to the window.
    roll_text.draw(window)
    rule_text.draw(window)
    earnings_text.draw(window)
    question_text.draw(window)
    yes_text.draw(window)
    no_text.draw(window)
    yes_box.draw(window)
    no_box.draw(window)

    #Call the display die function for the first roll, which will draw the die at coordinate (100, 400).
    display_die(current_roll, first_roll, window)

    #Start a while loop with conditions to continue to run as long as the rolls don't match and the game continues.
    while current_roll != first_roll and continuation:

        #Concatonate the earnings with the current roll.
        earnings += current_roll

        #Call the get a roll function to give the user a new current roll.
        current_roll = get_a_roll()

        #Initialize a yes_no variable and set it to the mouse click. This is use to determine if the user clicks the
        # yes box to determine the continuation of the program.
        yes_no = window.getMouse()

        #If statement to determine if the user clicked the mouse in the yes box or not. If so, it keeps continuation
        # flag as a True value. If not, it sets the continuation flag as False.
        if yes_no.getX() > 375 or yes_no.getX() < 325 or yes_no.getY() > 200 or yes_no.getY() < 150:
            continuation = False

        #If statement to determine the fate of the program. If checks to see if the user loses by checking to see if the
        # users current roll is the same as the first roll and that continuation is still True. If so it displays the
        # die, and sets the text objects in the window to display the losing message only. Undraws unnecessary text
        # objects.
        if current_roll == first_roll and continuation:
            display_die(current_roll, current_roll, window)
            roll_text.undraw()
            rule_text.setText('Game over, you rolled another ' + str(first_roll))
            earnings_text.setText('You win NOTHING!!!')
            question_text.undraw()
            yes_text.undraw()
            no_text.undraw()
            yes_box.undraw()
            no_box.undraw()

        #Elif checks that continuation is still True. This is the option where the user did not roll the same as the
        # first roll, and still wants to continue to play. Displays the die, shows the messages corresponding to the
        # continuation condition of the program.
        elif continuation:
            display_die(current_roll, current_roll, window)
            roll_text.setText("You rolled a " + str(current_roll))
            earnings_text.setText('You won $' + str(current_roll) + '\nYou now have $' + str(current_roll + earnings))

        #Else only runs if the continuation is False. This means the rolls were not the same, but the user wants to
        # stop playing. This shows the message that the user left with their total earnings. Undraws unnecessary text
        # objects.
        else:
            roll_text.undraw()
            rule_text.undraw()
            earnings_text.setText('You left with $' + str(earnings))
            question_text.undraw()
            yes_text.undraw()
            no_text.undraw()
            yes_box.undraw()
            no_box.undraw()

    #getMouse to pause the program so the user can see the final message of the program.
    window.getMouse()

    #Close the window to signal the end of the program.
    window.close()


#Call main.
main()
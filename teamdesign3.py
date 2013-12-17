# Prolog
# Authors: David Yurek, Stanley McClister, Evan Whitmer
# Team 3
# Section: 012
# Oct. 30, 2013
# Programming Assignment 3 Team Design

#Import randrange from random module.
#Import the graphics module.
#Define a get_a_roll function that returns a random number randrange(1, 7). Precursor it with a header comment.
#Define a draw_one function that will draw a one sided die in the window showing a one. No parameters, no return.
    #Draws a the die file using the image call from the graphics module.
#Define a draw_two function that will draw a one sided die in the window showing a two. No parameters, no return.
    #Draws a the die file using the image call from the graphics module.
#Define a draw_three function that will draw a one sided die in the window showing a three. No parameters, no return.
    #Draws a the die file using the image call from the graphics module.
#Define a draw_four function that will draw a one sided die in the window showing a four. No parameters, no return.
    #Draws a the die file using the image call from the graphics module.
#Define a draw_five function that will draw a one sided die in the window showing a five. No parameters, no return.
    #Draws a the die file using the image call from the graphics module.
#Define a draw_six function that will draw a one sided die in the window showing a six. No parameters, no return.
    #Draws a the die file using the image call from the graphics module.
#Define a display_die function that will accept an integer 1-6 and will call one of the draw die functions to display
#the die in the window. One integer parameter, no return.
#Define a check_box function that will check to see if the point given is within the coordinates of the yes box.
    #Use an if statement to test whether or not the point is within the yes box, if so, return 'y', else, return 'n'.
    #Accepts one parameter, a point, and returns a string 'y' or 'n'.
#Define main(). Precursor it with a header comment.
    #Define a window variable and assign it a GraphWin().
    #Define a first roll variable and call the get_a_roll() function as its value: first_roll
    #Define a current roll variable and set ot zero: current_roll
    #Define a continuation variable and sent to "y": continuation
    #Define an earnings variable and set to first_roll: earnings
    #Using the text function from the graphics module, define a text variable with the welcome message.
    #Draw the text in the window.
    #Using the text function from the graphics module, define a text variable with the rolls.
    #Draw the rolls text variable using the first_roll variable with a message about the first roll.
    #Using the text function from the graphics module, define a text variable with the game rules.
    #Draw the game rules text variable in the window.
    #Using the text function from the graphics module, define a text variable with the earnings.
    #Using the text function from the graphics module, define a text variable for the continuation of play.
    #Using the rectangle and text functions, make 2 buttons, yes and no.
    #Using the text function from the graphics module, define a text variable for the losing message.
    #Using the text function from the graphics module, define a text variable for the round winnings message.
    #Using the text function from the graphics module, define a text variable for the winning exit message.
    #Draw the buttons in the window.
    #Use a while loop to continue play as long as: current_roll != first_roll and continuation != 'n'
        #Add the value of current_roll to the earnings variable.
        #Draw the earnings text variable in the window.
        #Draw the continuation of play text variable n the window.
        #Call the get_a_roll() function and set to current_roll.
        #Use getMouse() to get a point and assign it to a variable: yes_no
        #Call the check_box() function with the yes_no variable as an argument and assign the return to continuation.
        #Use if statement to determine if: current_roll == first_roll and continuation == 'y'
            #If so, draw the losing message.
        #Use elif statement to determine if: continuation == 'y'
            #If so, draw the round winnings message.
            #Also, call the display_die() function with the current_roll as it's argument.
        #Use else statement when the conditions are met to exit the program with earnings.
            #Draw the winning exit message.
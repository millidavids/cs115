# Prolog
# Author: David Yurek
# Section 012
# Sept. 19, 2013
# Lab 5

# Draws a stick figure.

import graphics

def main():
    
    window = graphics.GraphWin()
    window.setCoords(-10.0, -10.0, 10.0, 10.0)
    
    circle = graphics.Circle(graphics.Point(0, 5), 2)
    circle.setFill("orange")
    circle.draw(window)
    
    triangle = graphics.Polygon(graphics.Point(0,3), graphics.Point(3,-3), graphics.Point(-3,-3))
    triangle.setFill("red")
    triangle.draw(window)
    
    message = graphics.Text(graphics.Point(0,-9), "Draw the right arm.")
    message.draw(window)
    p1 = window.getMouse()
    p2 = window.getMouse()
    rightArm = graphics.Line(p1, p2)
    rightArm.draw(window)
    
    message.setText("Draw the left arm.")
    p3 = window.getMouse()
    p4 = window.getMouse()
    leftArm = graphics.Line(p3, p4)
    leftArm.draw(window)    
    
    message.setText("Draw the right leg.")
    p5 = window.getMouse()
    p6 = window.getMouse()
    rightLeg = graphics.Line(p5, p6)
    rightLeg.draw(window)
        
    message.setText("Draw the left leg.")
    p7 = window.getMouse()
    p8 = window.getMouse()
    leftLeg = graphics.Line(p7, p8)
    leftLeg.draw(window)
    
    message.setText("Click to close.")
    window.getMouse()
    window.close()
    
main()
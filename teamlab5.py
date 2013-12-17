# Prolog
# Author: David Yurek, Stanley McClister, Evan Whitmer
# Section 012
# Sept. 19, 2013
# Lab 5 Team Problem
# Team 3

# Purpose To take eight points (two lines), find the intersection point, and display
# this data in a graphics window.
# Preconditions: The user must enter eight points. (x1, y1), (x2, y2) for both lines.
# Post-conditions: To calculate two slopes, two y-intercepts, show equations for both lines,
# then show the intersecting point between the two lines.

#Imports the graphics library.
import graphics

#Defines main().
def main():
    print("The Great Intersection Finder")
    print()

    #Point one and two for line one.
    print("Enter the x and y for the first point on line 1")
    line1point1x, line1point1y = eval(input("X1, Y1  "))
    print("Enter the x and y for the second point on line 1")
    line1point2x, line1point2y = eval(input("X2, Y2  "))
    #Point one and two for line two.
    print("Enter the x and y for the first point on line 2")
    line2point1x, line2point1y = eval(input("X1, Y1  "))
    print("Enter the x and y for the second point on line 2")
    line2point2x, line2point2y = eval(input("X2, Y2  "))

    #Calculating the slopes of the lines.
    line1slope = (line1point2y - line1point1y) / (line1point2x - line1point1x)
    line2slope = (line2point2y - line2point1y) / (line2point2x - line2point1x)

    #Calculating the y-intercepts of the lines.
    # y1 - m * x1
    line1yint = line1point1y - (line1slope * line1point1x)
    line2yint = line2point1y - (line2slope * line2point1x)

    #Calculate where the two lines intersect.
    intersectx = (-line1yint + line2yint) / (line1slope - line2slope)
    intersecty = line1yint + (line1slope * intersectx)

    #Show what line 1 and 2 points are, their lines, and point of intersection.
    print("Line 1: (", line1point1x, ",", line1point1y, ") and (", line1point2x, ",", line1point2y, ")")
    print("Equation of Line 1: y =", line1slope, 'x + ', line1yint)
    print("Line 2: (", line2point1x, ",", line2point1y, ") and (", line2point2x, ",", line2point2y, ")")
    print("Equation of Line 2  y =", line2slope, 'x + ', line2yint)
    print()
    print("Point of intersection = ( ", intersectx, ",", intersecty, ")")
    print()

    #Creates window with name a nd parameters.
    window = graphics.GraphWin("Intersection Finder", 400, 500)
    window.setCoords(-400, -500, 400, 500)

    #Creates and draws first circle on first line
    circle1line1 = graphics.Circle(graphics.Point(line1point1x, line1point1y), 12.5)
    circle1line1.setOutline("red")
    circle1line1.setFill("red")
    circle1line1.draw(window)

    #Creates and draws second circle on first line.
    circle2line1 = graphics.Circle(graphics.Point(line1point2x, line1point2y), 12.5)
    circle2line1.setOutline("red")
    circle2line1.setFill("red")
    circle2line1.draw(window)

    #Creates and draws first circle on second circle.
    circle1line2 = graphics.Circle(graphics.Point(line2point1x, line2point1y), 12.5)
    circle1line2.setOutline("red")
    circle1line2.setFill("red")
    circle1line2.draw(window)

    #Creates and draws second circle on second line.
    circle2line2 = graphics.Circle(graphics.Point(line2point2x, line2point2y), 12.5)
    circle2line2.setOutline("red")
    circle2line2.setFill("red")
    circle2line2.draw(window)

    #Creates and draws the two lines connecting the circles.
    Line1 = graphics.Line(graphics.Point(line1point1x, line1point1y), graphics.Point(line1point2x, line1point2y))
    Line2 = graphics.Line(graphics.Point(line2point1x, line2point1y), graphics.Point(line2point2x, line2point2y))
    Line1.draw(window)
    Line2.draw(window)

    #Creats and draws the circle at the intersection point.
    circleInt = graphics.Circle(graphics.Point(intersectx, intersecty), 17.5)
    circleInt.setFill("green")
    circleInt.setOutline("green")
    circleInt.draw(window)

    #Displays closing message and prompts the user for a mouse click to close.
    message = graphics.Text(graphics.Point(0, -350), "Click to close.")
    message.draw(window)

    #Waits for mouse input to close the window.
    window.getMouse()
    window.close()

#Calls main()
main()
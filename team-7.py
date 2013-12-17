# Prolog
# Author: David Yurek, Evan Whitmer, Stanley McClister
# Email: dayure2@g.uky.edu
# Section: 012 Team 3
# Oct. 4, 2013
# Lab 7 Team Assignment

from math import *
from graphics import *

# Write the definition of a function called distance
#  with the parameters of 2 points
# which returns the distance between the two points
#  you may NOT use the distance method which exists

def distance (pt1, pt2):

    x1 = pt1.getX()
    y1 = pt1.getY()
    x2 = pt2.getX()
    y2 = pt2.getY()
    d = sqrt((x2-x1)**2 + (y2-y1)**2)

    return d


def herons(s1, s2, s3):

    semi = (s1+s2+s3)/2
    area = sqrt(semi*(semi-s1)*(semi-s2)*(semi-s3))

    return area


def main():


    win = GraphWin("Heron's Formula",500, 500)
    win.setCoords (0,0, 499, 499)
    t = Text(Point(250,480),"Click 3 points")
    t.draw(win)
    p1 = win.getMouse()
    c1 = Circle(p1, 5)
    c1.setFill("red")
    c1.draw(win)
    p2 = win.getMouse()
    c2 = Circle(p2,5)
    c2.setFill("red")
    c2.draw(win)
    p3 = win.getMouse()
    c3 = Circle(p3,5)
    c3.setFill("red")
    c3.draw(win)
    line1 = Line(p1, p2)
    line1.draw(win)
    line2 = Line(p2, p3)
    line2.draw(win)
    line3 = Line(p1, p3)
    line3.draw(win)

    d1 = distance(p1, p2)
    d2 = distance(p2, p3)
    d3 = distance(p1, p3)
    mystr = "The total perimeter is "+str(d1+d2+d3)
    my_area_string = "The area is "+str(herons(d1, d2, d3))
    t2 = Text(Point(250, 20),mystr)
    t2.draw(win)
    Text(Point(250, 100),"click to exit").draw(win)
    Text(Point(250, 40), my_area_string).draw(win)

    win.getMouse()
    win.close()

main()

             
   

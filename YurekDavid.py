# Prolog
# Author: David Yurek
# email: dayure2@g.uky.edu
# Oct. 16, 2013
# Lab Test 1 :: Seat 12

from graphics import *

def main():

    window = GraphWin('Lab Test', 700, 700)
    window.setCoords(0,0,699,699)

    prompt = Text(Point(350,650), 'Click 2 points')
    prompt.setSize(30)
    prompt.draw(window)

    for i in range(3):
        point1 = window.getMouse()
        point2 = window.getMouse()

        rectangle = Rectangle(Point(point1.getX(), point1.getY()), Point(point2.getX(),point2.getY()))
        rectangle.draw(window)

        center = rectangle.getCenter()
        center_line = Line(Point(point1.getX(), center.getY()), Point(point2.getX(),center.getY()))
        center_line.draw(window)

    exit_prompt = Text(Point(350, 50), 'Click to exit')
    exit_prompt.setSize(30)
    exit_prompt.draw(window)

    window.getMouse()
    window.close()

main()

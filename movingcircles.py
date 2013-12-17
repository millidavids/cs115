# Prolog
# Author: David Yurek
# Moving Circles

from graphics import *
from time import sleep
from random import randrange

def main():

    win = GraphWin('Moving Circles', 600, 600)
    win.setCoords(0,0,599,599)

    circle1 = Circle(Point(50, 550), 40)
    circle2 = Circle(Point(550, 550), 40)
    circle3 = Circle(Point(550, 50), 40)
    circle4 = Circle(Point(50, 50), 40)

    circle1.draw(win)
    circle2.draw(win)
    circle3.draw(win)
    circle4.draw(win)

    win.getMouse()

    for cornercircles in range(125):
        circle1.move(4, 0)
        circle2.move(0, -4)
        circle3.move(-4, 0)
        circle4.move(0, 4)
        circle1.setFill(color_rgb(randrange(1,256), randrange(1,256), randrange(1,256)))
        circle2.setFill(color_rgb(randrange(1,256), randrange(1,256), randrange(1,256)))
        circle3.setFill(color_rgb(randrange(1,256), randrange(1,256), randrange(1,256)))
        circle4.setFill(color_rgb(randrange(1,256), randrange(1,256), randrange(1,256)))
        circle1.setOutline(color_rgb(randrange(1,256), randrange(1,256), randrange(1,256)))
        circle2.setOutline(color_rgb(randrange(1,256), randrange(1,256), randrange(1,256)))
        circle3.setOutline(color_rgb(randrange(1,256), randrange(1,256), randrange(1,256)))
        circle4.setOutline(color_rgb(randrange(1,256), randrange(1,256), randrange(1,256)))
        circle1.setWidth(randrange(1,11))
        circle2.setWidth(randrange(1,11))
        circle3.setWidth(randrange(1,11))
        circle4.setWidth(randrange(1,11))
        win.setBackground(color_rgb(randrange(1,256), randrange(1,256), randrange(1,256)))
        sleep(0.001)

    for centercircles in range(125):
        circle1.move(-2, -2)
        circle2.move(-2, 2)
        circle3.move(2, 2)
        circle4.move(2, -2)
        circle1.setFill(color_rgb(randrange(1,256), randrange(1,256), randrange(1,256)))
        circle2.setFill(color_rgb(randrange(1,256), randrange(1,256), randrange(1,256)))
        circle3.setFill(color_rgb(randrange(1,256), randrange(1,256), randrange(1,256)))
        circle4.setFill(color_rgb(randrange(1,256), randrange(1,256), randrange(1,256)))
        circle1.setOutline(color_rgb(randrange(1,256), randrange(1,256), randrange(1,256)))
        circle2.setOutline(color_rgb(randrange(1,256), randrange(1,256), randrange(1,256)))
        circle3.setOutline(color_rgb(randrange(1,256), randrange(1,256), randrange(1,256)))
        circle4.setOutline(color_rgb(randrange(1,256), randrange(1,256), randrange(1,256)))
        circle1.setWidth(randrange(1,11))
        circle2.setWidth(randrange(1,11))
        circle3.setWidth(randrange(1,11))
        circle4.setWidth(randrange(1,11))
        win.setBackground(color_rgb(randrange(1,256), randrange(1,256), randrange(1,256)))
        sleep(0.001)

        cc = 40.0

    for concentriccircles in range(150):
        concentriccir = Circle(circle1.getCenter(), cc+concentriccircles*3)
        concentriccir.draw(win)
        sleep(.0001)

    win.getMouse()
    win.close()

main()

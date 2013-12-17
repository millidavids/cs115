# Prolog
# Author: David Yurek
# Section 12
# Practice Test 1

from graphics import *

def main():
     window = GraphWin('Practice', 700, 700)
     window.setCoords(0,0,699,699)

     prompt_text = Text(Point(350, 650), 'Click a point.')
     prompt_text.draw(window)

     click_point = window.getMouse()

     circle = Circle(Point(click_point.getX()+50, click_point.getY()), 50)
     circle.setFill('red')
     circle.draw(window)

     window.getMouse()
     window.close()


main()

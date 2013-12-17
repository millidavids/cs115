# section 12
# graphics

import graphics

def main():
    
    window = graphics.GraphWin() # constructor
    circle = graphics.Circle(graphics.Point(100, 100), 50)
    circle.setFill("blue")
    circle.setWidth(10)
    print("click to close")
    circle.draw(window)
    window.getMouse()
    window.close()
    
    
main()
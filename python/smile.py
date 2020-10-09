from graphics import *
def main() :
    win = GraphWin()
    face = Circle(Point(100,95), 50)
    lefteye = Circle(Point(80,80), 5)
    lefteye.setFill("yellow")
    lefteye.setOutline("red")
    righteye = Circle(Point(120,80), 5)
    righteye.setFill("yellow")
    righteye.setOutline("red")
    mouth1 = Line(Point(80, 100), Point(100,120))
    mouth2 = Line(Point(100, 120), Point(120,100))
    
    face.draw(win)
    mouth1.draw(win)
    mouth2.draw(win) 
    lefteye.draw(win)
    righteye.draw(win)
    
main()
input()
    
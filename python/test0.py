from graphics import *
def main() :
    p1 = Point(100, 100)
    p1.getX()
    p2 = Point(150, 80)
    win = GraphWin()
    p1.draw(win)
    p2.draw(win)
    
main()
input()
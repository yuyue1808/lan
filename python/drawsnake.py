#第一个小程序 画彩色小蟒蛇
import turtle

def drawsnake(rad, angle, len, neckrad) :
    for i in range(len) :
        turtle.circle(rad, angle)
        turtle.pencolor("red")
        turtle.circle(-rad, angle)
        turtle.pencolor("blue")
    turtle.circle(rad, angle/2)
    turtle.pencolor("yellow")
    turtle.fd(rad)
    turtle.pencolor("green")
    turtle.circle(neckrad+1, 180)
    turtle.pencolor("red")
    turtle.fd(rad*2/3)
    
def main() :
    turtle.setup(1300, 800, 0, 0)
    pythonsize = 30
    turtle.pensize(pythonsize)
    turtle.seth(-40)
    drawsnake(40,80,2,pythonsize/2)#最后一个只是为了最后半圈的半径
    
main()
    
    

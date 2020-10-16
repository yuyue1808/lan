from turtle import *
def main() :
    pensize(10)
    penup()
    goto(0, 0)
    pendown()
    color("yellow")
    begin_fill()
    circle(20, steps = 5)
    color("red")#要在填充中画才能填充
    end_fill()
    penup()
    goto(-60,-100)
    pendown()
    color("green")
    write(("HELLO,WORLD!"), font = ("times",18,"bold"))
    
main()
input()
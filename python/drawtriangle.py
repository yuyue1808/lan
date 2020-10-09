#绘制等边三角形
from turtle import*
def main() :
    setup(500, 500, 0, 0)
    anglesize = 5
    pensize(anglesize)
    pencolor("black")
    seth(0)
    fd(anglesize+100)
    seth(120)
    fd(anglesize+100)
    seth(240)
    fd(anglesize+100)
    
main()
input()

    

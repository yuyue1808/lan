from turtle import *
from datetime import *

#提起画笔，往前走一定距离，然后落下画笔
def Skip(step) :
    penup()
    forward(step)
    pendown()
    
#绘制外表盘
def SetupClock(radius) :#radius为表盘半径长
    reset()
    pensize(7)
    for i in range(60) :
        Skip(radius)
        if i % 5 ==0 :
            forward(20)
            Skip(-radius-20) #回到画盘中心 
        else :
            dot(5)  #原点的直径为5
            Skip(-radius)
        right(6) #画笔右旋6度 
        
#注册表针turtle的形状
def mkHand(name, length) :
    reset()
    Skip(-length*0.1) #稍微变化指针起点
    begin_poly() #开始记录形状
    forward(length*1.1)
    end_poly()  #结束记录形状
    handForm = get_poly()
    register_shape(name, handForm)

def Init() :
    global secHand, minHand, hurHand, printer #建立全局变量
    mode("logo") #重置turtle并朝向北方
    #建立三个表针turtle并初始化    
    mkHand("secHand", 125)
    mkHand("minHand", 130)
    mkHand("hurHand", 90)
    secHand = Turtle()
    secHand.shape("secHand")
    minHand = Turtle()
    minHand.shape("minHand")
    hurHand = Turtle()
    hurHand.shape("hurHand")
    for hand in secHand, minHand, hurHand :#?
        hand.shapesize(1, 1, 3)
        hand.speed(0)
    #建立输出文字turtle
    printer = Turtle()
    printer.hideturtle() #隐藏画笔形状
    printer.penup()

#获得星期几
def Week(t) :
    week = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六","星期日"]
    return week[t.weekday()] 

#获得年月日
def Date(t) :
    y = t.year
    m = t.month
    d = t.day
    return "%s %d %d" %(y, m, d)

#绘制表针的动态显示
def Tick() :
    t = datetime.today() #获得今天的时间
    second = t.second + t.microsecond * 0.000001 #后者为微秒
    minute = t.minute +t.second / 60.0
    hour = t.hour + t.minute / 60.0
    secHand.setheading(6*second) #设置画笔朝向角度
    minHand.setheading(6*minute)
    hurHand.setheading(30*hour)
    
    
    printer.forward(65)
    printer.write(Week(t), align="center", font=("Courier",14,"bold"))
    printer.back(130)
    printer.write(Date(t), align="center", font=("Courier",14,"bold"))
    printer.home()
    
    
    ontimer(Tick, 100) #在100ms后继续调用Tick
    
def main() :
    
    Init()
    SetupClock(160)
    Tick()
    
    mainloop() #不断循环main，直到手动关闭   
main()
    
    
    
    
    
    
            
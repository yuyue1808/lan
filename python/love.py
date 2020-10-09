from turtle import *
from time import *
from pygame import mixer


# 清屏函数
def clear_all():
    penup()
    goto(0, 0)
    color('white')
    pensize(800)
    pendown()
    setheading(0)
    fd(300)
    bk(600)

# 重定位海龟的位置
def go_to(x, y, state):
    pendown() if state else penup()
    goto(x, y)

# 画线
# state为真时海龟回到原点，为假时不回到原来的出发点
def draw_line(length, angle, state):
    pensize(1)
    pendown()
    setheading(angle)
    fd(length)
    bk(length) if state else penup()
    penup()
    
# 画箭羽
def draw_feather(size):
    pensize(5)
    angle = 30                          # 箭的倾角
    feather_num = size//6               # 羽毛的数量
    feather_length = size // 3          # 羽毛的长度
    feather_gap = size//10              # 羽毛的间隔
    
    for i in range(feather_num):
        draw_line(feather_gap, angle+180, False)            # 箭柄，不折返
        draw_line(feather_length, angle + 145, True)        # 羽翼，要折返
    draw_line(feather_length, angle + 145, False)
    draw_line(feather_num*feather_gap, angle, False)
    draw_line(feather_length, angle + 145 + 180, False)
    
    for i in range(feather_num):
        draw_line(feather_gap, angle+180, False)            # 箭柄，不折返
        draw_line(feather_length, angle - 145, True)        # 羽翼，要折返

    draw_line(feather_length, angle - 145, False)
    draw_line(feather_num*feather_gap, angle, False)
    draw_line(feather_length, angle - 145 + 180, False)

# 画爱心
def draw_heart(size):
    color('red', 'pink')
    pensize(8)
    pendown()
    setheading(150)
    begin_fill()
    fd(size)
    circle(size * -3.745, 45)
    circle(size * -1.431, 165)
    left(120)
    circle(size * -1.431, 165)
    circle(size * -3.745, 45)
    fd(size)
    end_fill()

# 画箭
def draw_arrow(size):
    angle = 30
    color('black')
    draw_feather(size)
    pensize(8)
    setheading(angle)
    pendown()
    fd(size*2)

# 一箭穿心
# 箭的头没有画出来，而是用海龟来代替
def arrow_heart(x, y, size):
    go_to(x, y, False)
    draw_heart(size*1.15)
    setheading(-150)
    penup()
    fd(size*2.2)
    draw_heart(size)
    penup()
    setheading(150)
    fd(size * 2.2)
    draw_arrow(size)

# 画出发射爱心的小人
def draw_people(x, y):
    penup()
    goto(x, y)
    pendown()
    pensize(5)
    color('black')
    setheading(0)
    circle(60, 360)
    penup()
    setheading(90)
    fd(75)
    setheading(180)
    fd(20)
    pensize(4)
    pendown()
    circle(2, 360)
    setheading(0)
    penup()
    fd(40)
    pensize(4)
    pendown()
    circle(-2, 360)
    penup()
    goto(x, y)
    setheading(-90)
    pendown()
    fd(20)
    setheading(0)
    fd(35)
    setheading(60)
    fd(10)
    penup()
    goto(x, y)
    setheading(-90)
    pendown()
    fd(40)
    setheading(0)
    fd(35)
    setheading(-60)
    fd(10)
    penup()
    goto(x, y)
    setheading(-90)
    pendown()
    fd(60)
    setheading(-135)
    fd(60)
    bk(60)
    setheading(-45)
    fd(30)
    setheading(-135)
    fd(35)
    penup()
 
# 第一个画面，显示文字
def page0():
    penup()
    goto(-250, 0)
    color('black')
    write('属于我们的', font=('微软雅黑', 50, 'normal'))
    goto(100, 0)
    color('red')
    write('520', font=('Script MT Bold', 60, 'normal'))
    sleep(5)


# 第二个画面，显示发射爱心的小人
def page1():
    speed(8)
    draw_people(-250, 20)
    penup()
    goto(-150, -30)
    draw_heart(14)
    penup()
    goto(-20, -60)
    draw_heart(25)
    penup()
    goto(250, -100)
    draw_heart(45)
    hideturtle()
    sleep(3)

# 最后一个画面，一箭穿心
def page2():
    speed(1)
    penup()
    goto(-130, -250)
    color('yellow')
    pendown()
    write('YY', font=('Script MT Bold', 48, 'normal'))
    penup()
    goto(0, -250)
    color('red')
    pendown()
    write('&', font=('微软雅黑', 50, 'normal'))
    penup()
    goto(100, -250)
    color('blue')
    pendown()
    write('wp', font=('Script MT Bold', 60, 'normal'))

    arrow_heart(20, -60, 51)
    showturtle()

    
#绘制彩虹
def HSB2RGB(hues):
    hues = hues * 3.59 #100转成359范围
    rgb=[0.0,0.0,0.0]
    i = int(hues/60)%6
    f = hues/60 -i
    if i == 0:
        rgb[0] = 1; rgb[1] = f; rgb[2] = 0
    elif i == 1:
        rgb[0] = 1-f; rgb[1] = 1; rgb[2] = 0
    elif i == 2:
        rgb[0] = 0; rgb[1] = 1; rgb[2] = f
    elif i == 3:
        rgb[0] = 0; rgb[1] = 1-f; rgb[2] = 1
    elif i == 4:
        rgb[0] = f; rgb[1] = 0; rgb[2] = 1
    elif i == 5:
        rgb[0] = 1; rgb[1] = 0; rgb[2] = 1-f
    return rgb
     
def rainbow():
    hues = 0.0
    color(1,0,0)
    #绘制彩虹
    hideturtle()
    speed(100)
    pensize(3)
    penup()
    goto(-400,-300)
    pendown()
    right(110)
    for i in range (100):
        circle(1000)
        right(0.13)
        hues = hues + 1
        rgb = HSB2RGB(hues)
        color(rgb[0],rgb[1],rgb[2])    
    penup()

def write_1() :
    goto(155,-50)
    pendown()
    color("blue")
    write("How lucky to meet you",align="center",
          font=("Script MT Bold", 25, "bold"))
    sleep(2)
    penup()
    goto(100,-100)
    pendown()
    color("red")
    write("斯人若彩虹，遇上方知有",align="center",
          font=("Microsoft YaHei", 30, "bold"))
    sleep(2)
    penup()
    goto(160,-134)
    pendown()
    color("yellow")
    write("Darling, I love you!",align="center",
          font=("Script MT Bold", 23, "bold"))
    
def write_2():
    speed(2)
    penup()
    goto(250,260)
    pendown()
    color("black")
    write("THE END",align="center",
          font=("Script MT Bold", 30, "bold"))
    
def main():
    mixer.init()
    mixer.music.load('F:\love520\Taylor Swift - Lover [mqms2].mp3')
    mixer.music.play()
    sleep(14)
    setup(800, 600)
    
    bgcolor((0.8, 0.8, 1.0))
    rainbow()
    write_1()
    sleep(5)
    
    clear_all()
    page0()
    
    clear_all()
    page1()
    
    clear_all()
    page2()
    write_2()
    
    done()
    mixer.music.stop()

main()

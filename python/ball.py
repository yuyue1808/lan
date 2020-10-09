#模拟铅球抛出的运动过程（面向过程的程序设计方法
from math import sin,cos,radians
class project(object) :
    def __init__(self, angel, speed, h0):#没有定义到self里面的变量可以直接使用
        self.x = 0
        self.y = h0
        theta = radians(angel) #弧度角度转换
        self.x_speed = speed * cos(theta)
        self.y_speed = speed * sin(theta)
        
    def update(self, time) :
        self.x = self.x + time * self.x_speed
        y_speed1 = self.y_speed - time * 9.8
        self.y = self.y + time * (self.y_speed + y_speed1) / 2
        self.y_speed = y_speed1
    
    def get_Y(self) :
        return self.y   
    
    def get_X(self) :
        return self.x    

def inputs() :
    angel = eval(input("Please input the angel(°):"))
    speed = eval(input("Please input the speed(m/s):"))
    h0 = eval(input("Please input the h0(m):"))
    time = eval(input("Please input the time interval(s):"))#输入时间间隔
    return angel, speed, h0, time
   
def main() :
    angel1, speed1, h01, time1 = inputs()
    shot = project(angel1, speed1, h01)
    while shot.get_Y() >= 0 :
        shot.update(time1)    
    print("The x result and time = ", shot.get_X())    

main()
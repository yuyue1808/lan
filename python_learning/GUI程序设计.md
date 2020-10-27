## 一、GUI程序设计

### （一）GUI工具包简介

GUI，图形用户界面。由事件驱动，而不是程序流程输出

常用GUI工具包：tkinter, PyQt(均为跨平台windows，安卓等应用)

**tkinter**

由Tk GUI工具包（用于Tcl编程语言）包装而来

```python
from tkinter import Label
windget = Label(None, text='hello')#none表示放在主窗口里面
windget.pack()#打包语句，缺省表示第一行居中
windget.mainloop()#巨大的无限循环，不停等待用户进行操作
```

### （二）GUI编程步骤

**（事件驱动的编程形式）** 

1.安装和导入GUI工具包；

2.创建一个顶层窗口对象，包含整个GUI应用程序；

3.在创建的顶层窗口内部制作GUI应用程序的一些部件（控件、标签、文本框、菜单等等；

4.将GUI部件和应用程序代码结合起来，以事件驱动，并将控件放在窗口合适位置；

5.进入主事件循环

### （三）tkinter模块使用

![image-20201017143211543](C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201017143211543.png) 

#### 1.顶层窗口：tkinter.Tk():

```python
import tkinter
top = tkinter.Tk()
```

#### 2.部件集锦

①Frame: 主窗口里面的框框

②LabelFrame ：类似于Frame

③Label:用于包含文本或者图像

⑦Message：类似label，但显示是多行文本

⑧Text: 多行文本区，用来收集用户输入或向用户显示信息

⑥Entry: **单行的** 文本输入框，用来收集键盘输入

④Buttom: 可以用于鼠标停留或者按下，键盘的活动等操作响应

Radiobutton:一组按钮，每次只能按下其中一个

⑤Checkbuttom：任意个数的一组选框，允许选中多个选项

⑥Entry: **单行的** 文本输入框，用来收集键盘输入



#### 3.部件管理与显示

```
.pack
.grid(row = i, column = j)放置在第i行，第j列  网格管理器  可以使用第0行，如果没有被用则自动不显示
```

```
window.title("hello")
fg前景色，文字的颜色
bg背景，底板颜色
command把部件与方法连接起来
调用主循环，窗口才会被显示出来

需要调用这个类
```

```
frame1= #创建一个框框在窗口下
self.v1和一个变量相关联，关于按键是否被按的状态
```

```
生成一张画布
宽和高以像素为单位
delete清除标签对应的对象

```

```
网格状管理
message多行的文本输出
grid可以跨越多行多列  行的方向跨三行，列跨两列
padx pady上下空五格出来
sticky = E 代表紧贴最东边
```

```
pack打包方式：用于简单窗口布局
fill = both 两边对齐的扩展
place：把部件直接放置到绝对位置（由xy坐标决定，窗口内部区域左上角为原点）
```

### （四）举例

#### 1.贷款计数器

画好布局，确定好布局以及位置，确定管理器采用什么布局方式，是否与成员函数绑定

一般在构造函数里面布局界面，如果是庞大程序，建议使用额外的函数创建界面

![image-20201020160804442](C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201020160804442.png) 

```python
from tkinter import * # Import tkinter
    
class LoanCalculator:
    def __init__(self):
        window = Tk() # Create a window
        window.title("Loan Calculator") # Set title
        
        Label(window, text = "Annual Interest Rate").grid(row = 1, 
            column = 1, sticky = W)
        Label(window, text = "Number of Years").grid(row = 2, 
            column = 1, sticky = W)
        Label(window, text = "Loan Amount").grid(row = 3, 
            column = 1, sticky = W)
        Label(window, text = "Monthly Payment").grid(row = 4, 
            column = 1, sticky = W)
        Label(window, text = "Total Payment").grid(row = 5, 
            column = 1, sticky = W)
        
        self.annualInterestRateVar = StringVar()
        Entry(window, textvariable = self.annualInterestRateVar, 
            justify = RIGHT).grid(row = 1, column = 2)
        self.numberOfYearsVar = StringVar()
        Entry(window, textvariable = self.numberOfYearsVar, 
            justify = RIGHT).grid(row = 2, column = 2)
        self.loanAmountVar = StringVar()
        Entry(window, textvariable = self.loanAmountVar, 
            justify = RIGHT).grid(row = 3, column = 2)
        
        self.monthlyPaymentVar = StringVar()
        lblMonthlyPayment = Label(window, textvariable = 
            self.monthlyPaymentVar).grid(row = 4, column = 2, 
                sticky = E)  #变量是可变的
        self.totalPaymentVar = StringVar()
        lblTotalPayment = Label(window, textvariable = 
            self.totalPaymentVar).grid(row = 5, 
                column = 2, sticky = E)
        btComputePayment = Button(window, text = "Compute Payment", 
            command = self.computePayment).grid(
                row = 6, column = 2, sticky = E)
        
        window.mainloop() # Create an event loop
        
        def computePayment(self):
        monthlyPayment = self.getMonthlyPayment(
            float(self.loanAmountVar.get()), 
            float(self.annualInterestRateVar.get()) / 1200, 
            int(self.numberOfYearsVar.get()))
        self.monthlyPaymentVar.set(format(monthlyPayment, '10.2f'))
        totalPayment = float(self.monthlyPaymentVar.get()) * 12 \
            * int(self.numberOfYearsVar.get())
        self.totalPaymentVar.set(format(totalPayment, '10.2f'))
        
    def getMonthlyPayment(self,
            loanAmount, monthlyInterestRate, numberOfYears):
        monthlyPayment = loanAmount * monthlyInterestRate / (1
           - 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))
        return monthlyPayment;

LoanCalculator()  # Create GUI 



        
```

（数字习惯向右对齐，文字向左对齐）



#### 2.图片显示

图片可以用在按钮上，可以用在单选多选框

<img src="C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201020161824998.png" alt="image-20201020161824998" style="zoom:150%;" />  

```python
from tkinter import * # Import tkinter

class ImageDemo:
    def __init__(self):
        window = Tk() # Create a window
        window.title("Image Demo") # Set title
        
        # Create PhotoImage objects
        caImage = PhotoImage(file = "image/ca.gif")  #主要支持的是GIF文件，将图像文件载入内存， image目录与py文件同目录？？
        chinaImage = PhotoImage(file = "image/china.gif")
        leftImage = PhotoImage(file = "image/left.gif")
        rightImage = PhotoImage(file = "image/right.gif")
        usImage = PhotoImage(file = "image/usIcon.gif")
        ukImage = PhotoImage(file = "image/ukIcon.gif")
        crossImage = PhotoImage(file = "image/x.gif")
        circleImage = PhotoImage(file = "image/o.gif")
        # frame1 to contain label and canvas
        frame1 = Frame(window) 
        frame1.pack()
        Label(frame1, image = caImage).pack(side = LEFT)
        canvas = Canvas(frame1)
        canvas.create_image(90, 50, image = chinaImage)
        canvas["width"] = 200
        canvas["height"] = 100
        canvas.pack(side = LEFT)
        
        # frame2 to contain buttons, check buttons, and radio buttons
        frame2 = Frame(window)
        frame2.pack()
        Button(frame2, image = leftImage).pack(side = LEFT)  
        Button(frame2, image = rightImage).pack(side = LEFT)
        Checkbutton(frame2, image = usImage).pack(side = LEFT)
        Checkbutton(frame2, image = ukImage).pack(side = LEFT)
        Radiobutton(frame2, image = crossImage).pack(side = LEFT)
        Radiobutton(frame2, image = circleImage).pack(side = LEFT)
        
        window.mainloop() # Create an event loop这句话是不能省略的！！！

ImageDemo() # Create GUI 

```

#### 3.菜单设计

#### 4.弹出式菜单

<Button-3>鼠标右键

1左键   2中键

**按右键，然后哪里出菜单（这个超级实用！！！！）** 

#### 5.鼠标输入与键盘输入

将鼠标事件与键盘事件与代码绑定，不同事件有不同定义

#### 6.滚卷条
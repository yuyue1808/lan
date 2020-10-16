## 一、GUI程序设计

### （一）GUI工具包简介

GUI，图形用户界面。由事件驱动，而不是程序流程输出

常用GUI工具包：tkinter, PyQt(均为跨平台windows，安卓等应用)

**tkinter**

```python
from tkinter import Label
windget = Label(None, text='hello')#none表示放在主窗口里面
windget.pack()#打包语句，缺省表示第一行居中
windget.mainloop()#巨大的无限循环，不停等待用户进行操作
```

### （二）GUI编程步骤

1.安装和导入GUI工具包；

2.创建一个顶层窗口对象，包含整个GUI应用程序；

3.在创建的顶层窗口内部制作GUI应用程序的一些部件（控件、标签；

4.将GUI部件和应用程序代码结合起来，以事件驱动，并将控件放在窗口合适位置；

5.进入主事件循环

### （三）tkinter模块使用

#### 1.顶层窗口：tkinter.Tk():

```python
import tkinter
top = tkinter.Tk()
```

#### 2.部件集锦

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
pack打包方式
fill = both 两边对齐的扩展
```


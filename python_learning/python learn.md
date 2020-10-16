[TOC]





跨行字符串    '''hello,

eorls'''

### 字符串的格式化

老方法：采用%的控制符，左侧放置控制符，右侧括号内放置需转换对象具体请看C语言

```python
'%d %s you' % (78, 'hello')
'%10d %s you' % (78, 'hello')#左对齐
'%-10d %s you' % (78, 'hello')#右对齐
```

新方法：**str.format(args, kwargs)**

{0}代表format第一个参数，依次类推，format（）括号里是参数（对类型不要求）。变量类型更加灵活，老方法规定了每个参数必须是什么类型，限制了变量类型的灵活性

```python
>>>'{0}, {1}, {2}'.format('a', 'b', 'c')
'a, b, c'
>>>'{2}, {0}, {1}'.format('b', 'a', 'c')
'c, b, a'
>>>'{}, {}, {}'.format('a', 'b', 'c')
'a, b, c'
>>>'{0}, {1}, {2}'.format(78, 'bhng', 'c')
'78, bhng, c'
>>>'{var1}, {name}, {age}'.format(age=78, var1='bhng', name='c')#给数据项取名字：可以不关心顺序
'bhng, c, 78'
>>>'{var1}, {name}, {age:10d}'.format(age=78, var1='bhng', name='c')#右对齐
'bhng, c,           78'
>>>'{var1}, {name}, {age:<10d}'.format(age=78, var1='bhng', name='c')#左对齐
'bhng, c, 78          '
```



## 四、Python程序流程控制

### if条件语句

if语句不采用大括号表达代码逻辑，而通过控制缩进来控制逻辑，代码可读性更强。（建议往后缩四格）

往右缩：ctrl+]            往左缩：ctrl+[

```python
if <..>:#冒号后面表示后面还有缩进的语句块
    <...>
elif <..>:
    <..>
else:
    <..>
```

**语句逻辑比较符**

| 表达式     | 表达含义           |
| :--------- | ------------------ |
| x is  y    | x, y 是同一对象    |
| x is not y | x,y 不是同一个对象 |
| x in y     |                    |
|            |                    |



### while循环语句

while语句主要是用于条件判断，中可使用if...else去判断是否执行break和continue语句。**注意**如果一开始条件就不成立，else语句块也会被执行。

```python
while <..>:
    <..>
    if condition:
        break#退出while循环
    else:
        continue#继续运行else,与C语言不同
else:
    <..>
```



### for循环语句

for循环主要用于**遍历**任何有序地序列对象内的元素，比如字符串，列表，元祖，字典等（没有怎么搞清楚）

```python
for <target> in <object>:
    <....>
    if condition:
        break
    else:
        continue
else：
    <...>
```

**索引方法**（object）：

1.按元素索引

```python
>>>for x in 'hello':#object类型不受拘束，可枚举对象均可
       print( x )#自动默认换行
h
e
l
l
o
>>>for x in 'hello':
       print( x， end = ' ' )#打印后加空格，不进行换行
>>>for x in range(1,10):#range可迭代对象[1:10),自动生成对象,如果只使用range(1,10)占内存空间十分小
       print( x )
```

2.按位置索引

字符串、列表、元组等有序号对象可使用，字典和集合不可使用

```python
s='hello,world'
for i in range(len(s)):
    print(s[i],i)
```



### 控制语句扩展



break:立刻退出循环，后面部分的else语句都不执行

continue:跳过剩余循环体，开始下一轮循环，**执行else语句吗？？**

pass: pass语句不做任何事，空语句，但在调试程序时大有作用

**常用函数或语句**



```python
>>>a = [2,5,'45']
>>>del a[1]
>>>a
[2, '45']
```



## 五、Python函数

面向过程程序设计最基本的单元，而Python是面向对象（所有数据类型等等）的程序设计语言，但是有时候也要结合面向过程程序设计。

### 函数定义

```python
def 函数名(参数1,参数2,...):#参数类型不需要提前指定
    函数体
    return value #非必须,没有该语句，默认返回值为none
```

只有代码执行完以后，函数才会被定义出来

### 函数参数

**函数参数分类：**

| 参数名称                                             | def表示                           |
| ---------------------------------------------------- | --------------------------------- |
| 位置参数（通过位置对应传递参数）                     | def function(args1, args2, .....) |
| 关键字参数（位置变得不重要）                         | def function(arg=value, ......)   |
| 元组参数（支持可变个数的参数）元组不是不可以变吗？？ | def function(*args1）             |
| 字典参数                                             | def function(**args1)             |



```python
def func(a, b=5, c=10):
    print(a,b,c)

func(3,7)  #a=3,b=7,c=10
func(3,c=24)  #a=3, b=5, c=24   关键字参数
func(c=10,a=10) #a=10, b=5，c=10
```

```python
def total(a=5, *number, **phonebook):
    print("a=",a)
    
    for single_item in number:
        print("single_item", single_item)
    for first_part, second_part in phonebook_item():#？？？？？
        print(first_part, second_part)
        
total(4,8,5,7,9,"hello"=1452,"hell"=1452)#对应类型的位置要排好
```

注意：如果参数是可变类型参数，对其进行修改，如果参数是列表、字典、数组等，函数外面的参数会跟着一起变化。如果参数只是普通变量则不会影响。

### 函数文档字符串

文档字符串（docstring)：在函数定义后紧跟的字符串会被认为是函数的说明文档

可以使用**help（函数名）**显示出来     貌似命令行里面不能写

或者**print(函数名.__doc__)**打印出来

```python
def add():
    "add is a ....function" #这就是一个文档字符串
    
help(add)
print(add.__doc__)
```



### 函数变量作用域

函数体内定义变量只能在该函数中使用，除非使用global或者nonlocal进行修饰



### lambda函数

使用lambda关键字定义匿名函数，适用于在本地小小的用一下

```python
lambda (参数):表达式
>>>g=lambda x:x*2
>>>g(2)
>>>4

>>>(lambda x:x*2)(5) #5是参数
>>>10

Help>lambda????
```

### 常用内置函数

dir将内置函数都屏蔽了，通过以下方式查看

```python
import builtins
dir(builtins)
len(dir(builtins))  #有154个内置函数
```

具体需要什么百度什么 filter

### 函数高级主题

#### 1.函数嵌套（embedded)

应用场合：如果一个函数需要返回一个函数，可以在函数中定义函数或者只在这小块应用时使用

```python
def func(a):
    def func1(b):
        print(a**b)
    return func1#!!!!
        
>>>func(10)(4)
10000
>>>f=func(10)#f变成的一个func1的函数
>>>f(2)
100
```

#### 2.函数递归

函数调用它自己，但是要有停止项，不能无限循环

#### 3.生成器（generator)

yield 生成器????

```python
def f(m):
    n,a,b=
    
    
>>f1（10）调用生成器

>>>for x in fl(10):
    print(x)
```

<<<<<<< HEAD
## 六、面向过程程序设计

略

## 七、面向对象的程序设计

### 类与对象（封装）

#### 1.特点

类与对象的概念与java类似

```python
#关键字：class
#类名：circle
#构造函数：__init__(self, )
#类的特性：self.radius    self表示被调用的对象本身
#类的方法：getarea()
```

math.pi 小圆点实际是范围限定符，可以理解为取对象（调用）

**定义对象：** 

举例：

```python
class Person:
    value = 1 #类变量
    def __init__(self,name): #构造函数
        self.name = name;
    def say_hi(self):
        print("hello,how are you?")
    
    @classmethod  #类方法，不能访问任何对象里面的变量，只能访问类里面的
    def how_many():
        
    
    
p = Person()
print(p)
p.say_hi()
Person.say_hi(p)#需要有个p的self参数

Person.value #访问类变量
p.value

Person.how_many()
```

**self使用原理**

（补充!!!!!!)

查看帮助信息：

help(Person.say_hi)



### 继承与多态

共性与特性，继承共性，多态展现为特性（复制PPT代码）

```python
class 
```

多用set  get，实际是接口不变（主程序不变），变化的只有类，更加灵活

### 高级主题

#### 1.构造方法

旧方法：

新方法：

```python
super(SongBird)
```

#### 2.成员访问

#### 6.类装饰器

作为一个函数，可以接受类作为输入并返回类作为输出



## 




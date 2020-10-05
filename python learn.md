[TOC]



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


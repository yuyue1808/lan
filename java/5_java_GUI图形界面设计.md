# GUI图形界面设计

学gui,画布局

## 一、awt抽象窗口工具包（早期）

> java.awt.*

java提供的用来建立和设置java图形用户界面的基本工具。java.awt包中的所有类都可以用来建立与平台无关的图形用户界面（GUI）的类，这些类又称为组件。awt包提供的工具类主要有组件（Component)、容器（Container)、布局管理器（LayoutManager)。

<img src="C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201116204852035.png" alt="image-20201116204852035" style="zoom:67%;" /> 

### （一）组件（Component)

 Component是大部分图形组件的父类，**尤其注意组件是容器的父类！！！ ** 组件中包含容器、按钮、菜单、文本框、标签、滚动条等。具体怎么用按照所需查看API。

组件放置在容器中需要设定其位置大小，以下是一些共性方法：

<img src="C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201116205501905.png" alt="image-20201116205501905" style="zoom:67%;" /> 

### （二）容器（Container)

大容器套小容器，小容器里面套组件。

• Container是承载其它组件的容器，AWT的顶级容器包括：Applet、Frame、Dialog 

• 只有顶级容器才能显示，其它所有容器 Container及组件Component必须“挂靠” 一个顶级容器，它通过Add()方法来实现 

| 容器名称           | 含义                                                         | 默认布局管理器          |
| ------------------ | ------------------------------------------------------------ | ----------------------- |
| Panel(面板)        | 最简单的容器类，包含在窗口中的一个不带边框的区域，辅助GUI布局 | `FlowLayout` 布局管理器 |
| applet(小应用程序) | applet 是一种不能单独运行但可嵌入在其他应用程序中的小程序。  | `FlowLayout` 布局管理器 |
| Window             | 一个没有边界和菜单栏的顶层窗口                               | BorderLayout布局管理器  |
| Frame（框架）      | 带有标题和边框的顶层窗口                                     | BorderLayout            |
| Dialog（对话框）   | 带标题和边界的顶层窗口                                       | BorderLayout            |

例如：

```java
/*	范例名称：Panel应用举例
 * 	源文件名称：TestFrameWithPanel.java
 *	要  点：
 *		1. Panel组件的性质
 *		2. 容器和组件的概念
 *		3. setSize，setBackground，setLayout，add，setVisible等常用方法
 */

import java.awt.*;

public class TestFrameWithPanel {
	public static void main(String args[]) {
		Frame f = new Frame("MyTest Frame");
		Panel pan = new Panel();
		f.setSize(200, 200);
		f.setBackground(Color.blue);
		f.setLayout(null); // 取消默认布局管理器，采用绝对坐标布局
		pan.setSize(100, 100);
		pan.setBackground(Color.green);
		f.add(pan);//在框架上放一个面板
		f.setVisible(true);// 可视化后才能被显示
	}
}
```



### （三）布局管理器（LayoutManager)

所有的布局管理器都是**Layoutmanager接口**的子类，容器Container类都具有设置布局管理器的 方法。

![image-20201116211455824](C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201116211455824.png) 

**布局管理器的种类：** 

| 种类名称        | 含义                           |
| --------------- | ------------------------------ |
| Flow Layout     | 流式布局，组件从左向右依次排布 |
| Border Layout   | 结构化布局                     |
| Card Layout     |                                |
| Grid Layout     | 网格布局                       |
| Grid Bag Layout | 网格袋布局                     |

#### 1.绝对布局

•setLayout(null);//如果需要按绝对坐标布局， 可以设布局管理器为null 

• 对于需要添加到容器中的component，一定 要调用setBounds()（界限）方法确定具体布局

 • 注意：setBounds()中(x,y)是component<u>左下角</u>的坐标  **？？？** 

<img src="C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201116213538929.png" alt="image-20201116213538929" style="zoom:67%;" /> 

![image-20201116213207966](C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201116213207966.png) 

#### 2.相对布局

即使容器改变了大小，布局管理器也可以自己进行相对应的调整。**注意所有布局方式都是类，使用要用new 对象的方式 ** 

##### ①.流式布局（FlowLayout)

• FlowLayout是流式布局，组件从左向右依 次排布 

• 类似网页的缺省布局，当窗体改变时，组 件布局自动发生调整 

```java

public class FlowLayoutTest {
	public static void main(String[] args) {
		Frame frm = new Frame("Frame with Controls");

		frm.setLayout(new FlowLayout());

		Label lbl = new Label("Here is a label.");
		frm.add(lbl);

		Button btn1 = new Button("Click Me1");
		frm.add(btn1);
		Button btn2 = new Button("Click Me2");
		frm.add(btn2);
		Button btn3 = new Button("Click Me3");
		frm.add(btn3);

		frm.setBounds(0, 0, 400, 300);
		frm.setVisible(true);
	}
}
```

![image-20201116222847555](C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201116222847555.png)  

##### ②.结构化布局(BorderLayout)

![image-20201116223112542](C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201116223112542.png)  

 BorderLayout是结构化布局

 • 加入组件的方法 – add(组件, 加入位置) –

加入位置可為： • BorderLayout.CENTER （EAST,SOUTH,WEST,NORTH)

 ![image-20201116223304928](C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201116223304928.png) 

```java
Frame f;
f = new Frame("Border Layout");
Button bn = new Button("BN");
f.add(bn, "North");
//f.add(bn, BorderLayout.NORTH);
```



## 二、事件监听机制

> java.awt.event.*

事件监听机制，简单来说是加一个监视器monitor到控件上，当控件作出动作时，监视器调用响应的事件处理代码，给予相应的响应。

1）事件源对象
 事件源对象是指触发事件发生的控件。所有的容器组件和元素组件都可以是事件源对象。比如“登录按钮”。

2）事件监听方法 

比如我们的需求是如果当登录按钮被点击的时候，程序会采取相应操作。 
 这就需要我们为事件源对象（登录按钮）添加一个监视器来监视事件源上是否发生了对应的动作。 
 它的作用是捕获发生在事件源对象上的动作，具体由动作来确定。

 3）事件接口及实现（监视器类）

如果我们点击登录按钮后，程序采取相应的动作，我们必须**监听者必须实现ActionLister的<u>接口</u>（一个约定，里面就是事件处理代码）** ，在**actionPerformed**(ActionEvent e)这个方法里定义事件的处理方法，控件发生事件时，就会去调用监听器的方法。

双线程，操作系统（事件委托者）得出事件，然后给jvm虚拟机，虚拟机调用事件处理代码。响应式编程

时间逻辑：

<img src="C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201116224830911.png" alt="image-20201116224830911" style="zoom:67%;" /> 

#### **1.严格使用监视器三部曲 **

举例：

```java
import java.awt.*;
import java.awt.event.*;

public class TestActionEvent {
    public static void main(String args[]) {
			Frame f = new Frame("Test");
			Button b = new Button("Press Me!");
			Monitor bh = new Monitor();//1.定义一个监听器
			b.addActionListener(bh);//2.把这个监听器挂到按钮B上
			f.add(b,BorderLayout.CENTER);
			f.pack();
			f.setVisible(true);
    }
}
/*事件处理代码放在被监听者类的外面*/
class Monitor implements ActionListener { //3.实现事件处理的代码(必须写的接口和方法)
    public void actionPerformed(ActionEvent e) {
        System.out.println("a button has been pressed");    
    }
}
```

![image-20201116225627006](C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201116225627006.png) 

#### 2.利用ActionEvent的方法将事件处理与事件捆绑起来 （鸡肋）

利用事件对象本身传递信息

![image-20201116231604853](C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201116231604853.png) 

ActionEvent方法：

<img src="C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201116231520736.png" alt="image-20201116231520736" style="zoom:67%;" /> 

例如：

```java
/*	范例名称：Java事件处理举例
 * 	源文件名称：TestActionEvent2.java
 *	要  点：
 *  	1. 一个事件源组件上可以同时注册多个监听器
 *		2. 一个监听器对象可以同时注册到多个事件源组件上
 *		3. 事件源的信息可以随它所触发的事件自动传递到所有注册过的监听器
 */

import java.awt.*;
import java.awt.event.*;

public class TestActionEvent2 {
	public static void main(String args[]) {
		Frame f = new Frame("Test");
		Button b1 = new Button("Start");
		Button b2 = new Button("Stop");
		Monitor2 bh = new Monitor2();
		b1.addActionListener(bh);
		b2.addActionListener(bh);//一个监视器检测两个控件
		b2.setActionCommand("game over");//设置事件处理
		f.add(b1, "North");
		f.add(b2, "Center");
		f.pack();
		f.setVisible(true);
	}
}

class Monitor2 implements ActionListener {
	public void actionPerformed(ActionEvent e) {
		System.out.println("a button has been pressed," + "the relative info is:\n " + e.getActionCommand());//捕捉事件处理代码
	}
}
```

<img src="C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201116232243320.png" alt="image-20201116232243320" style="zoom:67%;" /> 



#### 3.利用Event的get.Sourse()的方法（鸡肋）

 所有event的父类拥有一个getSource()方法， 返回事件发生的对象(Object类型) 

<img src="C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201116232839756.png" alt="image-20201116232839756"  />  

```java
import java.awt.*;
import java.awt.event.*;
public class TestActionEvent3 {
    public static void main(String args[]) {
			Frame f = new Frame("Test");
			Button b1 = new Button("Start");//事件的标签在这里！！
			Button b2 = new Button("Stop");
			Monitor2 bh = new Monitor2();
			b1.addActionListener(bh);       
			b2.addActionListener(bh);
			f.add(b1,"North");       
			f.add(b2,"Center");	
			f.pack();        		
			f.setVisible(true);
    }
}

class Monitor2 implements ActionListener {
    public void actionPerformed(ActionEvent e) {
		Button b = (Button)e.getSource();//返回发生事件的控件
    	System.out.println("a button has been pressed," + 
    	"the relative info is:\n " + b.getLabel());  //读取事件的标签  
	}
}
```

<img src="C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201116233039057.png" alt="image-20201116233039057" style="zoom:67%;" /> 

#### 4.通过构造方法传递或者使用内部类（GOOD!）

事件类event和事件类getSource都不足以提供全部信息该如何？ 

①.通过构造方法传递

事件监听类的接口方法我们不能改变，但 可以改变其构造函数，通过构造函数传参 数 。



②.



参数传递

setSourse()抓住了按钮



1.为了一个类里面的属性能被另外一个类访问，放在肚子里  内部类


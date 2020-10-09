[TOC]



## 一、JAVA简介

Java是基于JVM虚拟机（高低版本完美兼容）的跨平台语言，可移植性极佳；介于编译型语言和解释型语言之间，将代码编译成一种“字节码”，它类似于抽象的CPU指令

## 二、JAVA快速入门

### 1.名词解释

## 三、面向对象程序设计

面向对象主要是关注对象的属性与方法，定义好相关对象，具体的对象正在做什么事情的流程，我们不予关注，唯一能做的只能控制时间与重置。“我们是创世者，但是七天后就得走，且不干预人间任何事情。” 面向过程语言如C语言，不存在对象概念，主要是控制目标实现的的每一个步骤，每一个步骤都是可操控的。

面向对象的程序设计有3个主要特征：封装性、继承性、多态性。学习主要是需要形成自己的程序时空观。

### （一）封装性

封装是为了有效描述对象，更简单的理解是将代码有效分隔，有利于程序员阅读与代码debug修改 。“高类聚，低耦合”，将对象的属性与方法封装在一起，定义为一个程序单位(class)，其访问权限可人为定义。 

#### 1.类与对象

类是一种结构定义，而对象是类的载体，一个类可以创造多种对象，两者不可以分割。

##### a.类（class）

类是由属性和方法组成。属性为类中包含的一些变量的定义，而方法是该类的一些操作行为。例如：

```java
/*定义了蜜蜂的类*/
public class Bee00{
	int id;		//蜜蜂的唯一标识
	int x,y;	//蜜蜂现在所处的位置坐标(最小单位：像素)
	int honey;	//当前蜜蜂采集蜂蜜的数量(单位：mg)
//以上三个变量为蜜蜂的属性
//以下为定义的蜜蜂的显示当前采蜜数方法（注意：存在返回值）
	public void showHoney()
	{
		System.out.println("Bee: "+id+" has ("+honey+"mg) honey ");
	}
	
```

##### b.类的构造方法

在类中存在类的同名方法，叫做类的构造方法。只要是类，必须存在构造方法。用于类的生（初始化） 

<u>注意：构造方法是没有返回值的，因为在创建对象，实例化对象时需要将返回对象的全部内容？？</u>

```java
public class Bee00{
	int id;		//蜜蜂的唯一标识
	int x,y;	//蜜蜂现在所处的位置坐标(最小单位：像素)
	int honey;	//当前蜜蜂采集蜂蜜的数量(单位：mg)
	
    public Bee00(int id,int x,int y)
    {   
		this.id = id;//this调用的是当前类，这句意为传入参数的id赋值给这个类的id初值
		this.x = x;
		this.y = y;
		this.honey = 0;
		System.out.println("Bee: "+id+" come from ("+x+","+y+")");
    }

```

**this关键字**

this表示当前对象，可以使用this调用本类的构造方法，具体见上。

##### c.对象创建及其实例化

通过new关键字对对象进行实例化

```java
public class Bee00{
	int id;		//蜜蜂的唯一标识
	int x,y;	//蜜蜂现在所处的位置坐标(最小单位：像素)
	int honey;	//当前蜜蜂采集蜂蜜的数量(单位：mg)
	
    public Bee00(int id,int x,int y)
    {   
		this.id = id;
		this.x = x;
		this.y = y;
		this.honey = 0;
		System.out.println("Bee: "+id+" come from ("+x+","+y+")");
    }
	
	public static void main(String[] args)//实例化在class中实现，参数为字符串类型的数组
	{
		Bee00 bee1 = new Bee00(1,50,50);//在主程序中实例化对象，声明对象名为bee1，然后调用构造方法(传递参数进去)进行实例化
		Bee00 bee2 = new Bee00(2,100,100);
	}
}
```

其对象通过操作句柄操作，具体内存映像为下图

![image-20201004081958302](C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201004081958302.png)

我们可调用的只有句柄，对象是无法直接调用的，句柄对应于对象的声明名字。句柄存储在栈中，而对象的属性存储在堆中，而方法在堆栈之外的其他内存（栈内存小，调用速度快；堆内存大，调用速度慢）

**调用方法：（属性）bee1.id    bee2.X     （方法）bee1.showhoney()**

当单纯打印句柄时，其返回值仅为句柄在栈中的地址。对象实例化称为对象的“生”，如果其句柄不再指向该对象对应的空间，这就称为对象的“死”。



### （二）继承性

#### 1.基本概念

继承的目的是为了条理清晰地代码重用 ，继承后子类拥有父类的结构、属性与方法。**值得注意：在实际内存中，父类并不存在，只存在子类的内存空间！！！** 

**继承方法：**

```java
class 父类{}
class 子类 extends 父类{}

class Bee{//父类：Bee,定义了采蜜容量，与采蜜的方法
	int honeyBag = 5;
	public void pickHoney(){
		honeyBag ++;
	}	
}

public class Ext1 extends Bee{//public表示访问权限
	public static void main(String[] args)
	{		
		//Bee b = new Bee();对父类实例化
		Ext1 e = new Ext1();//实际上一般只对子类实例化		
		e.pickHoney();//子类也拥有的父类的方法
		e.pickHoney();
		e.pickHoney();
		System.out.println("Mikee bee has "+e.honeyBag+" kg honey");
	}
}
```

**访问权限修饰符：**

访问权限大小关系：private<default<public

如果父类为private，子类将无法继承；如果父类为public，子类也必须为public，不然无法进行编译。

#### 2.方法覆盖与方法重载

方法覆盖要考虑权限，子类权限不能小于父类权限。另外子类方法一旦覆盖父类，每次**在主程序**调用**子类句柄** 使用子类方法。但是在子类中仍可以使用super.父类方法名称();调用父类的方法。

```java
class Bee{
	int honeyBag = 0;
	public void pickHoney(){
		honeyBag ++;
	}	
}

public class Ext2 extends Bee{
	public void pickHoney(){
		honeyBag += 5;
	}

	public static void main(String[] args)
	{
		Ext2 e = new Ext2();
		e.pickHoney();//此时调用采蜜方法，其为每次加5，子类覆盖了父类的方法
		e.pickHoney();
		e.pickHoney();
		System.out.println("Mikee bee has "+b.honeyBag+" kg honey");
	}
}
```

方法重载即可使用同名方法，但是参数不同，虚拟机会根据传递参数的不同选用不同的方法进行调用。

#### 3.属性覆盖

如果子类声明了和父类同名的属性，子类属性不会覆盖父类属性，而是同时存在两类属性。调用this，即为调用子类属性；调用父类属性通过使用super关键字。 

```java
  class Father{
	int speed;
	public Father(int speed){
		this.speed = speed;
	}

	public void run(){
		System.out.println("Father run "+speed+" km/h");
	}

}

class Son extends Father{
	int speed;
	public Son(int speed){
		super(speed-5);//设定父亲的speed，父亲比儿子速度慢5km/h
		this.speed = speed;//设定自己的speed
	}

	public void run(){
		//super.run();//打印父亲跑的信息(通过调用父类的方法)
		System.out.println("Father run "+super.speed+" km/h");//通过调用父类的属性
		System.out.println("Son run "+speed+" km/h");
	}

}

public class Job2{
	public static void main(String[] args) {
		Son s = new Son(30);
		s.run();
	}
}
```

**super关键字：**

 <font color=red >和this一样，调用父类的构造方法时要放在子类构造方法的第一句</font> 因为子类不会继承父类的构造方法，子类默认的构造方法是编译器自动生成的，不是继承的。如果没有写，编译器会在子类构造方法第一行加上super（）；如果父类有参数，则编译不会通过。因此需先调用父类的构造方法，使用**super（参数）；** 

| 使用super情景                    | 调用方法                   |
| -------------------------------- | -------------------------- |
| 在子类构造方法中调用父类构造方法 | super(父类构造方法参数)；  |
| 在子类中使用父类属性             | super.父类属性名称         |
| 在子类中调用父类的方法           | super.父类方法名称(参数)； |



#### 4.抽象方法

抽象方法只需声明(使用abstract关键字），而不需要实现。（一个子类只能继承一个抽象方法）抽象类必须被子类继承，且子类必须复写抽象类中的全部抽象方法。**注：抽象方法不能使用private声明，否则子类无法覆盖**

**可以包含非抽象方法！！！**                         

```java
abstract class 抽象类名称{
    属性;
    访问权限 返回值类型 方法名称(参数){//普通方法
        return 返回值;
    }
    访问权限 abstract 返回值类型 方法名称(参数); //抽象方法，没有方法体
}

abstract class Bee{
	int honeyBag = 0;
	public abstract void pickHoney();//抽象方法
}

class Honee extends Bee{
	public void pickHoney()
	{
		honeyBag +=1;
	}
}

class Mikee extends Bee{
	public void pickHoney()
	{
		honeyBag +=5;
	}
}

public class Ext4{
	public static void main(String[] args)
	{
		Honee h = new Honee();
		Mikee m = new Mikee();
		h.pickHoney();
		m.pickHoney();
		System.out.println("Honee has "+h.honeyBag+"kg and Mikee has "+m.honeyBag+"kg");
	}
}
```

#### 5.接口

接口是一种特殊的类，里面全部是由全局常量和公共的抽象方法所组成。**不允许有非抽象方法出现！！！** 接口中的访问权限无论写还是不写，都是public。接口就像干爹，可以认很多歌，而父类只能认一个。

```java
interface 接口名称{
    全局变量;
    抽象方法;
}
class 子类 implements 接口A,接口B{
    
}

public interface Runable
{
	public void run();
}
class People implements Runable{
	public void run(){
		System.out.println("People run……");
	}
}

class Dog implements Runable{
	public void run(){
		System.out.println("Dog run……");
	}
}

public class Interf1{
	public void run(Runable r){
		r.run();
	}

	public static void main(String[] args)
	{
		People p = new People();
		Dog d = new Dog();
		p.run();
		d.run();
		Interf1 f = new Interf1();
		f.run(d);
	}
}
```

**final关键字**

• final修饰的类，不能被继承 

• final修饰的属性，是常量 

• final修饰的方法，不能被覆盖（final关键字断子绝孙）
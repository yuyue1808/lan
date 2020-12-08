# 网络编程

## 一、基本知识

 • IPv4地址：是一个32位的整数，通常以4个255以内的数字表示（X.X.X.X），用于唯一标识网络中的硬件设备

 • 域名：为方便记忆和使用，用类似www.XXX.com 的字符串代替IP地址输入，靠DNS服务进行解析 localhost 127.0.0.1

 • 端口号：是一个标记机器的逻辑通信信道数。端 口号是用一个16位的整数来表达的，其范围为0 ～65535，其中0～1023为系统所保留。 （和《计算机网络》连接在一起咯）



​        使用Java进行网络编程时，由jvm虚拟机实现了底层复杂的网络协议，Java程序只需要调用Java标准库提供的**接口** ，就可以简单高效地编写网络程序。

**补充：InetAddress地址类**

>java.net.*

<img src="C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201121203126626.png" alt="image-20201121203126626" style="zoom:67%;" /> 

方法摘要：

<img src="C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201121203251510.png" alt="image-20201121203251510" style="zoom:67%;" /> 

例如：

<img src="C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201121203312080.png" alt="image-20201121203312080" style="zoom:67%;" /> 

```java
import java.net.*;

public class WhoAmI {
  public static void main(String[] args) 
      throws Exception {
    if(args.length != 1) {
      System.err.println(
        "Usage: WhoAmI MachineName");
      System.exit(1);
    }
    InetAddress a = InetAddress.getByName(args[0]);//通过主机名获得IP地址
    System.out.println(a);
	System.out.println(a.getHostName());//获取地址对象的主机名
  }
}
```

<img src="C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201121203907101.png" alt="image-20201121203907101" style="zoom:67%;" /> 



## 二、TCP编程

### （一）基本概念

TCP协议工作于传输层，是端到端的连接通信。TCP协议面向连接，具有可靠性和有序性，并且以字节流的方式发送数据，通常被称为流通信协议。(以下主要介绍服务器和客户端模式)

在Java中，基于TCP协议实现网络通信的类有两个：在客户端的Socket类与在服务器端的ServerSocket类

<img src="C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201121204654841.png" alt="image-20201121204654841" style="zoom:67%;" /> 

### （二）ServerSocket类

> java.net.*

服务于服务器端。ServerSocket的作用是等待网络连接请求，并构造本地Socket与远程Socket通信。

ServerSocket只监听本地端口，通过accept()方法等待接入要求，在没有接入要求时，程序处于阻塞状态，不会往下执行。一旦有连入者，连接生成Socket.

构造方法：

<img src="C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201121205510559.png" alt="image-20201121205510559" style="zoom:67%;" /> 

<img src="C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201121205708580.png" alt="image-20201121205708580" style="zoom:67%;" /> 

方法：

<img src="C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201121205542749.png" alt="image-20201121205542749" style="zoom:67%;" /> 

<img src="C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201121205442571.png" alt="image-20201121205442571" style="zoom:67%;" /> 



### （三）套接字Socket

> java.net.*

套接字Socket类服务于客户端。

构造方法：

<img src="C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201121210031237.png" alt="image-20201121210031237" style="zoom:67%;" /> 

方法：

<img src="C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201121210228712.png" alt="image-20201121210228712" style="zoom:67%;" /> 

注：Socket生成输入输出流（全双工通信），均需异常处理

<img src="C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201121210652239.png" alt="image-20201121210652239" style="zoom:67%;" /> 

**out.println()表示将信息输出到服务器**

例如：

```java
/*服务器代码*/
import java.io.*;
import java.net.*;

public class NetServer {
	public static final int PORT = 8080;

	public static void main(String[] args) throws IOException {
		InetAddress addr = InetAddress.getByName("localhost");// 获得本地IP地址

		ServerSocket s = new ServerSocket(PORT, 10, addr);// 建立一个可连接的服务
		System.out.println("虚拟Web服务器启动: " + s);
		try {
			while (true) {//服务器一直在循环
				Socket socket = s.accept();// 等待连接
				try {
					System.out.println("接受客户端连接请求: " + socket);// 只能为当前客户端提供服务
					BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));

					PrintWriter out = new PrintWriter(
							new BufferedWriter(new OutputStreamWriter(socket.getOutputStream())), true);
					String str = in.readLine();//读取
					System.out.println("收到: " + str);
					while (str != null && !str.equals("END")) {// 收到end就跳出循环
						str = in.readLine();
						System.out.println("收到: " + str);
					}
					out.println("客户端传送信息服务器已经接收完毕");//将信息发给客户端

					System.out.println("此次服务完毕，开始下轮监听");

				} finally {
					System.out.println("Socket关闭...");
					socket.close();//关闭Socket套接字
				}
			} // end while
		} finally {
			s.close();// 关闭ServerSocket套接字
		}
	}
}

/*客户端代码*/
import java.io.*;
import java.net.*;

public class NetClient {
	public static final int PORT = 8080;

	public static void main(String[] args) throws IOException {

		InetAddress addr = InetAddress.getByName("localhost");

		Socket socket = new Socket(addr, PORT);

		try {
			System.out.println("客户端请求: " + socket);

			BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));

			PrintWriter out = new PrintWriter(new BufferedWriter(new OutputStreamWriter(socket.getOutputStream())),
					true);
			out.println("我想获得一些信息");//将信息发给服务端
			out.println("END");
			String str;
			System.out.println("客户端请求发送完毕...");
			while ((str = in.readLine()).length() != 0) {
				System.out.println("接收: " + str);
			}
		} finally

		{
			System.out.println("客户端关闭...");
			socket.close();
		}
	}
}
```

<img src="C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201121214734424.png" alt="image-20201121214734424" style="zoom:67%;" /> 

<img src="C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201121214755423.png" alt="image-20201121214755423" style="zoom:67%;" /> 

```java
/*服务器 扩展板*/
            String str = in.readLine();//读套接字里面的信息
				byte[] input = new byte[20];
				int i = 0;
				System.out.println("收到" + (++i) + "条: " + str);
				while (str != null && !str.equals("END")) {
					// System.in.read(input);
					str = in.readLine();//如果没有这个读取，服务器端就一直无法跳出这个循环，而且要现收后打印
					System.out.println("收到" + (++i) + "条: " + str);
				}
/*客户端*/
	for (int i = 0; i < 20; i++) {
				out.println("我想获得一些信息");
			}
//说明是全双工通信，服务器接收与客户端发送的频率差不多，那边发的这边能准确接收到，通过Socket的输入输出流
```

<img src="C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201121221346643.png" alt="image-20201121221346643" style="zoom: 50%;" />  

<img src="C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201121221233895.png" alt="image-20201121221233895" style="zoom: 50%;" /> 

<img src="C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201127224231091.png" alt="image-20201127224231091" style="zoom: 67%;" />  



## 三、UDP编程

### （一）基本概念

 UDP是一种无连接的传输协议。

 – 首先需要将要传输的数据定义成一个**数据传输单元**  

– 在数据报中指明数据所要达到的主机地址和端口号 

– 将数据传输单元发送出去

 – 这与通过邮局发送邮件的情形非常相似。

 • 这种传输方式是无序的，也不能确保绝对的安全可靠，但 它很**简单**也具有比较**高的效率** 。 

 在Java中，基于UDP协议实现网络通信的类有两个： 

– 用于进行端到端通信的类 • **DatagramSocket ** （数据报套接字）服务于服务器

– 用于表达通信数据的数据报类 •  **DatagramPacket**     （数据报文）服务于客户端

<img src="C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201127225550272.png" alt="image-20201127225550272" style="zoom:67%;" /> 



### （二）DatagramSocket类

> java.net.*

服务于服务器端。DatagramSocket的作用是发送和接收数据报包的套接字。数据报套接字是包投递服务的发送或接收点。每个在数据报套接字上发送或接收的包都是单独编址和路由的。从一台机器发送到另一台机器的多个包可能选择不同的路由，也可能按不同的顺序到达。

用 UDP 广播发送。为了接收广播包，应该将 DatagramSocket 绑定到通配符地址。

**构造方法：**

 <img src="C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201127232247657.png" alt="image-20201127232247657" style="zoom:67%;" /> 

<img src="C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201127232322840.png" alt="image-20201127232322840" style="zoom:67%;" /> 

**方法：** 

 <img src="C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201127234105040.png" alt="image-20201127234105040" style="zoom:67%;" /> 

 

### （三）DatagramPacket类

> java.net.*

此类表示数据报包。 

数据报包用来实现**无连接** 包投递服务。每条报文仅根据该包中包含的信息从一台机器路由到另一台机器。从一台机器发送到另一台机器的多个包可能选择不同的路由，也可能按不同的顺序到达。不对包投递做出保证。

**构造方法：**

 <img src="C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201127233817414.png" alt="image-20201127233817414" style="zoom:67%;" /> 

<img src="C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201127233844073.png" alt="image-20201127233844073" style="zoom:67%;" /> 

<img src="C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201127233921271.png" alt="image-20201127233921271" style="zoom:67%;" /> 

**方法：** 

 <img src="C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201127234140975.png" alt="image-20201127234140975" style="zoom:67%;" /> 

还有对应的set部分



### （四）通信流程

**1.定义数据成员   **   

   DatagramSocket socket;    

   DatagramPacket packet;    

   InetAddress address;   (用来存放接收方的地址)    

   int port;       (用来存放接收方的端口号) 

**2.创建数据报文Socket对象**      

try {            

​        socket=new DatagramSocket(1111);     

}catch(java.net.SocketException e) {……} 

socket 绑定到一个本地的可用端口,等待接收客户的请求. 

**3.分配并填写数据缓冲区**(一个字节类型的数组)    

 byte[] Buf=new byte[256];     

 存放从客户端接收的请求信息. 

**4.创建一个DatagramPacket**     

​     packet=new DatagramPacket(buf, 256);

​    用来从socket接收数据,它只有两个参数 

**5.服务器阻塞 **     

   socket.receive(packet);   

   在客户的请求报道来之前一直等待

**6.从到来的包中得到地址和端口号**      

​    InetAddress address=packet.getAddress();    

​    int port=packet.getPort(); 

**7.将数据送入缓冲区 **  

   或来自文件,或键盘输入 

**8.建立报文包,用来从socket上发送信息**  

​     packet=new DatagramPacket (buf,buf.length, address, port); 

**9.发送数据包**   **10.关闭socket** 

​      socket.send(packet);   socket.close(); 

```java
/*服务端*/
import java.io.*;
import java.net.*;
import java.util.*; 

public class UDPServer
{
	public static final int PORT =8081;
	public static void main(String[] args) throws IOException
	{
		//建立数据报Socket
		InetAddress addr = InetAddress.getByName("localhost");
		DatagramSocket ds =new DatagramSocket(PORT);
		System.out.println("UDP服务器启动: "+ds);
		//建立接收数据报		
		byte[] buf = new byte[1000];
		DatagramPacket inDataPacket = new DatagramPacket(buf, buf.length);				
		try{			
			while(true) {
			    //等待数据报的到来
				ds.receive(inDataPacket);
				//显示接收的数据报
				String str = new String(inDataPacket.getData(), 0, inDataPacket.getLength());
				String rcvd = str +", from address: " + inDataPacket.getAddress() +", port: " + inDataPacket.getPort();
				System.out.println(rcvd);
				//回应数据报
				String echoString = "Echoed: " + rcvd;        
				DatagramPacket outDataPacket = new DatagramPacket(echoString.getBytes(),echoString.length(),
														inDataPacket.getAddress(), inDataPacket.getPort());
				ds.send(outDataPacket);			
			}
		}catch(SocketException e){
			System.err.println("Can't open socket");
			System.exit(1);
		}catch(IOException e){
			System.err.println("Communication error");
			e.printStackTrace();
		}finally{
			ds.close();
		}
	}
}							

/*客户端*/
import java.io.*;
import java.net.*;

public class UDPClient
{	
	public static final int PORT =8081;
	public static void main(String[] args) throws IOException
	{		
		//
		InetAddress addr = InetAddress.getByName("localhost");
		DatagramSocket datagramSocket = new DatagramSocket();
		//
		byte[] msg = new byte[100];
		DatagramPacket inDataPacket = new DatagramPacket(msg, msg.length); 
		//
		DatagramPacket outDataPacket; 
		String strSend = "udp request";
		outDataPacket = new DatagramPacket(strSend.getBytes(), strSend.length(), addr, PORT); 
		datagramSocket.send(outDataPacket); 
		//		
	  	datagramSocket.receive(inDataPacket); 
		String receivedMsg = new String (inDataPacket.getData(), 0, inDataPacket.getLength()); 
		System.out.println(receivedMsg); 
		datagramSocket.close(); 

	}
}	
```

<img src="C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201127234944456.png" alt="image-20201127234944456" style="zoom:67%;" /> 

<img src="C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201127234959673.png" alt="image-20201127234959673" style="zoom:67%;" /> 

服务器/客户机无本质差异，我们一般让服 务器while循环



```java
import java.net.*;

public class WhoAmI {
  public static void main(String[] args) throws Exception {
    if (args.length != 1) {
      System.err.println("Usage: WhoAmI MachineName");
      System.exit(1);//非正常退出，异常中止
    }
    InetAddress a = InetAddress.getByName(args[0]);
    System.out.println(a);
    System.out.println(a.getHostName());
  }
}
```

<img src="C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201127234441300.png" alt="image-20201127234441300" style="zoom:67%;" /> 
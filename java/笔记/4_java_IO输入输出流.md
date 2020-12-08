# IO输入输出

[TOC]



> java.io

IO即输入输出，input指从外部（如磁盘）读入数据到内存，以java提供的某种数据类型储存，比如byte,string,; ouput指从内存输出到外部。只有把数据读入内存才能被处理，因为代码存储在内存中，数据也必须读到内存里。

IO流是一种顺序读写数据的模式，单向流动。数据类似于水在水管中流动，所以称为IO流。

## 一、File文件处理

输入输出离不开文件的读写处理。

### （一）File类

> java.io.File

#### 1.构造File对象

构造方法：

![image-20201111182804851](C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201111182804851.png) 

例如：

实例File类的对象：

```java
File f = new File("F:\\lan\\git\\java\\4_java_IO输入输出流.md");
```

**注意：** Windows系统下路径必须用"\ \ "代替"\ "; Linux平台使用"/"作为路径分隔符

由于不同操作系统的差异性，最好使用separator静态变量来表示当前系统的分隔符

```java
File f = new File("F:"+File.separator+"test.txt");
```

**区分绝对路径、相对路径与规范路径**

| 路径名称 | 含义                                          | 举例                                                         | 方法                                                         |
| -------- | --------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 绝对路径 | 以根目录开头的完整路径                        | F:\\lan\\git\\java\\4_java_IO输入输出流.md                   | getPath()/getAbsolutePath()                                  |
| 相对路径 | 相对路径是省去的当前目录的路径                | ![image-20201111184736063](C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201111184736063.png) |                                                              |
| 规范路径 | 规范路径是把.和..转换成标准的绝对路径后的路径 | ![image-20201111185331542](C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201111185331542.png) | getCanonicalPath()注意：这个方法进行了异常处理，使用时必须加try..catch |

### （二）类的方法

File对象即可以表示文件，也可以表示目录。构造一个`File`对象，即使传入的文件或目录不存在，代码也不会出错，因为构造一个`File`对象，并不会导致任何磁盘操作。只有当我们调用`File`对象的某些方法的时候，才真正进行磁盘操作。

判断是文件还是目录的方法：

![image-20201111185734314](C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201111185734314.png) 



#### 1.当File对象表示文件时

![image-20201111192746282](C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201111192746282.png) 

**a.** 获取文件权限和大小

<img src="C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201111190008752.png" alt="image-20201111190008752" style="zoom:67%;" />  

<img src="C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201111190033528.png" alt="image-20201111190033528" style="zoom:67%;" />   

**b.**创建和删除文件

<img src="C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201111191616618.png" alt="image-20201111191616618" style="zoom:67%;" /> 

<img src="C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201111191630625.png" alt="image-20201111191630625" style="zoom:67%;" /> 

注意：使用createNewFile()创建新文件时，由于内含关键字throws，所以必须进行异常处理（异常类：IOException）。

创建临时文件与程序运行后删除：

<img src="C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201111191932109.png" alt="image-20201111191932109" style="zoom:67%;" /> 

<img src="C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201111191954782.png" alt="image-20201111191954782" style="zoom:67%;" /> 

```java
File f = File.createTempFile("tmp-", ".txt"); // 提供临时文件的前缀和后缀
f.deleteOnExit(); // JVM退出时自动删除，但是程序运行过程中这个文件是存在的
```

**c.**压缩文件

 压缩实现在java.util.zip.*; 

• 核心的类GZIPOutputStream插在File和Buffered 之间 GZIPOutputStream

```java
import java.io.*;
import java.util.zip.*;

public class GZIPcompress {
  public static void main(String[] args) {
    try {
      BufferedReader in =
        new BufferedReader(
          new FileReader(args[0]));
      BufferedOutputStream out =
        new BufferedOutputStream(
          new GZIPOutputStream(
            new FileOutputStream("test.gz")));
      System.out.println("Writing file");
      int c;
      while((c = in.read()) != -1)
        out.write(c);
      in.close();
      out.close();
      System.out.println("Reading file");
      BufferedReader in2 =
        new BufferedReader(
          new InputStreamReader(
            new GZIPInputStream(
              new FileInputStream("test.gz"))));
      String s;
      while((s = in2.readLine()) != null)
        System.out.println(s);
    } catch(Exception e) {
      e.printStackTrace();
    }
  }
}


```



#### 2.当File对象表示目录时

目录可以理解成文件夹

**a.**创建和删除目录

<img src="C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201111193010356.png" alt="image-20201111193010356" style="zoom:67%;" /> 

<img src="C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201111193040376.png" alt="image-20201111193040376" style="zoom:67%;" />  

**b.**遍历目录里面的子目录和文件

<img src="C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201111193113120.png" alt="image-20201111193113120" style="zoom:67%;" />  

方法一：使用list()

列出完整的名称，返回一个字符串数组，再把这个字符串数组遍历出来

```java
import java.io.*;

public class AllFiles{ 
	public static void main(String args[]){ 
		File files=new File(".");//表示当前目录
		String strFiles[]=files.list();
		for(int i=0;i<strFiles.length;i++){
            File files[]=strFiles[i];
			System.out.print(strFiles[i]);
}
```

<img src="C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201111200010286.png" alt="image-20201111200010286" style="zoom:67%;" /> 

方法二：使用listFiles()列出完整的路径，返回一个File对象数组

```java
import java.io.*;

public class AllFiles{ 
	public static void main(String args[]){ 
		File files=new File(".");//表示当前目录
		File files[]=files.listFiles();
		for(int i=0;i<files.length;i++){ 
			System.out.print(files[i]);
}
```

<img src="C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201111200118721.png" alt="image-20201111200118721" style="zoom:67%;" /> 

（更多的实用方法请看API文件）

## 二、字节输入输出流（byte)

<font color=red size=5 face="SentyZHAO 新蒂赵孟頫">**InputStream /OuputStream**"</font>

inputstream/outputstream都是最大的父类，自身为**抽象类** ，使用时必须通过子类实例化对象。以下重点将input，output类比就行惹

### （一）自身：InputStream

> java.io.InputStream

<img src="C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201111204838307.png" alt="image-20201111204838307" style="zoom:67%;" /> 

<img src="C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201111204712562.png" alt="image-20201111204712562" style="zoom:67%;" /> 

在使用后，都需要使用以下方法，关闭数据流，释放资源

<img src="C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201111205708665.png" alt="image-20201111205708665" style="zoom:67%;" /> 

<font color=red size=5 face="SentyZHAO 新蒂赵孟頫">**也可使用以下方法自动关闭资源，记得补充！！！ **"</font>

也可使用以下方法自动关闭资源，记得补充！！！java也提供自动关闭的方法

**注意：他们的方法都使用了异常类，所以需要使用try..catch进行异常处理（异常类：IOException)** 

### （二）子类：FileInputStream（文件）

**(异常类：FileNotFoundException) ** 

操作时必须接受File类的实例，实现文件的输入输出，输入输出都要指明被操作文件的路径。

#### 1.构造方法

（对于构造方法，重点关注的就是入口参数类型）

<img src="C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201111210316722.png" alt="image-20201111210316722" style="zoom:67%;" /> 

<img src="C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201111210333590.png" alt="image-20201111210333590" style="zoom:67%;" /> 

```java
File inFile=new File("file1.txt");
FileInputStream fis=new FileInputStream(inFile);
FileInputStream fis=new FileInputStream("f:"+File.separator+"gui");
```

#### 2.常用方法

<img src="C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201111211925304.png" alt="image-20201111211925304" style="zoom:67%;" /> 

<img src="C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201111211942041.png" alt="image-20201111211942041" style="zoom:67%;" /> 

请见API

示例：

```java
import java.io.*;
/*实现把文件1的内容复制到文件2*/
public class FileStream{  
	public static void main(String args[]){ 
		try{
			File inFile=new File("file1.txt");//构造文件对象，当路径不明确时，它会在java文件所在的目录下找
			File outFile=new File("file2.txt");
			FileInputStream fis=new FileInputStream(inFile);//创建文件流
			FileOutputStream fos=new  FileOutputStream(outFile);
			int c;  
			int i=1;
			while((c=fis.read())!=-1){  
				fos.write(c);
				//System.out.println("写入Buffer第"+i++);
			}
			fis.close(); //关闭文件流
			fos.close();
		}catch(FileNotFoundException e) {
			System.out.println("FileStreamsTest: "+e);
		}catch(IOException e) {
			System.err.println("FileStreamsTest: "+e);
		}
	}
}

```

实际上，程序中不断操作文件的效率是十分慢的，使用下面的孙子类更好。

### （三）孙子类：BufferedInputStream（缓存）

在读取流的时候，一次读取一个字节并不是最高效的方法。很多流支持一次性读取多个字节到缓冲区，对于文件和网络流来说，利用缓冲区一次性读取多个字节效率往往要高很多。为此我们使用Buffer，将文件操作转化为内存操作  **Buffer大小可由人工指定，超过大小可执行 一次写入或读出** 。

#### 1.构造方法

 <img src="C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201111213436244.png" alt="image-20201111213436244" style="zoom:67%;" />

注意，孙子类入口参数都要是数据流

#### 2.常用方法

其实对于io,最重要的方法就是输入输出了。

<img src="C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201111213641513.png" alt="image-20201111213641513" style="zoom:67%;" /> 

示例：

```java
import java.io.*;
/*实现把文件1的内容复制到文件2*/
public class BufferedStream {
	public static void main(String args[]) {
		try {
			File inFile = new File("file1.txt");
			File outFile = new File("file2.txt");
			FileInputStream fis = new FileInputStream(inFile);
			BufferedInputStream bis = new BufferedInputStream(fis);//把家族里面的叔叔放进自己口袋
			BufferedOutputStream bos = new BufferedOutputStream(new FileOutputStream(outFile), 5);//在缓存区里面操作5个字节即输出到文件里面；如果缺省默认全部操作完再输出
			int c;
			int i = 1;
			while ((c = bis.read()) != -1) {
				bos.write(c);
			}
			bis.close();
			bos.close();
		} catch (FileNotFoundException e) {
			System.out.println("FileStreamsTest: " + e);
		} catch (IOException e) {
			System.err.println("FileStreamsTest: " + e);
		}
	}
}
```



### （四）孙子类：DataInputStream（格式化数据）

File和Buffer都是字节流，即一次读写一个 字节（虽然buffer更高效，但是在缓存区还是一个一个字节读取的），而往往我们文件内有高级数据类型， int, float等，采用数据流可直接处理高级数据类型**格式化输入输出 ** 

####  1.构造方法

<img src="C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201111214931074.png" alt="image-20201111214931074" style="zoom:67%;" /> 

#### 2.常用方法

可以指定读写数据的类型

<img src="C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201111215120905.png" alt="image-20201111215120905" style="zoom:67%;" /> 

```java
import java.io.*;

public class DataStream{  
	public static void main(String args[])throws  IOException{ 
		FileOutputStream fos=new FileOutputStream("file2.txt");
		BufferedOutputStream bos = new BufferedOutputStream(fos);
		DataOutputStream dos=new DataOutputStream (bos);
		try{
			dos.writeBoolean(true);
			dos.writeByte((byte)123);
			dos.writeChar('J');
			dos.writeDouble(3.141592654);
			dos.writeFloat(2.7182f);
			dos.writeInt(1234567890);
			dos.writeLong(998877665544332211L);
			dos.writeShort((short)11223);
		}catch(Exception e) {
			System.err.println("FileStreamsTest: "+e);
		}
		finally{  
			dos.close(); 
		}	
		System.in.read();
		//BufferedInputStream dis = new BufferedInputStream(new DataInputStream(new FileInputStream("file2.txt")));
		DataInputStream dis=new DataInputStream(new FileInputStream("file2.txt"));
		try{
			System.out.println("\t "+dis.readBoolean());
			System.out.println("\t "+dis.readByte());
			System.out.println("\t "+dis.readChar());
			System.out.println("\t "+dis.readDouble());
			System.out.println("\t "+dis.readFloat());
			System.out.println("\t "+dis.readInt());
			System.out.println("\t "+dis.readLong());
			System.out.println("\t "+dis.readShort());
		}finally{
			dis.close();
		}	
	}
}
>>>  true
         123
         J
         3.141592654
         2.7182
         1234567890
         998877665544332211
         11223
```



## 三、字符输入输出流（char)

<font color=red size=5 face="SentyZHAO 新蒂赵孟頫">**Reader /Writer**"</font>

Reader/Writer本质上是能自动编解码（指定编解码方式）的InputStream和OutputStream。适用于文本的输入输出。

程序中一个字符等于两个字节。这两个类也是抽象类，使用子类实现。其中也暗含异常处理（**异常类：IOException**）

它与字节输入输出流极其类似，故不重复叙述。

![image-20201116194448146](C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201116194448146.png) 

主要子类如上，其中也包括文件读写与缓存区读写

**常用方法：**

<img src="C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201116194239556.png" alt="image-20201116194239556" style="zoom:67%;" /> 

<img src="C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201116194317255.png" alt="image-20201116194317255" style="zoom:67%;" /> 

```java
import java.io.*;

public class ReaderDiff {
	public static void main(String args[]) {
		try {
			File inFile1 = new File("file1.txt");
			File inFile2 = new File("file3.txt");

			BufferedInputStream bis = new BufferedInputStream(new FileInputStream(inFile1));
			// BufferedReader isr = new BufferedReader(new FileReader(inFile2));
			InputStreamReader isr = new InputStreamReader(new FileInputStream(inFile2), "GBK");
			// InputStreamReader isr = new InputStreamReader(new FileInputStream(inFile2),
			// "GB2312");
			int c1;
			byte[] bs = new byte[50];
			int c2;
			int count1 = 0;
			int count2 = 0;
			while ((c1 = bis.read()) != -1) {
				// System.out.print(new Byte((byte) c1));
				bs[count1] = (byte) c1;
				count1++;
			}
			System.out.println();
			System.out.println(new String(bs));
			System.out.println("------------------------------");
			while ((c2 = isr.read()) != -1) {
				System.out.print(new Character((char) c2));
				count2++;
			}
			System.out.println();
			System.out.println("------------------------------");
			System.out.println("Stream byte number=" + count1);
			System.out.println("Reader char number=" + count2);
			bis.close();
			isr.close();
		} catch (FileNotFoundException e) {
			System.out.println(e);
		} catch (IOException e) {
			System.err.println(e);
		}
	}
}

```



## 四、字节字符IO流的区别与联系

### （一）区别

字节流在操作的时候本身不会用到缓存区（内存），而是通过直接操作文件的；而字符流操作的时候使用缓存区在通过缓存区操作文件。例如，如果使用字节流写文件，在字节流不关闭时，文件是可以直接显示内容的；而使用字符流时，由于字符流文件未关闭1，没有执行将缓存读到文件中的操作，文件中就看不到写的内容。但是我们可以通过**writer.flush（）**进行强制的缓存刷新，内存内容被强制读取到文件

### （二）联系：InputStreamReader

它是Reader的儿子。它是从InputStreeam到Reader的转换器

<img src="C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201116195822784.png" alt="image-20201116195822784" style="zoom:67%;" /> 

常用方法：

<img src="C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201116195935046.png" alt="image-20201116195935046" style="zoom:67%;" /> 

现实使用时使用InputStream类更好，因为所有数据存储在硬盘中都是以字节存储的，字符流底层还是字节流，所以字节流使用更加广泛。

**编码：**

| 编码方式  |                                                              |
| --------- | ------------------------------------------------------------ |
| GB2312    | 汉字是双字节的。所谓双字节是指一个双字要占用两个BYTE的位 置（即16位），分别称为高位和低位。GB2312包括了一二级汉 字编码范围为0xb0a1到0xf7fe |
| GBK       | GBK提供了20902个汉字，它兼容GB2312，编码范围为0x8140 到0xfefe |
| ISO8859_1 | 英文字符                                                     |

一般默认为GBK或者GB2312

## 重点！InputStream 的继承关系

![image-20201111201428982](C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201111201428982.png) 

InputStream是最大的爸爸，其继承树关系如下：

![image-20201111201248064](C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201111201248064.png) 

特别值得关注的是：

<img src="C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201111202942918.png" alt="image-20201111202942918" style="zoom:67%;" /> 

<img src="C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201111203010019.png" alt="image-20201111203010019" style="zoom:67%;" /> 

<img src="C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201111203031628.png" alt="image-20201111203031628" style="zoom:67%;" /> 

FilterInputStream作为InputStream的第一任儿子，用爸爸的类作为构造参数入口，而BufferedInputStream作为FilterInputStream的儿子，InputStream的孙子居然也是用爷爷的类作为构造函数入口参数类型。而且FilterInputStream的所有儿子都是用爷爷的类构造入口参数的。说明他们之间可以互相套娃。沟通的桥梁就是InputStream这个爷爷。家族所有类都能传入家族下任何一个类里面。（同理，OutputStream这个超类也是这样的家族，而Reader和Writer也有类似的地方）

![image-20201111203702994](C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201111203702994.png) 

![image-20201111220245026](C:\Users\win10\AppData\Roaming\Typora\typora-user-images\image-20201111220245026.png) 
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
		super(speed - 5);//设定父亲的speed，父亲比儿子速度慢5km/h
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
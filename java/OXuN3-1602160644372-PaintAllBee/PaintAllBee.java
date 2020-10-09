interface Bee{
	public abstract void paint();
}

class Honee implements Bee
{
	public void paint()
	{
		System.out.println("��һֻС�۷�");
	}
}

class Mikee implements Bee
{
	public void paint()
	{
		System.out.println("��һֻ���۷�");
	}
}

class Guardian implements Bee
{
	public void paint()
	{
		System.out.println("��һֻ�����۷�");
	}
}

public class PaintAllBee{
	Bee[] bees;
	
	public PaintAllBee(){
		bees = new Bee[3];
	}
	
	public void addBee(Bee b,int index){
		bees[index] = b;
	}
	
	public void paintAll()
	{
		for(int i=0;i<3;i++)
			if(bees[i]!=null)
				bees[i].paint();
	}

	public static void main(String[] args)
	{
		PaintAllBee pab = new PaintAllBee();
		pab.addBee(new Honee(),0);
		pab.addBee(new Mikee(),1);
		pab.addBee(new Guardian(),2);
		pab.paintAll();
	}
}
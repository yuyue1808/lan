class Bee{
    int honeyBag = 0;
    public void pickHoney(){
         honeyBag ++;
    }
}

public class Test extends Bee{
   int honeyBag = 2;

   public static void main(String[] args) {
        Test b = new Test();
        b.pickHoney();
        System.out.println(b.honeyBag);
   }
}
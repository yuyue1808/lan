import java.util.Scanner;

public class test0 {
    public static void main(String[] args) {
        Scanner chengji1 = new Scanner(System.in);
        Scanner chengji2 = new Scanner(System.in);
        System.out.print("input the chengji1: ");
        double first = chengji1.nextDouble();
        System.out.println(" ");
        System.out.print("input the chengji2: ");
        double second = chengji2.nextDouble();
        double up = ((second-first)/second)*100;
        
        System.out.printf("%.2f%%", up);


    }
}
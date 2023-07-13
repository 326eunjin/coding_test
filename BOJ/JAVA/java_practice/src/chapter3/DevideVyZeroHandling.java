package chapter3;
import java.util.Scanner;
public class DevideVyZeroHandling {
    public static void main(String[] args)
    {
        Scanner scanner=new Scanner(System.in);
        while(true)
        {
            System.out.print("input dividend");
            int dividend = scanner.nextInt();
            System.out.print("input divisor");
            int divisor = scanner.nextInt();
            try{
                System.out.println("result is "+dividend/divisor);
                break;
            }
            catch(ArithmeticException e)
            {
                System.out.println("you can not divide into zero");
            }
        }
        scanner.close();
    }
}

package chapter2;
import java.util.Scanner;
public class dollar {
    public static void main(String[] args)
    {
        Scanner scanner=new Scanner(System.in);
        System.out.print("input won>>");
        int won = scanner.nextInt();
        float dollar=won/1100;
        System.out.println(won+"won is same as $"+dollar);
        scanner.close();
    }
}

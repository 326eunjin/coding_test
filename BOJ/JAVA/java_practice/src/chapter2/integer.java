package chapter2;
import java.util.Scanner;

public class integer {
    public static void main(String[] args){
        Scanner scanner=new Scanner(System.in);
        System.out.print("input integer between 10 and 99>>");
        int input= scanner.nextInt();
        int first=input/10;
        int second=input%10;
        if(first==second)
            System.out.println("Yes! first int and second int are same");
        else
            System.out.println("They are not same");
        scanner.close();
    }
}

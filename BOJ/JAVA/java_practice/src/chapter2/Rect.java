package chapter2;
import java.util.Scanner;
public class Rect {
    public static boolean inRect(int x, int y, int rectx1, int recty1, int rectx2, int recty2)
    {
        if((x>=rectx1 && x<= rectx2) &&(y >= recty1 && y <= recty2))
            return true;
        else
            return false;
    }
    public static void main(String[] args)
    {
        Scanner scanner = new Scanner(System.in);
        int x=scanner.nextInt();
        int y=scanner.nextInt();
        if (inRect(x,y,100,100,200,200))
            System.out.println("(x.y) is in rect");
        else
            System.out.println("(x.y) is not in rect");
        scanner.close();
    }
}

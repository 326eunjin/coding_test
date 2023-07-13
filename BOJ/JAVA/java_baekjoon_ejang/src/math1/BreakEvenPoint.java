package math1;

import java.util.Scanner;

public class BreakEvenPoint {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int a = scanner.nextInt();
        int b = scanner.nextInt();
        int c = scanner.nextInt();
        int result = 0;
        int tmp = 0;
        //int tmp = a / (c - b);
        if (c <= b)
            result = -1;
        else {
            tmp = a / (c - b);
            while (result <= tmp) {
                result++;
            }
        }
        System.out.println(result);
        scanner.close();
    }
}

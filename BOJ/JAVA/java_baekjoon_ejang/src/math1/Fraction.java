package math1;

import java.util.*;

public class Fraction {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int input = scanner.nextInt();
        int n = 0;
        while (input * 2 > n * (n + 1))
            n++;
        int a = input - (n - 1) * n / 2;
        int b = n + 1 - a;
        if (n % 2 == 0)//even
            System.out.println(a + "/" + b);
        else//odd
            System.out.println(b + "/" + a);
        scanner.close();
    }
}

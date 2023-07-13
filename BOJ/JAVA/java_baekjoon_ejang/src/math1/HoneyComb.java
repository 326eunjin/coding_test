package math1;

import java.util.*;

public class HoneyComb {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int input = scanner.nextInt();
        int result = 0;
        int tmp = 1;
        if (input == 1)
            System.out.println(1);
        else {
            input = input - 1;
            result = input / 6;
            while (result * 2 > tmp * (tmp + 1))
                tmp++;
            System.out.println(tmp + 1);
        }
        scanner.close();
    }
}

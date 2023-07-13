package brutal_force;

import java.util.*;

public class Decomposition_2231 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int input = scanner.nextInt();
        int result = 0;
        int tmp;
        for (int i = 0; i < 1000000; i++) {
            tmp = 0;
            result = i;
            while (result > 0) {
                tmp += result % 10;
                result /= 10;
            }
            if (tmp + i == input) {
                result = i;
                break;
            }
            if (i == 999999)
                result = 0;
        }
        System.out.println(result);
        scanner.close();
    }
}

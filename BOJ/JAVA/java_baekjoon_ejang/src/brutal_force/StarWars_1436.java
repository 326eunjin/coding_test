package brutal_force;

import java.util.*;

public class StarWars_1436 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int input = scanner.nextInt();
        String str;
        int tmp = 0;
        String result="";
        for (int i = 0; i < 2147483647; i++) {
            str = Integer.toString(i);
            if (str.contains("666")) {
                tmp++;
                result = str;
            }
            if (tmp == input)
                break;
        }
        System.out.println(result);
        scanner.close();
    }
}

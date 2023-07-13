package greedy_algorithm;

import java.util.Scanner;

public class Lost_bracket_1541 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String str = scanner.nextLine();
        String[] array = str.split("-");
        int tmp = 0;
        int result[] = new int[array.length];
        for (int i = 0; i < array.length; i++) {
            tmp = 0;
            String[] array2 = array[i].split("\\+");
            for (int j = 0; j < array2.length; j++)
                tmp += Integer.parseInt(array2[j]);
            result[i] = tmp;
        }
        tmp = result[0];
        for (int i = 1; i < result.length; i++)
            tmp -= result[i];
        System.out.println(tmp);
        scanner.close();
    }
}

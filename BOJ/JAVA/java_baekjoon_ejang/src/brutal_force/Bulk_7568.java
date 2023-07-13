package brutal_force;

import java.util.Scanner;

public class Bulk_7568 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[][] array;
        array = new int[n][3];
        for (int i = 0; i < n; i++) {
            array[i][0] = scanner.nextInt();
            array[i][1] = scanner.nextInt();
            array[i][2] = 1;
        }
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++) {
                if ((array[i][0] < array[j][0]) && (array[i][1] < array[j][1]))
                    array[i][2]++;
            }
        for (int i = 0; i < n; i++)
            System.out.print(array[i][2] + " ");
        scanner.close();
    }
}


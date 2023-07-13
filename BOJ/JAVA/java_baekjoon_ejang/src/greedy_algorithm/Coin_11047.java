package greedy_algorithm;

import java.util.Scanner;

public class Coin_11047 {
    public static int[][] arr;

    public static void main(String[] args) {
        int n, k;
        int result = 0;
        Scanner scanner = new Scanner(System.in);
        n = scanner.nextInt();
        k = scanner.nextInt();
        arr = new int[n][2];
        for (int i = 0; i < arr.length; i++)
            arr[i][0] = scanner.nextInt();
        scanner.nextLine();//개행 없애주기 위함
        coin(k);
        for (int i = 0; i < arr.length; i++)
            result += arr[i][1];
        System.out.println(result);
        scanner.close();
    }

    private static void coin(int k) {
        for (int i = arr.length - 1; i >= 0; i--) {
            arr[i][1] = k / arr[i][0];
            k -= arr[i][0] * arr[i][1];
        }
    }
}

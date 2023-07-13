package greedy_algorithm;

import java.util.Scanner;
import java.util.Arrays;

public class ATM_11399 {
    static int arr[];

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        arr = new int[n];
        scanner.nextLine();
        for (int i = 0; i < arr.length; i++)
            arr[i] = scanner.nextInt();
        ATM(n);
        scanner.close();
    }

    private static void ATM(int n) {
        Arrays.sort(arr);
        int[] result = new int[n];
        int tmp = 0;
        for (int i = 0; i < result.length; i++) {
            tmp = 0;
            for (int j = 0; j <= i; j++)
                tmp += arr[j];
            result[i] = tmp;
        }
        tmp = 0;
        for (int i = 0; i < result.length; i++)
            tmp += result[i];
        System.out.println(tmp);
    }
}

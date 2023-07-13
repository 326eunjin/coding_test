package sort;

import java.util.*;

public class SortNumber_2750 {
    public static void print(int arr[]){
        for(int i=0;i<arr.length;i++)
            System.out.println(arr[i]);
    }
    public static int[] sort(int arr[]) {
        int tmp;
        for (int i = 0; i < arr.length - 1; i++) {
            for (int j = 0; j < arr.length - 1 - i; j++)
                if (arr[j] > arr[j + 1]) {
                    tmp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = tmp;
                }
        }
        return arr;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int input = scanner.nextInt();
        int[] arr = new int[input];
        for (int i = 0; i < input; i++)
            arr[i] = scanner.nextInt();
        sort(arr);
        print(arr);
        scanner.close();
    }
}

package brutal_force;

import java.util.*;

public class Chess_1018 {
    final static int arr1[][] = {{1, 0, 1, 0, 1, 0, 1, 0}, {0, 1, 0, 1, 0, 1, 0, 1}, {1, 0, 1, 0, 1, 0, 1, 0}, {0, 1, 0, 1, 0, 1, 0, 1}, {1, 0, 1, 0, 1, 0, 1, 0}, {0, 1, 0, 1, 0, 1, 0, 1}, {1, 0, 1, 0, 1, 0, 1, 0}, {0, 1, 0, 1, 0, 1, 0, 1}};
    final static int arr2[][] = {{0, 1, 0, 1, 0, 1, 0, 1}, {1, 0, 1, 0, 1, 0, 1, 0}, {0, 1, 0, 1, 0, 1, 0, 1}, {1, 0, 1, 0, 1, 0, 1, 0}, {0, 1, 0, 1, 0, 1, 0, 1}, {1, 0, 1, 0, 1, 0, 1, 0}, {0, 1, 0, 1, 0, 1, 0, 1}, {1, 0, 1, 0, 1, 0, 1, 0}};

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String str1 = scanner.nextLine();
        String[] array1 = str1.split(" ");
        int n = Integer.parseInt(array1[0]);
        int m = Integer.parseInt(array1[1]);
        int result = 999999;
        int tmp = 0;
        int tmp2 = 0;
        int[][] arr3;
        arr3 = new int[n][m];
        //치환
        String[] array2 = new String[n];
        for (int i = 0; i < n; i++)
            array2[i] = scanner.nextLine();
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++) {
                if (array2[i].charAt(j) == 'W')
                    arr3[i][j] = 1;
                else
                    arr3[i][j] = 0;
            }
        //비교
        for (int i = 0; i <= n - 8; i++)
            for (int j = 0; j <= m - 8; j++) {
                tmp = 0;
                tmp2 = 0;
                for (int a = 0; a < 8; a++)
                    for (int b = 0; b < 8; b++) {
                        if (arr3[i + a][j + b] != arr1[a][b])
                            tmp++;
                        if (arr3[i + a][j + b] != arr2[a][b])
                            tmp2++;
                    }
                if (tmp >= tmp2)
                    tmp = tmp2;
                if (tmp <= result)
                    result = tmp;
            }
        System.out.println(result);
        scanner.close();
    }
}

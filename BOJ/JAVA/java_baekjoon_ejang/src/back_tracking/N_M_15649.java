package back_tracking;

import java.io.*;

public class N_M_15649 {
    static int[] arr;
    static boolean[] isUsed;
    static int n;
    static int m;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); // 선언
        String str = br.readLine();
        String tmp[] = str.split(" ");
        n=Integer.parseInt(tmp[0]);
        m=Integer.parseInt(tmp[1]);
        arr = new int[m + 1];
        isUsed = new boolean[n + 1];
        recursion(0);
        br.close();
    }

    private static void recursion(int index) {
        if (index == m) {
            for (int i = 0; i < m; i++) {
                System.out.println(arr[i]);
            }
            return;
        }
        for (int i = 1; i <= n; i++) {
            if (!isUsed[i]) {
                arr[index] = i;
                isUsed[i] = true;
                recursion(index + 1);
                isUsed[i] = false;
            }
        }
    }
}
package back_tracking;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Start_Link_14889 {
    private static int MIN = Integer.MAX_VALUE;
    static int[][] status;
    static int[] start;
    static int[] link;
    static boolean[] isUsed;
    static int n;

    public static void main(String[] args) throws IOException {
        StringTokenizer st;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); // 선언
        n = Integer.parseInt(br.readLine());
        status = new int[n][n];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++)
                status[i][j] = Integer.parseInt(st.nextToken());
        }
        start = new int[n / 2];
        link = new int[n / 2];
        isUsed = new boolean[n];
        recursion(0);
        System.out.println(MIN);
        br.close();
    }

    private static void recursion(int index) {
        if (index == n / 2) {
            int idx = 0;
            for (int i = 0; i < n; i++) {
                if (!isContains(i))
                    link[idx++] = i;
            }
            check_diff();
            return;
        }
        for (int i = 0; i < n; i++) {
            if (!isUsed[i]) {
                isUsed[i] = true;
                start[index] = i;
                recursion(index + 1);
                for (int j = i + 1; j < n; j++)
                    isUsed[j] = false;
            }
        }
    }

    private static void check_diff() {
        int result1 = 0;
        int result2 = 0;
        for (int i : start) {
            for (int j : start)
                result1 += status[i][j];
        }
        for (int i : link) {
            for (int j : link)
                result2 += status[i][j];
        }
        int n = Math.abs(result1 - result2);
        if (n == 0) {
            System.out.println(0);
            System.exit(0);
        } else
            MIN = Math.min(MIN, n);
    }

    private static boolean isContains(int id) {
        for (int i : start) {
            if (i == id)
                return true;
        }
        return false;
    }
}

package back_tracking;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class n_queens_9663 {
    static int n;
    static int cnt;
    static int temp[];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); // 선언
        n = Integer.parseInt(br.readLine());
        temp = new int[15];
        cnt = 0;
        for (int i = 0; i < n; i++) {
            temp[0] = i;
            nqueen(1);
        }
        System.out.println(cnt);
        br.close();
    }

    private static void nqueen(int col) {
        if (col == n) {
            cnt++;
            return;
        }
        for (int i = 0; i < n; i++) {
            boolean check = true;
            for (int j = 0; j < col; j++) {
                temp[col] = i;
                if (temp[j] == temp[col] || ((j - col) == (temp[j] - temp[col])) || ((j - col) == (temp[col] - temp[j]))) {
                    check = false;
                    break;
                }
            }
            if (check) {
                nqueen(col + 1);
            }
        }
    }
}

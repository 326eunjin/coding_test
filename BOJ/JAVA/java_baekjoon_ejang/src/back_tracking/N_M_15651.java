package back_tracking;

import java.io.*;

public class N_M_15651 {
    static int[] arr;
    static int n;
    static int m;
    public static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); // 선언
        String str = br.readLine();
        String tmp[] = str.split(" ");
        n=Integer.parseInt(tmp[0]);
        m=Integer.parseInt(tmp[1]);
        arr = new int[m + 1];
        recursion(0);
        System.out.print(sb);
        br.close();
    }

    private static void recursion(int index) {
        if (index == m) {
            for (int i = 0; i < m; i++) {
                sb.append(arr[i] + " ");
            }
            sb.append('\n');
            return;
        }
        for (int i = 1; i <= n; i++) {
                arr[index] = i;
                recursion(index + 1);
            }
        }
    }

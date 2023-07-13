package sort;

import java.util.*;
import java.io.*;

public class Coordinate2_11651 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); // 선언
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        int[][] arr = new int[n][2];
        for (int i = 0; i < arr.length; i++) {
            String str = br.readLine();
            String[] tmp = str.split(" ");
            arr[i][0] = Integer.parseInt(tmp[0]);
            arr[i][1] = Integer.parseInt(tmp[1]);
        }
        Arrays.sort(arr, new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                if (o1[1] == o2[1])
                    return o1[0] - o2[0];
                else
                    return o1[1] - o2[1];
            }
        });

        for (int i = 0; i < arr.length; i++) {
            bw.write(arr[i][0] + " " + arr[i][1] + "\n");
        }
        br.close();
        bw.close();
    }
}

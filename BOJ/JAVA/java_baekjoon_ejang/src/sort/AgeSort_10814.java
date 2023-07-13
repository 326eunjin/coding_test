package sort;

import java.util.*;
import java.io.*;

public class AgeSort_10814 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); // 선언
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        String[][] arr = new String[n][2];
        for (int i = 0; i < arr.length; i++) {
            String str = br.readLine();
            String[] tmp = str.split(" ");
            arr[i][0] = tmp[0];
            arr[i][1] = tmp[1];
        }
        Arrays.sort(arr, new Comparator<String[]>() {
            @Override
            public int compare(String[] s1, String[] s2) {
                //구현
                return Integer.compare(Integer.parseInt(s1[0]), Integer.parseInt(s2[0]));
            }
        });
        for (int i = 0; i < n; i++)
            bw.write(arr[i][0] + " " + arr[i][1] + "\n");
        br.close();
        bw.close();
    }
}

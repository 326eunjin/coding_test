package sort;

import java.io.*;

public class SortNumber3_10989 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); // 선언
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n];
        int[] count = new int[10001];
        int[] result = new int[n];

        for (int i = 0; i < arr.length; i++) {
            arr[i] = Integer.parseInt(br.readLine());
            count[arr[i]]++;
        }
        for (int i = 1; i < count.length; i++)
            count[i] += count[i - 1];

        for (int i = arr.length - 1; i >= 0; i--) {
            count[arr[i]]--;
            result[count[arr[i]]] = arr[i];
        }
        for (int i = 0; i < n; i++) {
            bw.write(result[i] + "\n");
        }
        br.close();
        bw.close();
    }
}

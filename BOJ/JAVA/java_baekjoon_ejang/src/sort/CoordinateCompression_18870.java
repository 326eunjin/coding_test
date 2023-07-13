package sort;

import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;

public class CoordinateCompression_18870 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); // 선언
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        int arr[] = new int[n];
        int result[] = new int[n];
        String str = br.readLine();
        String tmp[] = str.split(" ");
        for (int i = 0; i < arr.length; i++) {
            arr[i] = Integer.parseInt(tmp[i]);
        }
        ArrayList<Integer> arrayList = new ArrayList<Integer>();
        for (int item : arr) {
            if (!arrayList.contains(item))
                arrayList.add(item);
        }
//        for (int i = 0; i < arr.length; i++) {
//            int temp = 0;
//            for (int j = 0; j < arrayList.size(); j++) {
//                if (arr[i] > arrayList.get(j))
//                    temp++;
//            }
//            result[i] = temp;
//        }
//        Arrays.sort(arr, new Comparator<int>() {
//            @Override
//            public int compare(int o1, int o2) {
//
//            }
//        });

        for (int i = 0; i < result.length; i++)
            bw.write(result[i] + " ");
        br.close();
        bw.close();
    }
}

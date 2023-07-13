package sort;

import java.util.*;
import java.io.*;

public class SortNumber2_2751 {
    static int[] result;

    public static int[] merge(int list[], int left, int mid, int right) {
        int i, j, k, l;
        i = left;
        j = mid + 1;
        k = left;

        /* 분할 정렬된 list의 합병 */
        while (i <= mid && j <= right) {
            if (list[i] <= list[j])
                result[k++] = list[i++];
            else
                result[k++] = list[j++];
        }

        // 남아 있는 값들을 일괄 복사
        if (i > mid) {
            for (l = j; l <= right; l++)
                result[k++] = list[l];
        }
        // 남아 있는 값들을 일괄 복사
        else {
            for (l = i; l <= mid; l++)
                result[k++] = list[l];
        }

        // 배열 sorted[](임시 배열)의 리스트를 배열 list[]로 재복사
        for (l = left; l <= right; l++) {
            list[l] = result[l];
        }
        return list;
    }

    // 합병 정렬
    public static int[] merge_sort(int list[], int left, int right) {
        int mid;

        if (left < right) {
            mid = (left + right) / 2;// 중간 위치를 계산하여 리스트를 균등 분할 -분할(Divide)
            merge_sort(list, left, mid); // 앞쪽 부분 리스트 정렬 -정복(Conquer)
            merge_sort(list, mid + 1, right); // 뒤쪽 부분 리스트 정렬 -정복(Conquer)
            merge(list, left, mid, right); // 정렬된 2개의 부분 배열을 합병하는 과정 -결합(Combine)
        }
        return list;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); // 선언
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n];
        for (int i = 0; i < arr.length; i++) arr[i] = Integer.parseInt(br.readLine());
        Arrays.sort(arr);
        //정렬
        //merge_sort(arr, 0, n - 1);
        //출력
        for (int i = 0; i < n; i++) {
            bw.write(arr[i] + "\n");
        }
        br.close();
        bw.close();
    }
}

package sort;

import java.util.*;
import java.io.*;

public class VocabSort_1181 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); // 선언
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        String[] arr = new String[n];
        for (int i = 0; i < arr.length; i++)
            arr[i] = br.readLine();
        ArrayList<String> arrayList = new ArrayList<>();
        for (String item : arr) {
            if (!arrayList.contains(item))
                arrayList.add(item);
        }
        //중복 제거 후에 다시 배열로 넣기
        //배열에 넣었으면 이제 문자열의 길이대로 정렬
        String[] tmp = new String[arrayList.size()];
        int size = 0;
        for (String temp : arrayList)
            tmp[size++] = temp;
        Arrays.sort(tmp, new Comparator<String>() {
            @Override
            public int compare(String s1, String s2) {
                if (s1.length() == s2.length())
                    return s1.compareTo(s2);
                else
                    return s1.length() - s2.length();
            }
        });
        for (int i = 0; i < tmp.length; i++)
            bw.write(tmp[i] + "\n");
        br.close();
        bw.close();
    }
}

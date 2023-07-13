package sort;
import java.util.*;
import java.io.*;
public class SortInside_1427 {
    static int get_length(int input){
        int length =0;
        while(input>0)
        {
            length++;
            input=input/10;
        }
        return length;
    }
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); // 선언
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int input = Integer.parseInt(br.readLine());
        int length= get_length(input);
        int []arr=new int[length];
        //배열에 넣기
        while(input>0)
        {
            arr[length-1]=input%10;
            input=input/10;
            length--;
        }
        Arrays.sort(arr);
        for (int i = arr.length-1; i >=0; i--) {
            bw.write(String.valueOf(arr[i]));
        }
        br.close();
        bw.close();
    }
}

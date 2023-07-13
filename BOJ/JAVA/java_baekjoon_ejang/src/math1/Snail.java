package math1;

import java.io.*;
import java.util.*;

//public class Snail {
//    public static void main(String[] args) {
//        Scanner scanner = new Scanner(System.in);
//        int a = scanner.nextInt();
//        int b = scanner.nextInt();
//        int v = scanner.nextInt();
//        int result = (v - b) / (a - b);
//        if ((v - b) % (a - b) != 0)
//            result++;
//        System.out.println(result);
//    }
//}
public class Snail {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        int v = Integer.parseInt(st.nextToken());
        int result = (v - b) / (a - b);
        if ((v - b) % (a - b) != 0)
            result++;
        System.out.println(result);
    }
}
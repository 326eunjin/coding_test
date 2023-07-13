package brutal_force;

import java.util.Scanner;

public class BlackJack_2798 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String first = scanner.nextLine();
        String[] array1=first.split(" ");
        int n=Integer.parseInt(array1[0]);
        int m=Integer.parseInt(array1[1]);
        int result = 0;
        int temp = 0;
        String second = scanner.nextLine();
        int [] array2 = new int[n];
        String[] tmp=second.split(" ");
        for(int i= 0; i< n ;i++)
            array2[i]=Integer.parseInt(tmp[i]);
        for(int i = 0; i<n;i++)
            for(int j=i+1;j<n;j++)
                for(int k=j+1;k<n;k++)
                {
                    temp=array2[i]+array2[j]+array2[k];
                    if((temp<=m)&&(temp>=result))
                        result=temp;
                }
        System.out.println(result);
        scanner.close();
    }
}

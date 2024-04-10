import java.util.Scanner;

public class Main {

    public static final int MAX = (123456 * 2);
    public static int[] arr = new int[MAX+1];

    public static void getPrime() {
        for ( int i = 2; i < MAX + 1; i++ ) {
            if (arr[i] == -1)
                continue;
            for ( int j = i*2; j < MAX+1; j+=i){
                arr[j] = -1;
            }
        }
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        getPrime();

        while(true) {
            int n = in.nextInt();
            if (n == 0)
                return;

            int count = 0;
            for (int i = n+1; i <= 2*n; i++) {
                if(arr[i] != -1) count+=1;
            }
            System.out.println(count);
        }
    }
}
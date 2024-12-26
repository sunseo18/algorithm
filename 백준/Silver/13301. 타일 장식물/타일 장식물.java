import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static int n = 0;

    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());

        if (n == 1) {
            System.out.println(4);
            return;
        }

        if (n == 2) {
            System.out.println(6);
            return;
        }

        long[] fibo = new long[n + 1];
        long[] answer = new long[n+1];

        initFibo(fibo);
        initAnswer(answer, fibo);

        System.out.println(answer[n]);
    }

    public static void initFibo(long[] fibo) {
        fibo[0] = 0L;
        fibo[1] = 1L;

        for (int i = 2; i < n + 1; i++) {
            fibo[i] = fibo[i - 1] + fibo[i - 2];
        }
    }

    public static void initAnswer(long[] answer, long[] fibo) {
        answer[0] = 0;
        answer[1] = 4;
        answer[2] = 6;

        for (int i = 3; i < n + 1; i++) {
            answer[i] = (answer[i - 1] - fibo[i]) + (fibo[i] * 3);
        }
    }

}
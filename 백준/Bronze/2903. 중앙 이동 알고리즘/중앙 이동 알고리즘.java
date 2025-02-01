import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    private static long[] answer = new long[16];

    public static void main(String args[]) throws IOException {
        int n = Integer.parseInt(br.readLine());

        answer[1] = 3;
        for (int i = 2; i < 16; i++) {
            answer[i] = (answer[i - 1] * 2 - 1);
        }

        System.out.println(answer[n] * answer[n]);
    }
}
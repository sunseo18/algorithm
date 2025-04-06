import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;
import java.util.stream.Stream;

class Main {


    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(br.readLine());

        int[] p = new int[n+1];
        p[0] = 0;
        StringTokenizer st = new StringTokenizer(br.readLine());
        for ( int i = 1; i< n+1; i++) {
            p[i] = Integer.parseInt(st.nextToken());
        }

        int size = p.length;

        int[] dp = new int[size];

        dp[0] = p[0];
        dp[1] = p[1];
        for (int i = 2; i < n+1; i++) {
            int tmp = p[i];

            for (int j = i-1; j>=i/2; j--) {
                tmp = Math.max(tmp, dp[j] + dp[i-j]);
            }

            dp[i] = tmp;
        }

        System.out.println(dp[n]);
    }


}
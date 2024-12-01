import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.List;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static int MAX = 10000+2;

    public static void main(String args[]) throws IOException {

        int length = Integer.parseInt(br.readLine());

        List<Integer> numbers = new ArrayList<>();

        int[][] dp = new int[4][MAX];

        for (int i = 0; i < length; i++) {
            numbers.add(Integer.parseInt(br.readLine()));
        }

        for ( int i = 0; i < 4; i++ ) {
            for ( int j = 0; j < MAX; j++ ) {
                dp[i][j] = 0;
            }
        }

        init(dp);

        for ( int i = 1; i < 4; i++ ){
            for ( int j = 4; j < MAX; j++ ) {
                if ( i == 1 ) {
                    dp[i][j] = dp[i][j-1];
                }
                else if ( i == 2) {
                    dp[i][j] = dp[i-1][j] + dp[i][j-2];
                }

                else {
                    dp[i][j] = dp[i-1][j] + dp[i][j-3];
                }
            }
        }

        for ( Integer number: numbers) {
            bw.write(String.valueOf(dp[3][number]));
            bw.write('\n');
        }
        bw.flush();
    }

    public static void init(int[][] dp) {
        dp[1][1] = 1;
        dp[2][1] = 1;
        dp[3][1] = 1;

        dp[1][2] = 1;
        dp[2][2] = 2;
        dp[3][2] = 2;

        dp[1][3] = 1;
        dp[2][3] = 2;
        dp[3][3] = 3;

    }

}
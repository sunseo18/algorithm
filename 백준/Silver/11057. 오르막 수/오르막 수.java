// Online Java Compiler
// Use this editor to write, compile and run your Java code online

import java.io.*;
import java.util.Arrays;

class Main {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    
    public static void main(String[] args) throws IOException {
        int N = Integer.parseInt(br.readLine());
        
        long[][] dp = new long[10][1001];
        
        
        for (int i = 0; i < 10; i++) {
            dp[i][1] = i+1;
        }
        
        for (int j = 0; j < 1001;j++) {
            dp[0][j] = 1;
        }
        
        for (int j = 2; j < N+1; j++) {
            for ( int i = 1; i < 10; i++ ) {
                dp[i][j] = (dp[i][j-1] + dp[i-1][j]) % 10007;
            }
        }
        
        System.out.println(dp[9][N] % 10007);
        
    }
}
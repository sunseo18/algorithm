// Online Java Compiler
// Use this editor to write, compile and run your Java code online

import java.io.*;
import java.util.Arrays;

class Main {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    
    private static int MAX = 30;
    private static long[][] dp = new long[MAX*2+1][MAX+1];
    
    private static int T;
    
    public static void main(String[] args) throws IOException {

        for ( int i = 0; i < MAX*2+1; i++) {
            for ( int j = 0; j < MAX+1; j++) {
                if (i != 0 && j == 0) dp[i][j] = 1;
                else dp[i][j] = -1;
            }
        }
        
        while (true) {
            int N = Integer.parseInt(br.readLine());
            if (N == 0) return;
            
            
            System.out.println(dpf(0, N));
            
        }
    }
    
    public static long dpf(int i, int j) {
        if ( i < 0 || j < 0) return 0;
        
        if (dp[i][j] != -1)
            return dp[i][j];
        
        else {
            dp[i][j] = dpf(i-1, j) + dpf(i+1, j-1);
            return dp[i][j];
        }
    }
}
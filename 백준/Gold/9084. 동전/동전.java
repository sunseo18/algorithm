import java.util.*;
import java.io.*;
import java.util.stream.*;

public class Main {
  private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  private static int T;
  
    public static void main(String[] args) throws IOException{
      T = Integer.parseInt(br.readLine());
      for ( int t = 0 ; t < T; t++) {
        int N = Integer.parseInt(br.readLine());
        
        int[] coins = Stream.of(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        
        int M = Integer.parseInt(br.readLine());
        
        long[][] dp = new long[N][M+1];
        for ( int i = 0 ; i < N; i++) {
          dp[i][0] = 1;
        }
        
        long firstV;
        long secondV;
        for (int i = 0; i < N; i++) {
          for (int j = 1; j < M+1; j++) {
            
            firstV = i-1 < 0 ? 0 : dp[i-1][j];

            secondV = j - coins[i] < 0 ? 0 : dp[i][j-coins[i]];

            dp[i][j] = firstV + secondV;
          }
        }
        
        System.out.println(dp[N-1][M]);
        
      }
      
  }
}
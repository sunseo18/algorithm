import java.util.*;
import java.io.*;
import java.util.stream.*;

public class Main {
  
  private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  private static int N;
  private static long[] H;
  private static long[] A;
  private static long[] B;
  private static long[] dp;
  
  
  public static void main(String[] args) throws IOException {
    initialize();    
    dp = new long[N];
    
    dp[0] = 0;
    

    for ( int i = 1; i < N; i++ ) {
      int iOSB = indexOfStairBefore(i);
      
      if (iOSB < 0) {
        dp[i] = dp[i-1];
      }
      else {
        dp[i] = Math.max(A[i-1] + dp[iOSB], dp[i-1]);
      }
    }
    
    System.out.println(dp[N-1]);
    
  }
  
  public static void initialize() throws IOException{
    N = Integer.parseInt(br.readLine());
      
    H = Stream.of(br.readLine().split(" ")).mapToLong(Long::parseLong).toArray();
    A = Stream.of(br.readLine().split(" ")).mapToLong(Long::parseLong).toArray();
    B = Stream.of(br.readLine().split(" ")).mapToLong(Long::parseLong).toArray();
  }
  
  public static int indexOfStairBefore(int curIndex) {
    int start = 0;
    int end = curIndex-1;
    int iOSB = -1;
    long curStrength = H[curIndex] + B[curIndex-1];
    // System.out.println(curStrength);
    
    while (start <= end) {
      int mid = (start + end) / 2;
      // System.out.println(mid);
      
      // 유망한 계단을 찾음
      if (H[mid] >= curStrength) {
        iOSB = mid;
        start = mid + 1;
      }
      
      // 안 유망하면 무시  
      else {
        end = mid - 1;
      }

    }
     
    return iOSB;
  }
}
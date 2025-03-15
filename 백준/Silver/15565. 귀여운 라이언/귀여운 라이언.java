// Online Java Compiler
// Use this editor to write, compile and run your Java code online
import java.io.*;
import java.util.*;
import java.util.stream.Stream;

class Main {
  
    public static int i = 0;
    public static int j = 0;
    public static int answer;
    public static int lionNumber = 0;
    
    public static int N;
    public static int K;
    public static int[] dolls;
    public static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    
    public static void main(String[] args) throws IOException {
        String[] NAndK = br.readLine().split(" ");
        N = Integer.parseInt(NAndK[0]);
        K = Integer.parseInt(NAndK[1]);
        
        dolls = new int[N];
        
        dolls = Stream.of(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        
        answer = N+1;
        
        // i & j 초기화
        while ( i < N && dolls[i] == 2) i++;
        j = i;
        // System.out.println(i);
        
        while (i <= j && j < N) {

          if (dolls[j] == 1) lionNumber++;
          
          if (lionNumber == K) {
            answer = Math.min(answer, j-i+1);
            // System.out.printf("i: %d, j: %d\n", i, j);
            // 라이언 개수 다 참
            // i를 다음 1로 이동
            do {
              i++;
            } while( i < j && dolls[i] == 2);
            lionNumber--;
            
          }
          j++;
        }
        
        if (answer == N+1) System.out.println("-1");
        else System.out.println(answer);
    }
}
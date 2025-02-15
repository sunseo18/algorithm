import java.util.*;
import java.util.stream.*;
import java.io.*;

public class Main {
  private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  
  private static int answer = 0;
  private static int[][] firstBoard;
  private static int[][] secondBoard;
  private static int N;
  private static int M;
  
  public static void main(String[] args) throws IOException {

    String nAndM = br.readLine();
    
    StringTokenizer st = new StringTokenizer(nAndM);
    N = Integer.parseInt(st.nextToken());
    M = Integer.parseInt(st.nextToken());

    
    firstBoard = new int[N][M];
    for ( int i = 0 ; i < N; i++) {
      int[] row = Stream.of(br.readLine().split("")).mapToInt(Integer::parseInt).toArray();
      for ( int j = 0; j < M; j++ ) {
        firstBoard[i][j] = row[j];
      }
    }
        
    secondBoard = new int[N][M];
    for ( int i = 0 ; i < N; i++) {
      int[] row = Stream.of(br.readLine().split("")).mapToInt(Integer::parseInt).toArray();
      for ( int j = 0; j < M; j++ ) {
        secondBoard[i][j] = row[j];
      }
    }
    
    if (N < 3 && M < 3) {
      for ( int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
          if (firstBoard[i][j] != secondBoard[i][j]) {
            System.out.println(-1);
            return;
          }
        }
      }
      
      System.out.println(0);
      return;
    }
    
    for ( int i = 0 ; i < N-2; i++) {
      for ( int j = 0 ; j < M-2; j++) {
        if (firstBoard[i][j] != secondBoard[i][j]) {
          answer++;
          for ( int x = i; x < i+3; x++ ) {
            for ( int y = j; y < j+3; y++ ) {
              if(firstBoard[x][y] == 1)
                firstBoard[x][y] = 0; 
              else firstBoard[x][y] = 1;
            }
          }
        }
      }
    }
    
    for ( int i = 0 ; i < N; i++) {
      for ( int j = 0; j < M; j++) {
        if (firstBoard[i][j] != secondBoard[i][j]) answer = -1;
      }
    }
      System.out.println(answer);
    
    
  }
}
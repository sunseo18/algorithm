import java.util.*;
import java.io.*;
import java.util.stream.*;

public class Main {
  
  private static int N;
  private static int M;
  private static int[][] map;
  private static boolean[][] visited;
  private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  private static int[] dx = {0, 0, 1, -1, 1, -1, 1, -1};
  private static int[] dy = {1, -1, 0, 0, 1, -1, -1, 1};
  private static int answer = 0;
  
  public static void main(String[] args) throws IOException {
    String[] NAndM = br.readLine().split(" ");    
    
    N = Integer.parseInt(NAndM[0]);
    M = Integer.parseInt(NAndM[1]);
    
    map = new int[N][M];
    visited = new boolean[N][M];
    
    for (int i = 0; i < N; i++) {
      int[] line =  Stream.of(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
      for (int j = 0; j < M; j++) {
        map[i][j] = line[j];  
        visited[i][j] = false;
      }
    }
    
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < M; j++) {
        if (!visited[i][j] && map[i][j] != 0) {
          ArrayList<Point> sameHeightAdjacent = new ArrayList<Point>();
          sameHeightAdjacent.add(new Point(i, j));
          getArrayOfSameHeightAdjacentPoint(i, j, sameHeightAdjacent);
          if (checkIfBonguri(sameHeightAdjacent)) {
            answer++;
          }
          // for (Point point : sameHeightAdjacent) {
          //   System.out.printf("%d %d\n", point.x, point.y);
          // }
        }
      }
    }
    
    System.out.println(answer);
    
  }
  
  public static void getArrayOfSameHeightAdjacentPoint(int x, int y, ArrayList<Point> sameHieghtAdjacent) {
    visited[x][y] = true;
    
    for (int d = 0; d < dx.length; d++) {
      int nx = x+dx[d];
      int ny = y+dy[d];
      
      if ((0 <= nx && nx < N && 0 <= ny && ny < M) && !visited[nx][ny] && map[nx][ny] == map[x][y]) {
        sameHieghtAdjacent.add(new Point(nx, ny));
        getArrayOfSameHeightAdjacentPoint(nx, ny, sameHieghtAdjacent);
      }
    }
  }
  
  
  public static boolean checkIfBonguri(ArrayList<Point> sameHeightAdjacent) {
    for (Point point : sameHeightAdjacent) {
      for ( int d = 0; d < dx.length; d ++ ) {
        int nx = point.x + dx[d];
        int ny = point.y + dy[d];
        
        if(0 <= nx && nx < N && 0 <= ny && ny < M) {
          if ( map[nx][ny] > map[point.x][point.y] ) return false;
        }
      }
    }
    
    return true;
  }
  
  public static class Point {
    public int x;
    public int y;
    
    public Point(int x, int y) {
      this.x = x;
      this.y = y;
    }
  }
}
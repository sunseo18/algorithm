import java.util.*;
import java.util.stream.Stream;
import java.io.*;

public class Main
{

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    
    private static int length = 19;
    private static int[][] board = new int[length][length];
    
    private static int[] di = {1, 1, 0, -1};
    private static int[] dj = {0, 1, 1, 1};
    
    public static void main(String args[]) throws IOException {
        StringTokenizer st = null;
        
        for ( int i = 0; i < length; i++) {
            int[] line = Stream.of(br.readLine().split(" ")).mapToInt(Integer::valueOf).toArray();
            for ( int j = 0; j < length; j++) {
                board[i][j] = line[j];
            }
        }
        
        for ( int i = 0; i < length; i++) {
            for ( int j = 0; j < length; j++) {
                if (board[i][j] != 0 && hasWon(i, j, board[i][j])) {
                    if (board[i][j] == 1) System.out.println("1");
                    else if (board[i][j] == 2) System.out.println("2");
                    
                    
                    System.out.printf("%d %d", i+1, j+1);
                    
                    return;
                }
            }
        }
        
        System.out.println("0");
        
    } 
    
    private static void initBoard(int[][] board) {
        for ( int i = 0; i < length; i++) {
            for ( int j = 0; j < length; j++) {
                board[i][j] = 0;
            }   
        }
    }
    
    private static boolean hasWon(int i, int j, int color) {
        for (int d = 0; d < 4; d++) {
            int ni = i;
            int nj = j;
            int cnt = 1;
            for (int y = 0; y < 5; y++, cnt++) {
                ni += di[d];
                nj += dj[d];
                
                // 오목판 넘으면 그만두기
                if ( ni < 0 || ni >= length || nj < 0 || nj >= length) 
                    break;
                    
                // 색이 다르면 그만두기
                if ( board[ni][nj] != color) 
                    break;
                
            }
            
            // 오목 다섯개 일때 이전 방향 검사 후 이겼는지 최종 검사
            if (cnt == 5) {
                int oi = i - di[d];
                int oj = j - dj[d];
                
                // 오목판 넘으면 이긴 거
                if ( oi < 0 || oi >= length || oj < 0 || oj >= length) return true;
                // 반대 방향 색 같으면 6개 이상으로 진 거 
                else if ( board[oi][oj] == color ) return false;
                // 반대 방향 색 다르면 이긴 거 
                else return true;
            }
        }
        return false;
    }

}
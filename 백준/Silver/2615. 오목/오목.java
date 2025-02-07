import java.util.*;
import java.util.stream.Stream;
import java.io.*;

public class Main
{

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    
    private static int length = 19;
    private static int[][] board = new int[length][length];

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
                if (board[i][j] != 0 && checkWin(i, j, board[i][j])) {
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

    private static boolean checkWin(int i, int j, int color) {
        // checkRight
        if ( j-1 < 0 || (j-1 >= 0 && board[i][j-1] != color)) {
            int b = j;
            for (; b < j+6; b++) {
                // 벽에 마주쳤을 때
                if (b == length) break;
                // 연속되지 않을 때
                if (board[i][b] != color) break;
            }
            if (b == j+5) return true;
        }
        
        // checkDown
        if ( i-1 < 0 || (i-1 >= 0 && board[i-1][j] != color)) {
            int a = i;
            for (; a < i+6; a++) {
                if (a == length) break;
                if (board[a][j] != color) break;
            }
            if (a == i+5) return true;
        }
        
        // checkRightUp
        
        if ( (i+1 >= length || j-1 < 0) || (i+1<length && j-1 >= 0 && board[i+1][j-1] != color)) {
            int a = i;
            int b = j;
            for (; a > i-6 && b < j+6; a--, b++) {
                if (a < 0) break;
                if (b == length) break;
                if (board[a][b] != color) break;
            }
            if ((a == i-5) && (b == j+5)) return true;
        }
        
        // checkRightDown
        if ( (i-1 < 0 || j-1 <0) || (i-1>=0 && j-1>=0 && board[i-1][j-1] != color)) {
            int a = i;
            int b = j;
            for (; a < i+6 && b < j + 6; a++, b++) {
    
                if (a == length) break;
                if (b == length) break;
                if (board[a][b] != color) break;
            }
            if ((a==i+5) && (b == j+5)) return true;
        }
        return false;
    }
}
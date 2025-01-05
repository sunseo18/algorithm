import java.io.*;
import java.util.stream.*;

public class Main {
    public static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    public static int col;
    public static int row;
    public static int[][] array;
    public static int answer = 0;

    public static int maxFirstBox(int i, int j) {
        int sumBox = array[i][j] + array[i][j+1] + array[i+1][j] + array[i+1][j+1];

        int minOfFour = 10001;
        for(int a = i; a < i+2; a++) {
            for(int b = j; b<j+2; b++) {
                minOfFour =  Math.min(array[a][b], minOfFour);
            }
        }
        return sumBox - minOfFour;
    }

    public static int maxSecondBoxHorizontal(int i, int j ) {
        return array[i][j] + array[i][j+1] + array[i][j+2];
    }
    public static int maxSecondBoxVertical(int i, int j ) {
        return array[i][j] + array[i+1][j] + array[i+2][j];
    }

    public static void main(String[] args) throws IOException {
        String[] colAndRow = br.readLine().split(" ");
        row = Integer.parseInt(colAndRow[0]);
        col = Integer.parseInt(colAndRow[1]);

        array = new int[row][col];

        for(int i = 0; i < row; i++) {
            array[i] =  Stream.of(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        }

        for(int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                // 첫 번째 상자
                if (i+1<row) {
                    if (j+1<col) {
                        answer = Math.max(answer, maxFirstBox(i, j));
                    }
                } 
                // 두 번째 상자 (세로)
                if(i+2<row) {
                    answer = Math.max(answer, maxSecondBoxVertical(i, j));
                }
                // 두 번째 상자 (가로) 
                if (j+2<col) {
                    answer = Math.max(answer, maxSecondBoxHorizontal(i,j));
                }
            }
        }
        System.out.println(answer);
        
    }
}
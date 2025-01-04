import java.io.*;
import java.util.stream.*;

public class Main {

    public static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    public static int[][] array;
    public static int answer = 0;

    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(br.readLine());
        array = new int[n][n];

        for(int i = 0; i < n; i++) {
            int[] line = Stream.of(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            array[i] = line;
        }

        for(int i = 0; i < n-3+1; i++) {
            for(int j = 0; j < n-3+1; j++) {
                int count = 0;
                for(int x = i; x < i+3; x++) {
                    for (int y = j; y <j+3; y++) {
                        if (array[x][y] == 1) {
                            count++;
                        }
                    }
                }
                answer = Math.max(count, answer);
            }
        }

        System.out.println(answer);
    }
}
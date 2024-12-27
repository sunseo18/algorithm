import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.stream.Stream;

public class Main {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static int n = 0;
    private static int upperMax = 1;
    private static int downWardMax = 1;

    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());
        int[] numbers = Stream.of(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        int[] continuous = new int[n];

        continuous[0] = 1;
        for(int i = 1; i < n; i++ ) {
            if (numbers[i] >= numbers[i-1] ) {
                continuous[i] = continuous[i-1] +1;
                upperMax = Math.max(continuous[i], upperMax);
            } else {
                continuous[i] = 1;
            }
        }

        continuous[0] = 1;
        for(int i = 1; i < n;i ++) {
            if (numbers[i] <= numbers[i-1]) {
                continuous[i] = continuous[i-1] + 1;
                downWardMax = Math.max(continuous[i], downWardMax);
            } else {
                continuous[i] = 1;
            }
        }

        System.out.println(Math.max(upperMax, downWardMax));

    }

}
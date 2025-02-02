import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.stream.Stream;

public class Main {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void main(String args[]) throws IOException {
        while (true) {
            int[] input = Stream.of(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            if (input[0] == 0 && input[1] == 0) {
                break;
            }

            if (isFactor(input[0], input[1])) {
                bw.write("factor\n");
            }

            else if (isMultiple(input[0], input[1])) {
                bw.write("multiple\n");
            }

            else if (isNeither(input[0], input[1])) {
                bw.write("neither\n");
            }

            bw.flush();
        }
    }

    private static boolean isFactor(int a, int b) {
        if (b % a == 0) {
            return true;
        }
        return false;
    }

    private static boolean isMultiple(int a, int b) {
        if (a % b == 0) {
            return true;
        }
        return false;
    }

    private static boolean isNeither(int a, int b) {
        if (!isFactor(a, b) && !isMultiple(a, b)) {
            return true;
        }
        return false;
    }
}

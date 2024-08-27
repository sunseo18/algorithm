import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.stream.Stream;

class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        long[] weight = Stream.of(br.readLine().split(" ")).mapToLong(Long::parseLong).toArray();
        long[] point = Stream.of(br.readLine().split(" ")).mapToLong(Long::parseLong).toArray();

        long smallest = point[0];
        long answer = 0;
        for (int i = 1; i < n; i++) {
            if (point[i] >= smallest) {
                answer += weight[i - 1] * smallest;
            } else {
                answer += weight[i - 1] * smallest;
                smallest = point[i];
            }
        }

        System.out.println(answer);
    }


}
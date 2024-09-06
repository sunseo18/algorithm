import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.stream.Stream;

class Main {
    private static int n;
    private static int s;
    private static int answer = 0;
    private static int[] numbers;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] nAndS = br.readLine().split(" ");
        n = Integer.parseInt(nAndS[0]);
        s = Integer.parseInt(nAndS[1]);

        numbers = Stream.of(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        dfs(0, new ArrayList<>());

        System.out.println(answer);
    }

    private static void dfs(int depth, ArrayList<Integer> sum) {
        if (depth == n) {
            int tmp = 0;
            if (!sum.isEmpty()) {
                for (int s : sum) {
                    tmp += s;
                }
                if (tmp == s) {
                    answer++;
                }
            }
            return;

        }

        dfs(depth + 1, sum);
        sum.add(numbers[depth]);
        dfs(depth + 1, sum);
        sum.remove(sum.size()-1);
    }
}
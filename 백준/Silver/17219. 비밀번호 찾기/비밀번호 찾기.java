import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        int N = Integer.parseInt(input[0]);
        int M = Integer.parseInt(input[1]);

        Map<String, String> map = new HashMap<>();
        for (int i = 0; i < N; i++) {
            input = br.readLine().split(" ");
            map.put(input[0], input[1]);
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < M; i++) {
            String site = br.readLine();
            sb.append(map.get(site)).append('\n');
        }
        System.out.println(sb.toString());
    }
}
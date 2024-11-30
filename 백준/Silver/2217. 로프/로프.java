import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    static int answer = 0;

    public static void main(String args[]) throws IOException {
        int k = Integer.parseInt(br.readLine());

        List<Integer> numbers = new ArrayList<Integer>();

        for (int i = 0; i < k; i++) {
            numbers.add(Integer.valueOf(br.readLine()));
        }

        Collections.sort(numbers, Collections.reverseOrder());

        for (int i = 0; i < k; i++) {
            int tmp = numbers.get(i) * (i + 1);
            if (tmp > answer) {
                answer = tmp;
            }
        }

        System.out.println(answer);
    }

}
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        long[] nAndS = Stream.of(br.readLine().split(" ")).mapToLong(Long::parseLong).toArray();

        long n = nAndS[0];
        long s = nAndS[1];

        long answer = n+1;

        List<Long> numbers = Stream.of(br.readLine().split(" ")).map(Long::valueOf).collect(Collectors.toList());

        numbers.add(0, 0L);

        for (int i = 1; i < n+1; i++) {
            numbers.set(i, numbers.get(i) + numbers.get(i - 1));
        }

        int i = 0;
        int j = 0;
        while (i < n+1 && j < n+1) {
            long diff = numbers.get(j) - numbers.get(i);
            if (diff < s) {
                j++;
            } else {
                if (j - i <= answer) {
                    answer = j - i;
                }
                i++;
            }
        }

        if (answer == n+1) {
            System.out.println(0);
        } else {
            System.out.println(answer);
        }
    }
}
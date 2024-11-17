import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void main(String args[]) throws IOException {

        br.readLine();
        int[] numbers = Stream.of(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        HashSet<Integer> set = new HashSet<>();

        for (int n : numbers) {
            set.add(n);
        }

        for (Integer n : set.stream().sorted().collect(Collectors.toList())) {
            bw.write(n.toString());
            bw.write(" ");
        }
        bw.flush();
    }
}
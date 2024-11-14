
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.stream.Stream;

public class Main {


    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] lengths = br.readLine().split(" ");

        Integer[] A = Arrays.stream(br.readLine().split(" ")).map(Integer::valueOf).toArray(Integer[]::new);
        Integer[] B = Stream.of(br.readLine().split(" ")).map(Integer::valueOf).toArray(Integer[]::new);

        HashSet<Integer> setA = new HashSet(List.of(A));
        HashSet<Integer> setB = new HashSet(List.of(B));

        int answer = 0;

        for (Integer a : setA) {
            if (!setB.contains(a)) answer ++;
        }
        for (Integer b: setB) {
            if (!setA.contains(b)) answer++;
        }

        System.out.println(answer);
    }
}
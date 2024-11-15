import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class Main {

    private static int DEPTH = 6;
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void main(String args[]) throws IOException {

        while (true) {
            String[] line = br.readLine().split(" ");

            if (line.length == 1) {
                break;
            }

            List<Integer> array = Stream.of(line).map(Integer::valueOf).collect(Collectors.toList());

            for (int i = 1; i < array.get(0); i++) {
                Integer[] arrayForDfs = new Integer[DEPTH];
                arrayForDfs[0] = array.get(i);

                dfs(arrayForDfs, array.subList(1, array.size()), 1);
            }
            bw.write("\n");
        }
        bw.flush();

    }

    public static void dfs(Integer[] arrayForDfs, List<Integer> old, int depth) throws IOException {

        if (depth == DEPTH) {
            StringBuilder sb = new StringBuilder();
            for (Integer a : arrayForDfs) {
                sb.append(a);
                sb.append(" ");
            }
            sb.append("\n");
            bw.write(String.valueOf(sb));
            return;
        }

        for (Integer o : old) {
            if (o > arrayForDfs[depth - 1]) {
                arrayForDfs[depth] = o;
                dfs(arrayForDfs, old, depth + 1);
            }


        }

    }
}
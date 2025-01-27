
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayDeque;

public class Main {

    public static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    public static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    public static int N;

    public static ArrayDeque<Integer> queue = new ArrayDeque<>();

    public static void main(String args[]) throws IOException {
        N = Integer.parseInt(br.readLine());

        for (int i = 0; i < N; i++) {
            String[] cmd = br.readLine().split(" ");

            if (cmd[0].equals("push")) {
                queue.add(Integer.valueOf(cmd[1]));
            } else if (cmd[0].equals("front")) {
                if (!queue.isEmpty()) {
                    bw.write(queue.peekFirst().toString());
                } else {
                    bw.write("-1");
                }
            } else if (cmd[0].equals("back")) {
                if (!queue.isEmpty()) {
                    bw.write(queue.peekLast().toString());
                } else {
                    bw.write("-1");
                }
            } else if (cmd[0].equals("size")) {
                bw.write(String.valueOf(queue.size()));
            } else if (cmd[0].equals("empty")) {
                if (queue.isEmpty()) {
                    bw.write("1");
                } else {
                    bw.write("0");
                }
            } else if (cmd[0].equals("pop")) {
                if (queue.isEmpty()) {
                    bw.write("-1");
                } else {
                    bw.write(queue.removeFirst().toString());
                }
            }
            if (!cmd[0].equals("push"))
                bw.write("\n");
        }
        bw.flush();
    }

}
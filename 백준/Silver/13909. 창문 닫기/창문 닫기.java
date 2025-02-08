import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String args[]) throws IOException {
        int n = Integer.parseInt(br.readLine());

        int tmp;
        for (tmp = 1; tmp * tmp < n + 1; tmp += 1) {

        }

        System.out.println(tmp - 1);

    }

}

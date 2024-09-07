import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        Boolean[] sosu = new Boolean[10001];

        for (int i = 0; i < 10001; i++) {
            sosu[i] = true;
        }

        sosu[0] = false;
        sosu[1] = false;

        for (int i = 2; i < 10001; i++) {
            if (sosu[i]) {
                for (int j = i * 2; j < 10001; j += i) {
                    sosu[j] = false;
                }
            }
        }

        int T = Integer.parseInt(br.readLine());

        for (int i = 0; i < T; i++) {
            int n = Integer.parseInt(br.readLine());

            int c1 = 0;
            int c2 = 0;
            for (int j = 2; j < n / 2 + 1; j++) {
                if (sosu[j] && sosu[n - j]) {
                    c1 = j;
                    c2 = n - j;
                }
            }
            System.out.printf("%d %d%n", c1, c2);
        }
    }

}
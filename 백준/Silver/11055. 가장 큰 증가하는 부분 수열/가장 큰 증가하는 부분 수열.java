import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] dp = new int[N + 1];
        int[] I = new int[N + 1];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= N; i++) {
            I[i] = Integer.parseInt(st.nextToken());
        }

        dp[1] = I[1]; //초항처리
        //dp[i] : '부분'증가수열에서 'i번째 항'이 '최댓값'인 부분증가수열의 누적합
        for (int i = 1; i <= N; i++) {
            dp[i] = I[i]; // 디버깅하면서 알아가도 좋음.왜 이문장이 들어가야하는지.
            for (int j = 1; j < i; j++) {
                if (I[i] > I[j]) {
                    dp[i] = Math.max(dp[j] + I[i], dp[i]);
                }
            }
        }

        int max = Integer.MIN_VALUE;
        for (int i : dp) {
            max = Math.max(i, max);
        }
        System.out.println(max);

    }
}
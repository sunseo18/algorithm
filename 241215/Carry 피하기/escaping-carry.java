

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static int answer = 0;
    private static int length = 0;
    private static int[] numbers;

    public static void main(String[] args) throws IOException {        // 여기에 코드를 작성해주세요.

        length = Integer.parseInt(br.readLine());

        numbers = new int[length];

        for (int i = 0; i < length; i++) {
            numbers[i] = Integer.parseInt(br.readLine());

        }
        
        int[] array = new int[length];
        for (int i = 0; i < length; i++) {
            array[i] = 0;
        }
        dfs(array, -1, 0, 0);

        System.out.println(answer);
    }

    public static void dfs(int[] array, int last, int depth, int tmpCalc) {
        answer = Math.max(answer, depth);

        if (depth == length) {
            return;
        }

        for (int i = last + 1; i < length; i++) {
            // carry임
            int tmp = calcCarry(numbers[i] ,tmpCalc);
            if (tmp < 0) {
                continue;
            }

            array[depth] = numbers[i];
            dfs(array, i, depth + 1, tmp);
            array[depth] = 0;
        }
    }

    public static int calcCarry(int a, int b) {
        String smallerString = String.valueOf(Math.min(a, b));
        String biggerString = String.valueOf(Math.max(a, b));

        int minLength = smallerString.length();
        int lengthDiff = biggerString.length() - smallerString.length();

        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < lengthDiff; i++) {
            sb.append(biggerString.charAt(i));
        }

        for (int i = 0; i < minLength; i++) {
            int tmp = Integer.parseInt(String.valueOf(biggerString.charAt(i+lengthDiff)))
                    + Integer.parseInt(String.valueOf(smallerString.charAt(i)));

            if (tmp >= 10) {
                return -1;
            } else {
                sb.append(tmp);
            }
        }

            return Integer.parseInt(sb.toString());
    }
}
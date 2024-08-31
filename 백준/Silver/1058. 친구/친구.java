import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        ArrayList<String> friends = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            friends.add(br.readLine());
        }
        int answer = 0;
        for (int i = 0; i < n; i++) {
            int tmp = 0;
            ArrayList<Integer> realFriends = new ArrayList<>();
            for (int j = 0; j < n; j++) {
                // 한 다리 친구들 구하기
                if (j != i && friends.get(i).charAt(j) == 'Y') {
                    realFriends.add(j);
                    tmp += 1;
                }

            }
            ArrayList<Integer> secondFriends = new ArrayList<>();
            // 두 다리 친구들 구하기
            for (int one : realFriends) {
                for (int f = 0; f < n; f++) {
                    if (f != i && f != one && !realFriends.contains(f) && !secondFriends.contains(f) && friends.get(one).charAt(f) == 'Y') {
                        secondFriends.add(f);
                        tmp += 1;
                    }
                }
            }
            if (tmp > answer) {
                answer = tmp;
            }
        }

        System.out.println(answer);
    }
}
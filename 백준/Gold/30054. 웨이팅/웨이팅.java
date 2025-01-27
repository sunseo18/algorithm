import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.Queue;

public class Main {
    public static int answer = 0;
    public static int N;
    public static int maxTime;
    public static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    public static Map<Integer, Queue<Person>> vtMap = new HashMap<>();
    public static ArrayDeque<Person> waitingLine = new ArrayDeque<>();

    public static void main(String args[]) throws IOException {
        N = Integer.parseInt(br.readLine());
        Boolean[] rightOnTime = new Boolean[400001];
        int[] inLine = new int[400001];

        for (int i = 0; i < 400001; i++) {
            rightOnTime[i] = false;
        }

        for (int i = 0; i < 400001; i++) {
            inLine[i] = -1;
        }

        for (int i = 0; i < N; i++) {
            int[] rtVt = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

            maxTime = Math.max(maxTime, rtVt[0]);
            maxTime = Math.max(maxTime, rtVt[1]);

            // 입장 & 예약 시간 같으면 어짜피 대기 시간 0임
            if (rtVt[0] == rtVt[1]) {
                rightOnTime[rtVt[0]] = true;
            }

            if (vtMap.containsKey(rtVt[1])) {
                vtMap.get(rtVt[1]).add(new Person(rtVt[0], rtVt[1]));
            } else {
                Queue<Person> newQueue = new PriorityQueue<>();
                newQueue.add(new Person(rtVt[0], rtVt[1]));
                vtMap.put(Integer.valueOf(rtVt[1]), newQueue);
            }
        }

        for (int time = 1; time < 400001; time++) {

            // 제 시간에 온 사람 제외하고 줄세우기
            if (vtMap.containsKey(time)) {
                for (Person p : vtMap.get(time)) {
                    waitingLine.add(p);
                    inLine[p.reservationTime] = time;
                }
            }

            // 입장 시키기

            // 대기 줄이 있을 때
            if (!waitingLine.isEmpty()) {
                // 예약시간인 사람이 줄에 있으면
                if (inLine[time] != -1) {
                    answer = Math.max(answer, time - inLine[time]);
                    // 입장 처리
                    inLine[time] = -1;
                    continue;
                }

                // 입장한 사람이 줄에 있으면 삭제
                while (!waitingLine.isEmpty() && inLine[waitingLine.peek().reservationTime] == -1) {
                    waitingLine.removeFirst();
                }

                if (!waitingLine.isEmpty()) {
                    Person p = waitingLine.removeFirst();
                    inLine[p.reservationTime] = -1;
                    answer = Math.max(answer, time - p.visitTime);
                }
            }
            // 대기 줄 없으면 그냥 시간 보내기
        }

        System.out.println(answer);
    }

    public static class Person implements Comparable {
        int reservationTime;
        int visitTime;

        Person(int rt, int vt) {
            this.reservationTime = rt;
            this.visitTime = vt;
        }

        @Override
        public int compareTo(Object o) {

            if (this.reservationTime > ((Person) o).reservationTime) {
                return 1;
            } else if (this.reservationTime == ((Person) o).reservationTime) {
                return 0;
            } else {
                return -1;
            }
        }
    }
}
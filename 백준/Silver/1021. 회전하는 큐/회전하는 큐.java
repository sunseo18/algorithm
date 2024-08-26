import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.stream.Stream;

class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String firstLine = br.readLine();

        String[] splittedFirstLine = firstLine.split(" ");
        int n = Integer.parseInt(splittedFirstLine[0]);
        int m = Integer.parseInt(splittedFirstLine[1]);

        LinkedList<Integer> deque = new LinkedList<>();
        for (int i = 0; i < n; i++) {
            deque.offerLast(i + 1);
        }

        int[] splittedSecondLine = Stream.of(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int answer = 0;
        for (int elementsToFind : splittedSecondLine) {

            int indexOfElementsToFind = deque.indexOf(elementsToFind);

            int indexFromFirst = indexOfElementsToFind;
            int indexFromLast = deque.size() - indexFromFirst;

            if (indexFromFirst <= indexFromLast) {
                for (int i = 0; i < indexFromFirst; i++) {
                    firstOperand(deque);
                }
                answer += indexFromFirst;
                deque.pollFirst();
            } else {
                for (int i = 0; i < indexFromLast; i++) {
                    secondOperand(deque);
                }
                answer += indexFromLast;
                deque.pollFirst();
            }
        }

        System.out.println(answer);
    }

    public static void firstOperand(LinkedList<Integer> deque) {
        int first = deque.pollFirst();
        deque.offerLast(first);
    }

    public static void secondOperand(LinkedList<Integer> deque) {
        int last = deque.pollLast();
        deque.offerFirst(last);
    }
}
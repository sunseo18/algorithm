import java.io.*;
import java.util.*;
public class Main {

    public static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    public static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    public static int answerNo = 0;
    public static ArrayList<Integer> answerList = new ArrayList<>();

    public static void main(String[] args) throws IOException {

        int ALength = Integer.parseInt(br.readLine());
        ArrayList<Integer> A = new ArrayList();

        for (int i = 0; i < ALength; i++ ) {
            A.add(Integer.valueOf(br.readLine().trim()));
        }

        int BLength = Integer.parseInt(br.readLine());
        ArrayList<Integer> B = new ArrayList();

        for (int i = 0; i < BLength; i++ ) {
            B.add(Integer.valueOf(br.readLine().trim()));
        }

        Collections.sort(B);

        for (int i = 0; i < ALength - BLength + 1; i++) {
            boolean flag = true;

            int[] subArray = new int[BLength];

            for (int k = 0; k < BLength; k++) {
                subArray[k] = A.get(i+k);
            }

            Arrays.sort(subArray);

            int start = subArray[0] - B.get(0);

            for (int j = 1; j < BLength; j++) {
                if ( subArray[j] - B.get(j) != start) {
                    flag = false;
                }
            }

            if (flag) {
                answerNo++;
                answerList.add(i+1);
            }

        }

        bw.write(String.valueOf(answerNo));
        bw.write('\n');
        for (Integer no: answerList) {
            bw.write(String.valueOf(no));
            bw.write('\n');
        }
        bw.flush();
    }
}
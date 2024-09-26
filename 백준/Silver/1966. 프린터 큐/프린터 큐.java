import java.util.*;
import java.io.*;


public class Main {
    public static void main(String[] args) throws IOException{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.parseInt(br.readLine());

        for ( int i = 0; i < t ; i++ ) {

            String[] firstLine = br.readLine().split(" ");

            int length = Integer.parseInt(firstLine[0]);
            int question = Integer.parseInt(firstLine[1]);


            String[] secondLine = br.readLine().split(" ");
            int n = 0;

            ArrayList<Printer> printerList = new ArrayList();
            ArrayList<Printer> importance = new ArrayList();

            for (String s: secondLine) {
                printerList.add(new Printer(n, Integer.parseInt(s)));
                importance.add(new Printer(n, Integer.parseInt(s)));
                n++;
            }


            Collections.sort(importance);

            int cnt = 0;
            while (printerList.size() != 0) {
                Printer cur = printerList.get(0);
                Printer maxImportance = importance.get(0);

                if (cur.importance == maxImportance.importance) {
                    printerList.remove(0);
                    importance.remove(0);
                    cnt++;

                    if (cur.number == question) {
                        System.out.println(cnt);
                        break;
                    }
                } else {
                    Printer p = printerList.remove(0);
                    printerList.add(p);
                }
            }
        }
    }

    public static class Printer implements Comparable<Printer> {
        public int number;
        public int importance;

        public Printer(int number, int importance) {
            this.number = number;
            this.importance = importance;
        }

        @Override
        public int compareTo(Printer p) {
            if (this.importance < p.importance) {
                return 1;
            }
            else if (this.importance > p.importance) {
                return -1;
            }
            else {
                if (this.number > p.number) {
                    return 1;
                } else if (this.number < p.number) {
                    return -1;
                }
                return 0;
            }
        }
    }
}



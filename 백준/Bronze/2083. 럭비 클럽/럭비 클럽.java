import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        while (true) {
            String sentance = br.readLine();

            StringTokenizer st = new StringTokenizer(sentance);
            
            String name = st.nextToken();
            int age = Integer.parseInt(st.nextToken());
            int weight = Integer.parseInt(st.nextToken());

            if (name.equals("#") && age == 0 && weight == 0)
                break;


            String juniorOrSenior = "Junior";

            
            if (age > 17 || weight >= 80 ){
                juniorOrSenior = "Senior";
            }

            
            bw.write(String.format("%s %s", name, juniorOrSenior));
            bw.write('\n');
            
        }
        bw.flush();
        bw.close();
    }
}
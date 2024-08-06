import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        String number = "";
        while (true) {
            int answer = 2;
            number = br.readLine();

            if (number.equals("0"))
                break;

            for (int i = 0; i < number.length(); i++) {
                if (number.charAt(i) == '1') 
                    answer += 2;
                else if (number.charAt(i) == '0')
                    answer += 4;
                else
                    answer += 3;
            }
            answer += (number.length() - 1);

            bw.write(Integer.toString(answer));
            bw.newLine();
        
        }
        
        bw.flush();
        bw.close();
    }
}
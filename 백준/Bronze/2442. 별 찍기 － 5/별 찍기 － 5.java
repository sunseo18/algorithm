import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        int n = sc.nextInt();

        for(int i = 0; i < n; i++) {
            for(int blank = 0; blank < n-i-1; blank++) {
                bw.write(' ');
            }
            for(int star = 0; star < 2*i + 1; star++) {
                bw.write('*');
            }
            bw.write('\n');
        }

        bw.flush();
        bw.close();
    }
}
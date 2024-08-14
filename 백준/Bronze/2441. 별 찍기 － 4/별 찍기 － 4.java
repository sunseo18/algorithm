import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        int n = sc.nextInt();

        int space = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < space; j++) {
                bw.write(" ");
            }
            for (int k = 0; k < n-space; k++) {
                bw.write("*");
            }
            bw.write("\n");
            space ++;
            
        }

        bw.flush();
        bw.close();
    }
}
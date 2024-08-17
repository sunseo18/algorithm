import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args)throws IOException {

        Scanner sc = new Scanner(System.in);

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        int n = sc.nextInt();

        for (int i = 0; i < n; i++){
            for (int space = 0; space < i; space++) {
                bw.write(' ');
            }
            for (int star = 0; star < 2*n-i*2-1; star++) {
                bw.write('*');
            }
            bw.newLine();
        }

        bw.flush();
        bw.close();
    }
}
import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        int total = 0;
        
        for(int i = 0; i < n; i++) {
            int x = Integer.parseInt(br.readLine());  
            if (total != 0) {
                total--;
            }
            total+=x;
        }

        System.out.println(total);

    }
}
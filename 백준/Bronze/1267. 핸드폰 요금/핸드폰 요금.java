import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {

    static int Y = 30;
    static int M = 60;
    
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int number = Integer.parseInt(br.readLine());

        int[] timeArray = new int[number];

        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i = 0; i < number; i++) {
            timeArray[i] = Integer.parseInt(st.nextToken());
        }

        int countY = 0;
        int countM = 0;

        int amountY = 0;
        int amountM = 0;
        
        for (int i = 0; i < number; i++) {
            countY = timeArray[i] / Y;
            countM = timeArray[i] / M;
            
            countY++;
            countM++;

            amountY += countY * 10;
            amountM += countM * 15;

        }

        if (amountM == amountY) 
            System.out.println(String.format("Y M %d", amountM));
        else if (amountM > amountY)
            System.out.println(String.format("Y %d", amountY));
        else
            System.out.println(String.format("M %d", amountM));
            
        }
}
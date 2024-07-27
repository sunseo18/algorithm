import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        while (true) {
            String sentance = sc.nextLine();

            if (sentance.equals("#"))
                break;

            int moeum = 0;

            for (int i = 0; i < sentance.length(); i++ ){
                char lowerChar = Character.toLowerCase(sentance.charAt(i));

                if (lowerChar == 'a' || lowerChar == 'e' || lowerChar == 'i' || lowerChar== 'o' || lowerChar == 'u') {
                    moeum++;
                }

            }
            System.out.println(moeum);
        }
    }
}
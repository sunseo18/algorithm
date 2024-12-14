import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));


    public static void main(String[] args) throws IOException
    {

        String binary = br.readLine();
        String thirdary = br.readLine();


        int min = (int) Math.pow(2, (binary.length()-1));
        int max = (int) Math.pow(2, binary.length())  - 1;

        for (int number = min; number < max+1; number++) {
            String tmp =  Integer.toString(number,3);
            if (check(tmp, thirdary)) {
                System.out.println(Integer.parseInt(tmp, 3));
            }
        }

    }

    public static boolean check(String a, String b) {
        int diff = 0;

        if (a.length() != b.length() )
            return false;

        for ( int i = 0; i < a.length(); i++) {
            if ( a.charAt(i) != b.charAt(i)) diff++;
            if (diff > 1) 
                return false;
        }

        if (( a.length() == b.length() ) && diff == 1)
            return true;
        return false;
    }
}
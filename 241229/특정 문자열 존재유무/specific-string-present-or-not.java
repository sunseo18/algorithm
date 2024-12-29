import java.io.*;

public class Main {
    public static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    public static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void main(String[] args) throws IOException {
        String[] firstLine = br.readLine().split(" ");    

        int length = Integer.parseInt(firstLine[0]);
        String containWord = firstLine[1];

        for ( int i = 0; i < length; i++ ) {
            String word = br.readLine();
            if (word.contains(containWord) ) {
                bw.write(word);
                bw.write('\n');
            }
        }
        bw.flush();
    }
}
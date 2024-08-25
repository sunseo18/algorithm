import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) throws IOException{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String n = br.readLine();
        int lengthOfA = Integer.parseInt(n);

        String a = br.readLine();
        StringTokenizer st = new StringTokenizer(a, " ");

        int[] aArray = new int[lengthOfA];
        int[] pArray = new int[lengthOfA];
        
        int i = 0;
        while (st.hasMoreTokens()) {
            aArray[i] = Integer.parseInt(st.nextToken());
            i++;
        }

        int[] sortedAArray = aArray.clone();
        Arrays.sort(sortedAArray);
        
        int pIndex = 0;
        for (int j = 0; j < lengthOfA; j++) {
            for (int k = 0; k < lengthOfA; k++) {
                if (sortedAArray[k] == aArray[j]) {
                    pArray[pIndex] = k;
                    sortedAArray[k] = -1;
                    pIndex++; 
                    break;
                }
            }
        }

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        for (int p : pArray){
            bw.write(Integer.toString(p));
            bw.write(' ');
        }
        
        bw.flush();
        bw.close();
    }
}
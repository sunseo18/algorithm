import java.util.*;
import java.io.*;
import java.util.stream.*;

public class Main {
  public static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  public static int N;
  public static int k;
  public static Integer[] sensors;
  public static Integer[] diff;
  public static long answer = 0;
  
  public static void main(String[] args) throws IOException {
      N = Integer.parseInt(br.readLine());
      k = Integer.parseInt(br.readLine());
      
      int[] line = Stream.of(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();    
      sensors = new Integer[N];
      for ( int i = 0 ; i < N; i++) sensors[i] = line[i];
      
      Set<Integer> sensorsSet = new HashSet<Integer>(Arrays.asList(sensors));

      // 중복 제거된 센서
      sensors = sensorsSet.toArray(new Integer[0]);
      Arrays.sort(sensors);
      
      diff = new Integer[sensors.length-1];
      for ( int i = 0; i < sensors.length-1; i++) {
        diff[i] = sensors[i+1]-sensors[i];
      }
      
      Arrays.sort(diff, Comparator.reverseOrder());

      for ( int i = k-1; i < diff.length; i++ ){
        answer += diff[i];
      }
      
      System.out.println(answer);
  }
}
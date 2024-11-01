import java.io.*;
import java.util.*;

public class Main {
    
  private static long minStart;
  private static long maxEnd;
  private static long answer = 0;
  
  private final static int PARTIALLY_LONGER = 1;
  private final static int TOTALLY_SMALLER = 2;
  private final static int TOTALLY_NEW = 3;
    
  public static void main(String args[]) throws IOException{
    

    BufferedReader br  = new BufferedReader(new InputStreamReader(System.in));
    
    int N = Integer.parseInt(br.readLine());

    ArrayList<Line> lineList = new ArrayList<>();
    
    for (int i = 0; i < N; i++ ){
        String[] a = br.readLine().split(" ");
        
        long start = Long.parseLong(a[0]);
        long end = Long.parseLong(a[1]);
        
        lineList.add(new Line(start, end));
    }
    
    Collections.sort(lineList);

    
    minStart = lineList.get(0).start;
    maxEnd = lineList.get(0).end;
    answer = maxEnd - minStart;
    
    
    for (int i = 1; i < N; i++) {
        int type = checkType(minStart, maxEnd, lineList.get(i));
        
        if (type == PARTIALLY_LONGER) {
            answer += lineList.get(i).end - maxEnd;
            maxEnd = lineList.get(i).end;
        }
        else if (type == TOTALLY_NEW) {
            answer += lineList.get(i).end - lineList.get(i).start;
            minStart = lineList.get(i).start;
            maxEnd = lineList.get(i).end;
        }
    
        
    }
    
    System.out.println(answer);
    
  }
  
  public static int checkType(long minStart, long maxEnd, Line line) {
      if(maxEnd >= line.start && line.start >= minStart) {
          if (line.end <= maxEnd) 
            return TOTALLY_SMALLER;
          if ( line.end > maxEnd) 
            return PARTIALLY_LONGER;
      }
      if (line.start > maxEnd) {
          return TOTALLY_NEW;
      }
      return 0;
  }
  
  public static class Line implements Comparable {
      public long start;
      public long end;
      
      public Line(long start, long end) {
          this.start = start;
          this.end = end;
      }
      
        @Override
        public int compareTo(Object o) {
            Line line = (Line) o;
            if (line.start > this.start) {
                return -1;
            } else if (line.start == this.start) {
                if (line.end > this.end) {
                    return -1;
                } else if (line.end == this.end) {
                    return 0;
                } else {
                    return 1;
                }
            }
            return 1;
        }
      
  }
}
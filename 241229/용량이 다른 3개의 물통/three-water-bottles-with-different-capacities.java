import java.io.*;

public class Main {
    public static long[] bottleMax = new long[3];
    public static long[] bottleWaterAmount = new long[3];
    public static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException{
        String[] firstLine = br.readLine().split(" ");
        bottleMax[0] = Long.parseLong(firstLine[0]);
        bottleWaterAmount[0] = Long.parseLong(firstLine[1]);

        String[] secondLine = br.readLine().split(" ");
        bottleMax[1] = Long.parseLong(secondLine[0]);
        bottleWaterAmount[1] = Long.parseLong(secondLine[1]);

        String[] thirdLine = br.readLine().split(" ");
        bottleMax[2] = Long.parseLong(thirdLine[0]);
        bottleWaterAmount[2] = Long.parseLong(thirdLine[1]);

        for (int i = 0; i < 100; i++) {
            if ( i % 3 == 0 ) {
                moveWater(0, 1);
            } else if  (i % 3 == 1) {
                moveWater(1, 2);
            } else {
                moveWater(2, 0);
            }
        }
        
        for(long waterAmount: bottleWaterAmount) {
            System.out.println(waterAmount);
        }
    }

    public static void moveWater(int from, int to) {
        long leftAmount = bottleMax[to] - bottleWaterAmount[to];

        if (leftAmount < bottleWaterAmount[from]) {
            bottleWaterAmount[from] -= leftAmount;
            bottleWaterAmount[to] += leftAmount;
        } else{ 
            bottleWaterAmount[to] += bottleWaterAmount[from];
            bottleWaterAmount[from] = 0;
        }
    }
}
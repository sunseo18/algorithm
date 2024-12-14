import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        int[] arr = new int[a.length()]; // 10진수를 저장할 배열
        int res = Integer.MIN_VALUE; 

        for(int i = 0; i < a.length(); i++){
            char c = a.charAt(i);
            if(c == '1')
                c = '0';
            else if(c == '0')
                c = '1';

			// 비트 반전시킨 이진수 문자열 binary 변수에 저장
            String binary = a.substring(0, i) + c + a.substring(i+1); 
            
            // 2진수 → 10진수로 변환하여 배열에 저장
            arr[i] = Integer.parseInt(binary, 2);
        }

		// 배열에 저장된 10진수 값 중 최대값 찾아 출력
        for(int i = 0; i < a.length(); i++)
            res = Math.max(res, arr[i]);
        System.out.print(res);
    }
}
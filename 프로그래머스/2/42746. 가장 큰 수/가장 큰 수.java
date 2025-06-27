import java.util.*;

class Solution {
    public String solution(int[] numbers) {
        String[] sNumbers = new String[numbers.length];
        for (int i = 0; i < numbers.length; i++) {
            sNumbers[i] = String.valueOf(numbers[i]);
        }
        
        Arrays.sort(sNumbers, (a, b) -> (b + a).compareTo(a + b));
        
        // 가장 큰 수가 0인 경우
        if (sNumbers[0].equals("0")) return "0";
        
        StringBuilder answer = new StringBuilder();
        for (String s: sNumbers) {
            answer.append(s);
        }
        
        return answer.toString();
    }
}
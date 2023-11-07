import java.util.Arrays;

class Solution {
    public int solution(int[] numbers) {
        Arrays.sort(numbers);
        
        int right = numbers[numbers.length-1] * numbers[numbers.length-2]; 
        int left = numbers[0] * numbers[1];
        int answer = right > left ? right : left;
        return answer;
    }
}
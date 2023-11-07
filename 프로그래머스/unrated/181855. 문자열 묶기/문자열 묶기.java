import java.util.Arrays;

class Solution {
    public int solution(String[] strArr) {
        int[] count = new int[30];
        for (String s: strArr) {
            count[s.length()-1] += 1;
        }
        
        int answer = Arrays.stream(count).max().getAsInt();;
        return answer;
    }
}
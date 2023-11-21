import java.util.Arrays;

class Solution {
    public int solution(String before, String after) {
        int answer = 1;
        String[] before_s = before.split("");
        String[] after_s = after.split("");
        
        Arrays.sort(before_s);
        Arrays.sort(after_s);
        for (int i = 0; i < before_s.length; i++) {
            if (!before_s[i].equals(after_s[i])) {
                answer = 0;
                break;
            }
        }
        return answer;
    }
}
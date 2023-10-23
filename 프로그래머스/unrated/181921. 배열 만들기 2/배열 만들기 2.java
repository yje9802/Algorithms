import java.util.*;

class Solution {
    public List solution(int l, int r) {
        List<Integer> answer = new ArrayList<>();
        for (int i = l; i <= r; i++) {
            String str_i = "" + i;
            int count = 0;
            for (int s = 0; s < str_i.length(); s++) {
                if (str_i.charAt(s) == '0' || str_i.charAt(s) == '5') {
                    count++;
                }
            }
            if (count == str_i.length()) {
                answer.add(i);
            }
        }
        if (answer.isEmpty()) {
            answer.add(-1);
        }
        return answer;
    }
}
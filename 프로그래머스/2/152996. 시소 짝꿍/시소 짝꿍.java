import java.util.*;

class Solution {
    public long solution(int[] weights) {
        long answer = 0;
        
        Arrays.sort(weights);
        Map<Integer, Integer> cnt = new HashMap<>();
        
        for (int w: weights) {
            // 1:1
            answer += cnt.getOrDefault(w, 0);
            // 1:2
            if (w % 2 == 0) {
                answer += cnt.getOrDefault(w/2, 0);
            }
            // 2:3
            if (w % 3 == 0) {
                answer += cnt.getOrDefault(w*2/3, 0);
            }
            // 3:4
            if (w % 4 == 0) {
                answer += cnt.getOrDefault(w*3/4, 0);
            }
            
            cnt.put(w, cnt.getOrDefault(w, 0) + 1);
        }
        return answer;
    }
}
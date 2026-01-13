import java.util.*;

class Solution {
    public int solution(int[][] targets) {
        int answer = 0;
        
        Arrays.sort(targets, (o1, o2) -> (o1[1] - o2[1])); // e 기준 오름차순 정렬
        
        int curr = -1;
        
        for (int[] target: targets) {
            int s = target[0], e = target[1];
            if (curr < s) {
                curr = e - 1;
                answer++;
            }
        }
        
        return answer;
    }
}
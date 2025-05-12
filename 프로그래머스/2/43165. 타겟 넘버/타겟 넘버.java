import java.util.*;

class Solution {
    public int solution(int[] numbers, int target) {
        int answer = 0;
        
        Queue<int[]> queue = new LinkedList<>(); // [현재 합계, 인덱스]
        queue.offer(new int[]{0, 0});
        
        while (!queue.isEmpty()) {
            int[] curr = queue.poll();
            int currTotal = curr[0];
            int currIdx = curr[1];
            
            if (currIdx == numbers.length) {
                if (currTotal == target) {
                    answer++;
                }
            } else {
                queue.offer(new int[]{currTotal + numbers[currIdx], currIdx + 1});
                queue.offer(new int[]{currTotal - numbers[currIdx], currIdx + 1});
            }
        }
        
        return answer;
    }
}
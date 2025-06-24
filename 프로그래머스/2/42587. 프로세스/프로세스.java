import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        int answer = 0;
        
        Queue<int[]> queue = new LinkedList<>();
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder()); // 우선순위 순서 파악
        for (int i = 0; i < priorities.length; i++) {
            queue.add(new int[]{priorities[i], i});
            pq.add(priorities[i]);
        }
        
        while (!queue.isEmpty()) {
            int[] curr = queue.poll();
            if (curr[0] == pq.peek()) {
                answer++;
                pq.poll();
                if (curr[1] == location) {
                    return answer;
                }
            } else {
                queue.add(curr);
            }
        }
        
        return answer;
    }
}
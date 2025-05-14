import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        
        // scoville을 우선순위큐로 만들기
        Queue<Integer> pq = new PriorityQueue<>();
        for (int i = 0; i < scoville.length; i++) {
            pq.offer(scoville[i]);
        }
        
        while (!pq.isEmpty()) {
            int first = pq.poll();
            
            if (first >= K) break;
            
            if (pq.isEmpty()) {
                answer = -1;
                break;
            } 
            
            int second = pq.poll();
            pq.offer(first + (second * 2));
            answer++;
        }
        
        return answer;
    }
}
import java.util.*;

class Solution {
    public int solution(int n, int k, int[] enemy) {
        int answer = 0;
        Queue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder()); // 각 라운드마다 소모한 병사 수 저장
        
        int i = 0;
        while (i < enemy.length) {
            int curr = enemy[i]; // 이번에 소모한 병사 수
            pq.offer(curr);
            n -= curr;
            
            if (n < 0) {
                if (k == 0) break; // 더이상 무족권을 쓸 수도 병사를 소모할 수도 없음 -> 종료
                
                n += pq.poll();
                k--;
            }
            
            i++;
            answer++;
        }
        
        return answer;
    }
}
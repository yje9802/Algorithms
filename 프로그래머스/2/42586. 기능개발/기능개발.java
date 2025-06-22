import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        List<Integer> answer = new ArrayList<>();
        
        Queue<Integer> daysNeeded = new LinkedList<>();
        for (int i = 0; i < progresses.length; i++) {
            int remaining = 100 - progresses[i];
            daysNeeded.add((int) Math.ceil((double) remaining / speeds[i]));
        }
        
        int count = 1;
        int current = daysNeeded.poll(); // 먼저 배포되어야 하는 작업의 완료 시점
        while(!daysNeeded.isEmpty()) {
            int next = daysNeeded.poll();
            if (next <= current) {
                count++;
            } else {
                answer.add(count);
                current = next;
                count = 1;
            }
        }
        answer.add(count);
        
        return answer.stream().mapToInt(i -> i).toArray();
    }
}
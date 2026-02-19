import java.util.*;

class Solution {
    public int solution(int[][] board, int[] moves) {
        int answer = 0;
        
        List<Queue<Integer>> boardList = new ArrayList<>(); // 기존 board를 변형
        for (int i = 0; i < board.length; i++) {
            boardList.add(new LinkedList<>());
        }
        
        for (int[] basket: board) {
            for (int d = 0; d < basket.length; d++) {
                if (basket[d] != 0) boardList.get(d).offer(basket[d]);
            }
        }
        
        Deque<Integer> dolls = new LinkedList<>(); // 뽑은 인형 저장
        
        for (int move: moves) {
            if (!boardList.get(move-1).isEmpty()) { // 뽑을 수 있는 인형이 남아있다면
                Integer poppedOut = boardList.get(move-1).poll(); // 지금 뽑은 인형
                
                if (!dolls.isEmpty() && dolls.peekLast() == poppedOut) {
                    dolls.pollLast();
                    answer += 2;
                } else {
                    dolls.offerLast(poppedOut);
                }
            }
        }
        
        return answer;
    }
}
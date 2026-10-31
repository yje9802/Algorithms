import java.util.*;

class Solution {
    public String solution(String number, int k) {
        String answer = "";
        
        Deque<Character> stack = new LinkedList<>();
        for (char num: number.toCharArray()) {
            while (!stack.isEmpty() && k > 0 && stack.getLast() < num) {
                stack.pollLast();
                k--;
            }
            stack.offer(num);
        }
        
        // 아직 k만큼 숫자를 제거하지 못함
        while (k > 0){
            stack.pollLast();
            k--;
        }
        
        StringBuilder sb = new StringBuilder();
        for (char ch: stack) {
            sb.append(ch);
        }
        answer = sb.toString();
        
        return answer;
    }
}
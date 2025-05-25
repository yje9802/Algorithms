import java.util.*;

class Solution {
    public String solution(String number, int k) {
        Deque<Character> stack = new ArrayDeque<>();
        
        for (char digit: number.toCharArray()) {
            while (!stack.isEmpty() && k > 0 && stack.peekLast() < digit) {
                stack.removeLast();
                k--;
            }
            stack.addLast(digit);
        }
        
        // 아직 k개 만큼 다 제거하지 못 했다면
        while (k > 0) {
            stack.removeLast();
            k--;
        }
        
        StringBuilder answer = new StringBuilder();
        for (char ch : stack) {
            answer.append(ch);
        }
        
        return answer.toString();
    }
}
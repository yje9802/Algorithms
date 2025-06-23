import java.util.*;

class Solution {
    boolean solution(String s) {
        if (s.charAt(s.length()-1) == '(') {
            return false;
        }
        
        Queue<Character> stack = new LinkedList<>();
        char[] charS = s.toCharArray();
        for (int i = s.length()-1; i >= 0; i--) {
            if (charS[i] == ')') {
                stack.add(charS[i]);
            } else {
                if (!stack.isEmpty()) {
                    stack.poll();
                } else {
                    return false;
                }
            }
        }
        if (!stack.isEmpty()) {
            return false;
        }

        return true;
    }
}
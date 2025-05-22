import java.util.*;

class Solution {
    public int solution(String begin, String target, String[] words) {
        int answer = 0;
        
        Queue<WordNode> queue = new LinkedList<>();
        Set<String> set = new HashSet<>(Arrays.asList(words));
        
        if (!set.contains(target)) {
            return answer;
        }
        
        queue.offer(new WordNode(begin, 0));
        
        while (!queue.isEmpty()) {
            WordNode currNode = queue.poll();
            String curr = currNode.word;
            int step = currNode.step;
            
            if (curr.equals(target)) {
                return step;
            }
            
            for (String word: words) {
                int diffChar = 0; // curr와 word 중 알파벳이 다른 부분의 수
                for (int i = 0; i < word.length(); i++) {
                    if (word.charAt(i) != curr.charAt(i)) {
                        diffChar++;
                    }
                }
                
                if (diffChar == 1) {
                    queue.offer(new WordNode(word, step+1));
                }
            }
        }
        
        return answer;
    }
    
    class WordNode {
        String word;
        int step;
        
        WordNode(String word, int step) {
            this.word = word;
            this.step = step;
        }
    }
}
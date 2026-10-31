import java.util.*;

class Solution {
    public int solution(String begin, String target, String[] words) {
        int answer = 0;
        
        Set<String> set = new HashSet<>(Arrays.asList(words));
        // words에 target이 없으면 변환 불가능
        if (!set.contains(target)) return answer;
        
        Queue<WordNode> queue = new LinkedList<>();
        queue.offer(new WordNode(begin, 0));
        
        // BFS 탐색
        while(!queue.isEmpty()) {
            WordNode currNode = queue.poll();
            String curr = currNode.word;
            int step = currNode.step;
            
            if (curr.equals(target)) return step;
            
            for (String word: set) {
                int diff = 0; // curr와 word의 다른 부분 개수
                for (int i = 0; i < curr.length(); i++) {
                    if (curr.charAt(i) != word.charAt(i)) {
                        diff++;
                    }
                }
                
                if (diff == 1) {
                    queue.offer(new WordNode(word, step+1));
                }
            }
        }
        
        return answer;
    }
    
    class WordNode {
        String word;
        int step; // 현재 몇 단계인지
        
        WordNode(String word, int step) {
            this.word = word;
            this.step = step;
        }
    }
}
import java.util.*;

class Solution {
    public int[] solution(String[] name, int[] yearning, String[][] photo) {
        int n = photo.length; // 사진 개수
        int[] answer = new int[n];
        
        Map<String, Integer> scores = new HashMap<>();
        for (int i = 0; i < name.length; i++) {
            scores.putIfAbsent(name[i], yearning[i]);
        }
        
        for (int i = 0; i < n; i++) {
            int total = 0;
            for (String nm: photo[i]) {
                if (scores.containsKey(nm)) total += scores.get(nm);
            }
            answer[i] = total;
        }
        
        return answer;
    }
}
import java.util.*;

class Solution {
    public int solution(int k, int[] tangerine) {
        int answer = 0;
        
        Map<Integer, Integer> map = new HashMap<>();
        for (int tan: tangerine) {
            map.put(tan, map.getOrDefault(tan, 0) + 1);
        }
        List<Map.Entry<Integer, Integer>> list = new ArrayList<>(map.entrySet());
        list.sort((a, b) -> Integer.compare(b.getValue(), a.getValue()));
        
        for (Map.Entry<Integer, Integer> entry: list) {
            Integer cnt = entry.getValue();
            k -= cnt;
            answer++;
            if (k <= 0) break;
        }
        return answer;
    }
}
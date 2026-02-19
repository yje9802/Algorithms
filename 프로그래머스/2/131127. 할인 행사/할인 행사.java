import java.util.*;

class Solution {
    public int solution(String[] want, int[] number, String[] discount) {
        int answer = 0;
        
        int n = want.length; // 원하는 제품 종류의 개수
        
        for (int i = 0; i <= discount.length-10; i++) {
            Map<String, Integer> counts = getCounts(i, discount);
            boolean possible = true;
            for (int j = 0; j < n; j++) {
                if (!counts.containsKey(want[j])) {
                    possible = false;
                    break;
                }
                if (counts.get(want[j]) < number[j]) {
                    possible = false;
                    break;
                }
            }
            if (possible) answer++;
        }
        
        return answer;
    }
    
    private Map<String, Integer> getCounts(int start, String[] discount) {
        Map<String, Integer> counts = new HashMap<>(); // 할인 받을 수 있는 제품: 수량
        for (int i = start; i < start+10; i++) {
            counts.put(discount[i], counts.getOrDefault(discount[i], 0) + 1);
        }
        return counts;
    }
}
import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        List<Integer> answer = new ArrayList<>();
        
        for (int a: arr) {
            if (answer.isEmpty()) {
                answer.add(a);
            } else {
                if (answer.get(answer.size()-1) != a) {
                    answer.add(a);
                }
            }
        }

        return answer.stream().mapToInt(i->i).toArray();
    }
}
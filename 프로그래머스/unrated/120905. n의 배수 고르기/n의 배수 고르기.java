import java.util.*;

class Solution {
    public int[] solution(int n, int[] numlist) {
        List<Integer> ntimes = new ArrayList<>();
        for (int i: numlist) {
            if (i % n == 0) {
                ntimes.add(i);
            }
        }
        
        int[] answer = new int[ntimes.size()];
        answer = ntimes.stream().mapToInt(i->i).toArray();
        return answer;
    }
}
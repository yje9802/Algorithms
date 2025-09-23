import java.util.*;

class Solution {
    public int solution(int[] diffs, int[] times, long limit) {
        int left = 1, right = Arrays.stream(diffs).max().getAsInt();
        int answer = right;
        
        while (left <= right) {
            int mid = (left + right) / 2;
            if (canSolve(mid, diffs, times, limit)) {
                answer = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return answer;
    }
    
    private boolean canSolve(int level, int[] diffs, int[] times, long limit) {
        long total = times[0];
        if (total > limit) return false;
        
        for (int i = 1; i < diffs.length; i++) {
            int k = Math.max(0, diffs[i] - level);
            total += (long) times[i] + (long) (times[i-1] + times[i]) * k;
            if (total > limit) return false;
        }
        return true;
    }
}
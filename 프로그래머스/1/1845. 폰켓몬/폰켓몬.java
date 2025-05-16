import java.util.*;

class Solution {
    public int solution(int[] nums) {
        Set<Integer> numsSet = new HashSet<>();
        for (int n: nums) {
            numsSet.add(n);
        }
        
        int answer = (numsSet.size() >= nums.length / 2) ? nums.length / 2 : numsSet.size();
        
        return answer;
    }
}
import java.util.*;

class Solution {
    public int[] solution(String[] intStrs, int k, int s, int l) {
        List<Integer> arr = new ArrayList<>();
        
        for (String intStr: intStrs) {
            int ss = Integer.parseInt(intStr.substring(s, s+l));
            if (ss > k) {
                arr.add(ss);
            }
        }
        int[] answer = arr.stream().mapToInt(i->i).toArray();
        return answer;
    }
}
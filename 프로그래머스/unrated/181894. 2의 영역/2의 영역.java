import java.util.*;

class Solution {
    public int[] solution(int[] arr) {
        List<Integer> index = new ArrayList<>();
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == 2) {
                index.add(i);
            }
        }
        int[] answer;
        if (index.size() == 0) {
            answer = new int[] {-1};
        } else {
            
            int first = index.get(0);
            int last = index.get(index.size() - 1);
            answer = Arrays.copyOfRange(arr, first, last + 1);
            
        }

        return answer;
    }
}
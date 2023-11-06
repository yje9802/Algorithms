import java.util.ArrayList;

class Solution {
    public int[] solution(int[] arr) {
        ArrayList<Integer> stk = new ArrayList<>();
        int i = 0;
        while (i < arr.length) {
            if (stk.size() == 0) {
                stk.add(arr[i]);
            } else {
                if (stk.get(stk.size()-1) == arr[i]) {
                    stk.remove(stk.size()-1);
                } else {
                    stk.add(arr[i]);
                }
            }
            i++;
        }
        int[] answer;
        if (stk.size() == 0) {
            answer = new int[] {-1};
        } else {
            answer = stk.stream().mapToInt(n->n).toArray();
        }
        return answer; 
    }
}
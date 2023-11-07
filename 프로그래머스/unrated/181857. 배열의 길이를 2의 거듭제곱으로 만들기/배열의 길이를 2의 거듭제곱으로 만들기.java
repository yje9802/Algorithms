import java.util.ArrayList;

class Solution {
    public int[] solution(int[] arr) {
        ArrayList<Integer> list = new ArrayList<>();
        int i = 0;
        while (arr.length > Math.pow(2, i)) {
            i++;
        }
        
        for (int j = 0; j < Math.pow(2, i); j++) {
            if (j < arr.length) {
                list.add(arr[j]);
            } else {
                list.add(0);
            }
        }
        
        int[] answer = list.stream().mapToInt(a->a).toArray();
        return answer;
    }
}
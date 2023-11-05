import java.util.ArrayList;

class Solution {
    public int[] solution(int[] arr, boolean[] flag) {
        ArrayList<Integer> list = new ArrayList<>();
        for (int i = 0; i < arr.length; i++) {
            if (flag[i] == true) {
                for (int j = 0; j < arr[i]*2; j++) {
                    list.add(arr[i]);
                }
            } else {
                for (int k = 0; k < arr[i]; k++) {
                    list.remove(list.size()-1);
                }
            }
        }
        
        int[] answer = list.stream().mapToInt(i->i).toArray();
        return answer;
    }
}
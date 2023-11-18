import java.util.ArrayList;

class Solution {
    public int[] solution(int[] arr, int[] delete_list) {
        int[] answer;
        
        ArrayList<Integer> arrAnswer = new ArrayList<>();

        for (int i = 0; i < arr.length; i++) {
            boolean except = true;
            for (int j = 0; j < delete_list.length; j++) {
                if (arr[i]==delete_list[j]) {
                    except = false;
                    break;
                }
            }
            if (except == true) {
                arrAnswer.add(arr[i]);
            }
        }
        answer = arrAnswer.stream().mapToInt(i->i).toArray();
        return answer;
    }
}
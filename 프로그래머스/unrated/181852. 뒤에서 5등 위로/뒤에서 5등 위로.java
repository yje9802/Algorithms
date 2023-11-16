import java.util.Arrays;

class Solution {
    public int[] solution(int[] num_list) {
        int[] answer = new int[num_list.length - 5];
        Arrays.sort(num_list);
        answer = Arrays.copyOfRange(num_list, 5, num_list.length);
        // answer = Arrays.stream(numList).sorted().skip(5).toArray();
        return answer;
    }
}
import java.util.stream.IntStream;

class Solution {
    public int[] solution(int[] arr, int k) {
        int[] answer = new int[k];
        
        int i = 0;
        int j = 0;
        while (i < arr.length) {
            int z = arr[i];
            if (i == 0 || !IntStream.of(answer).anyMatch(x -> x == z)) {
                answer[j] = arr[i];
                j++;
                if (j == k) {
                    break;
                }
            }
            i++;
        }
        if (j != k) {
            for (int a = j; a < k; a++) {
                answer[a] = -1;
            }
        }
        return answer;
    }
}
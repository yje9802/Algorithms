import java.util.*;

class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int[] answer = new int[queries.length];
        Arrays.fill(answer, Integer.MAX_VALUE);

        for (int q = 0; q < queries.length; q++) {
            int[] query = queries[q];
            for (int i = query[0]; i <= query[1]; i++) {
                if (arr[i] > query[2]) {
                    answer[q] = Math.min(answer[q], arr[i]);
                } 
            }
            if (answer[q] == Integer.MAX_VALUE) answer[q] = -1;
        }
        return answer;
    }
}
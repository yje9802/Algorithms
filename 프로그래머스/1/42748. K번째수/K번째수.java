import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        List<Integer> answer = new ArrayList<>();
        
        for (int[] command: commands) {
            int[] sliced = Arrays.copyOfRange(array, command[0]-1, command[1]);
            Arrays.sort(sliced);
            answer.add(sliced[command[2]-1]);
        }
        return answer.stream().mapToInt(i -> i).toArray();
    }
}
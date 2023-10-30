import java.lang.Math;

class Solution {
    public int solution(int[] array, int n) {
        int answer = array[0];
        int distance = Math.abs(n - array[0]);
        
        for (int i = 1; i < array.length; i++) {
            if (Math.abs(n - array[i]) < distance) {
                distance = Math.abs(n - array[i]);
                answer = array[i];
            } else if (Math.abs(n - array[i]) == distance && array[i] < answer) {
                answer = array[i];
            }
        }
            
        return answer;
    }
}
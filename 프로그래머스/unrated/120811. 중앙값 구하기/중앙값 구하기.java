import java.util.Arrays;
class Solution {
    public int solution(int[] arr) {
        int answer = 0;
        Arrays.sort(arr);
        answer = arr[arr.length/2];
        return answer;
    }
}
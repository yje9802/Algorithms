class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        
        int sum = 0;
        int multiple = 1;
        for (int i: num_list) {
            sum += i;
            multiple *= i;
        }
        if (sum*sum > multiple) {
            answer = 1;
        }
        return answer;
    }
}
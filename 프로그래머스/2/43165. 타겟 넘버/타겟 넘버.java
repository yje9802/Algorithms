class Solution {
    public int solution(int[] numbers, int target) {
        int answer = dfs(numbers, target, 0, 0);
        return answer;
    }
    
    int dfs(int[] numbers, int target, int curr, int idx) {
        int answer = 0;
        
        if (idx == numbers.length) {
            if (curr == target) {
                answer++;
            }
        } else {
            answer += dfs(numbers, target, curr + numbers[idx], idx+1);
            answer += dfs(numbers, target, curr - numbers[idx], idx+1);
        }
        
        return answer;
    }
}
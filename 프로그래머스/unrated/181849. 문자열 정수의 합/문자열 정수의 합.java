class Solution {
    public int solution(String num_str) {
        int answer = 0;
        String[] nums = num_str.split("");
        for (int i = 0; i < nums.length; i++) {
            answer += Integer.parseInt(nums[i]);
        }
        return answer;
    }
}
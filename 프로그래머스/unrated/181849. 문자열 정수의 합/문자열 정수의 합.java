class Solution {
    public int solution(String num_str) {
        int answer = 0;
        String[] nums = num_str.split("");
        for (String s: nums) {
            answer += Integer.parseInt(s);
        }
        // answer = num_str.chars().map(c -> c - 48).sum();
        return answer;
    }
}
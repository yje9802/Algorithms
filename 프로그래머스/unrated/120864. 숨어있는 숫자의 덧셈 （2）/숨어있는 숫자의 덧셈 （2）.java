class Solution {
    public int solution(String my_string) {
        int answer = 0;
        String[] nums = my_string.split("[a-zA-Z]");
        for (String s: nums) {
            if (!s.equals("")) {
                answer += Integer.parseInt(s);
            }
        }
        return answer;
    }
}
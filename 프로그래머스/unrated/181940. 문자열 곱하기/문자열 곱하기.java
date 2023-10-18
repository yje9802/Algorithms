class Solution {
    public String solution(String my_string, int k) {
        String answer = "";
        if (my_string.length() >= 1 && my_string.length() <= 100) {
            for (int i = 0; i < k; i++) {
                answer += my_string;
            }
        }
        return answer;
    }
}
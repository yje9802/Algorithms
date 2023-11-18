class Solution {
    public String solution(String n_str) {
        String answer = n_str;
        for (int i = 0; i < n_str.length(); i++) {
            if (n_str.charAt(i) == '0') {
                answer = answer.substring(1);
            } else {
                break;
            }
        }
        return answer;
    }
}
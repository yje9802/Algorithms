class Solution {
    public int solution(String myString, String pat) {
        int answer = 0;
        int p_length = pat.length();
        for (int i = 0; i < myString.length() - p_length + 1; i++) {
            String temp = myString.substring(i, i + p_length);
            if (pat.equals(temp)) {
                answer += 1;
            }
        }
        return answer;
    }
}
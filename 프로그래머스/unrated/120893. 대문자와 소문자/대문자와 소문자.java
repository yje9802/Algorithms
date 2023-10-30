class Solution {
    public String solution(String my_string) {
        String answer = "";
        int num_s = 0;
        
        for (int i = 0; i < my_string.length(); i++) {
            char s = my_string.charAt(i);
            if ((int) s >= 65 && (int) s <= 90) {
                num_s = (int) s + 32;
                answer += (char) num_s;
            } else {
                num_s = (int) s - 32;
                answer += (char) num_s;
            }
        }
        return answer;
    }
}
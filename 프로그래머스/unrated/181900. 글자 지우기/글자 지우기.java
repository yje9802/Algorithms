class Solution {
    public String solution(String my_string, int[] indices) {
        String answer = "";
        String[] temp = my_string.split("");
        for (int i: indices) {
            temp[i] = "";
        }
        for (String s: temp) {
            answer += s;
        }
        return answer;
    }
}
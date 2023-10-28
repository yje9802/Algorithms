class Solution {
    public int solution(String my_string) {
        int answer = 0;
        my_string = my_string.replaceAll("[a-zA-z]", "");
        String[] my_strings = my_string.split("");
        for (int i = 0; i < my_strings.length; i++) {
            answer += Integer.parseInt(my_strings[i]);
        }
        return answer;
    }
}
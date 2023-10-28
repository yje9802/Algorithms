class Solution {
    public String solution(String my_string) {
        String answer = "";
        String[] vowel = {"a", "e", "i", "o", "u"};
        for (int i = 0; i < vowel.length; i++) {
            answer = my_string.replaceAll(vowel[i], "");
            my_string = answer;
        }
        return answer;
    }
}
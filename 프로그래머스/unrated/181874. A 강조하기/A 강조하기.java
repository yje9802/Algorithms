class Solution {
    public String solution(String myString) {
        String answer = "";
        myString = myString.toLowerCase();
        myString = myString.replace("a", "A");
        answer += myString;
        return answer;
    }
}
class Solution {
    public String solution(String myString, String pat) {
        String answer = "";
        
        for (int i = 0; i < myString.length(); i++) {
            String temp = myString.substring(0, i + 1);
            if (temp.endsWith(pat)) {
                answer = temp;
            }
        }
        return answer;
    }
}
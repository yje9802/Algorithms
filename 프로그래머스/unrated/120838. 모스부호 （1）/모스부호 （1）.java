class Solution {
    public String solution(String letter) {
        String answer = "";
        String[] morse = {".-","-...","-.-.","-..",".","..-.",
            "--.","....","..",".---","-.-",".-..",
            "--","-.","---",".--.","--.-",".-.",
            "...","-","..-","...-",".--","-..-",
            "-.--","--.."};
        String[] message = letter.split(" ");
        for (String m: message) {
            for (int i = 0; i < morse.length; i++) {
                if (m.equals(morse[i])) {
                    answer += Character.toString(i + (int)'a');
                }
            }
        }
        return answer;
    }
}
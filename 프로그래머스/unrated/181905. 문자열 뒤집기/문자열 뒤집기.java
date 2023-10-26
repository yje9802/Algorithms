class Solution {
    public String solution(String my_string, int s, int e) {
        String answer = "";
        char[] reversed = new char[e-s+1];
        if (s == e) {
            answer = my_string;
        } else {
            for (int i = 0; i < reversed.length / 2; i++) {
                reversed[i] = my_string.charAt(e-i);
                reversed[e-s-i] = my_string.charAt(s+i);
            }
            if (reversed.length % 2 == 1) {
                reversed[reversed.length / 2] = my_string.charAt((e+s)/2);
            }
            String reverse = new String(reversed);
            answer = my_string.substring(0, s) + reverse + my_string.substring(e+1);
        }
        return answer;
    }
}
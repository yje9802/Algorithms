class Solution {
    public String solution(String polynomial) {
        String answer = "";
        String[] poly = polynomial.split(" +");
        
        int x_num = 0;
        int num = 0;
        for (String s: poly) {
            if (s.equals("x")) {
                x_num += 1;
            } else if (s.contains("x")) {
                x_num += Integer.parseInt(s.substring(0, s.length() - 1));
            } else if (!s.equals("+")) {
                num += Integer.parseInt(s);
            }
        }
        if (x_num != 0 && num == 0) {
            if (x_num == 1) {
                answer = "x";
            } else {
                answer = x_num + "x";
            }
        } 
        if (x_num != 0 && num != 0) {
            if (x_num == 1) {
                answer = "x" + " + " + num;
            } else {
                answer = x_num + "x" + " + " + num;
            }
        }

        if (x_num == 0 && num != 0) {
            answer = String.valueOf(num);
        }
        return answer;
    }
}
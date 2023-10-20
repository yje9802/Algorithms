class Solution {
    public String solution(String code) {
        String answer = "";
        
        int idx = 0;
        int mode = 0;
        String ret = "";
        while (idx < code.length()) {
            if (code.charAt(idx) == '1') {
                mode = mode == 1 ? 0 : 1;
            } else {
                if (mode == 0) {
                    if (idx % 2 == 0) {
                        ret += code.charAt(idx);
                    }
                } else {
                    if (idx % 2 == 1) {
                        ret += code.charAt(idx);
                    }
                }
            }
            idx++;
        }
        if (ret.length() == 0) {
           answer = "EMPTY"; 
        } else {
            answer = ret;
        }
        
        return answer;
    }
}
import java.util.Arrays;

class Solution {
    public String solution(String s) {
        String answer = "";
        String[] ss = s.split("");
        Arrays.sort(ss);
        
        int count = 0;
        for (int i = 0; i < ss.length; i++) {
            count = 0;
            for (int j = 0; j < ss.length; j++) {
                if (ss[i].equals(ss[j])) {
                    count++;
                } 
            }
            if (count == 1) {
                answer += ss[i];
            }
        }
        
        return answer;
    }
}
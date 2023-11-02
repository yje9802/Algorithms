import java.util.*;

class Solution {
    public String[] solution(String myString) {
        String[] ss = myString.split("x");
        
        List<String> lanswer = new ArrayList<>();
        
        for (int i = 0; i < ss.length; i++) {
            if (!ss[i].isEmpty()) {
                lanswer.add(ss[i]);
            }
        }
        String[] answer = lanswer.toArray(new String[lanswer.size()]);
        Arrays.sort(answer);
        
        return answer;
    }
}
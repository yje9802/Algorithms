import java.util.*;

class Solution {
    public String[] solution(String myStr) {
        String[] temp = myStr.split("[abc]");
        List<String> list = new ArrayList<>();
        for (String s: temp) {
            if (!s.equals("")) {
                list.add(s);
            }
        }
        
        String[] answer;
        if (list.size() == 0) {
            answer = new String[] {"EMPTY"};
        } else {
            answer = list.toArray(new String[list.size()]);
        }
        
        return answer;
    }
}
import java.util.*;

class Solution {
    public String[] solution(String[] strArr) {
        List<String> not_ad = new ArrayList<>();
        
        for (String s: strArr) {
            if (!s.contains("ad")) {
                not_ad.add(s);
            }
        }
        String[] answer = not_ad.toArray(new String[not_ad.size()]);
        
        return answer;
    }
}
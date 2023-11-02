import java.util.Arrays;

class Solution {
    public String solution(String my_string) {
        String answer = "";
        // my_string = my_string.toLowerCase();
        String[] to_sort = my_string.toLowerCase().split("");
        Arrays.sort(to_sort);
        
        for (String s: to_sort) {
            answer += s;
        }
        return answer;
    }
}
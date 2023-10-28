import java.util.Arrays;

class Solution {
    public int[] solution(String my_string) {
        my_string = my_string.replaceAll("[a-z]", "");
        String[] my_strings = my_string.split("");
        Arrays.sort(my_strings);
        int[] answer = Arrays.stream(my_strings).mapToInt(Integer::parseInt).toArray();;
        return answer;
    }
}
class Solution {
    public String solution(String my_string, int[][] queries) {
        String answer;
        char[] arr = my_string.toCharArray();
        for (int[] query: queries) {
            for (int i = query[0]; i <= (query[1] + query[0])/2; i++) {
                char temp = arr[i];
                arr[i] = arr[query[1] + query[0] - i];
                arr[query[1] + query[0] - i] = temp;
            }
        }
        answer = new String(arr);
        return answer;
    }
}
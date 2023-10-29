class Solution {
    public int[] solution(int[] num_list, int n) {
        String temp = "";
        for (int i = 0; i < num_list.length; i += n) {
            temp += num_list[i];
        }
        int[] answer = new int[temp.length()];
        for (int j = 0; j < temp.length(); j++) {
            answer[j] = (int)temp.charAt(j) - '0';
        }
        return answer;
    }
}
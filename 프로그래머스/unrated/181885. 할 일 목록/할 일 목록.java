class Solution {
    public String[] solution(String[] todo_list, boolean[] finished) {
        String[] answer;
        String not_finished = "";
        for (int i = 0; i < finished.length; i++) {
            if (!finished[i]) {
                not_finished += todo_list[i] + ",";
            }
        }
        answer = not_finished.split(",");
        return answer;
    }
}
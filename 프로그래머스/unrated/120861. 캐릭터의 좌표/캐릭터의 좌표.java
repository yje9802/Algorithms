class Solution {
    public int[] solution(String[] keyinput, int[] board) {
        int[] answer = new int[2];
        int w_limit = board[0] / 2;
        int h_limit = board[1] / 2;
        
        for (String s: keyinput) {
            if ("left".equals(s)) {
                answer[0] += -1;
                if (Math.abs(answer[0]) > w_limit) {
                    answer[0] = 0 - w_limit;
                }
            } else if ("right".equals(s)) {
                answer[0] += 1;
                if (Math.abs(answer[0]) > w_limit) {
                    answer[0] = w_limit;
                }
            } else if ("up".equals(s)) {
                answer[1] += 1;
                if (Math.abs(answer[1]) > h_limit) {
                    answer[1] = h_limit;
                }
            } else {
                answer[1] += -1;
                if (Math.abs(answer[1]) > h_limit) {
                    answer[1] = 0 - h_limit;
                }
            }
        }
        
        return answer;
    }
}
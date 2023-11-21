class Solution {
    public String[] solution(String[] picture, int k) {
        String[] answer = new String[picture.length * k];
        for (int i = 0; i < answer.length; i+=k) {
            String rep_x = "x";
            String rep_d = ".";
            for (int s = 1; s < k; s++) {
                rep_x += "x";
                rep_d += ".";
            }
            for (int j = 0; j < k; j++) {
                if (i == 0) {
                    answer[i+j] = picture[i].replace("x", rep_x);
                } else {
                    answer[i+j] = picture[i/k].replace("x", rep_x);
                }
                answer[i+j] = answer[i+j].replace(".",rep_d);
            }
        }
        return answer;
    }
}
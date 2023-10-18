class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        String result_1 = a + "" + b;
        String result_2 = b + "" + a;
        if (Integer.parseInt(result_1) > Integer.parseInt(result_2)) {
            answer = Integer.parseInt(result_1);
        } else {
            answer = Integer.parseInt(result_2);
        }
        return answer;
    }
}
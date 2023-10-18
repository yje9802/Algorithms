class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        int result_1 = Integer.parseInt(""+a+b);
        int result_2 = 2 * a * b;
        if (result_1 > result_2) {
            answer = result_1;
        } else {
            answer = result_2;
        }
        return answer;
    }
}
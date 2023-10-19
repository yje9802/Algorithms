class Solution {
    public int solution(int n) {
        int answer = 0;
        if (n % 2 == 0) {
            for (int i = 1; i < n/2 + 1; i++) {
                answer += Math.pow((2*i), 2);
            }
        } else {
            for (int i = 0; i < n/2 + 1; i++) {
                answer += 2 * i + 1;
            }
        }
        return answer;
    }
}
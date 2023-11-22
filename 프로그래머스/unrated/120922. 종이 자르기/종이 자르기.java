class Solution {
    public int solution(int M, int N) {
        int answer = 0;
        if (M == N && M == 1) {
            return answer;
        }
        answer = (M-1) + M*(N-1);
        return answer;
    }
}
class Solution {
    public int solution(int n) {
        int answer = 0;
        
        if (n < 4) {
            answer = 0;
        } else {
            for (int i = 4; i <= n; i++) {
                int count = 0;
                for (int j = 1; j <= i; j++) {
                    if (i % j == 0) {
                        count++;
                    }
                }
                if (count >= 3) {
                    answer++;
                }
            }
        }
        return answer;
    }
}